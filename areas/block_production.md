# block_production

55 ideas: 11 not, 6 partial, 34 implemented, 4 n/a; 11 actionable (high or medium value, verdict `not` or `partial`). [Back to the summary](../README.md).

Ids missing from the sequence are ideas that have not been checked against Lighthouse yet.

| id | idea | verdict | value | effort | resources |
|---|---|---|---|---|---|
| [block_production-001](#block_production-001) | Bounded builder header timeout with local fallback | implemented | high | S | latency |
| [block_production-002](#block_production-002) **★** | Compute block root after broadcasting proposal | not | medium | S | latency |
| [block_production-003](#block_production-003) | SSZ encoding for VC block production requests | implemented | medium | S | bandwidth, latency, cpu |
| [block_production-004](#block_production-004) | Build proposals on state pre-advanced to proposal slot | implemented | high | S | latency, cpu |
| [block_production-005](#block_production-005) | Aggregate unaggregated attestations with aggregates when packing | implemented | low | S | bandwidth, cpu |
| [block_production-008](#block_production-008) **★** | Attester cache keyed by epoch and head root | partial | medium | S | latency |
| [block_production-011](#block_production-011) | Read next-slot proposer from head state lookahead | implemented | medium | S | cpu, latency |
| [block_production-013](#block_production-013) | Allocation-free scoring in greedy proof selection | implemented | low | S | cpu |
| [block_production-016](#block_production-016) **★** | Payload attributes withdrawals without cloning head state | partial | medium | S | cpu, memory, latency |
| [block_production-019](#block_production-019) | Publish proposed or gossip-valid block before full import | implemented | high | S | latency, bandwidth |
| [block_production-020](#block_production-020) | Publish block first, blob/column sidecars afterwards | implemented | medium | S | latency, cpu, bandwidth |
| [block_production-021](#block_production-021) | Tune EL payload collection deadline within slot | not | low | M | latency |
| [block_production-025](#block_production-025) | Block value from rewards cached during state transition | not | low | M | cpu, latency |
| [block_production-028](#block_production-028) | Credential prefix check before balance read in withdrawals | not | low | S | cpu |
| [block_production-029](#block_production-029) | Compute payload attributes once for SSE and fcU | implemented | low |  | cpu |
| [block_production-030](#block_production-030) | Early fcU with attributes hitting cached payload ID | implemented | high | S | latency |
| [block_production-032](#block_production-032) | Skip parent-weight check on early fcU | implemented | low |  | cpu, latency |
| [block_production-034](#block_production-034) | Delay post-import fcU until shortly before next slot | implemented | medium | S | latency |
| [block_production-035](#block_production-035) | Filter packed attestations by shuffling dependent root | implemented | medium | S | cpu, latency, bandwidth |
| [block_production-037](#block_production-037) **★** | Propose with builder header without awaiting local payload | not | medium | M | latency |
| [block_production-038](#block_production-038) **★** | Drop newPayload for locally built payloads | not | medium | S | latency |
| [block_production-040](#block_production-040) | Read proposer index from primed proposer cache | implemented | low |  | cpu, latency |
| [block_production-041](#block_production-041) | Drop subset aggregates before packing | implemented | medium | S | bandwidth |
| [block_production-045](#block_production-045) | Build block body in parallel with payload fetch | implemented | high | S | latency, cpu |
| [block_production-049](#block_production-049) | Fast retry of busy payload preparation | n/a | low |  | latency |
| [block_production-055](#block_production-055) | Recompute fork choice head right before building proposal | implemented | medium | S | latency |
| [block_production-057](#block_production-057) | Skip payload-attribute preparation when not synced | implemented | high | S | memory, cpu |
| [block_production-058](#block_production-058) | Greedy max-cover attestation selection | implemented | low |  | cpu |
| [block_production-060](#block_production-060) | Process slots and state root once for all attestations | implemented | low |  | cpu, latency |
| [block_production-064](#block_production-064) | Keep pool signatures in deserialized form | implemented | medium | S | cpu, latency |
| [block_production-065](#block_production-065) | Re-run payload preparation late in prior slot | implemented | medium | S | latency |
| [block_production-067](#block_production-067) | Locally aggregate sync messages into block sync aggregate | not | low | M | cpu |
| [block_production-070](#block_production-070) | Request local payload and builder bid concurrently with cutoff | implemented | medium | S | latency |
| [block_production-073](#block_production-073) | Fall back to P2P bid in parallel with local build | implemented | low |  | latency |
| [block_production-075](#block_production-075) **★** | Gossip-verify blinded block in parallel with unblinding | not | medium | M | latency |
| [block_production-076](#block_production-076) **★** | Participation overlay instead of rebuilding epoch participation | partial | medium | M | cpu, latency |
| [block_production-077](#block_production-077) | Score attestations by newly set participation flags | implemented | medium | S | cpu |
| [block_production-079](#block_production-079) | Record payload ID for late-arriving blocks | implemented | medium |  | latency |
| [block_production-082](#block_production-082) | Do not key payload cache on safe/finalized hashes | implemented | medium |  | latency |
| [block_production-083](#block_production-083) | Build consensus block body only once | implemented | medium |  | cpu, memory, latency |
| [block_production-084](#block_production-084) | At most one state and epoch transition per proposal | implemented | medium |  | cpu, memory, latency |
| [block_production-085](#block_production-085) | Pre-build and sign next block before slot start | n/a | medium |  | latency |
| [block_production-089](#block_production-089) **★** | Precompute attestation packing at slot start | partial | medium | M | latency |
| [block_production-091](#block_production-091) **★** | Advance state for expected reorg parent | not | medium | S | cpu, latency |
| [block_production-092](#block_production-092) **★** | Advance state for next slot after late blocks | partial | medium | S | latency |
| [block_production-094](#block_production-094) | Produce from in-memory head state, not store | implemented | low |  | disk, latency |
| [block_production-098](#block_production-098) | Stop eth1 data voting work after deposit transition | implemented | medium | S | memory, cpu |
| [block_production-099](#block_production-099) | Prune pending deposits on finalization | n/a | low |  | cpu, memory |
| [block_production-100](#block_production-100) **★** | Publish blob sidecars before the block | partial | medium | S | latency, bandwidth |
| [block_production-110](#block_production-110) | Size attestation selection buffers by new attesters | implemented | low |  | memory |
| [block_production-111](#block_production-111) | Skip signature verification in own block state transition | implemented | medium | S | cpu, latency |
| [block_production-115](#block_production-115) | Skip re-hashing transactions of unblinded builder payload | n/a | medium | S | cpu, latency |
| [block_production-125](#block_production-125) | Skip reward sorting when attestations fit | not | low | S | cpu, latency |
| [block_production-135](#block_production-135) | Validate packed attestations without mutating state | implemented | medium | S | cpu, memory, latency |
| [block_production-136](#block_production-136) | Do not pack attestations before tracked inclusion window | not | low | S | cpu, bandwidth |

★ actionable. Click an id for the full record.

## Ideas

<a id="block_production-001"></a>
<details>
<summary><b>block_production-001</b> Bounded builder header timeout with local fallback — <i>implemented · high · S · latency</i></summary>

**Idea.** Put a hard, short (configurable) timeout on the builder getHeader request during block production and fall back to the locally built payload when it expires, so a slow relay cannot delay the proposal.

**Impact.** none; already bounded and falls back to local payload.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/builder_client/src/pre_gloas_builder_http_client.rs:35`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/builder_client/src/pre_gloas_builder_http_client.rs#L35) default get_header timeout 1000ms
- beacon_node/cli.rs:963 --builder-header-timeout capped 3000ms
- [`beacon_node/execution_layer/src/lib.rs:1056`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/lib.rs#L1056) fetch_builder_and_local_payloads joins builder and local; falls back to local on error

**Sources.** [prysm#11021](https://github.com/OffchainLabs/prysm/pull/11021), [prysm#17283](https://github.com/OffchainLabs/prysm/pull/17283)

</details>


<a id="block_production-002"></a>
<details>
<summary><b>block_production-002</b> Compute block root after broadcasting proposal — <i>not · medium · S · latency</i></summary>

**Idea.** Defer hash_tree_root of the proposed block until after it is broadcast, using only the slot for pre-broadcast logging, to take the HTR off the proposal critical path.

**Gap in Lighthouse.** The full-block root is hashed twice before broadcast (publish_blocks.rs:167 and inside GossipVerifiedBlock::new). Pass the root computed once into gossip verification, or take it from GossipVerifiedBlock, to remove the duplicate. Gossip verification needs the root (seen-cache, proposer checks), so the root cannot move fully after broadcast the way Prysm does it.

**Impact.** Removes one redundant block-body HTR (~several ms for large payloads) from the proposal critical path; small.

**Best measured result.** HTR ~10-20ms on M1 Max (pr:prysm#12504)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/publish_blocks.rs:167`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/publish_blocks.rs#L167) block_root = block_root.unwrap_or_else(\|\| block.canonical_root()) before any publish (all full-block callers pass None: http_api/src/lib.rs:880,919,963,1005)
- [`beacon_node/beacon_chain/src/block_verification.rs:878-893`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L878-L893) GossipVerifiedBlock::new recomputes the root via signed_block_header()+get_block_header_root before publish
- [`beacon_node/http_api/src/publish_blocks.rs:249-268`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/publish_blocks.rs#L249-L268) publish_block_p2p runs only after into_gossip_verified_block succeeds
- [`beacon_node/http_api/src/publish_blocks.rs:664-669`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/publish_blocks.rs#L664-L669) blinded path hashes the cheaper blinded block and passes Some(root), but still before broadcast

**Second check.** Checked every publish_block caller, the blinded-block path, and GossipVerifiedBlock::new. No deferral exists. The search also found that the root is computed twice before publish, which is a cheaper and more realistic fix than full deferral.

**Sources.** [prysm#12504](https://github.com/OffchainLabs/prysm/pull/12504)

</details>


<a id="block_production-003"></a>
<details>
<summary><b>block_production-003</b> SSZ encoding for VC block production requests — <i>implemented · medium · S · bandwidth, latency, cpu</i></summary>

**Idea.** Have the validator client request and receive produced blocks as SSZ instead of JSON by default, avoiding JSON encode/decode cost and payload size for large blocks with blobs.

**Impact.** none; VC uses SSZ with fallback.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/block_service.rs:707`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/block_service.rs#L707) post_validator_blocks_v4_ssz
- [`validator_client/validator_services/src/block_service.rs:794`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/block_service.rs#L794) get_validator_blocks_v3_ssz

**Sources.** [lighthouse#7727](https://github.com/sigp/lighthouse/pull/7727)

</details>


<a id="block_production-004"></a>
<details>
<summary><b>block_production-004</b> Build proposals on state pre-advanced to proposal slot — <i>implemented · high · S · latency, cpu</i></summary>

**Idea.** Advance the head state to the proposal slot (slot and epoch processing, including any epoch transition) before the slot starts, cache it, and have block production clone that state and run only process_block on it, passing the known state root. This removes process_slots/epoch processing from the proposal critical path.

**Impact.** none.

**Best measured result.** Pyrmont block production ~550ms -&gt; ~150ms (pr:lighthouse#2241)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/state_advance_timer.rs:109`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L109) advances head state at 3/4 of slot
- [`beacon_node/beacon_chain/src/block_production/mod.rs:87`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_production/mod.rs#L87) get_advanced_hot_state used for production
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5870`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5870) complete_state_advance is a no-op when state is already at slot

**Sources.** [nimbus#7518](https://github.com/status-im/nimbus-eth2/pull/7518), [teku#9787](https://github.com/Consensys-Incorporated/teku/pull/9787), [lodestar@3c3662ce2](https://github.com/ChainSafe/lodestar/commit/3c3662ce28d9), [nimbus#4185](https://github.com/status-im/nimbus-eth2/pull/4185), [lighthouse#2241](https://github.com/sigp/lighthouse/pull/2241), [teku#3266](https://github.com/Consensys-Incorporated/teku/pull/3266), [lodestar@a8385b3c3](https://github.com/ChainSafe/lodestar/commit/a8385b3c3184), [teku#2814](https://github.com/Consensys-Incorporated/teku/pull/2814)

</details>


<a id="block_production-005"></a>
<details>
<summary><b>block_production-005</b> Aggregate unaggregated attestations with aggregates when packing — <i>implemented · low · S · bandwidth, cpu</i></summary>

**Idea.** When packing a block, pack aggregated and unaggregated pool attestations from one combined list, aggregating singles (e.g. previous slot) into matching aggregates before selection. The block carries fewer, denser attestations and more duplicates are removed.

**Impact.** None; singles are merged into aggregates in the op pool and max cover selects from that one list.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:5944-5960`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5944-L5960) naive aggregation pool attestations are inserted into op pool before packing
- [`beacon_node/operation_pool/src/attestation_storage.rs:457`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs#L457) AttestationMap::insert greedily aggregates into existing aggregates
- [`beacon_node/operation_pool/src/lib.rs:383`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L383) aggregate_across_committees for electra+

**Sources.** [prysm#6919](https://github.com/OffchainLabs/prysm/pull/6919), [teku#9197](https://github.com/Consensys-Incorporated/teku/pull/9197), [prysm#9683](https://github.com/OffchainLabs/prysm/pull/9683)

</details>


<a id="block_production-008"></a>
<details>
<summary><b>block_production-008</b> Attester cache keyed by epoch and head root — <i>partial · medium · S · latency</i></summary>

**Idea.** Keep a cache of attestation-data inputs (justified checkpoint, target root, committee lengths) keyed by epoch and head/target root, so attestation data for any slot can be served without loading and advancing a state.

**Gap in Lighthouse.** No (epoch, root)-keyed attester cache exists (no attester_cache.rs; only early_attester_cache, shuffling_cache, beacon_proposer_cache). Cross-epoch requests still load an advanced hot state and may partial-advance it; a small cache of justified checkpoint + committee lengths keyed by (epoch, decision root) would remove that.

**Impact.** Only epoch-boundary attestation production when head state lags request epoch; state advance timer usually pre-advances, so saving is small.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:2025`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2025) early_attester_cache.try_attest
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2124`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2124) same-epoch path reads justified checkpoint and committee len from head state
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2152`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2152) cross-epoch path get_advanced_hot_state + partial_state_advance + build_committee_cache

**Second check.** Listed beacon_chain/src for any attester/committee-length cache and grepped AttesterCache across beacon_node; only an error variant name survives in shuffling_cache.rs:83, no cache.

**Sources.** [lighthouse#2478](https://github.com/sigp/lighthouse/pull/2478)

</details>


<a id="block_production-011"></a>
<details>
<summary><b>block_production-011</b> Read next-slot proposer from head state lookahead — <i>implemented · medium · S · cpu, latency</i></summary>

**Idea.** Post-Fulu, read the next-slot proposer index from the head state's proposer lookahead instead of advancing a state through the epoch transition just to learn it, and build the prepared next-slot state only once.

**Impact.** Already cheap: next-slot proposer comes from the lookahead vector via the proposer cache, no epoch transition needed.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:1655`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L1655) get_beacon_proposer_index reads proposer_lookahead post-Fulu
- [`consensus/types/src/state/beacon_state.rs:1681`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L1681) get_beacon_proposer_indices slices lookahead
- [`beacon_node/beacon_chain/src/beacon_proposer_cache.rs:227`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_proposer_cache.rs#L227) proposer cache fills from that
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5286`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5286) get_pre_payload_attributes uses with_proposer_cache with head state

**Sources.** [lodestar#9762](https://github.com/ChainSafe/lodestar/pull/9762)

</details>


<a id="block_production-013"></a>
<details>
<summary><b>block_production-013</b> Allocation-free scoring in greedy proof selection — <i>implemented · low · S · cpu</i></summary>

**Idea.** In greedy aggregate/proof selection, count newly covered validators without allocating per candidate and materialize the covered set only for the winning pick.

**Gap in Lighthouse.** Minor: each candidate still owns a HashMap built up front in AttMaxCover::new_for_altair_or_later, and the winner is cloned (max_cover.rs:84).

**Impact.** Per-iteration allocation is already one clone of the winner; remaining cost is the up-front per-candidate HashMap, negligible against block production time.

**Best measured result.** Removes N-1 allocations per iteration (no timings) (pr:ethlambda#254)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/max_cover.rs:61-100`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/max_cover.rs#L61-L100) greedy loop updates candidate sets in place
- [`beacon_node/operation_pool/src/attestation.rs:165`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation.rs#L165) update_covering_set uses retain, no new set per candidate
- [`beacon_node/operation_pool/src/attestation.rs:176`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation.rs#L176) score sums values without allocating

**Sources.** [ethlambda#254](https://github.com/lambdaclass/ethlambda/pull/254)

</details>


<a id="block_production-016"></a>
<details>
<summary><b>block_production-016</b> Payload attributes withdrawals without cloning head state — <i>partial · medium · S · cpu, memory, latency</i></summary>

**Idea.** Compute withdrawals, randao mix and proposer index for next-slot payload attributes from the shared head/snapshot state without cloning it or doing extra state advances, and reuse cached payload attributes.

**Gap in Lighthouse.** Proposer index/randao come from caches and the Empty-parent Gloas case skips advance, but the normal path still clones (CoW) and partial-advances the head state to proposal_slot, including epoch processing across a boundary. Restoring the pre-Gloas cap (advance at most to the epoch boundary, or compute withdrawals from the unadvanced state) closes it.

**Impact.** Small: one partial advance per proposer-prep call; larger only at epoch boundaries.

**Best measured result.** reduced memory usage (pr:caplin#11997)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:5396`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5396) compute_withdrawals_for_payload_attributes borrows head state
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5432`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5432) Empty-parent path returns payload_expected_withdrawals without advance
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5440`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5440) TODO(gloas) restore pre-Gloas no-advance-past-epoch optimisation
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5452`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5452) into_owned + partial_state_advance to proposal_slot

**Second check.** Re-read the full function: found the additional Empty-parent short-circuit (no advance) not cited earlier, and the explicit TODO confirming the advance is still done otherwise.

**Sources.** [lighthouse#4027](https://github.com/sigp/lighthouse/pull/4027), [caplin#11997](https://github.com/erigontech/erigon/pull/11997)

</details>


<a id="block_production-019"></a>
<details>
<summary><b>block_production-019</b> Publish proposed or gossip-valid block before full import — <i>implemented · high · S · latency, bandwidth</i></summary>

**Idea.** Broadcast a block (and its blobs) as soon as gossip/consensus validation passes, in parallel with or before full import (DB write, fork choice), instead of only after import completes, so propagation starts earlier.

**Gap in Lighthouse.** Consensus/ConsensusAndEquivocation levels publish only after validation by design; VC default uses Gossip level.

**Impact.** none for default path.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/publish_blocks.rs:249`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/publish_blocks.rs#L249) BroadcastValidation::Gossip publishes right after gossip verification, before process_block
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1661`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1661) Accept propagated before import

**Sources.** [nimbus@850eece94](https://github.com/status-im/nimbus-eth2/commit/850eece949fe), [nimbus#3156](https://github.com/status-im/nimbus-eth2/pull/3156), [teku#8728](https://github.com/Consensys-Incorporated/teku/pull/8728), [teku#7371](https://github.com/Consensys-Incorporated/teku/pull/7371), [prysm#13380](https://github.com/OffchainLabs/prysm/pull/13380)

</details>


<a id="block_production-020"></a>
<details>
<summary><b>block_production-020</b> Publish block first, blob/column sidecars afterwards — <i>implemented · medium · S · latency, cpu, bandwidth</i></summary>

**Idea.** On proposal, publish the block to the network immediately without waiting on sidecars, then compute/broadcast the blob or data column sidecars (KZG cell proofs) concurrently afterwards. The block leaves sooner and low-upload nodes do not delay it behind sidecar uploads.

**Gap in Lighthouse.** At Consensus or ConsensusAndEquivocation broadcast validation the block is published from publish_fn inside process_block, after columns are built and gossip-verified; only the default Gossip level publishes before the sidecars.

**Impact.** Block leaves without waiting for KZG cell proof computation on the default path.

**Best measured result.** avg wait 18.04 ms vs 23.48 ms over 2000 holesky blocks (pr:teku#8868)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/publish_blocks.rs:242`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/publish_blocks.rs#L242) sidecar build spawned as blocking task concurrently
- [`beacon_node/http_api/src/publish_blocks.rs:249-266`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/publish_blocks.rs#L249-L266) block published p2p right after gossip verification (Gossip level, the VC default)
- [`beacon_node/http_api/src/publish_blocks.rs:295`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/publish_blocks.rs#L295) columns awaited and published afterwards (line 313)

**Sources.** [prysm#15720](https://github.com/OffchainLabs/prysm/pull/15720), [prysm#15719](https://github.com/OffchainLabs/prysm/pull/15719), [teku#8868](https://github.com/Consensys-Incorporated/teku/pull/8868), [grandine@c6d914c9c](https://github.com/grandinetech/grandine/commit/c6d914c9c334)

</details>


<a id="block_production-021"></a>
<details>
<summary><b>block_production-021</b> Tune EL payload collection deadline within slot — <i>not · low · M · latency</i></summary>

**Idea.** Choose the time to call getPayload relative to slot start and attestation deadline: give the EL a fill window instead of grabbing the first (near-empty) result, but stop early enough that the block is published in time.

**Gap in Lighthouse.** get_payload is called whenever the VC requests a block; the EL builds from the earlier forkchoiceUpdated with attributes, but nothing tunes call time against slot start or the attestation deadline. Would need a delay/deadline in the block production path before the get_payload call in execution_payload.rs.

**Impact.** Could raise block value (fuller local payloads) when the EL has little build time; no CPU saving. Gain depends on how early the VC requests the block.

**Best measured result.** Sepolia: 3 txs/0.185% gas/53 ms -&gt; 245 txs/33.1% gas/3.08 s build (pr:caplin#21989)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/execution_payload.rs:437`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/execution_payload.rs#L437) get_payload called when block production runs
- [`beacon_node/execution_layer/src/lib.rs:976`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/lib.rs#L976) get_payload has no fill-window or deadline logic

**Sources.** [caplin#21989](https://github.com/erigontech/erigon/pull/21989), [caplin#24948](https://github.com/erigontech/erigon/pull/24948)

</details>


<a id="block_production-025"></a>
<details>
<summary><b>block_production-025</b> Block value from rewards cached during state transition — <i>not · low · M · cpu, latency</i></summary>

**Idea.** Record consensus block rewards and payload value in a per-slot cache attached to the state while processing the produced block, so block production returns the block value without a second rewards pass or body parsing, and pass block metadata between VC and BN in headers.

**Gap in Lighthouse.** Record rewards inside per_block_processing (process_attestations, sync aggregate, slashings) into a state/ctxt accumulator, and have produce_partial_beacon_block/produce_block_on_state read it instead of calling compute_beacon_block_reward. Needs a reward-tracking hook in consensus/state_processing.

**Impact.** Removes one extra attestation-walk and participation-list clone per produced block (a few ms on proposal only); negligible for non-proposing nodes.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:6537`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L6537) compute_beacon_block_reward called as separate pass before per_block_processing
- [`beacon_node/beacon_chain/src/beacon_block_reward.rs:273`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_block_reward.rs#L273) re-walks block attestations, copies participation lists, rebuilds committee caches
- [`beacon_node/beacon_chain/src/block_production/gloas.rs:862`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_production/gloas.rs#L862) same second pass for Gloas

**Sources.** [teku#7953](https://github.com/Consensys-Incorporated/teku/pull/7953), [teku#7943](https://github.com/Consensys-Incorporated/teku/pull/7943), [teku#7987](https://github.com/Consensys-Incorporated/teku/pull/7987)

</details>


<a id="block_production-028"></a>
<details>
<summary><b>block_production-028</b> Credential prefix check before balance read in withdrawals — <i>not · low · S · cpu</i></summary>

**Idea.** In get_expected_withdrawals, test the eth1 withdrawal credential prefix with a single-byte compare first and read the validator balance only for validators that pass.

**Gap in Lighthouse.** In get_validators_sweep_withdrawals test validator.has_execution_withdrawal_credential(spec) first and only call get_balance_after_withdrawals for those that pass (skip validator otherwise). Note most validators are 0x01/0x02 on mainnet now, so the saving is smaller than in Teku's measurement; the balance lookup is a milhouse list get.

**Impact.** Saves up to 16384 balance tree lookups per get_expected_withdrawals (block processing, block production, payload attributes); likely sub-millisecond to low ms per call, only helps validators with 0x00 credentials.

**Best measured result.** Benchmark on mainnet-like state: ~0.023-0.029 s/op before, ~0.008-0.013 s/op after (pr:teku#6525)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_block_processing/withdrawals.rs:280-283`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/withdrawals.rs#L280-L283) get_validators_sweep_withdrawals reads balance via get_balance_after_withdrawals for every validator before calling is_fully/partially_withdrawable_validator
- [`consensus/types/src/validator/validator.rs:193-275`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/validator/validator.rs#L193-L275) credential check happens only inside those predicates, after the balance read

**Sources.** [teku#6525](https://github.com/Consensys-Incorporated/teku/pull/6525)

</details>


<a id="block_production-029"></a>
<details>
<summary><b>block_production-029</b> Compute payload attributes once for SSE and fcU — <i>implemented · low · cpu</i></summary>

**Idea.** Compute payload attributes (withdrawals, gas limit) once and reuse them for both the payload_attributes SSE event and the EL forkchoiceUpdated call.

**Impact.** Already computed once per prepare and shared by SSE and fcU.

**Best measured result.** best case 6.2us, worst case 2.8ms per run; PR calls it a cleanup, not a perf improvement (pr:lodestar#10056)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:6954`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L6954) payload_attributes fetched from EL cache, computed only on miss (comment: saves recomputing withdrawals)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:7033-7068`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L7033-L7068) PayloadAttributes::new once then insert_proposer
- [`beacon_node/beacon_chain/src/beacon_chain.rs:7103`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L7103) same value reused for SSE event; fcU reads it from the cache

**Sources.** [lodestar#10056](https://github.com/ChainSafe/lodestar/pull/10056)

</details>


<a id="block_production-030"></a>
<details>
<summary><b>block_production-030</b> Early fcU with attributes hitting cached payload ID — <i>implemented · high · S · latency</i></summary>

**Idea.** Before the slot of a known local proposer (at a proportional point in the prior slot, and again on head change), send forkchoiceUpdated with payload attributes to the EL and cache the returned payload ID keyed by head/parent, with attributes and fork detection matching those used at getPayload time. Block production then calls getPayload with the cached ID at once instead of building a payload last-minute.

**Impact.** none.

**Best measured result.** shaved 0.5s off block production in minimal-preset testnets (pr:nimbus#7986)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/state_advance_timer.rs:217`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L217) prepare_beacon_proposer called ahead of next slot
- [`beacon_node/beacon_chain/src/canonical_head.rs:1931`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1931) also on head change
- [`beacon_node/beacon_chain/src/beacon_chain.rs:6719`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L6719) sends fcU with payload attributes
- [`beacon_node/execution_layer/src/lib.rs:1342`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/lib.rs#L1342) engine.get_payload_id cache lookup before getPayload

**Sources.** [lighthouse#4703](https://github.com/sigp/lighthouse/pull/4703), [lodestar#4446](https://github.com/ChainSafe/lodestar/pull/4446), [nimbus#7986](https://github.com/status-im/nimbus-eth2/pull/7986), [prysm#10481](https://github.com/OffchainLabs/prysm/pull/10481), [lighthouse#3043](https://github.com/sigp/lighthouse/pull/3043), [lodestar#4209](https://github.com/ChainSafe/lodestar/pull/4209), [prysm#10803](https://github.com/OffchainLabs/prysm/pull/10803), [caplin#23399](https://github.com/erigontech/erigon/pull/23399)

</details>


<a id="block_production-032"></a>
<details>
<summary><b>block_production-032</b> Skip parent-weight check on early fcU — <i>implemented · low · cpu, latency</i></summary>

**Idea.** For early proposer forkchoiceUpdated calls, skip the parent-weight (reorg) check until current attestations are imported, so the EL does not build a payload that is later discarded.

**Impact.** Early fcU (before the re-org slot) skips the parent-weight check, so the EL builds on the parent rather than a payload later discarded.

**Best measured result.** avoids wasted EL payload build (pr:prysm#13683)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:5576-5586`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5576-L5586) head/parent weight thresholds only enforced when fork_choice_slot == re_org_block_slot, otherwise (true,true)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5611`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5611) head-late check is the early heuristic, comment explains attestations not yet imported

**Sources.** [prysm#13683](https://github.com/OffchainLabs/prysm/pull/13683)

</details>


<a id="block_production-034"></a>
<details>
<summary><b>block_production-034</b> Delay post-import fcU until shortly before next slot — <i>implemented · medium · S · latency</i></summary>

**Idea.** Instead of sending forkchoiceUpdated right after block import, send it shortly before the next slot so the EL returns a payload id and proposer-boost reorg remains possible.

**Gap in Lighthouse.** Lighthouse does not delay the post-import fcU but achieves the same effect differently: the post-import fcU is overridden to the parent when re-org conditions hold, and the payload-attribute fcU is sent late in the slot (not Gloas, which never overrides).

**Impact.** Same re-org and payload id outcome; no extra cost to add.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:5503`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5503) overridden_forkchoice_update_params suppresses head fcU when a re-org is planned
- [`beacon_node/beacon_chain/src/beacon_chain.rs:6719`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L6719) prepare_beacon_proposer sends the payload-attributes fcU shortly before next slot
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:210`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L210) calls it after pre-emptive fork choice

**Sources.** [lodestar#7428](https://github.com/ChainSafe/lodestar/pull/7428)

</details>


<a id="block_production-035"></a>
<details>
<summary><b>block_production-035</b> Filter packed attestations by shuffling dependent root — <i>implemented · medium · S · cpu, latency, bandwidth</i></summary>

**Idea.** When packing attestations, drop those whose target shuffling/dependent root differs from the proposal state's using a cheap root comparison, before any expensive validity checks.

**Impact.** Already done before expensive reward computation, with a per-call cache.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:2739`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2739) filter_op_pool_attestation
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2765`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2765) shuffling_is_compatible compares shuffling IDs from fork choice, cheap
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5983`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5983) filter passed into op_pool.get_attestations; cached per (block_root, target_epoch)
- [`beacon_node/operation_pool/src/lib.rs:327`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L327) filter runs before AttMaxCover::new

**Sources.** [nimbus#4273](https://github.com/status-im/nimbus-eth2/pull/4273), [lodestar#4336](https://github.com/ChainSafe/lodestar/pull/4336)

</details>


<a id="block_production-037"></a>
<details>
<summary><b>block_production-037</b> Propose with builder header without awaiting local payload — <i>not · medium · M · latency</i></summary>

**Idea.** If the builder header is ready, propose with it without waiting for a slow local payload; compare values only when the local payload has already finished.

**Gap in Lighthouse.** fetch_builder_and_local_payloads joins both futures; no select/early return when the builder header is ready, even with builder_boost_factor favoring the builder. Switch to select with a short grace period for the local payload.

**Impact.** Saves the local-vs-relay latency gap on builder proposals when the local getPayload is slow (usually fast since payload is prebuilt via fcU).

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/execution_layer/src/lib.rs:1076`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/lib.rs#L1076) comment 'Wait for the builder *and* local EL' + tokio::join!
- [`beacon_node/execution_layer/src/lib.rs:1157`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/lib.rs#L1157) determine_and_fetch_payload matches on both results after join

**Second check.** Searched execution_layer/src/lib.rs for select!/timeouts and builder-preference short circuits; only builder_header_timeout on the relay side and chain-health fallback to local exist.

**Sources.** [grandine#849](https://github.com/grandinetech/grandine/pull/849)

</details>


<a id="block_production-038"></a>
<details>
<summary><b>block_production-038</b> Drop newPayload for locally built payloads — <i>not · medium · S · latency</i></summary>

**Idea.** Do not call engine_newPayload on a locally built payload during block production; the safeguard costs more latency than it is worth.

**Gap in Lighthouse.** Own blocks and self-built Gloas envelopes still go through engine_newPayload; is_locally_built_block only affects provenance/logging. Add a precomputed Valid status for payloads the EL itself produced (e.g. hit in payload_cache) in PayloadNotifier::new and the envelope PayloadNotifier.

**Impact.** One EL round trip off local import of own block; block is already published, so small.

**Best measured result.** "a safeguard which probably costs more than is worth" (pr:nimbus#4186)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/execution_payload.rs:77`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/execution_payload.rs#L77) precomputed status only for NotifyExecutionLayer::No with optimistic_finalized_sync
- [`beacon_node/beacon_chain/src/execution_payload.rs:104`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/execution_payload.rs#L104) notify_new_payload otherwise calls EL
- [`beacon_node/beacon_chain/src/payload_envelope_verification/import.rs:451`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_envelope_verification/import.rs#L451) envelope import uses NotifyExecutionLayer::Yes
- [`beacon_node/execution_layer/src/lib.rs:1445`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/lib.rs#L1445) notify_new_payload has no payload_cache/self-built short-circuit

**Second check.** Also checked the Gloas envelope path (payload_notifier.rs, import.rs) and the EL's notify_new_payload/payload_cache; self-built envelopes only get a signature-verification fast path, not a newPayload skip.

**Sources.** [nimbus#4186](https://github.com/status-im/nimbus-eth2/pull/4186)

</details>


<a id="block_production-040"></a>
<details>
<summary><b>block_production-040</b> Read proposer index from primed proposer cache — <i>implemented · low · cpu, latency</i></summary>

**Idea.** During block creation, read the proposer index from the proposer cache instead of recomputing proposer shuffling (e.g. at epoch boundaries), and have the state advance timer prime the next-epoch proposer cache (Fulu lookahead) ahead of time.

**Impact.** Fulu lookahead makes the index a vector read; cache is primed ahead of the epoch boundary. Pre-Fulu recompute path remains but is dead on mainnet.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:1654-1700`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L1654-L1700) post-Fulu proposer index read from proposer_lookahead in state (O(1))
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:343-398`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L343-L398) state advance primes proposer cache for current and next epoch
- [`beacon_node/beacon_chain/src/block_production/gloas.rs:409`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_production/gloas.rs#L409) and beacon_chain.rs:5891 get_beacon_proposer_index on advanced state

**Sources.** [teku#693](https://github.com/Consensys-Incorporated/teku/pull/693), [lighthouse#8130](https://github.com/sigp/lighthouse/pull/8130), [lighthouse#4338](https://github.com/sigp/lighthouse/pull/4338)

</details>


<a id="block_production-041"></a>
<details>
<summary><b>block_production-041</b> Drop subset aggregates before packing — <i>implemented · medium · S · bandwidth</i></summary>

**Idea.** Just before packing, remove aggregates whose bits are a subset of another selected aggregate so no block space goes to attestations with no new votes.

**Impact.** None needed; subset aggregates score zero and are never selected.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/max_cover.rs:53`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/max_cover.rs#L53) maximum_cover drops score==0 items and removes covered validators after each pick
- [`beacon_node/operation_pool/src/attestation.rs:165`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation.rs#L165) update_covering_set removes already-covered validators so subsets reach score 0

**Sources.** [prysm#8063](https://github.com/OffchainLabs/prysm/pull/8063)

</details>


<a id="block_production-045"></a>
<details>
<summary><b>block_production-045</b> Build block body in parallel with payload fetch — <i>implemented · high · S · latency, cpu</i></summary>

**Idea.** Fire the engine getPayload and builder header requests at the start of production and build the consensus/blinded body (attestations, operations, state processing) concurrently as an independent part, joining at the end. Production takes the max of the two flows instead of their sum.

**Impact.** none; production is max of the two flows.

**Best measured result.** race cutoff lowered from 2.5s to 2s (pr:lodestar#7814)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:5919`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5919) get_execution_payload spawned before attestation packing
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5760`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5760) payload handle awaited after partial block built
- [`beacon_node/execution_layer/src/lib.rs:1077`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/lib.rs#L1077) tokio::join! of builder and local fetch

**Sources.** [lodestar#7814](https://github.com/ChainSafe/lodestar/pull/7814), [teku#9455](https://github.com/Consensys-Incorporated/teku/pull/9455), [lodestar#7726](https://github.com/ChainSafe/lodestar/pull/7726), [lodestar#7740](https://github.com/ChainSafe/lodestar/pull/7740), [prysm#12297](https://github.com/OffchainLabs/prysm/pull/12297), [prysm#12408](https://github.com/OffchainLabs/prysm/pull/12408), [prysm#12811](https://github.com/OffchainLabs/prysm/pull/12811), [prysm#13008](https://github.com/OffchainLabs/prysm/pull/13008), [prysm#12251](https://github.com/OffchainLabs/prysm/pull/12251), [grandine@7b959604b](https://github.com/grandinetech/grandine/commit/7b959604b516), [lodestar#7815](https://github.com/ChainSafe/lodestar/pull/7815)

</details>


<a id="block_production-049"></a>
<details>
<summary><b>block_production-049</b> Fast retry of busy payload preparation — <i>n/a · low · latency</i></summary>

**Idea.** When the EL is busy and payload build preparation is skipped, retry quickly (exponential backoff from ~10 ms, or frequent retries within the preparation window) instead of a fixed long delay, so the build starts earlier.

**Impact.** Caplin's embedded EL semaphore returns busy and defers; Lighthouse talks to an external EL via engine API fcU, which just blocks until the EL answers, so there is no skipped-preparation retry to tighten.

**Best measured result.** wait before build p50 200 ms -&gt; 71 ms, p90 200 -&gt; 151 ms (pr:caplin#24965)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/proposer_prep_service.rs:28-65`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/proposer_prep_service.rs#L28-L65) fixed timer prepare_payload_lookahead before slot
- [`beacon_node/beacon_chain/src/canonical_head.rs:1908-1931`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1908-L1931) prepare after each head fcU
- [`beacon_node/beacon_chain/src/beacon_chain.rs:7137-7150`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L7137-L7150) awaited fcU over JSON-RPC, no busy/skip state

**Sources.** [caplin#24965](https://github.com/erigontech/erigon/pull/24965), [caplin#25207](https://github.com/erigontech/erigon/pull/25207)

</details>


<a id="block_production-055"></a>
<details>
<summary><b>block_production-055</b> Recompute fork choice head right before building proposal — <i>implemented · medium · S · latency</i></summary>

**Idea.** Immediately before block production, process pending attestations and run fork choice to recompute the head, so the proposal builds on the freshest head.

**Impact.** Already in place: the proposal blocks until fork choice has run at the start of the proposal slot, so all attestations that may count (those from earlier slots) are applied. A second inline run would add only late votes that arrive in the few ms after slot start.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_production/mod.rs:48`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_production/mod.rs#L48) load_state_for_block_production first calls wait_for_fork_choice_before_block_production
- [`beacon_node/beacon_chain/src/block_production/mod.rs:130`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_production/mod.rs#L130) waits (fork_choice_before_proposal_timeout_ms) on fork_choice_signal_rx for the slot-start fork choice run
- [`beacon_node/beacon_chain/src/beacon_chain.rs:7496`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L7496) per_slot_task runs recompute_head_at_current_slot at slot start
- [`beacon_node/beacon_chain/src/beacon_chain.rs:7512`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L7512) then notifies the waiting block production via notify_fork_choice_complete
- [`beacon_node/beacon_chain/src/fork_choice_signal.rs:74`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/fork_choice_signal.rs#L74) wait_for_fork_choice
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:211`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L211) extra pre-emptive recompute_head_at_slot(next_slot) before the slot

**Second check.** The earlier review missed block_production/mod.rs: block production does not run fork choice itself, but it waits on the ForkChoiceSignal for the slot-start run. This gives the same freshest-head guarantee.

**Sources.** [teku#5569](https://github.com/Consensys-Incorporated/teku/pull/5569), [prysm#11992](https://github.com/OffchainLabs/prysm/pull/11992)

</details>


<a id="block_production-057"></a>
<details>
<summary><b>block_production-057</b> Skip payload-attribute preparation when not synced — <i>implemented · high · S · memory, cpu</i></summary>

**Idea.** Do not compute payload attributes (state copy and slot replay) while the node is not in regular sync, and do not consider the node synced while its head is far behind peer-reported heads. This stops payload-attribute preparation from regenerating state across hundreds of epochs.

**Gap in Lighthouse.** No peer-head based synced check, but head-vs-wallclock tolerance gives the same protection; cache miss clones head state without replay.

**Impact.** none.

**Best measured result.** Stated: 9 GB heap exhausted by replaying ~27-34 epoch transitions when head was 850-1100 slots behind (pr:teku#11219)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:6752`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L6752) skips prep if head older than sync_tolerance_epochs
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5319`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5319) SkipProposerPreparation on proposer cache miss when head far behind
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:269`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L269) MAX_ADVANCE_DISTANCE 256

**Sources.** [teku#11219](https://github.com/Consensys-Incorporated/teku/pull/11219), [prysm#16951](https://github.com/OffchainLabs/prysm/pull/16951)

</details>


<a id="block_production-058"></a>
<details>
<summary><b>block_production-058</b> Greedy max-cover attestation selection — <i>implemented · low · cpu</i></summary>

**Idea.** Select block attestations with a greedy max-cover algorithm, scoring each candidate by not-yet-covered bits, as a cheap approximation to optimal packing.

**Impact.** Lighthouse already packs attestations with greedy weighted max-cover (scored by newly covered validators times reward).

**Best measured result.** slower than naive sort: 512 single-bit atts about 5.1 ms vs 0.31 ms; a quality trade-off (pr:prysm#8571)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/max_cover.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/max_cover.rs) maximum_cover greedy
- [`beacon_node/operation_pool/src/lib.rs:447`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L447) merge_solutions of max-cover results
- [`beacon_node/operation_pool/src/lib.rs:345`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L345) get_attestations

**Sources.** [grandine#156](https://github.com/grandinetech/grandine/pull/156), [prysm#8571](https://github.com/OffchainLabs/prysm/pull/8571)

</details>


<a id="block_production-060"></a>
<details>
<summary><b>block_production-060</b> Process slots and state root once for all attestations — <i>implemented · low · cpu, latency</i></summary>

**Idea.** In block production, run process_slots and the state hash_tree_root once and reuse them for every packed attestation instead of per attestation.

**Impact.** State is advanced and rooted once, then all attestations are selected against that one state.

**Best measured result.** should save 50ms to 100ms on block proposals (pr:prysm#5632)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_production/gloas.rs:395`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_production/gloas.rs#L395) complete_state_advance once per production
- [`beacon_node/beacon_chain/src/block_production/gloas.rs:409-420`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_production/gloas.rs#L409-L420) one op_pool pass on the single advanced state
- [`beacon_node/operation_pool/src/lib.rs:345`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L345) get_attestations takes one state for all attestations

**Sources.** [prysm#5632](https://github.com/OffchainLabs/prysm/pull/5632)

</details>


<a id="block_production-064"></a>
<details>
<summary><b>block_production-064</b> Keep pool signatures in deserialized form — <i>implemented · medium · S · cpu, latency</i></summary>

**Idea.** Store attestation pool signatures as already-decompressed curve points (lazy aggregation) so building a block does not decompress each signature.

**Impact.** None needed; the pool keeps the aggregate as a blst point, so packing does not decompress per signature (assuming bls AggregateSignature holds the decompressed point, which it does in the blst backend).

**Best measured result.** Proposal ~6x faster at 220k validators: 14962ms -&gt; 2326ms non-epoch slot (pr:nimbus#2423)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/attestation_storage.rs:40`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs#L40) CompactIndexedAttestation stores bls AggregateSignature
- [`beacon_node/operation_pool/src/attestation_storage.rs:249`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs#L249) signature.add_assign_aggregate merges points in place

**Sources.** [nimbus#2423](https://github.com/status-im/nimbus-eth2/pull/2423)

</details>


<a id="block_production-065"></a>
<details>
<summary><b>block_production-065</b> Re-run payload preparation late in prior slot — <i>implemented · medium · S · latency</i></summary>

**Idea.** Re-send payload preparation (fcU with attributes) about one second before the slot ends so the EL builds with more mempool transactions.

**Impact.** None needed; fcU with attributes is re-sent about 0.5s before slot end (and at 4s), so the EL has mempool contents up to then.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/proposer_prep_service.rs:35`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/proposer_prep_service.rs#L35) fires prepare_beacon_proposer slot_duration/3 before slot end
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:217`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L217) prepare_beacon_proposer again at slot_duration/24 before slot end
- [`beacon_node/beacon_chain/src/beacon_chain.rs:7135`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L7135) sends fcU with payload attributes

**Sources.** [grandine@cf44fbdd0](https://github.com/grandinetech/grandine/commit/cf44fbdd0df4)

</details>


<a id="block_production-067"></a>
<details>
<summary><b>block_production-067</b> Locally aggregate sync messages into block sync aggregate — <i>not · low · M · cpu</i></summary>

**Idea.** When packing the sync aggregate, aggregate individually seen sync committee messages along with received contributions (parallel per subnet), so the block includes a fuller aggregate.

**Gap in Lighthouse.** Merge non-overlapping contributions per subcommittee (aggregate bits and signatures) in insert_sync_contribution, and fold naive_sync_aggregation_pool messages for the parent root into get_sync_aggregate at production time.

**Impact.** Slightly fuller sync aggregate (a little more proposer sync reward) at some extra aggregation CPU on the proposal path; small.

**Best measured result.** aggregation 3-4x faster per subnet parallelism (pr:prysm#15608)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/lib.rs:117`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L117) insert_sync_contribution keeps only the best contribution per subcommittee, no merging
- [`beacon_node/operation_pool/src/lib.rs:163`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L163) get_sync_aggregate builds only from pool contributions
- [`beacon_node/beacon_chain/src/beacon_chain.rs:6066`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L6066) block production uses op_pool.get_sync_aggregate; naive_sync_aggregation_pool (beacon_chain.rs:428) is only used to serve contribution requests

**Sources.** [nimbus#6384](https://github.com/status-im/nimbus-eth2/pull/6384), [prysm#15608](https://github.com/OffchainLabs/prysm/pull/15608)

</details>


<a id="block_production-070"></a>
<details>
<summary><b>block_production-070</b> Request local payload and builder bid concurrently with cutoff — <i>implemented · medium · S · latency</i></summary>

**Idea.** Request the local EL payload and the external builder bid concurrently rather than sequentially, with a cutoff (~3s) after which whichever is available is used. Proposal latency becomes the max of the two, bounded by the cutoff, so a slow EL or builder does not delay the proposal.

**Gap in Lighthouse.** Small: no single shared cutoff. Each leg has its own timeout (builder 1s, getPayload 2s), so the join is bounded by about 2s. On a payload-id cache miss (lib.rs:1370), the local leg first sends forkchoiceUpdated, which has an 8s timeout.

**Impact.** Already bounded: proposal latency is the max of the two requests and each has a timeout, so a slow EL or relay cannot stall it past about 2s in the normal pre-prepared-payload case.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/execution_layer/src/lib.rs:1077`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/lib.rs#L1077) tokio::join! of builder get_builder_header and local get_full_payload_caching
- [`beacon_node/builder_client/src/pre_gloas_builder_http_client.rs:35`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/builder_client/src/pre_gloas_builder_http_client.rs#L35) DEFAULT_GET_HEADER_TIMEOUT_MILLIS = 1000 (relay cutoff, configurable via builder_header_timeout)
- [`beacon_node/execution_layer/src/engine_api/http.rs:52`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engine_api/http.rs#L52) ENGINE_GET_PAYLOAD_TIMEOUT = 2s applied to every engine_getPayload version (http.rs:988-1136)

**Second check.** The earlier gap said the local EL request had no cutoff. That is wrong: engine_getPayload has a 2s HTTP timeout, and the builder header has a 1s default. Together they give the idea's bounded concurrent fetch.

**Sources.** [nimbus#4749](https://github.com/status-im/nimbus-eth2/pull/4749), [prysm#17607](https://github.com/OffchainLabs/prysm/pull/17607), [lodestar#5223](https://github.com/ChainSafe/lodestar/pull/5223)

</details>


<a id="block_production-073"></a>
<details>
<summary><b>block_production-073</b> Fall back to P2P bid in parallel with local build — <i>implemented · low · latency</i></summary>

**Idea.** When a supplied builder bid fails validation, consider the best P2P bid in parallel with local payload production and return whichever is ready by the cutoff.

**Impact.** Already races builder/gossip bids against the local build post-Gloas.

**Best measured result.** Observed local build 3.483s; P2P fallback could return about 2.086s sooner (pr:lodestar#10212)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_production/gloas.rs:310`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_production/gloas.rs#L310) tokio::join of acquire_external_bid_candidates and local build
- [`beacon_node/beacon_chain/src/block_production/gloas.rs:1117`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_production/gloas.rs#L1117) external candidates include direct and gossip bids; failed local build falls back to external bid
- [`beacon_node/beacon_chain/src/block_production/bid_selection.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_production/bid_selection.rs) select_payload_bid ranks all candidates
- [`beacon_node/beacon_chain/src/payload_bid_verification/payload_bid_cache.rs:71`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_bid_verification/payload_bid_cache.rs#L71) get_highest_bid for gossip bids

**Sources.** [lodestar#10212](https://github.com/ChainSafe/lodestar/pull/10212)

</details>


<a id="block_production-075"></a>
<details>
<summary><b>block_production-075</b> Gossip-verify blinded block in parallel with unblinding — <i>not · medium · M · latency</i></summary>

**Idea.** When publishing a blinded block, run the gossip validity and duplicate checks concurrently with the builder unblinding (submitBlindedBlock) request instead of after it. The checks then finish before the relay's gossip copy arrives, so the block is not delayed or treated as a duplicate.

**Gap in Lighthouse.** For builder (blinded) proposals, run gossip verification and seen-block registration of the blinded block concurrently with propose_blinded_beacon_block (for example with tokio::join!), so the full block that the relay gossips takes the fast path when it arrives.

**Impact.** Saves the gossip-verification time (tens of ms) on import of the relay's copy of our own builder blocks.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/publish_blocks.rs:657`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/publish_blocks.rs#L657) publish_blinded_block calls reconstruct_block, then returns Ok(empty) for builder blocks
- [`beacon_node/http_api/src/publish_blocks.rs:734`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/publish_blocks.rs#L734) el.propose_blinded_beacon_block is awaited alone and returns Ok(None); no GossipVerifiedBlock or duplicate check runs before or alongside it

**Second check.** Read the full blinded publish path (publish_blinded_block and reconstruct_block). Only local-payload blocks go through publish_block verification. Builder blocks are only submitted to the relay, with no parallel verification.

**Sources.** [lighthouse#4647](https://github.com/sigp/lighthouse/pull/4647)

</details>


<a id="block_production-076"></a>
<details>
<summary><b>block_production-076</b> Participation overlay instead of rebuilding epoch participation — <i>partial · medium · M · cpu, latency</i></summary>

**Idea.** In the attestation packing/sorting step, do not rebuild current and previous epoch participation from the state for every proposal; keep a cached copy of on-chain participation and apply an overlay that records the mutations of candidate attestations. This removes a full participation rebuild from block production.

**Gap in Lighthouse.** The overlay half exists: max-cover covering sets work against a read-only cached BitVec. But the cache is rebuilt by a full scan of both participation lists on the first proposal after each new head, which is in practice every proposal. Build it during the state advance or update it incrementally.

**Impact.** Removes two passes over all validators (single-digit to low tens of ms) from block production; smaller than Teku's 160 ms gain because Lighthouse already avoids state copies.

**Best measured result.** Sorting init 210-221 ms -&gt; 45-57 ms (pr:teku#9660)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/reward_cache.rs:14`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/reward_cache.rs#L14) RewardCache keeps a compact BitVec of on-chain participation, reused for the same (epoch, head block)
- [`beacon_node/operation_pool/src/attestation.rs:166`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation.rs#L166) update_covering_set removes covered validators from candidates (the overlay of candidate mutations); the state is never copied or mutated
- [`beacon_node/operation_pool/src/lib.rs:370`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L370) reward_cache.update(state) runs on the proposal path
- [`beacon_node/operation_pool/src/reward_cache.rs:88`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/reward_cache.rs#L88) the full BitVec is rebuilt whenever the head block changes

**Second check.** Checked AttMaxCover: candidate mutations are already applied as an overlay, without copying participation. The only remaining cost is the per-head BitVec rebuild on the proposal path.

**Sources.** [teku#9660](https://github.com/Consensys-Incorporated/teku/pull/9660)

</details>


<a id="block_production-077"></a>
<details>
<summary><b>block_production-077</b> Score attestations by newly set participation flags — <i>implemented · medium · S · cpu</i></summary>

**Idea.** When packing attestations, score each candidate by which participation flags (source/target/head) it would newly set in the state, i.e. by its actual reward, rather than only by the count of new attester bits. This packs higher-value attestations into the limited block space.

**Gap in Lighthouse.** Only the slashable-vote corner case: a validator with some flags already set is skipped instead of being scored for the missing flags.

**Impact.** Already in place: attestations are scored by actual proposer reward from newly set flags. The remaining case needs a slashable vote, so it has almost no effect.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/attestation.rs:88`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation.rs#L88) get_attestation_participation_flag_indices computes which flags the attestation would set at this inclusion delay
- [`beacon_node/operation_pool/src/attestation.rs:112`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation.rs#L112) per-validator reward = base_reward * sum of PARTICIPATION_FLAG_WEIGHTS for those flags
- [`beacon_node/operation_pool/src/attestation.rs:182`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation.rs#L182) score() is the summed proposer reward, not the bit count
- [`beacon_node/operation_pool/src/reward_cache.rs:17`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/reward_cache.rs#L17) documents why validators with any flag set cannot gain new flags except by slashable double voting

**Second check.** The earlier gap assumed that flags could be added to a validator who already has some. That is not possible: the head flag needs delay 1 and later inclusions only lose flags, so any other route is a double vote. Lighthouse's reward-weighted scoring is therefore what the idea describes.

**Sources.** [nimbus#5468](https://github.com/status-im/nimbus-eth2/pull/5468)

</details>


<a id="block_production-079"></a>
<details>
<summary><b>block_production-079</b> Record payload ID for late-arriving blocks — <i>implemented · medium · latency</i></summary>

**Idea.** When a block arrives late and triggers a forkchoiceUpdated, still store the returned payload ID in the proposer/payload-ID cache. The proposer then reuses it instead of issuing a fresh forkchoiceUpdated at proposal time.

**Impact.** None needed; every FCU response with a payload id is cached, including those for late blocks.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/execution_layer/src/engines.rs:176`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engines.rs#L176) Engine::notify_forkchoice_updated inserts any returned payload_id into payload_id_cache keyed by head hash + attributes, regardless of caller
- [`beacon_node/execution_layer/src/lib.rs:1342`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/lib.rs#L1342) get_full_payload_with reads cache first, only sends fresh FCU on miss

**Sources.** [prysm#16563](https://github.com/OffchainLabs/prysm/pull/16563)

</details>


<a id="block_production-082"></a>
<details>
<summary><b>block_production-082</b> Do not key payload cache on safe/finalized hashes — <i>implemented · medium · latency</i></summary>

**Idea.** When looking up a cached payload-build (payload ID) at proposal time, match on head/parent, timestamp and attributes but not on the safe and finalized block hashes. A changed finalized hash then does not cause a cache miss and an extra ~500ms getPayload delay.

**Impact.** None needed; a changed finalized or safe hash does not cause a payload id miss.

**Best measured result.** avoids consistent misses and additional 500ms delays when proposing (pr:nimbus#8268)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/execution_layer/src/engines.rs:109`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engines.rs#L109) PayloadIdCacheKey is only head_block_hash + payload_attributes
- [`beacon_node/execution_layer/src/engines.rs:149`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engines.rs#L149) get_payload_id looks up with that key (no safe/finalized hash)

**Sources.** [nimbus#8268](https://github.com/status-im/nimbus-eth2/pull/8268)

</details>


<a id="block_production-083"></a>
<details>
<summary><b>block_production-083</b> Build consensus block body only once — <i>implemented · medium · cpu, memory, latency</i></summary>

**Idea.** When producing a block with both builder and local EL payloads, build the consensus body (attestation packing, slashings, exits, proposal state) once and reuse it for both, or choose the payload first and then build one block, instead of building two full blocks and comparing.

**Impact.** None needed; consensus body is built once.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:5728`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5728) produce_block_on_state builds one partial block body, awaits one payload handle, completes once
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5917`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5917) get_execution_payload started concurrently with packing; builder-vs-local choice happens inside the payload fetch (Full or Blinded contents)

**Sources.** [nimbus#7353](https://github.com/status-im/nimbus-eth2/pull/7353), [lodestar#6270](https://github.com/ChainSafe/lodestar/pull/6270)

</details>


<a id="block_production-084"></a>
<details>
<summary><b>block_production-084</b> At most one state and epoch transition per proposal — <i>implemented · medium · cpu, memory, latency</i></summary>

**Idea.** In block assembly, generate only the state at the block slot and run the epoch transition at most once, sharing it across body pieces, instead of also loading the previous-block state or recomputing the transition per piece.

**Impact.** None needed; no extra parent state load or repeated transition.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_production/mod.rs:43`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_production/mod.rs#L43) load_state_for_block_production loads one state (advanced head state from cache)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5871`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5871) complete_state_advance advances that single state once to the proposal slot; all body pieces use it

**Sources.** [lodestar#1839](https://github.com/ChainSafe/lodestar/pull/1839), [teku#4703](https://github.com/Consensys-Incorporated/teku/pull/4703)

</details>


<a id="block_production-085"></a>
<details>
<summary><b>block_production-085</b> Pre-build and sign next block before slot start — <i>n/a · medium · latency</i></summary>

**Idea.** Build and sign the next slot's block before the slot starts against the current head, then at slot start revalidate parent and justified checkpoint and publish, falling back to a fresh build on mismatch. The heavy build work leaves the slot's critical path.

**Impact.** Lighthouse does not sign blocks (the VC does, and the randao reveal exists only at slot start), and pre-building would miss attestations from the end of the previous slot; the build is cheap, so there is little to move.

**Best measured result.** block build ~1-2s moved off interval 0, near-100% pre-build hit rate (pr:ethlambda#445)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:5237`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5237) produce_block_with_verification is driven by the VC request at slot start with randao_reveal supplied by the VC
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5960`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5960) pack_attestations is a few ms op-pool selection, not a 1-2s build

**Sources.** [ethlambda#445](https://github.com/lambdaclass/ethlambda/pull/445)

</details>


<a id="block_production-089"></a>
<details>
<summary><b>block_production-089</b> Precompute attestation packing at slot start — <i>partial · medium · M · latency</i></summary>

**Idea.** At slot start, for an expected local proposer, start attestation aggregation/packing asynchronously and return the in-flight result when the block is requested, instead of starting packing when the request arrives.

**Gap in Lighthouse.** Lighthouse aggregates within a committee as attestations arrive, but the naive-pool import, cross-committee aggregation, reward cache update and max-cover packing all still start when the block is requested. Missing: a task at slot start (or at the 11.5s fork-choice/prepare_beacon_proposer point) for a known local proposer that runs these steps on the advanced head state, and a produce_partial_beacon_block path that takes the result when parent and slot match.

**Impact.** Would take cross-committee aggregation plus max-cover (tens to low hundreds of ms on mainnet) off the proposal critical path. It helps only nodes with local proposers, and the result misses attestations that arrive after the precompute.

**Best measured result.** ~580 ms async compute moved off request path (pr:teku#9122)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/attestation_storage.rs:456`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs#L456) AttestationMap::insert greedily aggregates same-committee attestations at insertion time, so that part of aggregation is already off the proposal path
- [`beacon_node/operation_pool/src/lib.rs:382`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L382) aggregate_across_committees (Electra) runs on demand inside get_attestations
- [`beacon_node/operation_pool/src/lib.rs:367`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L367) reward cache update and max-cover packing run on demand
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5943`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5943) naive aggregation pool imported into op pool at request time, then pack_attestations

**Second check.** The earlier review missed insertion-time greedy aggregation in attestation_storage.rs. That is an equivalent mechanism for part of Teku's precomputed aggregation. Packing itself is still on demand, and no precompute or cache of packing results exists.

**Sources.** [teku#9122](https://github.com/Consensys-Incorporated/teku/pull/9122)

</details>


<a id="block_production-091"></a>
<details>
<summary><b>block_production-091</b> Advance state for expected reorg parent — <i>not · medium · S · cpu, latency</i></summary>

**Idea.** At the last slot of an epoch, when the head is weak and a proposer reorg is expected, run next-slot state preparation (including the epoch transition) on the parent block instead of the head, so the transition is not redone at proposal time.

**Gap in Lighthouse.** In state_advance_timer, when the head is late or weak at the last slot of an epoch and get_proposer_head would pick the parent, also advance the parent's state to the next slot (including epoch processing) and cache it, so get_state_for_re_org finds it ready.

**Impact.** Takes an epoch transition (hundreds of ms on mainnet) off the proposal path for epoch-boundary re-orgs, which have been enabled by default since v8.2.0. The event is rare, so the average gain is small.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/state_advance_timer.rs:277`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L277) advance_head only takes head_snapshot() and advances it; no parent or re-org-target branch
- [`beacon_node/beacon_chain/src/block_production/mod.rs:257`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_production/mod.rs#L257) get_state_for_re_org takes the parent state from get_advanced_hot_state_from_cache(parent, slot); at an epoch boundary this is the parent advanced only to the weak head's slot (from the previous slot's timer)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5870`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5870) complete_state_advance at production time then runs the epoch transition inline

**Second check.** Checked advance_head, the 11.5s fork_choice_advance / prepare_beacon_proposer block, the FCR head-state advance in canonical_head.rs (not cached) and all complete/partial_state_advance call sites. None of them advances or caches the re-org parent's state.

**Sources.** [lodestar#9915](https://github.com/ChainSafe/lodestar/pull/9915)

</details>


<a id="block_production-092"></a>
<details>
<summary><b>block_production-092</b> Advance state for next slot after late blocks — <i>partial · medium · S · latency</i></summary>

**Idea.** When a late block is imported (before the attestation deadline), still run the next-slot state advance for it, so attesters and proposers of the next slot find the advanced state ready.

**Gap in Lighthouse.** Shuffling is primed at import, but the late head's state is not advanced to the next slot. The next proposal (complete_state_advance) and the next block's import still pay the slot transition inline, plus the epoch transition at boundaries. Missing: after importing a head block that arrives after the 3/4-slot advance (or in the next slot before the attestation deadline), spawn advance_head for it.

**Impact.** Avoids one per-slot transition, or an epoch transition at a boundary, on the next proposal and block-import path after late blocks. Attestation committees are already covered.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:4720`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4720) import_block_update_shuffling_cache runs for every imported block
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5216`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5216) primes Current and Next epoch committee caches (plus PTCs) from the block's post-state, so next-slot attesters and gossip verification have committees even across an epoch boundary
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:143`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L143) advance_head fires only once at 3/4 of the slot; a head imported after that point is not advanced
- [`beacon_node/beacon_chain/src/canonical_head.rs:1137`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1137) head update only reads get_advanced_hot_state, with no advance on a miss

**Second check.** The earlier review missed import-time shuffling cache priming for current and next epoch. That covers the attester and committee half of the idea. The state advance itself is still absent.

**Sources.** [grandine@06bdb7cfe](https://github.com/grandinetech/grandine/commit/06bdb7cfefe8)

</details>


<a id="block_production-094"></a>
<details>
<summary><b>block_production-094</b> Produce from in-memory head state, not store — <i>implemented · low · disk, latency</i></summary>

**Idea.** Build the block on a copy of the in-memory head state rather than loading the base state from the fork choice store or disk.

**Impact.** Production starts from a cached, pre-advanced head state, not a disk load, in the normal case; the disk path (state_at_slot) is only for non-head parents.

**Best measured result.** described as much faster (pr:caplin#13051)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_production/mod.rs:84`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_production/mod.rs#L84) get_advanced_hot_state from the state cache, filled by the state advance timer
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5877`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5877) complete_state_advance on the loaded state

**Sources.** [caplin#13051](https://github.com/erigontech/erigon/pull/13051)

</details>


<a id="block_production-098"></a>
<details>
<summary><b>block_production-098</b> Stop eth1 data voting work after deposit transition — <i>implemented · medium · S · memory, cpu</i></summary>

**Idea.** Once EIP-6110 deposit requests have taken over (eth1_deposit_index reached deposit_requests_start_index), skip eth1data voting in block production and prune the eth1 block cache, avoiding eth1 lookups and unbounded cache growth.

**Impact.** None needed: block production does no eth1 lookups and there is no eth1 block cache (eth1 service was removed).

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:5931`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5931) eth1_data copied from state, no vote
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5933`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5933) deposits = vec![] (no eth1 deposit lookup)

**Sources.** [grandine@11239f188](https://github.com/grandinetech/grandine/commit/11239f18821e), [prysm#14835](https://github.com/OffchainLabs/prysm/pull/14835)

</details>


<a id="block_production-099"></a>
<details>
<summary><b>block_production-099</b> Prune pending deposits on finalization — <i>n/a · low · cpu, memory</i></summary>

**Idea.** On finalization, prune pending deposits up to the finalized checkpoint, so proposers do not read the deposit trie for old deposits.

**Impact.** Lighthouse no longer keeps an eth1 deposit cache or reads deposits from a trie during block production (post-Electra deposit requests), so there is nothing to prune.

**Best measured result.** marked performance increase for proposing nodes (pr:prysm#12598)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:5933`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5933) deposits = vec![] (no eth1 deposit tree is read in production)

**Sources.** [prysm#12598](https://github.com/OffchainLabs/prysm/pull/12598)

</details>


<a id="block_production-100"></a>
<details>
<summary><b>block_production-100</b> Publish blob sidecars before the block — <i>partial · medium · S · latency, bandwidth</i></summary>

**Idea.** When publishing a locally produced block with blobs, publish the blob sidecars first, before block import and block publish, so they propagate while peers validate the block and are ready when peers ask.

**Gap in Lighthouse.** Fulu: columns already go out before block import, and before the block when broadcast_validation is consensus/consensus_and_equivocation; only the default gossip level puts the block on the wire first. Gloas (the current path for payload data): columns are published only after process_execution_payload_envelope returns, i.e. after envelope import/EL verification, so they trail the envelope by the full import time. Fix: publish columns right after column_build_future resolves (before or in parallel with envelope import), and in the Fulu gossip path publish columns before publish_block_p2p if they are ready.

**Impact.** Gloas: columns reach peers earlier by roughly the envelope import time (EL newPayload, tens to hundreds of ms), lowering data-availability latency for the payload; Fulu: a few ms at the default level.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/publish_blocks.rs:243`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/publish_blocks.rs#L243) column build spawned before block gossip verification
- [`beacon_node/http_api/src/publish_blocks.rs:264`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/publish_blocks.rs#L264) default (Gossip) level: block published first
- [`beacon_node/http_api/src/publish_blocks.rs:270`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/publish_blocks.rs#L270) Consensus/ConsensusAndEquivocation: block publish deferred into publish_fn
- [`beacon_node/http_api/src/publish_blocks.rs:314`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/publish_blocks.rs#L314) columns published before block import (and before the block itself at consensus levels)
- [`beacon_node/http_api/src/publish_blocks.rs:335`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/publish_blocks.rs#L335) column import precedes block import at :353
- [`common/eth2/src/types.rs:1851`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/eth2/src/types.rs#L1851) default BroadcastValidation is Gossip
- [`beacon_node/http_api/src/beacon/execution_payload_envelopes.rs:335`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/beacon/execution_payload_envelopes.rs#L335) Gloas: envelope imported first
- [`beacon_node/http_api/src/beacon/execution_payload_envelopes.rs:374`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/beacon/execution_payload_envelopes.rs#L374) Gloas: columns awaited and published (:448) only after envelope import

**Second check.** Earlier review said columns always trail the block; at consensus validation levels the block is published inside process_block after columns are sent, and in all Fulu cases columns precede import. Also checked the Gloas envelope endpoint, where columns wait for envelope import, the larger remaining gap.

**Sources.** [lodestar#6431](https://github.com/ChainSafe/lodestar/pull/6431), [prysm#14442](https://github.com/OffchainLabs/prysm/pull/14442)

</details>


<a id="block_production-110"></a>
<details>
<summary><b>block_production-110</b> Size attestation selection buffers by new attesters — <i>implemented · low · memory</i></summary>

**Idea.** In attestation packing, size per-candidate selection slices by the number of attesters with new flags, not by committee size, to avoid reserving unused memory.

**Impact.** Covering sets are sized by fresh attesters, with no committee-sized buffers.

**Best measured result.** up to ~74 MB with a full pool (pr:caplin#24798)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/attestation.rs:93`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation.rs#L93) new_for_altair_or_later collects fresh_validators_rewards via filter_map over attesting indices, skipping already-attested ones
- [`beacon_node/operation_pool/src/attestation.rs:21`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation.rs#L21) covering set is a HashMap of fresh validators only

**Sources.** [caplin#24798](https://github.com/erigontech/erigon/pull/24798)

</details>


<a id="block_production-111"></a>
<details>
<summary><b>block_production-111</b> Skip signature verification in own block state transition — <i>implemented · medium · S · cpu, latency</i></summary>

**Idea.** When computing the post-state root of a block the node itself built (and when importing that block), run the state transition with signature verification disabled, since the contents come from verified pools and the block is verified again on import.

**Impact.** None; signature batch verification is skipped when computing the post-state root of a self-built block.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:6529-6547`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L6529-L6547) per_block_processing for state root uses VerifyRandao strategy (no attestation/op signature checks)
- [`beacon_node/http_api/src/produce_block.rs:44`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/produce_block.rs#L44) NoVerification option also exists

**Sources.** [nimbus#4184](https://github.com/status-im/nimbus-eth2/pull/4184), [prysm#1434](https://github.com/OffchainLabs/prysm/pull/1434), [lodestar@f1ebe0599](https://github.com/ChainSafe/lodestar/commit/f1ebe05995fc), [teku#643](https://github.com/Consensys-Incorporated/teku/pull/643)

</details>


<a id="block_production-115"></a>
<details>
<summary><b>block_production-115</b> Skip re-hashing transactions of unblinded builder payload — <i>n/a · medium · S · cpu, latency</i></summary>

**Idea.** When unblinding a builder payload, do not re-hash its transactions to check them against the signed header root before publishing, since a mismatch cannot be recovered anyway. This removes a full transactions tree hash from the publish path.

**Impact.** Lighthouse does not unblind a builder payload itself: the builder publishes the block, so no transactions tree hash happens on the publish path.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/publish_blocks.rs:734`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/publish_blocks.rs#L734) propose_blinded_beacon_block hands blinded block to builder, which publishes it
- [`beacon_node/http_api/src/publish_blocks.rs:715`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/publish_blocks.rs#L715) local payload looked up by header tree_hash_root (header only, no transactions re-hash)

**Sources.** [lodestar#6478](https://github.com/ChainSafe/lodestar/pull/6478)

</details>


<a id="block_production-125"></a>
<details>
<summary><b>block_production-125</b> Skip reward sorting when attestations fit — <i>not · low · S · cpu, latency</i></summary>

**Idea.** When all aggregated attestations already fit under the block limit, skip building the reward-based sorter state and sorting, since order is irrelevant.

**Gap in Lighthouse.** In get_attestations, collect candidates first and, when count (non-zero score) &lt;= curr_epoch_limit/prev_epoch_limit, return them directly without the greedy loop in maximum_cover; fork-aware merge_solutions would still be needed.

**Impact.** Saves the greedy cover loop (O(limit*n) with covering-set updates) on slots where few attestations are pooled; mostly small on mainnet where the pool exceeds the limit, the per-candidate scoring still dominates.

**Best measured result.** getAttestationsForBlock 124 ms -&gt; 7 ms (pr:teku#9617)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/lib.rs:326`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L326) get_valid_attestations_for_epoch builds an AttMaxCover for every candidate
- [`beacon_node/operation_pool/src/lib.rs:428`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L428) maximum_cover always runs
- [`beacon_node/operation_pool/src/max_cover.rs:53`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/max_cover.rs#L53) maximum_cover scores and iterates even if items.len() &lt;= limit

**Sources.** [teku#9617](https://github.com/Consensys-Incorporated/teku/pull/9617)

</details>


<a id="block_production-135"></a>
<details>
<summary><b>block_production-135</b> Validate packed attestations without mutating state — <i>implemented · medium · S · cpu, memory, latency</i></summary>

**Idea.** When packing pool attestations, validate them against the state without processing them (no state mutation or copy), removing state copies from the proposer hot path.

**Impact.** None; packing validates against an immutable state reference without processing attestations or copying state.

**Best measured result.** proposal &gt;250ms seen in 50+ profiles (pr:prysm#12704)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:2739`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2739) filter_op_pool_attestation checks shuffling compatibility against &amp;state
- [`beacon_node/operation_pool/src/lib.rs:317`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L317) get_valid_attestations_for_epoch filters on slot window and takes &amp;BeaconState

**Sources.** [prysm#12704](https://github.com/OffchainLabs/prysm/pull/12704)

</details>


<a id="block_production-136"></a>
<details>
<summary><b>block_production-136</b> Do not pack attestations before tracked inclusion window — <i>not · low · S · cpu, bandwidth</i></summary>

**Idea.** After startup, do not pack attestations from slots before the first slot for which on-chain inclusion is tracked, avoiding already-included attestations, and lower the packing timeout since sorting is faster.

**Gap in Lighthouse.** Add a floor slot (first slot after startup/tracked from state) in get_valid_attestations_for_epoch to drop candidates before AttMaxCover::new; Lighthouse reads inclusion from state participation so the benefit is only avoiding scoring work.

**Impact.** Avoids scoring attestations already on chain; small CPU saving of a few ms per proposal, not the 150 ms Teku saw since Lighthouse uses state participation flags.

**Best measured result.** sorting ~150 ms faster (pr:teku#9661)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/lib.rs:327`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L327) attestations filtered only by slot window and validity filter
- [`beacon_node/operation_pool/src/attestation.rs:96`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation.rs#L96) reward_cache.has_attested_in_epoch removes already-included validators only after computing flags for each candidate

**Sources.** [teku#9661](https://github.com/Consensys-Incorporated/teku/pull/9661)

</details>


