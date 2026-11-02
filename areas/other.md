# other

22 ideas: 2 not, 3 partial, 12 implemented, 5 n/a; 1 actionable (high or medium value, verdict `not` or `partial`). [Back to the summary](../README.md).

Ids missing from the sequence are ideas that have not been checked against Lighthouse yet.

| id | idea | verdict | value | effort | resources |
|---|---|---|---|---|---|
| [other-001](#other-001) | Slasher bloom filter of data root for double votes | partial | low | M | cpu, memory, disk |
| [other-002](#other-002) | Keep slasher span data cached in memory | partial | low | M | cpu, memory, disk, latency |
| [other-003](#other-003) | Aggregate lazy min-max surround detection | not | low | L | disk |
| [other-014](#other-014) | Slasher DB access in fewer transactions | implemented | low |  | cpu, memory, disk |
| [other-017](#other-017) | Fast integer square root | implemented | low |  | cpu |
| [other-019](#other-019) | Cold-start span init over history length only | implemented | low |  | startup, cpu |
| [other-028](#other-028) | Chunked min/max span storage for surround detection | implemented | low |  | cpu, disk, memory |
| [other-031](#other-031) | Compare state roots instead of deep state equality | n/a | low |  | startup, disk, cpu |
| [other-036](#other-036) **★** | Light client finality update only on finality change | partial | medium | S | cpu, bandwidth |
| [other-040](#other-040) | Move end-of-slot housekeeping earlier in the slot | implemented | medium |  | latency |
| [other-056](#other-056) | Fork-neutral slasher on-disk attestation format | implemented | medium |  | disk |
| [other-058](#other-058) | Tick delay computed relative to genesis | implemented | low |  | latency |
| [other-059](#other-059) | Allocation-free slasher span serialization | not | low | S | cpu, memory |
| [other-078](#other-078) | Raw key lists instead of encoded slasher index | implemented | low |  | cpu, disk |
| [other-079](#other-079) | Re-tick immediately after long duty handler | n/a | low |  | latency |
| [other-085](#other-085) | Restart from DB state, skip network fetch | implemented | medium |  | startup, bandwidth |
| [other-087](#other-087) | Static error construction without formatting | n/a | low |  | cpu |
| [other-088](#other-088) | Slasher writes only touched validators per batch | implemented | medium | S | cpu, memory, disk, latency |
| [other-089](#other-089) | Slasher accepts only verified, bounded attestations | implemented | medium |  | memory |
| [other-093](#other-093) | Stack buffer for deterministic randomness seed | n/a | low |  | cpu, memory |
| [other-095](#other-095) | Word-wide is-zero check for hashes | implemented | low |  | cpu |
| [other-096](#other-096) | Debug state dumps only for failed blocks | n/a | low |  | disk |

★ actionable. Click an id for the full record.

## Ideas

<a id="other-001"></a>
<details>
<summary><b>other-001</b> Slasher bloom filter of data root for double votes — <i>partial · low · M · cpu, memory, disk</i></summary>

**Idea.** In the slasher, store a tiny (about 2-byte) bloom filter of the attestation data root per validator and target epoch, inside the span entry, so double votes are detected without storing or loading full attestations. False positives are rare and are confirmed with a full lookup.

**Gap in Lighthouse.** Lighthouse reaches the same goal differently: the compact record is an id and the data root comes from an LRU (attestation_root_cache); a cache miss costs one indexed-attestation load. A 2-byte bloom filter in the span entry would only avoid those misses.

**Impact.** Negligible; misses are rare because the LRU is primed with each batch's roots. Only affects slasher users.

**Best measured result.** None (pr:prysm#4948)

**Evidence (Lighthouse @ 928b61e719).**

- [`slasher/src/database.rs:595`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/database.rs#L595) check_and_update_attester_record stores a compact per-validator/target-epoch record (indexed attestation id) in attesters_db
- [`slasher/src/database.rs:559`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/database.rs#L559) LRU cache of attestation data roots avoids loading full attestations

**Sources.** [prysm#4948](https://github.com/OffchainLabs/prysm/pull/4948), [prysm#4954](https://github.com/OffchainLabs/prysm/pull/4954)

</details>


<a id="other-002"></a>
<details>
<summary><b>other-002</b> Keep slasher span data cached in memory — <i>partial · low · M · cpu, memory, disk, latency</i></summary>

**Idea.** Keep recently used slasher min/max span data in an in-memory cache (LRU or a compact array over a recent epoch window), lazily load it, and write it to the DB only on eviction or shutdown, so detection does not save and load spans from disk on every attestation.

**Gap in Lighthouse.** Spans are loaded and written per batch (amortised over all attestations in the batch, not per attestation as in old Prysm), but there is no cache persisting chunks across batches. Add an LRU of chunks in SlasherDB used by get_chunk_for_update and flushed on eviction/shutdown.

**Impact.** Cuts chunk read/decompress and write per slasher batch; modest, and only for --slasher nodes. Write-back risks crash consistency.

**Best measured result.** None (pr:prysm#4388)

**Evidence (Lighthouse @ 928b61e719).**

- [`slasher/src/array.rs:397`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/array.rs#L397) get_chunk_for_update loads each chunk once per batch from DB and stores at the end of the batch
- [`slasher/src/database.rs:76`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/database.rs#L76) only an attestation-root LRU exists, no cross-batch span cache

**Sources.** [prysm#4388](https://github.com/OffchainLabs/prysm/pull/4388), [prysm#6455](https://github.com/OffchainLabs/prysm/pull/6455), [prysm#4920](https://github.com/OffchainLabs/prysm/pull/4920)

</details>


<a id="other-003"></a>
<details>
<summary><b>other-003</b> Aggregate lazy min-max surround detection — <i>not · low · L · disk</i></summary>

**Idea.** Detect possible surround votes with one aggregate min-max of source/target epochs across all attestations (constant size, about 65KB) instead of per-validator min/max span arrays, and scan historical blocks only when the aggregate flags a possible surround. This replaces gigabytes of slasher storage.

**Gap in Lighthouse.** Would need a new aggregate min/max surround prefilter in slasher plus a historical block scan fallback; a redesign of Slasher::process_batch.

**Impact.** Slasher is opt-in and few nodes run it; would save slasher disk (GBs) not normal node cost.

**Best measured result.** None (pr:lodestar#8873)

**Evidence (Lighthouse @ 928b61e719).**

- [`slasher/src/array.rs:140`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/array.rs#L140) per-validator chunked min/max spans (MinTargetChunk/MaxTargetChunk) are the only surround detector

**Sources.** [lodestar#8873](https://github.com/ChainSafe/lodestar/pull/8873), [lodestar#8874](https://github.com/ChainSafe/lodestar/pull/8874)

</details>


<a id="other-014"></a>
<details>
<summary><b>other-014</b> Slasher DB access in fewer transactions — <i>implemented · low · cpu, memory, disk</i></summary>

**Idea.** Batch slasher DB reads and writes into few large transactions (and run span detection concurrently with one put per detection) instead of one transaction per attestation, so a slot's attestations are processed within the slot and the queue does not grow.

**Impact.** Already batched into one transaction per update period; concurrency of span detection not done but minor.

**Best measured result.** None (pr:prysm#13629)

**Evidence (Lighthouse @ 928b61e719).**

- [`slasher/src/slasher.rs:94-97`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/slasher.rs#L94-L97) one rw txn per processing batch covering blocks and attestations
- [`slasher/src/slasher.rs:196`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/slasher.rs#L196) process_batch groups attestations by validator chunk

**Sources.** [prysm#4172](https://github.com/OffchainLabs/prysm/pull/4172), [prysm#13629](https://github.com/OffchainLabs/prysm/pull/13629)

</details>


<a id="other-017"></a>
<details>
<summary><b>other-017</b> Fast integer square root — <i>implemented · low · cpu</i></summary>

**Idea.** Compute integer square root (used for base reward per epoch) with a fast method such as binary search or a native isqrt, instead of the slow iterative spec method.

**Impact.** sqrt of total active balance is computed once per epoch (cached); the crate uses a fast bitwise method, negligible cost.

**Best measured result.** None (pr:prysm#3785)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/common/base.rs:12`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/common/base.rs#L12) integer_sqrt from integer-sqrt 0.1.5 crate, bit-shift Newton-free method O(bits)
- [`consensus/state_processing/src/epoch_cache.rs:197`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/epoch_cache.rs#L197) value cached

**Sources.** [prysm#3785](https://github.com/OffchainLabs/prysm/pull/3785)

</details>


<a id="other-019"></a>
<details>
<summary><b>other-019</b> Cold-start span init over history length only — <i>implemented · low · startup, cpu</i></summary>

**Idea.** On a slasher cold start with no DB, initialise the min/max span arrays by looping only over the circular-buffer history length instead of every epoch since genesis, because older cells are overwritten anyway. Boot goes from O(epochs*validators) to O(validators).

**Impact.** No cold-start initialisation over epochs since genesis exists; boot is O(1).

**Best measured result.** None (pr:prysm#13620)

**Evidence (Lighthouse @ 928b61e719).**

- [`slasher/src/array.rs:150`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/array.rs#L150) chunks loaded lazily, missing chunk gives None and empty() chunk is created on demand
- [`slasher/src/slasher.rs:94`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/slasher.rs#L94) no genesis-epoch init loop

**Sources.** [prysm#13620](https://github.com/OffchainLabs/prysm/pull/13620)

</details>


<a id="other-028"></a>
<details>
<summary><b>other-028</b> Chunked min/max span storage for surround detection — <i>implemented · low · cpu, disk, memory</i></summary>

**Idea.** Store slasher min and max spans in fixed-size chunks (several validators by several epochs per DB value), check surround votes by reading one span entry per target epoch, and update spans only as far as they change, instead of scanning each validator's full attestation history.

**Impact.** Lighthouse slasher pioneered this chunked min/max span design; same effect.

**Evidence (Lighthouse @ 928b61e719).**

- [`slasher/src/array.rs:23-37`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/array.rs#L23-L37) chunk layout N/C epochs by K validators per DB value, zlib-compressed
- [`slasher/src/array.rs:132`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/array.rs#L132) update() stops when spans no longer change

**Sources.** [prysm#8358](https://github.com/OffchainLabs/prysm/pull/8358), [prysm#8350](https://github.com/OffchainLabs/prysm/pull/8350), [prysm#8446](https://github.com/OffchainLabs/prysm/pull/8446)

</details>


<a id="other-031"></a>
<details>
<summary><b>other-031</b> Compare state roots instead of deep state equality — <i>n/a · low · startup, disk, cpu</i></summary>

**Idea.** Decide whether two states are equal (for example the stored genesis vs the provided genesis at startup) by comparing state roots, using the stored block's state root where possible, instead of loading the full state and deep-comparing every field.

**Impact.** Lighthouse never deep-compares states at startup, so there is nothing to replace with a root comparison.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/builder.rs:255-264`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/builder.rs#L255-L264) resume loads genesis block and state from store, no deep equality against the provided genesis state
- [`beacon_node/client/src/builder.rs:343`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/client/src/builder.rs#L343) genesis_state loaded for fresh start only

**Sources.** [lodestar@79f1df6c3](https://github.com/ChainSafe/lodestar/commit/79f1df6c3398), [lodestar@0b106e210](https://github.com/ChainSafe/lodestar/commit/0b106e210b90), [lodestar@5d018197f](https://github.com/ChainSafe/lodestar/commit/5d018197f591)

</details>


<a id="other-036"></a>
<details>
<summary><b>other-036</b> Light client finality update only on finality change — <i>partial · medium · S · cpu, bandwidth</i></summary>

**Idea.** Compute and publish light client finality updates only when the finalized checkpoint actually changes or improves, instead of building header and proof on every imported block or republishing identical updates.

**Gap in Lighthouse.** Republishing of identical finality updates is already suppressed (the Nimbus half). Still missing is the Prysm half: recompute_and_cache_updates loads the finalized blinded block and builds LightClientFinalityUpdate on every block, with no check on whether finalized_checkpoint changed. Note the spec wants the highest attested header, so the update legitimately changes per block; the saving is mainly the finalized-block DB load and header construction.

**Impact.** Small CPU/DB-read saving per imported block on nodes serving light clients; sub-ms work.

**Best measured result.** None (pr:nimbus#4546)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/light_client_server_cache.rs:305`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/light_client_server_cache.rs#L305) should_broadcast_latest_finality_update publishes only when the update differs from latest_broadcasted_finality_update
- [`beacon_node/http_api/src/sync_committees.rs:337`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/sync_committees.rs#L337) own finality-update gossip goes through that dedup gate
- [`beacon_node/beacon_chain/src/light_client_finality_update_verification.rs:87`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/light_client_finality_update_verification.rs#L87) incoming gossip ignored when equal to the already-broadcast update or older attested slot
- [`beacon_node/beacon_chain/src/light_client_server_cache.rs:153`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/light_client_server_cache.rs#L153) construction side still rebuilds LightClientFinalityUpdate on every imported block (only is_latest gate)

**Second check.** Beyond the earlier review, checked the publish path (http_api sync_committees -&gt; should_broadcast_latest_finality_update) and gossip verification: both dedup identical updates, which is what nimbus#4546 fixed. Only the per-block construction from prysm#14713 is missing.

**Sources.** [nimbus#4546](https://github.com/status-im/nimbus-eth2/pull/4546), [prysm#14713](https://github.com/OffchainLabs/prysm/pull/14713)

</details>


<a id="other-040"></a>
<details>
<summary><b>other-040</b> Move end-of-slot housekeeping earlier in the slot — <i>implemented · medium · latency</i></summary>

**Idea.** Schedule end-of-slot housekeeping and next-slot preparation earlier in the slot (for example at 19/24 and 7/8) so slow work such as state storage around epoch boundaries does not delay the start of the next slot.

**Impact.** Already done; no further gain.

**Best measured result.** None (pr:nimbus#8621)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/state_advance_timer.rs:126`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L126) state advance at slot_duration/4 before next slot
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:136`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L136) fork choice lookahead before slot end
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:1`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L1) advances head state through epoch boundary ahead of time

**Sources.** [nimbus#8621](https://github.com/status-im/nimbus-eth2/pull/8621)

</details>


<a id="other-056"></a>
<details>
<summary><b>other-056</b> Fork-neutral slasher on-disk attestation format — <i>implemented · medium · disk</i></summary>

**Idea.** Store slasher indexed attestations in a fork-neutral on-disk format so a fork upgrade does not require rewriting hundreds of gigabytes of slasher database.

**Impact.** Already done; no further gain.

**Best measured result.** None (pr:lighthouse#5975)

**Evidence (Lighthouse @ 928b61e719).**

- [`slasher/src/database.rs:259`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/database.rs#L259) IndexedAttestationOnDisk::into_indexed_attestation picks Base/Electra/Gloas from target epoch
- [`slasher/src/database.rs:878`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/database.rs#L878) roundtrip tests across forks

**Sources.** [lighthouse#5975](https://github.com/sigp/lighthouse/pull/5975)

</details>


<a id="other-058"></a>
<details>
<summary><b>other-058</b> Tick delay computed relative to genesis — <i>implemented · low · latency</i></summary>

**Idea.** Compute the delay to the next slot/interval tick relative to genesis time, not the unix epoch, so ticks do not fire hundreds of milliseconds late when genesis is not aligned to the interval.

**Impact.** Ticks are computed relative to genesis, no alignment-to-epoch error.

**Best measured result.** None (pr:ethlambda#392)

**Evidence (Lighthouse @ 928b61e719).**

- [`common/slot_clock/src/manual_slot_clock.rs:66-72`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/slot_clock/src/manual_slot_clock.rs#L66-L72) duration_to_next_slot_from uses start_of(slot+1)-now, start_of at :149 is genesis_duration + n*slot_duration
- [`common/slot_clock/src/system_time_slot_clock.rs:50`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/slot_clock/src/system_time_slot_clock.rs#L50) delegates to it

**Sources.** [ethlambda#392](https://github.com/lambdaclass/ethlambda/pull/392)

</details>


<a id="other-059"></a>
<details>
<summary><b>other-059</b> Allocation-free slasher span serialization — <i>not · low · S · cpu, memory</i></summary>

**Idea.** Serialize and deserialize slasher span records with inlinable code that writes into a preallocated buffer without intermediate allocations, halving per-call cost.

**Gap in Lighthouse.** Replace bincode+flate2 in TargetArrayChunk::store/load with direct u16 byte copy into a reused buffer (or drop compression); Lighthouse stores whole chunks, not small span records, so per-call allocation is amortised and the gain is small.

**Impact.** Slasher-only; zlib compression dominates chunk store cost, serialization allocations are minor.

**Best measured result.** None (pr:prysm#7062)

**Evidence (Lighthouse @ 928b61e719).**

- [`slasher/src/array.rs:182-190`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/array.rs#L182-L190) store(): bincode::serialize into a Vec then ZlibEncoder into another Vec, per chunk
- [`slasher/src/array.rs:150-165`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/array.rs#L150-L165) load() uses bincode::deserialize_from over ZlibDecoder

**Sources.** [prysm#7062](https://github.com/OffchainLabs/prysm/pull/7062)

</details>


<a id="other-078"></a>
<details>
<summary><b>other-078</b> Raw key lists instead of encoded slasher index — <i>implemented · low · cpu, disk</i></summary>

**Idea.** For the slasher's per-(epoch, validator) index of attestations, store a raw concatenated list of keys in the DB instead of a protobuf-style encoded value, avoiding decode/encode on every update and lookup.

**Impact.** Already avoided; keys and ids are raw fixed byte arrays with no codec.

**Best measured result.** None (pr:prysm#4832)

**Evidence (Lighthouse @ 928b61e719).**

- [`slasher/src/database.rs:170-200`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/database.rs#L170-L200) IndexedAttestationIdKey is a fixed [u8;N] big-endian epoch+root key
- [`slasher/src/database.rs:204-232`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/database.rs#L204-L232) IndexedAttestationId is a fixed 6-byte id

**Sources.** [prysm#4832](https://github.com/OffchainLabs/prysm/pull/4832)

</details>


<a id="other-079"></a>
<details>
<summary><b>other-079</b> Re-tick immediately after long duty handler — <i>n/a · low · latency</i></summary>

**Idea.** After a slot/interval tick handler returns, re-read the clock and run the next tick at once if an interval boundary passed, so a long duty such as block building does not cause the next interval's duties to be skipped.

**Impact.** Lighthouse VC runs block, attestation and sync duties as separate tasks keyed to the slot clock, so a long block build does not skip another service's tick (no single shared tick handler).

**Best measured result.** None (pr:ethlambda#416)

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/attestation_service.rs:195-243`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/attestation_service.rs#L195-L243) attestation loop is its own spawned task, sleeping to each slot independently

**Sources.** [ethlambda#416](https://github.com/lambdaclass/ethlambda/pull/416)

</details>


<a id="other-085"></a>
<details>
<summary><b>other-085</b> Restart from DB state, skip network fetch — <i>implemented · medium · startup, bandwidth</i></summary>

**Idea.** On restart, start from the state already in the database (genesis or checkpoint origin, if still within the weak subjectivity period) and download a checkpoint or genesis state only when the DB is empty or stale.

**Impact.** Already done; no further gain.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/client/src/builder.rs:282`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/client/src/builder.rs#L282) store_contains_beacon_chain
- [`beacon_node/client/src/builder.rs:295`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/client/src/builder.rs#L295) if chain exists, resume from store and refuse checkpoint sync (needs --purge-db)

**Sources.** [lodestar#4563](https://github.com/ChainSafe/lodestar/pull/4563), [prysm#10881](https://github.com/OffchainLabs/prysm/pull/10881)

</details>


<a id="other-087"></a>
<details>
<summary><b>other-087</b> Static error construction without formatting — <i>n/a · low · cpu</i></summary>

**Idea.** Build error values for fixed messages without a formatting call (for example in signature decoding), avoiding formatting work on error paths.

**Impact.** Error-path formatting only; Lighthouse uses typed enum errors and blst error codes, negligible and no matching hot path.

**Best measured result.** None (pr:prysm#15007)

**Evidence (Lighthouse @ 928b61e719).**

- Searched for signature decode paths; errors in Lighthouse are enum variants, not formatted strings

**Sources.** [prysm#15007](https://github.com/OffchainLabs/prysm/pull/15007)

</details>


<a id="other-088"></a>
<details>
<summary><b>other-088</b> Slasher writes only touched validators per batch — <i>implemented · medium · S · cpu, memory, disk, latency</i></summary>

**Idea.** In the slasher, run double-vote detection once per batch set instead of per validator-chunk batch, and write only the touched validators' latest-written epochs instead of the whole registry in one huge DB transaction.

**Impact.** None left; Lighthouse is the reference design Prysm copied.

**Best measured result.** None (pr:prysm#9833)

**Evidence (Lighthouse @ 928b61e719).**

- [`slasher/src/slasher.rs:194`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/slasher.rs#L194) batch grouped by validator chunk; only chunks with attestations are processed, in one txn
- [`slasher/src/slasher.rs:276`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/slasher.rs#L276) check_double_votes iterates only attesting_validators_in_chunk, so each validator is checked once per batch (no duplicated double-vote work)
- [`slasher/src/array.rs:518`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/array.rs#L518) current_epoch written only for the 256 validators (DEFAULT_VALIDATOR_CHUNK_SIZE, [`slasher/src/config.rs:10`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/config.rs#L10)) of touched chunks, not the whole registry
- [`slasher/src/array.rs:579`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/array.rs#L579) epoch_update_for_validator rewrites the whole validator chunk anyway, so current_epoch for the chunk must move with it

**Second check.** Read prysm#9833: it was explicitly modelled on Lighthouse's slasher and says it now 'matches' Lighthouse. Lighthouse already does the double-vote check only for attesting validators per chunk and writes only touched chunks. The remaining per-chunk current_epoch writes are needed because epoch_update_for_validator neutralises the whole chunk, so they are part of the design, not a gap.

**Sources.** [prysm#9833](https://github.com/OffchainLabs/prysm/pull/9833)

</details>


<a id="other-089"></a>
<details>
<summary><b>other-089</b> Slasher accepts only verified, bounded attestations — <i>implemented · medium · memory</i></summary>

**Idea.** Feed only verified attestations to the slasher and cap the validator index it accepts, so a bogus huge index cannot make it allocate unbounded memory.

**Impact.** Already done; no further gain.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/attestation_verification.rs:443`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L443) slasher fed only after verify_attestation_signature (line ~495) when signature not already checked
- [`slasher/src/attestation_queue.rs:14`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/attestation_queue.rs#L14) MAX_VALIDATOR_INDEX cap and :84 drop out-of-range index

**Sources.** [lighthouse#9141](https://github.com/sigp/lighthouse/pull/9141)

</details>


<a id="other-093"></a>
<details>
<summary><b>other-093</b> Stack buffer for deterministic randomness seed — <i>n/a · low · cpu, memory</i></summary>

**Idea.** Encode the deterministic-randomness seed into a fixed 8-byte stack buffer instead of a growable heap buffer, removing heap allocations in a hot helper.

**Impact.** Prysm's DeterministicRandomness helper has no Lighthouse counterpart; shuffling uses a fixed stack buffer in swap_or_not_shuffle/src/shuffle_list.rs:20-43.

**Best measured result.** None (pr:prysm#16695)

**Evidence (Lighthouse @ 928b61e719).**

- No deterministic-randomness helper; searched beacon_chain for seeded RNG, only rand in builder/test_utils

**Sources.** [prysm#16695](https://github.com/OffchainLabs/prysm/pull/16695)

</details>


<a id="other-095"></a>
<details>
<summary><b>other-095</b> Word-wide is-zero check for hashes — <i>implemented · low · cpu</i></summary>

**Idea.** Check whether a 32-byte hash is zero by comparing it as wide words (u64 chunks) instead of a byte-wise loop; this was 25% of time during sync.

**Impact.** Hash256 is alloy FixedBytes; is_zero is a single array equality that LLVM vectorises, no byte loop.

**Best measured result.** None (pr:nimbus#6682)

**Evidence (Lighthouse @ 928b61e719).**

- alloy-primitives-1.7.1/src/bits/fixed.rs:696 is_zero is `*self == Self::ZERO` (inlined, compiled to wide compares)
- [`beacon_node/store/src/iter.rs:264`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/iter.rs#L264) Hash256::is_zero use

**Sources.** [nimbus#6682](https://github.com/status-im/nimbus-eth2/pull/6682)

</details>


<a id="other-096"></a>
<details>
<summary><b>other-096</b> Debug state dumps only for failed blocks — <i>n/a · low · disk</i></summary>

**Idea.** When a debug flag dumps SSZ state and block per transition, persist only the failed transitions, since valid ones can be retrieved later and each full state is about 175MB.

**Impact.** Lighthouse has no flag that dumps state and block per transition, so there is nothing to restrict to failed blocks.

**Best measured result.** None (pr:prysm#13720)

**Evidence (Lighthouse @ 928b61e719).**

- [`lighthouse/src/main.rs:337-346`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/lighthouse/src/main.rs#L337-L346) dump-config flags only dump config; no per-transition SSZ state/block dump flag found in beacon_chain/src

**Sources.** [prysm#13720](https://github.com/OffchainLabs/prysm/pull/13720)

</details>


