# gossipsub

138 ideas: 27 not, 17 partial, 62 implemented, 32 n/a; 13 actionable (high or medium value, verdict `not` or `partial`). [Back to the summary](../README.md).

| id | idea | verdict | value | effort | resources |
|---|---|---|---|---|---|
| [gossipsub-001](#gossipsub-001) | Gossipsub IDONTWANT for received large messages | implemented | medium | S | bandwidth |
| [gossipsub-002](#gossipsub-002) **★** | Send IDONTWANT after publishing own messages | not | medium | S | bandwidth |
| [gossipsub-003](#gossipsub-003) | Size threshold for sending IDONTWANT | implemented | low | S | bandwidth |
| [gossipsub-004](#gossipsub-004) | Time-based O(1) gossip duplicate cache | implemented | low | S | cpu, latency |
| [gossipsub-005](#gossipsub-005) | QUIC transport alongside TCP | implemented | low | S | latency, bandwidth, cpu |
| [gossipsub-006](#gossipsub-006) **★** | Coded-chunk block broadcast (RLNC or erasure coding) | not | medium | L | latency, bandwidth |
| [gossipsub-007](#gossipsub-007) | Use the fastest snappy codec for gossip and RPC | partial | low | S | cpu, latency |
| [gossipsub-008](#gossipsub-008) | Close RPC streams asynchronously | implemented | low | S | latency |
| [gossipsub-009](#gossipsub-009) **★** | Encode gossip message once and share bytes | not | medium | M | cpu, memory, latency |
| [gossipsub-010](#gossipsub-010) | No broadcast to self; reply to single peer | n/a | low |  | bandwidth |
| [gossipsub-011](#gossipsub-011) | Do not republish gossip the library already forwards | implemented | low | S | bandwidth, cpu |
| [gossipsub-012](#gossipsub-012) | Drain gossip control events locally, not via queue | n/a | low |  | cpu, latency |
| [gossipsub-013](#gossipsub-013) | Compute fork digest once and cache it | implemented | low | S | cpu |
| [gossipsub-014](#gossipsub-014) | Build topic strings and message ids without copies | partial | low | S | cpu, memory |
| [gossipsub-015](#gossipsub-015) | Backpressure gossipsub RPC processing per packet | n/a | low |  | cpu, memory |
| [gossipsub-016](#gossipsub-016) | Bandwidth-based per-peer rate limiter | not | low | M | bandwidth, cpu |
| [gossipsub-017](#gossipsub-017) | Bitvector for permanent subnet subscriptions | not | low | S | memory |
| [gossipsub-018](#gossipsub-018) | Bound buffered gossip awaiting unknown block | implemented | medium | S | memory |
| [gossipsub-019](#gossipsub-019) | Bound per-connection QUIC and stream resources | partial | low | S | memory |
| [gossipsub-020](#gossipsub-020) | Size limit on gossip seen-message cache | not | low | S | memory |
| [gossipsub-021](#gossipsub-021) | Bound gossipsub RPC decode before unmarshalling | implemented | medium | S | memory |
| [gossipsub-022](#gossipsub-022) | Bounded per-connection gossipsub send queue | implemented | low | S | memory |
| [gossipsub-023](#gossipsub-023) | Limit light client update broadcasts | partial | low | S | bandwidth |
| [gossipsub-024](#gossipsub-024) | Upgrade QUIC library for throughput and CPU | implemented | low | S | cpu, memory, bandwidth |
| [gossipsub-025](#gossipsub-025) | Compute gossip message id once and store it | implemented | low | S | cpu, memory |
| [gossipsub-026](#gossipsub-026) | Cache gossip topic name string | not | low | S | cpu |
| [gossipsub-027](#gossipsub-027) | Direct callbacks between gossipsub and processor | n/a | low | S | cpu, latency |
| [gossipsub-028](#gossipsub-028) | Gossip data columns as partial cell messages | implemented | high | M | bandwidth, latency |
| [gossipsub-029](#gossipsub-029) | Compact fixed-size keys in gossip seen caches | not | low | M | cpu, memory |
| [gossipsub-030](#gossipsub-030) **★** | Reject oversized gossip by snappy header before decompress | partial | medium | S | cpu, memory |
| [gossipsub-031](#gossipsub-031) | Compute identical subnet score params once | implemented | low | S | cpu |
| [gossipsub-032](#gossipsub-032) | Publish light client updates concurrently | n/a | low | S | latency |
| [gossipsub-033](#gossipsub-033) | Concurrent map for topic subscriptions | n/a | low | S | cpu |
| [gossipsub-034](#gossipsub-034) | Dedupe by message id inside gossipsub | implemented | low | S | cpu, bandwidth |
| [gossipsub-035](#gossipsub-035) | Fast message id on raw bytes before decompress | not | low | M | cpu |
| [gossipsub-036](#gossipsub-036) | Fast non-cryptographic hash for gossip fast message id | not | low | S | cpu |
| [gossipsub-037](#gossipsub-037) | Decompress gossip payload once and share it | implemented | medium | S | cpu, memory |
| [gossipsub-038](#gossipsub-038) | Decode gossip off the gossipsub event thread | partial | low | M | cpu, latency |
| [gossipsub-039](#gossipsub-039) | Run libp2p networking on its own thread | partial | low | M | latency, cpu |
| [gossipsub-040](#gossipsub-040) | Node-id derived long-lived attestation subnets | implemented | low | S | bandwidth, cpu |
| [gossipsub-041](#gossipsub-041) | Move state dumps after fork choice update | n/a | low | S | disk, latency |
| [gossipsub-042](#gossipsub-042) **★** | Gate gossip subscriptions on sync state | partial | medium | S | cpu, bandwidth, memory, sync |
| [gossipsub-043](#gossipsub-043) | Keep libp2p/gossipsub dependencies on fixed, fast versions | implemented | medium | S | memory, cpu, latency, bandwidth |
| [gossipsub-044](#gossipsub-044) | Faster multistream handshake dependency | n/a | low | S | cpu, latency |
| [gossipsub-045](#gossipsub-045) | Disable gossipsub PRUNE peer exchange | implemented | low | S | bandwidth, cpu |
| [gossipsub-046](#gossipsub-046) | Disable unused TLS secure channel | implemented | low | S | cpu |
| [gossipsub-047](#gossipsub-047) | Disable gossipsub flood publish | implemented | medium | S | bandwidth, latency |
| [gossipsub-048](#gossipsub-048) | Disable gossipsub self-delivery of own messages | n/a | low | S | cpu |
| [gossipsub-049](#gossipsub-049) | Prefer yamux; disable mplex by default | partial | low | S | memory, cpu, bandwidth |
| [gossipsub-050](#gossipsub-050) | Drop decoded gossip objects from caches after handoff | n/a | low | S | memory |
| [gossipsub-051](#gossipsub-051) | Prune or disconnect peers whose send queue stays full | implemented | medium | S | memory, bandwidth, cpu |
| [gossipsub-052](#gossipsub-052) | Discard timed-out queued messages on poll | not | low | S | memory, latency |
| [gossipsub-053](#gossipsub-053) | Subscribe only to topics valid for current fork | implemented | low | S | bandwidth, cpu |
| [gossipsub-054](#gossipsub-054) | Subscribe attestation subnets only for duties | implemented | medium | S | bandwidth, cpu |
| [gossipsub-055](#gossipsub-055) | Dynamic sync committee subnet subscriptions | implemented | low | S | bandwidth, cpu |
| [gossipsub-056](#gossipsub-056) | Subscribe duty subnets one epoch early | partial | low | S | latency |
| [gossipsub-057](#gossipsub-057) | Correct subnet subscription time computation | implemented | low | S | latency |
| [gossipsub-058](#gossipsub-058) | Just-in-time short-lived duty subnet subscription | implemented | medium | S | bandwidth, cpu |
| [gossipsub-059](#gossipsub-059) | Expiring gossip topic listeners | not | low | M | cpu, bandwidth |
| [gossipsub-060](#gossipsub-060) | Wake network task on subnet service events | implemented | low | S | latency |
| [gossipsub-061](#gossipsub-061) | Publish completion signal on first send | not | low | M | latency |
| [gossipsub-062](#gossipsub-062) | One buffer allocation per gossip write | n/a | low |  | cpu, memory |
| [gossipsub-063](#gossipsub-063) | Flood publish time-critical messages | not | low | S | latency |
| [gossipsub-064](#gossipsub-064) | Forward gossip right after validation, before processing | implemented | high | S | latency |
| [gossipsub-065](#gossipsub-065) | Non-supernodes publish reconstructed custody columns | implemented | medium | S | latency, bandwidth |
| [gossipsub-066](#gossipsub-066) | Check topic subscription before decoding partial messages | not | low | S | cpu, latency |
| [gossipsub-067](#gossipsub-067) | Keep column gossip during optimistic sync | n/a | medium |  | sync, bandwidth |
| [gossipsub-068](#gossipsub-068) **★** | Cheaper gossipsub peer score computation | partial | medium | M | cpu |
| [gossipsub-069](#gossipsub-069) | Snappy-compress all gossip payloads | implemented | low | S | bandwidth |
| [gossipsub-070](#gossipsub-070) | Gossipsub topic subscription allowlist filter | implemented | medium | S | memory, cpu, bandwidth |
| [gossipsub-071](#gossipsub-071) **★** | Batch publish all sidecars of a block | partial | medium | M | latency |
| [gossipsub-072](#gossipsub-072) **★** | Lower gossipsub memory per message | not | medium | M | memory |
| [gossipsub-073](#gossipsub-073) | Larger recvmmsg/sendmmsg batches in UDP transport | n/a | low |  | cpu |
| [gossipsub-074](#gossipsub-074) | Lazy sweep of idle rate-limiter buckets | implemented | low | S | cpu, memory |
| [gossipsub-075](#gossipsub-075) | Copy native snappy output into runtime buffer | n/a | low |  | memory |
| [gossipsub-076](#gossipsub-076) **★** | Cap incoming connections and per-peer streams | partial | medium | S | memory, cpu |
| [gossipsub-077](#gossipsub-077) | Gossipsub seen-cache TTL spans attestation propagation window | implemented | medium | S | cpu, bandwidth |
| [gossipsub-078](#gossipsub-078) | Tune gossipsub mesh degree and gossip parameters | implemented | medium | S | bandwidth, cpu, memory |
| [gossipsub-079](#gossipsub-079) | Ethereum-specific per-topic gossipsub scoring parameters | partial | low | M | bandwidth, cpu |
| [gossipsub-080](#gossipsub-080) | Tune yamux flow-control window | implemented | low | S | bandwidth, memory |
| [gossipsub-081](#gossipsub-081) | Unsubscribe expired long-lived random subnets | n/a | low | S | bandwidth |
| [gossipsub-082](#gossipsub-082) | Subscribe to duty subnet only when aggregating | implemented | medium | S | bandwidth, cpu |
| [gossipsub-083](#gossipsub-083) | No subnet subscriptions without attached validators | implemented | low | S | bandwidth, cpu |
| [gossipsub-084](#gossipsub-084) | Skip subscription for already-past slots | implemented | low | S | cpu, bandwidth |
| [gossipsub-085](#gossipsub-085) | Avoid redundant topic re-subscription | implemented | low | S | cpu, bandwidth |
| [gossipsub-086](#gossipsub-086) | Request bitmap for missing partial-column cells | implemented | medium | S | bandwidth |
| [gossipsub-087](#gossipsub-087) | Proposer eagerly pushes all partial column cells | not | low | M | latency |
| [gossipsub-088](#gossipsub-088) | Send partial-column header once per peer per block | implemented | low | S | bandwidth |
| [gossipsub-089](#gossipsub-089) | Skip partial column construction when disabled | partial | low | S | cpu, memory |
| [gossipsub-090](#gossipsub-090) | Do not cache partial headers for imported blocks | implemented | low | S | cpu, memory, bandwidth |
| [gossipsub-091](#gossipsub-091) **★** | Bundle attestations via gossipsub partial messages | not | medium | L | bandwidth |
| [gossipsub-092](#gossipsub-092) | Custody all columns without all attestation subnets | implemented | medium | S | bandwidth, cpu |
| [gossipsub-093](#gossipsub-093) | Subscribe only to custody/sampling column subnets | implemented | low | S | bandwidth, cpu |
| [gossipsub-094](#gossipsub-094) | Process gossip RPC messages concurrently | n/a | low |  | latency |
| [gossipsub-095](#gossipsub-095) | Yield to the scheduler during gossip processing | n/a | low |  | latency |
| [gossipsub-096](#gossipsub-096) | Subscribe to gossip topics concurrently at startup | n/a | low |  | startup |
| [gossipsub-097](#gossipsub-097) | Send goodbye to peers concurrently on shutdown | n/a | low |  | latency |
| [gossipsub-098](#gossipsub-098) | Non-blocking gossip publish with backpressure | n/a | low |  | latency |
| [gossipsub-099](#gossipsub-099) | Asynchronous attestation subnet cycling | n/a | low |  | latency |
| [gossipsub-100](#gossipsub-100) | Synchronous topic subscribe/unsubscribe calls | n/a | low |  | cpu |
| [gossipsub-101](#gossipsub-101) | Short 8-byte gossip message ids | partial | low | S | bandwidth, memory, cpu |
| [gossipsub-102](#gossipsub-102) | Disable gossipsub message signing | implemented | low | S | cpu, bandwidth |
| [gossipsub-103](#gossipsub-103) | Optional bls_to_execution_changes topic subscription | not | low | S | bandwidth, cpu |
| [gossipsub-104](#gossipsub-104) | Per-topic bounded gossip work queues | implemented | medium | S | cpu, latency |
| [gossipsub-105](#gossipsub-105) **★** | Queue admission before decompression and message-id | not | medium | M | cpu |
| [gossipsub-106](#gossipsub-106) | Separate queue for subnet subscription messages | implemented | low | S | latency |
| [gossipsub-107](#gossipsub-107) | Native networking runtime with bounded budgets | n/a | low | L | memory, cpu, latency |
| [gossipsub-108](#gossipsub-108) | Synchronize read buffer once per read | n/a | low | L | cpu |
| [gossipsub-109](#gossipsub-109) | No zero-init for network read buffers | partial | low | S | cpu |
| [gossipsub-110](#gossipsub-110) | Plumtree epidemic broadcast gossip | not | low | L | bandwidth |
| [gossipsub-111](#gossipsub-111) | Snappy block format for gossip, framed for RPC | implemented | low | S | cpu, bandwidth |
| [gossipsub-112](#gossipsub-112) | No separate attestation announcement before gossip | n/a | low | S | bandwidth |
| [gossipsub-113](#gossipsub-113) | Rely on gossipsub dedup, drop app-level seen cache | implemented | low | S | memory, cpu |
| [gossipsub-114](#gossipsub-114) | Dispatch network events directly to processor | implemented | low | S | latency, cpu |
| [gossipsub-115](#gossipsub-115) | Timeout on incoming gossip buffer reservations | n/a | low |  | latency, memory |
| [gossipsub-116](#gossipsub-116) | Non-sequential gossip consumption and bigger socket buffers | n/a | low |  | latency |
| [gossipsub-117](#gossipsub-117) **★** | Raise OS UDP buffer limits for QUIC | not | medium | S | bandwidth, latency |
| [gossipsub-118](#gossipsub-118) | Reset libp2p streams on error and timeout | n/a | medium | S | memory |
| [gossipsub-119](#gossipsub-119) | Strict read/write timeouts on req/resp handlers | implemented | low | S | memory |
| [gossipsub-120](#gossipsub-120) **★** | Interleave column sidecar publish across columns | not | medium | M | latency, bandwidth |
| [gossipsub-121](#gossipsub-121) | Drive the swarm with an async select loop | implemented | low | S | cpu, latency |
| [gossipsub-122](#gossipsub-122) | Runtime-native timer for gossipsub heartbeat | not | low | S | cpu, latency |
| [gossipsub-123](#gossipsub-123) | Fastest AEAD/hash backend for noise transport | implemented | low | S | cpu |
| [gossipsub-124](#gossipsub-124) | No gossip validation or relay before genesis | not | low | S | cpu |
| [gossipsub-125](#gossipsub-125) | Reject undecompressable gossip before id and caching | implemented | low | S | cpu, memory |
| [gossipsub-126](#gossipsub-126) | Drop self-originated gossip before validation | implemented | low | S | cpu |
| [gossipsub-127](#gossipsub-127) | Do not regossip RPC-reconstructed columns | implemented | low | S | bandwidth |
| [gossipsub-128](#gossipsub-128) | Zero-copy byte handling in message-id computation | not | low | S | cpu, memory |
| [gossipsub-129](#gossipsub-129) | Parse fork digest from topic without allocation | not | low | S | cpu, memory |
| [gossipsub-130](#gossipsub-130) | Subscribe to next-fork topics just before the fork | implemented | low | S | bandwidth, cpu |
| [gossipsub-131](#gossipsub-131) | Transfer gossip buffers between threads without copy | n/a | low | S | memory, cpu |
| [gossipsub-132](#gossipsub-132) | Queue unknown-block attestations on the network thread | n/a | low | S | latency, cpu |
| [gossipsub-133](#gossipsub-133) | Cache attached validators to derive subnet subscriptions | implemented | low | S | cpu, bandwidth |
| [gossipsub-134](#gossipsub-134) | Parse gossip topics cheaply without regex or exceptions | implemented | low | S | cpu |
| [gossipsub-135](#gossipsub-135) | Gossip-only block body without unneeded fields | n/a | low |  | bandwidth |
| [gossipsub-136](#gossipsub-136) | One random long-lived subnet per attached validator | n/a | low |  | bandwidth |
| [gossipsub-137](#gossipsub-137) | Publish column sidecars only when self-building | implemented | low | S | bandwidth |
| [gossipsub-138](#gossipsub-138) | Enforce peer bans in the swarm layer | implemented | low | S | cpu, bandwidth |

★ actionable. Click an id for the full record.

## Ideas

<a id="gossipsub-001"></a>
<details>
<summary><b>gossipsub-001</b> Gossipsub IDONTWANT for received large messages — <i>implemented · medium · S · bandwidth</i></summary>

**Idea.** On receiving a large gossip message, send IDONTWANT to mesh peers and skip forwarding it to peers that sent IDONTWANT for it. Cuts duplicate transfers of blocks, blobs and columns.

**Impact.** Duplicate transfers of large gossip messages are already cut.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/config.rs:24`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/config.rs#L24) DEFAULT_IDONTWANT_MESSAGE_SIZE_THRESHOLD=1000
- ~/.cargo/git/checkouts/rust-libp2p-b7fa834aec8fc27c/accba72/protocols/gossipsub/src/behaviour.rs:1953-1976 IDONTWANT sent to mesh peers and promise peers when a large message is received
- ~/.cargo/git/checkouts/rust-libp2p-b7fa834aec8fc27c/accba72/protocols/gossipsub/src/behaviour.rs:3007 forward skips peers in dont_send
- ~/.cargo/git/checkouts/rust-libp2p-b7fa834aec8fc27c/accba72/protocols/gossipsub/src/behaviour.rs:3620-3635 received IDONTWANT also removes queued messages
- ~/.cargo/git/checkouts/rust-libp2p-b7fa834aec8fc27c/accba72/protocols/gossipsub/src/behaviour.rs:1495 IWANT replies also respect dont_send

**Skeptic check.** Checked that Cargo.lock pins the sigp fork at accba72 and that the fork sends IDONTWANT on receipt and publish, skips dont_send peers on forward and IWANT, and drops already-queued sends. Earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#5422](https://github.com/sigp/lighthouse/pull/5422), [silver#9](https://github.com/gattaca-com/silver/pull/9), [lodestar#7359](https://github.com/ChainSafe/lodestar/pull/7359), [prysm#14428](https://github.com/OffchainLabs/prysm/pull/14428), [teku#8648](https://github.com/Consensys-Incorporated/teku/pull/8648)

</details>


<a id="gossipsub-002"></a>
<details>
<summary><b>gossipsub-002</b> Send IDONTWANT after publishing own messages — <i>not · medium · S · bandwidth</i></summary>

**Idea.** After publishing a message the node already has (own block, columns or blobs from the EL), send IDONTWANT to mesh peers so they do not send it back. Saves inbound duplicate bytes.

**Gap in Lighthouse.** PR #6513 put IDONTWANT-on-publish into the old vendored gossipsub. After the move to the sigp/rust-libp2p fork it is behind a config flag that Lighthouse does not set. Add .idontwant_on_publish(true) to gossipsub_config in lighthouse_network/src/config.rs (this is open PR #8364).

**Impact.** Stops mesh peers from sending back large messages the node published itself (blobs or columns from getBlobs, own blocks). The gain is modest inbound bandwidth.

**Evidence (Lighthouse @ 928b61e719).**

- accba72/protocols/gossipsub/src/behaviour.rs:711-724 publish sends IDONTWANT only when config.idontwant_on_publish() is true
- accba72/protocols/gossipsub/src/config.rs:560 idontwant_on_publish default false
- accba72/protocols/gossipsub/src/behaviour.rs:1952-1976 the only other IDONTWANT send is on receipt of a forwarded message, not on own publish
- [`beacon_node/lighthouse_network/src/config.rs:509-531`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/config.rs#L509-L531) gossipsub_config builder sets idontwant_message_size_threshold but never idontwant_on_publish
- [`beacon_node/lighthouse_network/src/service/mod.rs:248-255`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/mod.rs#L248-L255) the only gossipsub config construction site

**Second check.** The prescreen said this was in LH because of the merged PR #6513, but that code was in the vendored crate that has been removed. I grepped beacon_node for every IDONTWANT config use and checked both IDONTWANT send sites in the pinned fork (accba72). Nothing turns the flag on.

**Verdict history.** not (checked) → not (refuted)

**Sources.** [lighthouse#6513](https://github.com/sigp/lighthouse/pull/6513), [lighthouse#8364](https://github.com/sigp/lighthouse/pull/8364), [lodestar#8324](https://github.com/ChainSafe/lodestar/pull/8324)

</details>


<a id="gossipsub-003"></a>
<details>
<summary><b>gossipsub-003</b> Size threshold for sending IDONTWANT — <i>implemented · low · S · bandwidth</i></summary>

**Idea.** Send IDONTWANT only for messages above a size threshold, since for small messages such as single attestations the control message costs about as much as the payload it saves.

**Impact.** IDONTWANT is not sent for single attestations or other small messages.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/config.rs:24`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/config.rs#L24) DEFAULT_IDONTWANT_MESSAGE_SIZE_THRESHOLD=1000
- [`beacon_node/lighthouse_network/src/config.rs:529`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/config.rs#L529) passed to gossipsub config builder
- ~/.cargo/git/checkouts/rust-libp2p-b7fa834aec8fc27c/accba72/protocols/gossipsub/src/behaviour.rs:713 and :1953 IDONTWANT only if raw_protobuf_len() &gt; threshold

**Skeptic check.** The threshold is applied at both IDONTWANT send sites in the sigp gossipsub fork pinned in Cargo.lock. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#6456](https://github.com/sigp/lighthouse/pull/6456), [silver#392](https://github.com/gattaca-com/silver/pull/392)

</details>


<a id="gossipsub-004"></a>
<details>
<summary><b>gossipsub-004</b> Time-based O(1) gossip duplicate cache — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Keep the gossipsub seen-message cache as a time-based structure with O(1) insert and expiry inside the gossipsub layer, not an LRU with O(N) updates per message, so duplicate checks do not block network threads.

**Impact.** Already done.

**Best measured result.** pr:lighthouse#1490: fixed high CPU, nodes not following head, HTTP delays; no numbers

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/git/checkouts/rust-libp2p-b7fa834aec8fc27c/accba72/protocols/gossipsub/src/time_cache.rs:44 TimeCache hash map plus expiry-ordered list
- ~/.cargo/git/checkouts/rust-libp2p-b7fa834aec8fc27c/accba72/protocols/gossipsub/src/time_cache.rs:124-135 remove_expired_keys pops only expired front entries
- ~/.cargo/git/checkouts/rust-libp2p-b7fa834aec8fc27c/accba72/protocols/gossipsub/src/time_cache.rs:169-195 DuplicateCache insert/contains
- [`beacon_node/lighthouse_network/src/config.rs:495`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/config.rs#L495) duplicate_cache_time

**Skeptic check.** The duplicate cache in the locked gossipsub fork is a time-based hash map with amortized O(1) insert and expiry, not an LRU. This is the result of the cited Lighthouse PRs. Earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#1490](https://github.com/sigp/lighthouse/pull/1490), [lighthouse#1400](https://github.com/sigp/lighthouse/pull/1400)

</details>


<a id="gossipsub-005"></a>
<details>
<summary><b>gossipsub-005</b> QUIC transport alongside TCP — <i>implemented · low · S · latency, bandwidth, cpu</i></summary>

**Idea.** Offer a QUIC transport next to TCP and dial QUIC when the peer advertises it. QUIC has built-in encryption and multiplexing and fewer handshake round trips than TCP+Noise+mux.

**Impact.** QUIC is on by default and is dialed first when the peer advertises it.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/service/utils.rs:70-76`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/utils.rs#L70-L76) QUIC transport or'd with TCP
- [`beacon_node/lighthouse_network/src/config.rs:365`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/config.rs#L365) disable_quic_support defaults false
- [`beacon_node/lighthouse_network/src/peer_manager/mod.rs:479-486`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/mod.rs#L479-L486) dial list puts ENR QUIC multiaddrs before TCP

**Skeptic check.** Confirmed the transport and the dial order: dialable_multiaddrs_quic comes before tcp. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#4577](https://github.com/sigp/lighthouse/pull/4577), [lodestar#8051](https://github.com/ChainSafe/lodestar/pull/8051)

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

**Verdict history.** not (checked) → not (refuted)

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
<summary><b>gossipsub-008</b> Close RPC streams asynchronously — <i>implemented · low · S · latency</i></summary>

**Idea.** Close req/resp streams with close-write plus reset, without waiting for the remote EOF on each request, so per-request latency does not include the close handshake.

**Impact.** Request latency does not include a wait for the remote side to close.

**Best measured result.** pr:prysm#8015: maybe latency improvements; no numbers

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/rpc/handler.rs:686-735`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/handler.rs#L686-L735) the last response moves the stream to Closing and is returned to the behaviour at once
- [`beacon_node/lighthouse_network/src/rpc/handler.rs:786-815`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/handler.rs#L786-L815) Closing is polled with Sink::poll_close, a half-close that does not wait for the remote EOF
- [`beacon_node/lighthouse_network/src/rpc/handler.rs:1154-1164`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/handler.rs#L1154-L1164) inbound side closes after the response has been sent

**Skeptic check.** The response is delivered before the close. Rust poll_close only half-closes the write side, which is the behaviour the prysm PR moved to; it does not wait for the remote EOF as go-libp2p's old full close did. For multi-chunk streams that hit the expected count, EndOfStream is sent after poll_close, but that is only a local FIN. Earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

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

**Verdict history.** not (checked) → not (refuted)

**Sources.** [nimbus#3830](https://github.com/status-im/nimbus-eth2/pull/3830), [nimbus#6280](https://github.com/status-im/nimbus-eth2/pull/6280), [lodestar#6597](https://github.com/ChainSafe/lodestar/pull/6597), [nimbus@6d4470a8c](https://github.com/status-im/nimbus-eth2/commit/6d4470a8c8b8), [silver#247](https://github.com/gattaca-com/silver/pull/247), [silver#202](https://github.com/gattaca-com/silver/pull/202)

</details>


<a id="gossipsub-010"></a>
<details>
<summary><b>gossipsub-010</b> No broadcast to self; reply to single peer — <i>n/a · low · bandwidth</i></summary>

**Idea.** Do not broadcast messages back to the local node, and answer a single peer's request directly instead of broadcasting the response to all peers.

**Impact.** rust-libp2p does not self-deliver and LH answers requests over req/resp.

**Evidence (Lighthouse @ 928b61e719).**

- accba72/protocols/gossipsub/src/behaviour.rs:707 publish does not loop back to self; replies use req/resp to a single peer

**Sources.** [prysm#1931](https://github.com/OffchainLabs/prysm/pull/1931)

</details>


<a id="gossipsub-011"></a>
<details>
<summary><b>gossipsub-011</b> Do not republish gossip the library already forwards — <i>implemented · low · S · bandwidth, cpu</i></summary>

**Idea.** For messages received from the network (for example attestations), do not re-serialize and republish them at the application level or again from the op pool path; let gossipsub forward and dedupe them, and publish only locally created messages once. Removes duplicate gossip and serialization work.

**Impact.** There is no duplicate application-level republish to remove.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/service.rs:661`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/service.rs#L661) received gossip is forwarded by gossipsub through report_message_validation_result
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1352-1366`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1352-L1366) only full columns completed from partials are published
- [`beacon_node/network/src/network_beacon_processor/mod.rs:1275`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/mod.rs#L1275) only reconstructed columns are published
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:940-990`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L940-L990) received full columns are sent as partial messages, which is a different protocol and not a duplicate

**Skeptic check.** A grep over network_beacon_processor finds no Publish of received attestations, blocks or columns, only of locally completed or reconstructed columns. Earlier evidence is correct, except that the cited reconstruction lines are at gossip_methods.rs:1352 and mod.rs:1275.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [caplin#13314](https://github.com/erigontech/erigon/pull/13314), [teku#5129](https://github.com/Consensys-Incorporated/teku/pull/5129), [prysm#2509](https://github.com/OffchainLabs/prysm/pull/2509)

</details>


<a id="gossipsub-012"></a>
<details>
<summary><b>gossipsub-012</b> Drain gossip control events locally, not via queue — <i>n/a · low · cpu, latency</i></summary>

**Idea.** Buffer control events inside the gossip handler and pass them straight to the peer manager instead of publishing to a queue that the same component consumes.

**Impact.** Event plumbing differs; any saving would be micro.

**Evidence (Lighthouse @ 928b61e719).**

- lighthouse_network/src/service/mod.rs: gossipsub events flow through the libp2p Swarm; no self-consumed queue found

**Sources.** [silver#142](https://github.com/gattaca-com/silver/pull/142)

</details>


<a id="gossipsub-013"></a>
<details>
<summary><b>gossipsub-013</b> Compute fork digest once and cache it — <i>implemented · low · S · cpu</i></summary>

**Idea.** Compute the fork digest once per fork and pass or cache it for gossip topics and req/resp, instead of recomputing it per message or per subnet subscription.

**Impact.** Gossip topics and RPC context bytes use cached digests.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/fork/fork_context.rs:58`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/fork/fork_context.rs#L58) digests precomputed per fork at construction
- [`consensus/types/src/fork/fork_context.rs:139-146`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/fork/fork_context.rs#L139-L146) context_bytes is a BTreeMap lookup
- [`beacon_node/lighthouse_network/src/rpc/codec.rs:473-484`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/codec.rs#L473-L484) RPC context bytes from ForkContext
- [`beacon_node/lighthouse_network/src/types/pubsub.rs:717`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/pubsub.rs#L717) gossip topics use fork_context.current_fork_digest()

**Skeptic check.** Two cold paths still recompute the digest: status_message (status.rs:22 via enr_fork_id) and light client updates-by-range (http_api/light_client.rs:159). Both run per peer status or per API chunk, so they are negligible. The hot paths are cached.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#9607](https://github.com/Consensys-Incorporated/teku/pull/9607), [lodestar#2441](https://github.com/ChainSafe/lodestar/pull/2441), [prysm#15490](https://github.com/OffchainLabs/prysm/pull/15490)

</details>


<a id="gossipsub-014"></a>
<details>
<summary><b>gossipsub-014</b> Build topic strings and message ids without copies — <i>partial · low · S · cpu, memory</i></summary>

**Idea.** Build gossip topic strings and message ids without intermediate string copies, and skip ENR updates when the syncnet bitfield did not change.

**Gap in Lighthouse.** ENR skip exists; topic strings still built with format!/to_string on each conversion. Would need caching of the topic string/TopicHash per GossipTopic in subscribe/publish paths (GossipTopic::to_string, Display).

**Impact.** Saves a few small allocations per publish/subscription; negligible.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/discovery/mod.rs:503`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/discovery/mod.rs#L503) update_enr_bitfield returns early when bit already set (attnets, same pattern for syncnets)
- [`beacon_node/lighthouse_network/src/types/topics.rs:333-360`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/topics.rs#L333-L360) GossipTopic Display builds String with format! each call

**Sources.** [nimbus#3015](https://github.com/status-im/nimbus-eth2/pull/3015)

</details>


<a id="gossipsub-015"></a>
<details>
<summary><b>gossipsub-015</b> Backpressure gossipsub RPC processing per packet — <i>n/a · low · cpu, memory</i></summary>

**Idea.** Await processing of each gossipsub RPC in the stream reader so TCP backpressure applies, instead of spawning unbounded concurrent processing that can overload the node.

**Impact.** Gossipsub RPC is processed inline in the swarm poll loop, so TCP/stream backpressure already applies; no unbounded spawn per RPC.

**Evidence (Lighthouse @ 928b61e719).**

- accba72/protocols/gossipsub/src/handler.rs:101 single inbound substream polled by handler, events handed to behaviour in swarm task (no per-RPC spawn)
- [`beacon_node/network/src/service.rs:1535`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/service.rs#L1535) forwards to beacon processor via bounded queues

**Sources.** [lodestar#4691](https://github.com/ChainSafe/lodestar/pull/4691)

</details>


<a id="gossipsub-016"></a>
<details>
<summary><b>gossipsub-016</b> Bandwidth-based per-peer rate limiter — <i>not · low · M · bandwidth, cpu</i></summary>

**Idea.** Rate-limit each peer with one limiter on actual bytes in and out, instead of separate limits per request type.

**Gap in Lighthouse.** Add a per-peer byte-based token bucket on RPC in/out in rpc/rate_limiter.rs (RPCRateLimiter) instead of per-protocol request counts; Lighthouse charges tokens by request count/blocks requested.

**Impact.** Mostly a DoS-hardening/fairness change; no clear CPU gain on a normal node.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/rpc/rate_limiter.rs:56`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/rate_limiter.rs#L56) Quota with max_tokens per protocol (request-count based)
- [`beacon_node/lighthouse_network/src/rpc/config.rs:74`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/config.rs#L74) per-protocol quotas

**Sources.** [caplin#12999](https://github.com/erigontech/erigon/pull/12999)

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
<summary><b>gossipsub-018</b> Bound buffered gossip awaiting unknown block — <i>implemented · medium · S · memory</i></summary>

**Idea.** Cap the gossip messages buffered while waiting for an unknown block (roots buffered per slot, roots searched per slot) so memory cannot grow without limit.

**Impact.** Memory is already bounded.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:84`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L84),595 attestations awaiting a block capped at 16384
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:87`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L87),867 columns awaiting a block capped at 256
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:78-81`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L78-L81),670,724,780,807 blocks and envelopes capped at 16
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:90`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L90),898 light client updates capped at 128
- [`beacon_node/network/src/sync/manager.rs:95`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/manager.rs#L95) pending unknown roots LRU 1024
- [`beacon_node/network/src/sync/block_lookups/mod.rs:77`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/block_lookups/mod.rs#L77),408 MAX_LOOKUPS=200

**Skeptic check.** Every buffer that holds gossip awaiting an unknown block has a global cap, and the searched roots are capped by the LRU and by MAX_LOOKUPS. Lodestar caps per slot instead, but that bounds memory the same way. Earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#10039](https://github.com/ChainSafe/lodestar/pull/10039)

</details>


<a id="gossipsub-019"></a>
<details>
<summary><b>gossipsub-019</b> Bound per-connection QUIC and stream resources — <i>partial · low · S · memory</i></summary>

**Idea.** Cap the QUIC receive window, disallow unused unidirectional streams and datagrams, close the previous gossip stream when a new one opens, and cap req/resp sizes at spec maxima.

**Gap in Lighthouse.** Uni streams, datagrams disabled and gossip stream replacement exist; receive windows left at libp2p defaults (15MB/10MB) and LH uses libp2p::quic::Config::new without lowering them (service/utils.rs:73). Could set max_stream_data/max_connection_data smaller.

**Impact.** Bounds worst-case per-connection memory for QUIC peers; hardening only.

**Evidence (Lighthouse @ 928b61e719).**

- accba72/transports/quic/src/config.rs:145 max_concurrent_uni_streams(0)
- accba72/transports/quic/src/config.rs:148 datagrams disabled
- accba72/transports/quic/src/config.rs:93-94 256 bidi streams, 15MB conn / 10MB stream receive windows
- accba72/protocols/gossipsub/src/handler.rs:200 new inbound substream replaces old one; attempts bounded

**Sources.** [silver#447](https://github.com/gattaca-com/silver/pull/447), [lodestar#9792](https://github.com/ChainSafe/lodestar/pull/9792)

</details>


<a id="gossipsub-020"></a>
<details>
<summary><b>gossipsub-020</b> Size limit on gossip seen-message cache — <i>not · low · S · memory</i></summary>

**Idea.** Put a hard size limit on the gossipsub seen-message cache in addition to its time expiry.

**Gap in Lighthouse.** Add a max-entries bound to TimeCache/DuplicateCache in the sigp rust-libp2p fork, evicting oldest from the list when exceeded.

**Impact.** Memory safety under message flood; cache is bounded by rate limits/validation in practice so little gain.

**Evidence (Lighthouse @ 928b61e719).**

- accba72/protocols/gossipsub/src/time_cache.rs:44 TimeCache is time-expiry only (map+VecDeque), no size cap
- [`beacon_node/lighthouse_network/src/config.rs:507`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/config.rs#L507) duplicate_cache_time = 2 epochs

**Sources.** [teku#11445](https://github.com/Consensys-Incorporated/teku/pull/11445)

</details>


<a id="gossipsub-021"></a>
<details>
<summary><b>gossipsub-021</b> Bound gossipsub RPC decode before unmarshalling — <i>implemented · medium · S · memory</i></summary>

**Idea.** Reject gossipsub RPCs above a size cap and set finite decode limits on subscriptions, messages, IHAVE/IWANT/IDONTWANT ids and PX peers before decoding, so crafted control messages cannot force large allocations.

**Impact.** Pre-decode caps on total RPC size, publish count and aggregate control bytes bound the allocation from crafted RPCs.

**Best measured result.** pr:caplin#24616: unbounded allocation; short burst OOM-kills

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/git/checkouts/rust-libp2p-b7fa834aec8fc27c/accba72/protocols/gossipsub/src/protocol.rs:295 validate_rpc_limits walks the protobuf wire format without allocating
- ~/.cargo/git/checkouts/rust-libp2p-b7fa834aec8fc27c/accba72/protocols/gossipsub/src/protocol.rs:349-356 runs before prost decode in GossipsubCodec::decode
- ~/.cargo/git/checkouts/rust-libp2p-b7fa834aec8fc27c/accba72/protocols/gossipsub/src/protocol.rs:370-376 per-topic max transmit size
- [`beacon_node/lighthouse_network/src/config.rs:520-522`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/config.rs#L520-L522) max_publish_messages(500), max_control_message_size(128KB)

**Skeptic check.** Verified the pre-decode wire walk and Lighthouse's 128KB control cap. There are no per-field id counts, but the byte cap bounds the allocation in the same way, so the earlier verdict holds.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#9117](https://github.com/ChainSafe/lodestar/pull/9117), [caplin#24616](https://github.com/erigontech/erigon/pull/24616)

</details>


<a id="gossipsub-022"></a>
<details>
<summary><b>gossipsub-022</b> Bounded per-connection gossipsub send queue — <i>implemented · low · S · memory</i></summary>

**Idea.** Bound each connection handler's gossipsub send queue (for example 5000 messages) to apply backpressure, instead of an unbounded queue that can OOM under load.

**Impact.** The per-peer send queue is bounded. Messages are dropped when the queue is full, so it cannot grow without limit.

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/git/checkouts/rust-libp2p-b7fa834aec8fc27c/accba72/protocols/gossipsub/src/config.rs:556 connection_handler_queue_len 5000
- ~/.cargo/git/checkouts/rust-libp2p-b7fa834aec8fc27c/accba72/protocols/gossipsub/src/behaviour.rs:3424 Queue::new(connection_handler_queue_len)
- ~/.cargo/git/checkouts/rust-libp2p-b7fa834aec8fc27c/accba72/protocols/gossipsub/src/queue.rs:51-84 Publish/IHave/IWant go to bounded non_priority; control bounded by CONTROL_MSGS_LIMIT; only subscribe/extensions are unbounded

**Skeptic check.** Verified the Queue implementation: all data and control messages are bounded, and only the tiny subscription messages are unbounded. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#5066](https://github.com/sigp/lighthouse/pull/5066), [lighthouse#4999](https://github.com/sigp/lighthouse/pull/4999)

</details>


<a id="gossipsub-023"></a>
<details>
<summary><b>gossipsub-023</b> Limit light client update broadcasts — <i>partial · low · S · bandwidth</i></summary>

**Idea.** Broadcast each light client finality update at most as often as the spec allows (twice), with the broadcast logic in the light client store.

**Gap in Lighthouse.** should_broadcast_latest_finality_update and the gossip check in light_client_finality_update_verification.rs::verify do not apply the spec rule. The spec rule is to forward only when finalized_header.slot is new, or the slot is unchanged and the update newly reaches supermajority. Without it, a new finality update goes out about every slot instead of at most twice per finalized checkpoint.

**Impact.** Small cut in gossip bandwidth and CPU: about 30 fewer finality-update broadcasts and validations per epoch.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/light_client_server_cache.rs:151-170`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/light_client_server_cache.rs#L151-L170) latest_finality_update replaced whenever attested slot is newer (each block)
- [`beacon_node/beacon_chain/src/light_client_server_cache.rs:305-325`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/light_client_server_cache.rs#L305-L325) should_broadcast_latest_finality_update only dedupes identical updates
- [`beacon_node/http_api/src/sync_committees.rs:337-350`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/sync_committees.rs#L337-L350) broadcast after sync committee message submission
- [`beacon_node/beacon_chain/src/light_client_finality_update_verification.rs:87-102`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/light_client_finality_update_verification.rs#L87-L102) forwarding filter keyed on attested_header_slot, not finalized_header slot/supermajority

**Skeptic check.** The broadcast logic does live in the LC cache, but it only suppresses identical updates. latest_finality_update changes with every block's attested header, so the twice-per-finalized-header limit from prysm #15540 is missing. The earlier verdict ('once per change') confused deduplication with the spec limit.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [prysm#15540](https://github.com/OffchainLabs/prysm/pull/15540)

</details>


<a id="gossipsub-024"></a>
<details>
<summary><b>gossipsub-024</b> Upgrade QUIC library for throughput and CPU — <i>implemented · low · S · cpu, memory, bandwidth</i></summary>

**Idea.** Keep the QUIC transport library current to get throughput, CPU and memory improvements in the QUIC stack.

**Impact.** Recent quinn versions are in use. This is ongoing upkeep, not a code change.

**Best measured result.** pr:nimbus#8836: "should improve throughput, cpu and ram usage in quic transport"

**Evidence (Lighthouse @ 928b61e719).**

- Cargo.toml:177 libp2p sigp fork rev accba72 with quic feature
- Cargo.lock libp2p-quic 0.14.0, quinn 0.11.12, quinn-proto 0.11.19, quinn-udp 0.5.16

**Skeptic check.** The lock file has the newest quinn and quinn-proto versions present in the local registry (quinn-proto 0.11.19 is the highest cached). The earlier verdict holds.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#8836](https://github.com/status-im/nimbus-eth2/pull/8836)

</details>


<a id="gossipsub-025"></a>
<details>
<summary><b>gossipsub-025</b> Compute gossip message id once and store it — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Compute the gossip message id (sha256 of the uncompressed payload) once per message and store it on the message object, instead of recomputing it each time the pubsub layer asks or keeping it in a separate lookup map. Removes repeated hashing and map lookups.

**Impact.** One hash per message. The only remaining cost is the payload copy into a Vec in prefix(), which is small.

**Best measured result.** getMsgId() took 3% of CPU time (pr:lodestar#3834)

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/git/checkouts/rust-libp2p-b7fa834aec8fc27c/accba72/protocols/gossipsub/src/behaviour.rs:1950 msg_id computed once after inbound_transform and reused for IDONTWANT, validation, duplicate_cache and mcache
- ~/.cargo/git/checkouts/rust-libp2p-b7fa834aec8fc27c/accba72/protocols/gossipsub/src/behaviour.rs:650 computed once on publish
- [`beacon_node/lighthouse_network/src/config.rs:467-497`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/config.rs#L467-L497) prefix() + Sha256 message id closure

**Skeptic check.** Verified that the id is computed once per received message and carried as msg_id through the whole pipeline. The earlier verdict and its note about the minor copy are right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#3251](https://github.com/Consensys-Incorporated/teku/pull/3251), [lodestar#3834](https://github.com/ChainSafe/lodestar/pull/3834), [teku#5469](https://github.com/Consensys-Incorporated/teku/pull/5469)

</details>


<a id="gossipsub-026"></a>
<details>
<summary><b>gossipsub-026</b> Cache gossip topic name string — <i>not · low · S · cpu</i></summary>

**Idea.** Compute each gossip topic name string once in its topic handler instead of rebuilding it on every use.

**Gap in Lighthouse.** Cache the rendered topic String/TopicHash in GossipTopic or the per-fork topic list rather than formatting on each use (GossipTopic Display).

**Impact.** Negligible: a few allocations per publish/subscribe, not per received message.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/types/topics.rs:333`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/topics.rs#L333) From&lt;GossipTopic&gt; for String via to_string each time

**Sources.** [teku#8776](https://github.com/Consensys-Incorporated/teku/pull/8776), [caplin#9000](https://github.com/erigontech/erigon/pull/9000)

</details>


<a id="gossipsub-027"></a>
<details>
<summary><b>gossipsub-027</b> Direct callbacks between gossipsub and processor — <i>n/a · low · S · cpu, latency</i></summary>

**Idea.** Hand gossip messages from gossipsub to the processor through direct calls or channels instead of a generic event emitter dispatch.

**Impact.** None; the Rust swarm already hands messages to the network service and then the beacon processor by direct return and mpsc channel, there is no event-emitter dispatch to remove.

**Best measured result.** pr:lodestar#5300: deployed on test node; screenshots only

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/service/mod.rs:1380`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/mod.rs#L1380) inject_gs_event returns NetworkEvent directly from the swarm poll, no generic emitter
- [`beacon_node/network/src/network_beacon_processor/mod.rs:178`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/mod.rs#L178) send_gossip_beacon_block sends Work to the beacon processor via channel

**Sources.** [lodestar#5300](https://github.com/ChainSafe/lodestar/pull/5300)

</details>


<a id="gossipsub-028"></a>
<details>
<summary><b>gossipsub-028</b> Gossip data columns as partial cell messages — <i>implemented · high · M · bandwidth, latency</i></summary>

**Idea.** Use gossipsub partial messages to disseminate data columns at cell granularity, so peers send only the cells a peer lacks (filling the rest from EL getBlobs) rather than whole column sidecars, and republish as partials complete. Cuts column gossip bandwidth.

**Impact.** Column gossip at cell granularity, on by default, filled from getBlobs and republished as partials complete.

**Best measured result.** pr:lodestar#8748: Reduces bandwidth by ~500KiB per slot (stated)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/src/cli.rs:693-701`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/cli.rs#L693-L701) --enable-partial-columns default_value true
- [`beacon_node/src/config.rs:111-118`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/config.rs#L111-L118) enabled when subnets == columns
- [`beacon_node/lighthouse_network/src/types/topics.rs:210-213`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/topics.rs#L210-L213) use_partial_messages for DataColumnSidecar
- [`beacon_node/lighthouse_network/src/service/mod.rs:372-375`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/mod.rs#L372-L375) enable_partials_for_topic
- [`beacon_node/lighthouse_network/src/service/mod.rs:907`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/mod.rs#L907) publish_partial with request_cells
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1395-1424`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1395-L1424) republish updated partials after merge
- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:299`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L299) import_custody_partial_columns from EL getBlobs

**Skeptic check.** Verified every part of the idea: the default-on flag, topic enablement, cell requests, the EL fill and republish after merge. Partials are disabled only on networks with several columns per subnet.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [grandine#629](https://github.com/grandinetech/grandine/pull/629), [lodestar#8748](https://github.com/ChainSafe/lodestar/pull/8748), [teku#10262](https://github.com/Consensys-Incorporated/teku/pull/10262), [lighthouse#8314](https://github.com/sigp/lighthouse/pull/8314), [prysm#15869](https://github.com/OffchainLabs/prysm/pull/15869), [lighthouse#9343](https://github.com/sigp/lighthouse/pull/9343), [nimbus#8905](https://github.com/status-im/nimbus-eth2/pull/8905), [nimbus#9035](https://github.com/status-im/nimbus-eth2/pull/9035), [prysm#16505](https://github.com/OffchainLabs/prysm/pull/16505), [prysm#16733](https://github.com/OffchainLabs/prysm/pull/16733), [silver#260](https://github.com/gattaca-com/silver/pull/260), [lodestar#9160](https://github.com/ChainSafe/lodestar/pull/9160), [lighthouse#9773](https://github.com/sigp/lighthouse/pull/9773), [prysm#17072](https://github.com/OffchainLabs/prysm/pull/17072)

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

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [lodestar#4169](https://github.com/ChainSafe/lodestar/pull/4169), [caplin#25078](https://github.com/erigontech/erigon/pull/25078), [lodestar#10053](https://github.com/ChainSafe/lodestar/pull/10053)

</details>


<a id="gossipsub-031"></a>
<details>
<summary><b>gossipsub-031</b> Compute identical subnet score params once — <i>implemented · low · S · cpu</i></summary>

**Idea.** Compute topic score parameters once for the attestation subnet topics and reuse them for all 64 subnets instead of per subnet.

**Impact.** None left; params computed once and cloned 64 times.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/service/gossipsub_scoring_parameters.rs:153-155`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/gossipsub_scoring_parameters.rs#L153-L155) get_dynamic_topic_params called once
- [`beacon_node/lighthouse_network/src/service/gossipsub_scoring_parameters.rs:166-171`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/gossipsub_scoring_parameters.rs#L166-L171) same beacon_attestation_subnet_params cloned for each of attestation_subnet_count subnets

**Skeptic check.** Verified: subnet topic params are computed once in get_dynamic_topic_params and cloned per subnet. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar@a40a0a9cc](https://github.com/ChainSafe/lodestar/commit/a40a0a9ccdaf)

</details>


<a id="gossipsub-032"></a>
<details>
<summary><b>gossipsub-032</b> Publish light client updates concurrently — <i>n/a · low · S · latency</i></summary>

**Idea.** Publish light client optimistic and finality updates concurrently, not one after the other.

**Impact.** None; Lighthouse does not originate light client gossip updates, so there is nothing to publish concurrently.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/service.rs:1535`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/service.rs#L1535) LightClientFinalityUpdate gossip is only received and forwarded to the processor
- [`beacon_node/lighthouse_network/src/types/pubsub.rs:184`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/pubsub.rs#L184) topic kinds exist for relay only; no publish path from beacon_chain found

**Sources.** [nimbus#8624](https://github.com/status-im/nimbus-eth2/pull/8624)

</details>


<a id="gossipsub-033"></a>
<details>
<summary><b>gossipsub-033</b> Concurrent map for topic subscriptions — <i>n/a · low · S · cpu</i></summary>

**Idea.** Keep gossip topic subscriptions in a concurrent map instead of a mutex-guarded map copied on every read.

**Impact.** None; the gossipsub behaviour is single-owner in the swarm task so no lock or map copy exists.

**Evidence (Lighthouse @ 928b61e719).**

- accba72/protocols/gossipsub/src/behaviour.rs:323 mesh is a plain HashMap&lt;TopicHash, BTreeSet&lt;PeerId&gt;&gt; owned by the behaviour (&amp;mut self), no mutex and no copy on read

**Sources.** [caplin#9743](https://github.com/erigontech/erigon/pull/9743)

</details>


<a id="gossipsub-034"></a>
<details>
<summary><b>gossipsub-034</b> Dedupe by message id inside gossipsub — <i>implemented · low · S · cpu, bandwidth</i></summary>

**Idea.** Use a content-hash message id and drop already-seen messages inside the gossipsub layer, before application decoding, validation or re-propagation, so duplicates from several peers are processed once.

**Impact.** Duplicates are dropped inside gossipsub before SSZ decoding or validation.

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/git/checkouts/rust-libp2p-b7fa834aec8fc27c/accba72/protocols/gossipsub/src/behaviour.rs:1934-1992 transform, msg_id, duplicate_cache.insert returns early before the message is emitted to the application or forwarded
- [`beacon_node/lighthouse_network/src/config.rs:503`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/config.rs#L503),526-527 duplicate_cache_time 2 epochs, content-hash message_id_fn

**Skeptic check.** Verified that the duplicate check runs before the application event and the forwarding. The earlier verdict holds.

**Verdict history.** implemented (checked) → implemented (skeptic)

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

**Impact.** One decompression per received message, shared by id computation and SSZ decode.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/types/pubsub.rs:104-132`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/pubsub.rs#L104-L132) SnappyTransform::inbound_transform decompresses once
- ~/.cargo/git/checkouts/rust-libp2p-b7fa834aec8fc27c/accba72/protocols/gossipsub/src/behaviour.rs:1934 the only non-test inbound_transform call; msg_id at 1950 hashes the decompressed data
- [`beacon_node/lighthouse_network/src/config.rs:490-497`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/config.rs#L490-L497) message id over message.data (decompressed)

**Skeptic check.** A grep shows inbound_transform has exactly one production call site. The decompressed bytes go to the id function and the application, so the earlier verdict holds.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#2101](https://github.com/sigp/lighthouse/pull/2101), [teku#3188](https://github.com/Consensys-Incorporated/teku/pull/3188), [lodestar#3839](https://github.com/ChainSafe/lodestar/pull/3839), [lodestar#2803](https://github.com/ChainSafe/lodestar/pull/2803)

</details>


<a id="gossipsub-038"></a>
<details>
<summary><b>gossipsub-038</b> Decode gossip off the gossipsub event thread — <i>partial · low · M · cpu, latency</i></summary>

**Idea.** Do SSZ decoding and fork checks of gossip messages on a worker pool, not on the single gossipsub event thread, rejecting early when the queue is full.

**Gap in Lighthouse.** Snappy decompression and full SSZ decode (blocks, data columns, aggregates) stay on the single network service task. Pass the raw gs_msg and topic to a beacon processor work item that decodes on a worker, and report Reject/Ignore via report_message_validation_result when the queue is full.

**Impact.** Removes block/column/aggregate decode from the task that also drives libp2p IO; decode is small versus signature checks, so the gain is mostly tail latency under load.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/types/pubsub.rs:104`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/pubsub.rs#L104) SnappyTransform::inbound_transform decompresses inside the gossipsub behaviour (swarm poll)
- [`beacon_node/lighthouse_network/src/service/mod.rs:1390`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/mod.rs#L1390) PubsubMessage::decode runs synchronously in inject_gs_event on the network service task
- [`beacon_node/lighthouse_network/src/types/pubsub.rs:266`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/pubsub.rs#L266) SignedBeaconBlock::from_ssz_bytes_by_fork and :296 DataColumnSidecar::from_ssz_bytes_for_fork are full SSZ decodes inside that call
- [`beacon_node/network/src/network_beacon_processor/mod.rs:178`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/mod.rs#L178) only verification is handed to beacon processor workers

**Second check.** Confirmed inject_gs_event still calls PubsubMessage::decode inline and that decode builds full typed objects (no lazy or deferred decode); no worker-pool decode or queue-full early reject exists in lighthouse_network or the gossipsub crate.

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [teku#11447](https://github.com/Consensys-Incorporated/teku/pull/11447)

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
<summary><b>gossipsub-040</b> Node-id derived long-lived attestation subnets — <i>implemented · low · S · bandwidth, cpu</i></summary>

**Idea.** Subscribe each node to a fixed small set (two) of long-lived attestation subnets computed from its node id per spec, not one subnet per attached validator, so gossip load per node does not scale with validator count.

**Impact.** Long-lived subnet load does not scale with validator count. Only the short-lived aggregator subscriptions do, as the spec requires.

**Best measured result.** pr:lodestar#5822: most nodes use significantly less resource (charts)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/subnet_service/mod.rs:133-140`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/subnet_service/mod.rs#L133-L140) SubnetId::compute_attestation_subnets(node_id) for permanent subscriptions
- [`consensus/types/src/attestation/subnet_id.rs:106`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/attestation/subnet_id.rs#L106) compute_attestation_subnets
- [`beacon_node/network/src/subnet_service/mod.rs:171-174`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/subnet_service/mod.rs#L171-L174) pre-populates Subscribe events

**Skeptic check.** Verified that permanent subnets come from the node id unless subscribe_all_subnets is set. The earlier verdict holds.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#5822](https://github.com/ChainSafe/lodestar/pull/5822), [lodestar#5704](https://github.com/ChainSafe/lodestar/pull/5704), [prysm#13179](https://github.com/OffchainLabs/prysm/pull/13179), [nimbus#5402](https://github.com/status-im/nimbus-eth2/pull/5402)

</details>


<a id="gossipsub-041"></a>
<details>
<summary><b>gossipsub-041</b> Move state dumps after fork choice update — <i>n/a · low · S · disk, latency</i></summary>

**Idea.** Write beacon state disk dumps after the fork choice update, track gossip subscription expiry with one task, and expire block and blob jobs sooner.

**Impact.** None; this is Caplin-specific scheduling of state dumps and subscription expiry tasks that has no counterpart in Lighthouse.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store) and beacon_chain persist states via the hot/cold DB on import, not as periodic Caplin-style state dumps

**Sources.** [caplin#11058](https://github.com/erigontech/erigon/pull/11058)

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

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [grandine#149](https://github.com/grandinetech/grandine/pull/149), [lighthouse#1613](https://github.com/sigp/lighthouse/pull/1613), [lodestar@3e48a2d07](https://github.com/ChainSafe/lodestar/commit/3e48a2d0743c), [prysm#7468](https://github.com/OffchainLabs/prysm/pull/7468), [lodestar#1712](https://github.com/ChainSafe/lodestar/pull/1712), [nimbus@d9bf6f450](https://github.com/status-im/nimbus-eth2/commit/d9bf6f450d05), [lodestar#1117](https://github.com/ChainSafe/lodestar/pull/1117), [nimbus#1532](https://github.com/status-im/nimbus-eth2/pull/1532), [nimbus#2162](https://github.com/status-im/nimbus-eth2/pull/2162), [teku#3534](https://github.com/Consensys-Incorporated/teku/pull/3534), [prysm#4767](https://github.com/OffchainLabs/prysm/pull/4767), [teku#4914](https://github.com/Consensys-Incorporated/teku/pull/4914)

</details>


<a id="gossipsub-043"></a>
<details>
<summary><b>gossipsub-043</b> Keep libp2p/gossipsub dependencies on fixed, fast versions — <i>implemented · medium · S · memory, cpu, latency, bandwidth</i></summary>

**Idea.** Track upstream libp2p and gossipsub releases (and roll back regressed ones) to pick up hot-path performance fixes (large messages, many topics, router, muxer, crypto) and memory-leak fixes such as duplicate caches holding message references or leaked TCP connections. Upstream perf and leak fixes arrive without local work.

**Impact.** Upstream fixes arrive through the sigp fork, which Lighthouse maintains. This is ongoing upkeep.

**Best measured result.** recent libp2p updates resolve some memory leaks (pr:lodestar#8049)

**Evidence (Lighthouse @ 928b61e719).**

- Cargo.toml:177 libp2p pinned to sigp/rust-libp2p rev accba72 with gossipsub-partial-messages
- Cargo.lock libp2p 0.57.0, libp2p-gossipsub 0.51.0, libp2p-yamux 0.48.0, yamux 0.14.1

**Skeptic check.** Verified the fork pin and the recent crate versions, which include partial messages and IDONTWANT. This is a process idea, and Lighthouse does it.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#14192](https://github.com/OffchainLabs/prysm/pull/14192), [lodestar#6676](https://github.com/ChainSafe/lodestar/pull/6676), [lodestar#6711](https://github.com/ChainSafe/lodestar/pull/6711), [lighthouse#1524](https://github.com/sigp/lighthouse/pull/1524), [lodestar#6156](https://github.com/ChainSafe/lodestar/pull/6156), [prysm#12132](https://github.com/OffchainLabs/prysm/pull/12132), [prysm#15677](https://github.com/OffchainLabs/prysm/pull/15677), [lodestar#6399](https://github.com/ChainSafe/lodestar/pull/6399), [teku#3260](https://github.com/Consensys-Incorporated/teku/pull/3260), [teku#5979](https://github.com/Consensys-Incorporated/teku/pull/5979), [nimbus#2510](https://github.com/status-im/nimbus-eth2/pull/2510), [lodestar#6285](https://github.com/ChainSafe/lodestar/pull/6285), [nimbus#6859](https://github.com/status-im/nimbus-eth2/pull/6859), [teku#6134](https://github.com/Consensys-Incorporated/teku/pull/6134), [lodestar#8049](https://github.com/ChainSafe/lodestar/pull/8049), [prysm#10082](https://github.com/OffchainLabs/prysm/pull/10082), [lighthouse#7828](https://github.com/sigp/lighthouse/pull/7828), [lodestar#3489](https://github.com/ChainSafe/lodestar/pull/3489), [lighthouse#1358](https://github.com/sigp/lighthouse/pull/1358)

</details>


<a id="gossipsub-044"></a>
<details>
<summary><b>gossipsub-044</b> Faster multistream handshake dependency — <i>n/a · low · S · cpu, latency</i></summary>

**Idea.** Use a fast stream handshake implementation for multistream-select protocol negotiation.

**Impact.** None; the idea replaces a slow JS handshake library. Rust multistream-select is already cheap; only V1Lazy could save a round trip, not CPU.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/service/utils.rs:53`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/utils.rs#L53) and :64 upgrade(core::upgrade::Version::V1) with rust multistream-select 0.14 from sigp/rust-libp2p fork

**Sources.** [lodestar#4715](https://github.com/ChainSafe/lodestar/pull/4715), [lodestar#4718](https://github.com/ChainSafe/lodestar/pull/4718), [lodestar#4719](https://github.com/ChainSafe/lodestar/pull/4719)

</details>


<a id="gossipsub-045"></a>
<details>
<summary><b>gossipsub-045</b> Disable gossipsub PRUNE peer exchange — <i>implemented · low · S · bandwidth, cpu</i></summary>

**Idea.** Send zero peers in PRUNE and accept zero peer-exchange records, which saves discovery and dial work and bandwidth.

**Impact.** Outgoing PRUNE carries no peers and incoming PX is ignored.

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/git/checkouts/rust-libp2p-b7fa834aec8fc27c/accba72/protocols/gossipsub/src/config.rs:539-542 do_px false, prune_peers 0
- ~/.cargo/git/checkouts/rust-libp2p-b7fa834aec8fc27c/accba72/protocols/gossipsub/src/behaviour.rs:1253 make_prune selects PX peers only if do_px
- ~/.cargo/git/checkouts/rust-libp2p-b7fa834aec8fc27c/accba72/protocols/gossipsub/src/behaviour.rs:1797 px_connect skipped when prune_peers is 0
- [`beacon_node/lighthouse_network/src/config.rs:509`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/config.rs#L509) builder never sets do_px/prune_peers

**Skeptic check.** Verified both send (make_prune) and receive (handle_prune -&gt; px_connect) paths are disabled by the defaults Lighthouse keeps. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#7894](https://github.com/Consensys-Incorporated/teku/pull/7894), [teku#8056](https://github.com/Consensys-Incorporated/teku/pull/8056)

</details>


<a id="gossipsub-046"></a>
<details>
<summary><b>gossipsub-046</b> Disable unused TLS secure channel — <i>implemented · low · S · cpu</i></summary>

**Idea.** Do not offer the libp2p TLS secure channel when Noise is enough, to save handshake resources.

**Impact.** No TLS security upgrade negotiated over TCP.

**Evidence (Lighthouse @ 928b61e719).**

- Cargo.toml:177 libp2p features have noise, no tls
- [`beacon_node/lighthouse_network/src/service/utils.rs:37-77`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/utils.rs#L37-L77) build_transport authenticates TCP only with noise

**Skeptic check.** Verified TCP transport only offers Noise; the TLS inside QUIC is part of QUIC itself, not an extra negotiated secure channel. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#2622](https://github.com/OffchainLabs/prysm/pull/2622)

</details>


<a id="gossipsub-047"></a>
<details>
<summary><b>gossipsub-047</b> Disable gossipsub flood publish — <i>implemented · medium · S · bandwidth, latency</i></summary>

**Idea.** Turn off gossipsub flood publishing so own blocks and messages go to mesh peers only, not to every connected peer. Cuts upload bandwidth and propagation delay at high peer counts.

**Impact.** Own publishes already go to mesh/fanout peers only.

**Best measured result.** pr:ethlambda#588: 31 to 8 recipients, roughly 4x cut on block/aggregate traffic

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/config.rs:519`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/config.rs#L519)

**Skeptic check.** gossipsub_config builds with .flood_publish(false) and no other place re-enables it; earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [ethlambda#588](https://github.com/lambdaclass/ethlambda/pull/588), [lodestar#6755](https://github.com/ChainSafe/lodestar/pull/6755), [lodestar#6760](https://github.com/ChainSafe/lodestar/pull/6760), [teku#8661](https://github.com/Consensys-Incorporated/teku/pull/8661), [lodestar#6815](https://github.com/ChainSafe/lodestar/pull/6815), [lighthouse#4383](https://github.com/sigp/lighthouse/pull/4383)

</details>


<a id="gossipsub-048"></a>
<details>
<summary><b>gossipsub-048</b> Disable gossipsub self-delivery of own messages — <i>n/a · low · S · cpu</i></summary>

**Idea.** Do not deliver locally published messages back to own subscription handlers when all processing happens in validation, to avoid an async dispatch per publish.

**Impact.** rust-libp2p gossipsub does not deliver own published messages to local handlers, so no async self-dispatch cost exists.

**Best measured result.** pr:nimbus#3826: "the self-publish is async, and therefore has an associated cost"

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/git/checkouts/rust-libp2p-b7fa834aec8fc27c/accba72/protocols/gossipsub/src/behaviour.rs:624-702 publish() puts message in mcache/duplicate cache and sends to peers, with no local Message event

**Sources.** [nimbus#3826](https://github.com/status-im/nimbus-eth2/pull/3826)

</details>


<a id="gossipsub-049"></a>
<details>
<summary><b>gossipsub-049</b> Prefer yamux; disable mplex by default — <i>partial · low · S · memory, cpu, bandwidth</i></summary>

**Idea.** Order stream-multiplexer negotiation so yamux is preferred over mplex, disable mplex by default, and apply strict substream limits when it is enabled.

**Gap in Lighthouse.** Lighthouse PR 9365 made mplex off by default, but this checkout still defaults enable_mplex to true (yamux preferred, strict mplex limits are present). Change the default to false in config.rs:377 and cli.rs, and update the tests in lighthouse/tests/beacon_node.rs:2903.

**Impact.** Peers that support only mplex could still negotiate it; disabling cuts attack surface and a second muxer code path. Small effect on CPU.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/service/utils.rs:47-58`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/utils.rs#L47-L58) SelectUpgrade::new(yamux_config, mplex_config) lists yamux first
- [`beacon_node/lighthouse_network/src/service/utils.rs:49-51`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/utils.rs#L49-L51) mplex max 32 streams, ResetStream
- [`beacon_node/lighthouse_network/src/config.rs:377`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/config.rs#L377) enable_mplex: true default
- [`beacon_node/src/cli.rs:399-406`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/cli.rs#L399-L406) enable-mplex default_value true

**Sources.** [lighthouse#9365](https://github.com/sigp/lighthouse/pull/9365), [prysm#12502](https://github.com/OffchainLabs/prysm/pull/12502)

</details>


<a id="gossipsub-050"></a>
<details>
<summary><b>gossipsub-050</b> Drop decoded gossip objects from caches after handoff — <i>n/a · low · S · memory</i></summary>

**Idea.** Remove the deserialized gossip object from per-message caches (such as a transformed-objects map) right after it is emitted to handlers, not when the cache is pruned, so large decoded objects are not retained.

**Impact.** Lighthouse gossipsub caches raw bytes in mcache and does not keep decoded objects in a per-message cache.

**Best measured result.** 3% of memory retained in transformedObjects (pr:lodestar#2125)

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/git/checkouts/rust-libp2p-b7fa834aec8fc27c/accba72/protocols/gossipsub/src/behaviour.rs: no transformed-objects map; data_transform only used on raw bytes
- [`beacon_node/lighthouse_network/src`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src)/ (grep for data_transform finds no decoded-object cache)

**Sources.** [lodestar@7a67144bc](https://github.com/ChainSafe/lodestar/commit/7a67144bc93e), [lodestar#2125](https://github.com/ChainSafe/lodestar/pull/2125)

</details>


<a id="gossipsub-051"></a>
<details>
<summary><b>gossipsub-051</b> Prune or disconnect peers whose send queue stays full — <i>implemented · medium · S · memory, bandwidth, cpu</i></summary>

**Idea.** React to gossipsub slow-peer signals (send queue stays full) by pruning the peer from the mesh via scoring or disconnecting it, because queued message copies stay in memory and repeated forwards to it are dropped anyway.

**Impact.** Per-peer send queue is bounded (5000), each full-queue drop adds slow_peer_penalty (weight -10, threshold 0) so the peer goes negative and is pruned from the mesh; SlowPeer events also feed peer-manager HighToleranceError reports toward disconnect.

**Best measured result.** pr:ethlambda#739: ~490 MB of queued gossipsub copies in a 2.8 GB steady RSS mainnet follower

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/service/mod.rs:1537`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/mod.rs#L1537)
- [`beacon_node/lighthouse_network/src/service/gossipsub_scoring_parameters.rs:98`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/gossipsub_scoring_parameters.rs#L98)
- accba72/protocols/gossipsub/src/behaviour.rs:3166
- accba72/protocols/gossipsub/src/behaviour.rs:2729
- accba72/protocols/gossipsub/src/config.rs:556

**Skeptic check.** Verified in the sigp rust-libp2p fork: try_push failure increments failed_messages and the score penalty, heartbeat emits SlowPeer, Lighthouse reports the peer. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [ethlambda#739](https://github.com/lambdaclass/ethlambda/pull/739), [ethlambda#589](https://github.com/lambdaclass/ethlambda/pull/589)

</details>


<a id="gossipsub-052"></a>
<details>
<summary><b>gossipsub-052</b> Discard timed-out queued messages on poll — <i>not · low · S · memory, latency</i></summary>

**Idea.** Remove timed-out messages from the connection handler queue whenever it is polled, not only when the next message is sent.

**Gap in Lighthouse.** lighthouse#5175 added a send_queue.poll_stale(cx) step at the end of EnabledHandler::poll that drops the head message if its timeout elapsed, independent of the outbound substream state. The current sigp rust-libp2p (accba72) Queue/Shared has no poll_stale, and EnabledHandler::poll only drops timed-out Publish messages when popping for send. While a send is slow (PendingSend/PendingFlush), expired Publish/forward messages stay in the bounded non_priority queue and cause try_push to reject fresh messages.

**Impact.** On slow peers, stale publishes/forwards keep queue capacity and fresh messages get dropped instead; low overall impact.

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/git/checkouts/rust-libp2p-b7fa834aec8fc27c/accba72/protocols/gossipsub/src/handler.rs:262-275 timeout checked only after poll_pop in the WaitingOutput state, i.e. when the next message is about to be sent
- ~/.cargo/git/checkouts/rust-libp2p-b7fa834aec8fc27c/accba72/protocols/gossipsub/src/handler.rs:289-330 PendingSend/PendingFlush states never inspect the queue
- ~/.cargo/git/checkouts/rust-libp2p-b7fa834aec8fc27c/accba72/protocols/gossipsub/src/handler.rs:411 poll ends with Poll::Pending, no stale-drop step
- ~/.cargo/git/checkouts/rust-libp2p-b7fa834aec8fc27c/accba72/protocols/gossipsub/src/queue.rs:88-106 only remove_data_messages (IDONTWANT) prunes the queue
- git show 256d9042d358 (lighthouse#5175) added send_queue.poll_stale(cx) at the end of EnabledHandler::poll

**Skeptic check.** The earlier evidence cites the send-time timeout check, which existed before #5175. The poll-time stale drop that #5175 added was lost when gossipsub moved to the upstream-style Queue.

**Verdict history.** implemented (checked) → not (skeptic)

**Sources.** [lighthouse#5175](https://github.com/sigp/lighthouse/pull/5175)

</details>


<a id="gossipsub-053"></a>
<details>
<summary><b>gossipsub-053</b> Subscribe only to topics valid for current fork — <i>implemented · low · S · bandwidth, cpu</i></summary>

**Idea.** Define the topic set per fork and subscribe only to topics and subnet counts the current fork uses, unsubscribing obsolete ones (for example blob topics after PeerDAS).

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/types/topics.rs:49-108`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/topics.rs#L49-L108)
- [`beacon_node/lighthouse_network/src/service/mod.rs:726`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/mod.rs#L726)
- [`beacon_node/lighthouse_network/src/service/mod.rs:750`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/mod.rs#L750)
- [`beacon_node/network/src/service.rs:493-495`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/service.rs#L493-L495)

**Skeptic check.** core_topics_to_subscribe builds the set per fork (data columns from Fulu, no blob topics, Gloas/Heze additions), and old-digest topics are dropped by unsubscribe_from_old_fork_topics after the fork. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#4016](https://github.com/sigp/lighthouse/pull/4016), [lighthouse#6932](https://github.com/sigp/lighthouse/pull/6932), [nimbus#6962](https://github.com/status-im/nimbus-eth2/pull/6962), [nimbus#4735](https://github.com/status-im/nimbus-eth2/pull/4735), [lodestar#8497](https://github.com/ChainSafe/lodestar/pull/8497)

</details>


<a id="gossipsub-054"></a>
<details>
<summary><b>gossipsub-054</b> Subscribe attestation subnets only for duties — <i>implemented · medium · S · bandwidth, cpu</i></summary>

**Idea.** Subscribe to short-lived attestation subnets only for committees of attached validators and unsubscribe after, including at startup, instead of all subnets.

**Impact.** Short-lived subnets joined only for aggregator duties and left after the slot; otherwise only spec long-lived subnets.

**Best measured result.** pr:prysm#5123: reduces network spam of unaggregated attestations (no numbers)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/subnet_service/mod.rs:270-273`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/subnet_service/mod.rs#L270-L273)
- [`beacon_node/network/src/subnet_service/mod.rs:435-485`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/subnet_service/mod.rs#L435-L485)
- [`beacon_node/lighthouse_network/src/types/topics.rs:62-66`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/topics.rs#L62-L66)

**Skeptic check.** validator_subscriptions calls subscribe_to_subnet only when is_aggregator, and the subscription expires at slot+1; subscribe_all_subnets is opt-in. Earlier evidence correct (even stricter than the idea: non-aggregators never subscribe).

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#5123](https://github.com/OffchainLabs/prysm/pull/5123), [nimbus#1462](https://github.com/status-im/nimbus-eth2/pull/1462), [nimbus#1346](https://github.com/status-im/nimbus-eth2/pull/1346), [nimbus#2231](https://github.com/status-im/nimbus-eth2/pull/2231), [prysm#4316](https://github.com/OffchainLabs/prysm/pull/4316), [nimbus#1646](https://github.com/status-im/nimbus-eth2/pull/1646), [nimbus#2201](https://github.com/status-im/nimbus-eth2/pull/2201)

</details>


<a id="gossipsub-055"></a>
<details>
<summary><b>gossipsub-055</b> Dynamic sync committee subnet subscriptions — <i>implemented · low · S · bandwidth, cpu</i></summary>

**Idea.** Subscribe to sync committee subnets only for periods when attached validators are in the sync committee.

**Impact.** Nodes join sync subnets only while attached validators are in the sync committee.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/subnet_service/mod.rs:277-330`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/subnet_service/mod.rs#L277-L330) sync subnets subscribed only from VC SyncCommittee subscriptions with until_epoch expiry
- [`beacon_node/network/src/subnet_service/mod.rs:590-603`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/subnet_service/mod.rs#L590-L603) unsubscribe and EnrRemove when expired
- [`beacon_node/lighthouse_network/src/types/topics.rs:71-75`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/topics.rs#L71-L75) sync subnets are core topics only with subscribe_all_subnets

**Skeptic check.** Verified the subscription is driven by VC duties with an expiry, and sync subnets are not core topics by default. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#3308](https://github.com/status-im/nimbus-eth2/pull/3308)

</details>


<a id="gossipsub-056"></a>
<details>
<summary><b>gossipsub-056</b> Subscribe duty subnets one epoch early — <i>partial · low · S · latency</i></summary>

**Idea.** Subscribe to the attestation subnet one epoch before the duty slot so the mesh is formed in time.

**Gap in Lighthouse.** The BN node-side scheduler subscribes only one slot before the duty (subscribe_to_subnet), not an epoch. The VC sends subscriptions earlier, and discovery runs ahead, but the gossip mesh join is one slot ahead. To follow the idea, raise the advance duration in subscribe_to_subnet to a full epoch (costs more subnet churn).

**Impact.** Mesh may be formed less well for a short-lived attester's first message; small gain, extra bandwidth if lengthened.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/subnet_service/mod.rs:48-51`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/subnet_service/mod.rs#L48-L51) ADVANCE_SUBSCRIBE_SLOT_FRACTION=1 (one slot ahead)
- [`validator_client/validator_services/src/duties_service.rs:79`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L79) MIN_ATTESTATION_SUBSCRIPTION_LOOKAHEAD, ATTESTATION_SUBSCRIPTION_OFFSETS

**Sources.** [lighthouse#1600](https://github.com/sigp/lighthouse/pull/1600)

</details>


<a id="gossipsub-057"></a>
<details>
<summary><b>gossipsub-057</b> Correct subnet subscription time computation — <i>implemented · low · S · latency</i></summary>

**Idea.** Compute the subscribe time as time to next slot plus slot duration times slots until subscribe, so subscriptions are sent on time.

**Impact.** Subscriptions are scheduled from the slot clock's exact duration to the target slot.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/subnet_service/mod.rs:446-461`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/subnet_service/mod.rs#L446-L461) time_to_subscription_start = slot_clock.duration_to_slot(slot) - advance

**Skeptic check.** duration_to_slot gives the exact time to the slot, so it includes the time-to-next-slot part the original fix added. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#981](https://github.com/sigp/lighthouse/pull/981)

</details>


<a id="gossipsub-058"></a>
<details>
<summary><b>gossipsub-058</b> Just-in-time short-lived duty subnet subscription — <i>implemented · medium · S · bandwidth, cpu</i></summary>

**Idea.** Join a short-lived attestation/aggregation subnet only a few slots before the duty slot (while searching for subnet peers earlier) and leave right after the slot, rather than at epoch granularity or with long lead time. Cuts time subscribed and subnet traffic received.

**Impact.** Already just-in-time: discovery starts &gt;=2 slots early, subscription one slot before duty, unsubscribe at end of duty slot.

**Best measured result.** about 25% reduction in attestation subnet topic subscription in the ideal case (pr:nimbus#2240)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/subnet_service/mod.rs:51`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/subnet_service/mod.rs#L51)
- [`beacon_node/network/src/subnet_service/mod.rs:387-428`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/subnet_service/mod.rs#L387-L428)
- [`beacon_node/network/src/subnet_service/mod.rs:452-482`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/subnet_service/mod.rs#L452-L482)

**Skeptic check.** subscribe_to_subnet schedules the join at duty slot minus one slot and subscribe_to_subnet_immediately ends it at slot+1; discover_peers_request runs separately ahead of time. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#3419](https://github.com/sigp/lighthouse/pull/3419), [lighthouse#3475](https://github.com/sigp/lighthouse/pull/3475), [lodestar#5810](https://github.com/ChainSafe/lodestar/pull/5810), [nimbus#2240](https://github.com/status-im/nimbus-eth2/pull/2240), [nimbus#2555](https://github.com/status-im/nimbus-eth2/pull/2555), [teku#3854](https://github.com/Consensys-Incorporated/teku/pull/3854), [teku#1553](https://github.com/Consensys-Incorporated/teku/pull/1553)

</details>


<a id="gossipsub-059"></a>
<details>
<summary><b>gossipsub-059</b> Expiring gossip topic listeners — <i>not · low · M · cpu, bandwidth</i></summary>

**Idea.** Give each topic subscription an expiry; once it passes, close the listener but keep the topic joined for publishing, and revive it on renewal.

**Gap in Lighthouse.** Lighthouse has no listener-vs-publish split; subnet subscriptions are unsubscribed explicitly from subnet_service expiry events. Would need a gossipsub-level 'publish-only' topic state.

**Impact.** Marginal: avoids re-graft churn when a short-lived subnet subscription is renewed; negligible CPU on mainnet.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/service/mod.rs:816`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/mod.rs#L816) subscribe/unsubscribe called explicitly
- [`beacon_node/lighthouse_network/src/service/mod.rs:829`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/mod.rs#L829) unsubscribe sends gossipsub unsubscribe, leaving mesh

**Sources.** [caplin#9734](https://github.com/erigontech/erigon/pull/9734), [caplin#9821](https://github.com/erigontech/erigon/pull/9821)

</details>


<a id="gossipsub-060"></a>
<details>
<summary><b>gossipsub-060</b> Wake network task on subnet service events — <i>implemented · low · S · latency</i></summary>

**Idea.** Register a waker so the network task is polled as soon as the subnet subscription service has new events.

**Impact.** Network task is woken as soon as the subnet service queues events.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/subnet_service/mod.rs:101`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/subnet_service/mod.rs#L101) waker field
- [`beacon_node/network/src/subnet_service/mod.rs:376-381`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/subnet_service/mod.rs#L376-L381) queue_event wakes the waker
- [`beacon_node/network/src/subnet_service/mod.rs:609-616`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/subnet_service/mod.rs#L609-L616) poll_next stores/updates the waker

**Skeptic check.** Verified that queue_event calls wake_by_ref and poll_next refreshes the waker. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#1305](https://github.com/sigp/lighthouse/pull/1305)

</details>


<a id="gossipsub-061"></a>
<details>
<summary><b>gossipsub-061</b> Publish completion signal on first send — <i>not · low · M · latency</i></summary>

**Idea.** Return a future from gossip publish that completes when the first message hits the wire, so block and blob publishing can report completion.

**Gap in Lighthouse.** Gossipsub publish returns MessageId only after enqueuing; no wire-send completion future. Would need a completion channel in the sigp/rust-libp2p handler and plumbing back through NetworkMessage::Publish.

**Impact.** Reporting/metrics only (time-to-wire for blocks/blobs); no speedup.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/service/mod.rs:844`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/mod.rs#L844) publish() is synchronous, returns nothing to the caller
- [`beacon_node/network/src/service.rs:687`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/service.rs#L687) calls libp2p.publish(messages) fire-and-forget

**Sources.** [teku#8735](https://github.com/Consensys-Incorporated/teku/pull/8735)

</details>


<a id="gossipsub-062"></a>
<details>
<summary><b>gossipsub-062</b> One buffer allocation per gossip write — <i>n/a · low · cpu, memory</i></summary>

**Idea.** Reserve the length prefix in the same buffer reservation and allocate one buffer wrapper per write, not per partial write, on the gossip send path.

**Gap in Lighthouse.** Idea targets a .NET/Nim-style codec buffer wrapper allocation; Lighthouse's Rust BytesMut encode path has no per-partial-write wrapper allocation.

**Impact.** Nothing comparable to save.

**Evidence (Lighthouse @ 928b61e719).**

- rust-libp2p gossipsub protocol.rs:200 uses prost_codec::Codec over asynchronous_codec::Framed
- [`beacon_node/lighthouse_network/src/types/pubsub.rs:149`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/pubsub.rs#L149) snappy encoder separate

**Sources.** [silver#408](https://github.com/gattaca-com/silver/pull/408)

</details>


<a id="gossipsub-063"></a>
<details>
<summary><b>gossipsub-063</b> Flood publish time-critical messages — <i>not · low · S · latency</i></summary>

**Idea.** Flood-publish selected time-critical messages (such as payload bids) to all peers per publish call, while other messages go to mesh only.

**Gap in Lighthouse.** Gossipsub flood_publish is global and set false; there is no per-publish flood option. Would need a per-topic or per-call flood flag in the sigp gossipsub fork and use it for bids in publish().

**Impact.** Faster dissemination of the node's own time-critical messages (e.g. Gloas payload bids) by one mesh hop; affects only publishers, a few messages per slot.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/config.rs:519`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/config.rs#L519) .flood_publish(false)
- rust-libp2p gossipsub behaviour.rs:771 flood_publish is a global config flag, no per-topic/per-call override

**Sources.** [lodestar#9914](https://github.com/ChainSafe/lodestar/pull/9914)

</details>


<a id="gossipsub-064"></a>
<details>
<summary><b>gossipsub-064</b> Forward gossip right after validation, before processing — <i>implemented · high · S · latency</i></summary>

**Idea.** Forward an ACCEPTed gossip message (notably a block) to the mesh as soon as gossip validation passes, before heavy handlers such as fork choice and full block import run. Cuts per-hop propagation delay.

**Impact.** Blocks, columns and attestations forwarded right after gossip verification, before import/fork choice.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1661`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1661)
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:728`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L728)
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:416-424`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L416-L424)
- [`beacon_node/lighthouse_network/src/config.rs:524`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/config.rs#L524)

**Skeptic check.** Accept is propagated immediately after verify_*_for_gossip on block, data column and attestation paths, before process_gossip_verified_block / fork choice application. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#9990](https://github.com/ChainSafe/lodestar/pull/9990), [silver#174](https://github.com/gattaca-com/silver/pull/174)

</details>


<a id="gossipsub-065"></a>
<details>
<summary><b>gossipsub-065</b> Non-supernodes publish reconstructed custody columns — <i>implemented · medium · S · latency, bandwidth</i></summary>

**Idea.** Let full nodes publish their custody data columns built from EL getBlobs, in random order, so columns propagate sooner.

**Impact.** Any node publishes its getBlobs-built custody columns, shuffled and in batches, skipping columns already seen.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/mod.rs:997-1020`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/mod.rs#L997-L1020)
- [`beacon_node/network/src/network_beacon_processor/mod.rs:1264-1320`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/mod.rs#L1264-L1320)
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1125`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1125)
- [`beacon_node/network/src/network_beacon_processor/mod.rs:1218`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/mod.rs#L1218)

**Skeptic check.** fetch_engine_blobs_and_publish_full uses sampling_columns_for_epoch (custody, not supernode-only) and publish_blobs=true on the gossip path; publish_data_columns_gradually shuffles. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#7258](https://github.com/sigp/lighthouse/pull/7258)

</details>


<a id="gossipsub-066"></a>
<details>
<summary><b>gossipsub-066</b> Check topic subscription before decoding partial messages — <i>not · low · S · cpu, latency</i></summary>

**Idea.** Check that a topic is subscribed before SSZ-decoding large partial messages from peers on the shared gossip loop.

**Gap in Lighthouse.** Partials are enabled for all 128 column subnets on all current and future digests. handle_received gates on that enabled set, not on subscription, so a peer can push partial columns for subnets this node does not sample, and Lighthouse SSZ-decodes them in the Event::Partial branch of the swarm event handler in service/mod.rs. Add a subscribed-topic check (gossipsub mesh contains topic, or network_globals.gossipsub_subscriptions) before decode_partial, or before EmitEvent in handle_received.

**Impact.** Avoids decoding large unsolicited partial columns on the network thread; only applies with enable_partial_columns, which defaults to off, so low today.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/service/mod.rs:372-377`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/mod.rs#L372-L377) enable_partials_for_topic for every topic in all_topics_for_digests
- [`beacon_node/lighthouse_network/src/types/topics.rs:140-149`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/topics.rs#L140-L149) all_topics_at_fork includes all data column subnets (worst case), not only sampling subnets
- ~/.cargo/git/checkouts/rust-libp2p-b7fa834aec8fc27c/accba72/protocols/gossipsub/src/extensions/partial_messages.rs:127-143 enabled topics are never removed
- ~/.cargo/git/checkouts/rust-libp2p-b7fa834aec8fc27c/accba72/protocols/gossipsub/src/extensions/partial_messages.rs:295-368 handle_received checks only the enabled-topic map, then emits EmitEvent when no local partial exists
- ~/.cargo/git/checkouts/rust-libp2p-b7fa834aec8fc27c/accba72/protocols/gossipsub/src/behaviour.rs:3655-3690 only a graylist check before handle_received, no mesh/subscription check
- [`beacon_node/lighthouse_network/src/service/mod.rs:1414-1432`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/mod.rs#L1414-L1432) Event::Partial goes straight to decode_partial with no subscription check

**Skeptic check.** The earlier evidence took 'enabled for partials' to mean 'subscribed'. Lighthouse enables partials for every column subnet at startup, so the gossipsub check does not filter unsubscribed subnets.

**Verdict history.** implemented (checked) → not (skeptic)

**Sources.** [prysm#17074](https://github.com/OffchainLabs/prysm/pull/17074)

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

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [teku#3812](https://github.com/Consensys-Incorporated/teku/pull/3812)

</details>


<a id="gossipsub-069"></a>
<details>
<summary><b>gossipsub-069</b> Snappy-compress all gossip payloads — <i>implemented · low · S · bandwidth</i></summary>

**Idea.** Publish gossip payloads only in snappy-compressed (ssz_snappy) encoding on the wire and never also uncompressed, to cut bytes sent.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/types/pubsub.rs:136-150`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/pubsub.rs#L136-L150)
- [`beacon_node/lighthouse_network/src/types/pubsub.rs:104-133`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/pubsub.rs#L104-L133)
- [`beacon_node/lighthouse_network/src/types/topics.rs:235-239`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/topics.rs#L235-L239)

**Skeptic check.** GossipEncoding has only SSZSnappy and the SnappyTransform outbound_transform compresses every payload. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#860](https://github.com/ChainSafe/lodestar/pull/860), [nimbus#1240](https://github.com/status-im/nimbus-eth2/pull/1240), [lighthouse#984](https://github.com/sigp/lighthouse/pull/984), [teku#1722](https://github.com/Consensys-Incorporated/teku/pull/1722), [nimbus#890](https://github.com/status-im/nimbus-eth2/pull/890)

</details>


<a id="gossipsub-070"></a>
<details>
<summary><b>gossipsub-070</b> Gossipsub topic subscription allowlist filter — <i>implemented · medium · S · memory, cpu, bandwidth</i></summary>

**Idea.** Install a gossipsub subscription/topic filter so the router tracks peer subscriptions and accepts messages only for topics valid for the current fork digest and actually needed, before keeping state or validating them. Saves memory, bandwidth and validation.

**Impact.** Peer subscription tracking is limited to known Ethereum topics with a max count; messages on topics we do not subscribe to never reach Lighthouse validation.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/service/utils.rs:266-305`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/utils.rs#L266-L305) create_whitelist_filter
- [`beacon_node/lighthouse_network/src/service/mod.rs:129-131`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/mod.rs#L129-L131),332-340 MaxCountSubscriptionFilter&lt;WhitelistSubscriptionFilter&gt;
- ~/.cargo/git/checkouts/rust-libp2p-b7fa834aec8fc27c/accba72/protocols/gossipsub/src/behaviour.rs:2111 filter_incoming_subscriptions on peer SUBSCRIBE
- ~/.cargo/git/checkouts/rust-libp2p-b7fa834aec8fc27c/accba72/protocols/gossipsub/src/behaviour.rs:2021-2034 messages on unsubscribed topics are not dispatched for validation

**Skeptic check.** Verified the whitelist plus max-count filter is applied to incoming peer subscriptions, matching the Prysm/Teku topic filter. The whitelist covers all fork digests (not only the current ones), and gossipsub still puts unsubscribed-topic messages in mcache, but the core mechanism and its effect are present.

**Verdict history.** implemented (checked) → implemented (skeptic)

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

**Verdict history.** not (checked) → partial (refuted)

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

**Verdict history.** not (checked) → not (refuted)

**Sources.** [nimbus#2172](https://github.com/status-im/nimbus-eth2/pull/2172)

</details>


<a id="gossipsub-073"></a>
<details>
<summary><b>gossipsub-073</b> Larger recvmmsg/sendmmsg batches in UDP transport — <i>n/a · low · cpu</i></summary>

**Idea.** Handle more UDP datagrams per recvmmsg or sendmmsg syscall in the QUIC/UDP transport, so fewer syscalls are needed per packet under high throughput.

**Gap in Lighthouse.** Batching size is inside the quinn-udp dependency (already uses recvmmsg and GSO on Linux); Lighthouse does not own that code.

**Impact.** Only a dependency bump could change it; marginal.

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/registry/src/*/quinn-udp-0.5.16/src/unix.rs:466 recvmmsg batched with BATCH_SIZE
- libp2p-quic from sigp/rust-libp2p uses quinn-udp

**Sources.** [silver@b77055396](https://github.com/gattaca-com/silver/commit/b77055396b7c)

</details>


<a id="gossipsub-074"></a>
<details>
<summary><b>gossipsub-074</b> Lazy sweep of idle rate-limiter buckets — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Sweep idle per-peer rate-limiter buckets lazily in the acquire path instead of one sleeping cleanup task per limiter.

**Impact.** None; there is no per-limiter cleanup task to remove.

**Best measured result.** pr:caplin#25039: cleanup goroutines 13 -&gt; 0

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/rpc/rate_limiter.rs:93`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/rate_limiter.rs#L93) prune_interval field
- [`beacon_node/lighthouse_network/src/rpc/rate_limiter.rs:275-280`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/rate_limiter.rs#L275-L280) single 30s interval
- [`beacon_node/lighthouse_network/src/rpc/rate_limiter.rs:425-467`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/rate_limiter.rs#L425-L467),474-476 prune() of all per-protocol limiters from one Future::poll

**Skeptic check.** Confirmed the RPC rate limiter prunes all per-protocol buckets from one interval polled inside the behaviour, with no spawned task per limiter. Earlier evidence was right; the pruning is not in the acquire path, but the cost the idea removes (many sleeping tasks) does not exist.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [caplin#25039](https://github.com/erigontech/erigon/pull/25039)

</details>


<a id="gossipsub-075"></a>
<details>
<summary><b>gossipsub-075</b> Copy native snappy output into runtime buffer — <i>n/a · low · memory</i></summary>

**Idea.** Have a native snappy binding copy output into a runtime-owned buffer, so native allocations free inside the call and not on a finalizer, lowering peak RSS.

**Gap in Lighthouse.** Lighthouse uses the pure-Rust snap crate with Rust-owned buffers; there is no native binding with finalizer-freed memory.

**Impact.** None.

**Best measured result.** pr:lodestar#10069: Reqresp 64 KiB alloc trial peak RSS 183.4 -&gt; 109.1 MiB; durable merge RSS growth 73.0 -&gt; 55.4 MiB; read-all 2.354 -&gt; 3.806 ms

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/types/pubsub.rs:6`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/pubsub.rs#L6) uses pure-Rust snap::raw
- [`beacon_node/lighthouse_network/src/rpc/codec.rs:8`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/codec.rs#L8) snap::read FrameDecoder

**Sources.** [lodestar#10069](https://github.com/ChainSafe/lodestar/pull/10069)

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

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [lighthouse#1413](https://github.com/sigp/lighthouse/pull/1413), [caplin#11756](https://github.com/erigontech/erigon/pull/11756)

</details>


<a id="gossipsub-077"></a>
<details>
<summary><b>gossipsub-077</b> Gossipsub seen-cache TTL spans attestation propagation window — <i>implemented · medium · S · cpu, bandwidth</i></summary>

**Idea.** Configure the gossipsub duplicate/seen-message cache duration to cover the whole period a message can still propagate (up to two epochs for attestations), so late duplicates are dropped at the network layer instead of being re-validated and re-forwarded.

**Impact.** Late duplicate attestations within 2 epochs are dropped in gossipsub before Lighthouse validation.

**Best measured result.** cache 2.1s to 8.4s; max RPC messages 10 to 500 (pr:lighthouse#2391)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/config.rs:500-507`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/config.rs#L500-L507) duplicate_cache_time = 2 epochs
- [`beacon_node/lighthouse_network/src/config.rs:526`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/config.rs#L526) .duplicate_cache_time(duplicate_cache_time)
- [`beacon_node/lighthouse_network/src/config.rs:516`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/config.rs#L516) max_publish_messages(500)
- ~/.cargo/git/checkouts/rust-libp2p-b7fa834aec8fc27c/accba72/protocols/gossipsub/src/behaviour.rs:1986-1993 duplicate_cache check before dispatch

**Skeptic check.** Verified the seen cache TTL is 2 epochs for every fork and gossipsub drops duplicates before dispatch. The 500 publish-message cap from lighthouse#2391 is also present.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#2542](https://github.com/sigp/lighthouse/pull/2542), [teku#3257](https://github.com/Consensys-Incorporated/teku/pull/3257), [nimbus#6098](https://github.com/status-im/nimbus-eth2/pull/6098), [prysm#14030](https://github.com/OffchainLabs/prysm/pull/14030), [lighthouse#2391](https://github.com/sigp/lighthouse/pull/2391)

</details>


<a id="gossipsub-078"></a>
<details>
<summary><b>gossipsub-078</b> Tune gossipsub mesh degree and gossip parameters — <i>implemented · medium · S · bandwidth, cpu, memory</i></summary>

**Idea.** Set gossipsub D/D_low/D_high/D_lazy, gossip factor and history length in the network config to values tuned for Ethereum peer counts rather than library defaults, so fewer duplicate messages, IHAVEs and cached messages are handled.

**Impact.** Mesh and gossip parameters are tuned per network-load setting rather than library defaults.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/config.rs:389-469`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/config.rs#L389-L469) NetworkLoad presets (mesh_n, mesh_n_low/high, outbound_min, gossip_lazy, history_gossip, heartbeat)
- [`beacon_node/lighthouse_network/src/config.rs:509-526`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/config.rs#L509-L526) gossipsub ConfigBuilder with history_length(12), fanout_ttl, flood_publish(false), control message caps

**Skeptic check.** Confirmed all the named parameters are set from Lighthouse-specific presets in gossipsub_config. Earlier evidence was accurate.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#2169](https://github.com/status-im/nimbus-eth2/pull/2169), [lodestar#5427](https://github.com/ChainSafe/lodestar/pull/5427), [lodestar#5865](https://github.com/ChainSafe/lodestar/pull/5865), [teku#7419](https://github.com/Consensys-Incorporated/teku/pull/7419), [lighthouse#2608](https://github.com/sigp/lighthouse/pull/2608), [lighthouse#1449](https://github.com/sigp/lighthouse/pull/1449)

</details>


<a id="gossipsub-079"></a>
<details>
<summary><b>gossipsub-079</b> Ethereum-specific per-topic gossipsub scoring parameters — <i>partial · low · M · bandwidth, cpu</i></summary>

**Idea.** Configure gossipsub peer scoring with per-topic parameters derived from expected Ethereum message rates per topic type, instead of generic defaults, so poor peers are pruned from meshes.

**Gap in Lighthouse.** get_peer_score_params has no TopicScoreParams for SyncCommitteeMessage subnets, SignedContributionAndProof, BlsToExecutionChange, light-client topics, or DataColumnSidecar subnets (nimbus#6979 scores sync committee, contribution and BLS-change topics). Peers on those meshes are scored only by global P5/P7, so poor column/sync peers are never pruned by topic delivery scoring.

**Impact.** Faster pruning of under-delivering peers on data column and sync committee meshes; small gain, with risk of false penalties if expected rates are wrong.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/service/gossipsub_scoring_parameters.rs:83-174`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/gossipsub_scoring_parameters.rs#L83-L174) get_peer_score_params inserts topic params only for VoluntaryExit, AttesterSlashing, ProposerSlashing, BeaconBlock, BeaconAggregateAndProof, Attestation subnets
- [`beacon_node/lighthouse_network/src/service/gossipsub_scoring_parameters.rs:176-235`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/gossipsub_scoring_parameters.rs#L176-L235) get_dynamic_topic_params covers only block, aggregate, attestation

**Skeptic check.** Verified the per-topic, rate-derived scoring is real but stops at phase0 topics. The earlier evidence was right about the mechanism and wrong to call it complete; post-Altair/PeerDAS topics are unscored.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [nimbus#6979](https://github.com/status-im/nimbus-eth2/pull/6979), [lodestar#3126](https://github.com/ChainSafe/lodestar/pull/3126), [lighthouse#2165](https://github.com/sigp/lighthouse/pull/2165)

</details>


<a id="gossipsub-080"></a>
<details>
<summary><b>gossipsub-080</b> Tune yamux flow-control window — <i>implemented · low · S · bandwidth, memory</i></summary>

**Idea.** Configure the yamux stream multiplexer window mode/size so streams get high throughput without overfilling buffers under load.

**Impact.** Already in effect: yamux 0.14 auto-tunes the per-stream window from RTT and always sends window updates on read, which is what the LH PRs configured by hand.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/service/utils.rs:44`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/utils.rs#L44) yamux::Config::default()
- Cargo.lock:6115-6124 libp2p-yamux 0.48.0 depends only on yamux 0.14.1
- ~/.cargo/registry/src/*/yamux-0.14.1/src/lib.rs:45,87-89 DEFAULT_CREDIT 256KiB, max_connection_receive_window Some(GIB)
- ~/.cargo/registry/src/*/yamux-0.14.1/src/connection/stream.rs:11,134-173 Rtt-based auto-tuned receive window

**Skeptic check.** Confirmed libp2p-yamux 0.48 uses only yamux 0.14.1 (no legacy 0.12 path), whose flow control is RTT auto-tuned with a 1 GiB connection cap. Earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#4996](https://github.com/sigp/lighthouse/pull/4996), [lighthouse#2390](https://github.com/sigp/lighthouse/pull/2390)

</details>


<a id="gossipsub-081"></a>
<details>
<summary><b>gossipsub-081</b> Unsubscribe expired long-lived random subnets — <i>n/a · low · S · bandwidth</i></summary>

**Idea.** When a long-lived (random/backbone) attestation subnet subscription expires, actually unsubscribe from it so subscriptions and bandwidth do not accumulate over time.

**Impact.** None.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/subnet_service/mod.rs:126-140`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/subnet_service/mod.rs#L126-L140) permanent attestation subnets computed once from node id
- [`consensus/types/src/attestation/subnet_id.rs:106`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/attestation/subnet_id.rs#L106) compute_attestation_subnets has no epoch/random component

**Sources.** [lighthouse#3600](https://github.com/sigp/lighthouse/pull/3600)

</details>


<a id="gossipsub-082"></a>
<details>
<summary><b>gossipsub-082</b> Subscribe to duty subnet only when aggregating — <i>implemented · medium · S · bandwidth, cpu</i></summary>

**Idea.** For attestation duties, subscribe to the subnet only if the validator is an aggregator for that slot; non-aggregators publish via gossipsub fanout without subscribing, avoiding subnet decode/verify/relay work.

**Impact.** Non-aggregating duties do not subscribe to the subnet; they publish through fanout peers found by discovery.

**Best measured result.** 64 validators: 55 subnets subscribed vs ~4.9 aggregator subnets (estimate) (pr:caplin#25008)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/subnet_service/mod.rs:266-275`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/subnet_service/mod.rs#L266-L275) subscribe_to_subnet only when subscription.is_aggregator
- [`beacon_node/network/src/subnet_service/mod.rs:256-262`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/subnet_service/mod.rs#L256-L262) non-aggregators only add the subnet to discovery
- [`beacon_node/network/src/subnet_service/mod.rs:119-127`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/subnet_service/mod.rs#L119-L127) subscribe_all_subnets is opt-in

**Skeptic check.** Verified the attestation duty path subscribes only for aggregators; non-aggregators only trigger peer discovery for that subnet. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [caplin#25008](https://github.com/erigontech/erigon/pull/25008), [nimbus#2254](https://github.com/status-im/nimbus-eth2/pull/2254), [ethlambda#160](https://github.com/lambdaclass/ethlambda/pull/160), [ethlambda#265](https://github.com/lambdaclass/ethlambda/pull/265), [prysm#5318](https://github.com/OffchainLabs/prysm/pull/5318), [teku#1556](https://github.com/Consensys-Incorporated/teku/pull/1556)

</details>


<a id="gossipsub-083"></a>
<details>
<summary><b>gossipsub-083</b> No subnet subscriptions without attached validators — <i>implemented · low · S · bandwidth, cpu</i></summary>

**Idea.** A node with zero attached validators holds no duty or stability attestation subnet subscriptions beyond what the spec requires, avoiding subnet gossip traffic.

**Impact.** None; a node with no validators holds only spec-required node-id backbone subnets.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/subnet_service/mod.rs:126-142`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/subnet_service/mod.rs#L126-L142) permanent subscriptions only from node-id (compute_attestation_subnets) unless subscribe_all_subnets
- [`beacon_node/network/src/subnet_service/mod.rs:209-225`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/subnet_service/mod.rs#L209-L225) duty subnets only come from validator_subscriptions; proposer_only ignores all
- [`beacon_node/network/src/subnet_service/mod.rs:257-262`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/subnet_service/mod.rs#L257-L262) short-lived attestation subnet only subscribed when is_aggregator

**Skeptic check.** Verified that with no attached validators no duty or sync subnets are subscribed; the backbone subnets are spec-mandated. Earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#2230](https://github.com/status-im/nimbus-eth2/pull/2230), [prysm#421](https://github.com/OffchainLabs/prysm/pull/421), [caplin#9803](https://github.com/erigontech/erigon/pull/9803)

</details>


<a id="gossipsub-084"></a>
<details>
<summary><b>gossipsub-084</b> Skip subscription for already-past slots — <i>implemented · low · S · cpu, bandwidth</i></summary>

**Idea.** When a subnet subscription request targets a slot that has already passed, drop it instead of subscribing and immediately unsubscribing.

**Impact.** None; past-slot subscriptions never emit Subscribe/Unsubscribe.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/subnet_service/mod.rs:452-458`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/subnet_service/mod.rs#L452-L458) past slot yields zero duration
- [`beacon_node/network/src/subnet_service/mod.rs:472-474`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/subnet_service/mod.rs#L472-L474) subscribe_to_subnet_immediately(subnet, slot + 1)
- [`beacon_node/network/src/subnet_service/mod.rs:546-555`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/subnet_service/mod.rs#L546-L555) returns Err when end slot already passed, no Subscribe event
- [`beacon_node/network/src/subnet_service/mod.rs:315-330`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/subnet_service/mod.rs#L315-L330) sync subscription past expiration skipped
- [`beacon_node/network/src/subnet_service/mod.rs:403-423`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/subnet_service/mod.rs#L403-L423) discovery skipped for slots without lookahead

**Skeptic check.** Confirmed both attestation and sync paths drop already-expired subscriptions before emitting events, and discovery is skipped too. Only a trivial aggregate-tracking map insert remains.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#8837](https://github.com/Consensys-Incorporated/teku/pull/8837)

</details>


<a id="gossipsub-085"></a>
<details>
<summary><b>gossipsub-085</b> Avoid redundant topic re-subscription — <i>implemented · low · S · cpu, bandwidth</i></summary>

**Idea.** Skip subscribe/unsubscribe calls for topics already subscribed (core topics, subscribe-all subnets, data column topics, fixed subnet sets) and only change subscriptions when the required set changes, instead of re-issuing them every slot or epoch.

**Impact.** None; subscriptions change only when the required set changes.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/service.rs:742-761`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/service.rs#L742-L761) core topics subscribed once on startup/fork events
- [`beacon_node/network/src/service.rs:856-871`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/service.rs#L856-L871) subnet subscribe/unsubscribe only on SubnetServiceMessage
- [`beacon_node/network/src/subnet_service/mod.rs:498-526`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/subnet_service/mod.rs#L498-L526),557-586 existing subscription only extends timeout, no new Subscribe event
- ~/.cargo/git/checkouts/rust-libp2p-b7fa834aec8fc27c/accba72/protocols/gossipsub/src/behaviour.rs:563-566 subscribe returns Ok(false) if already in mesh

**Skeptic check.** Confirmed the subnet service checks the existing subscription deadline and emits Subscribe only for new subnets; subscribe_all_subnets returns early. Libp2p also short-circuits duplicate subscribes.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#4829](https://github.com/ChainSafe/lodestar/pull/4829), [lighthouse#4271](https://github.com/sigp/lighthouse/pull/4271), [nimbus#8688](https://github.com/status-im/nimbus-eth2/pull/8688), [prysm#15895](https://github.com/OffchainLabs/prysm/pull/15895), [prysm#5349](https://github.com/OffchainLabs/prysm/pull/5349)

</details>


<a id="gossipsub-086"></a>
<details>
<summary><b>gossipsub-086</b> Request bitmap for missing partial-column cells — <i>implemented · medium · S · bandwidth</i></summary>

**Idea.** Include a request bitmap in partial-column metadata so a peer advertises exactly which cells it still needs, letting senders transmit only requested cells; publish an empty column plus request when the EL has no blobs.

**Impact.** When partial columns are enabled, peers send only the cells a node requests, and custody columns with no EL blobs are announced as empty plus request-all.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/types/partial.rs:30-61`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/partial.rs#L30-L61) OutgoingPartialColumnFulu metadata with available + requests bitmap
- [`beacon_node/lighthouse_network/src/types/partial.rs:214-240`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/partial.rs#L214-L240) action_from_present_metadata sends only requests minus available
- [`beacon_node/network/src/network_beacon_processor/mod.rs:1141-1196`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/mod.rs#L1141-L1196) empty placeholder column with request-all for each custody column without local cells
- [`beacon_node/network/src/network_beacon_processor/mod.rs:1079`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/mod.rs#L1079) gated on enable_partial_columns (default false)

**Skeptic check.** Verified both halves of the idea for Fulu and Gloas partial columns. The whole partial-message feature is opt-in (enable_partial_columns defaults to false), as it is an experimental extension in all clients.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#9361](https://github.com/sigp/lighthouse/pull/9361), [prysm#16334](https://github.com/OffchainLabs/prysm/pull/16334), [prysm#16335](https://github.com/OffchainLabs/prysm/pull/16335)

</details>


<a id="gossipsub-087"></a>
<details>
<summary><b>gossipsub-087</b> Proposer eagerly pushes all partial column cells — <i>not · low · M · latency</i></summary>

**Idea.** When the node is the block proposer, push all partial column cells to peers eagerly instead of waiting for peer requests, to cut first-hop propagation delay.

**Gap in Lighthouse.** In partial_action_from_metadata, when metadata is None and the node is the proposer (all cells present), also send the cells (not just the header) for the first hop, behind a flag. Needs a way to mark the outgoing partial as proposer-origin from publish_blocks.

**Impact.** Cuts one round trip of first-hop propagation of column cells for blocks Lighthouse proposes; only affects proposer nodes with partial columns enabled (off by default).

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/types/partial.rs:184-203`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/partial.rs#L184-L203) with no peer metadata only the header-only message is sent
- http_api/src/publish_blocks.rs:516-545 proposer publishes full-cell partials but gossipsub only pushes cells after peer metadata arrives

**Sources.** [prysm#16571](https://github.com/OffchainLabs/prysm/pull/16571)

</details>


<a id="gossipsub-088"></a>
<details>
<summary><b>gossipsub-088</b> Send partial-column header once per peer per block — <i>implemented · low · S · bandwidth</i></summary>

**Idea.** Send the partial-column header only once per peer per block root across all columns, instead of once per column, to cut duplicate gossip bytes.

**Impact.** Already saves duplicate header bytes: one header per peer per block across all columns.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/service/partial_column_header_tracker.rs:10-27`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/partial_column_header_tracker.rs#L10-L27) LRU (4 blocks) of HeaderSentSet per block root
- [`beacon_node/lighthouse_network/src/service/mod.rs:935-941`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/mod.rs#L935-L941) same HeaderSentSet shared by every column of a block
- [`beacon_node/lighthouse_network/src/types/partial.rs:185-201`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/partial.rs#L185-L201) header sent only if header_sent_set.insert(peer_id)
- [`beacon_node/lighthouse_network/src/types/partial.rs:207-210`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/partial.rs#L207-L210) peers that show metadata are marked as knowing the header

**Skeptic check.** Verified the per-block set is shared across all column topics, matching prysm#16613. Gloas partials carry no header, so there is nothing to dedupe there.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#16613](https://github.com/OffchainLabs/prysm/pull/16613)

</details>


<a id="gossipsub-089"></a>
<details>
<summary><b>gossipsub-089</b> Skip partial column construction when disabled — <i>partial · low · S · cpu, memory</i></summary>

**Idea.** Do not build partial data column structures when partial messages are disabled, avoiding wasted CPU and memory.

**Gap in Lighthouse.** fetch_and_process_blobs_v2_or_v3 (and the v4 path via build_partial_columns_from_v4_response) build PartialDataColumn structures even when enable_partial_columns is false. For a Fulu block, a partial getBlobsV3 response still pays compute_cells for every returned blob plus partial-column construction, and import_custody_partial_columns then throws all of it away because try_into_full returns None for incomplete columns. Missing: when partials are disabled on the Fulu path, treat a partial V3/V4 response as a miss before compute_custody_columns_to_import (as the V2 branch already does).

**Impact.** Saves wasted KZG cell computation (several ms of CPU per blob) on every partial EL response when partial messages are off; this is the default config with a V3-capable EL.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_availability_checker.rs:128`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L128) assembler only created when enabled
- [`beacon_node/http_api/src/publish_blocks.rs:516`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/publish_blocks.rs#L516) to_partial gated
- [`beacon_node/network/src/network_beacon_processor/mod.rs:1079`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/mod.rs#L1079) publish_partial_data_columns gated
- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:246-265`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L246-L265) getBlobsV3 partial EL response is accepted regardless of enable_partial_columns
- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:657-700`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L657-L700) compute_custody_columns_to_import runs kzg.compute_cells and blobs_to_partial_data_columns unconditionally
- [`beacon_node/beacon_chain/src/fetch_blobs/mod.rs:346-353`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fetch_blobs/mod.rs#L346-L353) with no assembler, try_into_full drops incomplete columns
- [`beacon_node/beacon_chain/src/kzg_utils.rs:425-460`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/kzg_utils.rs#L425-L460) blobs_to_partial_data_columns

**Skeptic check.** The gossip, publish and assembler sites the earlier evidence cites are correctly gated, but the EL fetch-blobs path is partial-first and ungated, so with partials disabled it computes and discards incomplete columns.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [prysm#16593](https://github.com/OffchainLabs/prysm/pull/16593)

</details>


<a id="gossipsub-090"></a>
<details>
<summary><b>gossipsub-090</b> Do not cache partial headers for imported blocks — <i>implemented · low · S · cpu, memory, bandwidth</i></summary>

**Idea.** Ignore partial column headers for blocks already in fork choice, so the header cache is not churned and redundant regossip and slashability checks are skipped.

**Impact.** Already avoids header cache churn, regossip and redundant slashability checks for imported blocks; only matters with partial columns.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_column_verification.rs:660-682`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L660-L682) assembler.init only if !is_block_data_imported; observe_slashable only if newly_cached
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2480-2510`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2480-L2510) cached header short-circuits re-verification
- [`beacon_node/beacon_chain/src/beacon_chain.rs:3508-3510`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L3508-L3510) merge rejects fully imported blocks
- [`beacon_node/beacon_chain/src/partial_data_column_assembler.rs:255-275`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/partial_data_column_assembler.rs#L255-L275) assemblies retained until epoch maintenance

**Skeptic check.** Code matches lighthouse#9604 exactly. A small leftover: a header that first arrives after import is never cached, so each such arrival re-runs inclusion-proof and proposer-signature verification. That is an edge case beyond the idea.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#9604](https://github.com/sigp/lighthouse/pull/9604)

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

**Verdict history.** not (checked) → not (refuted)

**Sources.** [prysm#17210](https://github.com/OffchainLabs/prysm/pull/17210)

</details>


<a id="gossipsub-092"></a>
<details>
<summary><b>gossipsub-092</b> Custody all columns without all attestation subnets — <i>implemented · medium · S · bandwidth, cpu</i></summary>

**Idea.** Provide a separate option for supernodes to subscribe to all data column subnets without also subscribing to all attestation and sync-committee subnets, avoiding unneeded subnet gossip load.

**Impact.** Supernodes custody all columns without subscribing to all attestation and sync-committee subnets.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/src/config.rs:129-138`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/config.rs#L129-L138) --supernode only sets node_custody_type
- [`beacon_node/src/config.rs:1198`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/config.rs#L1198) subscribe_all_subnets set only by its own flag
- [`beacon_node/lighthouse_network/src/types/topics.rs:62-75`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/topics.rs#L62-L75) attestation and sync subnets gated on subscribe_all_subnets
- [`beacon_node/lighthouse_network/src/types/topics.rs:88-91`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/topics.rs#L88-L91) data column topics from sampling_subnets

**Skeptic check.** Confirmed the supernode flag and subscribe-all-subnets are separate, and core topic selection gates attestation/sync subnets only on the latter. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#15197](https://github.com/OffchainLabs/prysm/pull/15197), [nimbus#6764](https://github.com/status-im/nimbus-eth2/pull/6764)

</details>


<a id="gossipsub-093"></a>
<details>
<summary><b>gossipsub-093</b> Subscribe only to custody/sampling column subnets — <i>implemented · low · S · bandwidth, cpu</i></summary>

**Idea.** Subscribe only to the data column subnets the node custodies or samples rather than all column subnets, so it does not receive and validate columns it does not need (about 8 instead of 128 per slot).

**Impact.** None; only sampling column subnets are subscribed (all 128 only for supernodes, which is correct).

**Best measured result.** 128 logs per slot vs 8 needed (pr:lodestar#8181)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/types/topics.rs:87-90`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/topics.rs#L87-L90)
- [`beacon_node/lighthouse_network/src/service/mod.rs:790`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/mod.rs#L790)
- [`beacon_node/lighthouse_network/src/types/globals.rs:75-79`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/globals.rs#L75-L79)

**Skeptic check.** Verified core_topics_to_subscribe pushes DataColumnSidecar topics only for opts.sampling_subnets, and the fork-transition subscribe uses network_globals.sampling_subnets(). subscribe_all_subnets affects only attestation and sync-committee subnets. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#7607](https://github.com/ChainSafe/lodestar/pull/7607), [lodestar#7860](https://github.com/ChainSafe/lodestar/pull/7860), [lodestar#8181](https://github.com/ChainSafe/lodestar/pull/8181)

</details>


<a id="gossipsub-094"></a>
<details>
<summary><b>gossipsub-094</b> Process gossip RPC messages concurrently — <i>n/a · low · latency</i></summary>

**Idea.** Handle the messages within one gossipsub RPC concurrently instead of awaiting each validation in sequence, so a slow validation does not delay later messages such as blocks.

**Gap in Lighthouse.** Gossip RPC messages are handed to the beacon processor as separate work items and validated in worker tasks, with results reported back asynchronously; no sequential await per message inside an RPC.

**Impact.** Nothing to gain.

**Best measured result.** blocks arrived late &gt;90% of the time before (pr:lodestar#3130)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/service/mod.rs:844`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/mod.rs#L844) (publish path)
- [`beacon_node/network/src/service.rs:489`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/service.rs#L489) (libp2p events forwarded)

**Sources.** [lodestar#3130](https://github.com/ChainSafe/lodestar/pull/3130)

</details>


<a id="gossipsub-095"></a>
<details>
<summary><b>gossipsub-095</b> Yield to the scheduler during gossip processing — <i>n/a · low · latency</i></summary>

**Idea.** Split processing of large gossip RPCs into separately scheduled tasks and yield regularly, so synchronous validation does not block the network event loop and req/resp stays responsive.

**Gap in Lighthouse.** Rust gossipsub in the swarm does not run validation inline; validation runs in beacon processor workers/blocking pool, so no JS-style event loop starvation.

**Impact.** Nothing to gain.

**Best measured result.** event loop lag clearly better, incoming/outgoing request times improved (charts) (pr:lodestar#5664)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/service.rs:481-489`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/service.rs#L481-L489) (network loop only forwards events)

**Sources.** [lodestar#5316](https://github.com/ChainSafe/lodestar/pull/5316), [lodestar#5664](https://github.com/ChainSafe/lodestar/pull/5664)

</details>


<a id="gossipsub-096"></a>
<details>
<summary><b>gossipsub-096</b> Subscribe to gossip topics concurrently at startup — <i>n/a · low · startup</i></summary>

**Idea.** Issue all startup topic subscriptions concurrently rather than sequentially, shortening startup.

**Gap in Lighthouse.** Subscribe calls are synchronous in-memory swarm calls with no IO, so there is nothing to parallelize.

**Impact.** Nothing to gain.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/service.rs:742-762`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/service.rs#L742-L762) (subscribe is a synchronous call per topic)

**Sources.** [nimbus@425b0e13d](https://github.com/status-im/nimbus-eth2/commit/425b0e13dac9)

</details>


<a id="gossipsub-097"></a>
<details>
<summary><b>gossipsub-097</b> Send goodbye to peers concurrently on shutdown — <i>n/a · low · latency</i></summary>

**Idea.** On shutdown send goodbye messages to all peers concurrently, so shutdown time does not scale with peer count.

**Gap in Lighthouse.** Lighthouse does not send goodbyes to all peers on shutdown, so there is no sequential loop to make concurrent.

**Impact.** Nothing to gain.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/service/mod.rs:1994`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/mod.rs#L1994) (goodbye only on peer manager disconnect)
- [`beacon_node/network/src/service.rs:1698`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/service.rs#L1698) (shutdown just logs)

**Sources.** [prysm#15542](https://github.com/OffchainLabs/prysm/pull/15542)

</details>


<a id="gossipsub-098"></a>
<details>
<summary><b>gossipsub-098</b> Non-blocking gossip publish with backpressure — <i>n/a · low · latency</i></summary>

**Idea.** Make gossip publish non-blocking for the caller while keeping backpressure, so publishing cannot deadlock or stall the caller.

**Gap in Lighthouse.** Publish is a synchronous call on the swarm; callers send via a channel, so the Nim async deadlock does not arise.

**Impact.** Nothing to gain.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/service/mod.rs:844-880`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/mod.rs#L844-L880) (publish is a sync call inside the swarm owner task)
- [`beacon_node/network/src/service.rs:481`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/service.rs#L481) (NetworkMessage channel into the service)

**Sources.** [nimbus#1563](https://github.com/status-im/nimbus-eth2/pull/1563)

</details>


<a id="gossipsub-099"></a>
<details>
<summary><b>gossipsub-099</b> Asynchronous attestation subnet cycling — <i>n/a · low · latency</i></summary>

**Idea.** Perform attestation subnet subscription cycling asynchronously so it does not block the main event loop during slot processing.

**Gap in Lighthouse.** Subnet cycling runs in a separate subnet service task and applies cheap sync subscribe calls; no main loop blocking.

**Impact.** Nothing to gain.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/service.rs:862-869`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/service.rs#L862-L869) (subnet service sends Subscribe/Unsubscribe messages)

**Sources.** [nimbus@32a18769e](https://github.com/status-im/nimbus-eth2/commit/32a18769e6f4)

</details>


<a id="gossipsub-100"></a>
<details>
<summary><b>gossipsub-100</b> Synchronous topic subscribe/unsubscribe calls — <i>n/a · low · cpu</i></summary>

**Idea.** Make topic subscribe/unsubscribe plain synchronous calls rather than async ones, since they do no IO, removing future allocation and scheduling overhead.

**Gap in Lighthouse.** Subscribe/unsubscribe are already plain synchronous calls.

**Impact.** Nothing to gain.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/service/mod.rs:840`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/mod.rs#L840) (unsubscribe sync)
- [`beacon_node/network/src/service.rs:756`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/service.rs#L756) (subscribe returns bool, sync)

**Sources.** [nimbus#2197](https://github.com/status-im/nimbus-eth2/pull/2197)

</details>


<a id="gossipsub-101"></a>
<details>
<summary><b>gossipsub-101</b> Short 8-byte gossip message ids — <i>partial · low · S · bandwidth, memory, cpu</i></summary>

**Idea.** Derive the gossip message id from a truncated hash (first 8 bytes, no base64 encoding or padding), shrinking IHAVE/IWANT control messages and id caches.

**Gap in Lighthouse.** Id is already raw bytes with no base64, but 20 bytes not 8. The consensus spec defines the id as the first 20 bytes, so shortening to 8 would break interop with other clients.

**Impact.** Control message savings from 20-&gt;8 byte ids are tiny and not allowed by spec; effectively done.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/config.rs:495-501`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/config.rs#L495-L501) id = first 20 bytes of sha256, raw bytes via MessageId::from(&amp;[..20])

**Sources.** [prysm#7304](https://github.com/OffchainLabs/prysm/pull/7304), [lighthouse#1083](https://github.com/sigp/lighthouse/pull/1083), [lighthouse#1607](https://github.com/sigp/lighthouse/pull/1607), [lodestar#1603](https://github.com/ChainSafe/lodestar/pull/1603)

</details>


<a id="gossipsub-102"></a>
<details>
<summary><b>gossipsub-102</b> Disable gossipsub message signing — <i>implemented · low · S · cpu, bandwidth</i></summary>

**Idea.** Use anonymous/strict-no-sign gossipsub mode: do not sign published messages or verify libp2p signatures, since Ethereum messages carry their own signatures. Saves a signature and bytes per message.

**Impact.** None; no gossip signing or signature verification.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/config.rs:525`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/config.rs#L525)
- [`beacon_node/lighthouse_network/src/service/mod.rs:348`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/mod.rs#L348)

**Skeptic check.** Verified ValidationMode::Anonymous and MessageAuthenticity::Anonymous in the gossipsub config and behaviour construction. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus@e470bbb52](https://github.com/status-im/nimbus-eth2/commit/e470bbb52e97), [prysm#2339](https://github.com/OffchainLabs/prysm/pull/2339), [prysm#7093](https://github.com/OffchainLabs/prysm/pull/7093)

</details>


<a id="gossipsub-103"></a>
<details>
<summary><b>gossipsub-103</b> Optional bls_to_execution_changes topic subscription — <i>not · low · S · bandwidth, cpu</i></summary>

**Idea.** Allow disabling subscription to the bls_to_execution_changes topic, avoiding its traffic and validation when not needed.

**Gap in Lighthouse.** Add a CLI flag and an opts field checked in core_topics_to_subscribe before pushing GossipKind::BlsToExecutionChange (topics.rs core_topics_to_subscribe), and reject API publishes when off.

**Impact.** Saves a tiny amount of gossip traffic and BLS verifications; topic is near-idle on mainnet.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/types/topics.rs:83`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/topics.rs#L83) - bls_to_execution_change subscribed unconditionally from Capella
- [`beacon_node/lighthouse_network/src/service/utils.rs:286`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/utils.rs#L286) - same topic in the topic-add list

**Sources.** [teku#6786](https://github.com/Consensys-Incorporated/teku/pull/6786)

</details>


<a id="gossipsub-104"></a>
<details>
<summary><b>gossipsub-104</b> Per-topic bounded gossip work queues — <i>implemented · medium · S · cpu, latency</i></summary>

**Idea.** Give each gossip message kind its own bounded queue with tuned size in the beacon processor, so a flood on one topic drops its own work instead of starving others.

**Impact.** None; each Work kind has its own bounded queue sized by BeaconProcessorQueueLengths, and a full queue drops only its own item.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/lib.rs:765`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L765)
- [`beacon_node/beacon_processor/src/lib.rs:1292-1351`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L1292-L1351)
- [`beacon_node/beacon_processor/src/scheduler/work_queue.rs:48-59`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_queue.rs#L48-L59)
- [`beacon_node/beacon_processor/src/scheduler/work_queue.rs:135-150`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_queue.rs#L135-L150)

**Skeptic check.** Verified WorkQueues::new(queue_lengths), per-kind push, and FifoQueue/per-peer queue drop-on-full. The shared 16384-entry event channel ahead of the manager is drained fast and does not change this. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

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

**Verdict history.** not (checked) → not (refuted)

**Sources.** [lodestar#3554](https://github.com/ChainSafe/lodestar/pull/3554)

</details>


<a id="gossipsub-106"></a>
<details>
<summary><b>gossipsub-106</b> Separate queue for subnet subscription messages — <i>implemented · low · S · latency</i></summary>

**Idea.** Route attestation and sync-committee subscription requests to the network service on their own channel, separate from the main command channel, so a subscription flood cannot starve req/resp.

**Impact.** Already done; subscription floods cannot fill the main network message queue.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/service.rs:164-197`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/service.rs#L164-L197) NetworkSenders has a bounded validator_subscription channel separate from the unbounded network_send
- [`beacon_node/network/src/service.rs:480-484`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/service.rs#L480-L484) separate select! arm for validator_subscription_recv
- [`beacon_node/http_api/src/lib.rs:460`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L460) and http_api/src/validator/mod.rs:661-679,1158-1179 API subscription endpoints send on validator_subscription_tx

**Skeptic check.** Verified the dedicated bounded channel and that both attestation and sync-committee subscription endpoints use it. Earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#3508](https://github.com/sigp/lighthouse/pull/3508)

</details>


<a id="gossipsub-107"></a>
<details>
<summary><b>gossipsub-107</b> Native networking runtime with bounded budgets — <i>n/a · low · L · memory, cpu, latency</i></summary>

**Idea.** Run socket, QUIC and gossip admission in a dedicated native runtime with bounded per-kind item and byte budgets that stay charged until the work retires, bounding memory under load.

**Impact.** Idea is a Node.js native-runtime offload; Lighthouse already runs networking in Rust/tokio without a JS event loop to protect.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/service.rs:473-500`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/service.rs#L473-L500) - network runs as a normal tokio task; libp2p swarm

**Sources.** [lodestar#10375](https://github.com/ChainSafe/lodestar/pull/10375)

</details>


<a id="gossipsub-108"></a>
<details>
<summary><b>gossipsub-108</b> Synchronize read buffer once per read — <i>n/a · low · L · cpu</i></summary>

**Idea.** In the network read path, synchronize buffer state once per read call rather than once per byte.

**Impact.** Nim async-stream per-byte buffer sync has no counterpart in Rust tokio/libp2p buffers.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/rpc/codec.rs:188`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/codec.rs#L188) - read via tokio_util codec on BytesMut, no per-byte sync

**Sources.** [nimbus#1567](https://github.com/status-im/nimbus-eth2/pull/1567)

</details>


<a id="gossipsub-109"></a>
<details>
<summary><b>gossipsub-109</b> No zero-init for network read buffers — <i>partial · low · S · cpu</i></summary>

**Idea.** Allocate network read buffers without zero-initializing them when they are immediately overwritten.

**Gap in Lighthouse.** RPC decode buffers are zero-initialised with vec![0; length] before read_exact (codec.rs:188,283,319); calloc makes this nearly free, so only a marginal gain remains.

**Impact.** Negligible: calloc'd pages are lazily zeroed; at most a memset on multi-MB blocks/blob RPC responses.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/rpc/codec.rs:188`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/codec.rs#L188) - vec![0; length] for decoded buffer then read_exact overwrites it
- [`beacon_node/lighthouse_network/src/types/pubsub.rs:122`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/pubsub.rs#L122) - decompress_vec allocates output (snap handles init)

**Sources.** [nimbus#5178](https://github.com/status-im/nimbus-eth2/pull/5178)

</details>


<a id="gossipsub-110"></a>
<details>
<summary><b>gossipsub-110</b> Plumtree epidemic broadcast gossip — <i>not · low · L · bandwidth</i></summary>

**Idea.** Use an epidemic broadcast tree: eager push along a spanning tree and lazy announcements to other peers, to cut duplicate deliveries.

**Gap in Lighthouse.** Would need a Plumtree implementation in rust-libp2p gossipsub and a spec/network-wide change; not interoperable with other clients' meshes.

**Impact.** Could cut duplicate deliveries but the network-wide protocol is gossipsub v1.1; a unilateral change is not viable. Gossipsub v1.2 IDONTWANT already reduces duplicates.

**Evidence (Lighthouse @ 928b61e719).**

- Cargo.lock:5870 - libp2p-gossipsub 0.51.0 is plain mesh gossipsub (eager mesh + IHAVE/IWANT)
- [`beacon_node/lighthouse_network/src/service/utils.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/utils.rs) - gossipsub config, no tree mode

**Sources.** [teku#562](https://github.com/Consensys-Incorporated/teku/pull/562)

</details>


<a id="gossipsub-111"></a>
<details>
<summary><b>gossipsub-111</b> Snappy block format for gossip, framed for RPC — <i>implemented · low · S · cpu, bandwidth</i></summary>

**Idea.** Use snappy block compression for single gossip messages and the framed format only for req/resp streams, since block format is cheaper for small whole messages.

**Impact.** None left; the spec requires this split and Lighthouse follows it.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/types/pubsub.rs:6`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/pubsub.rs#L6) snap::raw Decoder/Encoder
- [`beacon_node/lighthouse_network/src/types/pubsub.rs:106-131`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/pubsub.rs#L106-L131) inbound_transform uses raw block decompress_vec
- [`beacon_node/lighthouse_network/src/rpc/codec.rs:8-9`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/codec.rs#L8-L9),127,187,389 FrameEncoder/FrameDecoder for req/resp

**Skeptic check.** Verified that gossip uses snap::raw block format in SnappyTransform and RPC uses the snap frame format in the codec. Earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#5435](https://github.com/OffchainLabs/prysm/pull/5435)

</details>


<a id="gossipsub-112"></a>
<details>
<summary><b>gossipsub-112</b> No separate attestation announcement before gossip — <i>n/a · low · S · bandwidth</i></summary>

**Idea.** Do not send a separate announcement message for attestations before gossiping them; rely on gossip alone.

**Impact.** Lighthouse has no separate attestation announcement message; attestations go through gossipsub only.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/types/pubsub.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/pubsub.rs) - only gossip PubsubMessage variants; no attestation announce message exists

**Sources.** [prysm#3165](https://github.com/OffchainLabs/prysm/pull/3165)

</details>


<a id="gossipsub-113"></a>
<details>
<summary><b>gossipsub-113</b> Rely on gossipsub dedup, drop app-level seen cache — <i>implemented · low · S · memory, cpu</i></summary>

**Idea.** Remove application-level seen-message tables/LRUs for gossip ids and rely on the gossipsub duplicate cache, avoiding duplicate memory and lookups.

**Impact.** None left; gossip message-id dedup is done only in the gossipsub duplicate cache.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/config.rs:507`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/config.rs#L507),526 duplicate_cache_time set on gossipsub config
- rust-libp2p accba72 protocols/gossipsub/src/behaviour.rs:1985 duplicate_cache.insert drops repeats before app delivery

**Skeptic check.** Grep of lighthouse_network and network finds no app-level LRU keyed by gossip message id; the remaining LRUs are sync/discovery caches, and the beacon_chain observed_* caches are semantic (per validator/slot), not message-id dedup. Earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#713](https://github.com/Consensys-Incorporated/teku/pull/713), [lighthouse#1324](https://github.com/sigp/lighthouse/pull/1324)

</details>


<a id="gossipsub-114"></a>
<details>
<summary><b>gossipsub-114</b> Dispatch network events directly to processor — <i>implemented · low · S · latency, cpu</i></summary>

**Idea.** Send inbound network events straight to the beacon processor and sync manager without re-wrapping them into a second enum and router task, removing a channel hop per event.

**Impact.** None left; the router task and its channel hop are gone.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/service.rs:517-580`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/service.rs#L517-L580) on_libp2p_event matches NetworkEvent and calls handle_gossip/handle_rpc_request/send_to_sync inline
- [`beacon_node/network/src`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src)/ (no router.rs; no RouterMessage anywhere)

**Skeptic check.** Verified that there is no router module and no RouterMessage type, and that the network service dispatches events straight to the processor and sync. Earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#10122](https://github.com/sigp/lighthouse/pull/10122), [silver#140](https://github.com/gattaca-com/silver/pull/140)

</details>


<a id="gossipsub-115"></a>
<details>
<summary><b>gossipsub-115</b> Timeout on incoming gossip buffer reservations — <i>n/a · low · latency, memory</i></summary>

**Idea.** Time out a reserved receive buffer if the peer never sends the payload, so one slow peer cannot block processing of later gossip.

**Impact.** Silver-specific reserved-buffer design; libp2p gossipsub reads whole messages from the stream, so there is no reservation to time out.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/service/mod.rs:2046`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/mod.rs#L2046) swarm polled via libp2p

**Sources.** [silver#165](https://github.com/gattaca-com/silver/pull/165)

</details>


<a id="gossipsub-116"></a>
<details>
<summary><b>gossipsub-116</b> Non-sequential gossip consumption and bigger socket buffers — <i>n/a · low · latency</i></summary>

**Idea.** Consume incoming gossip with random access instead of a strictly sequential queue and enlarge socket buffers, so one slow message does not block those behind it.

**Impact.** Applies to Silver's custom gossip stack; Lighthouse uses libp2p gossipsub with per-connection handlers, no sequential shared queue.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/service/mod.rs:2046`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/mod.rs#L2046) libp2p swarm

**Sources.** [silver#169](https://github.com/gattaca-com/silver/pull/169)

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

**Verdict history.** not (checked) → not (refuted)

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


<a id="gossipsub-119"></a>
<details>
<summary><b>gossipsub-119</b> Strict read/write timeouts on req/resp handlers — <i>implemented · low · S · memory</i></summary>

**Idea.** Apply strict read/write timeouts to p2p request handlers so stalled streams release buffers sooner.

**Impact.** Marginal; a lower timeout value would free stalled-stream buffers a few seconds sooner.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/rpc/handler.rs:44`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/handler.rs#L44) RESP_TIMEOUT 10s
- [`beacon_node/lighthouse_network/src/rpc/handler.rs:414-436`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/handler.rs#L414-L436) expired inbound substreams removed at once
- [`beacon_node/lighthouse_network/src/rpc/handler.rs:438-458`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/handler.rs#L438-L458) expired outbound substreams removed
- [`beacon_node/lighthouse_network/src/rpc/handler.rs:543-545`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/handler.rs#L543-L545),710-711 per-chunk timer reset
- [`beacon_node/lighthouse_network/src/rpc/protocol.rs:132`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/protocol.rs#L132),808-812 15s timeout on inbound request read

**Skeptic check.** Verified the request read has a timeout, each response chunk has a 10s timer on inbound and outbound substreams, and expired streams are dropped right away. The libp2p SubstreamProtocol default upgrade timeout also applies. Earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [caplin#16719](https://github.com/erigontech/erigon/pull/16719)

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

**Verdict history.** not (checked) → not (refuted)

**Sources.** [prysm#16130](https://github.com/OffchainLabs/prysm/pull/16130), [prysm#16183](https://github.com/OffchainLabs/prysm/pull/16183)

</details>


<a id="gossipsub-121"></a>
<details>
<summary><b>gossipsub-121</b> Drive the swarm with an async select loop — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Drive the libp2p swarm from an async select loop rather than a hand-written poll, avoiding missed wakeups and busy polling.

**Impact.** None left.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/service/mod.rs:2044-2049`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/mod.rs#L2044-L2049) next_event uses tokio::select! over self.swarm.next()

**Skeptic check.** Verified that next_event is an async select loop over the swarm stream, with no hand-written poll. Earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#6550](https://github.com/sigp/lighthouse/pull/6550)

</details>


<a id="gossipsub-122"></a>
<details>
<summary><b>gossipsub-122</b> Runtime-native timer for gossipsub heartbeat — <i>not · low · S · cpu, latency</i></summary>

**Idea.** Drive the gossipsub heartbeat from the async runtime's interval timer rather than a custom polling timer, so it fires on schedule at lower CPU cost.

**Gap in Lighthouse.** The gossipsub heartbeat in the pinned libp2p fork still uses futures_timer::Delay (behaviour.rs:342,480); switching it to tokio::time::interval means editing the sigp/rust-libp2p fork and bumping the rev in Cargo.toml.

**Impact.** Heartbeat fires once per second so CPU saving is negligible; only the scheduling accuracy would change.

**Evidence (Lighthouse @ 928b61e719).**

- Cargo.toml:177 sigp/rust-libp2p rev accba72
- ~/.cargo/git/checkouts/rust-libp2p-b7fa834aec8fc27c/accba72/protocols/gossipsub/src/behaviour.rs:34 heartbeat uses futures_timer::Delay, not tokio interval

**Sources.** [lighthouse#3012](https://github.com/sigp/lighthouse/pull/3012)

</details>


<a id="gossipsub-123"></a>
<details>
<summary><b>gossipsub-123</b> Fastest AEAD/hash backend for noise transport — <i>implemented · low · S · cpu</i></summary>

**Idea.** Use the fastest available chacha20poly1305 and sha256 implementations for the noise transport (chosen by payload size where needed) and reuse the ciphertext buffer, since noise encryption runs on every byte sent.

**Impact.** None; noise uses ring's assembly ChaCha20-Poly1305/SHA-256 and reuses the encrypt buffer.

**Best measured result.** chacha20poly1305Decrypt was ~10% of CPU, now 3.4% (pr:lodestar#4787)

**Evidence (Lighthouse @ 928b61e719).**

- Cargo.lock:5991-6005
- Cargo.lock:9481-9494
- accba72/transports/noise/Cargo.toml:28
- accba72/transports/noise/src/io/framed.rs:52-61
- accba72/transports/noise/src/io/framed.rs:169-180

**Skeptic check.** Verified libp2p-noise (sigp fork) depends on snow 0.10 with ring-resolver, and Codec keeps a reusable encrypt_buffer (the buffer-reuse part the earlier check left unverified).

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#5900](https://github.com/ChainSafe/lodestar/pull/5900), [lodestar#4787](https://github.com/ChainSafe/lodestar/pull/4787)

</details>


<a id="gossipsub-124"></a>
<details>
<summary><b>gossipsub-124</b> No gossip validation or relay before genesis — <i>not · low · S · cpu</i></summary>

**Idea.** Do not validate or relay gossip messages before chainstart/genesis, when they cannot be verified.

**Gap in Lighthouse.** Would need a check in the gossip handler or the topic subscription path in NetworkService to skip validation before genesis time.

**Impact.** Only matters for nodes started before genesis on a new network; no effect on mainnet.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/service.rs:887`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/service.rs#L887) only slot-clock fallback to genesis slot
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs): no pre-genesis gate found

**Sources.** [prysm#7494](https://github.com/OffchainLabs/prysm/pull/7494)

</details>


<a id="gossipsub-125"></a>
<details>
<summary><b>gossipsub-125</b> Reject undecompressable gossip before id and caching — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Reject messages that fail snappy decompression immediately, without computing ids or storing them in the message-id path.

**Impact.** None left.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/types/pubsub.rs:106-125`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/pubsub.rs#L106-L125) size and decompress_len checks before decompression
- rust-libp2p accba72 protocols/gossipsub/src/behaviour.rs:1934-1945 transform error -&gt; handle_invalid_message(None) and return
- rust-libp2p accba72 protocols/gossipsub/src/behaviour.rs:1948 message_id computed only after a successful transform
- rust-libp2p accba72 protocols/gossipsub/src/behaviour.rs:1985 duplicate cache insert after that

**Skeptic check.** Verified in handle_received_message that a failed snappy transform returns before message_id, IDONTWANT and the duplicate cache. Earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#3471](https://github.com/status-im/nimbus-eth2/pull/3471)

</details>


<a id="gossipsub-126"></a>
<details>
<summary><b>gossipsub-126</b> Drop self-originated gossip before validation — <i>implemented · low · S · cpu</i></summary>

**Idea.** Drop gossip messages whose source is the local node before validation, since they were handled when produced.

**Impact.** Echoes of own messages never reach app validation; only decompression and the id hash remain, which the id needs.

**Evidence (Lighthouse @ 928b61e719).**

- rust-libp2p accba72 protocols/gossipsub/src/behaviour.rs:650-655,701 publish() computes msg id and inserts it into duplicate_cache
- rust-libp2p accba72 protocols/gossipsub/src/behaviour.rs:1985-1992 echoed copy dropped as duplicate before delivery to the app
- [`beacon_node/lighthouse_network/src/config.rs:525`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/config.rs#L525),528 Anonymous validation, allow_self_origin(true)

**Skeptic check.** Verified that publish puts the id into the duplicate cache when there are recipients, so an echo is dropped in gossipsub before Lighthouse validation. With Anonymous mode there is no source field to filter on, so dedup is the right mechanism. Earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#4337](https://github.com/OffchainLabs/prysm/pull/4337)

</details>


<a id="gossipsub-127"></a>
<details>
<summary><b>gossipsub-127</b> Do not regossip RPC-reconstructed columns — <i>implemented · low · S · bandwidth</i></summary>

**Idea.** Do not republish data columns reconstructed from RPC-fetched columns to gossip, since peers already have them and old-slot columns cause downscoring.

**Impact.** None left; RPC-fetched columns never trigger reconstruction or republish.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1490-1520`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1490-L1520) the gossip column path is the only scheduler of attempt_data_column_reconstruction
- [`beacon_node/network/src/network_beacon_processor/mod.rs:1213-1217`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/mod.rs#L1213-L1217) reconstruction then publish_data_columns_gradually
- [`beacon_node/beacon_chain/src/data_availability_checker.rs:537`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L537) reconstruct_data_columns (no RPC-side caller)

**Skeptic check.** PR 7409 added a publish_columns=false flag on the sync path. Current code removed RPC-triggered reconstruction entirely, which is a stronger form of the same fix. Reconstruction runs only from gossip columns, which are current-slot by gossip validation. Earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#7409](https://github.com/sigp/lighthouse/pull/7409)

</details>


<a id="gossipsub-128"></a>
<details>
<summary><b>gossipsub-128</b> Zero-copy byte handling in message-id computation — <i>not · low · S · cpu, memory</i></summary>

**Idea.** When computing gossip message ids, use views/zero-copy casts of the input and hash bytes instead of copying them, since thousands of ids are computed per slot.

**Gap in Lighthouse.** In gossip_message_id replace prefix() Vec building with Sha256::new() and update() on prefix, topic length, topic bytes and message.data, then finalize and take 20 bytes. Removes one full-payload memcpy and allocation per received message.

**Impact.** One memcpy plus alloc per inbound gossip message; memcpy is much cheaper than the SHA-256 that follows, so a few percent of id cost at best.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/config.rs:467-496`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/config.rs#L467-L496) prefix() allocates a Vec and copies topic+data before Sha256::digest at :498-503

**Sources.** [lodestar#4342](https://github.com/ChainSafe/lodestar/pull/4342), [prysm#14591](https://github.com/OffchainLabs/prysm/pull/14591)

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


<a id="gossipsub-130"></a>
<details>
<summary><b>gossipsub-130</b> Subscribe to next-fork topics just before the fork — <i>implemented · low · S · bandwidth, cpu</i></summary>

**Idea.** Keep per-fork core topic lists and subscribe to a new fork's topics only about 2 slots before the fork, not long in advance, so no mesh upkeep or traffic is spent on empty topics.

**Impact.** Next-fork topics are subscribed only one epoch before the fork, not long in advance. The window is 1 epoch, not the 2 slots of PR 4030; this looks like a deliberate change for mesh formation.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/service.rs:60`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/service.rs#L60) SUBSCRIBE_DELAY_EPOCHS=1
- [`beacon_node/network/src/service.rs:452`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/service.rs#L452) required_gossip_fork_digests adds next digest only within SUBSCRIBE_DELAY_EPOCHS
- [`beacon_node/network/src/service.rs:498-504`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/service.rs#L498-L504) timer fires subscribe_new_fork_topics
- [`beacon_node/network/src/service.rs:1673-1680`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/service.rs#L1673-L1680) duration_to_next_topic_subscriptions
- [`beacon_node/lighthouse_network/src/service/mod.rs:726-745`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/mod.rs#L726-L745) subscribe_new_fork_topics uses per-fork core_topics_to_subscribe

**Skeptic check.** Verified the timer-driven subscribe and the per-fork core topic list. The earlier evidence was right; the only difference is the lead time (1 epoch, not 2 slots), and it is a deliberate tuning choice, not a missing mechanism.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#4030](https://github.com/sigp/lighthouse/pull/4030)

</details>


<a id="gossipsub-131"></a>
<details>
<summary><b>gossipsub-131</b> Transfer gossip buffers between threads without copy — <i>n/a · low · S · memory, cpu</i></summary>

**Idea.** Move gossip message buffers from the network thread to the processing thread by ownership transfer rather than cloning, cutting GC/allocation on both sides.

**Impact.** Rust has no GC and moves messages by ownership; the idea targets JS worker-thread transfer. Only a minor related copy exists in gossipsub (raw_message.clone() before transform).

**Best measured result.** GC on network thread lower than stable (1% / 3.35% baselines) (pr:lodestar#8638)

**Evidence (Lighthouse @ 928b61e719).**

- accba72/protocols/gossipsub/src/behaviour.rs:1934 raw_message.clone() copies compressed payload, within one thread

**Sources.** [lodestar#8638](https://github.com/ChainSafe/lodestar/pull/8638), [lodestar#8689](https://github.com/ChainSafe/lodestar/pull/8689), [silver#4](https://github.com/gattaca-com/silver/pull/4)

</details>


<a id="gossipsub-132"></a>
<details>
<summary><b>gossipsub-132</b> Queue unknown-block attestations on the network thread — <i>n/a · low · S · latency, cpu</i></summary>

**Idea.** Hold gossip attestations whose block root is unknown in a queue on the network thread, off the main processing thread, to cut main-thread congestion.

**Impact.** Lighthouse already parks unknown-block attestations in a dedicated reprocessing queue task; the JS main-thread congestion does not exist.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:132`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L132),291,844 ReprocessQueue with UnknownBlockUnaggregate, cap 16384 at :84

**Sources.** [lodestar#7189](https://github.com/ChainSafe/lodestar/pull/7189)

</details>


<a id="gossipsub-133"></a>
<details>
<summary><b>gossipsub-133</b> Cache attached validators to derive subnet subscriptions — <i>implemented · low · S · cpu, bandwidth</i></summary>

**Idea.** Keep a cache of validators attached to the node, filled from committee-subscription calls and pruned on finalization or expiry, and derive subnet subscriptions from it instead of recomputing the subnet per slot or committee.

**Impact.** No per-slot subnet recomputation; subscription state is derived from VC calls and pruned by expiry.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/subnet_service/mod.rs:219-260`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/subnet_service/mod.rs#L219-L260) validator_subscriptions computes the subnet once per subscription from the HTTP API call
- [`beacon_node/network/src/subnet_service/mod.rs:79-98`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/subnet_service/mod.rs#L79-L98) subscriptions, scheduled_subscriptions and aggregate_validators_on_subnet are HashSetDelay sets that expire entries

**Skeptic check.** Lighthouse has no explicit attached-validator cache, but the subnet service stores computed subnets with expiry timers, giving the same effect (no per-slot or per-committee recompute). Earlier verdict upheld on effect, not on mechanism.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#1450](https://github.com/ChainSafe/lodestar/pull/1450), [lodestar#2427](https://github.com/ChainSafe/lodestar/pull/2427)

</details>


<a id="gossipsub-134"></a>
<details>
<summary><b>gossipsub-134</b> Parse gossip topics cheaply without regex or exceptions — <i>implemented · low · S · cpu</i></summary>

**Idea.** Parse incoming gossip topic strings by splitting or looking them up in a parsed-topic cache, and treat unknown topics as a plain miss rather than a regex match or a thrown and caught error.

**Gap in Lighthouse.** Minor: decode allocates a Vec and hex-decodes the fork digest for each message; no topic-hash to GossipTopic cache.

**Impact.** Negligible; microseconds per gossip message.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/types/topics.rs:265-315`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/topics.rs#L265-L315) GossipTopic::decode uses split('/') and string match, returns Err for unknown topics
- [`beacon_node/lighthouse_network/src/types/pubsub.rs:200`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/pubsub.rs#L200) decode once per message

**Skeptic check.** Verified no regex and no panic/exception path; unknown topic is a plain Err. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#3881](https://github.com/ChainSafe/lodestar/pull/3881), [lodestar#2589](https://github.com/ChainSafe/lodestar/pull/2589)

</details>


<a id="gossipsub-135"></a>
<details>
<summary><b>gossipsub-135</b> Gossip-only block body without unneeded fields — <i>n/a · low · bandwidth</i></summary>

**Idea.** Use a gossip-specific block body type that omits fields receivers do not need, such as execution requests, to shrink block messages on the wire.

**Impact.** The gossip block type is fixed by the consensus spec (open spec issue); Lighthouse cannot change the wire type unilaterally, and the requests are usually empty.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/block/beacon_block_body.rs:242`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/block/beacon_block_body.rs#L242) Gloas body carries parent_execution_requests; gossip type is the spec type

**Sources.** [prysm#16729](https://github.com/OffchainLabs/prysm/pull/16729)

</details>


<a id="gossipsub-136"></a>
<details>
<summary><b>gossipsub-136</b> One random long-lived subnet per attached validator — <i>n/a · low · bandwidth</i></summary>

**Idea.** Give each attached validator a single random long-lived attestation subnet so subscriptions grow with validator count in a bounded way, not a larger fixed set.

**Impact.** Spec replaced random per-validator stability subnets with node-id derived subnets (fixed count); the nimbus change was reverted and does not apply.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/subnet_service/mod.rs:126-140`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/subnet_service/mod.rs#L126-L140) permanent subnets derived from node_id via compute_attestation_subnets

**Sources.** [nimbus#2194](https://github.com/status-im/nimbus-eth2/pull/2194)

</details>


<a id="gossipsub-137"></a>
<details>
<summary><b>gossipsub-137</b> Publish column sidecars only when self-building — <i>implemented · low · S · bandwidth</i></summary>

**Idea.** Publish data column sidecars only when the proposer built the payload itself, not when a builder supplies it, to avoid redundant publication.

**Impact.** Builder-supplied payloads do not cause column publication by the proposer node.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/publish_blocks.rs:656-682`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/publish_blocks.rs#L656-L682) publish_blinded_block returns without publishing when the builder accepted the blinded block
- [`beacon_node/http_api/src/publish_blocks.rs:722-736`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/publish_blocks.rs#L722-L736) reconstruct_block submits to builder and returns Ok(None), so no columns are built or published
- [`beacon_node/http_api/src/publish_blocks.rs:168-174`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/publish_blocks.rs#L168-L174) Gloas: fetch_columns skipped when self-built payload columns come from the envelope path
- [`beacon_node/http_api/src/publish_blocks.rs:434-450`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/publish_blocks.rs#L434-L450) spawn_build_data_sidecar_task builds columns only when blobs are supplied (local build)

**Skeptic check.** Verified the mev-boost path returns after submitting to the builder and only locally built blocks carry blobs into column building. Earlier evidence was right, and the blinded path adds to it.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [grandine@eb86597c2](https://github.com/grandinetech/grandine/commit/eb86597c2728)

</details>


<a id="gossipsub-138"></a>
<details>
<summary><b>gossipsub-138</b> Enforce peer bans in the swarm layer — <i>implemented · low · S · cpu, bandwidth</i></summary>

**Idea.** Drop banned peers in the swarm layer and refuse their future handshakes, so redialing banned peers does not cost the crypto and protocol handshake.

**Impact.** Banned peers are refused in the swarm and not redialed; peer-id-only bans can only be checked after the crypto handshake.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/peer_manager/network_behaviour.rs:156-180`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/network_behaviour.rs#L156-L180) handle_pending_inbound_connection rejects banned IPs before the handshake
- [`beacon_node/lighthouse_network/src/peer_manager/network_behaviour.rs:182-196`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/network_behaviour.rs#L182-L196),229-234 established-connection ban_status checks for peer ids
- [`beacon_node/lighthouse_network/src/peer_manager/peerdb.rs:153-160`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/peerdb.rs#L153-L160) should_dial excludes banned peers so they are not redialed
- [`beacon_node/lighthouse_network/src/discovery/mod.rs:634-642`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/discovery/mod.rs#L634-L642) ban_peer also bans node id and IPs in discv5

**Skeptic check.** Lighthouse's own PR; verified inbound IP pre-handshake reject, peer-id reject on establishment, and outbound dial filtering. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#2442](https://github.com/sigp/lighthouse/pull/2442)

</details>


