# op_pool

96 ideas: 9 not, 23 partial, 43 implemented, 21 n/a; 9 actionable (high or medium value, verdict `not` or `partial`). [Back to the summary](../README.md).

| id | idea | verdict | value | effort | resources |
|---|---|---|---|---|---|
| [op_pool-001](#op_pool-001) **★** | Bound pool size with hard cap and oldest-first eviction | partial | medium | S | memory |
| [op_pool-002](#op_pool-002) | Size pool retention to the inclusion window | implemented | low | S | memory |
| [op_pool-003](#op_pool-003) **★** | Skip attestations whose attesters are already on chain | partial | medium | M | cpu, bandwidth, memory |
| [op_pool-004](#op_pool-004) **★** | Remove block-included attestations from the pool on import | not | medium | M | memory, bandwidth, cpu |
| [op_pool-005](#op_pool-005) | Aggregate attestations into pool entries on arrival | implemented | low | S | cpu, memory, bandwidth, latency |
| [op_pool-006](#op_pool-006) | Aggregate lazily at block production or aggregator duty | partial | low | M | cpu, memory, latency |
| [op_pool-007](#op_pool-007) | Avoid duplicate aggregation passes per slot | partial | low | S | cpu, memory |
| [op_pool-008](#op_pool-008) **★** | Aggregate only committees a local aggregator will request | partial | medium | S | cpu, memory |
| [op_pool-009](#op_pool-009) | Index pool entries in hash maps by data root | implemented | low | S | cpu |
| [op_pool-010](#op_pool-010) | Prune pool by slot inclusion window each slot | partial | low | S | memory, cpu |
| [op_pool-011](#op_pool-011) | Reuse stored roots instead of rehashing pool keys | implemented | low | S | cpu |
| [op_pool-012](#op_pool-012) | Fast custom hash for attestation pool keys | partial | low | M | cpu |
| [op_pool-013](#op_pool-013) | Lightweight pooled-attestation struct | implemented | low | S | cpu |
| [op_pool-014](#op_pool-014) **★** | Fine-grained or concurrent locking in the op pool | partial | medium | M | cpu, latency |
| [op_pool-015](#op_pool-015) | Greedy max-cover attestation selection by marginal reward | implemented | medium | S | cpu, bandwidth |
| [op_pool-016](#op_pool-016) | Greedy packing instead of unbounded ILP solver | implemented | low | S | cpu, latency |
| [op_pool-017](#op_pool-017) | In-place bitfield operations in max-cover | partial | low | M | cpu, memory |
| [op_pool-018](#op_pool-018) | Compare and merge aggregates with bitfields, not indices | partial | low | M | cpu |
| [op_pool-019](#op_pool-019) **★** | Fast Electra committee-bits aggregation | partial | medium | S | cpu, memory |
| [op_pool-020](#op_pool-020) | Electra cross-committee merge of aggregates at packing | implemented | medium | S | cpu, bandwidth |
| [op_pool-021](#op_pool-021) | Key packing candidates by data and committee index | implemented | medium | S | bandwidth |
| [op_pool-022](#op_pool-022) | Group by committee, cache validity, prune by score bound | partial | low | M | cpu, latency |
| [op_pool-023](#op_pool-023) | Merge only within committee and skip subset candidates | partial | low | S | cpu, latency |
| [op_pool-024](#op_pool-024) | Filter packing candidates by dependent root first | implemented | low | S | cpu |
| [op_pool-025](#op_pool-025) | Check attestation targets without slot processing | implemented | medium | S | cpu, latency |
| [op_pool-026](#op_pool-026) | Validate exits without cloning or advancing state | implemented | low | S | cpu, memory |
| [op_pool-027](#op_pool-027) | Drop duplicate exits before storing | implemented | low | S | cpu, disk |
| [op_pool-028](#op_pool-028) | Stop exit selection at the per-block maximum | implemented | low | S | cpu |
| [op_pool-029](#op_pool-029) | Linked list with map index for operation pools | n/a | low |  | memory |
| [op_pool-030](#op_pool-030) | Key slashings and exits by validator, prune with retain | implemented | low | S | cpu |
| [op_pool-031](#op_pool-031) | Prune op pools in a background worker off the lock | not | low | S | latency, cpu |
| [op_pool-032](#op_pool-032) | Batch database deletes when pruning pooled aggregates | n/a | low |  | cpu, disk |
| [op_pool-033](#op_pool-033) | Skip canonical-chain check when pruning included attestations | n/a | low | S | cpu |
| [op_pool-034](#op_pool-034) | Keep pools in memory, persist only on shutdown | implemented | low | S | disk, latency |
| [op_pool-035](#op_pool-035) | Delete attestations that fail verification | n/a | low | S | cpu, disk |
| [op_pool-036](#op_pool-036) | Reject too-old attestations at pool entry | implemented | low | S | cpu, memory |
| [op_pool-037](#op_pool-037) | Allocation-free committee index computation | implemented | low | S | memory, cpu |
| [op_pool-038](#op_pool-038) | Pass sync message pool by reference to verifier | n/a | low | S | cpu, memory |
| [op_pool-039](#op_pool-039) | Batch-verify signatures of packed operations | n/a | medium |  | cpu |
| [op_pool-040](#op_pool-040) | Rate-limit broadcast of queued operation bursts | n/a | low | S | bandwidth, latency, cpu |
| [op_pool-041](#op_pool-041) | Cache deserialized signatures of pooled attestations | implemented | medium | S | cpu, latency |
| [op_pool-042](#op_pool-042) | Reuse gossip-validation results when inserting contributions | not | low | S | cpu |
| [op_pool-043](#op_pool-043) | Cached base rewards for attestation reward scoring | implemented | low | S | cpu |
| [op_pool-044](#op_pool-044) | Expire stale proposer preparation and registrations | implemented | low | S | memory |
| [op_pool-045](#op_pool-045) | Pool indexed by validator participation | implemented | medium | S | cpu, latency |
| [op_pool-046](#op_pool-046) | Keep best sync contribution per subnet, aggregate late | implemented | low | S | bandwidth |
| [op_pool-047](#op_pool-047) | Fill aggregate gaps from bounded single-attestation pool | implemented | medium | S | memory |
| [op_pool-048](#op_pool-048) | Store one proof per data root, not per validator | n/a | low | S | memory, disk, cpu |
| [op_pool-049](#op_pool-049) | Keep seen-attestation cache for two epochs | implemented | low | S | bandwidth, cpu |
| [op_pool-050](#op_pool-050) | Max-cover aggregation of pooled attestations | partial | low | M | cpu, bandwidth |
| [op_pool-051](#op_pool-051) | Max-cover selection of sync committee contributions | n/a | low |  | bandwidth, cpu |
| [op_pool-052](#op_pool-052) | Word-packed native bitsets for aggregation bits | not | low | M | cpu, memory |
| [op_pool-053](#op_pool-053) **★** | Parallel aggregation across attestation data groups | partial | medium | S | cpu, latency |
| [op_pool-054](#op_pool-054) | Shorter read-lock holds in naive aggregation pool | partial | low | S | latency |
| [op_pool-055](#op_pool-055) | Aggregate sync messages only for receiving subnet | not | low | S | cpu |
| [op_pool-056](#op_pool-056) **★** | Drop or replace subset aggregates on pool insertion | partial | medium | S | memory, cpu, bandwidth |
| [op_pool-057](#op_pool-057) | Skip subset sync contributions, key by slot | implemented | low | S | memory, cpu |
| [op_pool-058](#op_pool-058) | Store attesting indices and reward cache for packing | implemented | low | S | cpu, latency |
| [op_pool-059](#op_pool-059) | Skip BLS re-verification of pooled operations at packing | implemented | low | S | cpu |
| [op_pool-060](#op_pool-060) | Skip signature group checks when aggregating into pool | implemented | low | S | cpu |
| [op_pool-061](#op_pool-061) | Priority queue with evict-on-access for sync pool | n/a | low |  | cpu, memory |
| [op_pool-062](#op_pool-062) | Store pristine attestations to avoid conversion | not | low | M | cpu |
| [op_pool-063](#op_pool-063) | Remove included BLS changes from pool on import | implemented | low | S | memory |
| [op_pool-064](#op_pool-064) | Prune operation pool on finalization | implemented | low | S | memory, cpu, disk, latency |
| [op_pool-065](#op_pool-065) | Prune finalized deposits from pending deposit store | n/a | low |  | memory |
| [op_pool-066](#op_pool-066) | Prune sync committee message pool by slot | partial | low | S | memory |
| [op_pool-067](#op_pool-067) | Prune pending pools every epoch | n/a | low |  | memory |
| [op_pool-068](#op_pool-068) | Prune voluntary exits signed under old forks | partial | low | S | memory, cpu |
| [op_pool-069](#op_pool-069) | Prune BLS change pool using head state | implemented | low | S | memory |
| [op_pool-070](#op_pool-070) | Prune op pool without regenerating finalized state; persist diff | implemented | low | S | disk, memory, cpu |
| [op_pool-071](#op_pool-071) | Rebuild pool hash map after surge drains | partial | low | S | memory |
| [op_pool-072](#op_pool-072) | Reject slashings covering only already-slashed validators | implemented | low | S | memory, cpu |
| [op_pool-073](#op_pool-073) | Skip unslashable proposer slashings at block packing | implemented | low | S | cpu, bandwidth |
| [op_pool-074](#op_pool-074) | Single pass when marking BLS changes included | implemented | low | S | cpu |
| [op_pool-075](#op_pool-075) | Drop redundant dedup pass in max-cover | implemented | low | S | cpu |
| [op_pool-076](#op_pool-076) | No deep copy when pushing to pool queue | n/a | low | S | cpu |
| [op_pool-077](#op_pool-077) | Retain attestations of reorged-out blocks for reuse | implemented | low | S | cpu |
| [op_pool-078](#op_pool-078) | Separate pool for orphaned-block attestations | n/a | low | S | cpu |
| [op_pool-079](#op_pool-079) | Persistent iterator in attestation aggregating iterator | n/a | low |  | cpu |
| [op_pool-080](#op_pool-080) | Single-pass op pool metrics | implemented | low | S | cpu |
| [op_pool-081](#op_pool-081) | Fast path for single-bit attestations in bit ops | not | low | S | cpu |
| [op_pool-082](#op_pool-082) | One aggregate call over all collected signatures | implemented | low | S | cpu |
| [op_pool-083](#op_pool-083) | Skip duplicate attestation save, delete and broadcast | implemented | low | S | cpu |
| [op_pool-084](#op_pool-084) | Avoid removing included attestations twice | n/a | low |  | cpu |
| [op_pool-085](#op_pool-085) | Do not store empty pool entries | implemented | low | S | memory, cpu |
| [op_pool-086](#op_pool-086) | Rescore only same-data aggregates during packing | partial | low | S | cpu |
| [op_pool-087](#op_pool-087) | Slimmer single-attestation storage in pool | n/a | low |  | memory |
| [op_pool-088](#op_pool-088) **★** | Time-boxed lock-free block attestation packing | not | medium | M | cpu, latency |
| [op_pool-089](#op_pool-089) | Optimize unaggregated storage and expiry paths | n/a | low |  | cpu |
| [op_pool-090](#op_pool-090) | Share one attestation pool for fork choice and blocks | n/a | low |  | memory, cpu |
| [op_pool-091](#op_pool-091) | Validate max-cover inputs once | n/a | low |  | cpu |
| [op_pool-092](#op_pool-092) | Cache block roots by slot while filtering attestations | partial | low | S | cpu, latency |
| [op_pool-093](#op_pool-093) | Drop single-vote attestations once committee aggregate exists | partial | low | S | cpu, memory |
| [op_pool-094](#op_pool-094) | Lazy max-heap greedy max-cover for block attestations | not | low | M | cpu |
| [op_pool-095](#op_pool-095) | Remove unused state fetch and slot advance in attestation path | n/a | low |  | cpu |
| [op_pool-096](#op_pool-096) | Skip re-verifying gossip-verified attestations in the pool | implemented | low | S | cpu |

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

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [ethlambda#290](https://github.com/lambdaclass/ethlambda/pull/290), [teku#5305](https://github.com/Consensys-Incorporated/teku/pull/5305), [ethlambda#182](https://github.com/lambdaclass/ethlambda/pull/182)

</details>


<a id="op_pool-002"></a>
<details>
<summary><b>op_pool-002</b> Size pool retention to the inclusion window — <i>implemented · low · S · memory</i></summary>

**Idea.** Size the attestation pool cap and retention period so it still holds every attestation that can be included (64 slots post-EIP-7045, worst-case validator set), and re-read the live size while trimming. Block building then still has old attestations instead of pruning them early.

**Impact.** Already done; retention covers the full EIP-7045 window and there is no count cap that can trim early.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/attestation_storage.rs:632-635`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs#L632-L635) prune keeps target_epoch+1 &gt;= current_epoch (previous and current epoch)
- [`beacon_node/operation_pool/src/lib.rs:455-457`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L455-L457) prune_attestations is the only removal
- [`beacon_node/beacon_chain/src/canonical_head.rs:1566`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1566) pruned by epoch on head update

**Skeptic check.** The op pool has no size cap (max_aggregates_per_data is a stat only) and retains previous+current epoch, which covers every includable attestation. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#8110](https://github.com/Consensys-Incorporated/teku/pull/8110), [teku#8114](https://github.com/Consensys-Incorporated/teku/pull/8114)

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

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [prysm#7015](https://github.com/OffchainLabs/prysm/pull/7015), [prysm#7203](https://github.com/OffchainLabs/prysm/pull/7203), [nimbus#2061](https://github.com/status-im/nimbus-eth2/pull/2061), [teku#916](https://github.com/Consensys-Incorporated/teku/pull/916), [teku#701](https://github.com/Consensys-Incorporated/teku/pull/701), [teku#2969](https://github.com/Consensys-Incorporated/teku/pull/2969), [prysm#6993](https://github.com/OffchainLabs/prysm/pull/6993), [teku#4312](https://github.com/Consensys-Incorporated/teku/pull/4312), [teku#4311](https://github.com/Consensys-Incorporated/teku/pull/4311)

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

**Verdict history.** not (checked) → not (refuted)

**Sources.** [teku#2000](https://github.com/Consensys-Incorporated/teku/pull/2000), [prysm#14896](https://github.com/OffchainLabs/prysm/pull/14896), [lodestar@4d2caec94](https://github.com/ChainSafe/lodestar/commit/4d2caec94991), [prysm#10623](https://github.com/OffchainLabs/prysm/pull/10623), [prysm#9444](https://github.com/OffchainLabs/prysm/pull/9444), [prysm#4241](https://github.com/OffchainLabs/prysm/pull/4241), [prysm#4798](https://github.com/OffchainLabs/prysm/pull/4798), [prysm#1942](https://github.com/OffchainLabs/prysm/pull/1942), [prysm#11771](https://github.com/OffchainLabs/prysm/pull/11771), [prysm#1626](https://github.com/OffchainLabs/prysm/pull/1626)

</details>


<a id="op_pool-005"></a>
<details>
<summary><b>op_pool-005</b> Aggregate attestations into pool entries on arrival — <i>implemented · low · S · cpu, memory, bandwidth, latency</i></summary>

**Idea.** When an unaggregated gossip attestation arrives, OR its bits and add its signature into an existing pool aggregate with the same data (keyed by attestation data), so the pool holds few large aggregates. Fewer objects are stored, hashed and compared, and an aggregator request becomes a lookup of a precomputed aggregate.

**Impact.** Already in place; the aggregator endpoint is a hash map lookup of a precomputed aggregate.

**Best measured result.** None (pr:prysm#4376)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/naive_aggregation_pool.rs:255-293`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/naive_aggregation_pool.rs#L255-L293) AggregatedAttestationMap::insert ORs the single bit and aggregates the signature into the one entry per attestation key root
- [`beacon_node/beacon_chain/src/naive_aggregation_pool.rs:543-547`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/naive_aggregation_pool.rs#L543-L547) get() serves aggregator requests by lookup
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:422-456`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L422-L456) gossip unaggregated attestations go into the naive pool on arrival when should_import
- [`beacon_node/operation_pool/src/attestation_storage.rs:457-484`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs#L457-L484) AttestationMap::insert greedily merges disjoint aggregates with the same data

**Skeptic check.** Verified that single gossip votes are aggregated on arrival into one entry per data (naive pool) and the op pool merges disjoint aggregates on insert. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#3761](https://github.com/OffchainLabs/prysm/pull/3761), [prysm#3149](https://github.com/OffchainLabs/prysm/pull/3149), [prysm#4794](https://github.com/OffchainLabs/prysm/pull/4794), [prysm#4478](https://github.com/OffchainLabs/prysm/pull/4478), [lodestar#2851](https://github.com/ChainSafe/lodestar/pull/2851), [lodestar#2679](https://github.com/ChainSafe/lodestar/pull/2679), [prysm#14324](https://github.com/OffchainLabs/prysm/pull/14324), [prysm#16158](https://github.com/OffchainLabs/prysm/pull/16158), [lighthouse#950](https://github.com/sigp/lighthouse/pull/950), [prysm#4376](https://github.com/OffchainLabs/prysm/pull/4376), [lighthouse#10038](https://github.com/sigp/lighthouse/pull/10038)

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

**Verdict history.** not (checked) → partial (refuted)

**Sources.** [prysm#7206](https://github.com/OffchainLabs/prysm/pull/7206), [grandine@fca5f062a](https://github.com/grandinetech/grandine/commit/fca5f062a1a6), [lodestar#5284](https://github.com/ChainSafe/lodestar/pull/5284), [lodestar#5256](https://github.com/ChainSafe/lodestar/pull/5256)

</details>


<a id="op_pool-009"></a>
<details>
<summary><b>op_pool-009</b> Index pool entries in hash maps by data root — <i>implemented · low · S · cpu</i></summary>

**Idea.** Index attestations (and other pool items) by attestation data root or id in a hash map, so existence checks and lookups are O(1) and do not rehash data or scan the list.

**Impact.** Already O(1) lookups by data key in every pool.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/attestation_storage.rs:59-67`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs#L59-L67) HashMap&lt;CheckpointKey, HashMap&lt;CompactAttestationData, Vec&lt;..&gt;&gt;&gt;
- [`beacon_node/beacon_chain/src/naive_aggregation_pool.rs:236-239`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/naive_aggregation_pool.rs#L236-L239) HashMap keyed by AttestationKeyRoot
- [`beacon_node/operation_pool/src/lib.rs:52-70`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L52-L70) slashings/exits/payload attestations in HashMap/HashSet

**Skeptic check.** All pools are hash maps keyed by data (op pool) or data root (naive pool), with no list scans for existence. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#4837](https://github.com/OffchainLabs/prysm/pull/4837), [teku#749](https://github.com/Consensys-Incorporated/teku/pull/749), [lodestar#2295](https://github.com/ChainSafe/lodestar/pull/2295)

</details>


<a id="op_pool-010"></a>
<details>
<summary><b>op_pool-010</b> Prune pool by slot inclusion window each slot — <i>partial · low · S · memory, cpu</i></summary>

**Idea.** Store pool entries in per-slot maps and, every slot, drop whole slots that fall outside the inclusion window by the current wall-clock slot (for every attestation variant), instead of per-entry TTL caches or finality-based pruning. The pool stays bounded even during non-finality.

**Gap in Lighthouse.** OperationPool::prune_sync_contributions and prune_payload_attestations are called only from prune_all, which runs only when finality advances (canonical_head.rs:1710). During non-finality the sync contributions and payload attestations of the op pool are never pruned, so they grow with every slot and are all serialized by persist_op_pool. Call both from per_slot_task with the current slot.

**Impact.** Bounded memory during long non-finality (a few MB per day of sync contributions) and a smaller persisted op pool; no effect while the chain finalizes.

**Best measured result.** None (pr:teku#5197)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:7477`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L7477) naive_aggregation_pool pruned every slot by wall clock
- [`beacon_node/beacon_chain/src/naive_aggregation_pool.rs:555-580`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/naive_aggregation_pool.rs#L555-L580) per-slot maps, SLOTS_RETAINED=3
- [`beacon_node/beacon_chain/src/canonical_head.rs:1564-1567`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1564-L1567) op pool attestations pruned by wall-clock epoch on epoch transition or reorg
- [`beacon_node/operation_pool/src/lib.rs:191-200`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L191-L200) prune_sync_contributions is slot-based but
- [`beacon_node/operation_pool/src/lib.rs:739-753`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L739-L753) its only caller is prune_all
- [`beacon_node/beacon_chain/src/canonical_head.rs:1710`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1710) prune_all runs only on finalization

**Skeptic check.** Unaggregated and op-pool attestations are pruned by wall-clock slot/epoch independent of finality, as the earlier evidence said. But the other variants in the same pool (sync contributions, Gloas payload attestations) are pruned only on finalization, which is the exact failure mode the idea fixes.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [prysm#5087](https://github.com/OffchainLabs/prysm/pull/5087), [nimbus@535819263](https://github.com/status-im/nimbus-eth2/commit/535819263d61), [lighthouse#1805](https://github.com/sigp/lighthouse/pull/1805), [teku#1741](https://github.com/Consensys-Incorporated/teku/pull/1741), [prysm#2439](https://github.com/OffchainLabs/prysm/pull/2439), [prysm#2442](https://github.com/OffchainLabs/prysm/pull/2442), [teku#5197](https://github.com/Consensys-Incorporated/teku/pull/5197), [teku#966](https://github.com/Consensys-Incorporated/teku/pull/966)

</details>


<a id="op_pool-011"></a>
<details>
<summary><b>op_pool-011</b> Reuse stored roots instead of rehashing pool keys — <i>implemented · low · S · cpu</i></summary>

**Idea.** When pruning or deleting pool or seen-cache entries, reuse the already stored key or hash_tree_root instead of recomputing it, and rank attestations by participant count. This removes repeated hashing and shortens lock hold time.

**Impact.** None left: no pool or seen-cache prune path recomputes a key or hash_tree_root.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/attestation_storage.rs:13`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs#L13) CheckpointKey/CompactAttestationData keys are plain fields, no tree hash
- [`beacon_node/operation_pool/src/attestation_storage.rs:632`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs#L632) prune is a HashMap::retain on the stored checkpoint key
- [`beacon_node/beacon_chain/src/naive_aggregation_pool.rs:557`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/naive_aggregation_pool.rs#L557) prune drops whole per-slot maps
- [`beacon_node/beacon_chain/src/observed_aggregates.rs:429`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/observed_aggregates.rs#L429) prune retains sets by stored slot
- [`beacon_node/operation_pool/src/attestation.rs:78`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation.rs#L78) max-cover scoring by new participants

**Skeptic check.** Checked the op pool, naive aggregation pool and observed-aggregates prune paths: all prune by stored slot/epoch keys without rehashing. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#2351](https://github.com/ChainSafe/lodestar/pull/2351), [prysm#13261](https://github.com/OffchainLabs/prysm/pull/13261)

</details>


<a id="op_pool-012"></a>
<details>
<summary><b>op_pool-012</b> Fast custom hash for attestation pool keys — <i>partial · low · M · cpu</i></summary>

**Idea.** Key pool attestations with a fast non-SSZ hash of their fields instead of the generic SSZ hash_tree_root. Key computation becomes over 10x cheaper.

**Gap in Lighthouse.** AggregatedAttestationMap::insert (naive_aggregation_pool.rs:255) keys each unaggregated gossip attestation by an SSZ tree_hash_root of AttestationData plus committee index (about 10 SHA-256 compressions), although signature verification already computed the data root. A map keyed by AttestationKey with a derived Hash, plus a root-&gt;key index only for the API lookup by root, would remove this per-attestation hashing.

**Impact.** About 1-2 us per unaggregated gossip attestation on aggregating nodes (should_import); a few ms per slot of CPU at most.

**Best measured result.** 24274 ns/op -&gt; 1582 ns/op (pr:prysm#5217)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/attestation_storage.rs:59-67`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs#L59-L67) op pool keyed by CompactAttestationData with derived Hash, no tree hash
- [`beacon_node/beacon_chain/src/naive_aggregation_pool.rs:62-110`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/naive_aggregation_pool.rs#L62-L110) AttestationKey::from_attestation_ref computes att.data.tree_hash_root()
- [`beacon_node/beacon_chain/src/naive_aggregation_pool.rs:267-268`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/naive_aggregation_pool.rs#L267-L268) every gossip insert computes attestation_key.tree_hash_root() as the map key
- [`beacon_node/beacon_chain/src/naive_aggregation_pool.rs:303`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/naive_aggregation_pool.rs#L303) get() hashes again

**Skeptic check.** The op pool path is fast-keyed as the earlier evidence said, but the naive aggregation pool, which is the per-gossip-message hot path the Prysm PR targeted, still keys by SSZ hash_tree_root. Partly forced by the API, which looks up by attestation_data_root.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [prysm#5217](https://github.com/OffchainLabs/prysm/pull/5217)

</details>


<a id="op_pool-013"></a>
<details>
<summary><b>op_pool-013</b> Lightweight pooled-attestation struct — <i>implemented · low · S · cpu</i></summary>

**Idea.** Hold a dedicated minimal struct for attestations in the aggregation pool instead of wrapping full validatable attestation objects, so packing avoids conversions and extra hashing.

**Impact.** Pool already holds a minimal struct; packing works on refs and converts only the chosen ones.

**Best measured result.** getAttestationsForBlock 0.021 -&gt; 0.017 s/op (pr:teku#9407)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/attestation_storage.rs:19`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs#L19) CompactAttestationData
- [`beacon_node/operation_pool/src/attestation_storage.rs:32`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs#L32) CompactIndexedAttestation with precomputed attesting_indices
- [`beacon_node/operation_pool/src/attestation_storage.rs:70`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs#L70) SplitAttestation::new splits on insert
- [`beacon_node/operation_pool/src/lib.rs:317`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L317) get_valid_attestations_for_epoch packs over CompactAttestationRef

**Skeptic check.** Verified the pool stores compact data plus indices and max-cover runs on CompactAttestationRef; earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#9407](https://github.com/Consensys-Incorporated/teku/pull/9407)

</details>


<a id="op_pool-014"></a>
<details>
<summary><b>op_pool-014</b> Fine-grained or concurrent locking in the op pool — <i>partial · medium · M · cpu, latency</i></summary>

**Idea.** Put the locks inside the operation pool, per pool field or per attestation-data key, or use concurrent maps and lock-free groups, instead of one big lock around the whole pool on the chain. Gossip inserts and block production reads then do not contend on a single lock.

**Gap in Lighthouse.** There is no per-checkpoint or per-data locking for attestations. OperationPool::get_attestations holds the single attestations lock in write mode for aggregate_across_committees (quadratic bit copy, ~1.6 ms per data, see op_pool-019) and in read mode for the whole packing, so every insert_attestation from gossip aggregates and the naive-pool import wait for the whole block production packing. Lock per CheckpointKey (or per data), or aggregate on a snapshot outside the lock.

**Impact.** Removes gossip-insert stalls of tens to ~100+ ms during block production (mainnet beacon_block_production_attestation_seconds is 170-270 ms on sigp ma-* nodes, of which max cover is ~5 ms and the reward cache ~38 ms).

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/lib.rs:52-70`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L52-L70) one RwLock per pool field, but all attestations share one RwLock&lt;AttestationMap&gt;
- [`beacon_node/operation_pool/src/lib.rs:381-387`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L381-L387) get_attestations takes the attestations write lock for aggregate_across_committees
- [`beacon_node/operation_pool/src/lib.rs:389-446`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L389-L446) then holds the downgraded read guard through both maximum_cover runs
- [`beacon_node/operation_pool/src/lib.rs:295-303`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L295-L303) insert_attestation needs the same write lock

**Skeptic check.** The earlier evidence was right that the locks are per field and not chain-level, but the attestation field is one big lock held across block-production packing, which is the contention the Teku and Prysm changes removed.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [lighthouse@cd9494181](https://github.com/sigp/lighthouse/commit/cd9494181c80), [teku#9297](https://github.com/Consensys-Incorporated/teku/pull/9297), [teku#9225](https://github.com/Consensys-Incorporated/teku/pull/9225), [teku#9438](https://github.com/Consensys-Incorporated/teku/pull/9438), [lighthouse#339](https://github.com/sigp/lighthouse/pull/339), [prysm#3470](https://github.com/OffchainLabs/prysm/pull/3470)

</details>


<a id="op_pool-015"></a>
<details>
<summary><b>op_pool-015</b> Greedy max-cover attestation selection by marginal reward — <i>implemented · medium · S · cpu, bandwidth</i></summary>

**Idea.** When producing a block, select attestations from the op pool with a greedy maximum-coverage algorithm whose score is the marginal proposer reward (validators newly covered given those already chosen), instead of naive ordering. Blocks carry more rewarded attesters within the attestation limit.

**Impact.** Already packs by marginal proposer reward.

**Best measured result.** Prysm packed 8 attestations where others pack 1-2 (pr:prysm#17416)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/max_cover.rs:53-101`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/max_cover.rs#L53-L101) greedy maximum_cover with covering-set updates after each pick
- [`beacon_node/operation_pool/src/attestation.rs:165-178`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation.rs#L165-L178) score = sum of fresh validator proposer rewards, covered validators removed
- [`beacon_node/operation_pool/src/lib.rs:428-446`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L428-L446) prev/curr runs merged by score

**Skeptic check.** Verified greedy max-cover with marginal reward scoring. A residual: aggregate_across_committees (attestation_storage.rs:520-560) picks the per-committee aggregate for the on-chain aggregate by num_set_bits, not fresh reward, but the other aggregates stay available to max cover, so the effect is mostly kept.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#17416](https://github.com/OffchainLabs/prysm/pull/17416), [prysm#6305](https://github.com/OffchainLabs/prysm/pull/6305), [prysm#10109](https://github.com/OffchainLabs/prysm/pull/10109), [caplin#11984](https://github.com/erigontech/erigon/pull/11984), [lighthouse@38d2d03e3](https://github.com/sigp/lighthouse/commit/38d2d03e3a98), [lighthouse#416](https://github.com/sigp/lighthouse/pull/416), [prysm#6344](https://github.com/OffchainLabs/prysm/pull/6344), [prysm#9684](https://github.com/OffchainLabs/prysm/pull/9684)

</details>


<a id="op_pool-016"></a>
<details>
<summary><b>op_pool-016</b> Greedy packing instead of unbounded ILP solver — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Pack attestations with a greedy best-per-committee pass, and either drop the integer-programming/knapsack solver or cap its input (aggregates per data) so it fits a time budget. Packing CPU stays bounded with almost no loss of coverage.

**Impact.** Packing is already greedy; max cover itself costs ~1-5 ms on mainnet (op_pool_attestation_*_epoch_packing_time on sigp ma-* nodes).

**Best measured result.** a plain best-per-committee greedy already covers 99.89% of observed attesters (pr:grandine#823)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/max_cover.rs:53`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/max_cover.rs#L53) plain greedy, no ILP/knapsack
- [`beacon_node/operation_pool/src/lib.rs:428-446`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L428-L446) two greedy runs in rayon::join

**Skeptic check.** No solver exists to drop; measured max cover time is small, so an input cap gives nothing. Earlier verdict upheld.

**Verdict history.** implemented (checked) → implemented (skeptic)

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
<summary><b>op_pool-019</b> Fast Electra committee-bits aggregation — <i>partial · medium · S · cpu, memory</i></summary>

**Idea.** In post-Electra aggregation, skip committee-bit remapping when committee bits are equal, avoid recomputing committee start offsets and SSZ-hashing committee bits in superset checks, and OR aggregation bits directly on a bitset. Aggregation of many attestations gets faster with less memory.

**Gap in Lighthouse.** compute_on_chain_aggregate calls aggregate_with_disjoint_committees once per committee. Each call runs bitlist_extend, which allocates a new BitList and copies every bit of the growing aggregate one at a time, and re-merges the growing attesting_indices Vec. That is O(committees^2 * committee_size) per attestation data. Build the on-chain aggregate once: compute total length, then copy each committee's bytes (shift-OR at the offset) and concatenate the sorted indices once. Inferior single-committee aggregates are also re-aggregated on every call.

**Impact.** Scratch bench (64 committees x 488 bits, mainnet size, ssz 974f78f, release): 1.59 ms per attestation data for the bit copy alone. With ~64+ data across prev/curr epoch that is ~100 ms per block production under the attestations write lock. Mainnet beacon_block_production_attestation_seconds is 170-270 ms on sigp ma-* nodes, against ~5 ms max cover and ~38 ms reward cache.

**Best measured result.** or rewrite ~4x faster, far less memory (pr:teku#8346)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/attestation_storage.rs:254-277`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs#L254-L277) same-committee checks and unions are byte-wise, no hashing (upheld)
- [`beacon_node/operation_pool/src/attestation_storage.rs:279-300`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs#L279-L300) aggregate_with_disjoint_committees rebuilds the whole bitlist and merges attesting_indices for every committee added
- [`beacon_node/operation_pool/src/attestation_storage.rs:415-431`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs#L415-L431) bitlist_extend copies bit by bit with get/set
- [`beacon_node/operation_pool/src/attestation_storage.rs:578-586`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs#L578-L586) compute_on_chain_aggregate folds 64 committees one by one, so the copy is quadratic
- [`beacon_node/operation_pool/src/lib.rs:381-387`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L381-L387) runs for both epochs on every block production under the write lock

**Second check.** Read the ethereum_ssz git dependency: union/intersection/is_subset are byte-wise on flat bytes, so the Teku costs (SSZ hashing, slow or, offset remapping) do not exist in Lighthouse; only the per-bit extend remains.

**Skeptic check.** The earlier evidence was right that Lighthouse has none of Teku's tree-hash or offset-remap costs. It was wrong to call bitlist_extend 'well under a millisecond per block': the fold is quadratic, measured at ~1.6 ms per data, and it runs for every data on every block production.

**Verdict history.** partial (checked) → implemented (refuted) → partial (skeptic)

**Sources.** [teku#9293](https://github.com/Consensys-Incorporated/teku/pull/9293), [teku#8346](https://github.com/Consensys-Incorporated/teku/pull/8346)

</details>


<a id="op_pool-020"></a>
<details>
<summary><b>op_pool-020</b> Electra cross-committee merge of aggregates at packing — <i>implemented · medium · S · cpu, bandwidth</i></summary>

**Idea.** Post-Electra, group pooled aggregates by AttestationData and merge those with disjoint committee bits into one on-chain multi-committee attestation when packing, keeping all aggregates for that data rather than only the best one. Fewer, larger attestations fit more votes into the block.

**Impact.** Multi-committee on-chain aggregates are built at packing time; all other aggregates for the same data remain as max-cover candidates.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/attestation_storage.rs:475`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs#L475) aggregate_across_committees keeps the best single-committee aggregate per committee in a BTreeMap and pushes the inferior ones back into the list
- [`beacon_node/operation_pool/src/attestation_storage.rs:579`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs#L579) compute_on_chain_aggregate merges them via aggregate_with_disjoint_committees (:270) in increasing committee order
- [`beacon_node/operation_pool/src/lib.rs:394-397`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L394-L397) called for prev and curr epoch keys before max cover when electra_enabled

**Skeptic check.** Verified the merge is done at packing in get_attestations and that non-best aggregates are kept, not dropped. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#6732](https://github.com/ChainSafe/lodestar/pull/6732), [lighthouse#5749](https://github.com/sigp/lighthouse/pull/5749), [prysm#14534](https://github.com/OffchainLabs/prysm/pull/14534), [nimbus#6498](https://github.com/status-im/nimbus-eth2/pull/6498)

</details>


<a id="op_pool-021"></a>
<details>
<summary><b>op_pool-021</b> Key packing candidates by data and committee index — <i>implemented · medium · S · bandwidth</i></summary>

**Idea.** Post-Electra, key attestation packing candidates by (AttestationData, committee index), not data alone, because all committees of a slot share the same data. Deduplicating by data alone drops most votes from the block.

**Impact.** Packing candidates are per committee/aggregate under a shared data key, so no committee's votes are dropped by dedup on data.

**Best measured result.** ~95% of a slot's votes left out of the next block (commit:grandine@3d511c2f35f6)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/attestation_storage.rs:66`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs#L66) AttestationDataMap maps data -&gt; Vec&lt;CompactIndexedAttestation&gt;
- [`beacon_node/operation_pool/src/attestation_storage.rs:239`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs#L239) Electra should_aggregate only merges equal committee_bits, so each committee keeps its own entries
- [`beacon_node/operation_pool/src/lib.rs:321`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L321) get_valid_attestations_for_epoch feeds every entry of the Vec to maximum_cover

**Skeptic check.** Confirmed the data key holds a Vec of per-committee aggregates and that max cover iterates all of them; there is no per-data dedup. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

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


<a id="op_pool-023"></a>
<details>
<summary><b>op_pool-023</b> Merge only within committee and skip subset candidates — <i>partial · low · S · cpu, latency</i></summary>

**Idea.** At block production, group attestations by data root and committee, merge only within a committee, and drop candidates that are subsets of existing aggregates. This removes most pairwise comparisons.

**Gap in Lighthouse.** Committee-scoped merging exists (data-keyed map, committee_bits check), but a candidate that is a strict subset of an existing aggregate is pushed as a new entry. AttestationMap::insert would need to drop subsets (and evict existing subsets of a new superset).

**Impact.** Smaller per-data vectors, so fewer AttMaxCover::new reward computations at block production; small gain, mostly under attestation spam.

**Evidence (Lighthouse @ 928b61e719).**

- operation_pool/src/attestation_storage.rs:457 insert only merges disjoint or equal, groups by data
- operation_pool/src/attestation_storage.rs:253 Electra should_aggregate requires equal committee_bits
- operation_pool/src/lib.rs:317 get_valid_attestations_for_epoch builds AttMaxCover for every stored entry

**Sources.** [caplin#14624](https://github.com/erigontech/erigon/pull/14624)

</details>


<a id="op_pool-024"></a>
<details>
<summary><b>op_pool-024</b> Filter packing candidates by dependent root first — <i>implemented · low · S · cpu</i></summary>

**Idea.** When packing block attestations, filter candidates by target dependent root before other checks, so only attestations valid on the proposal's fork are considered.

**Impact.** Fork/dependent-root compatibility filter runs before reward scoring, cached per block root and epoch.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:2739`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2739) filter_op_pool_attestation cached per (beacon_block_root,target_epoch)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2765`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2765) shuffling_is_compatible compares dependent (RANDAO) block ancestry
- [`beacon_node/operation_pool/src/lib.rs:327`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L327) get_attestations(checkpoint_key) pre-filters by source/target epoch then slot window, validity_filter before AttMaxCover::new

**Skeptic check.** shuffling_is_compatible is effectively a dependent-root check and runs before the costly AttMaxCover::new; earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [grandine@63e7d20b3](https://github.com/grandinetech/grandine/commit/63e7d20b3e4f)

</details>


<a id="op_pool-025"></a>
<details>
<summary><b>op_pool-025</b> Check attestation targets without slot processing — <i>implemented · medium · S · cpu, latency</i></summary>

**Idea.** When validating or converting pooled attestations for packing or aggregation, get the target dependent root from block-root history or the nearest cached state and reuse cached target checkpoint states, instead of running slot processing to build a checkpoint state. This removes state-cache lock contention and CPU in block production.

**Impact.** Block-production filtering of pooled attestations is a fork-choice lookup; pool aggregation needs no checkpoint state.

**Best measured result.** greatly reduces state cache locking (pr:grandine#891)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:2739`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2739) filter_op_pool_attestation memoized by (beacon_block_root, target_epoch)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2783`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2783) shuffling_is_compatible_result compares AttestationShufflingId from the head state with the fork-choice ProtoBlock shuffling ids, with no state load or slot processing
- [`beacon_node/operation_pool/src/attestation_storage.rs:69`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs#L69) SplitAttestation::new stores attesting_indices computed at verification, so pool aggregation needs no target state

**Skeptic check.** Verified that the inclusion filter uses the dependent-root (shuffling decision block) from fork choice instead of building target states, which is the grandine#891 mechanism. The pool never converts attestations against a state, so the grandine#510 path does not exist in Lighthouse.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [grandine#891](https://github.com/grandinetech/grandine/pull/891), [grandine@9dc532a70](https://github.com/grandinetech/grandine/commit/9dc532a7031c), [grandine@35c820ecd](https://github.com/grandinetech/grandine/commit/35c820ecda72), [grandine#510](https://github.com/grandinetech/grandine/pull/510)

</details>


<a id="op_pool-026"></a>
<details>
<summary><b>op_pool-026</b> Validate exits without cloning or advancing state — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Validate gossip and pool voluntary exits against the head state directly, without cloning it, skipping slots, or building a shuffling/epoch cache, since exit validity does not depend on slot processing.

**Best measured result.** None (pr:lighthouse#4183)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:2841-2872`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2841-L2872) verify_voluntary_exit_for_gossip borrows head_snapshot.beacon_state and uses wall-clock epoch
- [`beacon_node/beacon_chain/src/observed_operations.rs:161`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/observed_operations.rs#L161) verify_and_observe_at passes head_state by reference to validate_at
- [`consensus/state_processing/src/verify_operation.rs:310`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/verify_operation.rs#L310) SignedVoluntaryExit::validate_at calls verify_exit(state, Some(epoch)) with no clone or slot advance
- [`beacon_node/operation_pool/src/lib.rs:629`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L629) pool re-check uses verify_exit with VerifySignatures::False

**Skeptic check.** Followed the gossip/API exit path down to verify_exit: head state by reference, epoch override, no clone, skip or committee cache. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#4181](https://github.com/sigp/lighthouse/pull/4181), [nimbus#2188](https://github.com/status-im/nimbus-eth2/pull/2188), [lighthouse#4183](https://github.com/sigp/lighthouse/pull/4183)

</details>


<a id="op_pool-027"></a>
<details>
<summary><b>op_pool-027</b> Drop duplicate exits before storing — <i>implemented · low · S · cpu, disk</i></summary>

**Idea.** Check whether a voluntary exit for the validator was already seen and drop duplicates before storing or forwarding, so the pool does no repeated work.

**Impact.** Duplicate exits dropped before signature verification, storage and forwarding.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/observed_operations.rs:108`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/observed_operations.rs#L108) all-observed validator indices short-circuit to AlreadyKnown before validate()
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2841`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2841) verify_voluntary_exit_for_gossip cheap epoch/already-exited checks then observed_voluntary_exits
- [`beacon_node/operation_pool/src/lib.rs:608`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L608) insert_voluntary_exit keyed by validator_index

**Skeptic check.** Verified the dedup check precedes validation in verify_and_observe_parametric; earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#1437](https://github.com/OffchainLabs/prysm/pull/1437)

</details>


<a id="op_pool-028"></a>
<details>
<summary><b>op_pool-028</b> Stop exit selection at the per-block maximum — <i>implemented · low · S · cpu</i></summary>

**Idea.** When selecting voluntary exits for a block, stop iterating the pool once the per-block maximum (16) is reached instead of processing every pending exit and truncating.

**Impact.** Iteration and verify_exit stop once the per-block max is reached.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/lib.rs:833`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L833) filter_limit_operations: lazy filter().take(limit)
- [`beacon_node/operation_pool/src/lib.rs:615`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L615) get_voluntary_exits passes MaxVoluntaryExits, verify_exit inside the lazy filter

**Skeptic check.** Iterator is lazy so the expensive filter stops at the limit; earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#7772](https://github.com/OffchainLabs/prysm/pull/7772)

</details>


<a id="op_pool-029"></a>
<details>
<summary><b>op_pool-029</b> Linked list with map index for operation pools — <i>n/a · low · memory</i></summary>

**Idea.** Store exits and BLS-to-execution changes in a doubly linked list with a map index by validator, giving O(1) removal and compact memory.

**Impact.** Hash map by validator already gives O(1) lookup and removal; a linked list adds nothing for pools of a few entries.

**Evidence (Lighthouse @ 928b61e719).**

- operation_pool/src/lib.rs:62 voluntary_exits is HashMap&lt;u64,..&gt;; removal via retain at :858 prune_validator_hash_map

**Sources.** [prysm#11898](https://github.com/OffchainLabs/prysm/pull/11898), [prysm#11631](https://github.com/OffchainLabs/prysm/pull/11631)

</details>


<a id="op_pool-030"></a>
<details>
<summary><b>op_pool-030</b> Key slashings and exits by validator, prune with retain — <i>implemented · low · S · cpu</i></summary>

**Idea.** Key slashings and exits in the op pool by validator index in a hash map and prune them with one retain pass against the finalized registry instead of collecting keys and then removing.

**Impact.** Already in this shape (this is the Lighthouse commit itself).

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/lib.rs:858`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L858) prune_validator_hash_map uses HashMap::retain against the finalized state
- [`beacon_node/operation_pool/src/lib.rs:58`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L58) pool maps for slashings/exits keyed by validator index

**Skeptic check.** Verified retain-based pruning keyed by validator index; attester slashings are a HashSet pruned with retain too. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse@03c01c8a8](https://github.com/sigp/lighthouse/commit/03c01c8a8db8)

</details>


<a id="op_pool-031"></a>
<details>
<summary><b>op_pool-031</b> Prune op pools in a background worker off the lock — <i>not · low · S · latency, cpu</i></summary>

**Idea.** Prune operations made terminal by finality from a bounded background worker with coalesced finality updates, outside the fork-choice lock, and skip loading the finalized state when pools are empty. Block import latency is not affected by pruning.

**Gap in Lighthouse.** Pruning and the finalized-state load happen synchronously inside after_finalization under the fork-choice write lock. Move prune_all to a spawned blocking task with coalesced finality updates, and skip get_hot_state when all pools are empty (needs num_* checks in prune_all caller).

**Impact.** Shorter fork-choice write-lock hold once per epoch on finality; likely milliseconds at most since the state is usually cached.

**Evidence (Lighthouse @ 928b61e719).**

- beacon_chain/src/canonical_head.rs:1710 prune_all called inline in after_finalization
- beacon_chain/src/canonical_head.rs:1278 comment: after_finalization takes the fork_choice write lock
- beacon_chain/src/canonical_head.rs:1697 get_hot_state of finalized state loaded before pruning even if pools are empty
- operation_pool/src/lib.rs:739 prune_all runs all pool prunes synchronously

**Sources.** [caplin#22884](https://github.com/erigontech/erigon/pull/22884)

</details>


<a id="op_pool-032"></a>
<details>
<summary><b>op_pool-032</b> Batch database deletes when pruning pooled aggregates — <i>n/a · low · cpu, disk</i></summary>

**Idea.** Key pooled aggregates by attestation root and delete included or finalized ones with one database batch delete instead of per-item reads and deletes.

**Impact.** Pooled aggregates live in memory and persist as one blob at shutdown; there are no per-item DB reads or deletes to batch.

**Evidence (Lighthouse @ 928b61e719).**

- operation_pool/src/persistence.rs:31 PersistedOperationPool serialised as one blob
- beacon_chain/src/canonical_head.rs:1566 pruning is in-memory

**Sources.** [lodestar#1647](https://github.com/ChainSafe/lodestar/pull/1647), [lodestar@ae22d026b](https://github.com/ChainSafe/lodestar/commit/ae22d026bf0c)

</details>


<a id="op_pool-033"></a>
<details>
<summary><b>op_pool-033</b> Skip canonical-chain check when pruning included attestations — <i>n/a · low · S · cpu</i></summary>

**Idea.** When pruning included attestations from the pool, do not do a per-attestation canonical-chain lookup, which is redundant work.

**Impact.** Nothing to save: pruning is a retain on checkpoint keys.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/attestation_storage.rs:632`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs#L632) prune by target epoch only, no canonical lookup

**Sources.** [prysm#11935](https://github.com/OffchainLabs/prysm/pull/11935)

</details>


<a id="op_pool-034"></a>
<details>
<summary><b>op_pool-034</b> Keep pools in memory, persist only on shutdown — <i>implemented · low · S · disk, latency</i></summary>

**Idea.** Keep pending and pooled operations in in-memory maps and do not write or prune them in the database on every block; persist only on shutdown (or after they pass processing). This removes per-block disk writes and reads.

**Impact.** Pool lives in memory and is written only at shutdown; no per-block DB writes.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:723`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L723) persist_op_pool
- [`beacon_node/beacon_chain/src/beacon_chain.rs:8464`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L8464) only caller, in Drop

**Skeptic check.** grep shows persist_op_pool has a single call site in Drop; earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#3223](https://github.com/ChainSafe/lodestar/pull/3223), [prysm#3542](https://github.com/OffchainLabs/prysm/pull/3542), [lodestar#3134](https://github.com/ChainSafe/lodestar/pull/3134)

</details>


<a id="op_pool-035"></a>
<details>
<summary><b>op_pool-035</b> Delete attestations that fail verification — <i>n/a · low · S · cpu, disk</i></summary>

**Idea.** Remove pooled attestations that fail verification so they are not re-verified on every block proposal.

**Impact.** Attestations are verified before pool entry; packing filter is a cached shuffling check.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:2699`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2699) pool takes only VerifiedAttestation
- [`beacon_node/operation_pool/src/lib.rs:333`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L333) validity_filter at packing

**Sources.** [prysm#2528](https://github.com/OffchainLabs/prysm/pull/2528), [teku#6122](https://github.com/Consensys-Incorporated/teku/pull/6122)

</details>


<a id="op_pool-036"></a>
<details>
<summary><b>op_pool-036</b> Reject too-old attestations at pool entry — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Check the attestation slot at pool insertion and reject attestations older than the inclusion window, before state or committee lookups, so they are never stored or processed.

**Impact.** Too-old attestations rejected before committee/state lookups and never reach the pool.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/attestation_verification.rs:540`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L540) verify_propagation_slot_range first in aggregate gossip verify
- [`beacon_node/beacon_chain/src/attestation_verification.rs:920`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L920) same for unaggregated
- [`beacon_node/beacon_chain/src/attestation_verification.rs:1298`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1298) verify_propagation_slot_range
- [`beacon_node/operation_pool/src/attestation_storage.rs:632`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs#L632) prune drops entries older than previous epoch

**Skeptic check.** All pool entry paths (gossip and HTTP API, which reuse gossip verification) check slot range before any state work; earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [grandine@79277a2a6](https://github.com/grandinetech/grandine/commit/79277a2a69d8), [grandine#148](https://github.com/grandinetech/grandine/pull/148)

</details>


<a id="op_pool-037"></a>
<details>
<summary><b>op_pool-037</b> Allocation-free committee index computation — <i>implemented · low · S · memory, cpu</i></summary>

**Idea.** Compute the attestation committee index without building an intermediate collection, so listing pool attestations does not allocate per item.

**Impact.** None remaining; committee_index() uses iter().find() with no Vec.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/attestation_storage.rs:316`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs#L316)
- [`beacon_node/operation_pool/src/attestation_storage.rs:518`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs#L518)
- [`beacon_node/operation_pool/src/attestation_storage.rs:551`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs#L551)

**Skeptic check.** committee_index() finds the first set committee bit without collecting, and the pool iteration paths (lines 518, 551) use it. The earlier evidence is correct; get_committee_indices() still collects but is not used on the listing path.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#7298](https://github.com/sigp/lighthouse/pull/7298)

</details>


<a id="op_pool-038"></a>
<details>
<summary><b>op_pool-038</b> Pass sync message pool by reference to verifier — <i>n/a · low · S · cpu, memory</i></summary>

**Idea.** Pass the sync committee message pool to the async batch signature verifier by reference instead of copying it.

**Impact.** Nim async copy semantics; Rust passes by reference.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/sync_committee_verification.rs:616`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/sync_committee_verification.rs#L616) slices passed by reference

**Sources.** [nimbus#3185](https://github.com/status-im/nimbus-eth2/pull/3185)

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


<a id="op_pool-040"></a>
<details>
<summary><b>op_pool-040</b> Rate-limit broadcast of queued operation bursts — <i>n/a · low · S · bandwidth, latency, cpu</i></summary>

**Idea.** Broadcast a large backlog of queued operations (for example BLS-to-execution changes at the fork) in small shuffled batches over time (128 per 500 ms), and rate limit re-broadcast of API-submitted ones, so the send channel, peers and network are not flooded.

**Impact.** Capella fork-boundary burst is past and the broadcast code is gone; one-off.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/lib.rs:696`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L696) received_pre_capella getter only used in tests
- [`beacon_node/http_api/src/beacon/pool.rs:86`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/beacon/pool.rs#L86) API path

**Sources.** [lighthouse#3919](https://github.com/sigp/lighthouse/pull/3919), [prysm#11923](https://github.com/OffchainLabs/prysm/pull/11923)

</details>


<a id="op_pool-041"></a>
<details>
<summary><b>op_pool-041</b> Cache deserialized signatures of pooled attestations — <i>implemented · medium · S · cpu, latency</i></summary>

**Idea.** Store pooled attestation signatures already decompressed and subgroup-checked, so block production does not re-deserialize them each time. At 220k validators this made block production about 5x faster.

**Impact.** Block production never decompresses pooled signatures; only final block serialization compresses.

**Best measured result.** Block production ~5x faster, sim 41m -&gt; 18m at 220k validators (pr:nimbus#2419)

**Evidence (Lighthouse @ 928b61e719).**

- [`crypto/bls/src/generic_aggregate_signature.rs:60-62`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/generic_aggregate_signature.rs#L60-L62) GenericAggregateSignature holds the decompressed point Option&lt;AggSig&gt;, decompressed once at deserialize (:166)
- [`beacon_node/operation_pool/src/attestation_storage.rs:40`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs#L40) CompactIndexedAttestation keeps signature: AggregateSignature
- [`beacon_node/operation_pool/src/attestation_storage.rs:157`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs#L157) clone_as_attestation clones the point; aggregation uses add_assign_aggregate (:228, :262)

**Skeptic check.** Confirmed that the bls wrapper stores the decompressed point and that the pool keeps that type through aggregation and packing. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#2419](https://github.com/status-im/nimbus-eth2/pull/2419), [caplin#24813](https://github.com/erigontech/erigon/pull/24813)

</details>


<a id="op_pool-042"></a>
<details>
<summary><b>op_pool-042</b> Reuse gossip-validation results when inserting contributions — <i>not · low · S · cpu</i></summary>

**Idea.** Reuse the participant count computed in sync contribution gossip validation when inserting into the pool, and defer signature deserialization until aggregation is needed, so discarded contributions cost nothing extra.

**Gap in Lighthouse.** Reuse participant count from VerifiedSyncContribution in insert_sync_contribution and defer signature use.

**Impact.** Saves a popcount and a clone per contribution; negligible.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/sync_committee_verification.rs:287-420`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/sync_committee_verification.rs#L287-L420) participant_pubkeys built then dropped
- [`beacon_node/operation_pool/src/lib.rs:117`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L117) insert recomputes num_set_bits

**Sources.** [lodestar#3726](https://github.com/ChainSafe/lodestar/pull/3726)

</details>


<a id="op_pool-043"></a>
<details>
<summary><b>op_pool-043</b> Cached base rewards for attestation reward scoring — <i>implemented · low · S · cpu</i></summary>

**Idea.** Use the epoch cache's base rewards when computing attestation rewards for block packing instead of recomputing them per attestation.

**Impact.** None post-Altair; base reward is an epoch-cache lookup per validator.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/attestation.rs:112`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation.rs#L112)
- [`consensus/types/src/state/beacon_state.rs:3136`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L3136)

**Skeptic check.** new_for_altair_or_later calls state.get_base_reward, which reads epoch_cache(). Only the phase0 path recomputes, and that path does not run on mainnet. The earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#5223](https://github.com/sigp/lighthouse/pull/5223)

</details>


<a id="op_pool-044"></a>
<details>
<summary><b>op_pool-044</b> Expire stale proposer preparation and registrations — <i>implemented · low · S · memory</i></summary>

**Idea.** Expire prepared proposer data and validator registrations that are no longer refreshed with a periodic cleanup, so these caches do not grow without limit.

**Impact.** Caches bounded by the periodic routine.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/execution_layer/src/lib.rs:741`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/lib.rs#L741)
- [`beacon_node/execution_layer/src/lib.rs:851`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/lib.rs#L851)
- [`beacon_node/client/src/builder.rs:811`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/client/src/builder.rs#L811)
- [`beacon_node/http_api/src/validator/mod.rs:813`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validator/mod.rs#L813)

**Skeptic check.** spawn_clean_proposer_caches_routine runs clean_proposer_caches, which keeps preparation entries updated in the last 2 epochs and proposers from slots after that point. Validator registrations go straight to post_builder_validators and the BN does not cache them. The earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#5747](https://github.com/Consensys-Incorporated/teku/pull/5747)

</details>


<a id="op_pool-045"></a>
<details>
<summary><b>op_pool-045</b> Pool indexed by validator participation — <i>implemented · medium · S · cpu, latency</i></summary>

**Idea.** Use an attestation pool indexed by validator participation as the default implementation, for faster aggregation and block packing.

**Impact.** Lighthouse has one bitfield pool per data plus a per-validator participation cache for packing; there is no legacy pool to replace.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/attestation_storage.rs:32`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs#L32) CompactIndexedAttestation keeps aggregation_bits plus sorted attesting_indices
- [`beacon_node/operation_pool/src/reward_cache.rs:14-24`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/reward_cache.rs#L14-L24) RewardCache keeps per-validator participation BitVecs for prev and curr epoch, refreshed per block
- [`beacon_node/operation_pool/src/attestation.rs:75`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation.rs#L75) AttMaxCover::new_for_altair_or_later scores only validators not already participating

**Skeptic check.** teku#9721 only flips a default to PoolV2. Lighthouse's pool already has PoolV2's main features: validator-index tracking and skipping validators already included on chain. It is not structured the same way, so confidence is low.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#9721](https://github.com/Consensys-Incorporated/teku/pull/9721)

</details>


<a id="op_pool-046"></a>
<details>
<summary><b>op_pool-046</b> Keep best sync contribution per subnet, aggregate late — <i>implemented · low · S · bandwidth</i></summary>

**Idea.** Store the best (most participants) sync committee contribution per subnet and aggregate them only at block production, instead of pre-aggregating the first one seen. Sync aggregate participation rises.

**Best measured result.** participation 87% and 82% in test blocks vs about 50-60% before (pr:lodestar#2898)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/lib.rs:117-155`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L117-L155) insert_sync_contribution replaces the per-subcommittee contribution only if the new one has more set bits
- [`beacon_node/operation_pool/src/lib.rs:163-179`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L163-L179) get_sync_aggregate builds SyncAggregate::from_contributions only at block production

**Skeptic check.** Verified that the pool keeps the best contribution per subcommittee and aggregates only at block production, which matches lodestar#2898. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#2898](https://github.com/ChainSafe/lodestar/pull/2898)

</details>


<a id="op_pool-047"></a>
<details>
<summary><b>op_pool-047</b> Fill aggregate gaps from bounded single-attestation pool — <i>implemented · medium · S · memory</i></summary>

**Idea.** Keep a size-bounded pool of unaggregated single attestations and use them to add committee members missing from aggregates when packing blocks, so blocks carry more votes with bounded memory.

**Impact.** Single attestations fill aggregate gaps at block production; memory is bounded.

**Best measured result.** block production performance even better; memory bounded to 50MB (pr:lodestar#8076)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:5940-5960`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5940-L5960) produce_partial_beacon_block imports every naive_aggregation_pool entry into op_pool before pack_attestations
- [`beacon_node/operation_pool/src/attestation_storage.rs:452`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs#L452) AttestationMap::insert greedily aggregates them into existing aggregates with disjoint bits (same committee)
- [`beacon_node/beacon_chain/src/naive_aggregation_pool.rs:143`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/naive_aggregation_pool.rs#L143) SLOTS_RETAINED=3, :148 MAX_ATTESTATIONS_PER_SLOT=16384 bound memory; keyed per (data, committee_index) at :20

**Skeptic check.** Confirmed that the naive pool (per data+committee, bounded) is merged into the op pool on every local block production. Its retention is 3 slots, while lodestar#8076 (closed, unmerged) kept up to 63 slots. So singles older than 3 slots are lost if the node does not propose in that window. This is a minor tuning difference, not a missing mechanism.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#8076](https://github.com/ChainSafe/lodestar/pull/8076)

</details>


<a id="op_pool-048"></a>
<details>
<summary><b>op_pool-048</b> Store one proof per data root, not per validator — <i>n/a · low · S · memory, disk, cpu</i></summary>

**Idea.** Key aggregated proofs and gossip signatures by attestation data root and store each proof once with its participation bits, instead of one copy per validator, keeping transient gossip signatures in memory. Memory and disk use fall with the number of validators.

**Impact.** Lean consensus gossip-signature/proof design; Lighthouse already stores one aggregate per data root and has no per-validator proofs.

**Best measured result.** One ~3KB proof was cloned per validator (9x for 9 validators); tables 8 to 6 (pr:ethlambda#253)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/attestation_storage.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs): attestations stored per AttestationData root with aggregation bits

**Sources.** [ethlambda#253](https://github.com/lambdaclass/ethlambda/pull/253)

</details>


<a id="op_pool-049"></a>
<details>
<summary><b>op_pool-049</b> Keep seen-attestation cache for two epochs — <i>implemented · low · S · bandwidth, cpu</i></summary>

**Idea.** Retain the seen-attestation cache for two epochs instead of 32 slots, so attestations still valid on gossip are recognised as already seen and are not re-processed or re-sent.

**Impact.** Seen caches already cover the full gossip validity window.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/observed_aggregates.rs:57`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/observed_aggregates.rs#L57)
- [`beacon_node/beacon_chain/src/observed_aggregates.rs:419`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/observed_aggregates.rs#L419)
- [`beacon_node/beacon_chain/src/observed_attesters.rs:419`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/observed_attesters.rs#L419)

**Skeptic check.** ObservedAggregateAttestations keeps 2*slots_per_epoch+2 slots. Unaggregated attesters are tracked per epoch in ObservedAttesters. This matches the Prysm fix (seen-cache expiry aligned to current+previous epoch), so the earlier verdict holds.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#14156](https://github.com/OffchainLabs/prysm/pull/14156)

</details>


<a id="op_pool-050"></a>
<details>
<summary><b>op_pool-050</b> Max-cover aggregation of pooled attestations — <i>partial · low · M · cpu, bandwidth</i></summary>

**Idea.** Aggregate pooled attestations with the same data using a greedy maximum-coverage algorithm over aggregation bits instead of naive pairwise merging. This yields fewer aggregates that cover more validators, so the pool and blocks hold fewer attestations.

**Gap in Lighthouse.** Op pool only merges attestations with disjoint bits; overlapping aggregates stay separate and are resolved by max-cover at packing time. Pre-aggregating overlapping ones would need a max-cover pass in AttestationMap insert/get_attestations.

**Impact.** Marginally fewer pooled entries and packing work; blocks are already packed by max-cover so block quality is unaffected.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/attestation_storage.rs:199-260`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs#L199-L260) should_aggregate only merges disjoint aggregation bits
- [`beacon_node/operation_pool/src/lib.rs:384`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L384) aggregate_across_committees
- [`beacon_node/operation_pool/src/max_cover.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/max_cover.rs) max-cover used at block packing

**Sources.** [prysm#6343](https://github.com/OffchainLabs/prysm/pull/6343), [prysm#6960](https://github.com/OffchainLabs/prysm/pull/6960)

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

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [prysm#12553](https://github.com/OffchainLabs/prysm/pull/12553), [prysm#13407](https://github.com/OffchainLabs/prysm/pull/13407)

</details>


<a id="op_pool-054"></a>
<details>
<summary><b>op_pool-054</b> Shorter read-lock holds in naive aggregation pool — <i>partial · low · S · latency</i></summary>

**Idea.** Restructure the naive aggregation pool so read locks are held only for the minimal section, reducing contention with gossip writers.

**Gap in Lighthouse.** In block production, the 'import_naive_aggregation_pool' loop (beacon_chain.rs:5947) holds naive_aggregation_pool.read() for the whole iteration. Under that guard it runs get_attesting_indices_from_state, clones each attestation and calls op_pool.insert_attestation, which takes the op_pool write lock. Gossip add_to_naive_aggregation_pool writers wait for the full loop. Fix: clone the values into a Vec and drop the guard before the per-item work.

**Impact.** Small: hundreds of aggregates, once per proposal. Removes a few ms of writer stall on gossip during block production.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:1878`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1878)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2604`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2604)
- [`beacon_node/beacon_chain/src/naive_aggregation_pool.rs:557`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/naive_aggregation_pool.rs#L557)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5947`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5947)

**Skeptic check.** The gossip get/insert paths and prune do hold locks only briefly, as the earlier evidence says. The block-production path that iterates the pool is not minimal. The PR diff is not in the corpus, so I could not check whether #1151 had this path in scope.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [lighthouse#1151](https://github.com/sigp/lighthouse/pull/1151)

</details>


<a id="op_pool-055"></a>
<details>
<summary><b>op_pool-055</b> Aggregate sync messages only for receiving subnet — <i>not · low · S · cpu</i></summary>

**Idea.** Add a sync committee message to the contribution of the subnet it arrived on only, not to every subcommittee the validator belongs to, to avoid duplicate aggregation work when the same message arrives on several subnets.

**Gap in Lighthouse.** add_to_naive_sync_aggregation_pool iterates all subnet_positions rather than only the subnet of arrival; filter to the arrival subnet. Duplicate inserts are already cheap SignatureAlreadyKnown or distinct bits.

**Impact.** Negligible: only validators in multiple subcommittees cause extra inserts, and each is a distinct bit so work is not wasted duplicate.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:2650-2670`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2650-L2670) inserts message at every position in every subnet the validator belongs to
- [`beacon_node/beacon_chain/src/naive_aggregation_pool.rs:355`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/naive_aggregation_pool.rs#L355) sync insert dedups by committee bit

**Sources.** [teku#5843](https://github.com/Consensys-Incorporated/teku/pull/5843)

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

**Verdict history.** not (checked) → partial (refuted)

**Sources.** [prysm#4493](https://github.com/OffchainLabs/prysm/pull/4493), [prysm#6912](https://github.com/OffchainLabs/prysm/pull/6912), [caplin#12019](https://github.com/erigontech/erigon/pull/12019), [lodestar#2883](https://github.com/ChainSafe/lodestar/pull/2883), [ethlambda#313](https://github.com/lambdaclass/ethlambda/pull/313)

</details>


<a id="op_pool-057"></a>
<details>
<summary><b>op_pool-057</b> Skip subset sync contributions, key by slot — <i>implemented · low · S · memory, cpu</i></summary>

**Idea.** In the sync committee contribution pool, ignore contributions whose bits are a subset of an already known contribution and key entries by slot so old ones can be pruned cheaply.

**Impact.** None meaningful.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/observed_aggregates.rs:407`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/observed_aggregates.rs#L407)
- [`beacon_node/operation_pool/src/lib.rs:117`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L117)
- [`beacon_node/operation_pool/src/lib.rs:189`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L189)

**Skeptic check.** Gossip rejects subset contributions with is_known_subset. The pool key is (slot, block_root), and an insert replaces an entry only when the new one has more bits. Pruning is a retain over a small HashMap, not a slot-ordered map, but the map holds about 2 slots of entries, so the cost is negligible. Upheld.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [grandine@20784a99b](https://github.com/grandinetech/grandine/commit/20784a99b731)

</details>


<a id="op_pool-058"></a>
<details>
<summary><b>op_pool-058</b> Store attesting indices and reward cache for packing — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Store attesting indices with pooled attestations and keep a reward cache of per-validator participation bitfields, so block packing scores attestations without committee lookups and skips re-verifying attestations that are valid by construction.

**Impact.** Already in place (Lighthouse's own PR #3312).

**Best measured result.** None (pr:lighthouse#3312)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/attestation_storage.rs:70`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs#L70)
- [`beacon_node/operation_pool/src/lib.rs:298`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L298)
- [`beacon_node/operation_pool/src/lib.rs:370`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L370)
- [`beacon_node/operation_pool/src/attestation.rs:98-124`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation.rs#L98-L124)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5992`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5992) (signature re-check only under paranoid_block_proposal)

**Skeptic check.** SplitAttestation stores attesting_indices, RewardCache.update runs once per get_attestations, and AttMaxCover scores from stored indices with has_attested_in_epoch; signature re-verification at packing is off unless paranoid mode. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#3312](https://github.com/sigp/lighthouse/pull/3312)

</details>


<a id="op_pool-059"></a>
<details>
<summary><b>op_pool-059</b> Skip BLS re-verification of pooled operations at packing — <i>implemented · low · S · cpu</i></summary>

**Idea.** When packing pool operations such as BLS-to-execution changes into a block, skip signature verification because they were verified on insertion; store the signing epoch/fork and prune on fork change so this stays safe.

**Impact.** None; packing does no BLS verification of pooled ops.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/verify_operation.rs:152`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/verify_operation.rs#L152)
- [`consensus/state_processing/src/verify_operation.rs:176`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/verify_operation.rs#L176)
- [`beacon_node/operation_pool/src/lib.rs:674`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L674)
- [`beacon_node/operation_pool/src/lib.rs:614`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L614)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:6530`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L6530)

**Skeptic check.** At insert, SigVerifiedOp records the fork versions it was verified against. Packing calls only signature_is_still_valid (a fork-version compare). Exits use verify_exit with VerifySignatures::False. The produced block is processed with a RANDAO-only or no-verification strategy. The earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#12021](https://github.com/OffchainLabs/prysm/pull/12021), [lodestar#4923](https://github.com/ChainSafe/lodestar/pull/4923), [lodestar#10217](https://github.com/ChainSafe/lodestar/pull/10217)

</details>


<a id="op_pool-060"></a>
<details>
<summary><b>op_pool-060</b> Skip signature group checks when aggregating into pool — <i>implemented · low · S · cpu</i></summary>

**Idea.** When aggregating already gossip-verified attestation signatures into the op pool, skip the BLS signature group/subgroup validity check, which is redundant after gossip validation.

**Impact.** None left to gain.

**Best measured result.** None (pr:lodestar#4838)

**Evidence (Lighthouse @ 928b61e719).**

- [`crypto/bls/src/impls/blst.rs:237-244`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L237-L244)
- [`crypto/bls/src/generic_aggregate_signature.rs:141`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/generic_aggregate_signature.rs#L141)
- [`beacon_node/operation_pool/src/attestation_storage.rs:252`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs#L252)
- [`beacon_node/beacon_chain/src/naive_aggregation_pool.rs:281`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/naive_aggregation_pool.rs#L281)
- ~/.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/blst-0.3.17/src/lib.rs:1670-1696

**Skeptic check.** add_assign calls add_signature(sig,false) and add_assign_aggregate is a raw blst add_or_dbl with no group check; both the naive aggregation pool and the op pool merge use these. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#4838](https://github.com/ChainSafe/lodestar/pull/4838)

</details>


<a id="op_pool-061"></a>
<details>
<summary><b>op_pool-061</b> Priority queue with evict-on-access for sync pool — <i>n/a · low · cpu, memory</i></summary>

**Idea.** Back the sync committee message pool with a slot-ordered priority queue that trims old entries on write and read, instead of a map plus a background time-based pruning service.

**Impact.** Lighthouse already uses a slot-keyed map pruned on insert (naive pool) and prunes the op-pool contributions on head update; a priority queue gains nothing measurable.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/lib.rs:191`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L191) prune_sync_contributions
- [`beacon_node/beacon_chain/src/naive_aggregation_pool.rs:533`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/naive_aggregation_pool.rs#L533) prune(slot) on every insert, slot-keyed map

**Sources.** [prysm#9018](https://github.com/OffchainLabs/prysm/pull/9018), [prysm#9203](https://github.com/OffchainLabs/prysm/pull/9203)

</details>


<a id="op_pool-062"></a>
<details>
<summary><b>op_pool-062</b> Store pristine attestations to avoid conversion — <i>not · low · M · cpu</i></summary>

**Idea.** Keep attestations in the aggregate pool in their original wire form so packing into blocks or serving over the API needs no conversion step.

**Gap in Lighthouse.** Pool stores a compact form (data split by checkpoint) so every API read or block pack re-assembles Attestation via clone_as_attestation. Storing pristine form would cost memory and break max-cover aggregation indexing.

**Impact.** Saves one small clone per attestation at packing/API; packing cost is dominated by max-cover, so gain is marginal and the compact layout is deliberate.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/attestation_storage.rs:156`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs#L156) clone_as_attestation rebuilds Attestation from compact form
- [`beacon_node/operation_pool/src/attestation_storage.rs:53`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs#L53) CompactAttestationRef

**Sources.** [grandine@63806e0e2](https://github.com/grandinetech/grandine/commit/63806e0e2c4d)

</details>


<a id="op_pool-063"></a>
<details>
<summary><b>op_pool-063</b> Remove included BLS changes from pool on import — <i>implemented · low · S · memory</i></summary>

**Idea.** After block import, remove the bls_to_execution_changes (and similar non-attestation operations) the block included from the operation pool, so the pool does not hold or re-propose them.

**Impact.** Negligible; a few stale entries live until the next finalization and are never re-proposed.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/bls_to_execution_changes.rs:102`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/bls_to_execution_changes.rs#L102)
- [`beacon_node/operation_pool/src/lib.rs:739`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L739)
- [`beacon_node/beacon_chain/src/canonical_head.rs:1710`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1710)
- [`beacon_node/operation_pool/src/lib.rs:674`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L674)

**Skeptic check.** Pruning runs from prune_all at finalization, not on each import. get_bls_to_execution_changes filters out validators that already have execution credentials, so included changes are never packed again. The effect the idea wants (no re-proposal, bounded pool) is present. Upheld.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#6793](https://github.com/Consensys-Incorporated/teku/pull/6793)

</details>


<a id="op_pool-064"></a>
<details>
<summary><b>op_pool-064</b> Prune operation pool on finalization — <i>implemented · low · S · memory, cpu, disk, latency</i></summary>

**Idea.** On each new finalized checkpoint, drop pool attestations and operations older than the finalized epoch (and aggregated payloads at or below the finalized slot), so the pool, its persisted copy and block-packing scans stay bounded.

**Impact.** Already in place; pruning is even more aggressive than finality (attestations pruned each epoch transition/reorg).

**Best measured result.** None (pr:lighthouse#500)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/canonical_head.rs:1563-1566`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1563-L1566)
- [`beacon_node/beacon_chain/src/canonical_head.rs:1710`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1710)
- [`beacon_node/operation_pool/src/lib.rs:739-754`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L739-L754)
- [`beacon_node/operation_pool/src/attestation_storage.rs:632-635`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs#L632-L635)
- [`beacon_node/operation_pool/src/lib.rs:279`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L279)

**Skeptic check.** prune_all on finalization prunes attestations, sync contributions, payload attestations, slashings, exits and BLS changes; attestations are also pruned on every epoch transition. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse@6150f0ae1](https://github.com/sigp/lighthouse/commit/6150f0ae1a54), [lighthouse#500](https://github.com/sigp/lighthouse/pull/500), [lodestar@ebe02a3af](https://github.com/ChainSafe/lodestar/commit/ebe02a3afb36), [lighthouse@9c2dfba84](https://github.com/sigp/lighthouse/commit/9c2dfba843c2), [ethlambda#389](https://github.com/lambdaclass/ethlambda/pull/389)

</details>


<a id="op_pool-065"></a>
<details>
<summary><b>op_pool-065</b> Prune finalized deposits from pending deposit store — <i>n/a · low · memory</i></summary>

**Idea.** Keep pending deposits with proofs in a store that drops deposits already included in finalized state after each finalization, so memory does not grow with the total deposit count.

**Impact.** Current Lighthouse has no eth1 pending-deposit-with-proof store (post-Electra deposits come via execution requests), so there is nothing to prune.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/lib.rs:56-64`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L56-L64) pool fields have no deposit store
- grep for DepositCache/deposit_cache in beacon_node finds no eth1 deposit store

**Sources.** [teku#1152](https://github.com/Consensys-Incorporated/teku/pull/1152), [prysm#1530](https://github.com/OffchainLabs/prysm/pull/1530)

</details>


<a id="op_pool-066"></a>
<details>
<summary><b>op_pool-066</b> Prune sync committee message pool by slot — <i>partial · low · S · memory</i></summary>

**Idea.** Drop old slots from the sync committee message/contribution pool so it does not grow without bound.

**Gap in Lighthouse.** OperationPool::prune_sync_contributions (and prune_attestations) run only from prune_all inside after_finalization. During non-finality the op pool's sync_contributions map is never pruned and grows with every slot. Call prune_sync_contributions(slot) from BeaconChain::per_slot_task.

**Impact.** Bounded op pool memory during long non-finality; no effect while the chain finalizes normally.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/naive_aggregation_pool.rs:533`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/naive_aggregation_pool.rs#L533) naive (sync) pool prunes on every insert
- [`beacon_node/beacon_chain/src/naive_aggregation_pool.rs:557`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/naive_aggregation_pool.rs#L557) prune with SLOTS_RETAINED
- [`beacon_node/operation_pool/src/lib.rs:191`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L191) prune_sync_contributions by slot
- [`beacon_node/operation_pool/src/lib.rs:739-748`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L739-L748) only caller is prune_all
- [`beacon_node/beacon_chain/src/canonical_head.rs:1281`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1281) prune_all reached only via after_finalization (:1597, call :1710)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:7477`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L7477) per_slot_task prunes naive_aggregation_pool but not op_pool

**Skeptic check.** The naive sync message pool really prunes by slot on insert, but the op pool's contribution pool is pruned by slot only when finality advances. The earlier evidence missed that prune_all is gated on finalization.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [nimbus@7d1efa443](https://github.com/status-im/nimbus-eth2/commit/7d1efa443d60)

</details>


<a id="op_pool-067"></a>
<details>
<summary><b>op_pool-067</b> Prune pending pools every epoch — <i>n/a · low · memory</i></summary>

**Idea.** Run pruning of pending operation pools and blob sidecar trackers every epoch instead of every several epochs, reducing memory held and GC pressure.

**Impact.** Idea targets JVM GC pressure; Lighthouse pools are small, Rust-owned and already pruned on insert or head update.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/lib.rs:739`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L739) prune_all runs on head/finalization updates
- [`beacon_node/beacon_chain/src/naive_aggregation_pool.rs:557`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/naive_aggregation_pool.rs#L557) prune on insert

**Sources.** [teku#7964](https://github.com/Consensys-Incorporated/teku/pull/7964)

</details>


<a id="op_pool-068"></a>
<details>
<summary><b>op_pool-068</b> Prune voluntary exits signed under old forks — <i>partial · low · S · memory, cpu</i></summary>

**Idea.** Drop voluntary exits whose signature domain belongs to an old fork from the op pool and skip them at block production, so invalid exits are not packed and the pool does not grow.

**Gap in Lighthouse.** prune_voluntary_exits does not drop exits whose signature_is_still_valid is false. Such exits stay in the pool (and are persisted) until the validator exits by other means.

**Impact.** Negligible. The packing half (the part that keeps blocks valid) is done; the leak is a few stale exits. EIP-7044 pins exit domains to Capella, so new cases are rare.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/lib.rs:624-633`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L624-L633) get_voluntary_exits filters signature_is_still_valid before packing
- [`beacon_node/operation_pool/src/lib.rs:638-644`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L638-L644) prune_voluntary_exits removes only exits whose validator has exited, no fork check
- [`consensus/state_processing/src/verify_operation.rs:176-186`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/verify_operation.rs#L176-L186) signature_is_still_valid
- [`consensus/state_processing/src/verify_operation.rs:227`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/verify_operation.rs#L227) exit verification epoch = message.epoch

**Skeptic check.** I confirmed the packing filter. The pruning half of the idea is missing, which the earlier gap admitted while still calling it implemented.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [lodestar#4934](https://github.com/ChainSafe/lodestar/pull/4934)

</details>


<a id="op_pool-069"></a>
<details>
<summary><b>op_pool-069</b> Prune BLS change pool using head state — <i>implemented · low · S · memory</i></summary>

**Idea.** Prune the BLS-to-execution-change pool against the head state (keeping recently added entries) instead of the finalized state, so included changes leave the pool sooner.

**Impact.** None. Pruning already uses the head state and keeps changes from the head block for re-orgs.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/bls_to_execution_changes.rs:101-137`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/bls_to_execution_changes.rs#L101-L137) prune() checks head_state withdrawal credentials and keeps changes in head_block
- [`beacon_node/operation_pool/src/lib.rs:727-736`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L727-L736) prune_bls_to_execution_changes(head_block, head_state)
- [`beacon_node/beacon_chain/src/canonical_head.rs:1710`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1710) prune_all passes new_snapshot block/state

**Skeptic check.** Verified: prune uses head state and head block, which is exactly the Lodestar mechanism. It runs on finalization, but the BLS change pool is tiny and post-Capella mostly empty.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#6252](https://github.com/ChainSafe/lodestar/pull/6252)

</details>


<a id="op_pool-070"></a>
<details>
<summary><b>op_pool-070</b> Prune op pool without regenerating finalized state; persist diff — <i>implemented · low · S · disk, memory, cpu</i></summary>

**Idea.** Decide which op pool items are useless without regenerating the finalized state, and persist only the changed entries to the database instead of the whole pool.

**Impact.** None measurable. Pruning reads a cached hot state and the pool is persisted once at shutdown.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/canonical_head.rs:1702-1705`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1702-L1705) finalized state from get_hot_state with cache
- [`beacon_node/beacon_chain/src/beacon_chain.rs:723`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L723) persist_op_pool
- [`beacon_node/beacon_chain/src/beacon_chain.rs:8464`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L8464) only call, in Drop at shutdown

**Skeptic check.** Confirmed that persistence happens only on drop, so a diff persist would save nothing. The finalized state usually comes from the state cache, not a regeneration.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#3224](https://github.com/ChainSafe/lodestar/pull/3224)

</details>


<a id="op_pool-071"></a>
<details>
<summary><b>op_pool-071</b> Rebuild pool hash map after surge drains — <i>partial · low · S · memory</i></summary>

**Idea.** After a surge in a pool (e.g. BLS-to-execution changes) drains below a threshold, rebuild its hash map so the capacity grown during the surge is returned, since maps do not shrink on delete.

**Gap in Lighthouse.** After prune() in BlsToExecutionChanges, call shrink_to_fit (or shrink_to) on by_validator_index and queue when len falls far below capacity.

**Impact.** Returns a few MB at most after the Capella-fork surge; negligible on a running mainnet node today.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/bls_to_execution_changes.rs:28`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/bls_to_execution_changes.rs#L28) by_validator_index HashMap and queue Vec
- [`beacon_node/operation_pool/src/bls_to_execution_changes.rs:111`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/bls_to_execution_changes.rs#L111) prune uses retain and map remove, no shrink_to_fit; grep shrink in operation_pool/src finds nothing

**Sources.** [prysm#11873](https://github.com/OffchainLabs/prysm/pull/11873)

</details>


<a id="op_pool-072"></a>
<details>
<summary><b>op_pool-072</b> Reject slashings covering only already-slashed validators — <i>implemented · low · S · memory, cpu</i></summary>

**Idea.** On gossip, reject attester slashings whose slashable validators are all already slashed before they enter the op pool, so useless slashings use no memory or processing.

**Impact.** Already in place (Lighthouse PR #5385).

**Best measured result.** None (pr:lighthouse#5385)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_block_processing/verify_attester_slashing.rs:19-41`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/verify_attester_slashing.rs#L19-L41)
- [`consensus/state_processing/src/per_block_processing/verify_attester_slashing.rs:46-53`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/verify_attester_slashing.rs#L46-L53)
- [`beacon_node/beacon_chain/src/observed_operations.rs:114`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/observed_operations.rs#L114)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2920-2930`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2920-L2930)

**Skeptic check.** verify_attester_slashing ends in get_slashable_indices with is_slashable_at, which errors if no index is slashable; gossip verify_and_observe runs it before the op reaches import_attester_slashing/op pool. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#5385](https://github.com/sigp/lighthouse/pull/5385)

</details>


<a id="op_pool-073"></a>
<details>
<summary><b>op_pool-073</b> Skip unslashable proposer slashings at block packing — <i>implemented · low · S · cpu, bandwidth</i></summary>

**Idea.** When selecting proposer slashings for a block, skip validators that are no longer slashable (already slashed or past withdrawable epoch), so no block space is wasted and the block stays valid.

**Impact.** Already avoids wasted block space and invalid blocks.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/lib.rs:493-502`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L493-L502) proposer slashings filtered with signature_is_still_valid and is_slashable_at(current_epoch)
- [`beacon_node/operation_pool/src/lib.rs:506-510`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L506-L510) to_be_slashed set excludes them from attester slashings and exits
- [`beacon_node/operation_pool/src/lib.rs:562-570`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L562-L570) prune_proposer_slashings

**Skeptic check.** This is Lighthouse's own commit and it is present on the block production path in get_slashings_and_exits.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse@6e36491a9](https://github.com/sigp/lighthouse/commit/6e36491a9bcf)

</details>


<a id="op_pool-074"></a>
<details>
<summary><b>op_pool-074</b> Single pass when marking BLS changes included — <i>implemented · low · S · cpu</i></summary>

**Idea.** Mark BLS changes as included in one loop instead of two, and prune pools once using the head block instead of for every processed block.

**Impact.** None. Already a single pass, run once per finalization.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/bls_to_execution_changes.rs:107-137`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/bls_to_execution_changes.rs#L107-L137) single retain pass collecting pruned indices
- [`beacon_node/operation_pool/src/lib.rs:739-752`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L739-L752) prune_all once with head block/state
- [`beacon_node/beacon_chain/src/canonical_head.rs:1710`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1710) called once per finalization, not per block

**Skeptic check.** Verified a single retain loop and one prune call per finalization using the head block. There is no per-block pruning.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#12085](https://github.com/OffchainLabs/prysm/pull/12085)

</details>


<a id="op_pool-075"></a>
<details>
<summary><b>op_pool-075</b> Drop redundant dedup pass in max-cover — <i>implemented · low · S · cpu</i></summary>

**Idea.** Remove the explicit deduplication pass before max-cover attestation aggregation, since duplicates score zero after greedy selection and the pool already dedups on insert.

**Impact.** None. There is no redundant dedup pass to remove.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/max_cover.rs:53-80`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/max_cover.rs#L53-L80) maximum_cover builds items, filters zero scores, then greedy selection with no dedup pass

**Skeptic check.** maximum_cover has no explicit dedup step. Zero-score items are dropped at construction and during selection.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#8224](https://github.com/OffchainLabs/prysm/pull/8224)

</details>


<a id="op_pool-076"></a>
<details>
<summary><b>op_pool-076</b> No deep copy when pushing to pool queue — <i>n/a · low · S · cpu</i></summary>

**Idea.** Do not deep-copy objects when pushing them into a pool queue; copy once at the caller only where mutation requires it.

**Impact.** Rust moves values and shares via Arc; there is no deep copy on pool insert (Go-specific problem).

**Best measured result.** None (pr:prysm#9076)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/bls_to_execution_changes.rs:49`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/bls_to_execution_changes.rs#L49) inserts wrap in Arc once, queue and map share the Arc

**Sources.** [prysm#9076](https://github.com/OffchainLabs/prysm/pull/9076)

</details>


<a id="op_pool-077"></a>
<details>
<summary><b>op_pool-077</b> Retain attestations of reorged-out blocks for reuse — <i>implemented · low · S · cpu</i></summary>

**Idea.** When a block that included attestations is reorged out, keep (or restore) its attestations in the pool so the replacement block can include them.

**Impact.** No gain: Lighthouse never removes included attestations, so the Prysm problem does not exist.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/canonical_head.rs:1563-1566`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1563-L1566)
- [`beacon_node/operation_pool/src/attestation_storage.rs:632-635`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs#L632-L635)
- [`beacon_node/operation_pool/src/attestation.rs:98-106`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation.rs#L98-L106)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2699-2716`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2699-L2716)

**Skeptic check.** The op pool has no remove-on-inclusion path (only epoch prune); packing filters by the packing state's participation via RewardCache, so attestations of a reorged-out block stay usable. Attestations seen only inside blocks are not added to the pool, but that is outside this idea. Rated low instead of medium since nothing is missing.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#12107](https://github.com/OffchainLabs/prysm/pull/12107)

</details>


<a id="op_pool-078"></a>
<details>
<summary><b>op_pool-078</b> Separate pool for orphaned-block attestations — <i>n/a · low · S · cpu</i></summary>

**Idea.** Hold attestations from orphaned blocks in a separate pool so fork choice does not reprocess them as fresh attestations.

**Impact.** Lighthouse fork choice does not mix pool attestations with block-sourced ones, so no separate orphan pool is needed.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/lib.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs) attestation pool only holds unaggregated/aggregated gossip attestations; fork choice takes block attestations through its own on_attestation path

**Sources.** [prysm#9529](https://github.com/OffchainLabs/prysm/pull/9529)

</details>


<a id="op_pool-079"></a>
<details>
<summary><b>op_pool-079</b> Persistent iterator in attestation aggregating iterator — <i>n/a · low · cpu</i></summary>

**Idea.** In the iterator that yields aggregated attestations for packing, keep a persistent iterator over remaining attestations shared by hasNext and next, instead of re-streaming and re-filtering on each call.

**Impact.** Java stream hasNext/next re-filtering does not exist in Lighthouse.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/max_cover.rs:50`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/max_cover.rs#L50) greedy loop over a Vec with an available flag, no stream re-filtering

**Sources.** [teku#8307](https://github.com/Consensys-Incorporated/teku/pull/8307)

</details>


<a id="op_pool-080"></a>
<details>
<summary><b>op_pool-080</b> Single-pass op pool metrics — <i>implemented · low · S · cpu</i></summary>

**Idea.** Compute attestation pool metrics in one pass over each slot's attestation groups instead of looping twice.

**Impact.** None. Metrics are computed in one pass.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/attestation_storage.rs:638-649`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs#L638-L649) AttestationMap::stats folds per checkpoint
- [`beacon_node/operation_pool/src/attestation_storage.rs:666-676`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs#L666-L676) AttestationDataMap::stats single loop computing all three stats

**Skeptic check.** Confirmed one loop computes count, data count and max aggregates together.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#7672](https://github.com/ChainSafe/lodestar/pull/7672)

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
<summary><b>op_pool-082</b> One aggregate call over all collected signatures — <i>implemented · low · S · cpu</i></summary>

**Idea.** When aggregating many attestations of a committee, collect all signatures and call BLS aggregate once, merging bits in one pass, instead of pairwise re-aggregation in a reduce.

**Impact.** None left to gain: aggregation is an incremental in-place point add at insert, no per-request reduce.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/naive_aggregation_pool.rs:270-296`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/naive_aggregation_pool.rs#L270-L296)
- [`crypto/bls/src/generic_aggregate_signature.rs:141`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/generic_aggregate_signature.rs#L141)
- [`crypto/bls/src/impls/blst.rs:242`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L242)
- ~/.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/blst-0.3.17/src/lib.rs:1670
- [`beacon_node/operation_pool/src/attestation_storage.rs:252`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs#L252)

**Second check.** The Lodestar fix replaces a reduce that called aggregate pairwise, with its conversion overhead per step, inside the validator getAggregatedAttestation API. Lighthouse keeps an already-aggregated attestation in the naive pool as an unserialized blst point and serves it by lookup. Each merge is one point add, which is exactly what a bulk aggregate does, so the earlier 'not' (which itself rated the impact negligible) is really an equivalent implementation.

**Skeptic check.** Naive aggregation pool folds each gossip vote into a held aggregate at insert, so the aggregate API is a lookup; each fold is one projective add without serialization. Earlier evidence correct; value lowered to low.

**Verdict history.** not (checked) → implemented (refuted) → implemented (skeptic)

**Sources.** [lodestar@269d3f0b2](https://github.com/ChainSafe/lodestar/commit/269d3f0b2ab7)

</details>


<a id="op_pool-083"></a>
<details>
<summary><b>op_pool-083</b> Skip duplicate attestation save, delete and broadcast — <i>implemented · low · S · cpu</i></summary>

**Idea.** Before saving, broadcasting or deleting an attestation in the pool, check whether it is already present/absent and skip the duplicate work.

**Impact.** Exact duplicates are deduplicated on insert. The pool never rebroadcasts or deletes single items, so the duplicate-broadcast and duplicate-delete parts of the idea do not apply. Subset duplicates are still stored, but the gain is tiny.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/attestation_storage.rs:457-480`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs#L457-L480) AttestationMap::insert sets aggregated=true when existing == indexed, so an exact duplicate is not pushed
- [`beacon_node/operation_pool/src/lib.rs:295`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L295) insert_attestation is the only write path; the pool has no per-item delete or broadcast
- [`beacon_node/operation_pool/src/lib.rs:455`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L455) removal only by epoch prune

**Skeptic check.** Read AttestationMap::insert: the equality check skips the push for an exact duplicate. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#2146](https://github.com/OffchainLabs/prysm/pull/2146)

</details>


<a id="op_pool-084"></a>
<details>
<summary><b>op_pool-084</b> Avoid removing included attestations twice — <i>n/a · low · cpu</i></summary>

**Idea.** Remove a block's included attestations from the pool in only one place (on-block processing), not again at block receipt.

**Impact.** Lighthouse never removes included attestations from the pool; it filters them via the reward cache at packing time, so no double removal exists.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/lib.rs:455`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L455) prune_attestations prunes only by epoch
- [`beacon_node/operation_pool/src/attestation.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation.rs) AttMaxCover::new scores against state participation so included attestations score zero

**Sources.** [prysm#11764](https://github.com/OffchainLabs/prysm/pull/11764)

</details>


<a id="op_pool-085"></a>
<details>
<summary><b>op_pool-085</b> Do not store empty pool entries — <i>implemented · low · S · memory, cpu</i></summary>

**Idea.** Do not insert empty attestations or empty per-key lists into the attestation pool, avoiding useless entries and iterations.

**Impact.** Empty per-key entries are created only together with a real attestation. Zero-score items are dropped before max-cover packing.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/attestation_storage.rs:462-463`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs#L462-L463) entry(checkpoint)/entry(data).or_default() are created only inside insert, which then pushes or aggregates a real attestation
- [`beacon_node/operation_pool/src/max_cover.rs:55-60`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/max_cover.rs#L55-L60) maximum_cover filters out score()==0 items before packing

**Skeptic check.** Confirmed that or_default runs only on the insert path and is filled at once, and confirmed the score()!=0 filter in maximum_cover. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#4753](https://github.com/OffchainLabs/prysm/pull/4753)

</details>


<a id="op_pool-086"></a>
<details>
<summary><b>op_pool-086</b> Rescore only same-data aggregates during packing — <i>partial · low · S · cpu</i></summary>

**Idea.** In greedy block attestation packing, after selecting an aggregate, rescore only remaining candidates with the same (slot, committee) data, since others' marginal coverage cannot change.

**Gap in Lighthouse.** The pack loop still touches all candidates each round; only the retain is limited to same data. Group candidates by (slot,index) (committee_bits post-Electra) so only matching groups are updated, and cache score in AttMaxCover rather than re-summing in maximum_cover/score().

**Impact.** Packing runs at most 8 or 128 rounds over hundreds to thousands of candidates; a score cache and grouped update could cut packing CPU several-fold, but it already runs in rayon::join so the saving is milliseconds.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/attestation.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation.rs) update_covering_set checks slot and index before retain
- [`beacon_node/operation_pool/src/max_cover.rs:76-90`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/max_cover.rs#L76-L90) still visits every available item each round and calls score() (sums a HashMap) in filter and max_by_key

**Sources.** [nimbus#5471](https://github.com/status-im/nimbus-eth2/pull/5471)

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

**Verdict history.** not (checked) → not (refuted)

**Sources.** [teku#9445](https://github.com/Consensys-Incorporated/teku/pull/9445)

</details>


<a id="op_pool-089"></a>
<details>
<summary><b>op_pool-089</b> Optimize unaggregated storage and expiry paths — <i>n/a · low · cpu</i></summary>

**Idea.** Optimize the attestation pool's unaggregated-attestation storage and its expiry pruning code paths.

**Impact.** Lighthouse's unaggregated storage is the naive aggregation pool keyed per slot with cheap prune; the Prysm PR is a vague 3-line tweak with no equivalent defect.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/lib.rs:455`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L455) checkpoint_map prune
- [`beacon_node/beacon_chain/src/naive_aggregation_pool.rs:557`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/naive_aggregation_pool.rs#L557) prune retains slots &gt;= lowest_permissible_slot

**Sources.** [prysm#11869](https://github.com/OffchainLabs/prysm/pull/11869)

</details>


<a id="op_pool-090"></a>
<details>
<summary><b>op_pool-090</b> Share one attestation pool for fork choice and blocks — <i>n/a · low · memory, cpu</i></summary>

**Idea.** Use a single attestation pool for fork-choice votes and block inclusion instead of two separate pools, avoiding duplicate storage and processing.

**Impact.** Fork-choice votes are already stored as latest messages, not a second attestation pool, so there is no duplicate storage to merge.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/lib.rs:295`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L295) op pool serves block inclusion only
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2699`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2699) add_to_block_inclusion_pool; fork choice records per-validator latest messages instead of a pool

**Sources.** [prysm#4014](https://github.com/OffchainLabs/prysm/pull/4014)

</details>


<a id="op_pool-091"></a>
<details>
<summary><b>op_pool-091</b> Validate max-cover inputs once — <i>n/a · low · cpu</i></summary>

**Idea.** Validate that all candidate bitlists have equal length once before max-cover aggregation, instead of on every greedy iteration.

**Impact.** Lighthouse does no per-iteration bitlist length validation in max-cover, so there is nothing to hoist.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/max_cover.rs:53`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/max_cover.rs#L53) maximum_cover loop has no per-iteration length validation
- [`beacon_node/operation_pool/src/attestation.rs:165`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation.rs#L165) update_covering_set uses difference_inplace

**Sources.** [prysm#8213](https://github.com/OffchainLabs/prysm/pull/8213)

</details>


<a id="op_pool-092"></a>
<details>
<summary><b>op_pool-092</b> Cache block roots by slot while filtering attestations — <i>partial · low · S · cpu, latency</i></summary>

**Idea.** While filtering pooled aggregates for block inclusion, cache block roots by slot for the pass so source, target and head checks do not re-read each root from the state tree. Cheaper because repeated tree lookups become hash-map hits.

**Gap in Lighthouse.** AttMaxCover::new_for_altair_or_later calls get_attestation_participation_flag_indices once per pooled aggregate. Each call reads state.get_block_root_at_epoch(target.epoch) and state.get_block_root(data.slot) from the milhouse block_roots tree. No per-pass slot-&gt;root (or per-AttestationData) cache is shared across aggregates in OperationPool::get_attestations.

**Impact.** Negligible. It saves two milhouse Vector lookups (about 13 levels) per aggregate, a few hundred per block proposal, which is microseconds.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:2739-2754`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2739-L2754)
- [`beacon_node/operation_pool/src/attestation.rs:74-95`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation.rs#L74-L95)
- [`consensus/state_processing/src/common/get_attestation_participation.rs:36-70`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/common/get_attestation_participation.rs#L36-L70)

**Skeptic check.** The earlier evidence cites the (root, target_epoch) memo in filter_op_pool_attestation. That memo caches the fork-choice shuffling-compatibility check, not the state block-root reads for the target and head checks, and those reads still happen per aggregate in the reward computation.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [lodestar#2910](https://github.com/ChainSafe/lodestar/pull/2910)

</details>


<a id="op_pool-093"></a>
<details>
<summary><b>op_pool-093</b> Drop single-vote attestations once committee aggregate exists — <i>partial · low · S · cpu, memory</i></summary>

**Idea.** Once a full committee aggregate has been built, delete the single-vote attestations it covers from the pool, and key the production cache without the redundant slot. The pool stores fewer entries and does less work.

**Gap in Lighthouse.** Insert already aggregates single votes into existing aggregates in place, so singles are not stored separately; the idea only matters if a full aggregate arrives after disjoint singles, and then should_aggregate/subset checks drop covered entries only partially.

**Impact.** Marginally fewer entries in the op pool; negligible on a mainnet node.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/attestation_storage.rs:457`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs#L457) insert greedily aggregates into existing entries; no deletion of covered singles
- [`beacon_node/operation_pool/src/attestation_storage.rs:489`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs#L489) aggregate_across_committees only merges committees

**Sources.** [nimbus#7959](https://github.com/status-im/nimbus-eth2/pull/7959)

</details>


<a id="op_pool-094"></a>
<details>
<summary><b>op_pool-094</b> Lazy max-heap greedy max-cover for block attestations — <i>not · low · M · cpu</i></summary>

**Idea.** Select block attestations by greedy max-cover using a max-heap and re-score only the top candidate, since marginal reward only shrinks. Avoids re-scoring all candidates after every pick.

**Gap in Lighthouse.** maximum_cover has no BinaryHeap or lazy re-scoring. To add it: keep a max-heap of (score, idx), pop the top, apply only the pending covering updates to that item, and push it back if its score dropped. score() sums a HashMap on every call, so cache it as well.

**Impact.** Since Electra the limit is 8 rounds, so the current cost is about 8 full scans of the candidate list, and the per-item update skips other slots and committees. Expect sub-millisecond to low-millisecond savings, on block production only.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/max_cover.rs:51`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/max_cover.rs#L51) documents O(limit * items)
- [`beacon_node/operation_pool/src/max_cover.rs:73-96`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/max_cover.rs#L73-L96) each round does a full max_by_key scan and a full update_covering_set pass over every available item
- [`beacon_node/operation_pool/src/attestation.rs:165-174`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation.rs#L165-L174) update_covering_set already returns early unless slot and committee index match, so most of the per-round update is cheap
- [`beacon_node/operation_pool/src/lib.rs:413-441`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L413-L441) curr and prev epoch covers already run in parallel with rayon::join; Electra limit is MaxAttestationsElectra (8)

**Second check.** Searched all of operation_pool for BinaryHeap, lazy or priority-queue selection and found none; max_cover.rs is the only selection path for attestations and attester slashings. Value lowered to low: the Electra limit is 8 and the per-item updates are filtered to the same slot and committee.

**Verdict history.** not (checked) → not (refuted)

**Sources.** [caplin#24566](https://github.com/erigontech/erigon/pull/24566)

</details>


<a id="op_pool-095"></a>
<details>
<summary><b>op_pool-095</b> Remove unused state fetch and slot advance in attestation path — <i>n/a · low · cpu</i></summary>

**Idea.** Remove a beacon state load and process-slots call in attestation handling whose result is unused. Saves a state load and slot advance per attestation.

**Gap in Lighthouse.** Lighthouse's pool insert path loads no state and advances no slots; the prysm waste does not exist here.

**Impact.** None.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:2699`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2699) add_to_block_inclusion_pool takes verified attestation, loads no state
- [`beacon_node/operation_pool/src/lib.rs:295`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L295) insert_attestation uses supplied attesting_indices

**Sources.** [prysm#3544](https://github.com/OffchainLabs/prysm/pull/3544)

</details>


<a id="op_pool-096"></a>
<details>
<summary><b>op_pool-096</b> Skip re-verifying gossip-verified attestations in the pool — <i>implemented · low · S · cpu</i></summary>

**Idea.** Do not re-verify attestation signatures when aggregating into the pool or when reading the pool, since gossip validation already verified them and block import verifies again; validate only when a proposer requests attestations for a slot.

**Impact.** The pool never re-verifies signatures on insert, on aggregate or on read. Block production re-verifies only with paranoid_block_proposal and otherwise uses NoVerification or VerifyRandao.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/lib.rs:290-303`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L290-L303)
- [`beacon_node/operation_pool/src/attestation_storage.rs:457`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs#L457)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2699-2716`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2699-L2716)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5995-6015`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5995-L6015)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:6530`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L6530)

**Skeptic check.** Confirmed insert_attestation takes already-verified attestations and only merges bitfields and aggregates signatures. The earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#3468](https://github.com/OffchainLabs/prysm/pull/3468), [prysm#3560](https://github.com/OffchainLabs/prysm/pull/3560)

</details>


