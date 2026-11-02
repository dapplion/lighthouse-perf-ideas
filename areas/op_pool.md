# op_pool

39 ideas: 4 not, 10 partial, 22 implemented, 3 n/a; 7 actionable (high or medium value, verdict `not` or `partial`). [Back to the summary](../README.md).

Ids missing from the sequence are ideas that have not been checked against Lighthouse yet.

| id | idea | verdict | value | effort | resources |
|---|---|---|---|---|---|
| [op_pool-001](#op_pool-001) **★** | Bound pool size with hard cap and oldest-first eviction | partial | medium | S | memory |
| [op_pool-003](#op_pool-003) **★** | Skip attestations whose attesters are already on chain | partial | medium | M | cpu, bandwidth, memory |
| [op_pool-004](#op_pool-004) **★** | Remove block-included attestations from the pool on import | not | medium | M | memory, bandwidth, cpu |
| [op_pool-005](#op_pool-005) | Aggregate attestations into pool entries on arrival | implemented | low |  | cpu, memory, bandwidth, latency |
| [op_pool-006](#op_pool-006) | Aggregate lazily at block production or aggregator duty | partial | low | M | cpu, memory, latency |
| [op_pool-007](#op_pool-007) | Avoid duplicate aggregation passes per slot | partial | low | S | cpu, memory |
| [op_pool-008](#op_pool-008) **★** | Aggregate only committees a local aggregator will request | partial | medium | S | cpu, memory |
| [op_pool-009](#op_pool-009) | Index pool entries in hash maps by data root | implemented | low |  | cpu |
| [op_pool-010](#op_pool-010) | Prune pool by slot inclusion window each slot | implemented | low |  | memory, cpu |
| [op_pool-012](#op_pool-012) | Fast custom hash for attestation pool keys | implemented | low |  | cpu |
| [op_pool-014](#op_pool-014) | Fine-grained or concurrent locking in the op pool | implemented | medium |  | cpu, latency |
| [op_pool-015](#op_pool-015) | Greedy max-cover attestation selection by marginal reward | implemented | medium |  | cpu, bandwidth |
| [op_pool-016](#op_pool-016) | Greedy packing instead of unbounded ILP solver | implemented | low | S | cpu, latency |
| [op_pool-017](#op_pool-017) | In-place bitfield operations in max-cover | partial | low | M | cpu, memory |
| [op_pool-018](#op_pool-018) | Compare and merge aggregates with bitfields, not indices | partial | low | M | cpu |
| [op_pool-019](#op_pool-019) | Fast Electra committee-bits aggregation | implemented | medium | S | cpu, memory |
| [op_pool-020](#op_pool-020) | Electra cross-committee merge of aggregates at packing | implemented | medium |  | cpu, bandwidth |
| [op_pool-021](#op_pool-021) | Key packing candidates by data and committee index | implemented | medium |  | bandwidth |
| [op_pool-022](#op_pool-022) | Group by committee, cache validity, prune by score bound | partial | low | M | cpu, latency |
| [op_pool-025](#op_pool-025) | Check attestation targets without slot processing | implemented | medium |  | cpu, latency |
| [op_pool-026](#op_pool-026) | Validate exits without cloning or advancing state | implemented | low |  | cpu, memory |
| [op_pool-039](#op_pool-039) | Batch-verify signatures of packed operations | n/a | medium |  | cpu |
| [op_pool-041](#op_pool-041) | Cache deserialized signatures of pooled attestations | implemented | medium |  | cpu, latency |
| [op_pool-045](#op_pool-045) | Pool indexed by validator participation | implemented | medium |  | cpu, latency |
| [op_pool-046](#op_pool-046) | Keep best sync contribution per subnet, aggregate late | implemented | low |  | bandwidth |
| [op_pool-047](#op_pool-047) | Fill aggregate gaps from bounded single-attestation pool | implemented | medium |  | memory |
| [op_pool-051](#op_pool-051) | Max-cover selection of sync committee contributions | n/a | low |  | bandwidth, cpu |
| [op_pool-052](#op_pool-052) | Word-packed native bitsets for aggregation bits | not | low | M | cpu, memory |
| [op_pool-053](#op_pool-053) **★** | Parallel aggregation across attestation data groups | partial | medium | S | cpu, latency |
| [op_pool-056](#op_pool-056) **★** | Drop or replace subset aggregates on pool insertion | partial | medium | S | memory, cpu, bandwidth |
| [op_pool-058](#op_pool-058) | Store attesting indices and reward cache for packing | implemented | low |  | cpu, latency |
| [op_pool-060](#op_pool-060) | Skip signature group checks when aggregating into pool | implemented | low |  | cpu |
| [op_pool-064](#op_pool-064) | Prune operation pool on finalization | implemented | low |  | memory, cpu, disk, latency |
| [op_pool-072](#op_pool-072) | Reject slashings covering only already-slashed validators | implemented | low |  | memory, cpu |
| [op_pool-077](#op_pool-077) | Retain attestations of reorged-out blocks for reuse | implemented | medium |  | cpu |
| [op_pool-081](#op_pool-081) | Fast path for single-bit attestations in bit ops | not | low | S | cpu |
| [op_pool-082](#op_pool-082) | One aggregate call over all collected signatures | implemented | medium | S | cpu |
| [op_pool-087](#op_pool-087) | Slimmer single-attestation storage in pool | n/a | low |  | memory |
| [op_pool-088](#op_pool-088) **★** | Time-boxed lock-free block attestation packing | not | medium | M | cpu, latency |

★ actionable. Click an id for the full record.

## Ideas

<a id="op_pool-001"></a>
<details>
<summary><b>op_pool-001</b> Bound pool size with hard cap and oldest-first eviction — <i>partial · medium · S · memory</i></summary>

**Idea.** Put a hard cap on the number of attestations or gossip signatures held in the pool and evict the oldest slot or data root first (FIFO) when it is exceeded, with an O(1) size counter. This keeps memory bounded when finalization stalls or gossip floods.

**Gap in Lighthouse.** The gossip-signature analogue (naive aggregation pool) has a hard per-slot cap but rejects new items rather than evicting oldest. The op pool has no entry cap, only a 2-epoch target window that does not depend on finalization, so it cannot grow without bound under a finality stall. Add a cap with oldest-slot eviction and an O(1) counter to AttestationMap.

**Impact.** Low on Lighthouse: the time-based prune (not finality-based) plus observed_aggregators/observed_attesters dedup already bound pool size; a cap only guards pathological floods.

**Best measured result.** Devnet memory climbed to ~11.5 GB and crashed every ~27 min before; caps 4096/512 entries (pr:ethlambda#182)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/naive_aggregation_pool.rs:143`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/naive_aggregation_pool.rs#L143) SLOTS_RETAINED=3
- [`beacon_node/beacon_chain/src/naive_aggregation_pool.rs:287`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/naive_aggregation_pool.rs#L287) hard cap MAX_ATTESTATIONS_PER_SLOT rejects new entries (no eviction)
- [`beacon_node/operation_pool/src/attestation_storage.rs:632`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs#L632) op pool prune by target epoch only
- [`beacon_node/operation_pool/src/attestation_storage.rs:457`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs#L457) insert has no size check
- [`beacon_node/operation_pool/src/attestation_storage.rs:638`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs#L638) stats() walks every map (no O(1) counter)

**Second check.** Checked observed_aggregates/observed_attesters capacities and the naive pool cap; the ethlambda crash case (pool tied to finalization) does not apply because LH prunes by epoch, but no hard op-pool cap or FIFO eviction exists.

**Sources.** [ethlambda#290](https://github.com/lambdaclass/ethlambda/pull/290), [teku#5305](https://github.com/Consensys-Incorporated/teku/pull/5305), [ethlambda#182](https://github.com/lambdaclass/ethlambda/pull/182)

</details>


<a id="op_pool-003"></a>
<details>
<summary><b>op_pool-003</b> Skip attestations whose attesters are already on chain — <i>partial · medium · M · cpu, bandwidth, memory</i></summary>

**Idea.** Track, per attestation data, the union of validators already included on chain (bitlists or index sets updated incrementally from imported blocks, with epoch-scale expiry) plus those already covered in the block being built, and reject, prune or skip pool attestations whose bits are all covered. The pool stays smaller and block packing does less work and carries no redundant attestations.

**Gap in Lighthouse.** Packing skips on-chain-covered attesters and gossip rejects subset aggregates vs seen aggregates, but nothing rejects or prunes pool entries whose bits are all already included on chain. observed_block_attesters already tracks per-epoch on-chain attesters and could be used to filter at add_to_block_inclusion_pool and to prune after block import.

**Impact.** Smaller op pool and fewer AttMaxCover constructions during block production; modest packing-time win.

**Best measured result.** None (pr:prysm#6993)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/attestation.rs:96`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation.rs#L96) has_attested_in_epoch drops on-chain-covered validators at packing
- [`beacon_node/operation_pool/src/max_cover.rs:62`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/max_cover.rs#L62) zero-score items excluded
- [`beacon_node/beacon_chain/src/attestation_verification.rs:574`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L574) is_known_subset rejects gossip aggregates that are subsets of already-seen aggregates
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5067`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5067) observed_block_attesters filled from block attestations
- [`beacon_node/beacon_chain/src/beacon_chain.rs:8355`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L8355) observed_block_attesters used only for liveness, not pool filtering
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2699`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2699) add_to_block_inclusion_pool inserts without on-chain check

**Second check.** Beyond the earlier review, found observed_block_attesters (on-chain attester set) and the gossip subset check; neither is used to drop pool entries covered on chain.

**Sources.** [prysm#7015](https://github.com/OffchainLabs/prysm/pull/7015), [prysm#7203](https://github.com/OffchainLabs/prysm/pull/7203), [nimbus#2061](https://github.com/status-im/nimbus-eth2/pull/2061), [teku#916](https://github.com/Consensys-Incorporated/teku/pull/916), [teku#701](https://github.com/Consensys-Incorporated/teku/pull/701), [teku#2969](https://github.com/Consensys-Incorporated/teku/pull/2969), [prysm#6993](https://github.com/OffchainLabs/prysm/pull/6993), [teku#4312](https://github.com/Consensys-Incorporated/teku/pull/4312)

</details>


<a id="op_pool-004"></a>
<details>
<summary><b>op_pool-004</b> Remove block-included attestations from the pool on import — <i>not · medium · M · memory, bandwidth, cpu</i></summary>

**Idea.** When a block is imported (or becomes canonical on head change), delete its attestations from the op pool right away instead of waiting for expiry, decomposing post-Electra multi-committee attestations into per-committee aggregates so they match pool entries. The pool stays small and block production does not rescan or re-pack them.

**Gap in Lighthouse.** Block-included attestations remain until epoch prune. Add op_pool removal on block import/head change (decomposing Electra multi-committee attestations per committee), or reuse observed_block_attesters to drop fully covered entries.

**Impact.** Smaller pool, cheaper get_attestations and less memory; packing cost scales with pool size.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/lib.rs:295`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L295) insert_attestation; no remove-by-block method in the op pool API
- [`beacon_node/operation_pool/src/lib.rs:455`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L455) prune_attestations by epoch only
- [`beacon_node/beacon_chain/src/canonical_head.rs:1566`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1566) only op-pool attestation prune call site
- [`beacon_node/operation_pool/src/attestation.rs:96`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation.rs#L96) reward-cache filter only skips them at packing

**Second check.** Listed every op pool pub fn and every op_pool.prune/remove call in beacon_chain; the only attestation removal is the epoch prune.

**Sources.** [teku#2000](https://github.com/Consensys-Incorporated/teku/pull/2000), [prysm#14896](https://github.com/OffchainLabs/prysm/pull/14896), [lodestar@4d2caec94](https://github.com/ChainSafe/lodestar/commit/4d2caec94991), [prysm#10623](https://github.com/OffchainLabs/prysm/pull/10623), [prysm#9444](https://github.com/OffchainLabs/prysm/pull/9444), [prysm#4241](https://github.com/OffchainLabs/prysm/pull/4241), [prysm#4798](https://github.com/OffchainLabs/prysm/pull/4798), [prysm#1942](https://github.com/OffchainLabs/prysm/pull/1942), [prysm#11771](https://github.com/OffchainLabs/prysm/pull/11771)

</details>


<a id="op_pool-005"></a>
<details>
<summary><b>op_pool-005</b> Aggregate attestations into pool entries on arrival — <i>implemented · low · cpu, memory, bandwidth, latency</i></summary>

**Idea.** When an unaggregated gossip attestation arrives, OR its bits and add its signature into an existing pool aggregate with the same data (keyed by attestation data), so the pool holds few large aggregates. Fewer objects are stored, hashed and compared, and an aggregator request becomes a lookup of a precomputed aggregate.

**Best measured result.** None (pr:prysm#4376)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/attestation_storage.rs:535-560`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs#L535-L560) AttestationMap::insert merges into an existing entry with same data when bits are disjoint
- [`beacon_node/beacon_chain/src/naive_aggregation_pool.rs:276-282`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/naive_aggregation_pool.rs#L276-L282) gossip single votes aggregated into one entry per data root
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2596`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2596) add_to_naive_aggregation_pool serves aggregator requests by lookup (get at :1877)

**Sources.** [prysm#3761](https://github.com/OffchainLabs/prysm/pull/3761), [prysm#3149](https://github.com/OffchainLabs/prysm/pull/3149), [prysm#4794](https://github.com/OffchainLabs/prysm/pull/4794), [prysm#4478](https://github.com/OffchainLabs/prysm/pull/4478), [lodestar#2851](https://github.com/ChainSafe/lodestar/pull/2851), [lodestar#2679](https://github.com/ChainSafe/lodestar/pull/2679), [prysm#14324](https://github.com/OffchainLabs/prysm/pull/14324), [prysm#16158](https://github.com/OffchainLabs/prysm/pull/16158), [lighthouse#950](https://github.com/sigp/lighthouse/pull/950), [prysm#4376](https://github.com/OffchainLabs/prysm/pull/4376)

</details>


<a id="op_pool-006"></a>
<details>
<summary><b>op_pool-006</b> Aggregate lazily at block production or aggregator duty — <i>partial · low · M · cpu, memory, latency</i></summary>

**Idea.** Store single-vote attestations separately, with no periodic background aggregation routine, and aggregate them only when an aggregate is requested or a block is produced, using hash tables keyed by attestation data and a temporary cache. No aggregation or signature deserialization is paid for aggregates that are never used.

**Gap in Lighthouse.** Only cross-committee aggregation and the naive-to-op-pool copy are lazy. Per-attestation aggregation into the op pool happens eagerly on each gossip arrival (BeaconChain::add_to_block_inclusion_pool); making it lazy would mean storing singles and aggregating in get_attestations.

**Impact.** Small CPU saving at best (skips aggregation for votes never packed); Lighthouse already uses hash maps keyed by data and has no background aggregation routine.

**Best measured result.** Speeds up iterating all attestations for a slot; improves aggregate quality and block packing (commit:nimbus@4ed2e34a9eb7)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:2596`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2596),2699 single votes are aggregated eagerly on arrival, in both the naive pool and the op pool
- [`beacon_node/operation_pool/src/lib.rs:380`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L380) Electra cross-committee aggregation is lazy, done only in get_attestations
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5944`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5944) naive pool is copied into the op pool lazily at block production

**Sources.** [lodestar#4712](https://github.com/ChainSafe/lodestar/pull/4712), [nimbus#125](https://github.com/status-im/nimbus-eth2/pull/125), [teku#1532](https://github.com/Consensys-Incorporated/teku/pull/1532), [nimbus@4ed2e34a9](https://github.com/status-im/nimbus-eth2/commit/4ed2e34a9eb7), [nimbus#2495](https://github.com/status-im/nimbus-eth2/pull/2495), [prysm#5302](https://github.com/OffchainLabs/prysm/pull/5302)

</details>


<a id="op_pool-007"></a>
<details>
<summary><b>op_pool-007</b> Avoid duplicate aggregation passes per slot — <i>partial · low · S · cpu, memory</i></summary>

**Idea.** Do not aggregate the same unaggregated attestations twice in a slot (for example for fork choice and again for an aggregator request), do not re-aggregate an aggregate with itself, and do not reset aggregate expiry on update. Reuse the earlier result to cut CPU and keep the pool small.

**Gap in Lighthouse.** No self-re-aggregation and no expiry reset, but the naive pool is re-imported in full at each block production (import loop in produce_partial_beacon_block), repeating work done in prior slots. Track a high-water mark or drain imported entries to avoid it.

**Impact.** Saves a few hundred to a few thousand insert calls (index lookups plus clones) per produced block; only matters on proposer duty.

**Best measured result.** pool count below 500 versus 2000 before (pr:prysm#4932)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/attestation_storage.rs:540-549`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs#L540-L549) insert only aggregates when bits are disjoint; equal entry is detected, so an aggregate is not merged with itself
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5944-5960`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5944-L5960) every block production re-inserts the whole naive pool into the op pool, recomputing attesting indices and cloning each attestation
- [`beacon_node/beacon_chain/src/naive_aggregation_pool.rs:268`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/naive_aggregation_pool.rs#L268) naive pool skips already-set bits

**Sources.** [prysm#5354](https://github.com/OffchainLabs/prysm/pull/5354), [prysm#4932](https://github.com/OffchainLabs/prysm/pull/4932)

</details>


<a id="op_pool-008"></a>
<details>
<summary><b>op_pool-008</b> Aggregate only committees a local aggregator will request — <i>partial · medium · S · cpu, memory</i></summary>

**Idea.** Pre-aggregate gossip attestations and sync messages only for (slot, committee/subnet) pairs with a subscribed local aggregator or an imminent local proposer, and skip messages from old slots or arriving after 2/3 of the slot. Aggregation work for other committees is skipped.

**Gap in Lighthouse.** Unaggregated attestations are already only pre-aggregated for exact (subnet, slot) pairs with a subscribed local aggregator, as in Lodestar #5284 and Grandine. Missing: no gating of sync committee messages, no skip of attestations arriving after 2/3 of the slot, and no imminent-proposer exception (not needed since LH packs from aggregates).

**Impact.** Remaining gain is small: sync committee messages are few, and late-arrival skipping saves little.

**Best measured result.** None (pr:lodestar#5256)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/subnet_service/mod.rs:353`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/subnet_service/mod.rs#L353) should_process_attestation: true only if a local aggregator is tracked for the exact (subnet, slot)
- [`beacon_node/network/src/subnet_service/mod.rs:270`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/subnet_service/mod.rs#L270) aggregator subscriptions recorded per ExactSubnet
- [`beacon_node/network/src/subnet_service/mod.rs:152`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/subnet_service/mod.rs#L152) tracking disabled only with import_all_attestations
- [`beacon_node/network/src/service.rs:572`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/service.rs#L572) should_process computed per gossip attestation
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:422`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L422) if !should_import return before fork choice and naive pool
- [`beacon_node/src/cli.rs:122`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/cli.rs#L122) --import-all-attestations opt-out flag
- [`beacon_node/beacon_chain/src/naive_aggregation_pool.rs:143`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/naive_aggregation_pool.rs#L143) old slots refused (SlotTooLow)

**Second check.** The earlier review missed the network-layer gate: NetworkService asks SubnetService::should_process_attestation and the processor returns before add_to_naive_aggregation_pool unless a local aggregator has that exact subnet/slot.

**Sources.** [prysm#7206](https://github.com/OffchainLabs/prysm/pull/7206), [grandine@fca5f062a](https://github.com/grandinetech/grandine/commit/fca5f062a1a6), [lodestar#5284](https://github.com/ChainSafe/lodestar/pull/5284), [lodestar#5256](https://github.com/ChainSafe/lodestar/pull/5256)

</details>


<a id="op_pool-009"></a>
<details>
<summary><b>op_pool-009</b> Index pool entries in hash maps by data root — <i>implemented · low · cpu</i></summary>

**Idea.** Index attestations (and other pool items) by attestation data root or id in a hash map, so existence checks and lookups are O(1) and do not rehash data or scan the list.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/attestation_storage.rs:60-67`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs#L60-L67) HashMap&lt;CheckpointKey, HashMap&lt;CompactAttestationData, Vec&lt;..&gt;&gt;&gt;
- [`beacon_node/beacon_chain/src/naive_aggregation_pool.rs:239`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/naive_aggregation_pool.rs#L239) HashMap keyed by attestation key tree-hash root
- [`beacon_node/operation_pool/src/lib.rs:858`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L858) slashings and exits in HashMap by validator index

**Sources.** [prysm#4837](https://github.com/OffchainLabs/prysm/pull/4837), [teku#749](https://github.com/Consensys-Incorporated/teku/pull/749), [lodestar#2295](https://github.com/ChainSafe/lodestar/pull/2295)

</details>


<a id="op_pool-010"></a>
<details>
<summary><b>op_pool-010</b> Prune pool by slot inclusion window each slot — <i>implemented · low · memory, cpu</i></summary>

**Idea.** Store pool entries in per-slot maps and, every slot, drop whole slots that fall outside the inclusion window by the current wall-clock slot (for every attestation variant), instead of per-entry TTL caches or finality-based pruning. The pool stays bounded even during non-finality.

**Best measured result.** None (pr:teku#5197)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/naive_aggregation_pool.rs:557`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/naive_aggregation_pool.rs#L557) prunes per slot, keeps SLOTS_RETAINED=3 slots (per-slot maps)
- [`beacon_node/operation_pool/src/attestation_storage.rs:632`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs#L632) op pool prune retains only target epochs within the last 1 epoch
- [`beacon_node/beacon_chain/src/canonical_head.rs:1566`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1566) prune_attestations(wall-clock epoch) on epoch transition or reorg, independent of finality

**Sources.** [prysm#5087](https://github.com/OffchainLabs/prysm/pull/5087), [nimbus@535819263](https://github.com/status-im/nimbus-eth2/commit/535819263d61), [lighthouse#1805](https://github.com/sigp/lighthouse/pull/1805), [teku#1741](https://github.com/Consensys-Incorporated/teku/pull/1741), [prysm#2439](https://github.com/OffchainLabs/prysm/pull/2439), [prysm#2442](https://github.com/OffchainLabs/prysm/pull/2442), [teku#5197](https://github.com/Consensys-Incorporated/teku/pull/5197), [teku#966](https://github.com/Consensys-Incorporated/teku/pull/966)

</details>


<a id="op_pool-012"></a>
<details>
<summary><b>op_pool-012</b> Fast custom hash for attestation pool keys — <i>implemented · low · cpu</i></summary>

**Idea.** Key pool attestations with a fast non-SSZ hash of their fields instead of the generic SSZ hash_tree_root. Key computation becomes over 10x cheaper.

**Impact.** No tree-hash on the key path; nothing to gain.

**Best measured result.** 24274 ns/op -&gt; 1582 ns/op (pr:prysm#5217)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/attestation_storage.rs:49`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs#L49) pool keyed by CompactAttestationData (plain struct with derived Hash in HashMap), no SSZ hash_tree_root

**Sources.** [prysm#5217](https://github.com/OffchainLabs/prysm/pull/5217)

</details>


<a id="op_pool-014"></a>
<details>
<summary><b>op_pool-014</b> Fine-grained or concurrent locking in the op pool — <i>implemented · medium · cpu, latency</i></summary>

**Idea.** Put the locks inside the operation pool, per pool field or per attestation-data key, or use concurrent maps and lock-free groups, instead of one big lock around the whole pool on the chain. Gossip inserts and block production reads then do not contend on a single lock.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:416`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L416) op_pool: OperationPool is a plain field, no chain-level lock
- [`beacon_node/operation_pool/src/lib.rs:52-70`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L52-L70) separate RwLock per pool field

**Sources.** [lighthouse@cd9494181](https://github.com/sigp/lighthouse/commit/cd9494181c80), [teku#9297](https://github.com/Consensys-Incorporated/teku/pull/9297), [teku#9225](https://github.com/Consensys-Incorporated/teku/pull/9225), [teku#9438](https://github.com/Consensys-Incorporated/teku/pull/9438), [lighthouse#339](https://github.com/sigp/lighthouse/pull/339), [prysm#3470](https://github.com/OffchainLabs/prysm/pull/3470)

</details>


<a id="op_pool-015"></a>
<details>
<summary><b>op_pool-015</b> Greedy max-cover attestation selection by marginal reward — <i>implemented · medium · cpu, bandwidth</i></summary>

**Idea.** When producing a block, select attestations from the op pool with a greedy maximum-coverage algorithm whose score is the marginal proposer reward (validators newly covered given those already chosen), instead of naive ordering. Blocks carry more rewarded attesters within the attestation limit.

**Best measured result.** Prysm packed 8 attestations where others pack 1-2 (pr:prysm#17416)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/max_cover.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/max_cover.rs) maximum_cover greedy
- [`beacon_node/operation_pool/src/attestation.rs:176`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation.rs#L176) score = marginal proposer reward
- [`beacon_node/operation_pool/src/lib.rs:407`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L407) rayon::join prev/curr epoch packing

**Sources.** [prysm#17416](https://github.com/OffchainLabs/prysm/pull/17416), [prysm#6305](https://github.com/OffchainLabs/prysm/pull/6305), [prysm#10109](https://github.com/OffchainLabs/prysm/pull/10109), [caplin#11984](https://github.com/erigontech/erigon/pull/11984), [lighthouse@38d2d03e3](https://github.com/sigp/lighthouse/commit/38d2d03e3a98), [lighthouse#416](https://github.com/sigp/lighthouse/pull/416), [prysm#6344](https://github.com/OffchainLabs/prysm/pull/6344), [prysm#9684](https://github.com/OffchainLabs/prysm/pull/9684)

</details>


<a id="op_pool-016"></a>
<details>
<summary><b>op_pool-016</b> Greedy packing instead of unbounded ILP solver — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Pack attestations with a greedy best-per-committee pass, and either drop the integer-programming/knapsack solver or cap its input (aggregates per data) so it fits a time budget. Packing CPU stays bounded with almost no loss of coverage.

**Gap in Lighthouse.** Input is not capped, so cost is O(limit*items*set size); a cap on aggregates per data would bound it.

**Impact.** Packing is already greedy; a cap would only trim the worst case on a busy pool (block production, ms-level).

**Best measured result.** a plain best-per-committee greedy already covers 99.89% of observed attesters (pr:grandine#823)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/max_cover.rs:53`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/max_cover.rs#L53) maximum_cover is a plain greedy selection, no ILP/knapsack solver
- [`beacon_node/operation_pool/src/lib.rs:392`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L392) two greedy runs (prev/curr epoch) in rayon::join

**Sources.** [grandine#823](https://github.com/grandinetech/grandine/pull/823), [grandine@e12ae9738](https://github.com/grandinetech/grandine/commit/e12ae9738876)

</details>


<a id="op_pool-017"></a>
<details>
<summary><b>op_pool-017</b> In-place bitfield operations in max-cover — <i>partial · low · M · cpu, memory</i></summary>

**Idea.** In the max-cover aggregation loop, mutate bitfields and candidate slices in place instead of allocating new bitlists and slices each step, and drop per-call length checks. This cuts allocations during aggregation and packing.

**Gap in Lighthouse.** Cache the score in AttMaxCover (update on retain) and avoid cloning the selected item; covering sets are HashMap&lt;u64,u64&gt; rather than bitfields so every set is an allocated map built in AttMaxCover::new_for_altair_or_later.

**Impact.** Fewer allocations and hash-map work in block production packing; small absolute gain (tens of ms at most).

**Best measured result.** Benchmarks show fewer allocations; ops/sec only relatively useful (pr:prysm#7938)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/attestation.rs:165`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation.rs#L165) update_covering_set uses HashMap::retain in place
- [`beacon_node/operation_pool/src/max_cover.rs:73`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/max_cover.rs#L73) best.clone() per step, and score() at max_cover.rs:63-80 re-sums the HashMap several times per item per round

**Sources.** [prysm#7938](https://github.com/OffchainLabs/prysm/pull/7938), [prysm#8311](https://github.com/OffchainLabs/prysm/pull/8311)

</details>


<a id="op_pool-018"></a>
<details>
<summary><b>op_pool-018</b> Compare and merge aggregates with bitfields, not indices — <i>partial · low · M · cpu</i></summary>

**Idea.** Merge, compare and score aggregate participation (OR, subset, superset, intersection, unseen count) directly on committee-ordered aggregation bitfields, instead of expanding them to validator index arrays or Sets through committee lookups. Aggregates of one committee share bit positions so this is much cheaper.

**Gap in Lighthouse.** Insertion uses bitfields, but each aggregate also carries and merges an attesting_indices Vec, and max-cover scores via index HashMaps. Store only bits plus the committee and compute rewards via bit position lookups in AttMaxCover and update_covering_set.

**Impact.** Cheaper insert and packing and less memory per pooled aggregate; modest on mainnet.

**Best measured result.** Says perf tests show BitArray much faster; no numbers (pr:lodestar#4034)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/attestation_storage.rs:235`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs#L235) should_aggregate / :241 aggregate use bitfield intersection/union for disjoint check and merge
- [`beacon_node/operation_pool/src/attestation_storage.rs:241-250`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs#L241-L250) aggregate also merges Vec&lt;u64&gt; attesting_indices (sorted merge+dedup)
- [`beacon_node/operation_pool/src/attestation.rs:23`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation.rs#L23),165 max-cover covering set and subset updates use validator-index HashMap

**Sources.** [lodestar#4034](https://github.com/ChainSafe/lodestar/pull/4034), [lodestar#4038](https://github.com/ChainSafe/lodestar/pull/4038), [lodestar#3725](https://github.com/ChainSafe/lodestar/pull/3725)

</details>


<a id="op_pool-019"></a>
<details>
<summary><b>op_pool-019</b> Fast Electra committee-bits aggregation — <i>implemented · medium · S · cpu, memory</i></summary>

**Idea.** In post-Electra aggregation, skip committee-bit remapping when committee bits are equal, avoid recomputing committee start offsets and SSZ-hashing committee bits in superset checks, and OR aggregation bits directly on a bitset. Aggregation of many attestations gets faster with less memory.

**Gap in Lighthouse.** Residual micro-opt only: bitlist_extend (attestation_storage.rs:416, TODO) copies bits one at a time when merging disjoint committees, once per block production.

**Impact.** Teku's gains came from SSZ-tree bitlists and committee-offset remapping that Lighthouse's flat byte bitfields never had; byte-copying bitlist_extend would save well under a millisecond per block.

**Best measured result.** or rewrite ~4x faster, far less memory (pr:teku#8346)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/attestation_storage.rs:254`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs#L254) should_aggregate compares committee_bits by value, no hashing
- [`beacon_node/operation_pool/src/attestation_storage.rs:264`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs#L264) aggregate_same_committee unions bits with no committee remapping
- 974f78f/ssz/src/bitfield.rs:247 BitList union is a byte-wise OR on a plain Vec&lt;u8&gt;
- 974f78f/ssz/src/bitfield.rs:525 is_subset byte-wise, no tree hashing
- [`beacon_node/operation_pool/src/attestation_storage.rs:279`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs#L279) cross-committee merge appends in increasing committee order, no offset recompute

**Second check.** Read the ethereum_ssz git dependency: union/intersection/is_subset are byte-wise on flat bytes, so the Teku costs (SSZ hashing, slow or, offset remapping) do not exist in Lighthouse; only the per-bit extend remains.

**Sources.** [teku#9293](https://github.com/Consensys-Incorporated/teku/pull/9293), [teku#8346](https://github.com/Consensys-Incorporated/teku/pull/8346)

</details>


<a id="op_pool-020"></a>
<details>
<summary><b>op_pool-020</b> Electra cross-committee merge of aggregates at packing — <i>implemented · medium · cpu, bandwidth</i></summary>

**Idea.** Post-Electra, group pooled aggregates by AttestationData and merge those with disjoint committee bits into one on-chain multi-committee attestation when packing, keeping all aggregates for that data rather than only the best one. Fewer, larger attestations fit more votes into the block.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/attestation_storage.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs) aggregate_across_committees
- [`beacon_node/operation_pool/src/attestation_storage.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs) compute_on_chain_aggregate / aggregate_with_disjoint_committees
- [`beacon_node/operation_pool/src/lib.rs:397`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L397) called for prev and curr epoch keys when electra_enabled

**Sources.** [lodestar#6732](https://github.com/ChainSafe/lodestar/pull/6732), [lighthouse#5749](https://github.com/sigp/lighthouse/pull/5749), [prysm#14534](https://github.com/OffchainLabs/prysm/pull/14534), [nimbus#6498](https://github.com/status-im/nimbus-eth2/pull/6498)

</details>


<a id="op_pool-021"></a>
<details>
<summary><b>op_pool-021</b> Key packing candidates by data and committee index — <i>implemented · medium · bandwidth</i></summary>

**Idea.** Post-Electra, key attestation packing candidates by (AttestationData, committee index), not data alone, because all committees of a slot share the same data. Deduplicating by data alone drops most votes from the block.

**Impact.** Packing candidates are per committee/aggregate, not one per data, so no votes lost.

**Best measured result.** ~95% of a slot's votes left out of the next block (commit:grandine@3d511c2f35f6)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/attestation_storage.rs:66`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs#L66) map data -&gt; Vec&lt;CompactIndexedAttestation&gt;, one entry per committee_bits/aggregation set
- [`beacon_node/operation_pool/src/attestation_storage.rs:489`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs#L489) aggregate_across_committees keeps best per committee_index

**Sources.** [grandine@3d511c2f3](https://github.com/grandinetech/grandine/commit/3d511c2f35f6)

</details>


<a id="op_pool-022"></a>
<details>
<summary><b>op_pool-022</b> Group by committee, cache validity, prune by score bound — <i>partial · low · M · cpu, latency</i></summary>

**Idea.** When selecting block attestations, group by (slot, committee index) so the committee is fetched once, track not-yet-seen attesters, cache validity per (head root, target epoch), and skip data whose maximum possible score is below the lowest included score. Worst-case selection drops from about 1s to about 100ms.

**Gap in Lighthouse.** Validity is cached per attestation data, but there is no grouping by committee for lookups and no skipping of items whose max possible score is below the lowest selected score. Add a score upper bound (initial score) and break/skip in maximum_cover.

**Impact.** Cuts worst-case packing time when the pool holds many aggregates per data; likely 2-10x on pathological pools, little at normal load.

**Best measured result.** ~1s down to ~100ms in worst case in benchmark (pr:lodestar#6367)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:5973-5980`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5973-L5980) filter_op_pool_attestation with prev/curr filter caches (validity cached per data)
- [`beacon_node/operation_pool/src/lib.rs:317-340`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L317-L340) get_valid_attestations_for_epoch filters by slot window only
- [`beacon_node/operation_pool/src/max_cover.rs:53-100`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/max_cover.rs#L53-L100) every round scans all items, no upper-bound pruning

**Sources.** [lodestar#6367](https://github.com/ChainSafe/lodestar/pull/6367)

</details>


<a id="op_pool-025"></a>
<details>
<summary><b>op_pool-025</b> Check attestation targets without slot processing — <i>implemented · medium · cpu, latency</i></summary>

**Idea.** When validating or converting pooled attestations for packing or aggregation, get the target dependent root from block-root history or the nearest cached state and reuse cached target checkpoint states, instead of running slot processing to build a checkpoint state. This removes state-cache lock contention and CPU in block production.

**Impact.** Already cheap; no checkpoint-state build in block production.

**Best measured result.** greatly reduces state cache locking (pr:grandine#891)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:2739`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2739) filter_op_pool_attestation cached by (block_root,target_epoch)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2783`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2783) shuffling_is_compatible_result uses fork-choice shuffling ids, no slot processing

**Sources.** [grandine#891](https://github.com/grandinetech/grandine/pull/891), [grandine@9dc532a70](https://github.com/grandinetech/grandine/commit/9dc532a7031c), [grandine@35c820ecd](https://github.com/grandinetech/grandine/commit/35c820ecda72), [grandine#510](https://github.com/grandinetech/grandine/pull/510)

</details>


<a id="op_pool-026"></a>
<details>
<summary><b>op_pool-026</b> Validate exits without cloning or advancing state — <i>implemented · low · cpu, memory</i></summary>

**Idea.** Validate gossip and pool voluntary exits against the head state directly, without cloning it, skipping slots, or building a shuffling/epoch cache, since exit validity does not depend on slot processing.

**Best measured result.** None (pr:lighthouse#4183)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:2841-2872`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2841-L2872) verify_voluntary_exit_for_gossip uses head_snapshot state by reference and wall-clock epoch, no clone or slot advance
- [`beacon_node/operation_pool/src/lib.rs:629`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L629) verify_exit against given state with VerifySignatures::False

**Sources.** [lighthouse#4181](https://github.com/sigp/lighthouse/pull/4181), [nimbus#2188](https://github.com/status-im/nimbus-eth2/pull/2188), [lighthouse#4183](https://github.com/sigp/lighthouse/pull/4183)

</details>


<a id="op_pool-039"></a>
<details>
<summary><b>op_pool-039</b> Batch-verify signatures of packed operations — <i>n/a · medium · cpu</i></summary>

**Idea.** When packing operations from the pool into a block, check validity without signatures first, then verify all signatures as one batch, falling back to individual checks only if the batch fails.

**Impact.** Pool entries are signature-verified before insertion, so packing does no signature checks; nothing to batch (paranoid mode checks individually, opt-in).

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:5978`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5978) pack_attestations calls op_pool.get_attestations with no signature work
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5995`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5995) signatures re-checked only under paranoid_block_proposal

**Sources.** [prysm#11718](https://github.com/OffchainLabs/prysm/pull/11718)

</details>


<a id="op_pool-041"></a>
<details>
<summary><b>op_pool-041</b> Cache deserialized signatures of pooled attestations — <i>implemented · medium · cpu, latency</i></summary>

**Idea.** Store pooled attestation signatures already decompressed and subgroup-checked, so block production does not re-deserialize them each time. At 220k validators this made block production about 5x faster.

**Impact.** Block production never decompresses pooled signatures; only the final block serialization compresses.

**Best measured result.** Block production ~5x faster, sim 41m -&gt; 18m at 220k validators (pr:nimbus#2419)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/attestation_storage.rs:40`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs#L40) signature: AggregateSignature kept in decompressed blst form
- [`beacon_node/operation_pool/src/attestation_storage.rs:249`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs#L249) aggregation is point addition, no re-deserialization

**Sources.** [nimbus#2419](https://github.com/status-im/nimbus-eth2/pull/2419)

</details>


<a id="op_pool-045"></a>
<details>
<summary><b>op_pool-045</b> Pool indexed by validator participation — <i>implemented · medium · cpu, latency</i></summary>

**Idea.** Use an attestation pool indexed by validator participation as the default implementation, for faster aggregation and block packing.

**Impact.** Lighthouse pool is already bitfield-based per data; no separate legacy pool variant to swap.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/attestation_storage.rs:32`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs#L32) CompactIndexedAttestation with aggregation_bits and attesting_indices
- [`beacon_node/operation_pool/src/attestation_storage.rs:457`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs#L457) insert aggregates by bitlist disjointness

**Sources.** [teku#9721](https://github.com/Consensys-Incorporated/teku/pull/9721)

</details>


<a id="op_pool-046"></a>
<details>
<summary><b>op_pool-046</b> Keep best sync contribution per subnet, aggregate late — <i>implemented · low · bandwidth</i></summary>

**Idea.** Store the best (most participants) sync committee contribution per subnet and aggregate them only at block production, instead of pre-aggregating the first one seen. Sync aggregate participation rises.

**Best measured result.** participation 87% and 82% in test blocks vs about 50-60% before (pr:lodestar#2898)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/lib.rs:117-155`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L117-L155) insert_sync_contribution keeps the contribution with most set bits per subcommittee
- [`beacon_node/operation_pool/src/lib.rs:163-179`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L163-L179) get_sync_aggregate aggregates only at block production

**Sources.** [lodestar#2898](https://github.com/ChainSafe/lodestar/pull/2898)

</details>


<a id="op_pool-047"></a>
<details>
<summary><b>op_pool-047</b> Fill aggregate gaps from bounded single-attestation pool — <i>implemented · medium · memory</i></summary>

**Idea.** Keep a size-bounded pool of unaggregated single attestations and use them to add committee members missing from aggregates when packing blocks, so blocks carry more votes with bounded memory.

**Impact.** Singles already fill aggregate gaps through greedy aggregation on insert; memory bounded.

**Best measured result.** block production performance even better; memory bounded to 50MB (pr:lodestar#8076)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:5944`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5944) naive_aggregation_pool entries imported into op_pool before packing
- [`beacon_node/beacon_chain/src/naive_aggregation_pool.rs:143`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/naive_aggregation_pool.rs#L143) SLOTS_RETAINED=3, :148 MAX_ATTESTATIONS_PER_SLOT=16384 bound

**Sources.** [lodestar#8076](https://github.com/ChainSafe/lodestar/pull/8076)

</details>


<a id="op_pool-051"></a>
<details>
<summary><b>op_pool-051</b> Max-cover selection of sync committee contributions — <i>n/a · low · bandwidth, cpu</i></summary>

**Idea.** When building the block sync aggregate, select sync committee contributions with a greedy max-cover over aggregation bits so fewer non-overlapping contributions cover the most participants.

**Impact.** Subcommittee bit ranges are disjoint and only the best per subnet is kept, so there is no overlap for max-cover to resolve.

**Best measured result.** None (pr:prysm#14794)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/lib.rs:130-150`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L130-L150) only one best contribution per (slot,root,subcommittee) is kept
- [`consensus/types/src/sync_committee/sync_aggregate.rs:55`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/sync_committee/sync_aggregate.rs#L55) from_contributions ORs bits of disjoint subcommittees

**Sources.** [prysm#14794](https://github.com/OffchainLabs/prysm/pull/14794)

</details>


<a id="op_pool-052"></a>
<details>
<summary><b>op_pool-052</b> Word-packed native bitsets for aggregation bits — <i>not · low · M · cpu, memory</i></summary>

**Idea.** Represent attestation aggregation bits in the op pool as packed 64-bit-word bitsets (per committee for Electra) so superset checks, merges and max-cover scoring use word-level bit operations with constant allocations instead of generic SSZ bitlist operations.

**Gap in Lighthouse.** Replace BitList intersection/union in should_aggregate/aggregate with in-place word-wise is_disjoint/or_assign, and replace AttMaxCover's HashMap&lt;u64,u64&gt; fresh set with a bitset plus reward vec in max_cover.rs. Needs ssz_types support or a local bitset type.

**Impact.** get_attestations_for_block and insert_attestation would allocate less; Prysm saw ~8-10x on the bit ops, but the whole pack is dominated by reward computation, so the end-to-end gain is smaller.

**Best measured result.** None (pr:prysm#8352)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/attestation_storage.rs:35`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs#L35) aggregation_bits is ssz BitList (byte vec)
- attestation_storage.rs:237 should_aggregate uses intersection().is_zero(), allocating a new list
- attestation_storage.rs:244 aggregate uses union(), allocating
- [`beacon_node/operation_pool/src/attestation.rs:21`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation.rs#L21) max-cover set is HashMap&lt;u64,u64&gt; of validator index to reward

**Sources.** [teku#9393](https://github.com/Consensys-Incorporated/teku/pull/9393), [prysm#8352](https://github.com/OffchainLabs/prysm/pull/8352)

</details>


<a id="op_pool-053"></a>
<details>
<summary><b>op_pool-053</b> Parallel aggregation across attestation data groups — <i>partial · medium · S · cpu, latency</i></summary>

**Idea.** Aggregate attestations in the pool in parallel, one task per attestation data group on a worker pool sized to the CPU count, instead of serially.

**Gap in Lighthouse.** Run aggregate_across_committees over attestation data groups with rayon par_iter_mut (and the two epoch keys in parallel). Lighthouse aggregates incrementally on insert, so the large batch cost Prysm parallelized does not exist here.

**Impact.** Small: a few ms off the write-locked cross-committee step at block production on Electra+.

**Best measured result.** None (pr:prysm#12553)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/lib.rs:428`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L428) rayon::join only splits prev/curr epoch max cover (the only rayon use in operation_pool)
- [`beacon_node/operation_pool/src/lib.rs:379-382`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L379-L382) aggregate_across_committees runs serially for both epochs under the write lock
- [`beacon_node/operation_pool/src/attestation_storage.rs:489-497`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs#L489-L497) serial loop over attestation_map.attestations.values_mut()
- [`beacon_node/operation_pool/src/attestation_storage.rs:457-483`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs#L457-L483) per-insert greedy aggregation, so no batch aggregation step exists
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5944-5952`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5944-L5952) naive aggregation pool imported into op pool serially at block production

**Second check.** Grepped operation_pool and naive_aggregation_pool for rayon/par_iter and checked the block-production naive-pool import path; only the prev/curr max-cover join is parallel.

**Sources.** [prysm#12553](https://github.com/OffchainLabs/prysm/pull/12553), [prysm#13407](https://github.com/OffchainLabs/prysm/pull/13407)

</details>


<a id="op_pool-056"></a>
<details>
<summary><b>op_pool-056</b> Drop or replace subset aggregates on pool insertion — <i>partial · medium · S · memory, cpu, bandwidth</i></summary>

**Idea.** On inserting an attestation or aggregate into the pool, keyed by data root, skip it if an existing aggregate's bits are a superset and remove existing entries that it strictly supersedes, optionally capping aggregates per data. The pool keeps only non-dominated aggregates, saving memory, BLS work and block space.

**Gap in Lighthouse.** The 'skip if a superset is known' half exists at the gossip layer (ObservedAggregates), so dominated aggregates mostly never enter the pool. Missing: evicting existing pool entries that a newly inserted aggregate strictly supersedes, subset checks for naive-pool and API-imported items, and a per-data cap. Add that in AttestationMap::insert.

**Impact.** Modest: fewer max-cover candidates and less pool memory; most of the dominated-input filtering is already done at gossip, so the gain is smaller than Prysm/Lodestar saw.

**Best measured result.** None (pr:lodestar#2883)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/attestation_verification.rs:571-580`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L571-L580) gossip aggregates that are a non-strict subset of an already observed aggregate are rejected (AttestationSupersetKnown) before reaching the op pool
- [`beacon_node/beacon_chain/src/observed_aggregates.rs:262-287`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/observed_aggregates.rs#L262-L287) observe_item keeps only non-dominated aggregates per data root, replacing subsets with supersets
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2699-2713`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2699-L2713) add_to_block_inclusion_pool is the gossip/API entry into the op pool, fed only by verified aggregates
- [`beacon_node/operation_pool/src/attestation_storage.rs:470-482`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs#L470-L482) pool insert drops exact duplicates and merges disjoint ones, but never drops a subset or evicts entries the new item strictly supersedes

**Second check.** The earlier review only looked at operation_pool. ObservedAggregates subset/superset tracking in gossip aggregate verification already filters dominated aggregates before pool insert.

**Sources.** [prysm#4493](https://github.com/OffchainLabs/prysm/pull/4493), [prysm#6912](https://github.com/OffchainLabs/prysm/pull/6912), [caplin#12019](https://github.com/erigontech/erigon/pull/12019), [lodestar#2883](https://github.com/ChainSafe/lodestar/pull/2883), [ethlambda#313](https://github.com/lambdaclass/ethlambda/pull/313)

</details>


<a id="op_pool-058"></a>
<details>
<summary><b>op_pool-058</b> Store attesting indices and reward cache for packing — <i>implemented · low · cpu, latency</i></summary>

**Idea.** Store attesting indices with pooled attestations and keep a reward cache of per-validator participation bitfields, so block packing scores attestations without committee lookups and skips re-verifying attestations that are valid by construction.

**Best measured result.** None (pr:lighthouse#3312)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/attestation_storage.rs:70`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs#L70) SplitAttestation::new takes attesting_indices and stores them
- [`beacon_node/operation_pool/src/lib.rs:298`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L298) insert_attestation(attestation, attesting_indices)
- [`beacon_node/operation_pool/src/reward_cache.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/reward_cache.rs) (RewardCache of per-validator participation bools)
- [`beacon_node/operation_pool/src/lib.rs:370`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L370) reward_cache.update(state) in get_attestations
- [`beacon_node/operation_pool/src/attestation.rs:104`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation.rs#L104) uses att.indexed.attesting_indices() and reward_cache.has_attested_in_epoch

**Sources.** [lighthouse#3312](https://github.com/sigp/lighthouse/pull/3312)

</details>


<a id="op_pool-060"></a>
<details>
<summary><b>op_pool-060</b> Skip signature group checks when aggregating into pool — <i>implemented · low · cpu</i></summary>

**Idea.** When aggregating already gossip-verified attestation signatures into the op pool, skip the BLS signature group/subgroup validity check, which is redundant after gossip validation.

**Best measured result.** None (pr:lodestar#4838)

**Evidence (Lighthouse @ 928b61e719).**

- [`crypto/bls/src/impls/blst.rs:238`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L238) add_assign: add_signature(other,false) skips subgroup check
- [`crypto/bls/src/impls/blst.rs:242`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L242) add_assign_aggregate uses add_aggregate with no validation
- [`beacon_node/operation_pool/src/attestation_storage.rs:249`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs#L249) pool aggregation uses add_assign_aggregate

**Sources.** [lodestar#4838](https://github.com/ChainSafe/lodestar/pull/4838)

</details>


<a id="op_pool-064"></a>
<details>
<summary><b>op_pool-064</b> Prune operation pool on finalization — <i>implemented · low · memory, cpu, disk, latency</i></summary>

**Idea.** On each new finalized checkpoint, drop pool attestations and operations older than the finalized epoch (and aggregated payloads at or below the finalized slot), so the pool, its persisted copy and block-packing scans stay bounded.

**Best measured result.** None (pr:lighthouse#500)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/canonical_head.rs:1710`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1710) op_pool.prune_all called on finalization
- [`beacon_node/operation_pool/src/lib.rs:455`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L455) prune_attestations
- [`beacon_node/operation_pool/src/attestation_storage.rs:632`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs#L632) prune retains only target_epoch+1 &gt;= current_epoch
- [`beacon_node/operation_pool/src/lib.rs:750`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L750) prune_proposer/attester_slashings, voluntary_exits use finalized_state

**Sources.** [lighthouse@6150f0ae1](https://github.com/sigp/lighthouse/commit/6150f0ae1a54), [lighthouse#500](https://github.com/sigp/lighthouse/pull/500), [lodestar@ebe02a3af](https://github.com/ChainSafe/lodestar/commit/ebe02a3afb36), [lighthouse@9c2dfba84](https://github.com/sigp/lighthouse/commit/9c2dfba843c2), [ethlambda#389](https://github.com/lambdaclass/ethlambda/pull/389)

</details>


<a id="op_pool-072"></a>
<details>
<summary><b>op_pool-072</b> Reject slashings covering only already-slashed validators — <i>implemented · low · memory, cpu</i></summary>

**Idea.** On gossip, reject attester slashings whose slashable validators are all already slashed before they enter the op pool, so useless slashings use no memory or processing.

**Best measured result.** None (pr:lighthouse#5385)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_block_processing/verify_attester_slashing.rs:40`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/verify_attester_slashing.rs#L40) get_slashable_indices errors if none
- [`consensus/state_processing/src/per_block_processing/verify_attester_slashing.rs:56`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/verify_attester_slashing.rs#L56) uses is_slashable_at, so already-slashed validators are excluded
- [`beacon_node/beacon_chain/src/observed_operations.rs:114`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/observed_operations.rs#L114) validate runs before the op enters the pool

**Sources.** [lighthouse#5385](https://github.com/sigp/lighthouse/pull/5385)

</details>


<a id="op_pool-077"></a>
<details>
<summary><b>op_pool-077</b> Retain attestations of reorged-out blocks for reuse — <i>implemented · medium · cpu</i></summary>

**Idea.** When a block that included attestations is reorged out, keep (or restore) its attestations in the pool so the replacement block can include them.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/canonical_head.rs:1566`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1566) reorg only prunes by epoch, never removes included attestations
- [`beacon_node/operation_pool/src/lib.rs:455`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L455) prune_attestations drops only checkpoints older than 1 epoch
- [`beacon_node/operation_pool/src/attestation.rs:98`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation.rs#L98) max cover skips validators already in the packing state's participation, so reorged-out attestations are reused

**Sources.** [prysm#12107](https://github.com/OffchainLabs/prysm/pull/12107)

</details>


<a id="op_pool-081"></a>
<details>
<summary><b>op_pool-081</b> Fast path for single-bit attestations in bit ops — <i>not · low · S · cpu</i></summary>

**Idea.** Special-case single (one-bit) attestations in superset checks and aggregation of attestation bits, testing or setting one bit instead of running generic bitlist operations.

**Gap in Lighthouse.** Add a branch in AttestationMap::insert / should_aggregate for aggregation_bits.num_set_bits()==1 that tests and sets one bit (get/set) instead of allocating intersection and union.

**Impact.** Insert of unaggregated attestations (most gossip traffic when subscribed to many subnets) would skip two list allocations per existing aggregate; small, likely a few percent of op-pool insert cost.

**Best measured result.** None (pr:teku#9589)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/attestation_storage.rs:237-248`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs#L237-L248) Base aggregate/should_aggregate use generic BitList intersection and union for every attestation
- attestation_storage.rs:459-480 insert greedily aggregates each new attestation with all existing ones, no single-bit special case

**Sources.** [teku#9589](https://github.com/Consensys-Incorporated/teku/pull/9589)

</details>


<a id="op_pool-082"></a>
<details>
<summary><b>op_pool-082</b> One aggregate call over all collected signatures — <i>implemented · medium · S · cpu</i></summary>

**Idea.** When aggregating many attestations of a committee, collect all signatures and call BLS aggregate once, merging bits in one pass, instead of pairwise re-aggregation in a reduce.

**Impact.** None left to gain: an equivalent mechanism is in place. A one-shot bulk aggregate would cost the same N point adds as the incremental fold.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/naive_aggregation_pool.rs:281`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/naive_aggregation_pool.rs#L281) each gossip vote is folded into a running aggregate at insert time, so no per-request reduce exists
- [`beacon_node/beacon_chain/src/beacon_chain.rs:1886-1900`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1886-L1900) get_aggregated_attestation_electra (the validator aggregate API path, the Lodestar commit's target) is a map lookup of the pre-aggregated attestation
- [`crypto/bls/src/generic_aggregate_signature.rs:141`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/generic_aggregate_signature.rs#L141) add_assign_aggregate works on the held point, with no serialize/deserialize
- [`crypto/bls/src/impls/blst.rs:242`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L242) maps to blst AggregateSignature::add_aggregate
- blst-0.3.17/src/lib.rs:1670 add_aggregate is one in-place projective point add (add_or_dbl)
- [`beacon_node/operation_pool/src/attestation_storage.rs:252`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs#L252) op pool merge is likewise an in-place point add

**Second check.** The Lodestar fix replaces a reduce that called aggregate pairwise, with its conversion overhead per step, inside the validator getAggregatedAttestation API. Lighthouse keeps an already-aggregated attestation in the naive pool as an unserialized blst point and serves it by lookup. Each merge is one point add, which is exactly what a bulk aggregate does, so the earlier 'not' (which itself rated the impact negligible) is really an equivalent implementation.

**Sources.** [lodestar@269d3f0b2](https://github.com/ChainSafe/lodestar/commit/269d3f0b2ab7)

</details>


<a id="op_pool-087"></a>
<details>
<summary><b>op_pool-087</b> Slimmer single-attestation storage in pool — <i>n/a · low · memory</i></summary>

**Idea.** Drop per-seen-aggregate vote tracking from pooled single attestations so they take less memory and can be kept for more slots.

**Gap in Lighthouse.** Lighthouse's pools do not keep the per-aggregate vote tracking that Lodestar's SeenAttestation structure had, so there is nothing to drop.

**Best measured result.** None (pr:lodestar#8084)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/naive_aggregation_pool.rs:238`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/naive_aggregation_pool.rs#L238) pool stores one Attestation per data root, no per-seen-aggregate vote tracking
- [`beacon_node/operation_pool/src/attestation_storage.rs:32`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs#L32) compact attestation holds only bits, indices, signature

**Sources.** [lodestar#8084](https://github.com/ChainSafe/lodestar/pull/8084)

</details>


<a id="op_pool-088"></a>
<details>
<summary><b>op_pool-088</b> Time-boxed lock-free block attestation packing — <i>not · medium · M · cpu, latency</i></summary>

**Idea.** Build block attestation aggregates without a global pool lock and under a time budget, sort by reward and take the top entries, then fill up with single attestations under a total budget, so block production latency is bounded.

**Gap in Lighthouse.** There is no time budget for packing and no lock-free snapshot. Add a deadline to maximum_cover (return the best result so far) and/or take a snapshot of the per-checkpoint map so that packing does not hold the pool RwLock. Move the Electra aggregate_across_committees work out of the write-locked section. Lighthouse already has the parts that are not time-boxing: greedy packing ordered by reward score, and insert-time aggregation of single votes (a fill-up equivalent).

**Impact.** This affects tail latency only. It bounds block production time with very large pools (non-finality, many aggregates that do not merge). Typical mainnet packing takes tens of ms.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/lib.rs:381-387`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L381-L387) attestations.write() held for aggregate_across_committees, then downgraded to a read lock that is held through packing (blocks insert_attestation writers at lib.rs:301)
- [`beacon_node/operation_pool/src/max_cover.rs:53-80`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/max_cover.rs#L53-L80) greedy maximum_cover, O(limit x items), no deadline or early exit
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5964-5989`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5964-L5989) block production calls get_attestations synchronously with only a timer metric, no timeout
- [`beacon_node/operation_pool/src/lib.rs:424`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L424) only prev/curr epoch packed in parallel (rayon::join)

**Second check.** I also checked the block production call site for a timeout or a spawn_blocking deadline (none), and the max_cover internals for an early exit (none). Reward-sorted selection and insert-time aggregation exist, but the idea's core (time-boxed and lock-free) is absent.

**Sources.** [teku#9445](https://github.com/Consensys-Incorporated/teku/pull/9445)

</details>


