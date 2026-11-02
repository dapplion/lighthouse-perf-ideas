# other

118 ideas: 11 not, 11 partial, 38 implemented, 58 n/a; 1 actionable (high or medium value, verdict `not` or `partial`). [Back to the summary](../README.md).

| id | idea | verdict | value | effort | resources |
|---|---|---|---|---|---|
| [other-001](#other-001) | Slasher bloom filter of data root for double votes | partial | low | M | cpu, memory, disk |
| [other-002](#other-002) | Keep slasher span data cached in memory | partial | low | M | cpu, memory, disk, latency |
| [other-003](#other-003) | Aggregate lazy min-max surround detection | not | low | L | disk |
| [other-004](#other-004) | Append-only compressed validator reward files | n/a | low |  | cpu, disk |
| [other-005](#other-005) | Automatic checkpoint state download on first start | partial | low | S | startup, sync |
| [other-006](#other-006) | Guard slot tickers against unset genesis time | n/a | low |  | cpu |
| [other-007](#other-007) | Avoid string-to-bytes conversion allocations | n/a | low |  | cpu, memory |
| [other-008](#other-008) | DB analysis tool: skip hashing, bigger transactions | n/a | low |  | cpu, disk |
| [other-009](#other-009) | Use compile-time constant zero values | implemented | low | S | cpu, memory |
| [other-010](#other-010) | Compute slot start times once | implemented | low | S | cpu |
| [other-011](#other-011) | Construct union objects directly in final variant | n/a | low | S | cpu |
| [other-012](#other-012) | Batch JSON-RPC requests in one call | not | low | M | latency |
| [other-013](#other-013) | Slasher batches attestations by chunk index | implemented | low | S | cpu, disk |
| [other-014](#other-014) | Slasher DB access in fewer transactions | implemented | low | M | cpu, memory, disk |
| [other-015](#other-015) | Batched double-proposal lookup in slasher | not | low | S | cpu, disk |
| [other-016](#other-016) | Binary search eth1 block for genesis time | n/a | low | S | startup, latency |
| [other-017](#other-017) | Fast integer square root | implemented | low | S | cpu |
| [other-018](#other-018) | Bit-trick is_power_of_two | n/a | low | S | cpu |
| [other-019](#other-019) | Cold-start span init over history length only | partial | low | S | startup, cpu |
| [other-020](#other-020) | Bounded per-subscriber event queues with backpressure | n/a | low | S | cpu, memory |
| [other-021](#other-021) | Shrink large error enums by boxing | implemented | low | S | memory, cpu |
| [other-022](#other-022) | Buffered error channel prevents task leak | n/a | low |  | memory |
| [other-023](#other-023) | Incremental deposit Merkle tree append | implemented | low | S | cpu, memory, startup, sync |
| [other-024](#other-024) | Light client best update only on canonical chain | partial | low | S | memory, disk, cpu |
| [other-025](#other-025) | Native case-insensitive string comparison | n/a | low |  | cpu |
| [other-026](#other-026) | Cheap slashable check before index intersection | n/a | low |  | cpu |
| [other-027](#other-027) | Is-zero check without large static zero array | n/a | low |  | cpu |
| [other-028](#other-028) | Chunked min/max span storage for surround detection | implemented | low |  | cpu, disk, memory |
| [other-029](#other-029) | Reuse a few keypairs in test state builders | n/a | low |  | cpu, startup |
| [other-030](#other-030) | Span entry keeps evidence key for direct lookup | implemented | low | S | disk, latency |
| [other-031](#other-031) | Compare state roots instead of deep state equality | n/a | low |  | startup, disk, cpu |
| [other-032](#other-032) | Slasher work outside DB write transaction | partial | low | S | disk, latency |
| [other-033](#other-033) | Prune light client data by its own retention | not | low | S | disk |
| [other-034](#other-034) | Dedicated thread pool for async networking | n/a | low |  | latency |
| [other-035](#other-035) | Prevent duplicate event-stream subscription handlers | n/a | low |  | cpu |
| [other-036](#other-036) **★** | Light client finality update only on finality change | partial | medium | S | cpu, bandwidth |
| [other-037](#other-037) | Derive head slot from head block | implemented | low | S | cpu |
| [other-038](#other-038) | Return hex strings directly from native code | n/a | low |  | cpu |
| [other-039](#other-039) | Return promises directly, not awaited | n/a | low |  | latency, cpu |
| [other-040](#other-040) | Move end-of-slot housekeeping earlier in the slot | implemented | medium |  | latency |
| [other-041](#other-041) | Check deadline before expensive work | not | low | M | cpu |
| [other-042](#other-042) | Early exit in fork schedule scan | implemented | low | S | cpu |
| [other-043](#other-043) | Embed mainnet genesis state in binary | implemented | low | S | startup, sync |
| [other-044](#other-044) | Iterate map entries instead of key lookups | n/a | low | S | cpu |
| [other-045](#other-045) | Slasher records keyed for range-scan pruning | implemented | low | S | cpu, disk |
| [other-046](#other-046) | Faster big-integer arithmetic on carry intrinsics | n/a | low | S | cpu |
| [other-047](#other-047) | Fast endian conversion in uint256 serialization | n/a | low | S | cpu |
| [other-048](#other-048) | Lookup-table hex decoder on hot paths | not | low | S | cpu |
| [other-049](#other-049) | Cheaper deposit-key derivation in testnet tooling | n/a | low | S | cpu, startup |
| [other-050](#other-050) | Faster test attester-slashing builder | n/a | low | S | cpu |
| [other-051](#other-051) | Request finality update right after LC sync | n/a | low | S | latency, startup |
| [other-052](#other-052) | Remove buffer copies in async TCP/HTTP read path | n/a | low | S | cpu, bandwidth |
| [other-053](#other-053) | Eth1 deposit cache download range fix | n/a | low | S | sync, startup |
| [other-054](#other-054) | Deposit tree as flat list of roots | n/a | low | S | memory |
| [other-055](#other-055) | Plain loops instead of callback iteration | n/a | low | S | cpu |
| [other-056](#other-056) | Fork-neutral slasher on-disk attestation format | implemented | medium |  | disk |
| [other-057](#other-057) | Whole-list swap-or-not shuffle | implemented | high | S | cpu |
| [other-058](#other-058) | Tick delay computed relative to genesis | implemented | low |  | latency |
| [other-059](#other-059) | Allocation-free slasher span serialization | not | low | S | cpu, memory |
| [other-060](#other-060) | into_owned instead of to_string on Cow | not | low | S | cpu |
| [other-061](#other-061) | Keep torrent metadata for resumed snapshot sync | n/a | low |  | startup, sync |
| [other-062](#other-062) | Lazy deposit proofs at proposal time | n/a | low |  | cpu |
| [other-063](#other-063) | Committees as borrowed slices of shuffled list | implemented | low | S | memory, cpu |
| [other-064](#other-064) | Compile regexes once in static cells | partial | low | S | cpu, startup |
| [other-065](#other-065) | Linear max scan in slashing-protection import | implemented | low | S | cpu, startup |
| [other-066](#other-066) | Multi-threaded event-channel subscribers | n/a | low |  | latency |
| [other-067](#other-067) | Native buffer compare for roots | n/a | low |  | cpu |
| [other-068](#other-068) | Worker-split utility for genesis generation | n/a | low |  | cpu |
| [other-069](#other-069) | Concurrent graceful shutdown tasks | partial | low | S | latency |
| [other-070](#other-070) | Concurrent validator generation in test builder | n/a | low | S | cpu, startup |
| [other-071](#other-071) | Persist eth1 deposit checkpoints to disk | n/a | low | S | startup, sync |
| [other-072](#other-072) | Hardware popcount for bitfields | implemented | low | S | cpu |
| [other-073](#other-073) | Preallocate capacity in dedupe helpers | n/a | low | S | memory, cpu |
| [other-074](#other-074) | Primitive-specialized collections instead of boxed | n/a | low | S | memory, cpu |
| [other-075](#other-075) | Cache proposer indices per epoch | implemented | high | S | cpu |
| [other-076](#other-076) | Prune persisted invalid-object debug dumps | n/a | low | S | disk |
| [other-077](#other-077) | Range primitive to initialise shuffle indices | n/a | low | S | cpu |
| [other-078](#other-078) | Raw key lists instead of encoded slasher index | implemented | low |  | cpu, disk |
| [other-079](#other-079) | Re-tick immediately after long duty handler | n/a | low |  | latency |
| [other-080](#other-080) | Remove redundant clones in services | implemented | low | S | cpu, memory |
| [other-081](#other-081) | Remove needless async on synchronous paths | n/a | low | S | cpu, latency |
| [other-082](#other-082) | Fixed-layout shared memory for thread messages | n/a | low | S | cpu, latency |
| [other-083](#other-083) | Download genesis or anchor state only once | implemented | low | S | startup, bandwidth |
| [other-084](#other-084) | Reward aggregates computed during data generation | n/a | low | S | cpu, disk |
| [other-085](#other-085) | Restart from DB state, skip network fetch | implemented | medium |  | startup, bandwidth |
| [other-086](#other-086) | Skip slashing DB write when none found | partial | low | S | disk |
| [other-087](#other-087) | Static error construction without formatting | n/a | low |  | cpu |
| [other-088](#other-088) | Slasher writes only touched validators per batch | implemented | medium | S | cpu, memory, disk, latency |
| [other-089](#other-089) | Slasher accepts only verified, bounded attestations | implemented | medium | S | memory |
| [other-090](#other-090) | Slasher processing keeps up with chain head | implemented | low | S | latency |
| [other-091](#other-091) | Smaller slasher span bucket layout | n/a | low | S | disk |
| [other-092](#other-092) | EIP-4881 snapshot deposit tree | n/a | low |  | memory |
| [other-093](#other-093) | Stack buffer for deterministic randomness seed | n/a | low |  | cpu, memory |
| [other-094](#other-094) | Transfer large buffers to workers, not copy | n/a | low |  | cpu, latency |
| [other-095](#other-095) | Word-wide is-zero check for hashes | implemented | low | S | cpu |
| [other-096](#other-096) | Debug state dumps only for failed blocks | n/a | low |  | disk |
| [other-097](#other-097) | Slasher DB lookup once per unique detection | implemented | low | S | cpu, disk |
| [other-098](#other-098) | Build genesis state incrementally from deposit stream | n/a | low |  | startup, cpu, memory |
| [other-099](#other-099) | Hardware-accelerated SHA-256 selected by CPU | implemented | low | S | cpu |
| [other-100](#other-100) | Hash shuffle rounds from reusable buffers | implemented | low | S | cpu, memory |
| [other-101](#other-101) | Compressed genesis state download | not | low | S | bandwidth, startup |
| [other-102](#other-102) | Read genesis time from config constant | implemented | low | S | cpu, latency |
| [other-103](#other-103) | Cancellation-aware sleeps in background loops | n/a | low |  | latency |
| [other-104](#other-104) | Slasher block-header queue as hash set | implemented | low | S | cpu, memory |
| [other-105](#other-105) | Exit debounce loops when channel closes | n/a | low |  | cpu |
| [other-106](#other-106) | Incremental span update with early stop | implemented | low | S | cpu |
| [other-107](#other-107) | Indices-only sync committee accessor | partial | low | S | cpu, memory |
| [other-108](#other-108) | Minify slashing protection data on import | not | low | S | disk, startup |
| [other-109](#other-109) | Minimal assert helper in hot paths | n/a | low |  | cpu |
| [other-110](#other-110) | Native integers instead of bignum for slots and balances | n/a | low |  | cpu, memory |
| [other-111](#other-111) | Flag to disable light client server | implemented | low | S | cpu, disk, bandwidth |
| [other-112](#other-112) | Release resources per loop iteration | n/a | low |  | memory |
| [other-113](#other-113) | Remove event listeners when done | n/a | low |  | memory, cpu |
| [other-114](#other-114) | Single hash-map lookup on hot path | not | low | S | cpu |
| [other-115](#other-115) | Single-pass filter into preallocated array | n/a | low |  | cpu, memory |
| [other-116](#other-116) | Sleep in idle main-thread loop | implemented | low | S | cpu |
| [other-117](#other-117) | Slasher attestation index keyed by target epoch only | implemented | low | S | disk |
| [other-118](#other-118) | Typed sort instead of reflection sort | n/a | low |  | cpu, memory |

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


<a id="other-004"></a>
<details>
<summary><b>other-004</b> Append-only compressed validator reward files — <i>n/a · low · cpu, disk</i></summary>

**Idea.** Persist per-epoch validator reward data as append-only compressed CSV plus aggregated daily summaries, and clear the state cache each iteration, so reward/analysis tooling writes faster, stores less and reports quickly.

**Impact.** Nimbus-specific offline reward tooling; Lighthouse serves rewards via the HTTP API and has no reward file writer.

**Best measured result.** None (commit:nimbus@47f1f7ff1a12)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/standard_block_rewards.rs:1`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/standard_block_rewards.rs#L1) rewards are computed on demand via API, no reward files

**Sources.** [nimbus@47f1f7ff1](https://github.com/status-im/nimbus-eth2/commit/47f1f7ff1a12)

</details>


<a id="other-005"></a>
<details>
<summary><b>other-005</b> Automatic checkpoint state download on first start — <i>partial · low · S · startup, sync</i></summary>

**Idea.** On first start with an empty database, download a checkpoint state from a configured remote provider automatically instead of syncing from genesis, so startup and sync are much shorter.

**Gap in Lighthouse.** Lighthouse has no built-in list of checkpoint providers and no automatic fetch when the DB is empty and no --checkpoint-sync-url is given. The ClientGenesis::GenesisState path in ClientBuilder::beacon_chain_builder stops with an error instead of falling back to a remote provider (silver#331 adds checkpoint_providers.rs with per-network defaults).

**Impact.** UX only. Once the user passes the URL, the checkpoint sync speed is the same. Lighthouse already refuses the slow genesis-sync path on mainnet.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/client/src/builder.rs:340-386`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/client/src/builder.rs#L340-L386) ClientGenesis::GenesisState returns an error outside the blob window unless --allow-insecure-genesis-sync is set; it does not download a state
- [`beacon_node/client/src/builder.rs:378`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/client/src/builder.rs#L378) the error message tells the user to pass --checkpoint-sync-url

**Skeptic check.** Checkpoint sync exists, but only behind an explicit flag, and the empty-DB fallback is an error, not an automatic download. The earlier verdict said the same thing in its impact text but still labelled the idea implemented.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [silver#331](https://github.com/gattaca-com/silver/pull/331)

</details>


<a id="other-006"></a>
<details>
<summary><b>other-006</b> Guard slot tickers against unset genesis time — <i>n/a · low · cpu</i></summary>

**Idea.** Make slot tickers and timing loops wait until genesis time is set, so a zero genesis time on a fresh DB does not make a ticker spin and fire tasks rapidly.

**Impact.** Go ticker spin on unset genesis; Lighthouse builds its slot clock from a known genesis time and uses sleeps via duration_to_next_slot.

**Evidence (Lighthouse @ 928b61e719).**

- [`common/slot_clock/src/lib.rs:26`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/slot_clock/src/lib.rs#L26) now_or_genesis returns genesis slot before genesis
- [`beacon_node/client/src/builder.rs:972`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/client/src/builder.rs#L972) clock built from known genesis_time

**Sources.** [prysm#7947](https://github.com/OffchainLabs/prysm/pull/7947)

</details>


<a id="other-007"></a>
<details>
<summary><b>other-007</b> Avoid string-to-bytes conversion allocations — <i>n/a · low · cpu, memory</i></summary>

**Idea.** Write strings directly into buffers (WriteString, NewBufferString equivalents) instead of converting string to byte slices first, and enforce it with a linter, to skip needless allocations.

**Impact.** Go string-to-byte-slice conversion allocation; no equivalent in Rust.

**Sources.** [prysm#13342](https://github.com/OffchainLabs/prysm/pull/13342), [caplin#23097](https://github.com/erigontech/erigon/pull/23097)

</details>


<a id="other-008"></a>
<details>
<summary><b>other-008</b> DB analysis tool: skip hashing, bigger transactions — <i>n/a · low · cpu, disk</i></summary>

**Idea.** In database analysis/inspection tools, do not hash objects unless needed and group writes into larger transactions, so offline DB tooling runs faster.

**Impact.** Nimbus offline DB inspection tool; Lighthouse has no comparable hashing tool on a hot path.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/lib.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/lib.rs): no DB analysis tool in store crate

**Sources.** [nimbus#2885](https://github.com/status-im/nimbus-eth2/pull/2885)

</details>


<a id="other-009"></a>
<details>
<summary><b>other-009</b> Use compile-time constant zero values — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Compare against or use compile-time constant zero values (ZERO_HASH, an empty SyncCommittee) instead of allocating and zeroing a fresh object at runtime on each check, avoiding the memset and stack use.

**Impact.** In Rust, Hash256 zero is a const and the compare is trivial. The only runtime-built empty SyncCommittee is in the one-time Altair upgrade, so there is nothing measurable to gain.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_slot_processing.rs:143`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_slot_processing.rs#L143) compares against Hash256::zero(), a const 32-byte value
- [`consensus/proto_array/src/proto_array_fork_choice.rs:1415`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array_fork_choice.rs#L1415) vote roots compared with Hash256::zero()
- [`consensus/state_processing/src/upgrade/altair.rs:60`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/upgrade/altair.rs#L60) SyncCommittee::temporary() only at the one-time fork upgrade

**Skeptic check.** Grepped for runtime zero-object construction on hot paths and found only the fork-upgrade site. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#5401](https://github.com/status-im/nimbus-eth2/pull/5401), [nimbus#8252](https://github.com/status-im/nimbus-eth2/pull/8252)

</details>


<a id="other-010"></a>
<details>
<summary><b>other-010</b> Compute slot start times once — <i>implemented · low · S · cpu</i></summary>

**Idea.** Compute slot start times once and pass them to callers, instead of recomputing them from genesis time and the fork schedule in many places.

**Impact.** start_of is one checked multiply-add, and the slot clock is a single shared object. teku#9562 is mostly a refactor, so caching would gain nothing here.

**Evidence (Lighthouse @ 928b61e719).**

- [`common/slot_clock/src/system_time_slot_clock.rs:55`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/slot_clock/src/system_time_slot_clock.rs#L55) start_of delegates to ManualSlotClock
- [`common/slot_clock/src/manual_slot_clock.rs:149-158`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/slot_clock/src/manual_slot_clock.rs#L149-L158) start_of = genesis_duration + slot_duration * slot, with no fork-schedule lookup

**Skeptic check.** Read ManualSlotClock::start_of: it uses constant arithmetic with no per-fork recomputation. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#9562](https://github.com/Consensys-Incorporated/teku/pull/9562)

</details>


<a id="other-011"></a>
<details>
<summary><b>other-011</b> Construct union objects directly in final variant — <i>n/a · low · S · cpu</i></summary>

**Idea.** Construct tagged-union objects (for example light client fork variants) directly with their final variant, instead of default-initializing, zeroing and then assigning, to avoid the redundant memset.

**Impact.** Rust enums are constructed directly in the final variant; no default-then-assign pattern.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/core/slot_epoch_macros.rs:216`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/core/slot_epoch_macros.rs#L216) (no relevant code)

**Sources.** [nimbus#5479](https://github.com/status-im/nimbus-eth2/pull/5479)

</details>


<a id="other-012"></a>
<details>
<summary><b>other-012</b> Batch JSON-RPC requests in one call — <i>not · low · M · latency</i></summary>

**Idea.** Send several JSON-RPC requests to the execution node as one batch request (for example in the light client prover) to cut round trips.

**Gap in Lighthouse.** Add batch request support to rpc_request; but Lighthouse has no light-client prover making many EL calls, and engine calls are sequential by nature.

**Impact.** Negligible on a mainnet node; EL calls are few and latency-critical individually.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/execution_layer/src/engine_api/http.rs:661`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engine_api/http.rs#L661) rpc_request sends one JSON-RPC call per request, no batching

**Sources.** [lodestar#5636](https://github.com/ChainSafe/lodestar/pull/5636)

</details>


<a id="other-013"></a>
<details>
<summary><b>other-013</b> Slasher batches attestations by chunk index — <i>implemented · low · S · cpu, disk</i></summary>

**Idea.** Group incoming slasher attestations by validator chunk index and process them in batches on an epoch/interval ticker, so each span chunk is loaded from the DB once, updated for every attester in the batch, and written once.

**Impact.** Each span chunk is already read and written once per batch. This only matters for slasher nodes.

**Evidence (Lighthouse @ 928b61e719).**

- [`slasher/src/attestation_queue.rs:80`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/attestation_queue.rs#L80) group_by_validator_chunk_index splits the batch into per-chunk subqueues
- [`slasher/src/slasher.rs:93`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/slasher.rs#L93) process_queued drains the queue on the slasher update-period ticker
- [`slasher/src/slasher.rs:194`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/slasher.rs#L194) batch processed per validator chunk index
- [`slasher/src/array.rs:566-621`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/array.rs#L566-L621) update_array keeps an updated_chunks BTreeMap, so each chunk is loaded once, updated for all attesters, and stored once

**Skeptic check.** Followed the grouping, the updated_chunks cache and the single store loop at array.rs:620. This is the same mechanism as prysm#8386/#8423.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#8386](https://github.com/OffchainLabs/prysm/pull/8386), [prysm#8423](https://github.com/OffchainLabs/prysm/pull/8423)

</details>


<a id="other-014"></a>
<details>
<summary><b>other-014</b> Slasher DB access in fewer transactions — <i>implemented · low · M · cpu, memory, disk</i></summary>

**Idea.** Batch slasher DB reads and writes into few large transactions (and run span detection concurrently with one put per detection) instead of one transaction per attestation, so a slot's attestations are processed within the slot and the queue does not grow.

**Impact.** Core benefit present (one rw txn per batch, chunk-level writes). Parallel span detection is absent but secondary.

**Best measured result.** None (pr:prysm#13629)

**Evidence (Lighthouse @ 928b61e719).**

- [`slasher/src/slasher.rs:93-102`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/slasher.rs#L93-L102)
- [`slasher/src/slasher.rs:192-196`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/slasher.rs#L192-L196)
- [`slasher/src/array.rs:576-621`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/array.rs#L576-L621)

**Skeptic check.** process_queued opens one rw transaction for all queued blocks and attestations; attestations are grouped by validator chunk and span updates accumulate in updated_chunks and are stored once per chunk. Only the concurrency part of Prysm #13629 is not done.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#4172](https://github.com/OffchainLabs/prysm/pull/4172), [prysm#13629](https://github.com/OffchainLabs/prysm/pull/13629)

</details>


<a id="other-015"></a>
<details>
<summary><b>other-015</b> Batched double-proposal lookup in slasher — <i>not · low · S · cpu, disk</i></summary>

**Idea.** Detect double proposals with one batched DB lookup of all (proposer, slot) entries in a batch and compare signing roots, instead of one lookup per block.

**Gap in Lighthouse.** Sort queued blocks by key and do one cursor pass in process_blocks instead of per-block lookup in check_or_insert_block_proposal.

**Impact.** Block volume is ~1 per slot, so savings are tiny and only on slasher nodes.

**Evidence (Lighthouse @ 928b61e719).**

- [`slasher/src/slasher.rs:107-120`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/slasher.rs#L107-L120) process_blocks loops with one check_or_insert_block_proposal per block
- [`slasher/src/database.rs:702`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/database.rs#L702) get_block_proposal per (proposer, slot)

**Sources.** [prysm#8470](https://github.com/OffchainLabs/prysm/pull/8470)

</details>


<a id="other-016"></a>
<details>
<summary><b>other-016</b> Binary search eth1 block for genesis time — <i>n/a · low · S · startup, latency</i></summary>

**Idea.** When looking for the first eth1 block that meets the minimum genesis time, binary search over block numbers instead of scanning linearly.

**Impact.** Eth1 genesis search was removed from Lighthouse; genesis comes from a state.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/genesis/src`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/genesis/src)/ has only common.rs, interop.rs, lib.rs; no eth1 directory

**Sources.** [teku#1621](https://github.com/Consensys-Incorporated/teku/pull/1621)

</details>


<a id="other-017"></a>
<details>
<summary><b>other-017</b> Fast integer square root — <i>implemented · low · S · cpu</i></summary>

**Idea.** Compute integer square root (used for base reward per epoch) with a fast method such as binary search or a native isqrt, instead of the slow iterative spec method.

**Impact.** Negligible; already fast and cached.

**Best measured result.** None (pr:prysm#3785)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/common/base.rs:10-13`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/common/base.rs#L10-L13)
- ~/.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/integer-sqrt-0.1.5/src/lib.rs:47-77
- [`consensus/state_processing/src/epoch_cache.rs:197`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/epoch_cache.rs#L197)

**Skeptic check.** integer-sqrt 0.1.5 uses the bitwise digit-by-digit method (O(bits/2) iterations), and the result is cached per epoch in the epoch cache. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#3785](https://github.com/OffchainLabs/prysm/pull/3785)

</details>


<a id="other-018"></a>
<details>
<summary><b>other-018</b> Bit-trick is_power_of_two — <i>n/a · low · S · cpu</i></summary>

**Idea.** Implement is_power_of_two with the bit trick (n &amp; (n-1)) == 0 instead of the naive spec loop.

**Impact.** Rust's std is_power_of_two already uses a bit trick.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/core/slot_epoch_macros.rs:216`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/core/slot_epoch_macros.rs#L216) uses std u64::is_power_of_two

**Sources.** [teku#448](https://github.com/Consensys-Incorporated/teku/pull/448)

</details>


<a id="other-019"></a>
<details>
<summary><b>other-019</b> Cold-start span init over history length only — <i>partial · low · S · startup, cpu</i></summary>

**Idea.** On a slasher cold start with no DB, initialise the min/max span arrays by looping only over the circular-buffer history length instead of every epoch since genesis, because older cells are overwritten anyway. Boot goes from O(epochs*validators) to O(validators).

**Gap in Lighthouse.** Cold start with an empty DB is O(1), as the idea wants. But after a restart following downtime longer than history_length, epoch_update_for_validator (called from update_array for both MinTargetChunk and MaxTargetChunk) loops over every elapsed epoch per validator, rewriting the same circular cells several times. Start the loop at max(previous_current_epoch, current_epoch + 1 - history_length).

**Impact.** Only after long slasher downtime (&gt; history_length epochs, ~18 days by default): it removes redundant cell writes, about 256 validators x elapsed epochs x 2 arrays per chunk on the first batch.

**Best measured result.** None (pr:prysm#13620)

**Evidence (Lighthouse @ 928b61e719).**

- [`slasher/src/array.rs:528-530`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/array.rs#L528-L530) epoch_update_for_validator returns early when no current epoch is stored (cold start: no genesis loop)
- [`slasher/src/array.rs:532-553`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/array.rs#L532-L553) loop runs from previous_current_epoch to current_epoch with no clamp to history_length
- [`slasher/src/array.rs:568-578`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/array.rs#L568-L578) update_array calls it for every validator of each touched chunk
- [`slasher/src/database.rs:96-101`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/database.rs#L96-L101) cells are indexed modulo history_length (circular buffer)

**Skeptic check.** The earlier evidence was right for the cold-start case: no genesis initialisation exists. It missed the analogous restart-after-downtime path, where the epoch loop has no history_length bound.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [prysm#13620](https://github.com/OffchainLabs/prysm/pull/13620)

</details>


<a id="other-020"></a>
<details>
<summary><b>other-020</b> Bounded per-subscriber event queues with backpressure — <i>n/a · low · S · cpu, memory</i></summary>

**Idea.** Deliver internal events through bounded per-subscriber queues so slow consumers apply backpressure to the producer, instead of spawning a task or thread per event until resources run out.

**Impact.** The JVM thread-per-event pattern does not exist in Lighthouse.

**Evidence (Lighthouse @ 928b61e719).**

- Lighthouse uses tokio channels and task spawns, not a thread per event

**Sources.** [teku#1124](https://github.com/Consensys-Incorporated/teku/pull/1124)

</details>


<a id="other-021"></a>
<details>
<summary><b>other-021</b> Shrink large error enums by boxing — <i>implemented · low · S · memory, cpu</i></summary>

**Idea.** Box large, rarely used fields or inner errors of big error enum variants (and drop extraneous fields) so Result types on hot paths stay small and cheap to move.

**Impact.** Large inner errors are boxed on block and attestation verification. The remaining clippy::result_large_err allows have documented reasons (the error is the same size as the Ok value) or are in tests or the http_api, slasher and network service crates.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/errors.rs:156`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/errors.rs#L156) Box&lt;execution_layer::Error&gt;
- [`beacon_node/beacon_chain/src/errors.rs:333`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/errors.rs#L333) Box&lt;BeaconChainError&gt;
- [`beacon_node/beacon_chain/src/block_verification.rs:252`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L252) BlockError::BeaconChainError(Box&lt;BeaconChainError&gt;)
- [`beacon_node/beacon_chain/src/block_verification.rs:347`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L347) Box&lt;EnvelopeError&gt;
- [`beacon_node/beacon_chain/src/attestation_verification.rs:285`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L285) Box&lt;BeaconChainError&gt;
- [`beacon_node/beacon_chain/src/attestation_verification.rs:33`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L33) lint allowed only because the SlashInfo error is about the same size as the Ok types

**Skeptic check.** The hot-path modules allow the lint, but the comments say the Err is about the same size as the Ok value, so boxing would not shrink the Result. The earlier verdict holds.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#7623](https://github.com/sigp/lighthouse/pull/7623), [lighthouse#3916](https://github.com/sigp/lighthouse/pull/3916), [lighthouse#2850](https://github.com/sigp/lighthouse/pull/2850), [lighthouse#7471](https://github.com/sigp/lighthouse/pull/7471)

</details>


<a id="other-022"></a>
<details>
<summary><b>other-022</b> Buffered error channel prevents task leak — <i>n/a · low · memory</i></summary>

**Idea.** Give resubscriber error channels a buffer so a sender in a race does not block forever and leak a goroutine/task.

**Impact.** No Go goroutine leak pattern; Rust channels drop on receiver close.

**Evidence (Lighthouse @ 928b61e719).**

- [`slasher/src/slasher.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/slasher.rs): no resubscriber error channels (Rust tokio, no goroutines)

**Sources.** [prysm#9513](https://github.com/OffchainLabs/prysm/pull/9513)

</details>


<a id="other-023"></a>
<details>
<summary><b>other-023</b> Incremental deposit Merkle tree append — <i>implemented · low · S · cpu, memory, startup, sync</i></summary>

**Idea.** Append deposits to the eth1 deposit Merkle tree incrementally: keep the frontier of left-sibling branch roots (with precomputed zero hashes) and rehash only the path from the new leaf to the root, O(log n) per deposit, instead of rebuilding the tree from all leaves. This removes quadratic cost in genesis building and deposit replay.

**Impact.** The deposit tree append is already incremental (O(depth) per leaf, worst case O(depth^2) when it probes a full left subtree). Only genesis and deposit replay use it.

**Best measured result.** None (pr:prysm#4299)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/merkle_proof/src/lib.rs:104-150`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/merkle_proof/src/lib.rs#L104-L150) MerkleTree::push_leaf descends one path and rehashes on the way up, using Zero nodes for empty subtrees
- [`consensus/state_processing/src/common/deposit_data_tree.rs:51`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/common/deposit_data_tree.rs#L51) DepositDataTree::push_leaf
- [`consensus/state_processing/src/genesis.rs:37-45`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/genesis.rs#L37-L45) genesis appends each deposit with push_leaf and reads root(), with no rebuild

**Skeptic check.** Confirmed that genesis appends incrementally instead of rebuilding from all leaves. This matches lighthouse#563/#574, and the earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#5605](https://github.com/Consensys-Incorporated/teku/pull/5605), [teku#1145](https://github.com/Consensys-Incorporated/teku/pull/1145), [nimbus@f6de87b80](https://github.com/status-im/nimbus-eth2/commit/f6de87b80ed8), [prysm#4299](https://github.com/OffchainLabs/prysm/pull/4299), [lighthouse#563](https://github.com/sigp/lighthouse/pull/563), [lighthouse#574](https://github.com/sigp/lighthouse/pull/574), [lodestar#217](https://github.com/ChainSafe/lodestar/pull/217), [nimbus#1504](https://github.com/status-im/nimbus-eth2/pull/1504)

</details>


<a id="other-024"></a>
<details>
<summary><b>other-024</b> Light client best update only on canonical chain — <i>partial · low · S · memory, disk, cpu</i></summary>

**Idea.** Track the best/latest light client update only for the branch fork choice selects, instead of across all branches within a sync committee period, to reduce bookkeeping, memory and stored data.

**Gap in Lighthouse.** Updates are computed for every imported block (recompute_and_cache_updates) not only blocks on the fork-choice head chain; restricting to canonical head would skip work on side branches.

**Impact.** Saves a little work per non-canonical block on nodes with the light client server enabled; rare setup.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/light_client_server_cache.rs:191-205`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/light_client_server_cache.rs#L191-L205) keeps best update per period via is_better_light_client_update and persists it
- light_client_server_cache.rs:243 get_light_client_update uses one latest cached update

**Sources.** [nimbus#5613](https://github.com/status-im/nimbus-eth2/pull/5613), [nimbus#5691](https://github.com/status-im/nimbus-eth2/pull/5691)

</details>


<a id="other-025"></a>
<details>
<summary><b>other-025</b> Native case-insensitive string comparison — <i>n/a · low · cpu</i></summary>

**Idea.** Use a native case-insensitive comparison instead of lowercasing both strings and comparing, to avoid allocations (cold paths such as CLI prompts only).

**Impact.** Cold CLI-only concern in Go.

**Evidence (Lighthouse @ 928b61e719).**

- no hot-path case-insensitive string comparison

**Sources.** [prysm#8193](https://github.com/OffchainLabs/prysm/pull/8193)

</details>


<a id="other-026"></a>
<details>
<summary><b>other-026</b> Cheap slashable check before index intersection — <i>n/a · low · cpu</i></summary>

**Idea.** In slasher duplicate-attestation detection, test the cheap slashable-vote condition first and compute the expensive intersection of attesting indices only when that condition holds.

**Impact.** Lighthouse slasher stores one record per validator and never intersects attesting index sets, so there is no expensive intersection to defer.

**Evidence (Lighthouse @ 928b61e719).**

- [`slasher/src/database.rs:610-632`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/database.rs#L610-L632) check_and_update_attester_record compares per-validator record ids and data roots
- [`slasher/src/slasher.rs:266`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/slasher.rs#L266) check_double_votes iterates validators individually

**Sources.** [prysm#5835](https://github.com/OffchainLabs/prysm/pull/5835)

</details>


<a id="other-027"></a>
<details>
<summary><b>other-027</b> Is-zero check without large static zero array — <i>n/a · low · cpu</i></summary>

**Idea.** In light client header validation, test fields such as the execution branch for all-zero with a loop or a dedicated is-zero routine, instead of comparing against a large static zero array.

**Impact.** Lighthouse is a light client server only; it does not validate headers by comparing the execution branch to a zero array.

**Best measured result.** None (pr:nimbus#8782)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/light_client/light_client_header.rs:224`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/light_client/light_client_header.rs#L224) uses FixedVector::default(); no is-zero check against static array on a validation path

**Sources.** [nimbus#8782](https://github.com/status-im/nimbus-eth2/pull/8782)

</details>


<a id="other-028"></a>
<details>
<summary><b>other-028</b> Chunked min/max span storage for surround detection — <i>implemented · low · cpu, disk, memory</i></summary>

**Idea.** Store slasher min and max spans in fixed-size chunks (several validators by several epochs per DB value), check surround votes by reading one span entry per target epoch, and update spans only as far as they change, instead of scanning each validator's full attestation history.

**Impact.** Lighthouse's slasher uses this chunked min/max span design; same effect.

**Evidence (Lighthouse @ 928b61e719).**

- [`slasher/src/array.rs:16-32`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/array.rs#L16-L32) Chunk is C epochs x K validators of u16 distances
- [`slasher/src/array.rs:157-170`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/array.rs#L157-L170) chunk load/store with bincode + zlib under one disk key
- [`slasher/src/array.rs:132-140`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/array.rs#L132-L140) update() returns bool so propagation stops when spans stop changing
- [`slasher/src/array.rs:397-418`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/array.rs#L397-L418) get_chunk_for_update caches loaded chunks per batch

**Skeptic check.** Confirmed the chunked span layout, the lookup of one distance per check, and the early stop on updates. The earlier verdict is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#8358](https://github.com/OffchainLabs/prysm/pull/8358), [prysm#8350](https://github.com/OffchainLabs/prysm/pull/8350), [prysm#8446](https://github.com/OffchainLabs/prysm/pull/8446), [prysm#3941](https://github.com/OffchainLabs/prysm/pull/3941), [prysm#3967](https://github.com/OffchainLabs/prysm/pull/3967)

</details>


<a id="other-029"></a>
<details>
<summary><b>other-029</b> Reuse a few keypairs in test state builders — <i>n/a · low · cpu, startup</i></summary>

**Idea.** In test state builders, clone a small set of keypairs instead of generating a distinct keypair per validator, so test setup is faster (test tooling only).

**Impact.** Test tooling only, no mainnet node effect.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/test_utils`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/test_utils): generate_deterministic_keypairs used in tests ([`beacon_node/beacon_chain/src/test_utils.rs:503`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/test_utils.rs#L503))

**Sources.** [lighthouse@f4959fc03](https://github.com/sigp/lighthouse/commit/f4959fc03c28)

</details>


<a id="other-030"></a>
<details>
<summary><b>other-030</b> Span entry keeps evidence key for direct lookup — <i>implemented · low · S · disk, latency</i></summary>

**Idea.** Store each slasher min/max span entry as a compact struct that also keeps a few bytes of the evidence key, so the conflicting attestation is found with a direct DB lookup instead of a search.

**Impact.** Conflicting attestation found by two keyed DB gets (attester record, then indexed attestation by id); no search.

**Evidence (Lighthouse @ 928b61e719).**

- [`slasher/src/array.rs:30-52`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/array.rs#L30-L52) Chunk stores u16 target distances, get_target reconstructs target epoch
- [`slasher/src/array.rs:219-235`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/array.rs#L219-L235) MinTargetChunk::check_slashable calls db.get_attestation_for_validator(validator, min_target)
- [`slasher/src/database.rs:654-669`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/database.rs#L654-L669) get_attestation_for_validator: keyed get on AttesterKey(validator, target) then get_indexed_attestation by id

**Skeptic check.** Verified: the span chunk keeps the target epoch (as a distance), which with the validator index is the full key of the attester record, which points to the indexed attestation id. The mechanism differs from Prysm's (no key bytes in the span) but the effect, a direct lookup, is the same; earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#4981](https://github.com/OffchainLabs/prysm/pull/4981)

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


<a id="other-032"></a>
<details>
<summary><b>other-032</b> Slasher work outside DB write transaction — <i>partial · low · S · disk, latency</i></summary>

**Idea.** In the slasher, do the expensive computation before opening the database write transaction so the transaction is short and does not block other DB users.

**Gap in Lighthouse.** Move the dequeue, validate, AttestationBatch queueing and group_by_validator_chunk_index steps in process_attestations ahead of begin_rw_txn in process_queued. The per-chunk array updates read the DB so they must stay in the txn.

**Impact.** Slasher is an optional feature; LMDB/MDBX has a single writer so a shorter txn only helps the pruning and other writers marginally.

**Evidence (Lighthouse @ 928b61e719).**

- [`slasher/src/slasher.rs:93`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/slasher.rs#L93) process_queued opens begin_rw_txn before process_blocks/process_attestations
- [`slasher/src/slasher.rs:135`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/slasher.rs#L135) validate, dedupe, sort and group run inside the txn

**Sources.** [prysm#5963](https://github.com/OffchainLabs/prysm/pull/5963)

</details>


<a id="other-033"></a>
<details>
<summary><b>other-033</b> Prune light client data by its own retention — <i>not · low · S · disk</i></summary>

**Idea.** Prune light client data by its own retention period only, not bounded by the pruned block history tail, so LC data does not accumulate on disk.

**Gap in Lighthouse.** Add a prune step (for example in migrate.rs after finalization) that deletes LightClientUpdate keys older than a configured number of sync committee periods.

**Impact.** Saves a few hundred KB per year at most (one SSZ update per ~27h period); negligible disk gain.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:892`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L892) store_light_client_update only puts one row per sync committee period
- [`beacon_node/beacon_chain/src/light_client_server_cache.rs:33`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/light_client_server_cache.rs#L33) only latest update kept in memory
- no delete of DBColumn::LightClientUpdate found in store or beacon_chain

**Sources.** [nimbus#4702](https://github.com/status-im/nimbus-eth2/pull/4702)

</details>


<a id="other-034"></a>
<details>
<summary><b>other-034</b> Dedicated thread pool for async networking — <i>n/a · low · latency</i></summary>

**Idea.** Run async networking tasks on a dedicated thread pool so they do not compete with other node work for threads.

**Gap in Lighthouse.** Async networking in Lighthouse runs on tokio and CPU-heavy work is already moved to the beacon processor and rayon pools, so networking futures do not compete with blocking work.

**Impact.** Little to gain; a separate runtime for libp2p would add complexity for no measured benefit.

**Evidence (Lighthouse @ 928b61e719).**

- [`lighthouse/environment/src/lib.rs:172`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/lighthouse/environment/src/lib.rs#L172) single multi-thread tokio runtime
- [`common/task_executor/src/rayon_pool_provider.rs:28`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/task_executor/src/rayon_pool_provider.rs#L28) CPU work goes to dedicated rayon pools
- [`beacon_node/beacon_processor/src/lib.rs:1728`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L1728) heavy work offloaded via beacon processor

**Sources.** [teku#1787](https://github.com/Consensys-Incorporated/teku/pull/1787)

</details>


<a id="other-035"></a>
<details>
<summary><b>other-035</b> Prevent duplicate event-stream subscription handlers — <i>n/a · low · cpu</i></summary>

**Idea.** Mark an event-stream subscription as active once subscribed so repeated subscribe calls do not register duplicate handlers that process each update twice.

**Gap in Lighthouse.** Each SSE request gets its own broadcast receivers, so repeated subscription cannot register duplicate handlers on one stream.

**Impact.** None.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/lib.rs:3355`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L3355) each /events request creates fresh broadcast receivers per topic; no shared subscription flag to double-register

**Sources.** [lodestar#5151](https://github.com/ChainSafe/lodestar/pull/5151)

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

**Verdict history.** not (checked) → partial (refuted)

**Sources.** [nimbus#4546](https://github.com/status-im/nimbus-eth2/pull/4546), [prysm#14713](https://github.com/OffchainLabs/prysm/pull/14713)

</details>


<a id="other-037"></a>
<details>
<summary><b>other-037</b> Derive head slot from head block — <i>implemented · low · S · cpu</i></summary>

**Idea.** Derive the head slot from the head block instead of keeping a separately tracked, duplicated field.

**Impact.** No duplicated head-slot field to keep in sync.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/canonical_head.rs:336-338`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L336-L338) head_slot() returns self.snapshot.beacon_block.slot()

**Skeptic check.** Verified head_slot reads the head snapshot block directly. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#11833](https://github.com/OffchainLabs/prysm/pull/11833)

</details>


<a id="other-038"></a>
<details>
<summary><b>other-038</b> Return hex strings directly from native code — <i>n/a · low · cpu</i></summary>

**Idea.** Return roots (for example shuffling decision roots) from native code already as hex strings instead of byte arrays that the caller converts, avoiding an extra conversion.

**Gap in Lighthouse.** Specific to JS native bindings returning typed arrays; Rust has no equivalent conversion cost.

**Impact.** None.

**Best measured result.** None (commit:lodestar@aef44205b31d)

**Sources.** [lodestar@aef44205b](https://github.com/ChainSafe/lodestar/commit/aef44205b31d)

</details>


<a id="other-039"></a>
<details>
<summary><b>other-039</b> Return promises directly, not awaited — <i>n/a · low · latency, cpu</i></summary>

**Idea.** In async functions, return a promise directly instead of awaiting it and returning the result, to skip an extra microtask per call; enforce with a lint rule.

**Gap in Lighthouse.** JS promise microtask behavior; Rust futures have no equivalent extra await cost.

**Impact.** None.

**Best measured result.** None (pr:lodestar#5117)

**Sources.** [lodestar#5117](https://github.com/ChainSafe/lodestar/pull/5117)

</details>


<a id="other-040"></a>
<details>
<summary><b>other-040</b> Move end-of-slot housekeeping earlier in the slot — <i>implemented · medium · latency</i></summary>

**Idea.** Schedule end-of-slot housekeeping and next-slot preparation earlier in the slot (for example at 19/24 and 7/8) so slow work such as state storage around epoch boundaries does not delay the start of the next slot.

**Impact.** Already done; heavy next-slot preparation starts at 9s, earlier than Nimbus's new 10.5s.

**Best measured result.** None (pr:nimbus#8621)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/state_advance_timer.rs:125-132`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L125-L132) state advance (including the epoch transition) at 3/4 of the slot, in a blocking task
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:134-141`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L134-L141) fork choice lookahead at 23/24 of the slot
- [`beacon_node/beacon_chain/src/beacon_chain.rs:7471-7496`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L7471-L7496) per_slot_task at slot start does only light cache pruning plus fork choice

**Skeptic check.** Lighthouse already does the slow next-slot work (state advance through the epoch boundary) at 3/4 of the slot, off the slot-start path. The earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#8621](https://github.com/status-im/nimbus-eth2/pull/8621)

</details>


<a id="other-041"></a>
<details>
<summary><b>other-041</b> Check deadline before expensive work — <i>not · low · M · cpu</i></summary>

**Idea.** Check request context/deadline liveness before expensive work and after waiting on locks, so work whose deadline passed is abandoned early.

**Gap in Lighthouse.** Pass a cancellation or deadline signal into expensive handlers (state-heavy endpoints) and check it before the work and after lock waits; warp does not cancel spawned blocking tasks when the client disconnects.

**Impact.** Only helps under API overload by dropping abandoned requests; no effect on a typical node.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/task_spawner.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/task_spawner.rs): no deadline or cancellation checks
- [`beacon_node/http_api/src/lib.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs): warp handlers run via task_spawner.blocking_response_task without liveness check

**Sources.** [prysm#15360](https://github.com/OffchainLabs/prysm/pull/15360)

</details>


<a id="other-042"></a>
<details>
<summary><b>other-042</b> Early exit in fork schedule scan — <i>implemented · low · S · cpu</i></summary>

**Idea.** When finding the next fork epoch, break out of the fork schedule loop at the first fork after the current epoch instead of scanning all forks and keeping a running minimum.

**Impact.** Negligible; tiny lists, not hot.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/core/chain_spec.rs:420-440`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/core/chain_spec.rs#L420-L440) fork_name_at_epoch returns at first fork with epoch &gt;= fork_epoch
- [`consensus/types/src/core/chain_spec.rs:407-412`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/core/chain_spec.rs#L407-L412) next_fork_epoch uses ForkName::next_fork
- [`consensus/types/src/core/chain_spec.rs:711-721`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/core/chain_spec.rs#L711-L721) next_digest_epoch uses .find() (early exit)

**Skeptic check.** Verified early exit in fork_name_at_epoch and next_digest_epoch. all_digest_epochs (695) builds and sorts a HashSet each call before the find, but on a list of about ten entries this is not a meaningful gap. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#8153](https://github.com/status-im/nimbus-eth2/pull/8153)

</details>


<a id="other-043"></a>
<details>
<summary><b>other-043</b> Embed mainnet genesis state in binary — <i>implemented · low · S · startup, sync</i></summary>

**Idea.** Embed the mainnet genesis state in the binary (and allow loading it from an SSZ file) so a fresh node does not rebuild genesis from eth1 deposit data.

**Impact.** Fresh mainnet nodes load the embedded genesis; no eth1 deposit rebuild.

**Best measured result.** None (pr:prysm#8614)

**Evidence (Lighthouse @ 928b61e719).**

- [`common/eth2_config/src/lib.rs:309-314`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/eth2_config/src/lib.rs#L309-L314) mainnet GenesisStateSource::IncludedBytes
- [`common/eth2_network_config/build.rs:1-52`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/eth2_network_config/build.rs#L1-L52) unzip genesis.ssz.zip for include_bytes!
- [`common/eth2_network_config/src/lib.rs:358-385`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/eth2_network_config/src/lib.rs#L358-L385) genesis.ssz loaded from a testnet dir if present

**Skeptic check.** Verified mainnet uses IncludedBytes (holesky/hoodi/chiado use a URL with checksum, which is also not a rebuild), and custom networks load genesis.ssz from file. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#8614](https://github.com/OffchainLabs/prysm/pull/8614)

</details>


<a id="other-044"></a>
<details>
<summary><b>other-044</b> Iterate map entries instead of key lookups — <i>n/a · low · S · cpu</i></summary>

**Idea.** Iterate maps by entries (key and value together) instead of iterating keys and looking each value up again.

**Impact.** Java-specific pattern.

**Evidence (Lighthouse @ 928b61e719).**

- Rust iterators over HashMap yield (k,v) pairs; no key-then-lookup idiom is needed

**Sources.** [teku#5277](https://github.com/Consensys-Incorporated/teku/pull/5277)

</details>


<a id="other-045"></a>
<details>
<summary><b>other-045</b> Slasher records keyed for range-scan pruning — <i>implemented · low · S · cpu, disk</i></summary>

**Idea.** Key slasher attestation and proposal records by epoch first (for example (target_epoch, root)) so pruning old epochs is a linear, resumable range delete by key prefix with no orphaned records, and proposer double votes are a keyed lookup, instead of scanning the whole store.

**Impact.** Pruning is a prefix range delete; proposer double vote is a keyed lookup. Slasher only.

**Evidence (Lighthouse @ 928b61e719).**

- [`slasher/src/database.rs:44`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/database.rs#L44) INDEXED_ATTESTATION_ID_DB keyed (target_epoch, hash)
- [`slasher/src/database.rs:115-130`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/database.rs#L115-L130) ProposerKey big-endian (slot, validator_index)
- [`slasher/src/database.rs:751-776`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/database.rs#L751-L776) prune_proposers cursor.delete_while from first key
- [`slasher/src/database.rs:778-816`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/database.rs#L778-L816) prune_indexed_attestations cursor.delete_while then delete referenced indexed attestations
- [`slasher/src/database.rs:702-727`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/database.rs#L702-L727) check_or_insert_block_proposal keyed get by (slot, validator)

**Skeptic check.** Verified epoch/slot-first keys with range-delete pruning and keyed proposer lookup. The indexed attestation deletes use per-id txn.del (a code comment notes a cursor could be used), which is minor. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#1948](https://github.com/sigp/lighthouse/pull/1948), [prysm#9328](https://github.com/OffchainLabs/prysm/pull/9328)

</details>


<a id="other-046"></a>
<details>
<summary><b>other-046</b> Faster big-integer arithmetic on carry intrinsics — <i>n/a · low · S · cpu</i></summary>

**Idea.** Use a big-integer (U256) library built on low-level carry/multiply intrinsics so add, mul and similar ops compile to tight code; check that U256 arithmetic hot paths use native word operations.

**Impact.** Rust U256 already uses ruint with native carry ops; no hot U256 arithmetic in the CL.

**Best measured result.** None (pr:nimbus#7936)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/rpc/methods.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/methods.rs) and [`consensus/types/src/attestation/subnet_id.rs:113`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/attestation/subnet_id.rs#L113) use alloy/ruint U256 only for node-id arithmetic, off the hot path

**Sources.** [nimbus#7936](https://github.com/status-im/nimbus-eth2/pull/7936), [nimbus#7938](https://github.com/status-im/nimbus-eth2/pull/7938)

</details>


<a id="other-047"></a>
<details>
<summary><b>other-047</b> Fast endian conversion in uint256 serialization — <i>n/a · low · S · cpu</i></summary>

**Idea.** Use word-wide endian-conversion routines in the uint256 library used for serialization instead of byte-by-byte swaps.

**Impact.** Nim-library detail; Rust uses native word-wide conversions.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/attestation/subnet_id.rs:113`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/attestation/subnet_id.rs#L113) U256::from_be_slice
- ruint 1.20.1 handles endianness natively

**Sources.** [nimbus#6750](https://github.com/status-im/nimbus-eth2/pull/6750)

</details>


<a id="other-048"></a>
<details>
<summary><b>other-048</b> Lookup-table hex decoder on hot paths — <i>not · low · S · cpu</i></summary>

**Idea.** Use a fast lookup-table hex-to-bytes decoder instead of a generic hex parser on hot paths such as API parsing, state cache file names and the op pool.

**Gap in Lighthouse.** Switch remaining hex::decode calls on API parsing paths to const_hex::decode; not a measured hotspot.

**Impact.** Marginal; hex decoding is not a visible cost on a mainnet node.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/execution_layer/src/engine_api/json_structures.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engine_api/json_structures.rs) and [`beacon_node/src/config.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/config.rs) use hex/const-hex generic decode
- Cargo.lock has const-hex 1.19.3 (fast, SIMD) and hex 0.4.3

**Sources.** [lodestar#7080](https://github.com/ChainSafe/lodestar/pull/7080)

</details>


<a id="other-049"></a>
<details>
<summary><b>other-049</b> Cheaper deposit-key derivation in testnet tooling — <i>n/a · low · S · cpu, startup</i></summary>

**Idea.** Derive fewer or cheaper keys when generating eth1 deposit keys from a mnemonic in testnet tooling (not on the node hot path).

**Impact.** Tooling only, not on the node path.

**Evidence (Lighthouse @ 928b61e719).**

- [`account_manager/src/validator/recover.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/account_manager/src/validator/recover.rs) and [`validator_manager/src/common.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_manager/src/common.rs) are CLI tooling

**Sources.** [lodestar#618](https://github.com/ChainSafe/lodestar/pull/618)

</details>


<a id="other-050"></a>
<details>
<summary><b>other-050</b> Faster test attester-slashing builder — <i>n/a · low · S · cpu</i></summary>

**Idea.** Speed up the test helper that builds attester slashings (test tooling only).

**Impact.** Test tooling only; no runtime effect.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/test_utils.rs:2864`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/test_utils.rs#L2864) test-only make_attester_slashing

**Sources.** [lighthouse@6f5593ef2](https://github.com/sigp/lighthouse/commit/6f5593ef2bf2)

</details>


<a id="other-051"></a>
<details>
<summary><b>other-051</b> Request finality update right after LC sync — <i>n/a · low · S · latency, startup</i></summary>

**Idea.** After light client sync completes, immediately request one finality update from peers instead of waiting minutes for the next gossiped one.

**Gap in Lighthouse.** Lighthouse has no light client sync client; it only serves LC data.

**Impact.** Nothing to speed up on a full node.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/service.rs:1106`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/service.rs#L1106) serves LC finality update RPC
- [`beacon_node/network/src/service.rs:1535`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/service.rs#L1535) gossip LC update handling

**Sources.** [nimbus#6752](https://github.com/status-im/nimbus-eth2/pull/6752)

</details>


<a id="other-052"></a>
<details>
<summary><b>other-052</b> Remove buffer copies in async TCP/HTTP read path — <i>n/a · low · S · cpu, bandwidth</i></summary>

**Idea.** Remove needless buffer copying and queueing in the async networking stack's TCP read and HTTP paths so socket reads go straight into the caller's buffer.

**Gap in Lighthouse.** Nim async stack copy issue; Lighthouse uses tokio/libp2p.

**Impact.** No equivalent code.

**Best measured result.** None (commit:nimbus@c7e775c0eeca)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/service/mod.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/mod.rs): tokio+libp2p stack

**Sources.** [nimbus@c7e775c0e](https://github.com/status-im/nimbus-eth2/commit/c7e775c0eeca)

</details>


<a id="other-053"></a>
<details>
<summary><b>other-053</b> Eth1 deposit cache download range fix — <i>n/a · low · S · sync, startup</i></summary>

**Idea.** Make the eth1 deposit/block cache download range the larger of the catch-up batch range and the normal range, so the cache syncs continuously instead of stalling.

**Gap in Lighthouse.** Eth1 deposit cache download removed from Lighthouse.

**Impact.** None.

**Evidence (Lighthouse @ 928b61e719).**

- beacon_node: no eth1 crate or deposit cache (only [`consensus/state_processing/src/builder_deposits_cache.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/builder_deposits_cache.rs))

**Sources.** [lighthouse#3358](https://github.com/sigp/lighthouse/pull/3358)

</details>


<a id="other-054"></a>
<details>
<summary><b>other-054</b> Deposit tree as flat list of roots — <i>n/a · low · S · memory</i></summary>

**Idea.** Keep the eth1 deposit tree as a flat list of deposit data roots (hash-tree-root backed) instead of a full nested layer-by-layer Merkle tree, shrinking the stored and hashed structure.

**Gap in Lighthouse.** Eth1 deposit tree no longer exists in Lighthouse.

**Impact.** None.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/builder_deposits_cache.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/builder_deposits_cache.rs) unrelated; no eth1 deposit tree in tree

**Sources.** [lodestar@fd4146824](https://github.com/ChainSafe/lodestar/commit/fd414682429b)

</details>


<a id="other-055"></a>
<details>
<summary><b>other-055</b> Plain loops instead of callback iteration — <i>n/a · low · S · cpu</i></summary>

**Idea.** Use plain for-of loops instead of forEach callbacks in hot paths, avoiding a closure call per element.

**Gap in Lighthouse.** JS forEach closure overhead; Rust has no such cost.

**Impact.** None.

**Best measured result.** None (pr:lodestar#6307)

**Evidence (Lighthouse @ 928b61e719).**

- Rust iterators compile to loops

**Sources.** [lodestar@8059f347e](https://github.com/ChainSafe/lodestar/commit/8059f347e91d), [lodestar#6307](https://github.com/ChainSafe/lodestar/pull/6307), [lodestar#2134](https://github.com/ChainSafe/lodestar/pull/2134)

</details>


<a id="other-056"></a>
<details>
<summary><b>other-056</b> Fork-neutral slasher on-disk attestation format — <i>implemented · medium · disk</i></summary>

**Idea.** Store slasher indexed attestations in a fork-neutral on-disk format so a fork upgrade does not require rewriting hundreds of gigabytes of slasher database.

**Impact.** Already done; a fork does not need a DB rewrite.

**Best measured result.** None (pr:lighthouse#5975)

**Evidence (Lighthouse @ 928b61e719).**

- [`slasher/src/database.rs:250-256`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/database.rs#L250-L256) IndexedAttestationOnDisk has a fork-neutral layout (Vec&lt;u64&gt; indices)
- [`slasher/src/database.rs:258-283`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/database.rs#L258-L283) into_indexed_attestation picks the variant from the target-epoch fork at read time

**Skeptic check.** This is Lighthouse's own PR #5975, and it is present on unstable. The earlier verdict is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#5975](https://github.com/sigp/lighthouse/pull/5975)

</details>


<a id="other-057"></a>
<details>
<summary><b>other-057</b> Whole-list swap-or-not shuffle — <i>implemented · high · S · cpu</i></summary>

**Idea.** Shuffle the whole validator list in one pass with a swap-or-not variant that computes each round's hashes once per list, instead of shuffling each index separately.

**Impact.** Committee shuffling is one whole-list pass per epoch.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/swap_or_not_shuffle/src/shuffle_list.rs:92-160`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/swap_or_not_shuffle/src/shuffle_list.rs#L92-L160) shuffle_list whole-list swap-or-not, one hash per 256 positions per round
- [`consensus/types/src/state/committee_cache.rs:147`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/committee_cache.rs#L147) committee cache built with shuffle_list

**Skeptic check.** Verified shuffle_list is used for the committee cache. The remaining compute_shuffled_index callers (beacon_state.rs:1372, 1800, 3725) are proposer and sync committee sampling, which the spec defines per index over a candidate stream. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#266](https://github.com/sigp/lighthouse/pull/266)

</details>


<a id="other-058"></a>
<details>
<summary><b>other-058</b> Tick delay computed relative to genesis — <i>implemented · low · latency</i></summary>

**Idea.** Compute the delay to the next slot/interval tick relative to genesis time, not the unix epoch, so ticks do not fire hundreds of milliseconds late when genesis is not aligned to the interval.

**Impact.** Ticks are computed relative to genesis, so a genesis time that is not aligned to the interval adds no delay.

**Best measured result.** None (pr:ethlambda#392)

**Evidence (Lighthouse @ 928b61e719).**

- [`common/slot_clock/src/manual_slot_clock.rs:66-72`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/slot_clock/src/manual_slot_clock.rs#L66-L72) duration_to_next_slot_from = start_of(slot+1) - now
- [`common/slot_clock/src/manual_slot_clock.rs:149-157`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/slot_clock/src/manual_slot_clock.rs#L149-L157) start_of = genesis_duration + n*slot_duration
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:118-132`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L118-L132) intra-slot timers are offsets from duration_to_next_slot

**Skeptic check.** Confirmed that the slot clock and the timers built on it are anchored to genesis. The earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

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


<a id="other-060"></a>
<details>
<summary><b>other-060</b> into_owned instead of to_string on Cow — <i>not · low · S · cpu</i></summary>

**Idea.** Convert a lossy-UTF8 Cow&lt;str&gt; to String with into_owned() instead of to_string(), avoiding the Display formatting path (micro-optimisation).

**Gap in Lighthouse.** Replace .to_string() with .into_owned() on the Cow in methods.rs:62 and graffiti.rs:20.

**Impact.** Negligible: tiny strings on cold paths.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/rpc/methods.rs:62`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/methods.rs#L62) lossy().to_string()
- [`consensus/types/src/core/graffiti.rs:20`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/core/graffiti.rs#L20) same

**Sources.** [ethlambda#152](https://github.com/lambdaclass/ethlambda/pull/152)

</details>


<a id="other-061"></a>
<details>
<summary><b>other-061</b> Keep torrent metadata for resumed snapshot sync — <i>n/a · low · startup, sync</i></summary>

**Idea.** Keep snapshot torrent metadata files on disk before initial sync completes and recheck data only when an infohash changes, so a resumed snapshot sync starts faster.

**Impact.** Lighthouse has no snapshot torrent downloader.

**Best measured result.** None (pr:caplin#18056)

**Evidence (Lighthouse @ 928b61e719).**

- no torrent snapshot sync in Lighthouse (checkpoint sync over HTTP)

**Sources.** [caplin#18056](https://github.com/erigontech/erigon/pull/18056)

</details>


<a id="other-062"></a>
<details>
<summary><b>other-062</b> Lazy deposit proofs at proposal time — <i>n/a · low · cpu</i></summary>

**Idea.** After genesis, do not build a Merkle proof for every deposit when processing deposit logs; compute proofs only when a block proposal needs them.

**Impact.** Eth1 deposit-proof building is obsolete after Electra (EIP-6110).

**Evidence (Lighthouse @ 928b61e719).**

- beacon_node/eth1 / deposit cache: post-Electra deposits come from EL requests

**Sources.** [prysm#9289](https://github.com/OffchainLabs/prysm/pull/9289)

</details>


<a id="other-063"></a>
<details>
<summary><b>other-063</b> Committees as borrowed slices of shuffled list — <i>implemented · low · S · memory, cpu</i></summary>

**Idea.** Split the shuffled active validator list into committees as borrowed slice views through a lazy iterator, instead of copying each committee into a new vector.

**Impact.** Committees borrow the cached shuffled list; no per-committee copy.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/committee_cache.rs:202-228`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/committee_cache.rs#L202-L228) get_beacon_committee returns BeaconCommittee&lt;'_&gt; with a slice from compute_committee
- [`consensus/types/src/state/committee_cache.rs:195`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/committee_cache.rs#L195) shuffling() returns &amp;[usize]

**Skeptic check.** Verified committees are borrowed slices of the shuffling. get_beacon_committees_at_slot / get_all_beacon_committees collect a Vec of borrowed BeaconCommittee structs, not copies of indices. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse@874a0babb](https://github.com/sigp/lighthouse/commit/874a0babbb0f)

</details>


<a id="other-064"></a>
<details>
<summary><b>other-064</b> Compile regexes once in static cells — <i>partial · low · S · cpu, startup</i></summary>

**Idea.** Compile regexes once in static lazy cells instead of on every call in loops such as keystore file detection while scanning directories.

**Gap in Lighthouse.** Move the two regexes in the keystore filename detector in validator_definitions.rs into static LazyLock&lt;Regex&gt;. Other regex users (lighthouse_version, rpc/methods.rs:60) should be checked too.

**Impact.** Cold path (validator dir scan); only saves regex compile per file at VC startup/scan, negligible on a mainnet node.

**Evidence (Lighthouse @ 928b61e719).**

- [`common/account_utils/src/validator_definitions.rs:522`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/account_utils/src/validator_definitions.rs#L522) Regex::new compiled on every call
- [`common/account_utils/src/validator_definitions.rs:531`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/account_utils/src/validator_definitions.rs#L531) second regex also per call

**Sources.** [lighthouse#7738](https://github.com/sigp/lighthouse/pull/7738)

</details>


<a id="other-065"></a>
<details>
<summary><b>other-065</b> Linear max scan in slashing-protection import — <i>implemented · low · S · cpu, startup</i></summary>

**Idea.** On slashing-protection interchange import, find the highest-slot block with a linear scan instead of sorting all signed blocks, and drop the redundant attestation sort.

**Impact.** Interchange import is linear; no sort.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/slashing_protection/src/slashing_database.rs:866`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/slashing_protection/src/slashing_database.rs#L866) signed_blocks.iter().max_by_key(slot)
- [`validator_client/slashing_protection/src/slashing_database.rs:881-888`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/slashing_protection/src/slashing_database.rs#L881-L888) max_by_key for source and target epochs

**Skeptic check.** Verified linear max scans in import_interchange_record, and no sort calls in the slashing_protection src. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#7311](https://github.com/status-im/nimbus-eth2/pull/7311), [nimbus#7312](https://github.com/status-im/nimbus-eth2/pull/7312)

</details>


<a id="other-066"></a>
<details>
<summary><b>other-066</b> Multi-threaded event-channel subscribers — <i>n/a · low · latency</i></summary>

**Idea.** Let event-channel subscribers, such as the storage request handler, process events on several threads so requests are served in parallel.

**Impact.** Design specific to Teku's event channels.

**Evidence (Lighthouse @ 928b61e719).**

- tokio runtime/ rayon already parallel; no Java-style event-channel threads

**Sources.** [teku#1335](https://github.com/Consensys-Incorporated/teku/pull/1335)

</details>


<a id="other-067"></a>
<details>
<summary><b>other-067</b> Native buffer compare for roots — <i>n/a · low · cpu</i></summary>

**Idea.** Compare byte arrays such as roots with a native memory compare instead of a per-byte script loop.

**Impact.** Rust slice equality already uses memcmp.

**Best measured result.** None (pr:lodestar#7866)

**Evidence (Lighthouse @ 928b61e719).**

- Rust [u8;32]/Hash256 == compiles to memcmp

**Sources.** [lodestar#7866](https://github.com/ChainSafe/lodestar/pull/7866)

</details>


<a id="other-068"></a>
<details>
<summary><b>other-068</b> Worker-split utility for genesis generation — <i>n/a · low · cpu</i></summary>

**Idea.** Split array work across worker threads with a shared utility and use it for genesis state and deposit generation, for near-linear speedup.

**Impact.** Genesis state generation is not on a mainnet node's hot path.

**Best measured result.** None (pr:prysm#3813)

**Evidence (Lighthouse @ 928b61e719).**

- genesis generation is test/tooling only (testing/ and lcli)

**Sources.** [prysm#3813](https://github.com/OffchainLabs/prysm/pull/3813)

</details>


<a id="other-069"></a>
<details>
<summary><b>other-069</b> Concurrent graceful shutdown tasks — <i>partial · low · S · latency</i></summary>

**Idea.** Run independent shutdown tasks (node stop, validator stop, ENR write, DB cleanup) concurrently instead of one after another, so graceful shutdown finishes sooner.

**Gap in Lighthouse.** Run the three persist calls in BeaconChain::drop concurrently (or via join). Gain is milliseconds.

**Impact.** Shortens graceful exit by well under a second; no steady-state effect.

**Evidence (Lighthouse @ 928b61e719).**

- [`lighthouse/src/main.rs:874`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/lighthouse/src/main.rs#L874) block until shutdown then shutdown_on_idle
- [`lighthouse/environment/src/lib.rs:452`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/lighthouse/environment/src/lib.rs#L452) runtime.shutdown_timeout
- [`beacon_node/beacon_chain/src/beacon_chain.rs:8457`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L8457) Drop persists op pool, custody, fork choice sequentially

**Sources.** [lodestar@b2e11ea1d](https://github.com/ChainSafe/lodestar/commit/b2e11ea1d831)

</details>


<a id="other-070"></a>
<details>
<summary><b>other-070</b> Concurrent validator generation in test builder — <i>n/a · low · S · cpu, startup</i></summary>

**Idea.** Generate the initial validator objects concurrently in the test state builder (test tooling only).

**Gap in Lighthouse.** Test tooling only; no runtime effect.

**Impact.** None on a node.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/test_utils.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/test_utils.rs): test harness only

**Sources.** [lighthouse@5e5cfb782](https://github.com/sigp/lighthouse/commit/5e5cfb782ef8)

</details>


<a id="other-071"></a>
<details>
<summary><b>other-071</b> Persist eth1 deposit checkpoints to disk — <i>n/a · low · S · startup, sync</i></summary>

**Idea.** Persist eth1 data and deposit data (with the processed block) to disk so a restart does not replay all deposit logs from the eth1 chain.

**Gap in Lighthouse.** Eth1 deposit log syncing was removed from Lighthouse (no eth1 crate), so there is no deposit cache to persist.

**Impact.** None.

**Evidence (Lighthouse @ 928b61e719).**

- beacon_node/ has no eth1 crate (ls beacon_node)

**Sources.** [prysm#4329](https://github.com/OffchainLabs/prysm/pull/4329), [lodestar@dcd7304f5](https://github.com/ChainSafe/lodestar/commit/dcd7304f59b6)

</details>


<a id="other-072"></a>
<details>
<summary><b>other-072</b> Hardware popcount for bitfields — <i>implemented · low · S · cpu</i></summary>

**Idea.** Count set bits in aggregation and other bitfields with word-wide hardware popcount instead of a per-bit loop.

**Impact.** None worth having; byte-wise count_ones already avoids a per-bit loop. Counting u64 words would be a micro-gain.

**Evidence (Lighthouse @ 928b61e719).**

- ethereum_ssz-0.10.4/src/bitfield.rs:510 num_set_bits sums byte.count_ones() (hardware popcount per byte, auto-vectorizable)
- ethereum_ssz-0.10.4/src/bitfield.rs:505 is_zero is a byte scan

**Skeptic check.** Verified num_set_bits uses count_ones on bytes, not a per-bit loop; no per-bit counting loops on consensus paths found by grep. Earlier verdict right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#547](https://github.com/OffchainLabs/prysm/pull/547)

</details>


<a id="other-073"></a>
<details>
<summary><b>other-073</b> Preallocate capacity in dedupe helpers — <i>n/a · low · S · memory, cpu</i></summary>

**Idea.** In dedupe helpers, preallocate the map and output vector capacity and append, avoiding rehash growth and reallocation.

**Gap in Lighthouse.** Lighthouse has no equivalent dedupe helper hot path; where sets are built it already preallocates capacity, and the gain is a micro tweak.

**Impact.** Negligible.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/observed_attesters.rs:150`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/observed_attesters.rs#L150) HashSet::with_capacity
- [`beacon_node/network/src/sync/batch.rs:204`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/sync/batch.rs#L204) with_capacity

**Sources.** [prysm#15513](https://github.com/OffchainLabs/prysm/pull/15513), [caplin#22676](https://github.com/erigontech/erigon/pull/22676)

</details>


<a id="other-074"></a>
<details>
<summary><b>other-074</b> Primitive-specialized collections instead of boxed — <i>n/a · low · S · memory, cpu</i></summary>

**Idea.** Use primitive-specialized collections (int maps and lists) instead of collections of boxed integers to cut allocation and memory.

**Gap in Lighthouse.** Rust has no boxed integers; Vec&lt;usize&gt; and HashMap&lt;u64,_&gt; are already primitive-specialized.

**Impact.** None.

**Sources.** [teku#5166](https://github.com/Consensys-Incorporated/teku/pull/5166)

</details>


<a id="other-075"></a>
<details>
<summary><b>other-075</b> Cache proposer indices per epoch — <i>implemented · high · S · cpu</i></summary>

**Idea.** Cache the proposer indices of each epoch so they are not recomputed from the state for every request or block.

**Impact.** Proposer indices are cached per (epoch, decision root) for gossip block verification and the duties API; post-Fulu the state itself carries the lookahead.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_proposer_cache.rs:86`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_proposer_cache.rs#L86) LruCache&lt;(Epoch, decision root), Arc&lt;OnceCell&lt;EpochBlockProposers&gt;&gt;&gt;
- [`beacon_node/beacon_chain/src/beacon_proposer_cache.rs:133`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_proposer_cache.rs#L133) get_or_insert_key
- [`beacon_node/http_api/src/proposer_duties.rs:172`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/proposer_duties.rs#L172) API duties served from beacon_proposer_cache
- [`consensus/types/src/state/beacon_state.rs:1655`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L1655) post-Fulu get_beacon_proposer_index reads proposer_lookahead

**Skeptic check.** Confirmed the cache is used by gossip block verification and the proposer duties API; block processing uses proposer_lookahead post-Fulu. Earlier verdict right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#722](https://github.com/sigp/lighthouse/pull/722)

</details>


<a id="other-076"></a>
<details>
<summary><b>other-076</b> Prune persisted invalid-object debug dumps — <i>n/a · low · S · disk</i></summary>

**Idea.** Delete persisted invalid SSZ debug objects older than a retention period (for example 7 days) at startup and periodically, so the debug directory does not grow without bound.

**Gap in Lighthouse.** Lighthouse does not persist invalid SSZ objects to disk, so there is nothing to prune.

**Impact.** None.

**Evidence (Lighthouse @ 928b61e719).**

- beacon_node/ grep for invalid ssz dumps found only error variants, no persistence

**Sources.** [lodestar#5388](https://github.com/ChainSafe/lodestar/pull/5388)

</details>


<a id="other-077"></a>
<details>
<summary><b>other-077</b> Range primitive to initialise shuffle indices — <i>n/a · low · S · cpu</i></summary>

**Idea.** Initialise the shuffle index list with a range-to-array primitive instead of a manual loop.

**Impact.** None; Rust (0..n).collect() is already a range iterator. Java-specific micro tweak; Rust ranges collect directly.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/swap_or_not_shuffle/src/shuffle_list.rs:92`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/swap_or_not_shuffle/src/shuffle_list.rs#L92) takes a Vec built by caller

**Sources.** [teku#510](https://github.com/Consensys-Incorporated/teku/pull/510)

</details>


<a id="other-078"></a>
<details>
<summary><b>other-078</b> Raw key lists instead of encoded slasher index — <i>implemented · low · cpu, disk</i></summary>

**Idea.** For the slasher's per-(epoch, validator) index of attestations, store a raw concatenated list of keys in the DB instead of a protobuf-style encoded value, avoiding decode/encode on every update and lookup.

**Impact.** Already avoided; the index is one fixed-width key per (validator, epoch) with a raw id value, and there is no list to decode.

**Best measured result.** None (pr:prysm#4832)

**Evidence (Lighthouse @ 928b61e719).**

- [`slasher/src/database.rs:91-103`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/database.rs#L91-L103) AttesterKey is raw (target_epoch mod history, validator) bytes
- [`slasher/src/database.rs:644-648`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/database.rs#L644-L648) attesters_db value is the raw 6-byte IndexedAttestationId
- [`slasher/src/database.rs:170-232`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/database.rs#L170-L232) IndexedAttestationIdKey / IndexedAttestationId are fixed raw byte arrays

**Skeptic check.** Lighthouse stores one raw record per (validator, target epoch) and does not encode lists, so the codec overhead that Prysm removed never existed. The earlier verdict is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

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


<a id="other-080"></a>
<details>
<summary><b>other-080</b> Remove redundant clones in services — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Remove redundant Arc and value clones in long-lived services and other code by moving or borrowing values.

**Impact.** Marginal; generic clone cleanup with no specific hot path.

**Evidence (Lighthouse @ 928b61e719).**

- pr:lighthouse#1142 merged
- pr:lighthouse#4964 merged

**Skeptic check.** The idea is generic clone removal and the Lighthouse members are merged PRs; no specific hot-path mechanism to refute. Upheld.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#1142](https://github.com/sigp/lighthouse/pull/1142), [lighthouse#4964](https://github.com/sigp/lighthouse/pull/4964), [ethlambda#288](https://github.com/lambdaclass/ethlambda/pull/288), [nimbus#8251](https://github.com/status-im/nimbus-eth2/pull/8251)

</details>


<a id="other-081"></a>
<details>
<summary><b>other-081</b> Remove needless async on synchronous paths — <i>n/a · low · S · cpu, latency</i></summary>

**Idea.** Remove async functions and awaits from code that is synchronous, avoiding promise allocation and event-loop hops.

**Impact.** None. Tokio async has no promise hop cost like JS; sync paths use spawn_blocking (slasher/service/src/service.rs:84).

**Sources.** [lodestar@1713a47a2](https://github.com/ChainSafe/lodestar/commit/1713a47a24b2)

</details>


<a id="other-082"></a>
<details>
<summary><b>other-082</b> Fixed-layout shared memory for thread messages — <i>n/a · low · S · cpu, latency</i></summary>

**Idea.** Pass fixed-size messages between threads through shared memory with a fixed SSZ-style layout instead of structured cloning.

**Impact.** None. Lighthouse threads pass Rust structs via channels with no structured clone.

**Best measured result.** None (pr:lodestar#5302)

**Sources.** [lodestar#5302](https://github.com/ChainSafe/lodestar/pull/5302)

</details>


<a id="other-083"></a>
<details>
<summary><b>other-083</b> Download genesis or anchor state only once — <i>implemented · low · S · startup, bandwidth</i></summary>

**Idea.** At startup with an empty DB or during checkpoint sync, download the genesis/anchor state only once, and do not fetch the finalized state a second time to use as genesis or across retries.

**Impact.** None; each startup branch fetches genesis at most once and the finalized state once, and never reuses the finalized state as genesis.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/client/src/builder.rs:439`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/client/src/builder.rs#L439) finalized state downloaded once in CheckpointSyncUrl branch
- [`beacon_node/client/src/builder.rs:493`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/client/src/builder.rs#L493) genesis_state() called once per start (real genesis, not the finalized state)
- [`beacon_node/client/src/builder.rs:993`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/client/src/builder.rs#L993) genesis_state helper
- [`common/eth2_network_config/src/lib.rs:207`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/eth2_network_config/src/lib.rs#L207) genesis_state bundled bytes or one checksummed download

**Skeptic check.** Checked all genesis_state call sites: one per ClientGenesis branch; checkpoint sync downloads finalized state and block once. Earlier verdict right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#6452](https://github.com/status-im/nimbus-eth2/pull/6452), [grandine@71af31767](https://github.com/grandinetech/grandine/commit/71af317677a9)

</details>


<a id="other-084"></a>
<details>
<summary><b>other-084</b> Reward aggregates computed during data generation — <i>n/a · low · S · cpu, disk</i></summary>

**Idea.** Compute validator reward aggregates while generating the per-epoch data instead of in a separate pass, with an option to store only the aggregates for a much smaller data set.

**Impact.** None. Reward data generation tooling is not a Lighthouse feature.

**Best measured result.** None (commit:nimbus@ac16eb469168)

**Sources.** [nimbus@ac16eb469](https://github.com/status-im/nimbus-eth2/commit/ac16eb469168)

</details>


<a id="other-085"></a>
<details>
<summary><b>other-085</b> Restart from DB state, skip network fetch — <i>implemented · medium · startup, bandwidth</i></summary>

**Idea.** On restart, start from the state already in the database (genesis or checkpoint origin, if still within the weak subjectivity period) and download a checkpoint or genesis state only when the DB is empty or stale.

**Impact.** Already done; a restart makes no network state download.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/client/src/builder.rs:282`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/client/src/builder.rs#L282) store_contains_beacon_chain
- [`beacon_node/client/src/builder.rs:295-306`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/client/src/builder.rs#L295-L306) an existing chain forces ClientGenesis::FromStore, even when checkpoint sync is configured
- [`beacon_node/client/src/builder.rs:507`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/client/src/builder.rs#L507) FromStore =&gt; resume_from_db, with no genesis_state()/checkpoint fetch

**Skeptic check.** Confirmed that the FromStore path skips both the genesis_state download and the checkpoint download. Lighthouse does not check whether the stored state is outside the weak subjectivity period, but that is a safety matter, not a performance one.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#4563](https://github.com/ChainSafe/lodestar/pull/4563), [prysm#10881](https://github.com/OffchainLabs/prysm/pull/10881), [grandine@33cf0a979](https://github.com/grandinetech/grandine/commit/33cf0a979653)

</details>


<a id="other-086"></a>
<details>
<summary><b>other-086</b> Skip slashing DB write when none found — <i>partial · low · S · disk</i></summary>

**Idea.** Skip the slashing DB write transaction when a detection pass found no slashings.

**Gap in Lighthouse.** Skip commit (abort txn) when no new data/slashings were processed; but the txn also stores attestations/blocks so it is usually non-empty.

**Impact.** Negligible: txn nearly always has writes from queued attestations. Slashings are only pushed under is_empty checks (slasher.rs:123,226); the write txn is unconditional.

**Evidence (Lighthouse @ 928b61e719).**

- [`slasher/src/slasher.rs:93-99`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/slasher.rs#L93-L99) process_queued always begin_rw_txn and commit()

**Sources.** [prysm#6432](https://github.com/OffchainLabs/prysm/pull/6432)

</details>


<a id="other-087"></a>
<details>
<summary><b>other-087</b> Static error construction without formatting — <i>n/a · low · cpu</i></summary>

**Idea.** Build error values for fixed messages without a formatting call (for example in signature decoding), avoiding formatting work on error paths.

**Impact.** Error-path formatting only; Lighthouse uses typed enum errors and blst error codes, negligible and no matching hot path.

**Best measured result.** None (pr:prysm#15007)

**Evidence (Lighthouse @ 928b61e719).**

- Searched for signature decode paths; errors in Lighthouse are enum variants, not formatted strings

**Sources.** [prysm#15007](https://github.com/OffchainLabs/prysm/pull/15007), [nimbus#2159](https://github.com/status-im/nimbus-eth2/pull/2159)

</details>


<a id="other-088"></a>
<details>
<summary><b>other-088</b> Slasher writes only touched validators per batch — <i>implemented · medium · S · cpu, memory, disk, latency</i></summary>

**Idea.** In the slasher, run double-vote detection once per batch set instead of per validator-chunk batch, and write only the touched validators' latest-written epochs instead of the whole registry in one huge DB transaction.

**Impact.** None left; Prysm's change says the result 'matches' Lighthouse.

**Best measured result.** None (pr:prysm#9833)

**Evidence (Lighthouse @ 928b61e719).**

- [`slasher/src/slasher.rs:194-197`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/slasher.rs#L194-L197) batch grouped by validator chunk, all in one txn from process_queued
- [`slasher/src/slasher.rs:276-305`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/slasher.rs#L276-L305) check_double_votes covers only validators of the subqueue chunk
- [`slasher/src/array.rs:517-520`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/array.rs#L517-L520) current epoch written only for validators of touched chunks

**Second check.** Read prysm#9833: it was explicitly modelled on Lighthouse's slasher and says it now 'matches' Lighthouse. Lighthouse already does the double-vote check only for attesting validators per chunk and writes only touched chunks. The remaining per-chunk current_epoch writes are needed because epoch_update_for_validator neutralises the whole chunk, so they are part of the design, not a gap.

**Skeptic check.** Confirmed that double-vote checks run once per attestation and per chunk, and that current-epoch writes are limited to the touched validator chunks. The earlier evidence is correct.

**Verdict history.** partial (checked) → implemented (refuted) → implemented (skeptic)

**Sources.** [prysm#9833](https://github.com/OffchainLabs/prysm/pull/9833)

</details>


<a id="other-089"></a>
<details>
<summary><b>other-089</b> Slasher accepts only verified, bounded attestations — <i>implemented · medium · S · memory</i></summary>

**Idea.** Feed only verified attestations to the slasher and cap the validator index it accepts, so a bogus huge index cannot make it allocate unbounded memory.

**Impact.** Already done; no further gain.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/attestation_verification.rs:443`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L443)
- [`beacon_node/beacon_chain/src/attestation_verification.rs:493`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L493)
- [`beacon_node/beacon_chain/src/attestation_verification.rs:837`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L837)
- [`beacon_node/beacon_chain/src/attestation_verification.rs:1172`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1172)
- [`slasher/src/attestation_queue.rs:14`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/attestation_queue.rs#L14)
- [`slasher/src/attestation_queue.rs:84`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/attestation_queue.rs#L84)

**Skeptic check.** Confirmed: process_slash_info verifies the signature before slasher.accept_attestation for every unchecked-signature path, verified gossip paths feed already-verified indexed attestations, and group_by_validator_chunk_index stops at MAX_VALIDATOR_INDEX (break is correct since the BTreeMap is sorted by index). Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#9141](https://github.com/sigp/lighthouse/pull/9141)

</details>


<a id="other-090"></a>
<details>
<summary><b>other-090</b> Slasher processing keeps up with chain head — <i>implemented · low · S · latency</i></summary>

**Idea.** Make slasher processing follow the chain head instead of lagging behind, so detection latency stays bounded.

**Impact.** None; each run drains the full queue at the current epoch, so detection latency is bounded by update_period plus run time.

**Evidence (Lighthouse @ 928b61e719).**

- [`slasher/service/src/service.rs:81`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/service/src/service.rs#L81) run_notifier slot-aligned interval with sync_channel(1) try_send (drops ticks when busy)
- [`slasher/service/src/service.rs:111`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/service/src/service.rs#L111) run_processor processes the whole queue with the current epoch
- [`slasher/src/slasher.rs:140`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/slasher.rs#L140) attestation_queue.dequeue drains all queued attestations per run

**Skeptic check.** Verified that ticks carry the current epoch and the processor drains the whole queue, so it does not fall behind on a backlog of ticks. Earlier verdict right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#5124](https://github.com/OffchainLabs/prysm/pull/5124)

</details>


<a id="other-091"></a>
<details>
<summary><b>other-091</b> Smaller slasher span bucket layout — <i>n/a · low · S · disk</i></summary>

**Idea.** Restructure the slasher span database layout to reduce the size and complexity of the span bucket.

**Impact.** None; the Prysm change restructures Prysm's own span bucket layout. Lighthouse was designed from the start with a compact chunked u16 layout.

**Evidence (Lighthouse @ 928b61e719).**

- [`slasher/src/array.rs:14`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/array.rs#L14) MAX_DISTANCE u16 cells
- [`slasher/src/array.rs:16`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/array.rs#L16) chunk_size x validator_chunk_size 2D chunk layout
- [`slasher/src/array.rs:179`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/array.rs#L179) zlib-compressed chunks

**Skeptic check.** Confirmed the compact chunked, compressed u16 span matrix. Lighthouse has nothing to port, so n/a fits better than implemented, but either way there is no gap.

**Verdict history.** implemented (checked) → n/a (skeptic)

**Sources.** [prysm#5925](https://github.com/OffchainLabs/prysm/pull/5925)

</details>


<a id="other-092"></a>
<details>
<summary><b>other-092</b> EIP-4881 snapshot deposit tree — <i>n/a · low · memory</i></summary>

**Idea.** Use a deposit Merkle tree that stores only branch nodes and supports finalized snapshots (EIP-4881) instead of the full leaf tree, and build the tree once per block with deposits instead of per-deposit views.

**Impact.** Lighthouse has no live eth1 deposit cache; the tree is only built in genesis.rs (interop/test). Post-Electra deposits come via requests in the payload.

**Best measured result.** None (pr:teku#5501)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/client/src/builder.rs:504`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/client/src/builder.rs#L504) deposit contract genesis 'no longer supported'
- [`consensus/state_processing/src/common/deposit_data_tree.rs:69`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/common/deposit_data_tree.rs#L69) snapshot/from_snapshot exist but only used by genesis.rs

**Sources.** [teku#5501](https://github.com/Consensys-Incorporated/teku/pull/5501)

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


<a id="other-094"></a>
<details>
<summary><b>other-094</b> Transfer large buffers to workers, not copy — <i>n/a · low · cpu, latency</i></summary>

**Idea.** When sending payloads above about 400 bytes (blocks, blobs) to a worker thread, transfer ownership of the buffer instead of copying it, because copy cost grows linearly with size while transfer stays constant.

**Impact.** Rust threads share memory via Arc; no structured-clone copy between workers exists.

**Best measured result.** None (pr:lodestar#5470)

**Evidence (Lighthouse @ 928b61e719).**

- [`slasher/src/slasher.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/slasher.rs): slasher runs in plain Rust threads sharing Arc data

**Sources.** [lodestar#5470](https://github.com/ChainSafe/lodestar/pull/5470)

</details>


<a id="other-095"></a>
<details>
<summary><b>other-095</b> Word-wide is-zero check for hashes — <i>implemented · low · S · cpu</i></summary>

**Idea.** Check whether a 32-byte hash is zero by comparing it as wide words (u64 chunks) instead of a byte-wise loop; this was 25% of time during sync.

**Impact.** None; Hash256 zero check is already a fixed-size array equality.

**Best measured result.** None (pr:nimbus#6682)

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/alloy-primitives-1.7.3/src/bits/fixed.rs:696
- [`beacon_node/store/src/iter.rs:264`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/iter.rs#L264)
- [`consensus/proto_array/src/proto_array.rs:832`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L832)

**Skeptic check.** Cargo.lock pins alloy-primitives 1.7.3 (not 1.7.1 as cited), but is_zero is the same `*self == Self::ZERO` on [u8;32], which compiles to wide compares, not a byte loop. The Nimbus slowdown was specific to its isZeroMemory; Lighthouse has no equivalent.

**Verdict history.** implemented (checked) → implemented (skeptic)

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


<a id="other-097"></a>
<details>
<summary><b>other-097</b> Slasher DB lookup once per unique detection — <i>implemented · low · S · cpu, disk</i></summary>

**Idea.** For duplicate attestations in the slasher, do the database lookup once per unique detection instead of once per attesting index.

**Impact.** Duplicates are collapsed per batch and the data-root lookups for conflicting records are cached, so the DB work repeats only for the per-validator record check that is required anyway.

**Evidence (Lighthouse @ 928b61e719).**

- [`slasher/src/slasher.rs:160`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/slasher.rs#L160) AttestationBatch dedups attestations before DB work
- [`slasher/src/slasher.rs:166`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/slasher.rs#L166) store_indexed_attestation once per unique attestation
- [`slasher/src/database.rs:552`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/database.rs#L552) get_attestation_data_root with LRU attestation_root_cache
- [`slasher/src/database.rs:595`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/database.rs#L595) check_and_update_attester_record

**Skeptic check.** Verified batch dedup and the root cache. The per-validator attester record read is inherent to double-vote detection. Upheld.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#5886](https://github.com/OffchainLabs/prysm/pull/5886)

</details>


<a id="other-098"></a>
<details>
<summary><b>other-098</b> Build genesis state incrementally from deposit stream — <i>n/a · low · startup, cpu, memory</i></summary>

**Idea.** While waiting for genesis, build the genesis state incrementally as deposits arrive, keeping a tree-backed state and deposit tree, instead of rebuilding the state from all deposits at each check.

**Impact.** Lighthouse no longer watches eth1 for genesis; mainnet genesis is loaded from SSZ. Nothing to speed up.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/client/src/builder.rs:504`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/client/src/builder.rs#L504) deposit-contract genesis removed
- [`consensus/state_processing/src/genesis.rs:37`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/genesis.rs#L37) incremental DepositDataTree push_leaf per deposit, only for interop/tests

**Sources.** [lodestar@77742d13d](https://github.com/ChainSafe/lodestar/commit/77742d13d791)

</details>


<a id="other-099"></a>
<details>
<summary><b>other-099</b> Hardware-accelerated SHA-256 selected by CPU — <i>implemented · low · S · cpu</i></summary>

**Idea.** Pick the SHA-256 implementation used for shuffling by target CPU, using the SHA-extension library implementation when available instead of the generic one. Check which sha256 backend the shuffling hashes call in Lighthouse.

**Impact.** Shuffling hashes go through DynamicImpl::best(). On x86_64 this picks sha2 with SHA-NI when cpufeatures detects it, else ring. ring also uses ARMv8 SHA instructions on aarch64.

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/registry/src/*/ethereum_hashing-0.8.0/src/lib.rs:99-146
- Cargo.toml:153
- [`consensus/swap_or_not_shuffle/src/shuffle_list.rs:2`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/swap_or_not_shuffle/src/shuffle_list.rs#L2),34,48

**Skeptic check.** Verified that the runtime CPU detection in ethereum_hashing 0.8.0 is used by shuffle_list via hash_fixed. The earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#774](https://github.com/ChainSafe/lodestar/pull/774)

</details>


<a id="other-100"></a>
<details>
<summary><b>other-100</b> Hash shuffle rounds from reusable buffers — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** In swap-or-not shuffling, hash from slices of reusable buffers instead of allocating a small buffer per hash call. Check whether Lighthouse's shuffle allocates per hash.

**Impact.** Neither shuffle path allocates per hash. shuffle_list hashes slices of one stack [u8;37] buffer, and compute_shuffled_index streams into a hash context that returns a fixed array.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/swap_or_not_shuffle/src/shuffle_list.rs:12-50`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/swap_or_not_shuffle/src/shuffle_list.rs#L12-L50)
- [`consensus/swap_or_not_shuffle/src/shuffle_list.rs:106-130`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/swap_or_not_shuffle/src/shuffle_list.rs#L106-L130)
- [`consensus/swap_or_not_shuffle/src/compute_shuffled_index.rs:45-75`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/swap_or_not_shuffle/src/compute_shuffled_index.rs#L45-L75)

**Skeptic check.** Both the whole-list path and the single-index path were checked. Neither makes a heap allocation per hash.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#263](https://github.com/status-im/nimbus-eth2/pull/263)

</details>


<a id="other-101"></a>
<details>
<summary><b>other-101</b> Compressed genesis state download — <i>not · low · S · bandwidth, startup</i></summary>

**Idea.** Serve and download the genesis state snappy-framed compressed, detecting compression by the stream header so uncompressed SSZ still works. This roughly halves bytes transferred on first start.

**Gap in Lighthouse.** Add Accept-Encoding/snappy-framed support in get_state_bytes and detect the snappy frame header before the checksum and from_ssz_bytes in download_genesis_state; needs server support too.

**Impact.** Roughly halves genesis download bytes, only on first start of a non-checkpoint-synced node on large networks; mainnet checkpoint sync is the norm.

**Best measured result.** reduces the size of the downloaded file with roughly 50% (commit:nimbus@6b1ab8104655)

**Evidence (Lighthouse @ 928b61e719).**

- [`common/eth2_network_config/src/lib.rs:395`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/eth2_network_config/src/lib.rs#L395) download_genesis_state fetches raw SSZ and checks sha256 of raw bytes
- [`common/eth2_network_config/src/lib.rs:257`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/eth2_network_config/src/lib.rs#L257) built-in bytes are raw genesis.ssz

**Sources.** [nimbus@6b1ab8104](https://github.com/status-im/nimbus-eth2/commit/6b1ab8104655)

</details>


<a id="other-102"></a>
<details>
<summary><b>other-102</b> Read genesis time from config constant — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Read genesis time from a static per-network config constant instead of the locked beacon state on hot paths such as attestation and block pre-state checks. Fall back to state when no constant exists.

**Impact.** Hot paths use the slot clock and the BeaconChain.genesis_time field, so no locked state is read for genesis time.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:498`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L498)
- [`beacon_node/beacon_chain/src/builder.rs:1048`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/builder.rs#L1048)
- [`beacon_node/beacon_chain/src/builder.rs:1258`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/builder.rs#L1258)
- [`consensus/state_processing/src/per_block_processing.rs:550`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing.rs#L550)

**Skeptic check.** Outside the builder, the only state.genesis_time() read is in compute_timestamp_at_slot during per-block processing. That is a plain field read on an owned state, not a lock, so the lock contention the Prysm change removed does not exist in Lighthouse.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#6966](https://github.com/OffchainLabs/prysm/pull/6966)

</details>


<a id="other-103"></a>
<details>
<summary><b>other-103</b> Cancellation-aware sleeps in background loops — <i>n/a · low · latency</i></summary>

**Idea.** Replace blocking sleeps in background loops and retries with sleeps that wake on cancellation, so tasks exit immediately on shutdown. Check for plain sleeps in Lighthouse service loops.

**Impact.** Spawned tasks are dropped on the exit signal, so sleeps in them are cancelled automatically; only shutdown latency would matter anyway.

**Evidence (Lighthouse @ 928b61e719).**

- [`common/task_executor/src/lib.rs:273-284`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/task_executor/src/lib.rs#L273-L284) async tasks wrapped in select against exit future
- [`beacon_node/client/src/notifier.rs:74`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/client/src/notifier.rs#L74) plain sleep inside spawned task

**Sources.** [prysm#15894](https://github.com/OffchainLabs/prysm/pull/15894)

</details>


<a id="other-104"></a>
<details>
<summary><b>other-104</b> Slasher block-header queue as hash set — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Hold the slasher's pending block-header queue in a hash set so duplicate headers (for example one per blob sidecar) are stored and processed once.

**Impact.** Duplicate headers (one per sidecar) are stored and processed once.

**Evidence (Lighthouse @ 928b61e719).**

- [`slasher/src/block_queue.rs:7`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/block_queue.rs#L7) blocks: Mutex&lt;HashSet&lt;SignedBeaconBlockHeader&gt;&gt;
- [`slasher/src/block_queue.rs:11-13`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/block_queue.rs#L11-L13) queue inserts into HashSet
- [`slasher/src/slasher.rs:89`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/slasher.rs#L89) accept_block_header queues
- [`slasher/src/slasher.rs:108`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/slasher.rs#L108) process dequeues the set

**Skeptic check.** Verified BlockQueue is a HashSet and it is the only queue the slasher uses for headers. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#4976](https://github.com/sigp/lighthouse/pull/4976)

</details>


<a id="other-105"></a>
<details>
<summary><b>other-105</b> Exit debounce loops when channel closes — <i>n/a · low · cpu</i></summary>

**Idea.** Make debounce or select loops stop when their input channel closes, since receiving from a closed channel returns immediately and spins the CPU.

**Impact.** Rust channels return None when closed and the loops are written with while-let/match on that, so no busy spin; Lighthouse has no debounce helper.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src): loops use tokio mpsc recv, which returns None on close and exits via while let Some

**Sources.** [prysm#17003](https://github.com/OffchainLabs/prysm/pull/17003)

</details>


<a id="other-106"></a>
<details>
<summary><b>other-106</b> Incremental span update with early stop — <i>implemented · low · S · cpu</i></summary>

**Idea.** Update slasher min/max spans on each new attestation and stop walking epochs once an existing span is already tighter, bounding work per attestation.

**Impact.** Per-attestation span work is bounded by early stop.

**Evidence (Lighthouse @ 928b61e719).**

- [`slasher/src/array.rs:261-268`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/array.rs#L261-L268) Chunk update returns Ok(false) when existing target is already tighter
- [`slasher/src/array.rs:471-476`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/array.rs#L471-L476) apply_attestation_for_validator breaks when !keep_going

**Skeptic check.** Verified the min/max span walk stops at the first epoch whose stored target is already tighter, for both min and max arrays through the shared generic path. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#3951](https://github.com/OffchainLabs/prysm/pull/3951)

</details>


<a id="other-107"></a>
<details>
<summary><b>other-107</b> Indices-only sync committee accessor — <i>partial · low · S · cpu, memory</i></summary>

**Idea.** Give callers that need only sync committee validator indices a direct indices accessor instead of building the full indexed sync committee cache object.

**Gap in Lighthouse.** Lighthouse has no heavy indexed sync committee cache object to avoid; indices come from a pubkey lookup each call. Could cache the Vec&lt;usize&gt; per sync period in the state or chain, in get_sync_committee_indices callers.

**Impact.** Would save ~512 hash lookups per call to this accessor; small and not on a hot path.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:1753`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L1753) get_sync_committee_indices maps pubkeys through pubkey_cache directly (indices only, no indexed committee object)

**Sources.** [lodestar#768](https://github.com/ChainSafe/lodestar/pull/768)

</details>


<a id="other-108"></a>
<details>
<summary><b>other-108</b> Minify slashing protection data on import — <i>not · low · S · disk, startup</i></summary>

**Idea.** When importing a slashing-protection interchange file, reduce it to max slot/source/target per validator before writing to the DB, keeping imports small and fast.

**Gap in Lighthouse.** Call interchange.minify() at the start of import_interchange_info (or in the CLI import path) so only the max block/source/target per validator is written.

**Impact.** Import of large files from other clients (e.g. genesis-era validators) would write far fewer rows; one-off operation, affects few nodes.

**Evidence (Lighthouse @ 928b61e719).**

- [`common/eip_3076/src/lib.rs:99`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/eip_3076/src/lib.rs#L99) minify exists but only used in tests ([`validator_client/slashing_protection/src/interchange_test.rs:82`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/slashing_protection/src/interchange_test.rs#L82))
- [`validator_client/slashing_protection/src/slashing_database.rs:807`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/slashing_protection/src/slashing_database.rs#L807) import_interchange_info inserts records without minifying

**Sources.** [nimbus#3393](https://github.com/status-im/nimbus-eth2/pull/3393)

</details>


<a id="other-109"></a>
<details>
<summary><b>other-109</b> Minimal assert helper in hot paths — <i>n/a · low · cpu</i></summary>

**Idea.** Use a minimal assert in hot paths that does no message formatting or stack capture unless the condition fails.

**Impact.** Rust assert! evaluates its message lazily, so there is no formatting or stack capture cost on the success path.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src): asserts are plain Rust assert!/debug_assert!, which format only on failure

**Sources.** [lodestar#1014](https://github.com/ChainSafe/lodestar/pull/1014)

</details>


<a id="other-110"></a>
<details>
<summary><b>other-110</b> Native integers instead of bignum for slots and balances — <i>n/a · low · cpu, memory</i></summary>

**Idea.** Use native fixed-width integers for balances, slots and epochs rather than an arbitrary-precision bignum type, avoiding heap allocation and slow big-number arithmetic.

**Impact.** Lighthouse already uses native u64 for slots, epochs and balances.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/core/slot_epoch.rs:1`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/core/slot_epoch.rs#L1) Slot and Epoch are newtypes over u64

**Sources.** [lodestar@148189aa0](https://github.com/ChainSafe/lodestar/commit/148189aa051e), [lodestar@e093598bc](https://github.com/ChainSafe/lodestar/commit/e093598bc3c1)

</details>


<a id="other-111"></a>
<details>
<summary><b>other-111</b> Flag to disable light client server — <i>implemented · low · S · cpu, disk, bandwidth</i></summary>

**Idea.** Provide a flag that disables the light client server: skip building updates on import, its gossip topics, req/resp protocols and REST endpoints.

**Impact.** Flag removes light client work on import, gossip, RPC and REST; default remains enabled.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/src/cli.rs:1576`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/cli.rs#L1576) --disable-light-client-server
- [`beacon_node/src/config.rs:202-203`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/config.rs#L202-L203) chain flag
- [`beacon_node/src/config.rs:1498`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/config.rs#L1498) network flag
- [`beacon_node/beacon_chain/src/beacon_chain.rs:4787`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4787) cache_state_data skipped on import
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5178`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5178) update producer skipped
- [`beacon_node/client/src/builder.rs:272`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/client/src/builder.rs#L272) producer channel not created
- [`beacon_node/lighthouse_network/src/types/topics.rs:77`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/topics.rs#L77) gossip topics gated
- [`beacon_node/lighthouse_network/src/rpc/protocol.rs:506`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/rpc/protocol.rs#L506) req/resp gated
- [`beacon_node/http_api/src/lib.rs:520`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L520) REST gated

**Skeptic check.** Verified each gate in source; the single CLI flag drives both chain and network config. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#6913](https://github.com/ChainSafe/lodestar/pull/6913)

</details>


<a id="other-112"></a>
<details>
<summary><b>other-112</b> Release resources per loop iteration — <i>n/a · low · memory</i></summary>

**Idea.** Close files, DB transactions, HTTP bodies and timers inside each loop iteration rather than deferring to function exit, keeping resource use constant.

**Impact.** Go defer-in-loop issue; Rust scopes drop handles at the end of each iteration.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/src/lib.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/lib.rs) (Rust RAII drops per-iteration resources)

**Sources.** [caplin#22994](https://github.com/erigontech/erigon/pull/22994)

</details>


<a id="other-113"></a>
<details>
<summary><b>other-113</b> Remove event listeners when done — <i>n/a · low · memory, cpu</i></summary>

**Idea.** Remove one-shot or task event listeners exactly when they fire or the task stops, so listeners do not accumulate on the emitter.

**Impact.** Node/JS event-emitter listener leak; Lighthouse uses channels and futures dropped on completion.

**Evidence (Lighthouse @ 928b61e719).**

- Rust has no emitter listener lists in this design; gossip uses channels

**Sources.** [lodestar@3acfba21f](https://github.com/ChainSafe/lodestar/commit/3acfba21fd2d), [lodestar#1134](https://github.com/ChainSafe/lodestar/pull/1134)

</details>


<a id="other-114"></a>
<details>
<summary><b>other-114</b> Single hash-map lookup on hot path — <i>not · low · S · cpu</i></summary>

**Idea.** Replace a double hash-map lookup (contains then get) with one lookup, saving a hash computation.

**Gap in Lighthouse.** The PR (closed unmerged) changed add_sync_subnet to use entry.insert on the Vacant/Occupied entry; Lighthouse still re-inserts by key there. Same fix applies to BeaconProposerCache::insert and ObservedExecutionPayloads::insert (use entry API).

**Impact.** Saves one hash per call on cold, low-rate paths (sync committee subscriptions, per-block cache inserts); not measurable.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/peer_manager/mod.rs:410`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/peer_manager/mod.rs#L410) add_sync_subnet does entry() then insert (second lookup)
- [`beacon_node/beacon_chain/src/beacon_proposer_cache.rs:158`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_proposer_cache.rs#L158) contains_key then insert
- [`beacon_node/beacon_chain/src/observed_execution_payloads.rs:30`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/observed_execution_payloads.rs#L30) contains_key then insert
- [`beacon_node/beacon_chain/src/pre_finalization_cache.rs:50`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/pre_finalization_cache.rs#L50) contains_key then separate lookup

**Sources.** [lighthouse#8830](https://github.com/sigp/lighthouse/pull/8830)

</details>


<a id="other-115"></a>
<details>
<summary><b>other-115</b> Single-pass filter into preallocated array — <i>n/a · low · cpu, memory</i></summary>

**Idea.** Build filtered arrays in one loop into a pre-declared output instead of map then filter, avoiding an extra pass and intermediate array.

**Impact.** JS map-then-filter allocation issue; Rust iterators are lazy and single pass.

**Evidence (Lighthouse @ 928b61e719).**

- Rust iterator adaptors (filter_map) fuse into one pass without intermediate Vec

**Sources.** [lodestar#2135](https://github.com/ChainSafe/lodestar/pull/2135)

</details>


<a id="other-116"></a>
<details>
<summary><b>other-116</b> Sleep in idle main-thread loop — <i>implemented · low · S · cpu</i></summary>

**Idea.** Make the main thread's idle run loop sleep between iterations instead of busy-spinning, so it does not burn a full CPU core.

**Impact.** Main thread parks on futures; no busy loop.

**Evidence (Lighthouse @ 928b61e719).**

- [`lighthouse/environment/src/lib.rs:351-395`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/lighthouse/environment/src/lib.rs#L351-L395) block_until_shutdown_requested block_on select of shutdown channel and signal streams
- [`lighthouse/src/main.rs:874`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/lighthouse/src/main.rs#L874) main thread blocks on it

**Skeptic check.** Verified the main thread awaits signal/shutdown futures via runtime.block_on; no empty loop exists in lighthouse/beacon_node/validator_client/common. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse@eb4723fee](https://github.com/sigp/lighthouse/commit/eb4723fee547)

</details>


<a id="other-117"></a>
<details>
<summary><b>other-117</b> Slasher attestation index keyed by target epoch only — <i>implemented · low · S · disk</i></summary>

**Idea.** Key the slasher's indexed-attestation index by target epoch only, dropping the source epoch, which shrinks every key by 8 bytes.

**Impact.** Keys carry no source epoch.

**Evidence (Lighthouse @ 928b61e719).**

- [`slasher/src/database.rs:44`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/database.rs#L44) INDEXED_ATTESTATION_ID_DB maps (target_epoch, indexed_attestation_hash)
- [`slasher/src/database.rs:175-183`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/database.rs#L175-L183) IndexedAttestationIdKey::new writes 8-byte target epoch plus 32-byte root, no source epoch
- [`slasher/src/database.rs:96`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/src/database.rs#L96) AttesterKey::new(validator_index, target_epoch)

**Skeptic check.** Verified both the indexed-attestation id key and attester key use target epoch only. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#4010](https://github.com/OffchainLabs/prysm/pull/4010)

</details>


<a id="other-118"></a>
<details>
<summary><b>other-118</b> Typed sort instead of reflection sort — <i>n/a · low · cpu, memory</i></summary>

**Idea.** Use typed generic sort functions instead of reflection-based sort and a string builder instead of concatenation in loops.

**Impact.** Go reflect-based sort.Slice and string concatenation; not applicable in Rust.

**Evidence (Lighthouse @ 928b61e719).**

- Rust sort_by/sort_unstable_by are typed and generic; no reflection

**Sources.** [caplin#22523](https://github.com/erigontech/erigon/pull/22523)

</details>


