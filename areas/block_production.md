# block_production

147 ideas: 19 not, 15 partial, 73 implemented, 40 n/a; 13 actionable (high or medium value, verdict `not` or `partial`). [Back to the summary](../README.md).

| id | idea | verdict | value | effort | resources |
|---|---|---|---|---|---|
| [block_production-001](#block_production-001) | Bounded builder header timeout with local fallback | implemented | high | S | latency |
| [block_production-002](#block_production-002) **★** | Compute block root after broadcasting proposal | not | medium | S | latency |
| [block_production-003](#block_production-003) | SSZ encoding for VC block production requests | implemented | medium | S | bandwidth, latency, cpu |
| [block_production-004](#block_production-004) | Build proposals on state pre-advanced to proposal slot | implemented | high | S | latency, cpu |
| [block_production-005](#block_production-005) | Aggregate unaggregated attestations with aggregates when packing | implemented | low | S | bandwidth, cpu |
| [block_production-006](#block_production-006) | Fully async block production without blocking joins | n/a | low |  | latency, cpu |
| [block_production-007](#block_production-007) | Attest to already-validated head without waiting | not | low | M | latency |
| [block_production-008](#block_production-008) **★** | Attester cache keyed by epoch and head root | partial | medium | S | latency |
| [block_production-009](#block_production-009) | Parse EL execution requests with direct indexing | implemented | low | S | cpu, memory |
| [block_production-010](#block_production-010) | Pick payload-attestation fork from in-memory block ref | n/a | low |  | disk, latency |
| [block_production-011](#block_production-011) | Read next-slot proposer from head state lookahead | implemented | low | S | cpu, latency |
| [block_production-012](#block_production-012) | Build sync aggregate object only when needed | implemented | low | S | memory, cpu |
| [block_production-013](#block_production-013) | Allocation-free scoring in greedy proof selection | implemented | low | S | cpu |
| [block_production-014](#block_production-014) | Reuse held head snapshot in builder health check | implemented | low | S | latency |
| [block_production-015](#block_production-015) | Pass serialized block bytes to state-root computation | n/a | low |  | cpu |
| [block_production-016](#block_production-016) **★** | Payload attributes withdrawals without cloning head state | partial | medium | S | cpu, memory, latency |
| [block_production-017](#block_production-017) | State transition over blinded blocks for state root | implemented | low | S | latency, cpu, memory |
| [block_production-018](#block_production-018) | Timeout eth1 data fetch with default vote fallback | n/a | low |  | latency |
| [block_production-019](#block_production-019) | Publish proposed or gossip-valid block before full import | implemented | high | S | latency, bandwidth |
| [block_production-020](#block_production-020) | Publish block first, blob/column sidecars afterwards | implemented | medium | S | latency, cpu, bandwidth |
| [block_production-021](#block_production-021) | Tune EL payload collection deadline within slot | not | low | M | latency |
| [block_production-022](#block_production-022) | Websocket bid stream from builders before slot | implemented | low | S | latency |
| [block_production-023](#block_production-023) | Dedupe and cancel in-flight payload builders | n/a | low |  | cpu, memory |
| [block_production-024](#block_production-024) | Resolve builder addresses off the main loop | n/a | low |  | latency |
| [block_production-025](#block_production-025) | Block value from rewards cached during state transition | not | low | M | cpu, latency |
| [block_production-026](#block_production-026) | Proposer cap on distinct AttestationData per block | n/a | low |  | cpu, latency |
| [block_production-027](#block_production-027) | Cheap block-number check before hashing builder withdrawals | partial | low | S | cpu |
| [block_production-028](#block_production-028) | Credential prefix check before balance read in withdrawals | not | low | S | cpu |
| [block_production-029](#block_production-029) | Compute payload attributes once for SSE and fcU | implemented | low | S | cpu |
| [block_production-030](#block_production-030) | Early fcU with attributes hitting cached payload ID | implemented | high | S | latency |
| [block_production-031](#block_production-031) | One merged proof per AttestationData per block | n/a | low |  | bandwidth, cpu |
| [block_production-032](#block_production-032) | Skip parent-weight check on early fcU | implemented | low | S | cpu, latency |
| [block_production-033](#block_production-033) | Yield before sync body production to process I/O | n/a | low |  | latency |
| [block_production-034](#block_production-034) | Delay post-import fcU until shortly before next slot | implemented | medium | S | latency |
| [block_production-035](#block_production-035) | Filter packed attestations by shuffling dependent root | implemented | medium | S | cpu, latency, bandwidth |
| [block_production-036](#block_production-036) | Rebuild deposit trie when too many pending | n/a | low | S | cpu |
| [block_production-037](#block_production-037) **★** | Propose with builder header without awaiting local payload | not | medium | M | latency |
| [block_production-038](#block_production-038) **★** | Drop newPayload for locally built payloads | not | medium | S | latency |
| [block_production-039](#block_production-039) | Remove previous-epoch limits in post-Altair packing | implemented | low | S | cpu |
| [block_production-040](#block_production-040) | Read proposer index from primed proposer cache | implemented | low | S | cpu, latency |
| [block_production-041](#block_production-041) | Drop subset aggregates before packing | implemented | medium | S | bandwidth |
| [block_production-042](#block_production-042) | Lower block production wait cutoff | partial | low | S | latency |
| [block_production-043](#block_production-043) | Early exit in terminal PoW block search | n/a | low | S | cpu, latency |
| [block_production-044](#block_production-044) | Skip deposit reading and packing when none due | n/a | low | S | cpu, latency, disk |
| [block_production-045](#block_production-045) **★** | Build block body in parallel with payload fetch | partial | medium | M | latency, cpu |
| [block_production-046](#block_production-046) | Fast eth1 data vote counting with early exit | n/a | low | S | cpu, latency |
| [block_production-047](#block_production-047) | Emit payload_attributes event before awaiting fcU | implemented | low | S | latency |
| [block_production-048](#block_production-048) | Track eth1 deposit sync off the proposal path | n/a | low | S | latency |
| [block_production-049](#block_production-049) | Fast retry of busy payload preparation | n/a | low |  | latency |
| [block_production-050](#block_production-050) | Compare eth1 votes by hash tree root | n/a | low |  | cpu |
| [block_production-051](#block_production-051) | Use optimized cached state transition for state root | implemented | low | S | cpu, latency |
| [block_production-052](#block_production-052) | Fill remaining block space with unaggregated attestations | implemented | low | S | bandwidth |
| [block_production-053](#block_production-053) | Filter invalid-signature attestations before sort and cap | n/a | low |  | cpu |
| [block_production-054](#block_production-054) | Finalized deposit cache with trie snapshot | n/a | low |  | cpu |
| [block_production-055](#block_production-055) | Recompute fork choice head right before building proposal | implemented | medium | S | latency |
| [block_production-056](#block_production-056) | Attestation data from fork choice store | partial | low | M | cpu, memory, latency |
| [block_production-057](#block_production-057) | Skip payload-attribute preparation when not synced | implemented | high | S | memory, cpu |
| [block_production-058](#block_production-058) | Greedy max-cover attestation selection | implemented | low | S | cpu |
| [block_production-059](#block_production-059) | Read justified checkpoints once per block | implemented | low | S | cpu, latency |
| [block_production-060](#block_production-060) | Process slots and state root once for all attestations | implemented | low | S | cpu, latency |
| [block_production-061](#block_production-061) | Compute total active balance once per block | implemented | low | S | cpu |
| [block_production-062](#block_production-062) | Inline withdrawable checks, lazily load pending withdrawals | implemented | low | S | cpu |
| [block_production-063](#block_production-063) | Separate block producer from validator message processing | n/a | low | S | latency |
| [block_production-064](#block_production-064) | Keep pool signatures in deserialized form | implemented | low | S | cpu, latency |
| [block_production-065](#block_production-065) | Re-run payload preparation late in prior slot | implemented | low | S | latency |
| [block_production-066](#block_production-066) | Fetch deposits only up to canonical eth1 height | n/a | low | S | cpu |
| [block_production-067](#block_production-067) | Locally aggregate sync messages into block sync aggregate | not | low | M | cpu |
| [block_production-068](#block_production-068) | Non-blocking fork choice state getters for producer | partial | low | M | latency, cpu |
| [block_production-069](#block_production-069) | Optimized block production path avoiding redundant state work | implemented | low | S | latency, cpu |
| [block_production-070](#block_production-070) | Request local payload and builder bid concurrently with cutoff | implemented | medium | S | latency |
| [block_production-071](#block_production-071) | Broadcast each blob sidecar in its own task | n/a | low | S | latency |
| [block_production-072](#block_production-072) | Query multiple builder URLs in parallel | not | low | M | latency |
| [block_production-073](#block_production-073) | Fall back to P2P bid in parallel with local build | implemented | low | S | latency |
| [block_production-074](#block_production-074) | Build deposits and attestations concurrently | n/a | low | S | latency |
| [block_production-075](#block_production-075) **★** | Gossip-verify blinded block in parallel with unblinding | not | medium | M | latency |
| [block_production-076](#block_production-076) **★** | Participation overlay instead of rebuilding epoch participation | partial | medium | M | cpu, latency |
| [block_production-077](#block_production-077) | Score attestations by newly set participation flags | implemented | medium | S | cpu |
| [block_production-078](#block_production-078) | VC passes selected bid to beacon node producer | not | low | L | latency, bandwidth |
| [block_production-079](#block_production-079) | Record payload ID for late-arriving blocks | implemented | medium | S | latency |
| [block_production-080](#block_production-080) | Reuse live payload builder after head flips (ePBS) | implemented | low | S | latency, cpu |
| [block_production-081](#block_production-081) **★** | Re-trigger payload preparation on payload reveal/PTC verdict | partial | medium | S | latency |
| [block_production-082](#block_production-082) | Do not key payload cache on safe/finalized hashes | implemented | medium | S | latency |
| [block_production-083](#block_production-083) | Build consensus block body only once | implemented | medium | S | cpu, memory, latency |
| [block_production-084](#block_production-084) | At most one state and epoch transition per proposal | implemented | medium | S | cpu, memory, latency |
| [block_production-085](#block_production-085) | Pre-build and sign next block before slot start | n/a | medium |  | latency |
| [block_production-086](#block_production-086) | Clone head state shortly before proposal | implemented | low | S | latency |
| [block_production-087](#block_production-087) | Gossip pre-merged candidate block bodies from non-proposers | n/a | low |  | cpu, latency |
| [block_production-088](#block_production-088) | Proposal state with warm tree-hash cache | implemented | low | S | cpu, latency |
| [block_production-089](#block_production-089) **★** | Precompute attestation packing at slot start | partial | medium | M | latency |
| [block_production-090](#block_production-090) | Prefill shuffling cache before attestation packing | implemented | low | S | latency, cpu |
| [block_production-091](#block_production-091) **★** | Advance state for expected reorg parent | not | medium | S | cpu, latency |
| [block_production-092](#block_production-092) **★** | Advance state for next slot after late blocks | partial | medium | S | latency |
| [block_production-093](#block_production-093) | Cache produced block per slot for duplicate requests | not | low | S | cpu, latency |
| [block_production-094](#block_production-094) | Produce from in-memory head state, not store | implemented | low | S | disk, latency |
| [block_production-095](#block_production-095) | Proposer reorg of late weak head | implemented | low | S | latency |
| [block_production-096](#block_production-096) | Keep proposer signature outside aggregated attestation proof | n/a | low |  | cpu, latency |
| [block_production-097](#block_production-097) | Pack single best proof per data, no merging | n/a | low |  | cpu, latency |
| [block_production-098](#block_production-098) | Stop eth1 data voting work after deposit transition | implemented | medium | S | memory, cpu |
| [block_production-099](#block_production-099) | Prune pending deposits on finalization | n/a | low |  | cpu, memory |
| [block_production-100](#block_production-100) **★** | Publish blob sidecars before the block | partial | medium | S | latency, bandwidth |
| [block_production-101](#block_production-101) | Remove builder status check from proposal path | implemented | low | S | latency |
| [block_production-102](#block_production-102) | Drop duplicate pool deletion in proposal | implemented | low | S | cpu |
| [block_production-103](#block_production-103) | No proposer preparation from validator registration | implemented | low | S | cpu |
| [block_production-104](#block_production-104) | Single-pass committee bits for Electra on-chain aggregates | implemented | low | S | cpu |
| [block_production-105](#block_production-105) | No separate speculative advanced head state | implemented | low | S | memory, cpu |
| [block_production-106](#block_production-106) | Keep recent payload envelopes in memory | partial | low | S | disk, latency |
| [block_production-107](#block_production-107) | Reuse cached expected withdrawals in production | not | low | S | cpu |
| [block_production-108](#block_production-108) | Share body merkle branch across blob sidecar proofs | n/a | low | S | cpu, latency |
| [block_production-109](#block_production-109) | Single endpoint choosing blinded or full block | implemented | low | S | latency, bandwidth |
| [block_production-110](#block_production-110) | Size attestation selection buffers by new attesters | implemented | low | S | memory |
| [block_production-111](#block_production-111) | Skip signature verification in own block state transition | implemented | medium | S | cpu, latency |
| [block_production-112](#block_production-112) | Skip bid wait when no builders or bids | implemented | low | S | latency |
| [block_production-113](#block_production-113) | Skip blob sidecar construction after PeerDAS | implemented | low | S | cpu, latency |
| [block_production-114](#block_production-114) | Skip builder for unregistered validators | not | low | S | latency |
| [block_production-115](#block_production-115) | Skip re-hashing transactions of unblinded builder payload | n/a | medium | S | cpu, latency |
| [block_production-116](#block_production-116) | No deep copies in block-under-construction setters | n/a | low | S | cpu, memory |
| [block_production-117](#block_production-117) | Skip boosted value math at default boost factor | partial | low | S | cpu |
| [block_production-118](#block_production-118) | Build blocks directly from grouped aggregated payloads | n/a | low | S | cpu |
| [block_production-119](#block_production-119) | Skip per-slot proposer state load without proposers | implemented | low | S | cpu, memory |
| [block_production-120](#block_production-120) | Skip re-verifying pool operation signatures when packing | implemented | low | S | cpu, latency |
| [block_production-121](#block_production-121) | Skip duplicate sidecar publish after blinded submission | implemented | low | S | bandwidth |
| [block_production-122](#block_production-122) | Skip signature checks for self-signed messages | not | low | M | cpu |
| [block_production-123](#block_production-123) | Skip repacking operations after an earlier failure | n/a | low | S | cpu |
| [block_production-124](#block_production-124) | Ignore unaggregated attestations when packing blocks | n/a | low | S | cpu, latency |
| [block_production-125](#block_production-125) | Skip reward sorting when attestations fit | not | low | S | cpu, latency |
| [block_production-126](#block_production-126) | Sort aggregates by size before packing | implemented | low | S | cpu |
| [block_production-127](#block_production-127) | Split max-cover per epoch and run parallel | implemented | low | S | cpu, latency |
| [block_production-128](#block_production-128) | Advance head state more than one slot | implemented | medium | S | cpu, latency |
| [block_production-129](#block_production-129) | Lead-time cutoff for speculative state work | n/a | low |  | cpu, latency |
| [block_production-130](#block_production-130) | Stop deposit packing at per-block maximum | n/a | low |  | cpu |
| [block_production-131](#block_production-131) | Stop adding proofs once data has supermajority | n/a | low |  | cpu, latency |
| [block_production-132](#block_production-132) | Tiered greedy attestation selection, one state transition | n/a | low |  | cpu, latency |
| [block_production-133](#block_production-133) | Release locks early in block production | implemented | low | S | latency |
| [block_production-134](#block_production-134) | Timeout headroom for event-loop lag | n/a | low |  | latency |
| [block_production-135](#block_production-135) | Validate packed attestations without mutating state | implemented | medium | S | cpu, memory, latency |
| [block_production-136](#block_production-136) | Do not pack attestations before tracked inclusion window | not | low | S | cpu, bandwidth |
| [block_production-137](#block_production-137) | Weighted attestation ranking by count, delay, diversity | partial | low | Add tie-break terms in AttMaxCover::score / max_cover selection. | cpu |
| [block_production-138](#block_production-138) | Proposer delays request for more builder bids | not | low | Add optional sleep before get_header in execution_layer builder fetch, clamped to attestation deadline. | latency |
| [block_production-139](#block_production-139) | Return early from proposer reorg logic when disabled | implemented | low | S | cpu |
| [block_production-140](#block_production-140) | Poll fork choice within slot to refresh head | n/a | low |  | latency |
| [block_production-141](#block_production-141) | Pack operations in place on one scratch state | implemented | low | S | cpu, latency |
| [block_production-142](#block_production-142) | Return execution payload envelope with produced block | implemented | low | S | latency |
| [block_production-143](#block_production-143) | Reuse cached getPayload response for envelope and sidecars | implemented | low | S | cpu, latency |
| [block_production-144](#block_production-144) | Read parent block hash directly from state header | implemented | low | S | cpu |
| [block_production-145](#block_production-145) | Prepare payload only for local proposers | implemented | low | S | cpu, latency |
| [block_production-146](#block_production-146) | Check sync aggregate validity before PTC aggregation | n/a | low |  | cpu |
| [block_production-147](#block_production-147) | Builder bid carries only blob KZG commitments | implemented | low | S | bandwidth, latency |

★ actionable. Click an id for the full record.

## Ideas

<a id="block_production-001"></a>
<details>
<summary><b>block_production-001</b> Bounded builder header timeout with local fallback — <i>implemented · high · S · latency</i></summary>

**Idea.** Put a hard, short (configurable) timeout on the builder getHeader request during block production and fall back to the locally built payload when it expires, so a slow relay cannot delay the proposal.

**Impact.** None. A slow relay is cut off at the timeout, and production falls back to the local payload fetched at the same time.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/builder_client/src/pre_gloas_builder_http_client.rs:35`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/builder_client/src/pre_gloas_builder_http_client.rs#L35),46-48,396 get_builder_header uses the get_header timeout (default 1000ms)
- [`beacon_node/src/cli.rs:963-975`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/cli.rs#L963-L975) --builder-header-timeout configurable
- [`beacon_node/execution_layer/src/lib.rs:1056-1093`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/lib.rs#L1056-L1093) fetch_builder_and_local_payloads joins builder and local payload, so a timeout yields the local payload

**Skeptic check.** Verified the timeout on the getHeader request and the concurrent local fetch with fallback. Gloas uses p2p bids, so the relay path does not apply there.

**Verdict history.** implemented (checked) → implemented (skeptic)

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

**Verdict history.** not (checked) → not (refuted)

**Sources.** [prysm#12504](https://github.com/OffchainLabs/prysm/pull/12504)

</details>


<a id="block_production-003"></a>
<details>
<summary><b>block_production-003</b> SSZ encoding for VC block production requests — <i>implemented · medium · S · bandwidth, latency, cpu</i></summary>

**Idea.** Have the validator client request and receive produced blocks as SSZ instead of JSON by default, avoiding JSON encode/decode cost and payload size for large blocks with blobs.

**Impact.** None. The VC requests and publishes blocks and envelopes as SSZ by default, with a JSON fallback.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/block_service.rs:707-762`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/block_service.rs#L707-L762) post_validator_blocks_v4_ssz with a JSON fallback
- [`validator_client/validator_services/src/block_service.rs:787-836`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/block_service.rs#L787-L836) get_validator_blocks_v3_ssz with a JSON fallback
- [`validator_client/validator_services/src/block_service.rs:1110`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/block_service.rs#L1110),1124 blocks published as SSZ

**Skeptic check.** Confirmed SSZ is the default for produce and publish, including Gloas envelopes (block_service.rs:960,1004). The earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#7727](https://github.com/sigp/lighthouse/pull/7727)

</details>


<a id="block_production-004"></a>
<details>
<summary><b>block_production-004</b> Build proposals on state pre-advanced to proposal slot — <i>implemented · high · S · latency, cpu</i></summary>

**Idea.** Advance the head state to the proposal slot (slot and epoch processing, including any epoch transition) before the slot starts, cache it, and have block production clone that state and run only process_block on it, passing the known state root. This removes process_slots/epoch processing from the proposal critical path.

**Impact.** None on the normal path. Only the rare path that conflicts with head (state_at_slot, mod.rs:105) does a full advance, and the code logs a warning on that path.

**Best measured result.** Pyrmont block production ~550ms -&gt; ~150ms (pr:lighthouse#2241)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/state_advance_timer.rs:258-343`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L258-L343),455 advance_head pre-advances the head state to the next slot and caches it
- [`beacon_node/beacon_chain/src/block_production/mod.rs:84-98`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_production/mod.rs#L84-L98) continuation path uses get_advanced_hot_state with a known state_root
- [`beacon_node/beacon_chain/src/block_production/mod.rs:259`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_production/mod.rs#L259) re-org path uses get_advanced_hot_state_from_cache
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5870`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5870) complete_state_advance is a no-op when the state is already at the slot

**Skeptic check.** Verified that both the continuation and re-org production paths load pre-advanced cached states, so production runs only process_block. The earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#7518](https://github.com/status-im/nimbus-eth2/pull/7518), [teku#9787](https://github.com/Consensys-Incorporated/teku/pull/9787), [lodestar@3c3662ce2](https://github.com/ChainSafe/lodestar/commit/3c3662ce28d9), [nimbus#4185](https://github.com/status-im/nimbus-eth2/pull/4185), [lighthouse#2241](https://github.com/sigp/lighthouse/pull/2241), [teku#3266](https://github.com/Consensys-Incorporated/teku/pull/3266), [lodestar@a8385b3c3](https://github.com/ChainSafe/lodestar/commit/a8385b3c3184), [teku#2814](https://github.com/Consensys-Incorporated/teku/pull/2814)

</details>


<a id="block_production-005"></a>
<details>
<summary><b>block_production-005</b> Aggregate unaggregated attestations with aggregates when packing — <i>implemented · low · S · bandwidth, cpu</i></summary>

**Idea.** When packing a block, pack aggregated and unaggregated pool attestations from one combined list, aggregating singles (e.g. previous slot) into matching aggregates before selection. The block carries fewer, denser attestations and more duplicates are removed.

**Impact.** None. Singles merge into disjoint aggregates in one combined list before max-cover selection.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:5941-5961`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5941-L5961) naive aggregation pool imported into op pool before packing
- [`beacon_node/beacon_chain/src/block_production/gloas.rs:436-444`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_production/gloas.rs#L436-L444) same on the Gloas path
- [`beacon_node/operation_pool/src/attestation_storage.rs:457-482`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs#L457-L482) AttestationMap::insert greedily aggregates into existing aggregates
- [`beacon_node/operation_pool/src/attestation_storage.rs:485`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs#L485) aggregate_across_committees for Electra and later

**Skeptic check.** Verified the import and greedy merge on both the pre-Gloas and the Gloas production paths. Singles are available only for subnets the node subscribes to, and that limit applies equally to the source clients.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#6919](https://github.com/OffchainLabs/prysm/pull/6919), [teku#9197](https://github.com/Consensys-Incorporated/teku/pull/9197), [prysm#9683](https://github.com/OffchainLabs/prysm/pull/9683)

</details>


<a id="block_production-006"></a>
<details>
<summary><b>block_production-006</b> Fully async block production without blocking joins — <i>n/a · low · latency, cpu</i></summary>

**Idea.** Remove blocking join()/wait calls on the block creation path and compose it as async futures, so worker threads are not parked while waiting on dependencies.

**Impact.** Rust/tokio design has no blocking join of futures on worker threads in block creation; nothing to gain.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:6055`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L6055) produce path is async fn on tokio, no JVM-style join()

**Sources.** [teku#5572](https://github.com/Consensys-Incorporated/teku/pull/5572)

</details>


<a id="block_production-007"></a>
<details>
<summary><b>block_production-007</b> Attest to already-validated head without waiting — <i>not · low · M · latency</i></summary>

**Idea.** When producing attestations, use the head block that is already known valid instead of waiting for further validation, so attestations are produced earlier.

**Gap in Lighthouse.** Nimbus keeps a lastValidAttestedBlock and attests to it when the EL is not synced. Lighthouse has no such fallback; it would need to store the last non-optimistic head in produce_unaggregated_attestation and use it when the head is optimistic.

**Impact.** Only an availability gain when the EL is syncing or offline; no mainnet speed gain, so rare.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:2010`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2010) produce_unaggregated_attestation uses early_attester_cache then head_snapshot
- [`beacon_node/http_api/src/validator/mod.rs:259-295`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validator/mod.rs#L259-L295) attestation_data only gated by not_while_syncing, no last-valid-head fallback

**Sources.** [nimbus#5313](https://github.com/status-im/nimbus-eth2/pull/5313)

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

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [lighthouse#2478](https://github.com/sigp/lighthouse/pull/2478), [caplin#9728](https://github.com/erigontech/erigon/pull/9728)

</details>


<a id="block_production-009"></a>
<details>
<summary><b>block_production-009</b> Parse EL execution requests with direct indexing — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** When decoding execution requests returned by the EL, check lengths first and index directly instead of building intermediate per-type lists, avoiding O(n) allocation.

**Impact.** Only a per-request hex::decode allocation remains, negligible.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/execution_layer/src/engine_api/json_structures.rs:582`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engine_api/json_structures.rs#L582) parse_execution_requests: one pass, prefix and ordering checks, decode straight into typed struct field

**Skeptic check.** Verified the single-pass decode with no intermediate per-type lists. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#6822](https://github.com/status-im/nimbus-eth2/pull/6822)

</details>


<a id="block_production-010"></a>
<details>
<summary><b>block_production-010</b> Pick payload-attestation fork from in-memory block ref — <i>n/a · low · disk, latency</i></summary>

**Idea.** When producing a payload attestation, derive the fork from the in-memory block reference slot rather than loading the full block from the database.

**Impact.** Payload attestation is a Gloas feature; the fork comes from the slot/spec, not a DB block load, and it is rare.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:7993`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L7993) only is_healthy_pre_gloas; payload attestation production is Gloas-only and not on a hot path in unstable

**Sources.** [nimbus#8349](https://github.com/status-im/nimbus-eth2/pull/8349)

</details>


<a id="block_production-011"></a>
<details>
<summary><b>block_production-011</b> Read next-slot proposer from head state lookahead — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Post-Fulu, read the next-slot proposer index from the head state's proposer lookahead instead of advancing a state through the epoch transition just to learn it, and build the prepared next-slot state only once.

**Impact.** None: the next-slot proposer comes from the proposer cache. On a miss the cache is filled from a clone of the head state, and no epoch transition runs, because post-Fulu ensure_state_can_determine_proposers_for_epoch accepts a state from epoch N-1.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:1655`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L1655)
- [`consensus/types/src/state/beacon_state.rs:1681`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L1681)
- [`beacon_node/beacon_chain/src/beacon_proposer_cache.rs:201`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_proposer_cache.rs#L201)
- [`beacon_node/beacon_chain/src/beacon_proposer_cache.rs:330`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_proposer_cache.rs#L330)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5309`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5309)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5341`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5341)

**Skeptic check.** Verified that get_pre_payload_attributes fills with_proposer_cache from the head state. The minimum_epoch post-Fulu is N-1, so partial_state_advance is skipped and get_beacon_proposer_indices slices proposer_lookahead. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#9762](https://github.com/ChainSafe/lodestar/pull/9762), [nimbus#8600](https://github.com/status-im/nimbus-eth2/pull/8600)

</details>


<a id="block_production-012"></a>
<details>
<summary><b>block_production-012</b> Build sync aggregate object only when needed — <i>implemented · low · S · memory, cpu</i></summary>

**Idea.** Avoid constructing an empty sync aggregate on every block creation; create it lazily only when the block needs it.

**Impact.** None left; SyncAggregate::new() is built only in the unwrap_or_else fallback when the op pool has no contributions, and Base states get None.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:6063-6078`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L6063-L6078)

**Skeptic check.** Verified in produce_partial_beacon_block: the empty aggregate is built lazily on the fallback path only. Earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#4528](https://github.com/Consensys-Incorporated/teku/pull/4528)

</details>


<a id="block_production-013"></a>
<details>
<summary><b>block_production-013</b> Allocation-free scoring in greedy proof selection — <i>implemented · low · S · cpu</i></summary>

**Idea.** In greedy aggregate/proof selection, count newly covered validators without allocating per candidate and materialize the covered set only for the winning pick.

**Impact.** Negligible. Each iteration allocates only when it clones the winner (max_cover.rs:84). Scoring sums the values in place, and losing candidates shrink by retain.

**Best measured result.** Removes N-1 allocations per iteration (no timings) (pr:ethlambda#254)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/max_cover.rs:73-97`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/max_cover.rs#L73-L97)
- [`beacon_node/operation_pool/src/attestation.rs:180-188`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation.rs#L180-L188)
- [`beacon_node/operation_pool/src/attestation.rs:190-192`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation.rs#L190-L192)

**Skeptic check.** Verified that maximum_cover scores candidates by score() with no allocation, clones only the best pick, and that update_covering_set uses retain. This matches the idea. The up-front HashMap per candidate is a separate cost.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [ethlambda#254](https://github.com/lambdaclass/ethlambda/pull/254)

</details>


<a id="block_production-014"></a>
<details>
<summary><b>block_production-014</b> Reuse held head snapshot in builder health check — <i>implemented · low · S · latency</i></summary>

**Idea.** In the builder/chain health check during block production, reuse the head snapshot already obtained instead of taking the canonical head lock a second time.

**Impact.** None left; is_healthy_pre_gloas takes cached_head() once and reuses it for head hash, head slot and finalized checkpoint.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:7993-8030`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L7993-L8030)

**Skeptic check.** Verified that one cached_head snapshot is reused throughout. The only other lock is a fork_choice read lock for the parent execution status, which is a different data source. Earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#4323](https://github.com/sigp/lighthouse/pull/4323)

</details>


<a id="block_production-015"></a>
<details>
<summary><b>block_production-015</b> Pass serialized block bytes to state-root computation — <i>n/a · low · cpu</i></summary>

**Idea.** When computing the post-state root of a produced block with a transition that consumes raw bytes, pass the already-serialized block instead of serializing and deserializing it again.

**Impact.** Lighthouse state transition is native Rust on the typed block; no raw-bytes binding boundary exists.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:6542`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L6542) per_block_processing takes the typed block, no serialize/deserialize round trip

**Sources.** [lodestar#9945](https://github.com/ChainSafe/lodestar/pull/9945)

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

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [lighthouse#4027](https://github.com/sigp/lighthouse/pull/4027), [caplin#11997](https://github.com/erigontech/erigon/pull/11997)

</details>


<a id="block_production-017"></a>
<details>
<summary><b>block_production-017</b> State transition over blinded blocks for state root — <i>implemented · low · S · latency, cpu, memory</i></summary>

**Idea.** Let the state transition accept blinded blocks so the post-state root of a blinded proposal is computed without constructing a fake full execution payload or extra block copies.

**Impact.** None left; per_block_processing runs on the BlindedPayload block directly, with no fake full payload.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:6100-6104`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L6100-L6104)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5810-5822`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5810-L5822)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:6542-6551`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L6542-L6551)
- [`consensus/state_processing/src/per_block_processing.rs:116`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing.rs#L116)

**Skeptic check.** complete_partial_beacon_block is generic over AbstractExecPayload, and the builder path calls it with blinded contents and returns BeaconBlockResponseWrapper::Blinded. Earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#7396](https://github.com/status-im/nimbus-eth2/pull/7396)

</details>


<a id="block_production-018"></a>
<details>
<summary><b>block_production-018</b> Timeout eth1 data fetch with default vote fallback — <i>n/a · low · latency</i></summary>

**Idea.** Put a short timeout on eth1 data retrieval during block production and fall back to a default vote, so a slow eth1 endpoint cannot delay the proposal.

**Impact.** No eth1 endpoint is queried at block production; the vote is copied from state, so no fetch can stall a proposal.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:5931`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5931) eth1_data cloned from state
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5933`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5933) deposits = vec![]
- beacon_node/ has no eth1 service crate

**Sources.** [prysm#5583](https://github.com/OffchainLabs/prysm/pull/5583)

</details>


<a id="block_production-019"></a>
<details>
<summary><b>block_production-019</b> Publish proposed or gossip-valid block before full import — <i>implemented · high · S · latency, bandwidth</i></summary>

**Idea.** Broadcast a block (and its blobs) as soon as gossip/consensus validation passes, in parallel with or before full import (DB write, fork choice), instead of only after import completes, so propagation starts earlier.

**Impact.** On the default path the block propagates right after gossip verification, before process_block, the DB write and fork choice. This is true for both HTTP-published blocks and gossip-relayed blocks.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/publish_blocks.rs:244-266`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/publish_blocks.rs#L244-L266)
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1661`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1661)
- [`common/eth2/src/types.rs:1851-1852`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/eth2/src/types.rs#L1851-L1852)

**Skeptic check.** Verified that BroadcastValidation defaults to Gossip and that publish_block_p2p runs before the columns and the import. Gossip blocks get MessageAcceptance::Accept before import. The Consensus levels wait for import by design.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus@850eece94](https://github.com/status-im/nimbus-eth2/commit/850eece949fe), [nimbus#3156](https://github.com/status-im/nimbus-eth2/pull/3156), [teku#8728](https://github.com/Consensys-Incorporated/teku/pull/8728), [teku#7371](https://github.com/Consensys-Incorporated/teku/pull/7371), [prysm#13380](https://github.com/OffchainLabs/prysm/pull/13380)

</details>


<a id="block_production-020"></a>
<details>
<summary><b>block_production-020</b> Publish block first, blob/column sidecars afterwards — <i>implemented · medium · S · latency, cpu, bandwidth</i></summary>

**Idea.** On proposal, publish the block to the network immediately without waiting on sidecars, then compute/broadcast the blob or data column sidecars (KZG cell proofs) concurrently afterwards. The block leaves sooner and low-upload nodes do not delay it behind sidecar uploads.

**Impact.** With the default Gossip validation, the block is published without waiting for the sidecar build. The sidecar build is spawned at the same time on a blocking task, and the columns are awaited and published afterwards.

**Best measured result.** avg wait 18.04 ms vs 23.48 ms over 2000 holesky blocks (pr:teku#8868)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/publish_blocks.rs:241-242`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/publish_blocks.rs#L241-L242)
- [`beacon_node/http_api/src/publish_blocks.rs:248-266`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/publish_blocks.rs#L248-L266)
- [`beacon_node/http_api/src/publish_blocks.rs:294-321`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/publish_blocks.rs#L294-L321)

**Skeptic check.** Verified the order: spawn_build_data_sidecar_task, then gossip-verify the block, then publish_block_p2p, then await build_sidecar_task_handle, then publish_column_sidecars. At the Consensus levels the block is published only after import, as those levels require.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#15720](https://github.com/OffchainLabs/prysm/pull/15720), [prysm#15719](https://github.com/OffchainLabs/prysm/pull/15719), [teku#8868](https://github.com/Consensys-Incorporated/teku/pull/8868), [grandine@c6d914c9c](https://github.com/grandinetech/grandine/commit/c6d914c9c334), [grandine#844](https://github.com/grandinetech/grandine/pull/844)

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


<a id="block_production-022"></a>
<details>
<summary><b>block_production-022</b> Websocket bid stream from builders before slot — <i>implemented · low · S · latency</i></summary>

**Idea.** Open a streaming connection to each builder shortly before the slot so builders push improving bids and the proposer uses the latest at production time, instead of request/response bid fetches.

**Impact.** Opt-in streaming of Gloas direct-builder bids. Streams open at proposer prep (open_builder_bid_streams), and production falls back to HTTP. The pre-Gloas mev-boost path has no streaming, but that path is outside the scope of the source PR.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/builder_client/src/bid_streams.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/builder_client/src/bid_streams.rs)
- [`beacon_node/builder_client/src/builders.rs:172-215`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/builder_client/src/builders.rs#L172-L215)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:6903-6915`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L6903-L6915)
- [`beacon_node/src/cli.rs:1526`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/cli.rs#L1526)

**Skeptic check.** The source is Lighthouse's own PR #10418, and the mechanism is present: streams open in prepare_beacon_proposer and are consumed in bid_for_entry. Off by default (--builder-bid-streaming).

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#10418](https://github.com/sigp/lighthouse/pull/10418)

</details>


<a id="block_production-023"></a>
<details>
<summary><b>block_production-023</b> Dedupe and cancel in-flight payload builders — <i>n/a · low · cpu, memory</i></summary>

**Idea.** Key in-flight local payload builds by target timestamp with cancellable contexts, so duplicate requests share one builder and discarded builders release resources immediately.

**Impact.** Lighthouse uses an external EL that builds payloads; it only caches payload ids, so there is no in-process builder to dedupe or cancel.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/execution_layer/src/engines.rs:149`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engines.rs#L149) payload_id cache keyed by parent hash and attributes
- [`beacon_node/execution_layer/src/lib.rs:1342`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/lib.rs#L1342) reuse cached payload id

**Sources.** [caplin#23272](https://github.com/erigontech/erigon/pull/23272)

</details>


<a id="block_production-024"></a>
<details>
<summary><b>block_production-024</b> Resolve builder addresses off the main loop — <i>n/a · low · latency</i></summary>

**Idea.** Perform DNS/network resolution of builder endpoints on a separate thread so lookups never block the main processing loop.

**Impact.** Builder requests go through async reqwest/tokio; DNS runs off the async worker threads, so nothing blocks a main loop.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/builder_client/src/builder_http_client.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/builder_client/src/builder_http_client.rs) reqwest client, async

**Sources.** [silver#435](https://github.com/gattaca-com/silver/pull/435)

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


<a id="block_production-026"></a>
<details>
<summary><b>block_production-026</b> Proposer cap on distinct AttestationData per block — <i>n/a · low · cpu, latency</i></summary>

**Idea.** On the proposer side, cap the number of distinct AttestationData packed per block below the consensus maximum to bound build and proof-merge cost, while still accepting larger blocks.

**Impact.** Lean/leanSpec design with proofs per AttestationData; Lighthouse blocks have aggregated attestations bounded by the consensus max.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/lib.rs:414`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L414) packing bounded by MaxAttestations

**Sources.** [ethlambda#486](https://github.com/lambdaclass/ethlambda/pull/486)

</details>


<a id="block_production-027"></a>
<details>
<summary><b>block_production-027</b> Cheap block-number check before hashing builder withdrawals — <i>partial · low · S · cpu</i></summary>

**Idea.** Validate the builder payload's block number against the expected value before hashing its withdrawals, rejecting mismatches early.

**Gap in Lighthouse.** verify_builder_bid computes the withdrawals tree hash and verifies the BLS signature before any cheap field check. Reorder so the cheap checks (parent hash, randao, timestamp, block number) run first and the hash and signature are lazy.

**Impact.** Saves about 1 ms of BLS verify plus a small hash, only on bids that are invalid; honest builders pass all checks anyway.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/execution_layer/src/lib.rs:2022`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/lib.rs#L2022) signature verified before the other checks
- [`beacon_node/execution_layer/src/lib.rs:2031`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/lib.rs#L2031) expected withdrawals root hashed eagerly
- [`beacon_node/execution_layer/src/lib.rs:2057`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/lib.rs#L2057) block number check comes later

**Sources.** [prysm#13224](https://github.com/OffchainLabs/prysm/pull/13224)

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
<summary><b>block_production-029</b> Compute payload attributes once for SSE and fcU — <i>implemented · low · S · cpu</i></summary>

**Idea.** Compute payload attributes (withdrawals, gas limit) once and reuse them for both the payload_attributes SSE event and the EL forkchoiceUpdated call.

**Impact.** Already done: prepare_beacon_proposer computes the attributes once (or reads them from the EL cache) and passes the same value to the SSE event. The fcU reads it from the insert_proposer cache.

**Best measured result.** best case 6.2us, worst case 2.8ms per run; PR calls it a cleanup, not a perf improvement (pr:lodestar#10056)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:6954`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L6954)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:7033-7055`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L7033-L7055)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:7088-7103`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L7088-L7103)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:7133-7139`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L7133-L7139)

**Skeptic check.** Verified that the withdrawals are computed only on a cache miss, that a single PayloadAttributes value is inserted and then moved into the SSE event, and that update_execution_engine_forkchoice uses the cached entry.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#10056](https://github.com/ChainSafe/lodestar/pull/10056)

</details>


<a id="block_production-030"></a>
<details>
<summary><b>block_production-030</b> Early fcU with attributes hitting cached payload ID — <i>implemented · high · S · latency</i></summary>

**Idea.** Before the slot of a known local proposer (at a proportional point in the prior slot, and again on head change), send forkchoiceUpdated with payload attributes to the EL and cache the returned payload ID keyed by head/parent, with attributes and fork detection matching those used at getPayload time. Block production then calls getPayload with the cached ID at once instead of building a payload last-minute.

**Impact.** Implemented as Lighthouse's own feature (lighthouse#3043, #4703). The cached payload ID is hit at getPayload time.

**Best measured result.** shaved 0.5s off block production in minimal-preset testnets (pr:nimbus#7986)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/state_advance_timer.rs:212-217`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L212-L217)
- [`beacon_node/beacon_chain/src/canonical_head.rs:1931`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1931)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:7126-7139`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L7126-L7139)
- [`beacon_node/execution_layer/src/engines.rs:149-181`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engines.rs#L149-L181)
- [`beacon_node/execution_layer/src/lib.rs:1342-1350`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/lib.rs#L1342-L1350)

**Skeptic check.** Verified that the fcU with attributes is sent within prepare_payload_lookahead, from the state advance timer and on head change. The Engine payload_id_cache is keyed by (head hash, attributes), and get_full_payload_with checks it before it sends a fallback fcU.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#4703](https://github.com/sigp/lighthouse/pull/4703), [lodestar#4446](https://github.com/ChainSafe/lodestar/pull/4446), [nimbus#7986](https://github.com/status-im/nimbus-eth2/pull/7986), [prysm#10481](https://github.com/OffchainLabs/prysm/pull/10481), [lighthouse#3043](https://github.com/sigp/lighthouse/pull/3043), [lodestar#4209](https://github.com/ChainSafe/lodestar/pull/4209), [prysm#10803](https://github.com/OffchainLabs/prysm/pull/10803), [caplin#23399](https://github.com/erigontech/erigon/pull/23399)

</details>


<a id="block_production-031"></a>
<details>
<summary><b>block_production-031</b> One merged proof per AttestationData per block — <i>n/a · low · bandwidth, cpu</i></summary>

**Idea.** When building, aggregate/merge the proofs and bits of duplicate AttestationData so each appears once per block under a proof-count cap; on import reject duplicates with a cheap hash-set check before signature verification. Fewer proofs means smaller blocks and less downstream processing.

**Impact.** Concerns merged lean proofs per AttestationData; Lighthouse already aggregates per AttestationData in the op pool and has no proofs.

**Best measured result.** "reducing block size and simplifying downstream processing" (pr:ethlambda#258)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/lib.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs) max-cover packing of aggregates

**Sources.** [ethlambda#258](https://github.com/lambdaclass/ethlambda/pull/258), [ethlambda#284](https://github.com/lambdaclass/ethlambda/pull/284)

</details>


<a id="block_production-032"></a>
<details>
<summary><b>block_production-032</b> Skip parent-weight check on early fcU — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** For early proposer forkchoiceUpdated calls, skip the parent-weight (reorg) check until current attestations are imported, so the EL does not build a payload that is later discarded.

**Impact.** The head-weak and parent-strong thresholds apply only when the fork choice slot equals the re-org slot. That happens after recompute_head_at_slot(next_slot) dequeues the current-slot attestations, which is the same rule as prysm#13683.

**Best measured result.** avoids wasted EL payload build (pr:prysm#13683)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:5576-5586`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5576-L5586)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5606-5611`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5606-L5611)
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:212`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L212)

**Skeptic check.** Verified that overridden_forkchoice_update_params_or_failure_reason returns (true,true) when fork_choice_slot == head_slot. Gloas returns before these checks and never overrides.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#13683](https://github.com/OffchainLabs/prysm/pull/13683)

</details>


<a id="block_production-033"></a>
<details>
<summary><b>block_production-033</b> Yield before sync body production to process I/O — <i>n/a · low · latency</i></summary>

**Idea.** Defer synchronous block body construction to a later event-loop turn so pending I/O such as builder header requests is dispatched first.

**Impact.** Tokio runs builder requests as separate tasks, with no single-threaded event-loop starvation as in Node.js.

**Best measured result.** header seen by mev-boost at ~600ms vs logged ~100ms (pr:lodestar#8285)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_production/gloas.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_production/gloas.rs) block production in async tasks

**Sources.** [lodestar#8285](https://github.com/ChainSafe/lodestar/pull/8285)

</details>


<a id="block_production-034"></a>
<details>
<summary><b>block_production-034</b> Delay post-import fcU until shortly before next slot — <i>implemented · medium · S · latency</i></summary>

**Idea.** Instead of sending forkchoiceUpdated right after block import, send it shortly before the next slot so the EL returns a payload id and proposer-boost reorg remains possible.

**Impact.** Same outcome by a different mechanism: when re-org conditions hold, the post-import fcU is overridden to the parent. The fcU with payload attributes is sent late in the slot, so a proposer-boost re-org is still possible and the EL returns a payload id.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/canonical_head.rs:1913`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1913)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:7194-7200`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L7194-L7200)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5500-5515`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5500-L5515)
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:212-217`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L212-L217)

**Skeptic check.** The source PR, lodestar#7428, is closed and says it copies Lighthouse's timing. Lighthouse sends the post-import fcU with OverrideForkchoiceUpdate::Yes, which suppresses the head update when a re-org is planned. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#7428](https://github.com/ChainSafe/lodestar/pull/7428)

</details>


<a id="block_production-035"></a>
<details>
<summary><b>block_production-035</b> Filter packed attestations by shuffling dependent root — <i>implemented · medium · S · cpu, latency, bandwidth</i></summary>

**Idea.** When packing attestations, drop those whose target shuffling/dependent root differs from the proposal state's using a cheap root comparison, before any expensive validity checks.

**Impact.** Already done: incompatible-shuffling attestations are dropped by a cached root comparison before reward and max-cover work, on both pre-Gloas and Gloas production paths.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:2739`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2739) filter_op_pool_attestation memoizes per (beacon_block_root, target_epoch)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2763`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2763) shuffling_is_compatible compares AttestationShufflingId from fork choice
- [`beacon_node/operation_pool/src/lib.rs:327`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L327) validity_filter runs before AttMaxCover::new (reward computation)
- [`beacon_node/beacon_chain/src/block_production/gloas.rs:478`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_production/gloas.rs#L478) same filter used on the Gloas production path

**Skeptic check.** Verified the filter is a shuffling-ID comparison from fork choice, memoized per (block_root, target_epoch), and runs before AttMaxCover::new. Earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#4273](https://github.com/status-im/nimbus-eth2/pull/4273), [lodestar#4336](https://github.com/ChainSafe/lodestar/pull/4336), [lighthouse#900](https://github.com/sigp/lighthouse/pull/900)

</details>


<a id="block_production-036"></a>
<details>
<summary><b>block_production-036</b> Rebuild deposit trie when too many pending — <i>n/a · low · S · cpu</i></summary>

**Idea.** When the number of unfinalized deposits to apply is large, rebuild the deposit trie from scratch rather than applying incremental updates.

**Impact.** No deposit trie is built by the node at all; proposals carry no eth1 deposits.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:5931`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5931) eth1_data copied from state, no eth1 vote search
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5933`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5933) deposits = vec![] always; no eth1 service in beacon_node/ (dirs: beacon_chain, execution_layer, ... no eth1)
- [`consensus/state_processing/src/per_block_processing/process_operations.rs:652`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/process_operations.rs#L652) process_deposits only verifies

**Sources.** [prysm#10562](https://github.com/OffchainLabs/prysm/pull/10562)

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

**Verdict history.** not (checked) → not (refuted)

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

**Verdict history.** not (checked) → not (refuted)

**Sources.** [nimbus#4186](https://github.com/status-im/nimbus-eth2/pull/4186)

</details>


<a id="block_production-039"></a>
<details>
<summary><b>block_production-039</b> Remove previous-epoch limits in post-Altair packing — <i>implemented · low · S · cpu</i></summary>

**Idea.** Drop pre-Altair pending-attestation space bookkeeping from the greedy attestation packing loop, since post-Altair no such list can overflow.

**Impact.** None left; after Altair, prev_epoch_limit equals curr_epoch_limit, and no per-attestation pending-list bookkeeping happens in maximum_cover.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/lib.rs:418-426`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L418-L426)
- [`beacon_node/operation_pool/src/lib.rs:353`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L353)

**Skeptic check.** Verified in get_attestations: the MaxPendingAttestations limit is used only for BeaconState::Base. Earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#6508](https://github.com/status-im/nimbus-eth2/pull/6508)

</details>


<a id="block_production-040"></a>
<details>
<summary><b>block_production-040</b> Read proposer index from primed proposer cache — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** During block creation, read the proposer index from the proposer cache instead of recomputing proposer shuffling (e.g. at epoch boundaries), and have the state advance timer prime the next-epoch proposer cache (Fulu lookahead) ahead of time.

**Impact.** Proposer index is an O(1) lookahead read post-Fulu; the timer pre-fills the proposer cache before the epoch boundary.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:1655`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L1655) post-Fulu get_beacon_proposer_index reads proposer_lookahead
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:347`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L347) state advance primes proposer cache for current epoch
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:370`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L370) and next epoch once its decision slot has passed
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5888`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5888) production reads proposer index from the advanced state

**Skeptic check.** Confirmed the Fulu lookahead read and the state-advance priming of the current and next epoch proposer cache. The pre-Fulu shuffle path remains but is not used on mainnet; earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#693](https://github.com/Consensys-Incorporated/teku/pull/693), [lighthouse#8130](https://github.com/sigp/lighthouse/pull/8130), [lighthouse#4338](https://github.com/sigp/lighthouse/pull/4338)

</details>


<a id="block_production-041"></a>
<details>
<summary><b>block_production-041</b> Drop subset aggregates before packing — <i>implemented · medium · S · bandwidth</i></summary>

**Idea.** Just before packing, remove aggregates whose bits are a subset of another selected aggregate so no block space goes to attestations with no new votes.

**Impact.** Subset aggregates reach score 0 after their superset is chosen and are never packed.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/max_cover.rs:63`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/max_cover.rs#L63) zero-score items dropped up front
- [`beacon_node/operation_pool/src/max_cover.rs:76`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/max_cover.rs#L76) each round selects only items with score != 0
- [`beacon_node/operation_pool/src/max_cover.rs:88`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/max_cover.rs#L88) covering sets of remaining items updated after each pick
- [`beacon_node/operation_pool/src/attestation.rs:176`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation.rs#L176) update_covering_set removes validators already covered for the same slot/index

**Skeptic check.** Verified the greedy loop removes covered validators from same-committee candidates and stops selecting score-0 items, so subsets cannot use block space. Earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#8063](https://github.com/OffchainLabs/prysm/pull/8063)

</details>


<a id="block_production-042"></a>
<details>
<summary><b>block_production-042</b> Lower block production wait cutoff — <i>partial · low · S · latency</i></summary>

**Idea.** Lower the cutoff for waiting on payload/builder results during block production so the proposal is published early enough to be timely.

**Gap in Lighthouse.** Lighthouse has bounded waits (builder header 1s, engine getPayload 2s) but no slot-fraction cutoff derived from time into slot; tuning the constants is the only change.

**Impact.** Only matters when builder/EL is slow; marginal gain in proposal timeliness on rare slow-builder proposals.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/src/cli.rs:963`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/cli.rs#L963) builder-header-timeout default 1000ms, max 3000ms
- [`beacon_node/execution_layer/src/engine_api/http.rs:52`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engine_api/http.rs#L52) ENGINE_GET_PAYLOAD_TIMEOUT 2s
- [`beacon_node/builder_client/src/pre_gloas_builder_http_client.rs:46`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/builder_client/src/pre_gloas_builder_http_client.rs#L46) get_header timeout

**Sources.** [lodestar#5760](https://github.com/ChainSafe/lodestar/pull/5760)

</details>


<a id="block_production-043"></a>
<details>
<summary><b>block_production-043</b> Early exit in terminal PoW block search — <i>n/a · low · S · cpu, latency</i></summary>

**Idea.** When searching for the terminal PoW block, return immediately if the latest block's total difficulty is below TTD, skipping recursive parent lookups.

**Impact.** Merge transition search code is gone; nothing to optimize.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/execution_layer/src/lib.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/lib.rs): no terminal PoW block search remains (grep get_terminal_pow_block found nothing)

**Sources.** [prysm#10359](https://github.com/OffchainLabs/prysm/pull/10359)

</details>


<a id="block_production-044"></a>
<details>
<summary><b>block_production-044</b> Skip deposit reading and packing when none due — <i>n/a · low · S · cpu, latency, disk</i></summary>

**Idea.** Check up front whether any deposits must be included (state eth1 deposit index already equal to deposit count, or post-Electra where deposits come via execution requests) and skip the deposit DB read, deposit-tree building and proof work entirely.

**Impact.** Deposits are never read from a DB or proven at proposal; deposits vec is empty and post-Electra deposits come as execution requests.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:5931`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5931) eth1_data copied from state, no eth1 vote search
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5933`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5933) deposits = vec![] always; no eth1 service in beacon_node/ (dirs: beacon_chain, execution_layer, ... no eth1)
- [`consensus/state_processing/src/per_block_processing/process_operations.rs:652`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/process_operations.rs#L652) process_deposits only verifies

**Sources.** [prysm#5802](https://github.com/OffchainLabs/prysm/pull/5802), [prysm#14697](https://github.com/OffchainLabs/prysm/pull/14697), [lodestar#3737](https://github.com/ChainSafe/lodestar/pull/3737)

</details>


<a id="block_production-045"></a>
<details>
<summary><b>block_production-045</b> Build block body in parallel with payload fetch — <i>partial · medium · M · latency, cpu</i></summary>

**Idea.** Fire the engine getPayload and builder header requests at the start of production and build the consensus/blinded body (attestations, operations, state processing) concurrently as an independent part, joining at the end. Production takes the max of the two flows instead of their sum.

**Gap in Lighthouse.** Gloas path is serial: produce_block_on_state_gloas awaits produce_partial_beacon_block_gloas (slashings, exits, attestation max-cover, payload attestations) before it fires acquire_external_bid_candidates (direct builder getExecutionPayloadBid fan-out) and produce_execution_payload_bid/get_execution_payload_gloas (local engine getPayload). Production time is the sum of packing and payload/bid fetch, not the max. Start both futures before spawning the packing task and join them after.

**Impact.** Pre-Gloas (current mainnet) already gets max(packing, payload fetch). On Gloas, packing time (tens of ms, more under large op pools) plus builder HTTP round-trips are added together on every proposal.

**Best measured result.** race cutoff lowered from 2.5s to 2s (pr:lodestar#7814)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:5909`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5909) pre-Gloas: get_execution_payload spawned before op-pool/attestation packing
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5769`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5769) pre-Gloas: payload handle awaited after the partial block is built
- [`beacon_node/execution_layer/src/lib.rs:1077`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/lib.rs#L1077) tokio::join! of builder header and local payload
- [`beacon_node/beacon_chain/src/block_production/gloas.rs:217`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_production/gloas.rs#L217) Gloas: produce_partial_beacon_block_gloas (packing) is awaited first
- [`beacon_node/beacon_chain/src/block_production/gloas.rs:288`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_production/gloas.rs#L288) Gloas: acquire_external_bid_candidates and produce_execution_payload_bid start only after packing
- [`beacon_node/beacon_chain/src/block_production/gloas.rs:999`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_production/gloas.rs#L999) get_execution_payload_gloas called inside produce_execution_payload_bid

**Skeptic check.** Earlier evidence was right for the pre-Gloas produce_partial_beacon_block path. It missed the separate Gloas production path, where the payload/bid fetch starts only after packing completes.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [lodestar#7814](https://github.com/ChainSafe/lodestar/pull/7814), [teku#9455](https://github.com/Consensys-Incorporated/teku/pull/9455), [lodestar#7726](https://github.com/ChainSafe/lodestar/pull/7726), [lodestar#7740](https://github.com/ChainSafe/lodestar/pull/7740), [prysm#12297](https://github.com/OffchainLabs/prysm/pull/12297), [prysm#12408](https://github.com/OffchainLabs/prysm/pull/12408), [prysm#12811](https://github.com/OffchainLabs/prysm/pull/12811), [prysm#13008](https://github.com/OffchainLabs/prysm/pull/13008), [prysm#12251](https://github.com/OffchainLabs/prysm/pull/12251), [grandine@7b959604b](https://github.com/grandinetech/grandine/commit/7b959604b516), [lodestar#7815](https://github.com/ChainSafe/lodestar/pull/7815)

</details>


<a id="block_production-046"></a>
<details>
<summary><b>block_production-046</b> Fast eth1 data vote counting with early exit — <i>n/a · low · S · cpu, latency</i></summary>

**Idea.** When choosing eth1 data for a block, use a fast vote counting path that exits early when no candidate can reach majority and skips when the state already holds the same eth1 data.

**Impact.** Proposer copies state eth1_data, so no vote counting at production.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:5931`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5931) eth1_data copied from state, no eth1 vote search
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5933`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5933) deposits = vec![] always; no eth1 service in beacon_node/ (dirs: beacon_chain, execution_layer, ... no eth1)
- [`consensus/state_processing/src/per_block_processing/process_operations.rs:652`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/process_operations.rs#L652) process_deposits only verifies
- [`consensus/state_processing/src/per_block_processing.rs:357`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing.rs#L357) process_eth1_data only counts votes during import

**Sources.** [lodestar@ab2d2e13e](https://github.com/ChainSafe/lodestar/commit/ab2d2e13eb63)

</details>


<a id="block_production-047"></a>
<details>
<summary><b>block_production-047</b> Emit payload_attributes event before awaiting fcU — <i>implemented · low · S · latency</i></summary>

**Idea.** Emit the payload_attributes SSE event as soon as prepared state and parent hash are known, before awaiting the EL forkchoiceUpdated or cache warm-up, so external builders get it sooner.

**Impact.** None left; the SSE PayloadAttributes event is registered right after the attributes are known, before the duration_to_slot check and the update_execution_engine_forkchoice await.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:6954-7070`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L6954-L7070)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:7072-7111`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L7072-L7111)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:7113-7141`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L7113-L7141)

**Skeptic check.** Verified the order in prepare_beacon_proposer: compute/insert attributes, emit SSE, then the fcU. Earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#10037](https://github.com/ChainSafe/lodestar/pull/10037)

</details>


<a id="block_production-048"></a>
<details>
<summary><b>block_production-048</b> Track eth1 deposit sync off the proposal path — <i>n/a · low · S · latency</i></summary>

**Idea.** Track eth1 deposit sync against the finalized state in the background (lookup by deposit count) so proposing does not wait on or search the eth1 chain.

**Impact.** No eth1 deposit sync service exists in this Lighthouse; nothing runs on the proposal path.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:5931`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5931) eth1_data copied from state, no eth1 vote search
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5933`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5933) deposits = vec![] always; no eth1 service in beacon_node/ (dirs: beacon_chain, execution_layer, ... no eth1)
- [`consensus/state_processing/src/per_block_processing/process_operations.rs:652`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/process_operations.rs#L652) process_deposits only verifies

**Sources.** [nimbus@4eaf29875](https://github.com/status-im/nimbus-eth2/commit/4eaf29875a42)

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


<a id="block_production-050"></a>
<details>
<summary><b>block_production-050</b> Compare eth1 votes by hash tree root — <i>n/a · low · cpu</i></summary>

**Idea.** Compare eth1 data votes using their cached hash tree root on tree-backed values instead of deep value comparison.

**Impact.** Eth1 vote counting is a once-per-block scan of a list of at most 2048 items; the beacon_node/eth1 crate no longer exists, so nothing material to save.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_block_processing.rs:357`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing.rs#L357) process_eth1_data/get_new_eth1_data
- [`consensus/state_processing/src/per_epoch_processing/resets.rs:17`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/resets.rs#L17) votes reset

**Sources.** [lodestar#3721](https://github.com/ChainSafe/lodestar/pull/3721)

</details>


<a id="block_production-051"></a>
<details>
<summary><b>block_production-051</b> Use optimized cached state transition for state root — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Compute the produced block's state root with the optimized, cache-backed state transition (epoch context, cached committees) instead of a spec-style generic transition.

**Impact.** None left; production runs the same cache-backed per_block_processing on the advanced hot state, and update_tree_hash_cache computes the state root incrementally.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:6536-6551`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L6536-L6551)
- [`beacon_node/beacon_chain/src/block_production/mod.rs:87`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_production/mod.rs#L87)

**Skeptic check.** Verified that complete_partial_beacon_block uses the production state transition with committee and epoch caches and the milhouse incremental hash. Lighthouse has no separate spec-style transition. Earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#1006](https://github.com/ChainSafe/lodestar/pull/1006), [lodestar@ae658babb](https://github.com/ChainSafe/lodestar/commit/ae658babb9bb)

</details>


<a id="block_production-052"></a>
<details>
<summary><b>block_production-052</b> Fill remaining block space with unaggregated attestations — <i>implemented · low · S · bandwidth</i></summary>

**Idea.** After packing aggregates, add eligible unaggregated pool attestations if attestation slots remain, maximizing inclusion.

**Impact.** None left; before packing, every naive_aggregation_pool attestation (the locally aggregated unaggregated ones) is inserted into the op pool, so max cover can use them to fill spare slots.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:5941-5961`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5941-L5961)
- [`beacon_node/beacon_chain/src/block_production/gloas.rs:434-453`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_production/gloas.rs#L434-L453)
- [`beacon_node/operation_pool/src/lib.rs:345-444`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L345-L444)

**Skeptic check.** Upheld, but the earlier evidence missed the key step. The real mechanism is import_naive_aggregation_pool in block production (pre-Gloas and Gloas), not get_valid_attestations_for_epoch alone, because gossip inserts only aggregates into the op pool.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#4838](https://github.com/OffchainLabs/prysm/pull/4838)

</details>


<a id="block_production-053"></a>
<details>
<summary><b>block_production-053</b> Filter invalid-signature attestations before sort and cap — <i>n/a · low · cpu</i></summary>

**Idea.** Drop attestations with invalid signatures before sorting and truncating to MAX_ATTESTATIONS, so sorting handles fewer items and invalid ones cannot displace valid ones.

**Impact.** Lighthouse only inserts signature-verified attestations into the pool, so there are no invalid-signature ones to filter at packing time; paranoid mode optionally rechecks.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/lib.rs:295`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L295) insert_attestation assumes valid
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5992`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5992) paranoid_block_proposal recheck

**Sources.** [prysm#14259](https://github.com/OffchainLabs/prysm/pull/14259)

</details>


<a id="block_production-054"></a>
<details>
<summary><b>block_production-054</b> Finalized deposit cache with trie snapshot — <i>n/a · low · cpu</i></summary>

**Idea.** Cache finalized deposits with a merkle trie snapshot so the deposit proof is built from the finalized prefix plus pending deposits instead of rebuilding the whole trie.

**Impact.** The eth1 deposit cache and deposit trie are gone from this checkout; deposits come via EL requests.

**Evidence (Lighthouse @ 928b61e719).**

- beacon_node/ has no eth1 crate (ls beacon_node)

**Sources.** [prysm#6391](https://github.com/OffchainLabs/prysm/pull/6391), [prysm#10511](https://github.com/OffchainLabs/prysm/pull/10511), [lodestar#868](https://github.com/ChainSafe/lodestar/pull/868), [nimbus@18639c3ef](https://github.com/status-im/nimbus-eth2/commit/18639c3effc0)

</details>


<a id="block_production-055"></a>
<details>
<summary><b>block_production-055</b> Recompute fork choice head right before building proposal — <i>implemented · medium · S · latency</i></summary>

**Idea.** Immediately before block production, process pending attestations and run fork choice to recompute the head, so the proposal builds on the freshest head.

**Impact.** Proposal waits for the slot-start fork choice run, which applies queued attestations, on both production paths.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_production/mod.rs:48`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_production/mod.rs#L48) load_state_for_block_production calls wait_for_fork_choice_before_block_production first
- [`beacon_node/beacon_chain/src/block_production/mod.rs:129`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_production/mod.rs#L129) waits on fork_choice_signal_rx with timeout
- [`beacon_node/beacon_chain/src/beacon_chain.rs:7495`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L7495) per-slot task runs recompute_head_at_current_slot then notifies
- [`consensus/fork_choice/src/fork_choice.rs:1511`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L1511) update_time dequeues pending attestations via process_attestation_queue
- [`beacon_node/beacon_chain/src/block_production/gloas.rs:137`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_production/gloas.rs#L137) Gloas path uses the same load_state_for_block_production

**Second check.** The earlier review missed block_production/mod.rs: block production does not run fork choice itself, but it waits on the ForkChoiceSignal for the slot-start run. This gives the same freshest-head guarantee.

**Skeptic check.** Verified the wait-then-read-head ordering and that the slot-start recompute processes the attestation queue. Earlier evidence was correct.

**Verdict history.** partial (checked) → implemented (refuted) → implemented (skeptic)

**Sources.** [teku#5569](https://github.com/Consensys-Incorporated/teku/pull/5569), [prysm#11992](https://github.com/OffchainLabs/prysm/pull/11992), [teku#5686](https://github.com/Consensys-Incorporated/teku/pull/5686)

</details>


<a id="block_production-056"></a>
<details>
<summary><b>block_production-056</b> Attestation data from fork choice store — <i>partial · low · M · cpu, memory, latency</i></summary>

**Idea.** Build attestation data from the fork choice store (justified checkpoint, target root) instead of the head state, removing the need to advance the head state and an attestation cache.

**Gap in Lighthouse.** Attestation data is built from the head snapshot and early attester cache, not fork choice store; the head state is only advanced when the request is in a later epoch (get_advanced_hot_state). Switching to fork choice would only matter for the cross-epoch case.

**Impact.** Saves a state advance only on first attestation request of a new epoch when head lacks that epoch; small and rare, and fork choice justified can differ from state semantics.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:2010`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2010) produce_unaggregated_attestation uses early attester cache and head state
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2064`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2064) head_state justified checkpoint

**Sources.** [prysm#13256](https://github.com/OffchainLabs/prysm/pull/13256)

</details>


<a id="block_production-057"></a>
<details>
<summary><b>block_production-057</b> Skip payload-attribute preparation when not synced — <i>implemented · high · S · memory, cpu</i></summary>

**Idea.** Do not compute payload attributes (state copy and slot replay) while the node is not in regular sync, and do not consider the node synced while its head is far behind peer-reported heads. This stops payload-attribute preparation from regenerating state across hundreds of epochs.

**Impact.** Payload-attribute state advance is bounded to about 2 epochs; a far-behind node skips preparation.

**Best measured result.** Stated: 9 GB heap exhausted by replaying ~27-34 epoch transitions when head was 850-1100 slots behind (pr:teku#11219)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:6748`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L6748) prepare_beacon_proposer returns early if head is more than sync_tolerance_epochs behind current slot
- [`beacon_node/beacon_chain/src/chain_config.rs:16`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/chain_config.rs#L16) DEFAULT_SYNC_TOLERANCE_EPOCHS = 2
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5319`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5319) get_pre_payload_attributes skips on proposer cache miss far behind; else clones head state, no replay
- [`beacon_node/beacon_chain/src/beacon_chain.rs:6989`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L6989) compute_withdrawals_for_payload_attributes is only reached through prepare_beacon_proposer
- [`beacon_node/beacon_chain/src/canonical_head.rs:1931`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1931) all prep callers (head update, state advance timer, prep service, HTTP) go through prepare_beacon_proposer

**Skeptic check.** Confirmed every caller of the payload-attribute computation passes the head-vs-wallclock gate. There is no peer-head check, but the gate bounds the replay cost the idea targets. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#11219](https://github.com/Consensys-Incorporated/teku/pull/11219), [prysm#16951](https://github.com/OffchainLabs/prysm/pull/16951)

</details>


<a id="block_production-058"></a>
<details>
<summary><b>block_production-058</b> Greedy max-cover attestation selection — <i>implemented · low · S · cpu</i></summary>

**Idea.** Select block attestations with a greedy max-cover algorithm, scoring each candidate by not-yet-covered bits, as a cheap approximation to optimal packing.

**Impact.** Lighthouse packs attestations with reward-weighted greedy max-cover.

**Best measured result.** slower than naive sort: 512 single-bit atts about 5.1 ms vs 0.31 ms; a quality trade-off (pr:prysm#8571)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/max_cover.rs:53`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/max_cover.rs#L53) maximum_cover greedy selection by score
- [`beacon_node/operation_pool/src/attestation.rs:198`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation.rs#L198) score = sum of rewards of not-yet-covered validators
- [`beacon_node/operation_pool/src/lib.rs:413`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L413) prev/curr epoch max-cover run in parallel with rayon::join
- [`beacon_node/operation_pool/src/lib.rs:430`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L430) merge_solutions

**Skeptic check.** Verified greedy max-cover with fresh-validator reward scoring on the single get_attestations path used by both production paths. Earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [grandine#156](https://github.com/grandinetech/grandine/pull/156), [prysm#8571](https://github.com/OffchainLabs/prysm/pull/8571)

</details>


<a id="block_production-059"></a>
<details>
<summary><b>block_production-059</b> Read justified checkpoints once per block — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** When checking attestation validity during packing, read the state's justified checkpoints once rather than per attestation.

**Impact.** None left: the source-checkpoint check is done structurally by indexing the pool by CheckpointKey, which reads the justified checkpoints once per packing.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/attestation_storage.rs:184`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs#L184) keys_for_state reads previous/current justified checkpoints once
- [`beacon_node/operation_pool/src/lib.rs:364`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L364) get_attestations calls keys_for_state once per block
- [`beacon_node/operation_pool/src/lib.rs:317`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L317) get_valid_attestations_for_epoch only iterates attestations stored under that CheckpointKey
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2739`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2739) filter_op_pool_attestation memoizes per (block_root, target_epoch)

**Skeptic check.** Verified that LH never compares each attestation's source to the state's justified checkpoint. It looks up the bucket keyed by checkpoints read once in keys_for_state, which is stronger than the Lodestar fix. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#2948](https://github.com/ChainSafe/lodestar/pull/2948), [lighthouse#10266](https://github.com/sigp/lighthouse/pull/10266)

</details>


<a id="block_production-060"></a>
<details>
<summary><b>block_production-060</b> Process slots and state root once for all attestations — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** In block production, run process_slots and the state hash_tree_root once and reuse them for every packed attestation instead of per attestation.

**Impact.** State advance and root happen once; every attestation is checked against that one state.

**Best measured result.** should save 50ms to 100ms on block proposals (pr:prysm#5632)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:5866`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5866) complete_state_advance once per pre-Gloas production
- [`beacon_node/beacon_chain/src/block_production/gloas.rs:395`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_production/gloas.rs#L395) complete_state_advance once per Gloas production
- [`beacon_node/operation_pool/src/lib.rs:345`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L345) get_attestations evaluates all attestations against one state

**Skeptic check.** Confirmed one state advance per production on both paths, with one op-pool pass over the advanced state. Earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#5632](https://github.com/OffchainLabs/prysm/pull/5632)

</details>


<a id="block_production-061"></a>
<details>
<summary><b>block_production-061</b> Compute total active balance once per block — <i>implemented · low · S · cpu</i></summary>

**Idea.** Compute total active balance once per block and pass it into per-attestation participation processing instead of recomputing it per attestation.

**Impact.** None left: total active balance is cached on the state, and per-attestation base rewards come from the epoch cache on both the packing and import paths.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/lib.rs:364`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L364) total_active_balance read once from the state cache in get_attestations
- [`consensus/types/src/state/beacon_state.rs:2677`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2677) get_total_active_balance returns the cached value (no recompute)
- [`beacon_node/operation_pool/src/attestation.rs:96`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation.rs#L96) new_for_altair_or_later uses state.get_base_reward (epoch cache)
- [`consensus/state_processing/src/per_block_processing/process_operations.rs:280`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/process_operations.rs#L280) block-processing participation uses get_base_reward from the epoch cache

**Skeptic check.** Confirmed that the total active balance is a cached state field, read once for packing. Altair+ participation processing (packing and per_block_processing) uses precomputed base rewards from the epoch cache. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#9418](https://github.com/OffchainLabs/prysm/pull/9418)

</details>


<a id="block_production-062"></a>
<details>
<summary><b>block_production-062</b> Inline withdrawable checks, lazily load pending withdrawals — <i>implemented · low · S · cpu</i></summary>

**Idea.** In get_expected_withdrawals, inline the per-validator withdrawable checks and load the full pending-partial-withdrawal list only when needed.

**Impact.** Negligible: the Lodestar cost was materializing the full pending-partials list (getAllReadonly), which LH never does. Inlining is_fully/partially_withdrawable would save only microseconds.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_block_processing/withdrawals.rs:119`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/withdrawals.rs#L119) get_pending_partial_withdrawals iterates the milhouse list lazily and breaks at the first non-withdrawable entry or at the limit
- [`consensus/state_processing/src/per_block_processing/withdrawals.rs:244`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/withdrawals.rs#L244) get_validators_sweep_withdrawals bounded by max_validators_per_withdrawals_sweep

**Skeptic check.** Read the code: pending partials are consumed via an iterator with an early break, with no full-list copy. The sweep calls the validator methods per index, which costs very little in Rust. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#7045](https://github.com/ChainSafe/lodestar/pull/7045)

</details>


<a id="block_production-063"></a>
<details>
<summary><b>block_production-063</b> Separate block producer from validator message processing — <i>n/a · low · S · latency</i></summary>

**Idea.** Run block production as a dedicated task/service so HTTP block-produce requests do not block validator message processing.

**Impact.** Grandine's problem was a single-threaded mutator handling both; Lighthouse has no such actor, producer requests run on independent tasks.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:5728-5850`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5728-L5850) produce_block_on_state runs on its own tokio task with spawn_blocking for state work
- [`beacon_node/http_api/src/publish_blocks.rs:436-460`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/publish_blocks.rs#L436-L460) sidecar building in spawn_blocking

**Sources.** [grandine@d3fcc6d73](https://github.com/grandinetech/grandine/commit/d3fcc6d73065)

</details>


<a id="block_production-064"></a>
<details>
<summary><b>block_production-064</b> Keep pool signatures in deserialized form — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Store attestation pool signatures as already-decompressed curve points (lazy aggregation) so building a block does not decompress each signature.

**Impact.** None needed; pool signatures are stored as decompressed blst points and aggregated in place, so packing does not decompress them.

**Best measured result.** Proposal ~6x faster at 220k validators: 14962ms -&gt; 2326ms non-epoch slot (pr:nimbus#2423)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/attestation_storage.rs:40`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs#L40)
- [`beacon_node/operation_pool/src/attestation_storage.rs:249`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs#L249)
- [`crypto/bls/src/generic_aggregate_signature.rs:60`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/generic_aggregate_signature.rs#L60)

**Skeptic check.** Confirmed: CompactIndexedAttestation holds bls AggregateSignature, and GenericAggregateSignature wraps the point (point: Option&lt;AggSig&gt;). Aggregation is add_assign_aggregate on points. The earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#2423](https://github.com/status-im/nimbus-eth2/pull/2423)

</details>


<a id="block_production-065"></a>
<details>
<summary><b>block_production-065</b> Re-run payload preparation late in prior slot — <i>implemented · low · S · latency</i></summary>

**Idea.** Re-send payload preparation (fcU with attributes) about one second before the slot ends so the EL builds with more mempool transactions.

**Impact.** None needed; fcU with attributes is sent at 4s before slot end and again at the fork-choice instant (slot_duration/24, about 0.5s before slot end).

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/proposer_prep_service.rs:35`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/proposer_prep_service.rs#L35)
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:200`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L200)
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:217`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L217)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:7130`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L7130)
- [`beacon_node/beacon_chain/src/chain_config.rs:166`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/chain_config.rs#L166)

**Skeptic check.** Confirmed that the state advance timer calls prepare_beacon_proposer at the fork-choice lookahead, and that it sends fcU because till_prepare_slot &lt;= prepare_payload_lookahead (4s). This is the same as the grandine re-run at AggregateFourth. The earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [grandine@cf44fbdd0](https://github.com/grandinetech/grandine/commit/cf44fbdd0df4)

</details>


<a id="block_production-066"></a>
<details>
<summary><b>block_production-066</b> Fetch deposits only up to canonical eth1 height — <i>n/a · low · S · cpu</i></summary>

**Idea.** When proposing, fetch deposits only up to the canonical eth1 follow height to bound deposit trie size.

**Impact.** Lighthouse no longer packs deposits from an eth1 cache; nothing to bound.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:5931-5933`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5931-L5933) eth1_data cloned from state and deposits = vec![]

**Sources.** [prysm#6309](https://github.com/OffchainLabs/prysm/pull/6309)

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


<a id="block_production-068"></a>
<details>
<summary><b>block_production-068</b> Non-blocking fork choice state getters for producer — <i>partial · low · M · latency, cpu</i></summary>

**Idea.** Provide non-blocking variants of fork-choice/state getters so the block producer reads a snapshot without waiting on the fork choice mutator lock.

**Gap in Lighthouse.** Producer takes the cached_head read lock only briefly, but other proposer-path getters (get_state_for_re_org, proposer head) take the fork_choice read lock and can wait behind a write lock. Would need an ArcSwap snapshot for those getters in canonical_head.rs.

**Impact.** Would remove rare stalls of block production behind a long fork choice write; the code already logs hold times above 1s. Small gain for most nodes.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/canonical_head.rs:13-15`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L13-L15),85-107 fork choice and cached head are parking_lot RwLocks
- [`beacon_node/beacon_chain/src/block_production/mod.rs:49-58`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_production/mod.rs#L49-L58) producer reads cached_head briefly and clones Arc fields
- [`beacon_node/beacon_chain/src/block_production/mod.rs:130-160`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_production/mod.rs#L130-L160) waits for the fork choice signal with a bounded timeout rather than the lock

**Sources.** [grandine#496](https://github.com/grandinetech/grandine/pull/496), [grandine@e03c58e64](https://github.com/grandinetech/grandine/commit/e03c58e643f9)

</details>


<a id="block_production-069"></a>
<details>
<summary><b>block_production-069</b> Optimized block production path avoiding redundant state work — <i>implemented · low · S · latency, cpu</i></summary>

**Idea.** Use a block production path that avoids redundant state copies and transitions when building a block, as the default.

**Impact.** None left: there is one production path with one state transition on a cached, advanced, cheaply cloned (milhouse) state.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_production/mod.rs:43`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_production/mod.rs#L43) load_state_for_block_production takes the pre-advanced head state from the state cache via get_advanced_hot_state
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5870`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5870) complete_state_advance is a no-op when the state is already advanced
- [`beacon_node/beacon_chain/src/beacon_chain.rs:6542`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L6542) single per_block_processing pass, then update_tree_hash_cache at 6553
- [`beacon_node/beacon_chain/src/block_production/gloas.rs:867`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_production/gloas.rs#L867) the Gloas path does the same single pass

**Skeptic check.** Prysm#10113 only flipped a feature flag to make its optimized path the default. LH has no slow alternative path, and both the pre-Gloas and Gloas producers do one transition on the cached advanced state. Value lowered to low because nothing is left to gain.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#10113](https://github.com/OffchainLabs/prysm/pull/10113)

</details>


<a id="block_production-070"></a>
<details>
<summary><b>block_production-070</b> Request local payload and builder bid concurrently with cutoff — <i>implemented · medium · S · latency</i></summary>

**Idea.** Request the local EL payload and the external builder bid concurrently rather than sequentially, with a cutoff (~3s) after which whichever is available is used. Proposal latency becomes the max of the two, bounded by the cutoff, so a slow EL or builder does not delay the proposal.

**Gap in Lighthouse.** Small: no shared race cutoff. tokio::join! waits for both legs. On a payload-id cache miss, get_full_payload_with first sends forkchoiceUpdated (8s timeout) and then getPayload (2s), so a builder header that is ready can wait for the slow local leg.

**Impact.** Normal path is bounded at about 2s by the per-leg timeouts. Only the rare payload-id miss path can stall longer.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/execution_layer/src/lib.rs:1077`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/lib.rs#L1077)
- [`beacon_node/builder_client/src/pre_gloas_builder_http_client.rs:35`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/builder_client/src/pre_gloas_builder_http_client.rs#L35)
- [`beacon_node/execution_layer/src/engine_api/http.rs:52`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engine_api/http.rs#L52)
- [`beacon_node/execution_layer/src/lib.rs:1352`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/lib.rs#L1352)
- [`beacon_node/beacon_chain/src/block_production/gloas.rs:310`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_production/gloas.rs#L310)

**Second check.** The earlier gap said the local EL request had no cutoff. That is wrong: engine_getPayload has a 2s HTTP timeout, and the builder header has a 1s default. Together they give the idea's bounded concurrent fetch.

**Skeptic check.** Confirmed concurrent builder and local fetch pre-Gloas (fetch_builder_and_local_payloads), and the Gloas join in gloas.rs. The per-request timeouts work as the cutoff. The earlier verdict and the gap it named are correct.

**Verdict history.** partial (checked) → implemented (refuted) → implemented (skeptic)

**Sources.** [nimbus#4749](https://github.com/status-im/nimbus-eth2/pull/4749), [prysm#17607](https://github.com/OffchainLabs/prysm/pull/17607), [lodestar#5223](https://github.com/ChainSafe/lodestar/pull/5223), [grandine#948](https://github.com/grandinetech/grandine/pull/948), [lodestar#6241](https://github.com/ChainSafe/lodestar/pull/6241), [grandine#822](https://github.com/grandinetech/grandine/pull/822), [nimbus#8712](https://github.com/status-im/nimbus-eth2/pull/8712)

</details>


<a id="block_production-071"></a>
<details>
<summary><b>block_production-071</b> Broadcast each blob sidecar in its own task — <i>n/a · low · S · latency</i></summary>

**Idea.** When publishing a proposal's blobs, broadcast and process each blob sidecar in its own concurrent task so one slow blob does not delay the others.

**Impact.** Post-Fulu blobs are published as data column sidecars in one batch to the network service which does the gossip fan-out; per-blob tasks have no counterpart.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/publish_blocks.rs:243`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/publish_blocks.rs#L243) columns built in one blocking task
- publish_blocks.rs:493-560 all columns sent as a batch over the network channel; block published first at line ~262

**Sources.** [prysm#13959](https://github.com/OffchainLabs/prysm/pull/13959)

</details>


<a id="block_production-072"></a>
<details>
<summary><b>block_production-072</b> Query multiple builder URLs in parallel — <i>not · low · M · latency</i></summary>

**Idea.** Request bids from all configured builder endpoints in parallel rather than sequentially.

**Gap in Lighthouse.** Execution layer holds one builder client; would need a Vec of clients and join_all in fetch_builder_and_local_payloads, picking the best bid. Users today put mev-boost (which fans out to relays) in front.

**Impact.** Only helps the rare operator with several builder endpoints directly; relay fan-out already happens inside mev-boost.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/src/cli.rs:925-933`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/cli.rs#L925-L933) --builder takes one URL
- [`beacon_node/execution_layer/src/lib.rs:479`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/lib.rs#L479),626-640 single ArcSwapOption builder client
- lib.rs:1056-1100 only races the one builder against the local EL with tokio::join

**Sources.** [nimbus#9336](https://github.com/status-im/nimbus-eth2/pull/9336), [prysm#16596](https://github.com/OffchainLabs/prysm/pull/16596), [prysm#17067](https://github.com/OffchainLabs/prysm/pull/17067)

</details>


<a id="block_production-073"></a>
<details>
<summary><b>block_production-073</b> Fall back to P2P bid in parallel with local build — <i>implemented · low · S · latency</i></summary>

**Idea.** When a supplied builder bid fails validation, consider the best P2P bid in parallel with local payload production and return whichever is ready by the cutoff.

**Impact.** None needed; direct bids, the best gossip bid and the local build are candidates together, and a failed direct bid or local build falls back to the others.

**Best measured result.** Observed local build 3.483s; P2P fallback could return about 2.086s sooner (pr:lodestar#10212)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_production/gloas.rs:310`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_production/gloas.rs#L310)
- [`beacon_node/beacon_chain/src/block_production/gloas.rs:1117`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_production/gloas.rs#L1117)
- [`beacon_node/beacon_chain/src/block_production/gloas.rs:1193`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_production/gloas.rs#L1193)
- [`beacon_node/beacon_chain/src/block_production/gloas.rs:326`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_production/gloas.rs#L326)

**Skeptic check.** Confirmed: acquire_external_bid_candidates runs in tokio::join with the local build. It adds the highest gossip-verified bid from the cache after verify_bid_state_conditions, and select_payload_bid ranks all candidates. Only the single highest gossip bid is tried, which is a minor difference.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#10212](https://github.com/ChainSafe/lodestar/pull/10212)

</details>


<a id="block_production-074"></a>
<details>
<summary><b>block_production-074</b> Build deposits and attestations concurrently — <i>n/a · low · S · latency</i></summary>

**Idea.** Pack deposits and attestations concurrently during block production and skip a redundant execution-block fetch for the eth1 data vote.

**Impact.** Deposit packing from an eth1 cache no longer exists in Lighthouse, and the payload is already fetched concurrently with attestation packing.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:5931-5933`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5931-L5933) no deposit packing; eth1_data from state

**Sources.** [prysm#9541](https://github.com/OffchainLabs/prysm/pull/9541)

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

**Verdict history.** not (checked) → not (refuted)

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

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [teku#9660](https://github.com/Consensys-Incorporated/teku/pull/9660)

</details>


<a id="block_production-077"></a>
<details>
<summary><b>block_production-077</b> Score attestations by newly set participation flags — <i>implemented · medium · S · cpu</i></summary>

**Idea.** When packing attestations, score each candidate by which participation flags (source/target/head) it would newly set in the state, i.e. by its actual reward, rather than only by the count of new attester bits. This packs higher-value attestations into the limited block space.

**Gap in Lighthouse.** Only the slashable double-vote case: a validator that already has any flag set is skipped by has_attested_in_epoch.

**Impact.** Already in place; the score is the proposer reward from the flags set at this inclusion delay.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/attestation.rs:88`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation.rs#L88)
- [`beacon_node/operation_pool/src/attestation.rs:112`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation.rs#L112)
- [`beacon_node/operation_pool/src/attestation.rs:182`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation.rs#L182)
- [`beacon_node/operation_pool/src/reward_cache.rs:17`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/reward_cache.rs#L17)

**Second check.** The earlier gap assumed that flags could be added to a validator who already has some. That is not possible: the head flag needs delay 1 and later inclusions only lose flags, so any other route is a double vote. Lighthouse's reward-weighted scoring is therefore what the idea describes.

**Skeptic check.** Confirmed that new_for_altair_or_later uses get_attestation_participation_flag_indices with the inclusion delay and weights each validator by base_reward * flag weights. A later inclusion cannot add flags without a slashable vote, because the inclusion delay only grows. The earlier evidence is correct.

**Verdict history.** partial (checked) → implemented (refuted) → implemented (skeptic)

**Sources.** [nimbus#5468](https://github.com/status-im/nimbus-eth2/pull/5468)

</details>


<a id="block_production-078"></a>
<details>
<summary><b>block_production-078</b> VC passes selected bid to beacon node producer — <i>not · low · L · latency, bandwidth</i></summary>

**Idea.** Let the validator client pass an already selected execution payload bid into the beacon node block production endpoint. With several beacon nodes, each node then does not repeat the builder request.

**Gap in Lighthouse.** Add an optional selected-bid parameter to the produce-block endpoint and VC fallback path so the second BN skips acquire_external_bid_candidates.

**Impact.** Saves duplicate builder requests only for multi-BN setups; also needs a beacon-API change.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/block_service.rs:502`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/block_service.rs#L502) - VC only passes builder_boost_factor
- [`common/eth2/src/lib.rs:2954`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/eth2/src/lib.rs#L2954) - produce_block query only carries builder_boost_factor
- [`beacon_node/beacon_chain/src/block_production/gloas.rs:171`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_production/gloas.rs#L171) - BN itself fans out to direct builders

**Sources.** [lodestar#10057](https://github.com/ChainSafe/lodestar/pull/10057)

</details>


<a id="block_production-079"></a>
<details>
<summary><b>block_production-079</b> Record payload ID for late-arriving blocks — <i>implemented · medium · S · latency</i></summary>

**Idea.** When a block arrives late and triggers a forkchoiceUpdated, still store the returned payload ID in the proposer/payload-ID cache. The proposer then reuses it instead of issuing a fresh forkchoiceUpdated at proposal time.

**Impact.** None needed; a late block that becomes head triggers prepare_beacon_proposer, and the payload id from its fcU is cached for the proposal.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/execution_layer/src/engines.rs:176`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engines.rs#L176)
- [`beacon_node/beacon_chain/src/canonical_head.rs:1931`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1931)
- [`beacon_node/execution_layer/src/lib.rs:1580`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/lib.rs#L1580)
- [`beacon_node/execution_layer/src/lib.rs:1342`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/lib.rs#L1342)

**Skeptic check.** Confirmed that Engine::notify_forkchoice_updated caches every returned payload_id regardless of caller. After a new head, canonical_head.rs runs prepare_beacon_proposer, which sends an fcU with attributes for the new head root. The earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#16563](https://github.com/OffchainLabs/prysm/pull/16563)

</details>


<a id="block_production-080"></a>
<details>
<summary><b>block_production-080</b> Reuse live payload builder after head flips (ePBS) — <i>implemented · low · S · latency, cpu</i></summary>

**Idea.** Cache decoded FULL-parent execution requests, keep and reuse an exact matching in-progress EL payload build after a head flip, and collect a prepared build only when its payload ID matches. This avoids restarting payload builds when the head changes back and forth.

**Impact.** Marginal: payload ids are keyed by exact (parent hash, attributes), so the build is reused after head flips. Preparation picks the build variant, and parent requests are never re-decoded.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/execution_layer/src/engines.rs:108`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engines.rs#L108) PayloadIdCacheKey(head_block_hash, payload_attributes) LRU, so an A-&gt;B-&gt;A flip hits the old id
- [`beacon_node/execution_layer/src/lib.rs:1343`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/lib.rs#L1343) get_full_payload_with reuses the cached payload id and only issues a fresh FCU on a miss
- [`beacon_node/beacon_chain/src/beacon_chain.rs:6805`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L6805) prepare_beacon_proposer uses should_build_on_full so preparation targets the FULL/EMPTY variant the proposer will build on
- [`beacon_node/beacon_chain/src/block_production/gloas.rs:199`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_production/gloas.rs#L199) parent execution requests come from the cached envelope summary in the head snapshot (no decode)

**Skeptic check.** Verified the payload-id LRU and its use at getPayload time. Also verified the Lodestar#10410 aspect: LH already prepares on the variant chosen by should_build_on_full. Parent execution requests are held as an in-memory summary. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [caplin#24939](https://github.com/erigontech/erigon/pull/24939), [lodestar#10410](https://github.com/ChainSafe/lodestar/pull/10410)

</details>


<a id="block_production-081"></a>
<details>
<summary><b>block_production-081</b> Re-trigger payload preparation on payload reveal/PTC verdict — <i>partial · medium · S · latency</i></summary>

**Idea.** Under ePBS, send forkchoiceUpdated with attributes as soon as the payload reveal and PTC votes of the current slot are processed, and again whenever the PTC verdict flips the parent choice or the execution head changes with an unchanged beacon root. Skip it when head, parent choice and fee recipient are unchanged. The payload then has a ~4s lead instead of a fresh ~500ms request.

**Gap in Lighthouse.** Payload reveal and execution-head change at an unchanged beacon root already re-trigger prep via recompute_head, with skip-if-unchanged. A PTC verdict flip (votes arrive at about 9s) is only picked up by the 11.5s fork-choice prep run, which gives the EL about 0.5s. Re-run prepare_beacon_proposer from process_gossip_payload_attestation_result (or once at the PTC deadline) when should_build_on_full for the next slot changes.

**Impact.** Lead time after a PTC flip goes from ~0.5s to ~3s; the common no-flip case already has a 4s lead.

**Best measured result.** payload built with 4s lead time instead of 500ms (pr:lodestar#10508)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:4084`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L4084) - envelope (payload reveal) import calls recompute_head_at_current_slot
- [`beacon_node/beacon_chain/src/canonical_head.rs:1088`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1088) - recompute_head early-exits when view, payload status and FCU params are unchanged (skip-if-unchanged)
- [`beacon_node/beacon_chain/src/canonical_head.rs:1107`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1107) - payload status change with same beacon root counts as a head change
- [`beacon_node/beacon_chain/src/canonical_head.rs:1931`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1931) - every head change re-runs prepare_beacon_proposer
- [`beacon_node/beacon_chain/src/beacon_chain.rs:6806`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L6806) - prep picks build parent via should_build_on_full (PTC verdict)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:7125`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L7125) - FCU with attributes only sent within prepare_payload_lookahead
- [`beacon_node/beacon_chain/src/proposer_prep_service.rs:41`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/proposer_prep_service.rs#L41) - periodic prep at slot_duration - 4s (8s), before the PTC deadline
- [`consensus/types/src/core/chain_spec.rs:1276`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/core/chain_spec.rs#L1276) - payload_attestation_due_bps 7500 (9s)
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:136`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L136) - next prep run at 23/24 slot (11.5s)
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:217`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L217) - prep re-run after fork choice at 11.5s
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:4466`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L4466) - payload attestation only updates fork choice and pool, no prep

**Second check.** Beyond the earlier review, confirmed the timings: the prep service fires at 8s, before the 9s PTC deadline, so it cannot see PTC votes. The next prep after a PTC flip is the 11.5s state-advance fork-choice run. Also confirmed that recompute_head treats a payload-status change at the same root as a head change, and that it skips when nothing changed.

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [caplin#24938](https://github.com/erigontech/erigon/pull/24938), [grandine@a740b9ccf](https://github.com/grandinetech/grandine/commit/a740b9ccfa28), [grandine#899](https://github.com/grandinetech/grandine/pull/899), [lodestar#10508](https://github.com/ChainSafe/lodestar/pull/10508)

</details>


<a id="block_production-082"></a>
<details>
<summary><b>block_production-082</b> Do not key payload cache on safe/finalized hashes — <i>implemented · medium · S · latency</i></summary>

**Idea.** When looking up a cached payload-build (payload ID) at proposal time, match on head/parent, timestamp and attributes but not on the safe and finalized block hashes. A changed finalized hash then does not cause a cache miss and an extra ~500ms getPayload delay.

**Impact.** None needed; the payload id cache key does not include the safe or finalized hash.

**Best measured result.** avoids consistent misses and additional 500ms delays when proposing (pr:nimbus#8268)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/execution_layer/src/engines.rs:109`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engines.rs#L109)
- [`beacon_node/execution_layer/src/engines.rs:149`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/engines.rs#L149)
- [`beacon_node/execution_layer/src/lib.rs:1342`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/lib.rs#L1342)

**Skeptic check.** Confirmed that PayloadIdCacheKey is {head_block_hash, payload_attributes} and the lookup in get_full_payload_with uses only parent_hash and attributes. The earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#8268](https://github.com/status-im/nimbus-eth2/pull/8268)

</details>


<a id="block_production-083"></a>
<details>
<summary><b>block_production-083</b> Build consensus block body only once — <i>implemented · medium · S · cpu, memory, latency</i></summary>

**Idea.** When producing a block with both builder and local EL payloads, build the consensus body (attestation packing, slashings, exits, proposal state) once and reuse it for both, or choose the payload first and then build one block, instead of building two full blocks and comparing.

**Impact.** None needed; the consensus body is packed once and only the payload source is chosen.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:5728`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5728)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5766`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5766)
- [`beacon_node/execution_layer/src/lib.rs:1056`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/lib.rs#L1056)
- [`beacon_node/beacon_chain/src/block_production/gloas.rs:346`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_production/gloas.rs#L346)

**Skeptic check.** Confirmed: produce_block_on_state builds one partial block and awaits one payload handle. The builder-vs-local choice is made inside the execution layer (Full or Blinded). Gloas does the same with a single partial block and select_payload_bid. The earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#7353](https://github.com/status-im/nimbus-eth2/pull/7353), [lodestar#6270](https://github.com/ChainSafe/lodestar/pull/6270)

</details>


<a id="block_production-084"></a>
<details>
<summary><b>block_production-084</b> At most one state and epoch transition per proposal — <i>implemented · medium · S · cpu, memory, latency</i></summary>

**Idea.** In block assembly, generate only the state at the block slot and run the epoch transition at most once, sharing it across body pieces, instead of also loading the previous-block state or recomputing the transition per piece.

**Impact.** None needed: one state is loaded (cached advanced head, re-org parent, or state_at_slot) and complete_state_advance runs once; all body pieces and the post-state root share it.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_production/mod.rs:43`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_production/mod.rs#L43)
- [`beacon_node/beacon_chain/src/block_production/mod.rs:84`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_production/mod.rs#L84)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5870`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5870)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:6542`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L6542)
- [`beacon_node/beacon_chain/src/beacon_block_reward.rs:27`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_block_reward.rs#L27)

**Skeptic check.** Verified load_state_for_block_production loads exactly one state on each branch and produce_partial_beacon_block (and the Gloas path, gloas.rs:396) advances it once; compute_beacon_block_reward works on the same state without a transition. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#1839](https://github.com/ChainSafe/lodestar/pull/1839), [teku#4703](https://github.com/Consensys-Incorporated/teku/pull/4703), [lodestar#9736](https://github.com/ChainSafe/lodestar/pull/9736)

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


<a id="block_production-086"></a>
<details>
<summary><b>block_production-086</b> Clone head state shortly before proposal — <i>implemented · low · S · latency</i></summary>

**Idea.** When a local validator is about to propose, clone the head state ~500ms before slot start and cache it, then move it into block production. The expensive state clone is off the critical path.

**Impact.** None left: LH#4925's pre-clone became unnecessary with tree-states, because clones are O(1)-ish structural shares and the slot advance happens in the timer.

**Best measured result.** shave 250-500ms off block production (pr:lighthouse#4925)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/state_advance_timer.rs:257`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L257) advance_head advances the head state one slot before the slot and caches it
- [`beacon_node/beacon_chain/src/block_production/mod.rs:89`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_production/mod.rs#L89) production takes the advanced state via get_advanced_hot_state
- [`beacon_node/store/src/hot_cold_store.rs:1196`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1196) get_advanced_hot_state_from_cache returns a milhouse clone (structural sharing, cheap)

**Skeptic check.** The PR itself said it would not be needed after tree-states. The current code clones from the state cache cheaply and advances ahead of time, so the critical-path cost the idea targets no longer exists.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#4925](https://github.com/sigp/lighthouse/pull/4925)

</details>


<a id="block_production-087"></a>
<details>
<summary><b>block_production-087</b> Gossip pre-merged candidate block bodies from non-proposers — <i>n/a · low · cpu, latency</i></summary>

**Idea.** Let non-proposer nodes pack and merge candidate block-body proofs ahead of time and gossip them, so the proposer adopts a ready body instead of doing the multi-second merge itself.

**Impact.** Specific to ethlambda lean consensus proof aggregation; Lighthouse has no such block body.

**Best measured result.** merge ~2.4s off proposer; candidate reached peers median t+1210ms (pr:ethlambda#604)

**Evidence (Lighthouse @ 928b61e719).**

- No lean-consensus proof merging in Lighthouse

**Sources.** [ethlambda#604](https://github.com/lambdaclass/ethlambda/pull/604)

</details>


<a id="block_production-088"></a>
<details>
<summary><b>block_production-088</b> Proposal state with warm tree-hash cache — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Produce blocks from a state that already carries a built tree-hash cache (or compute hashTreeRoot during next-slot preparation), so computing the new state root at proposal time only rehashes changed parts instead of rebuilding the whole tree.

**Impact.** None left: milhouse keeps hashes in the tree, so the proposal state root rehashes only the changed subtrees.

**Best measured result.** block production sped up 200-400ms, now &lt;=300ms from 400-600ms (pr:lighthouse#2106)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/state_advance_timer.rs:343`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L343) update_tree_hash_cache on the advanced state before caching it
- [`beacon_node/store/src/hot_cold_store.rs:1170`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1170) states loaded on a cache miss get update_tree_hash_cache before being cached
- [`beacon_node/beacon_chain/src/beacon_chain.rs:6553`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L6553) the proposal state root only rehashes the nodes dirtied by the block

**Skeptic check.** Verified that the advanced state is hashed in the timer and that milhouse retains internal node hashes across clones. The re-org and cache-miss paths also hash before caching. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#2106](https://github.com/sigp/lighthouse/pull/2106), [lodestar#6195](https://github.com/ChainSafe/lodestar/pull/6195)

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

**Verdict history.** not (checked) → partial (refuted)

**Sources.** [teku#9122](https://github.com/Consensys-Incorporated/teku/pull/9122)

</details>


<a id="block_production-090"></a>
<details>
<summary><b>block_production-090</b> Prefill shuffling cache before attestation packing — <i>implemented · low · S · latency, cpu</i></summary>

**Idea.** Before packing attestations, populate the shuffling/committee cache from the proposal state, so a cache miss during packing cannot abort or stall block production.

**Impact.** None: packing in LH never depends on the global shuffling cache, so a miss there cannot abort production.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:5880`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5880) build_committee_cache(Current) on the proposal state before packing
- [`beacon_node/beacon_chain/src/block_production/gloas.rs:406`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_production/gloas.rs#L406) same on the Gloas path
- [`beacon_node/operation_pool/src/attestation.rs:96`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation.rs#L96) Altair+ AttMaxCover uses the attesting indices stored in the pool, with no committee lookup
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2739`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2739) filter_op_pool_attestation compares shuffling decision roots via fork choice, not the shuffling cache
- [`consensus/state_processing/src/per_block_processing.rs:186`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing.rs#L186) Previous/Current committee caches built on the state before verification

**Skeptic check.** Confirmed that packing and the final block verification use only state-embedded committee caches, which are built on the proposal state. The Lodestar failure mode (a shuffling-cache miss during packing) has no counterpart in LH. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#10285](https://github.com/ChainSafe/lodestar/pull/10285)

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

**Verdict history.** not (checked) → not (refuted)

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

**Verdict history.** not (checked) → partial (refuted)

**Sources.** [grandine@06bdb7cfe](https://github.com/grandinetech/grandine/commit/06bdb7cfefe8)

</details>


<a id="block_production-093"></a>
<details>
<summary><b>block_production-093</b> Cache produced block per slot for duplicate requests — <i>not · low · S · cpu, latency</i></summary>

**Idea.** Cache the block produced for a slot in the beacon node and return it if the produce-block endpoint is called again (e.g. by multiple validator clients), instead of building it again.

**Gap in Lighthouse.** Add a small per-slot cache keyed by (slot, randao, graffiti, boost) in produce_block_v3 returning the prior BeaconBlockResponseWrapper.

**Impact.** Only helps when several VCs or retries request the same block; negligible for single-VC mainnet nodes.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/produce_block.rs:137`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/produce_block.rs#L137) - v3 handler calls produce_block_with_verification each time
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5237`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5237) - no per-slot produced-block cache
- [`validator_client/validator_services/src/block_service.rs:252`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/block_service.rs#L252) - VC calls BNs sequentially via first_success

**Sources.** [teku#8773](https://github.com/Consensys-Incorporated/teku/pull/8773)

</details>


<a id="block_production-094"></a>
<details>
<summary><b>block_production-094</b> Produce from in-memory head state, not store — <i>implemented · low · S · disk, latency</i></summary>

**Idea.** Build the block on a copy of the in-memory head state rather than loading the base state from the fork choice store or disk.

**Impact.** Production starts from the cached pre-advanced head state in the normal case; disk load (state_at_slot) is only for producing on a non-head parent.

**Best measured result.** described as much faster (pr:caplin#13051)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_production/mod.rs:84`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_production/mod.rs#L84)
- [`beacon_node/beacon_chain/src/block_production/mod.rs:78`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_production/mod.rs#L78)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5870`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5870)

**Skeptic check.** Verified the continuation branch uses store.get_advanced_hot_state filled by the state advance timer; only the conflicting-head branch replays from store. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [caplin#13051](https://github.com/erigontech/erigon/pull/13051)

</details>


<a id="block_production-095"></a>
<details>
<summary><b>block_production-095</b> Proposer reorg of late weak head — <i>implemented · low · S · latency</i></summary>

**Idea.** When proposing, compute the proposer head (get_proposer_head) and build on the parent of a late, weakly voted head under strict conditions, suppressing forkchoiceUpdated for such heads and predicting it in the previous slot so the state is prepared early.

**Impact.** Already present (Lighthouse is the origin of this feature, PR 2860).

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_production/mod.rs:69`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_production/mod.rs#L69) load_state_for_block_production tries get_state_for_re_org first
- [`beacon_node/beacon_chain/src/block_production/mod.rs:181-290`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_production/mod.rs#L181-L290) get_state_for_re_org: get_proposer_head conditions, builds on parent_node, uses cached advanced parent state
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5284-5392`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5284-L5392) payload attributes computed for proposer_head = head parent
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5500-5534`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5500-L5534) overridden_forkchoice_update_params via get_preliminary_proposer_head suppresses FCU of weak head

**Skeptic check.** Verified the re-org path in block_production/mod.rs (the earlier cite pointed at beacon_chain.rs, where get_state_for_re_org no longer lives) and the FCU override with previous-slot prediction. Upheld.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#12075](https://github.com/OffchainLabs/prysm/pull/12075), [lighthouse#2860](https://github.com/sigp/lighthouse/pull/2860), [lodestar#6652](https://github.com/ChainSafe/lodestar/pull/6652)

</details>


<a id="block_production-096"></a>
<details>
<summary><b>block_production-096</b> Keep proposer signature outside aggregated attestation proof — <i>n/a · low · cpu, latency</i></summary>

**Idea.** Carry the proposer signature next to the aggregated attestation proof rather than inside it, so the attestation aggregate can be built before the block root is known and blocks without attestations need no prover call.

**Impact.** Lean consensus aggregated-proof design; Lighthouse has no proof/prover stage.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/attestation_storage.rs:593`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs#L593) plain on-chain aggregates, no proof

**Sources.** [ethlambda#467](https://github.com/lambdaclass/ethlambda/pull/467)

</details>


<a id="block_production-097"></a>
<details>
<summary><b>block_production-097</b> Pack single best proof per data, no merging — <i>n/a · low · cpu, latency</i></summary>

**Idea.** When building a block, keep only the best-coverage proof per attestation data and do not merge same-data proofs (make merging optional, default off), removing the recursive prover merge cost at the price of some coverage.

**Impact.** Concerns recursive proof merging; Lighthouse merges are bitfield unions.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/attestation_storage.rs:593`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs#L593) compute_on_chain_aggregate is cheap bit merge

**Sources.** [ethlambda#473](https://github.com/lambdaclass/ethlambda/pull/473), [ethlambda#479](https://github.com/lambdaclass/ethlambda/pull/479)

</details>


<a id="block_production-098"></a>
<details>
<summary><b>block_production-098</b> Stop eth1 data voting work after deposit transition — <i>implemented · medium · S · memory, cpu</i></summary>

**Idea.** Once EIP-6110 deposit requests have taken over (eth1_deposit_index reached deposit_requests_start_index), skip eth1data voting in block production and prune the eth1 block cache, avoiding eth1 lookups and unbounded cache growth.

**Impact.** None needed: eth1_data is copied from the state and deposits are always empty on both pre-Gloas and Gloas production paths, so there are no eth1 lookups or eth1 block cache.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:5931`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5931)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5933`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5933)
- [`beacon_node/beacon_chain/src/block_production/gloas.rs:423`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_production/gloas.rs#L423)
- [`beacon_node/beacon_chain/src/block_production/gloas.rs:425`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_production/gloas.rs#L425)

**Skeptic check.** Verified both produce_partial_beacon_block and the Gloas producer hard-code deposits = vec![] and copy state.eth1_data(); Lighthouse goes further than the idea (no eth1 voting at all). Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [grandine@11239f188](https://github.com/grandinetech/grandine/commit/11239f18821e), [prysm#14835](https://github.com/OffchainLabs/prysm/pull/14835), [grandine@351f52c02](https://github.com/grandinetech/grandine/commit/351f52c02d55), [grandine@c62b55c72](https://github.com/grandinetech/grandine/commit/c62b55c728dc)

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

**Verdict history.** not (checked) → partial (refuted)

**Sources.** [lodestar#6431](https://github.com/ChainSafe/lodestar/pull/6431), [prysm#14442](https://github.com/OffchainLabs/prysm/pull/14442)

</details>


<a id="block_production-101"></a>
<details>
<summary><b>block_production-101</b> Remove builder status check from proposal path — <i>implemented · low · S · latency</i></summary>

**Idea.** Do not call the builder status endpoint during block proposal; check builder reachability only at startup or in the background.

**Impact.** No builder status call on any path, including proposal.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/builder_client/src/pre_gloas_builder_http_client.rs:407`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/builder_client/src/pre_gloas_builder_http_client.rs#L407) get_builder_status defined but has no callers anywhere in the tree
- [`beacon_node/http_api/src/produce_block.rs:137`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/produce_block.rs#L137) produce_block_v3 path

**Skeptic check.** The earlier note said grep found no status call in builder_client; in fact get_builder_status exists, but a tree-wide grep shows it is never called, so the proposal path does not pay for it. Upheld.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#11052](https://github.com/OffchainLabs/prysm/pull/11052)

</details>


<a id="block_production-102"></a>
<details>
<summary><b>block_production-102</b> Drop duplicate pool deletion in proposal — <i>implemented · low · S · cpu</i></summary>

**Idea.** Do not delete included attestations from the pool in the block proposal path, since block import already removes them.

**Impact.** No deletion in the proposal path.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/lib.rs:345`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L345) get_attestations reads only
- [`beacon_node/operation_pool/src/lib.rs:455`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L455) prune_attestations by epoch
- [`beacon_node/operation_pool/src/attestation_storage.rs:632`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs#L632) prune retains by target epoch

**Skeptic check.** Confirmed that the op pool has no per-attestation removal on proposal; pool cleanup is epoch-based pruning only. Upheld.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#6911](https://github.com/OffchainLabs/prysm/pull/6911)

</details>


<a id="block_production-103"></a>
<details>
<summary><b>block_production-103</b> No proposer preparation from validator registration — <i>implemented · low · S · cpu</i></summary>

**Idea.** Do not trigger proposer preparation (prepare_beacon_proposer) from validator registration calls; rely on the scheduled preparation routine, avoiding duplicate calls and a forced early epoch transition to compute expected withdrawals.

**Impact.** Already decoupled.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/validator/mod.rs:780-790`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validator/mod.rs#L780-L790) register_validator only calls update_proposer_preparation and leaves the work to the scheduled prepare_beacon_proposer
- [`beacon_node/beacon_chain/src/proposer_prep_service.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/proposer_prep_service.rs) scheduled routine

**Skeptic check.** Read the register_validator handler: it updates the cache, then forwards to the builder in a spawned task, with no prepare_beacon_proposer call. Only the separate prepare_beacon_proposer endpoint (mod.rs:1071) triggers it, which is outside this idea. Upheld.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#9314](https://github.com/sigp/lighthouse/pull/9314)

</details>


<a id="block_production-104"></a>
<details>
<summary><b>block_production-104</b> Single-pass committee bits for Electra on-chain aggregates — <i>implemented · low · S · cpu</i></summary>

**Idea.** When building Electra on-chain aggregates for block packing, set committee bits in a single pass and sort by committee index with a direct getter, instead of redundant loops and repeated committee bit index extraction.

**Impact.** Sorting is implicit (BTreeMap); bit operations are on a 64-bit vector and negligible.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/attestation_storage.rs:593-601`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs#L593-L601) compute_on_chain_aggregate pops BTreeMap in committee order
- [`beacon_node/operation_pool/src/attestation_storage.rs:279-310`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs#L279-L310) aggregate_with_disjoint_committees unions committee_bits per merge

**Skeptic check.** Lighthouse builds on-chain aggregates in committee order at pool aggregation time, with no re-sort and no repeated index-extraction loops. Each merge still runs a few small bitvector passes (intersection, highest_set_bit, num_set_bits), which is immaterial. Upheld.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#15108](https://github.com/OffchainLabs/prysm/pull/15108)

</details>


<a id="block_production-105"></a>
<details>
<summary><b>block_production-105</b> No separate speculative advanced head state — <i>implemented · low · S · memory, cpu</i></summary>

**Idea.** Do not keep a separately maintained speculative advanced head state; compute from the canonical head state on demand, avoiding maintaining a duplicate state.

**Impact.** No duplicate speculative state.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_production/mod.rs:84-90`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_production/mod.rs#L84-L90) continuation path uses store.get_advanced_hot_state from the state cache
- [`beacon_node/beacon_chain/src/state_advance_timer.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs) advances head state into the state cache

**Skeptic check.** The idea is an old Lighthouse commit that removed the speculative state. Current code has no separate speculative or advanced head snapshot: advanced states live in the general state cache. Upheld.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse@682081ef0](https://github.com/sigp/lighthouse/commit/682081ef072c)

</details>


<a id="block_production-106"></a>
<details>
<summary><b>block_production-106</b> Keep recent payload envelopes in memory — <i>partial · low · S · disk, latency</i></summary>

**Idea.** After persisting payload envelopes, keep the last two (head and parent) in memory so next-slot block production reads them synchronously instead of loading them from the database.

**Gap in Lighthouse.** Only the head envelope is kept in memory (CachedHead.snapshot.execution_envelope). The head.parent envelope is not cached, so get_state_for_re_org and the parent!=head branch of the withdrawals calculation read the DB. recompute_head re-reads a freshly persisted envelope from hot_db instead of reusing the imported one. GossipVerifiedPayloadBid::new -&gt; parent_payload_exits_builder reads the parent summary from hot_db for every bid, without checking cached_head.snapshot.execution_envelope first.

**Impact.** Removes a DB read per gossip bid (many per slot) and on re-org or head-change paths. Each read is small (summary, no body), so the impact is low.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_production/mod.rs:56-64`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_production/mod.rs#L56-L64) head envelope taken from cached head
- [`beacon_node/beacon_chain/src/block_production/mod.rs:265-270`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_production/mod.rs#L265-L270) re-org path reads parent envelope summary from DB
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5465-5480`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5465-L5480) withdrawals calc uses the cached head envelope only when parent==head, else DB
- [`beacon_node/beacon_chain/src/canonical_head.rs:1121-1128`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1121-L1128) the head-change path re-reads the just-persisted envelope summary from DB
- [`beacon_node/beacon_chain/src/payload_bid_verification/gossip_verified_bid.rs:162-185`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_bid_verification/gossip_verified_bid.rs#L162-L185) parent_payload_exits_builder hits hot_db for every gossip bid whose parent is full, even when the parent is the cached head
- [`beacon_node/store/src/hot_cold_store.rs:703-708`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L703-L708) get_payload_envelope_summary is an uncached hot_db.get

**Skeptic check.** The earlier evidence is right that normal production reads the head envelope from memory. But the idea keeps head and parent in memory, and Lighthouse keeps only the head, so re-org production and gossip bid verification still read the store.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [lodestar#9249](https://github.com/ChainSafe/lodestar/pull/9249), [lodestar#9260](https://github.com/ChainSafe/lodestar/pull/9260)

</details>


<a id="block_production-107"></a>
<details>
<summary><b>block_production-107</b> Reuse cached expected withdrawals in production — <i>not · low · S · cpu</i></summary>

**Idea.** When producing a block, reuse the expected withdrawals already computed and cached (e.g. during payload preparation) rather than recomputing them from the state.

**Gap in Lighthouse.** Pass withdrawals from execution_layer.payload_attributes cache into get_execution_payload (check head root/timestamp match) instead of get_expected_withdrawals on the production state.

**Impact.** Saves one withdrawals sweep per proposal (sub-ms to few ms); proposer nodes only.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/execution_payload.rs:306-307`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/execution_payload.rs#L306-L307) recomputes get_expected_withdrawals
- [`beacon_node/beacon_chain/src/beacon_chain.rs:6952-6990`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L6952-L6990) withdrawals cached only in EL payload_attributes
- [`beacon_node/beacon_chain/src/block_production/gloas.rs:1433-1450`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_production/gloas.rs#L1433-L1450) recomputes too

**Sources.** [lighthouse#4337](https://github.com/sigp/lighthouse/pull/4337), [lighthouse#9014](https://github.com/sigp/lighthouse/pull/9014)

</details>


<a id="block_production-108"></a>
<details>
<summary><b>block_production-108</b> Share body merkle branch across blob sidecar proofs — <i>n/a · low · S · cpu, latency</i></summary>

**Idea.** When building blob sidecar inclusion proofs, compute the block body merkle branch to the commitments once and reuse it for every blob, instead of regenerating the full proof per sidecar.

**Impact.** Production publishes data columns, which share one proof; per-blob path is test-only.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/data/blob_sidecar.rs:277-287`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/data/blob_sidecar.rs#L277-L287) per-blob BlobSidecar::new rebuilds tree; only used in test_utils.rs:3676
- [`beacon_node/beacon_chain/src/kzg_utils.rs:318-319`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/kzg_utils.rs#L318-L319) column path computes proof once
- [`beacon_node/http_api/src/publish_blocks.rs:449`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/publish_blocks.rs#L449),466 builds columns only

**Sources.** [lighthouse#5060](https://github.com/sigp/lighthouse/pull/5060)

</details>


<a id="block_production-109"></a>
<details>
<summary><b>block_production-109</b> Single endpoint choosing blinded or full block — <i>implemented · low · S · latency, bandwidth</i></summary>

**Idea.** Provide one block production endpoint where the beacon node decides server-side between returning a full or blinded block, so the VC makes one request instead of trying builder and local flows separately.

**Impact.** Already a single request from the VC.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/produce_block.rs:137`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/produce_block.rs#L137) produce_block_v3
- [`validator_client/validator_services/src/block_service.rs:502-519`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/block_service.rs#L502-L519) VC calls get_validator_block_and_publish_block (v3) with builder_boost_factor

**Skeptic check.** Confirmed that the VC makes one v3 request and the BN chooses blinded or full on the server side. Upheld.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#4629](https://github.com/sigp/lighthouse/pull/4629)

</details>


<a id="block_production-110"></a>
<details>
<summary><b>block_production-110</b> Size attestation selection buffers by new attesters — <i>implemented · low · S · memory</i></summary>

**Idea.** In attestation packing, size per-candidate selection slices by the number of attesters with new flags, not by committee size, to avoid reserving unused memory.

**Impact.** Covering sets are HashMaps built by filter_map over attesting indices, skipping validators already in the reward cache; no committee-sized buffers.

**Best measured result.** up to ~74 MB with a full pool (pr:caplin#24798)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/attestation.rs:96`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation.rs#L96)
- [`beacon_node/operation_pool/src/attestation.rs:103`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation.rs#L103)
- [`beacon_node/operation_pool/src/attestation.rs:23`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation.rs#L23)

**Skeptic check.** Verified AttMaxCover::new_for_altair_or_later collects only fresh attesters with non-zero reward into a HashMap that grows from the filtered count. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [caplin#24798](https://github.com/erigontech/erigon/pull/24798)

</details>


<a id="block_production-111"></a>
<details>
<summary><b>block_production-111</b> Skip signature verification in own block state transition — <i>implemented · medium · S · cpu, latency</i></summary>

**Idea.** When computing the post-state root of a block the node itself built (and when importing that block), run the state transition with signature verification disabled, since the contents come from verified pools and the block is verified again on import.

**Impact.** None needed: the post-state root of a self-built block is computed with BlockSignatureStrategy::VerifyRandao (one signature) or NoVerification; operation signatures are not checked.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:6529`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L6529)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:6542`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L6542)
- [`beacon_node/beacon_chain/src/block_production/gloas.rs:855`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_production/gloas.rs#L855)
- [`beacon_node/http_api/src/produce_block.rs:44`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/produce_block.rs#L44)

**Skeptic check.** Verified per_block_processing in block production uses VerifyRandao/NoVerification on both fork paths; source PRs are all about the production state-root transition, which matches. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#4184](https://github.com/status-im/nimbus-eth2/pull/4184), [prysm#1434](https://github.com/OffchainLabs/prysm/pull/1434), [lodestar@f1ebe0599](https://github.com/ChainSafe/lodestar/commit/f1ebe05995fc), [teku#643](https://github.com/Consensys-Incorporated/teku/pull/643), [nimbus#3837](https://github.com/status-im/nimbus-eth2/pull/3837), [nimbus@a0aa230c4](https://github.com/status-im/nimbus-eth2/commit/a0aa230c4571)

</details>


<a id="block_production-112"></a>
<details>
<summary><b>block_production-112</b> Skip bid wait when no builders or bids — <i>implemented · low · S · latency</i></summary>

**Idea.** When no builders are configured and no bid for the parent is pooled, do not wait for the bid deadline; select the local block immediately.

**Impact.** No bid-deadline wait exists in Gloas production; local build is selected as soon as candidates are gathered.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_production/gloas.rs:1166-1191`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_production/gloas.rs#L1166-L1191) direct bids only requested when builder_config.builders is non-empty, else close_builder_bid_streams
- [`beacon_node/beacon_chain/src/block_production/gloas.rs:1193-1219`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_production/gloas.rs#L1193-L1219) gossip bid read synchronously from gossip_verified_payload_bid_cache.get_highest_bid, no deadline sleep

**Skeptic check.** Verified acquire_external_bid_candidates: no builders means no direct-bid request and the pooled gossip bid is a plain cache lookup with no timer. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#10423](https://github.com/ChainSafe/lodestar/pull/10423)

</details>


<a id="block_production-113"></a>
<details>
<summary><b>block_production-113</b> Skip blob sidecar construction after PeerDAS — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Once the data-column fork is active, do not build blob sidecars, their inclusion proofs or their verification on the proposer; build only data column sidecars.

**Impact.** Proposer builds only data column sidecars; the blob sidecar publish path is gone.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/publish_blocks.rs:436-460`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/publish_blocks.rs#L436-L460) spawn_build_data_sidecar_task builds only data columns
- [`beacon_node/http_api/src/publish_blocks.rs:466-490`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/publish_blocks.rs#L466-L490) build_data_columns via build_blob_data_column_sidecars, no blob sidecars or inclusion proofs
- [`consensus/types/src/data/blob_sidecar.rs:285`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/data/blob_sidecar.rs#L285) BlobSidecar::new only remains in a helper, not on the publish path

**Skeptic check.** publish_blocks.rs has no BlobSidecar construction at all; only column building remains. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#5759](https://github.com/sigp/lighthouse/pull/5759)

</details>


<a id="block_production-114"></a>
<details>
<summary><b>block_production-114</b> Skip builder for unregistered validators — <i>not · low · S · latency</i></summary>

**Idea.** For validators with no builder registration, do not request a builder header; go straight to local payload building.

**Gap in Lighthouse.** In determine_and_fetch_payload, treat builder_boost_factor == Some(0) (or unregistered proposer) as local-only and skip the relay call.

**Impact.** Saves a relay round trip for non-builder proposers; the local payload is fetched in parallel anyway so little latency gain.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/execution_layer/src/lib.rs:1112-1160`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/lib.rs#L1112-L1160) builder used whenever configured and healthy; no registration check
- [`beacon_node/execution_layer/src/lib.rs:1077`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/lib.rs#L1077) relay and local fetched concurrently
- [`validator_client/lighthouse_validator_store/src/lib.rs:931-953`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/lighthouse_validator_store/src/lib.rs#L931-L953) VC sends boost 0 if builder_proposals=false but BN still queries relay

**Sources.** [prysm#11023](https://github.com/OffchainLabs/prysm/pull/11023)

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


<a id="block_production-116"></a>
<details>
<summary><b>block_production-116</b> No deep copies in block-under-construction setters — <i>n/a · low · S · cpu, memory</i></summary>

**Idea.** Do not deep-copy fields when setting them on a block under construction, since the proposer is the only writer and block building is latency-critical.

**Impact.** Rust moves values into the block; no deep-copy setters exist.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_production/mod.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_production/mod.rs) blocks are built by value

**Sources.** [prysm#11795](https://github.com/OffchainLabs/prysm/pull/11795)

</details>


<a id="block_production-117"></a>
<details>
<summary><b>block_production-117</b> Skip boosted value math at default boost factor — <i>partial · low · S · cpu</i></summary>

**Idea.** When the builder boost factor is the default (100), return the plain relay value without computing the boosted value.

**Gap in Lighthouse.** Treat Some(100) like None in the match in the relay-vs-local comparison.

**Impact.** Saves one U256 divide+multiply per proposal; negligible.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/execution_layer/src/lib.rs:1241`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/lib.rs#L1241) boost math always runs when Some(factor); None short-circuits

**Sources.** [lighthouse#5352](https://github.com/sigp/lighthouse/pull/5352)

</details>


<a id="block_production-118"></a>
<details>
<summary><b>block_production-118</b> Build blocks directly from grouped aggregated payloads — <i>n/a · low · S · cpu</i></summary>

**Idea.** Build blocks directly from aggregated payloads grouped by attestation data with greedy set-cover proof selection, instead of extracting per-validator attestations and then regrouping and re-selecting proofs.

**Gap in Lighthouse.** Lean consensus aggregated-payload design; Lighthouse op pool already stores attestations grouped by data.

**Impact.** None.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/lib.rs:345`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L345) get_attestations uses max-cover over compact attestations

**Sources.** [ethlambda#251](https://github.com/lambdaclass/ethlambda/pull/251)

</details>


<a id="block_production-119"></a>
<details>
<summary><b>block_production-119</b> Skip per-slot proposer state load without proposers — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** In per-slot payload-attribute refresh, return early when no local proposers are prepared, so the node does not load and advance the proposer state every slot for nothing.

**Impact.** Per-slot proposer prep is skipped when no local proposers are registered.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:6719-6741`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L6719-L6741) prepare_beacon_proposer returns Ok(None) before any state/head work when !always_prepare_payload and !has_any_proposer_preparation_data

**Skeptic check.** The early return comes before the spawn_blocking head read and get_pre_payload_attributes, which is the Teku mechanism. The head-state advance timer runs regardless, but it serves other duties, not payload-attribute prep.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#11526](https://github.com/Consensys-Incorporated/teku/pull/11526)

</details>


<a id="block_production-120"></a>
<details>
<summary><b>block_production-120</b> Skip re-verifying pool operation signatures when packing — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** When selecting attestations and other operations from the op pool for a block, do not re-verify their BLS signatures, since they were verified on pool insertion (optionally batch-verify only those not matching the canonical chain).

**Impact.** Block packing does no BLS re-verification of pooled ops by default.

**Best measured result.** 562,000 ns -&gt; 366 ns per BLS change; full block ~9.0 ms -&gt; ~5.9 us (pr:caplin#22850); expected ~1000x (pr:lighthouse#820)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/lib.rs:483-534`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L483-L534) get_slashings_and_exits uses signature_is_still_valid (fork-version check, no BLS)
- [`beacon_node/operation_pool/src/lib.rs:615-629`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L615-L629) get_voluntary_exits verify_exit with VerifySignatures::False
- [`beacon_node/operation_pool/src/lib.rs:674-706`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L674-L706) get_bls_to_execution_changes signature_is_still_valid only
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5992-6060`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5992-L6060) BLS re-check only under paranoid_block_proposal
- [`beacon_node/beacon_chain/src/chain_config.rs:164`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/chain_config.rs#L164) paranoid_block_proposal default false
- [`beacon_node/beacon_chain/src/beacon_chain.rs:6530`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L6530) block completion uses BlockSignatureStrategy::VerifyRandao

**Skeptic check.** All op-pool getters use SigVerifiedOp fork checks, not BLS; the Gloas production path is gated the same way (gloas.rs:502). Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#8135](https://github.com/OffchainLabs/prysm/pull/8135), [prysm#4513](https://github.com/OffchainLabs/prysm/pull/4513), [lighthouse@a474061ec](https://github.com/sigp/lighthouse/commit/a474061ec75c), [lodestar#2233](https://github.com/ChainSafe/lodestar/pull/2233), [caplin#22850](https://github.com/erigontech/erigon/pull/22850), [lighthouse#820](https://github.com/sigp/lighthouse/pull/820), [prysm#14225](https://github.com/OffchainLabs/prysm/pull/14225)

</details>


<a id="block_production-121"></a>
<details>
<summary><b>block_production-121</b> Skip duplicate sidecar publish after blinded submission — <i>implemented · low · S · bandwidth</i></summary>

**Idea.** After a blinded block is submitted and the relay publishes it, do not publish the data column sidecars again from the beacon node.

**Impact.** No duplicate block/column publish after builder submission.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/publish_blocks.rs:657-682`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/publish_blocks.rs#L657-L682) publish_blinded_block returns empty reply when reconstruct_block gives None
- [`beacon_node/http_api/src/publish_blocks.rs:734-743`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/publish_blocks.rs#L734-L743) reconstruct_block returns Ok(None) after propose_blinded_beacon_block, no sidecar publish

**Skeptic check.** After a successful builder submission the BN publishes neither the block nor columns; only a locally cached payload leads to a local publish. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [grandine#278](https://github.com/grandinetech/grandine/pull/278)

</details>


<a id="block_production-122"></a>
<details>
<summary><b>block_production-122</b> Skip signature checks for self-signed messages — <i>not · low · M · cpu</i></summary>

**Idea.** Route locally produced and API-submitted messages (blocks, attestations, others) through one path that skips signature verification for messages the node signed itself before adding them to pools.

**Gap in Lighthouse.** Add a trusted path for API/locally signed messages that skips signature verification (e.g. in verify_and_publish_attestation and block gossip verification), but the VC is a separate process so trust is debatable.

**Impact.** Saves roughly one BLS verify per own attestation/block (sub-ms each); only on nodes with local validators.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/publish_attestations.rs:77`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/publish_attestations.rs#L77) API attestations go through verify_unaggregated_attestation_for_gossip with full signature check
- [`beacon_node/http_api/src/publish_blocks.rs:355`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/publish_blocks.rs#L355) locally built block still gossip-verified incl. proposer signature

**Sources.** [nimbus#3829](https://github.com/status-im/nimbus-eth2/pull/3829)

</details>


<a id="block_production-123"></a>
<details>
<summary><b>block_production-123</b> Skip repacking operations after an earlier failure — <i>n/a · low · S · cpu</i></summary>

**Idea.** In block production, do not repack attestations and deposits if an earlier step failed and they were already set empty.

**Gap in Lighthouse.** Lighthouse has no empty-then-repack flow in produce_partial_beacon_block.

**Impact.** None.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:5983`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5983) attestations fetched once; errors propagate with ? rather than empty-then-repack

**Sources.** [prysm#11987](https://github.com/OffchainLabs/prysm/pull/11987)

</details>


<a id="block_production-124"></a>
<details>
<summary><b>block_production-124</b> Ignore unaggregated attestations when packing blocks — <i>n/a · low · S · cpu, latency</i></summary>

**Idea.** When packing attestations, consider only aggregates and skip unaggregated single attestations from subscribed subnets, since considering all of them makes production slow.

**Gap in Lighthouse.** Lighthouse aggregates pool attestations on insertion and max-covers, so the Teku slowdown does not occur.

**Impact.** None; dropping unaggregated would reduce block quality.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/lib.rs:345`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L345) get_attestations; unaggregated attestations are aggregated into pool entries on insert (line 220-231 region)

**Sources.** [teku#9222](https://github.com/Consensys-Incorporated/teku/pull/9222)

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


<a id="block_production-126"></a>
<details>
<summary><b>block_production-126</b> Sort aggregates by size before packing — <i>implemented · low · S · cpu</i></summary>

**Idea.** Sort per-slot aggregates by size so the largest aggregates are chosen first when packing, so large Electra aggregates are not discarded.

**Impact.** The largest aggregate per committee is chosen and max cover ranks by coverage, so large Electra aggregates are not dropped by insertion order.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/attestation_storage.rs:489-583`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs#L489-L583) aggregate_across_committees keeps the attestation with the most aggregation bits per committee before building the on-chain aggregate
- [`beacon_node/operation_pool/src/max_cover.rs:53`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/max_cover.rs#L53) greedy maximum_cover picks the highest-score item each round
- [`beacon_node/operation_pool/src/lib.rs:428-451`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L428-L451) prev/curr max cover then merge_solutions

**Skeptic check.** Beyond the max-cover argument from earlier, the per-committee selection in aggregate_across_committees explicitly compares num_set_bits, which is the Teku size-ordering effect.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#9114](https://github.com/Consensys-Incorporated/teku/pull/9114)

</details>


<a id="block_production-127"></a>
<details>
<summary><b>block_production-127</b> Split max-cover per epoch and run parallel — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Run attestation max-cover packing as two independent instances, one for previous-epoch and one for current-epoch attestations, in parallel. Max cover is O(n^2), so splitting halves the work.

**Impact.** Packing split per epoch and run in parallel.

**Best measured result.** reduces computation by roughly half (pr:lighthouse#2307)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/lib.rs:428-442`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L428-L442) rayon::join of prev-epoch and curr-epoch maximum_cover
- [`beacon_node/operation_pool/src/lib.rs:447`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L447) merge_solutions

**Skeptic check.** Code matches lighthouse#2307 exactly. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#2307](https://github.com/sigp/lighthouse/pull/2307)

</details>


<a id="block_production-128"></a>
<details>
<summary><b>block_production-128</b> Advance head state more than one slot — <i>implemented · medium · S · cpu, latency</i></summary>

**Idea.** Let the head-state advance run more than one slot ahead so epoch processing is precomputed and cached before proposal, and prune the op pool using the finalized state.

**Impact.** The head state is advanced across skipped slots, so epoch boundaries are precomputed; the op pool is pruned using the finalized state.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/state_advance_timer.rs:38`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L38) MAX_ADVANCE_DISTANCE = 256
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:281-284`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L281-L284) get_advanced_hot_state reuses already-advanced state, StateAlreadyAdvanced guard removed
- [`beacon_node/beacon_chain/src/canonical_head.rs:1704-1716`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1704-L1716) op_pool.prune_all with new_finalized_state
- [`beacon_node/operation_pool/src/lib.rs:739-751`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L739-L751) prune_all prunes slashings/exits using finalized_state

**Skeptic check.** Both halves of lighthouse#8156 are present: the single-slot guard is gone, the distance is 256, and finalized-state pruning is in place. Earlier evidence covered only the advance half; the pruning half is also verified.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#8156](https://github.com/sigp/lighthouse/pull/8156)

</details>


<a id="block_production-129"></a>
<details>
<summary><b>block_production-129</b> Lead-time cutoff for speculative state work — <i>n/a · low · cpu, latency</i></summary>

**Idea.** Start speculative payload-preparation state work (head-state copy plus slot processing) only when more than a larger lead (cutoff + 1/8 slot) remains, and re-check before the copy, so uncancellable state work does not compete with production near the builder cutoff.

**Impact.** Lighthouse has no speculative payload-preparation state copy tied to a builder cutoff; advance runs at a fixed time and production loads its own state.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/state_advance_timer.rs:125-131`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L125-L131) fixed 3/4-slot offset, no builder cutoff
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5849-5875`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5849-L5875) production runs complete_state_advance on its own state

**Sources.** [caplin#25029](https://github.com/erigontech/erigon/pull/25029)

</details>


<a id="block_production-130"></a>
<details>
<summary><b>block_production-130</b> Stop deposit packing at per-block maximum — <i>n/a · low · cpu</i></summary>

**Idea.** When packing deposits, stop collecting eligible pending deposits once the per-block maximum is reached, instead of looping over all of them.

**Impact.** Lighthouse no longer packs eth1 deposits into blocks (empty vec); post-Electra deposits come via execution requests.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:5933`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5933) let deposits = vec![]

**Sources.** [prysm#9806](https://github.com/OffchainLabs/prysm/pull/9806)

</details>


<a id="block_production-131"></a>
<details>
<summary><b>block_production-131</b> Stop adding proofs once data has supermajority — <i>n/a · low · cpu, latency</i></summary>

**Idea.** When packing attestations, stop adding partial proofs for an attestation data once its voters cross 2/3, and pick a single proof if it alone exceeds 2/3, avoiding recursive proof merges with no consensus value.

**Impact.** Lean-consensus recursive proof merging; Lighthouse merges BLS signatures cheaply.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/lib.rs:428`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L428) max-cover over BLS aggregates

**Sources.** [ethlambda#472](https://github.com/lambdaclass/ethlambda/pull/472)

</details>


<a id="block_production-132"></a>
<details>
<summary><b>block_production-132</b> Tiered greedy attestation selection, one state transition — <i>n/a · low · cpu, latency</i></summary>

**Idea.** Choose block attestations with a tiered greedy over a projected state (finalize, then justify, then most voters), projecting justification incrementally, so the state transition runs once instead of once per fixed-point round.

**Impact.** Lighthouse's max-cover does not run a state transition per fixed-point round; the problem is lean-consensus specific.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/lib.rs:400-450`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L400-L450) greedy max-cover without state transition per round

**Sources.** [ethlambda#382](https://github.com/lambdaclass/ethlambda/pull/382)

</details>


<a id="block_production-133"></a>
<details>
<summary><b>block_production-133</b> Release locks early in block production — <i>implemented · low · S · latency</i></summary>

**Idea.** Drop locks (such as on the cached production state) as early as possible in block production, so concurrent production requests run in parallel instead of serializing.

**Impact.** No cached block-production-state mutex remains; concurrent requests load the advanced state independently.

**Best measured result.** 4 concurrent requests: 1026ms -&gt; 459ms for the last (pr:lighthouse#5368)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_production/mod.rs:43-100`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_production/mod.rs#L43-L100)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5252-5263`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5252-L5263)

**Skeptic check.** Verified load_state_for_block_production only clones values out of cached_head in a short scope and calls get_advanced_hot_state with no lock held; the old production-state lock PR 5368 shortened no longer exists. The naive_aggregation_pool read guard is held across the whole op-pool import loop (block_production/gloas.rs:438, beacon_chain.rs:5947), but that is a separate issue, not this idea.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#5368](https://github.com/sigp/lighthouse/pull/5368)

</details>


<a id="block_production-134"></a>
<details>
<summary><b>block_production-134</b> Timeout headroom for event-loop lag — <i>n/a · low · latency</i></summary>

**Idea.** Give block production and builder request timeouts headroom for scheduler/event-loop lag (GC, other work), so valid builder blocks are not rejected as late.

**Impact.** No GC or single event loop; tokio multi-thread runtime, lag headroom not a meaningful issue.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/builder_client/src/pre_gloas_builder_http_client.rs:35`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/builder_client/src/pre_gloas_builder_http_client.rs#L35) fixed 1000ms get_header timeout

**Sources.** [lodestar#7420](https://github.com/ChainSafe/lodestar/pull/7420)

</details>


<a id="block_production-135"></a>
<details>
<summary><b>block_production-135</b> Validate packed attestations without mutating state — <i>implemented · medium · S · cpu, memory, latency</i></summary>

**Idea.** When packing pool attestations, validate them against the state without processing them (no state mutation or copy), removing state copies from the proposer hot path.

**Impact.** None needed: packing filters by slot window, memoized shuffling compatibility and participation-flag computation against &amp;BeaconState; no attestation processing or state copy (full verification only in opt-in paranoid_block_proposal).

**Best measured result.** proposal &gt;250ms seen in 50+ profiles (pr:prysm#12704)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/lib.rs:317`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L317)
- [`beacon_node/operation_pool/src/lib.rs:345`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L345)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2739`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2739)
- [`beacon_node/operation_pool/src/attestation.rs:76`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation.rs#L76)

**Skeptic check.** Verified get_attestations/get_valid_attestations_for_epoch and filter_op_pool_attestation take immutable state refs; the only per-attestation verification (verify_attestation_for_block_inclusion) is behind paranoid mode and also does not mutate. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

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


<a id="block_production-137"></a>
<details>
<summary><b>block_production-137</b> Weighted attestation ranking by count, delay, diversity — <i>partial · low · Add tie-break terms in AttMaxCover::score / max_cover selection. · cpu</i></summary>

**Idea.** Aggregate attestations with equal data and rank packing candidates by validator count, inclusion delay and committee diversity.

**Gap in Lighthouse.** Pool already aggregates equal-data attestations and packs with max-cover by proposer reward, but no inclusion-delay or committee-diversity tie-breaking.

**Impact.** S

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/attestation.rs:176`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation.rs#L176) score is reward-only
- [`beacon_node/operation_pool/src/lib.rs:384`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L384) aggregate_across_committees
- [`beacon_node/operation_pool/src/max_cover.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/max_cover.rs) max-cover selection

**Sources.** [teku#9186](https://github.com/Consensys-Incorporated/teku/pull/9186)

</details>


<a id="block_production-138"></a>
<details>
<summary><b>block_production-138</b> Proposer delays request for more builder bids — <i>not · low · Add optional sleep before get_header in execution_layer builder fetch, clamped to attestation deadline. · latency</i></summary>

**Idea.** Optionally delay the proposal request within the slot (clamped before the attestation deadline) so builders accrue more bids, with a configurable builder getHeader timeout.

**Gap in Lighthouse.** Lighthouse requests builder bids immediately at proposal; only timeout configurable, no delayed request.

**Impact.** S

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/builder_client/src/pre_gloas_builder_http_client.rs:35`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/builder_client/src/pre_gloas_builder_http_client.rs#L35) only a header timeout, no pre-request delay
- [`beacon_node/http_api/src/produce_block.rs:151`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/produce_block.rs#L151) builder_boost_factor only

**Sources.** [prysm#17224](https://github.com/OffchainLabs/prysm/pull/17224)

</details>


<a id="block_production-139"></a>
<details>
<summary><b>block_production-139</b> Return early from proposer reorg logic when disabled — <i>implemented · low · S · cpu</i></summary>

**Idea.** When proposer reorgs are disabled, return at the top of the reorg decision before computing head and parent weights or loading fork-choice data. Check whether Lighthouse's proposer-reorg path does the weight checks even when the feature is off.

**Impact.** Both proposer-reorg paths return before any fork-choice weight work when reorgs are disabled.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_production/mod.rs:187-189`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_production/mod.rs#L187-L189) get_state_for_re_org returns None when disable_proposer_reorg is set
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5524-5526`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5524-L5526) overridden_forkchoice_update_params_or_failure_reason returns ReOrgsDisabled before fork_choice_read_lock

**Skeptic check.** Both early returns sit at the top of their functions, before the slot clock read and the fork-choice lock with get_preliminary_proposer_head. This matches PR #9926, so the earlier evidence is right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#9926](https://github.com/sigp/lighthouse/pull/9926)

</details>


<a id="block_production-140"></a>
<details>
<summary><b>block_production-140</b> Poll fork choice within slot to refresh head — <i>n/a · low · latency</i></summary>

**Idea.** Poll fork choice several times within a slot and wake the sync or production stage when the head changes without a new block arriving. Block production then reads a current head instead of waiting for the next slot.

**Impact.** Lighthouse head is event-driven (block, envelope, slot start, late-slot advance), no separate synced-head stage that can go stale.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:7496`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L7496) per_slot_task recompute_head_at_current_slot at slot start
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:212`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L212) recompute_head_at_slot(next_slot) late in slot
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:1008`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L1008) etc: recompute_head after block/envelope events
- [`beacon_node/beacon_chain/src/block_production/mod.rs:57`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_production/mod.rs#L57) reads cached_head

**Sources.** [caplin#24545](https://github.com/erigontech/erigon/pull/24545)

</details>


<a id="block_production-141"></a>
<details>
<summary><b>block_production-141</b> Pack operations in place on one scratch state — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** When packing operations into a block, apply each candidate in place on a single scratch state, with each process step validating before writing, instead of cloning the state per candidate.

**Impact.** No per-candidate state clone during packing; candidates are validated read-only against one advanced state and applied once in block processing.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_production/gloas.rs:478-497`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_production/gloas.rs#L478-L497) attestation filters and get_payload_attestations borrow the one advanced &amp;state
- [`beacon_node/beacon_chain/src/block_production/gloas.rs:502-510`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_production/gloas.rs#L502-L510) paranoid re-check uses verify_attestation_for_block_inclusion on the same &amp;state, no clone
- [`beacon_node/operation_pool/src/lib.rs:242`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L242) get_payload_attestations read-only

**Skeptic check.** Verified selection paths in gloas.rs take &amp;state and never clone per candidate. Mechanism differs (read-only validation, not in-place apply) but the effect, no per-candidate clone, is the same; earlier verdict right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [ethlambda#646](https://github.com/lambdaclass/ethlambda/pull/646)

</details>


<a id="block_production-142"></a>
<details>
<summary><b>block_production-142</b> Return execution payload envelope with produced block — <i>implemented · low · S · latency</i></summary>

**Idea.** Have the beacon node return the unsigned execution payload envelope together with the produced block, so the validator client signs and publishes it without a second round trip.

**Impact.** The VC gets the unsigned envelope in the produce-block response; no second round trip when the payload is included.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/produce_block.rs:212-222`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/produce_block.rs#L212-L222) BlockAndEnvelope bundles block, envelope, kzg_proofs and blobs
- [`beacon_node/beacon_chain/src/block_production/gloas.rs:899-931`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_production/gloas.rs#L899-L931) envelope built, verified and returned with the block

**Skeptic check.** Confirmed in produce_block.rs: when payload_contents is Some, the v4 response carries the envelope. Earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#11147](https://github.com/Consensys-Incorporated/teku/pull/11147)

</details>


<a id="block_production-143"></a>
<details>
<summary><b>block_production-143</b> Reuse cached getPayload response for envelope and sidecars — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Cache the engine getPayload response from block production and reuse it to build the payload envelope and data column sidecars, avoiding a second EL call.

**Impact.** One getPayload result feeds the envelope and the blobs for sidecars; no second EL call.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_production/gloas.rs:917-925`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_production/gloas.rs#L917-L925) blobs_and_proofs taken from the single payload_data and cached with the envelope
- [`beacon_node/beacon_chain/src/pending_payload_envelopes.rs:10-60`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/pending_payload_envelopes.rs#L10-L60) PendingEnvelopeData keeps envelope and blobs

**Skeptic check.** Verified that the envelope and blobs come from the same payload_data and are cached in pending_payload_envelopes for publication. Earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#10015](https://github.com/Consensys-Incorporated/teku/pull/10015)

</details>


<a id="block_production-144"></a>
<details>
<summary><b>block_production-144</b> Read parent block hash directly from state header — <i>implemented · low · S · cpu</i></summary>

**Idea.** When building the execution payload attributes, read the parent block hash straight from the state's latest execution payload header instead of running merge-transition-complete checks and extra lookups.

**Impact.** The parent hash comes straight from the state header; no merge-transition checks remain in this file.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/execution_payload.rs:302-303`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/execution_payload.rs#L302-L303) block_hash read from state.latest_execution_payload_header()
- [`beacon_node/beacon_chain/src/execution_payload.rs:390`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/execution_payload.rs#L390) parent_hash = latest_execution_payload_header_block_hash

**Skeptic check.** Grep shows no is_merge_transition_complete or terminal-block lookups in execution_payload.rs; the parent hash is read directly. Earlier verdict right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#12951](https://github.com/OffchainLabs/prysm/pull/12951)

</details>


<a id="block_production-145"></a>
<details>
<summary><b>block_production-145</b> Prepare payload only for local proposers — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Before calling the EL to prepare a payload for the next slot, check that the next-slot proposer index belongs to a locally registered validator, and skip the preparation call otherwise.

**Impact.** Payload preparation runs only for locally registered next-slot proposers, unless always_prepare_payload is set.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:6736-6740`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L6736-L6740) early exit when no proposer preparation data at all
- [`beacon_node/beacon_chain/src/beacon_chain.rs:6895-6902`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L6895-L6902) has_proposer_preparation_data(proposer) early return before the fcU with attributes

**Skeptic check.** Confirmed both early returns in prepare_beacon_proposer. Earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [grandine#185](https://github.com/grandinetech/grandine/pull/185)

</details>


<a id="block_production-146"></a>
<details>
<summary><b>block_production-146</b> Check sync aggregate validity before PTC aggregation — <i>n/a · low · cpu</i></summary>

**Idea.** In block production, check whether the sync aggregate failed before doing payload-timeliness-committee vote aggregation, so signature decompressions are not wasted on a discarded result.

**Impact.** Lighthouse does no signature aggregation for PTC votes during block production, so there is nothing wasted to skip.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/lib.rs:242-260`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L242-L260) PTC attestations are selected and sorted, no BLS aggregation or decompression
- [`beacon_node/beacon_chain/src/block_production/gloas.rs:523`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_production/gloas.rs#L523) signature work only in paranoid mode

**Sources.** [caplin#24683](https://github.com/erigontech/erigon/pull/24683)

</details>


<a id="block_production-147"></a>
<details>
<summary><b>block_production-147</b> Builder bid carries only blob KZG commitments — <i>implemented · low · S · bandwidth, latency</i></summary>

**Idea.** In the blinded block flow, have the builder return only the blob KZG commitments in the bid rather than the full blob bundle, with the relay building the sidecars. The bid is smaller on the wire and the beacon node skips sidecar construction.

**Impact.** Builder bids carry only commitments; the BN builds no sidecars from the bid.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/execution_layer/src/lib.rs:109-128`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/lib.rs#L109-L128) builder bids map to PayloadAndBlobs with kzg_commitments only and blobs_and_proofs: None

**Skeptic check.** Verified that every post-Deneb BuilderBid arm sets blobs_and_proofs: None and takes only blob_kzg_commitments, as the builder spec requires. Earlier verdict right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#5598](https://github.com/status-im/nimbus-eth2/pull/5598)

</details>


