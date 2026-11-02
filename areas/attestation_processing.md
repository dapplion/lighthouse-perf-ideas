# attestation_processing

63 checked ideas, 16 actionable. [Back to the summary](../README.md).

## Actionable (16)

High or medium value, verdict `not` or `partial`.

<a id="attestation_processing-006"></a>
<details>
<summary><b>attestation_processing-006</b> Same-message signature check for equal-data attestations — <i>not · high · M · cpu, latency</i></summary>

**Idea.** Group unaggregated gossip attestations by (slot, attestation data root), aggregate the pubkeys and signatures of each group and do one signature check per group, falling back to per-attestation verification on failure. Verification cost scales with distinct data, not message count.

**Gap in Lighthouse.** Group the partially verified unaggregated attestations in batch_verify_unaggregated_attestations by signing root, aggregate pubkeys and signatures per group into one SignatureSet (or merge equal messages inside verify_signature_sets), keep the existing per-attestation fallback via from_indexed with CheckAttestationSignature::Yes.

**Impact.** Pairing work for gossip unaggregated batches (up to 64) drops from one hash-to-curve + Miller loop per attestation to one per distinct data; several-fold less BLS CPU on subscribed subnets.

**Best measured result.** 128 sigs: 130.5 ms vs 8.97 ms; CPU 140-160% vs &gt;=300% (pr:lodestar#5729)

**Evidence (Lighthouse @ 928b61e719).**

- [`crypto/bls/src/impls/blst.rs:36`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L36) verify_signature_sets builds one (msg, agg_pk, sig, rand) tuple per set, no grouping by message
- blst-0.3.17/src/lib.rs:1335 verify_multiple_aggregate_signatures has '// TODO - check msg uniqueness?' and runs mul_n_aggregate (hash-to-curve + Miller loop) per element
- [`beacon_node/beacon_chain/src/attestation_verification/batch.rs:170`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification/batch.rs#L170) one signature set per unaggregated attestation

**Second check.** Checked the blst 0.3.17 crate itself for message dedup in the multi-verify path: none, only a TODO. No grouping in batch.rs or the beacon processor.

**Sources.** [prysm#3493](https://github.com/OffchainLabs/prysm/pull/3493), [lodestar#5729](https://github.com/ChainSafe/lodestar/pull/5729), [lodestar#5896](https://github.com/ChainSafe/lodestar/pull/5896)

</details>

<a id="attestation_processing-008"></a>
<details>
<summary><b>attestation_processing-008</b> Aggregate attestations in pool before fork choice — <i>not · medium · M · cpu, latency</i></summary>

**Idea.** Save gossip and API attestations straight into the fork-choice pool and aggregate equal-data ones there before applying them to fork choice, instead of a periodic batching step with many separate on-attestation calls.

**Gap in Lighthouse.** No aggregation of equal-data attestations before fork choice. Lighthouse has no periodic batching step to replace (it applies immediately), and on_attestation is a per-validator latest-message update, so aggregating first would only save write-lock acquisitions.

**Impact.** Negligible: per-validator vote work is the same with or without pre-aggregation; only lock acquisitions are saved.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:2573`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2573) apply_attestation_to_fork_choice takes the fork choice write lock and calls on_attestation per verified attestation
- [`beacon_node/http_api/src/publish_attestations.rs:100`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/publish_attestations.rs#L100) API path applies each attestation to fork choice, then to the naive aggregation pool
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2596`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2596) naive aggregation pool is separate and feeds aggregate production, not fork choice

**Second check.** Looked for any queue that aggregates before on_attestation (fork choice queued_attestations, naive aggregation pool); neither feeds aggregated votes into fork choice.

**Sources.** [prysm#12337](https://github.com/OffchainLabs/prysm/pull/12337)

</details>

<a id="attestation_processing-009"></a>
<details>
<summary><b>attestation_processing-009</b> Batch-verify API-submitted attestations — <i>not · medium · S · cpu</i></summary>

**Idea.** Hand attestations submitted through the validator HTTP API to the verifier as one batch so their signatures are batch verified rather than one by one.

**Gap in Lighthouse.** In publish_attestations, call chain.batch_verify_unaggregated_attestations_for_gossip over the request's SingleAttestations, then publish/apply each verified result; keep the UnknownHeadBlock reprocess path for individual failures.

**Impact.** Only for nodes serving many local validators: roughly halves BLS cost of their POSTed attestations (more with 006); nothing for ordinary nodes.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/publish_attestations.rs:143`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/publish_attestations.rs#L143) blocking task maps over the request's attestations one by one
- [`beacon_node/http_api/src/publish_attestations.rs:76`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/publish_attestations.rs#L76) verify_and_publish_attestation calls verify_unaggregated_attestation_for_gossip (single signature check)
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:327`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L327) only caller of batch_verify_unaggregated_attestations_for_gossip outside tests

**Second check.** Confirmed the API path does not go through the beacon processor batching and no other batch caller exists.

**Sources.** [grandine@f8cf3c33f](https://github.com/grandinetech/grandine/commit/f8cf3c33ff1d), [grandine#198](https://github.com/grandinetech/grandine/pull/198)

</details>

<a id="attestation_processing-024"></a>
<details>
<summary><b>attestation_processing-024</b> Keep gossip aggregates out of fork choice — <i>not · medium · S · cpu</i></summary>

**Idea.** Store gossip aggregate-and-proof attestations only in the op pool for block inclusion and do not apply them to fork choice, since their votes arrive anyway via unaggregated attestations and blocks.

**Gap in Lighthouse.** Lighthouse applies every verified gossip aggregate to fork choice (iterating all attesting indices into proto_array.process_attestation) and then to the op pool. Would skip the apply_attestation_to_fork_choice call in process_gossip_aggregate_result (keep op pool insert), accepting reliance on unaggregates and blocks.

**Impact.** Removes a write-lock acquisition plus ~hundreds of vote updates per aggregate (about 100 aggregates/slot after dedup), so less fork choice lock contention; modest CPU saving. Risk: slightly later vote visibility for validators on few subnets.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:631`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L631) process_gossip_aggregate_result calls chain.apply_attestation_to_fork_choice(&amp;verified_aggregate)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2573`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2573) apply_attestation_to_fork_choice takes fork_choice_write_lock and on_attestation

**Sources.** [lodestar#1722](https://github.com/ChainSafe/lodestar/pull/1722)

</details>

<a id="attestation_processing-053"></a>
<details>
<summary><b>attestation_processing-053</b> Park unknown-root attestations from raw bytes — <i>not · medium · M · cpu, latency</i></summary>

**Idea.** Extract slot and block root from the serialized attestation bytes first and park unknown-root attestations in a bounded map for reprocessing on block arrival, instead of fully deserialising and validating them first.

**Gap in Lighthouse.** No raw-byte peek of slot/beacon_block_root before SSZ decode. Lighthouse would need to read the fixed offsets of SingleAttestation in pubsub decode or the gossip handler and park unknown-root messages before decode (including signature point decompression).

**Impact.** Small: post-Electra gossip attestations are fixed-size SingleAttestation, so the only real saving is G2 point decompression for attestations with unknown roots; the reprocess queue already parks them before signature verification.

**Best measured result.** up to 16,000 attestations reprocessed at once previously (pr:lodestar#5327)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/types/pubsub.rs:254`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/pubsub.rs#L254) SingleAttestation::from_ssz_bytes runs on every gossip attestation before any root check
- [`crypto/bls/src/generic_signature.rs:145-149`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/generic_signature.rs#L145-L149) signature bytes are decompressed (Sig::deserialize) during that decode
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:2874`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L2874) UnknownHeadBlock is reached only after decode and early verification

**Second check.** Checked pubsub.rs decode for every topic and the bls signature deserialize path; no byte-offset peek or pre-decode diversion exists anywhere, so the verdict stands.

**Sources.** [lodestar#5327](https://github.com/ChainSafe/lodestar/pull/5327)

</details>

<a id="attestation_processing-060"></a>
<details>
<summary><b>attestation_processing-060</b> Subtract absent keys from committee aggregate pubkey — <i>not · medium · M · cpu</i></summary>

**Idea.** Cache one aggregate pubkey per committee and for high-participation attestations subtract the absent validators' keys instead of loading and adding every attester key.

**Gap in Lighthouse.** No per-committee aggregate pubkey cache and no subtract-absent path. It would need a cache keyed by shuffling id and committee, a negate-and-add step in crypto/bls (blst has no subtract), and use in the attestation signature-set builders.

**Impact.** Fewer G1 additions in block-import and aggregate attestation signature checks at high participation; Prysm measured key aggregation dropping from 56 to 11.5 ms per block.

**Best measured result.** ExecuteStateTransition CPU 131.1 to 92.3 ms per block; AggregateKeyFromIndices 56.0 to 11.5 ms; keys loaded 46,693 to 7,159 (pr:prysm#17799)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_block_processing/signature_sets.rs:327-356`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/signature_sets.rs#L327-L356) indexed_attestation_signature_set_from_pubkeys loads every attester key
- [`consensus/state_processing/src/per_block_processing/signature_sets.rs:814-818`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/signature_sets.rs#L814-L818) committee pubkeys are filtered per participant (sync committee only)
- [`consensus/types/src/state/beacon_state.rs:1843`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L1843) the only cached AggregatePublicKey is the sync committee aggregate
- [`crypto/bls/src/impls/blst.rs:102`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L102) aggregation always adds the participant keys

**Second check.** Searched beacon_node, consensus and crypto for AggregatePublicKey and committee pubkey caches; the only hits are the sync committee aggregate and the generic aggregate path, so the verdict stands.

**Sources.** [prysm#17799](https://github.com/OffchainLabs/prysm/pull/17799)

</details>

<a id="attestation_processing-090"></a>
<details>
<summary><b>attestation_processing-090</b> Lazy BLS signature decompression for gossip attestations — <i>not · medium · M · cpu</i></summary>

**Idea.** Keep gossip attestation signatures compressed on decode and decompress only after cheap checks (and redundancy filters) pass, so unviable or redundant attestations never pay decompression.

**Gap in Lighthouse.** Gossip attestations and aggregates decompress the G2 signature during SSZ decode, before any cheap check. Add a compressed/lazy signature type for the gossip attestation path (the closed #4409/#4567 did this) and decompress only in the batch verifier, after verify_early_checks and the observed_aggregates/observed_attesters filters.

**Impact.** Saves one G2 decompression for each gossip attestation that the cheap checks drop (duplicates, subsets, wrong slot). Only a few percent of gossip CPU.

**Evidence (Lighthouse @ 928b61e719).**

- [`crypto/bls/src/generic_aggregate_signature.rs:166`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/generic_aggregate_signature.rs#L166) deserialize builds the point at once via AggSig::deserialize
- [`crypto/bls/src/impls/blst.rs:250`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L250) blst Signature::from_bytes decompresses the G2 point at SSZ decode
- [`consensus/types/src/attestation/attestation.rs:90`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/attestation/attestation.rs#L90) Attestation.signature is AggregateSignature (decompressed point), not SignatureBytes

**Second check.** Checked the generic bls wrapper and the blst impl for a deferred or cached decompression, and the Attestation types for a SignatureBytes-style field. Only exact duplicate messages skip decode, through gossipsub message-id dedup; that is not this idea.

**Sources.** [lighthouse#4409](https://github.com/sigp/lighthouse/pull/4409), [lighthouse#4567](https://github.com/sigp/lighthouse/pull/4567)

</details>

<a id="attestation_processing-105"></a>
<details>
<summary><b>attestation_processing-105</b> Verify deferred attestations before queuing them — <i>not · medium · M · cpu, memory</i></summary>

**Idea.** BLS-verify attestations for unknown blocks or future slots at gossip time (through the batch verifier) before saving them for later, caching the valid result, so junk cannot fill pending caches and fork choice does not re-verify.

**Gap in Lighthouse.** Lighthouse queues attestations for unknown blocks without a signature check, and re-runs full gossip verification when the block arrives. To do it: on UnknownHeadBlock with a known target, get the committee and batch-verify the signature before queuing, reject and penalize when invalid, and cache the valid result so the reprocess does not verify again. The slasher path at attestation_verification.rs:446-500 already does the indexing and verification and could be reused.

**Impact.** Mostly DoS hardening. The queue is bounded to 16k and invalid signatures are rejected and penalized on reprocess, so the Teku penalty-free fork-choice cost is mostly not present. The gain is less junk in the queue and earlier peer penalties.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:2874`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L2874) UnknownHeadBlock queues the unverified attestation closure into the reprocess queue, gated only by reprocess_allowance
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:84`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L84) MAXIMUM_QUEUED_ATTESTATIONS = 16_384 bounds the queue
- [`beacon_node/beacon_chain/src/attestation_verification.rs:446`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L446) with a slasher, UnknownHeadBlock attestations whose target is known get indexed and signature-checked (line 493), but only to feed the slasher: the error is returned unchanged and the result is not cached
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:2629`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L2629) FutureSlot attestations are ignored, not saved

**Second check.** Found a similar mechanism the earlier review did not mention: with the slasher on, Lighthouse verifies signatures of unknown-head attestations whose target is known. It only feeds the slasher and does not gate or cache anything. Future-slot attestations are dropped, not deferred.

**Sources.** [teku#11554](https://github.com/Consensys-Incorporated/teku/pull/11554), [teku#11560](https://github.com/Consensys-Incorporated/teku/pull/11560)

</details>

<a id="attestation_processing-123"></a>
<details>
<summary><b>attestation_processing-123</b> Trigger-based batching of gossip attestation BLS verification — <i>not · medium · M · cpu, latency</i></summary>

**Idea.** Delay dispatching unaggregated gossip attestations to a worker until N are queued or a short max age expires, so BLS verification is batched even on many-core machines whose queues never fill.

**Gap in Lighthouse.** Add a hold-back in the beacon processor manager loop: when attestation_queue has fewer than N items and the oldest is younger than ~10ms, do not dispatch and arm a timer to wake the loop; track enqueue time in LifoQueue items. N and max age configurable.

**Impact.** Larger BLS batches on many-core nodes; PR measured BLS CPU -34% and total node CPU -30% on a high-subnet node, much less on default subscriptions.

**Best measured result.** BLS CPU -34%, total node CPU -30%; mean latency 104 ms -&gt; 37 ms; p99 1.80 s -&gt; 834 ms; p50 0.6 -&gt; 2.3 ms (trigger 8, max-age 10ms) (pr:lighthouse#9641)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/lib.rs:1017-1025`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L1017-L1025) attestation_queue dispatched as soon as non-empty; batch_size&lt;2 -&gt; individual
- [`beacon_node/beacon_processor/src/lib.rs:110`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L110) only a max batch size (64), no min size or max age
- [`beacon_node/network/src/network_beacon_processor/mod.rs:86-130`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/mod.rs#L86-L130) send_unaggregated_attestation forwards each attestation immediately, no buffering
- [`beacon_node/src/cli.rs:1654`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/cli.rs#L1654) only --beacon-processor-attestation-batch-size (max) is configurable
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:53`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L53) DelayQueue only for unknown-block reprocessing, not batch formation

**Second check.** Checked the network-side send path, the scheduler/ submodules (work_queue, reprocessing DelayQueue), the manager poll loop and CLI flags for any min-batch, trigger or max-age mechanism; none exist, so the batch is formed only from whatever is queued at dispatch time.

**Sources.** [lighthouse#9641](https://github.com/sigp/lighthouse/pull/9641)

</details>

<a id="attestation_processing-007"></a>
<details>
<summary><b>attestation_processing-007</b> Validate same-data attestations as one group — <i>partial · medium · M · cpu, latency</i></summary>

**Idea.** When draining queued or API-submitted attestations, group by attestation data, run the shared data checks, target state lookup and signing root once per group, and batch-verify the signatures, verifying individually only if the batch fails.

**Gap in Lighthouse.** The expensive parts of the idea (target state lookup once, batch signature verify with individual fallback) exist for gossip. Missing: bucketing by AttestationData so the head-block/target checks and signing-root hashing run once per bucket, and using the batch path for API submissions (see 009).

**Impact.** Small: remaining per-attestation work is a fork choice read lock, a committee cache hit and one signing-root hash (microseconds); the 50-100ms per-attestation cost the source PR fixed is state lookup, which the shuffling cache already avoids.

**Best measured result.** processing 100 attestations could take up to 10s; per-attestation 50-100ms before (pr:prysm#15801)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/attestation_verification/batch.rs:133`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification/batch.rs#L133) gossip unaggregated attestations are batch BLS verified with per-attestation fallback when the batch fails
- [`beacon_node/beacon_chain/src/attestation_verification.rs:1617`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1617) map_attestation_committees takes committees from shuffling_cache via with_committee_cache, so the target-state/committee lookup happens once per shuffling, not per attestation
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:106`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L106) CacheItem::Promise coalesces concurrent misses so only one state load runs for many attestations of the same target
- [`beacon_node/beacon_chain/src/attestation_verification/batch.rs:146`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification/batch.rs#L146) IndexedUnaggregatedAttestation::verify still runs per attestation (head block, slot range, signing root)

**Second check.** Earlier review missed that the shuffling cache (with promise-based miss coalescing) already gives the once-per-target state/committee lookup, and that gossip already batch-verifies with fallback.

**Sources.** [lodestar#3392](https://github.com/ChainSafe/lodestar/pull/3392), [prysm#15801](https://github.com/OffchainLabs/prysm/pull/15801), [lodestar#5311](https://github.com/ChainSafe/lodestar/pull/5311)

</details>

<a id="attestation_processing-011"></a>
<details>
<summary><b>attestation_processing-011</b> Batch-verify reprocessed pending attestations — <i>partial · medium · M · cpu, latency</i></summary>

**Idea.** When releasing queued attestations (e.g. after their block is imported), verify their signatures as one batch instead of one by one, and requeue future-slot or missing-target ones directly rather than reprocessing them.

**Gap in Lighthouse.** Released attestations get requeued directly (done) but are verified one by one via process_fn. Would need unknown_block queues to form GossipAttestationBatch/GossipAggregateBatch (or re-push released work into the normal batching queues) in BeaconProcessor::spawn_manager.

**Impact.** Fewer BLS verifications when a block arrives late and hundreds of queued attestations are released at once; batch verify is roughly 2x cheaper per sig, only on late-block slots.

**Best measured result.** attestation processing was 23% of profile (pr:lodestar#2754)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:2919`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L2919) failed unaggregate requeued as UnknownBlockUnaggregate with process_fn calling single process_gossip_attestation
- [`beacon_node/beacon_processor/src/lib.rs:1086`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L1086) unknown_block_*_queue popped one item at a time (Work::UnknownBlockAttestation process_fn, lib.rs:1682)
- [`beacon_node/beacon_processor/src/lib.rs:1030`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L1030) batching exists only for fresh gossip attestation_queue/aggregate_queue

**Sources.** [lodestar#2754](https://github.com/ChainSafe/lodestar/pull/2754), [teku#10431](https://github.com/Consensys-Incorporated/teku/pull/10431)

</details>

<a id="attestation_processing-021"></a>
<details>
<summary><b>attestation_processing-021</b> Process attestations and update head once per slot — <i>partial · medium · S · cpu</i></summary>

**Idea.** Apply pending attestations to fork choice and recompute head once per slot instead of both on tick and on proposal.

**Gap in Lighthouse.** Attestation application is batched per slot via the queue, but head is recomputed at the pre-slot timer, at slot start and on each block import, i.e. not once per slot. Could drop the per_slot_task recompute when state_advance_timer already ran for that slot.

**Impact.** Saves one get_head (proto-array apply_score_changes over all votes) per slot, likely a few ms of the fork choice write lock; small.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/fork_choice/src/fork_choice.rs:1386`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L1386) attestations of current slot queued; fork_choice.rs:1580 process_attestation_queue dequeues in bulk on update_time
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:212`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L212) recompute_head_at_slot(next_slot) pre-emptively before slot end
- [`beacon_node/beacon_chain/src/beacon_chain.rs:7496`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L7496) per_slot_task recomputes head again at slot start
- [`beacon_node/network/src/network_beacon_processor/sync_methods.rs:207`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/sync_methods.rs#L207) recompute on block import

**Sources.** [prysm#12087](https://github.com/OffchainLabs/prysm/pull/12087)

</details>

<a id="attestation_processing-026"></a>
<details>
<summary><b>attestation_processing-026</b> Allocation-free attesting indices computation — <i>partial · medium · S · cpu, memory</i></summary>

**Idea.** Compute attesting indices/participants without intermediate vectors or sequences (preallocate, write directly) so per-attestation work in block and epoch processing does not allocate.

**Gap in Lighthouse.** Electra/Gloas get_attesting_indices allocates a Vec for committee indices, a HashSet per committee and a growing Vec. Rewrite attesting_indices_electra::get_attesting_indices to size the output from aggregation_bits.num_set_bits(), push directly, iterate committee_bits without collecting, and drop the HashSet.

**Impact.** Fewer allocations in block processing and gossip aggregate verification (called for every aggregate and block attestation); likely a small percent of block import time, not the 15% seen in the old Nimbus sim.

**Best measured result.** 15% to 1% of block_sim at 100k validators (pr:nimbus#1351)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/common/get_attesting_indices.rs:30`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/common/get_attesting_indices.rs#L30) base version preallocates Vec::with_capacity(num_set_bits)
- [`consensus/state_processing/src/common/get_attesting_indices.rs:100`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/common/get_attesting_indices.rs#L100) electra version starts with vec![], collects a HashSet per committee, calls get_committee_indices that allocates a Vec, then extend and sort
- [`consensus/state_processing/src/consensus_context.rs:161`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/consensus_context.rs#L161) results memoised per attestation root so each is computed once per block

**Sources.** [nimbus#1351](https://github.com/status-im/nimbus-eth2/pull/1351), [lighthouse@a44d80006](https://github.com/sigp/lighthouse/commit/a44d80006a65)

</details>

<a id="attestation_processing-035"></a>
<details>
<summary><b>attestation_processing-035</b> Verify signatures without building indexed attestation — <i>partial · medium · M · cpu, memory</i></summary>

**Idea.** Verify attestation signatures directly from committee and aggregation bits without constructing a full indexed attestation, and skip building it entirely when signatures are not checked; avoid pointer work when adding to the pool.

**Gap in Lighthouse.** No signature-set builder works from committee and aggregation bits directly; IndexedAttestation (Vec alloc + sort) is always built, also when signatures are not verified. Only de-duplication via ConsensusContext cache exists. The indexed form is still needed afterwards for fork choice, slasher and validity checks, so the saving is one allocation/sort pass.

**Impact.** Small: one Vec allocation and sort per aggregate/block attestation; negligible next to BLS cost.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/consensus_context.rs:161`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/consensus_context.rs#L161) get_indexed_attestation caches the IndexedAttestation by attestation tree_hash_root, so the block signature verifier and process_operations build it once per block attestation
- [`consensus/state_processing/src/per_block_processing/block_signature_verifier.rs:297`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/block_signature_verifier.rs#L297) signature sets are built from the cached indexed attestation
- [`consensus/state_processing/src/per_block_processing/verify_attestation.rs:92`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/verify_attestation.rs#L92) indexed attestation is still built when verify_signatures is false (needed for is_valid_indexed_attestation sorted/non-empty checks)
- [`consensus/state_processing/src/common/get_attesting_indices.rs:25`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/common/get_attesting_indices.rs#L25) indices collected into a Vec and sorted
- [`consensus/state_processing/src/per_block_processing/signature_sets.rs:295`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/signature_sets.rs#L295) indexed_attestation_signature_set only accepts an IndexedAttestationRef; no committee+bits builder exists
- [`beacon_node/beacon_chain/src/attestation_verification.rs:1558`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1558) aggregate gossip path builds IndexedAttestation before signature set

**Second check.** Checked ConsensusContext caching, signature_sets.rs builders and the VerifySignatures::False path in verify_attestation; no bits-based signature-set builder or skip-when-unverified path exists, so partial (caching only) stands.

**Sources.** [nimbus@f1f424cc2](https://github.com/status-im/nimbus-eth2/commit/f1f424cc2d2f), [nimbus#2503](https://github.com/status-im/nimbus-eth2/pull/2503)

</details>

<a id="attestation_processing-037"></a>
<details>
<summary><b>attestation_processing-037</b> Fetch target checkpoint state asynchronously — <i>partial · medium · M · latency, cpu</i></summary>

**Idea.** Retrieve the attestation target checkpoint state asynchronously (cache hit or regeneration off the processing thread) instead of a blocking store lookup, so attestation processing threads are not blocked by state loading.

**Gap in Lighthouse.** Lighthouse avoids the state load in the common case by proactively priming the shuffling cache off-thread (block import + state advance timer), but a real miss (reorg, non-head target) still blocks a beacon-processor worker while the state is loaded and advanced; there is no async fetch with re-queue of the attestation.

**Impact.** Only matters on shuffling cache misses during reorgs/non-finality; little effect on a healthy node.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:5211`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5211) import_block_update_shuffling_cache_fallible primes current and next epoch shufflings at block import
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:167`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L167) state advance runs in spawn_blocking off the processing threads
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:409`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L409) advanced head state primes the next-epoch shuffling cache ahead of the epoch boundary
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:346`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L346) read-lock cache hit path
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:375`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L375) promise dedups concurrent misses (MAX_CONCURRENT_PROMISES=2 at :36)
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:371`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L371) miss path loads/advances state synchronously on the calling beacon-processor worker

**Second check.** Beyond the earlier review, found the proactive priming in block import and the spawn_blocking state advance timer, which is an equivalent mechanism for the hot path; the miss path is still synchronous, so partial stands.

**Sources.** [teku#2465](https://github.com/Consensys-Incorporated/teku/pull/2465)

</details>

<a id="attestation_processing-076"></a>
<details>
<summary><b>attestation_processing-076</b> Bound attestation pre-state regeneration concurrency — <i>partial · medium · S · cpu, memory</i></summary>

**Idea.** Gate attestation pre-state regeneration behind a semaphore (limit one) so attestations for different old targets do not each regenerate a state in parallel, and abort early when the request context is cancelled.

**Gap in Lighthouse.** Concurrency is bounded (2, not 1) and duplicate targets are deduplicated, but extra targets are dropped instead of queued, and there is no cancellation of an in-flight state load.

**Impact.** The memory and CPU bound already exists; queueing instead of dropping would only save some attestations on forky networks.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/shuffling_cache.rs:36`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L36) MAX_CONCURRENT_PROMISES = 2
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:287-297`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L287-L297) create_promise refuses over the cap
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:365`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L365) callers for the same shuffling id wait on the existing promise (dedup)
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:3227-3242`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L3227-L3242) over-cap attestations are dropped with Ignore

**Second check.** Confirmed the promise cap, the same-key wait in with_cached_shuffling and the drop path in gossip_methods; found no extra semaphore or cancellation, so partial stands.

**Sources.** [prysm#17456](https://github.com/OffchainLabs/prysm/pull/17456)

</details>

## Other checked ideas (47)

Implemented, not applicable, or low value.

<a id="attestation_processing-025"></a>
<details>
<summary><b>attestation_processing-025</b> Field-wise attestation data equality — <i>not · low · S · cpu, memory</i></summary>

**Idea.** Compare AttestationData with a direct field-by-field equality instead of serialising or hash-tree-rooting both sides, removing allocations on the duplicate-detection hot path.

**Gap in Lighthouse.** Dedup is a hash-map lookup keyed by tree_hash_root, so a field-wise compare would only help if the key were AttestationData itself (derive Hash, key map on it). Change ObservedAggregates key type and root().

**Impact.** Saves roughly 7 sha256 compressions plus a clone per gossip aggregate/attestation; small share of CPU.

**Best measured result.** fast 18.1 ns/op 0 allocs vs slow 4363 ns/op 30 allocs (pr:prysm#5834)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/observed_aggregates.rs:178-186`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/observed_aggregates.rs#L178-L186) root() clones AttestationData into ObservedAttestationKey and calls tree_hash_root for dedup
- [`consensus/types/src/attestation/attestation_data.rs:17`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/attestation/attestation_data.rs#L17) derives PartialEq but dedup is keyed by hash root

**Sources.** [prysm#5834](https://github.com/OffchainLabs/prysm/pull/5834)

</details>

<a id="attestation_processing-027"></a>
<details>
<summary><b>attestation_processing-027</b> Iterate only set bits of aggregation bitfield — <i>not · low · S · cpu, memory</i></summary>

**Idea.** Derive attesting indices by iterating the set bits of the aggregation bitfield directly (word-level scan) rather than testing every bit position.

**Gap in Lighthouse.** Iterate set bits (BitIter / byte-wise scan) and index into the committee slice instead of testing each position; drop the per-committee HashSet. Edit get_attesting_indices (electra) and the base variant.

**Impact.** Cuts per-attestation index derivation, used in block processing and fork choice; sparse aggregates benefit most. Small overall.

**Best measured result.** 2107 ns/op -&gt; 277 ns/op, 1057 -&gt; 576 B/op (pr:prysm#5160)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/common/get_attesting_indices.rs:116-125`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/common/get_attesting_indices.rs#L116-L125) enumerates every committee member and calls aggregation_bits.get(i) per position, collecting into a HashSet

**Sources.** [prysm#5160](https://github.com/OffchainLabs/prysm/pull/5160)

</details>

<a id="attestation_processing-028"></a>
<details>
<summary><b>attestation_processing-028</b> Avoid sorting attesting indices — <i>not · low · S · cpu, memory</i></summary>

**Idea.** Build attesting indices by walking the committee in aggregation-bit order and skip or minimise the generic sort, and skip sorting entirely where the spec does not need ordering. This removes the sort cost and allocation per attestation.

**Gap in Lighthouse.** Output ordering needed by IndexedAttestation requires sorted indices, and committee order is shuffled order, so the sort cannot be dropped in the indexed path; only callers needing just counts or a set (e.g. fork choice, rewards) could skip it. Add an unsorted variant and use it there.

**Impact.** Minor: saves a sort of up to a few hundred u64 per attestation on non-indexed callers.

**Best measured result.** 8% faster overall on ncli_db bench first 100k slots; ~12% on apply block (1.67ms to 1.47ms) (pr:nimbus#2274)

**Evidence (Lighthouse @ 928b61e719).**

- get_attesting_indices.rs:41 and :149 still call sort_unstable after collecting (electra path also via HashSet)
- committees are walked in order so output is already ascending in a single committee only if the committee is sorted, which it is not (shuffled)

**Sources.** [nimbus@490e4c766](https://github.com/status-im/nimbus-eth2/commit/490e4c766643), [nimbus#2274](https://github.com/status-im/nimbus-eth2/pull/2274), [prysm#2893](https://github.com/OffchainLabs/prysm/pull/2893)

</details>

<a id="attestation_processing-116"></a>
<details>
<summary><b>attestation_processing-116</b> Skip fork choice lookup for head-targeting attestations — <i>not · low · S · cpu, latency</i></summary>

**Idea.** When an attestation's block is the canonical head or in the early-attester cache, skip the fork choice block lookup and its finalized-descent ancestor walk.

**Gap in Lighthouse.** Lighthouse PR 7010 was closed unmerged. In verify_head_block_is_known, check the canonical head root and early_attester_cache first and return the ProtoBlock without calling fork choice get_block and verify_attestation_is_finalized_checkpoint_or_descendant.

**Impact.** Skips a fork-choice read lock and ancestor walk per head-targeting attestation; PR claims ~6ms per attestation process (unverified, closed WIP).

**Best measured result.** approx 6ms saved per attestation process in experiments (pr:lighthouse#7010)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/attestation_verification.rs:1244`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1244) verify_head_block_is_known does fork_choice get_block first, early_attester_cache only as fallback
- [`beacon_node/beacon_chain/src/attestation_verification.rs:1519`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1519) verify_attestation_is_finalized_checkpoint_or_descendant always runs after lookup

**Sources.** [lighthouse#7010](https://github.com/sigp/lighthouse/pull/7010)

</details>

<a id="attestation_processing-087"></a>
<details>
<summary><b>attestation_processing-087</b> Size attesting-indices output by set bits — <i>partial · low · S · memory</i></summary>

**Idea.** Allocate the attesting-indices output by the popcount of the aggregation bitlist rather than the full committee length.

**Gap in Lighthouse.** Electra/Gloas get_attesting_indices (attesting_indices_electra) uses vec![] and per-committee HashSet&lt;u64&gt;; pre-size the Vec by aggregation_bits.num_set_bits() and drop the HashSet.

**Impact.** Saves a few allocations per block attestation on Electra; negligible in total.

**Best measured result.** 544 -&gt; 480 B/op (pr:prysm#6508)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/common/get_attesting_indices.rs:30`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/common/get_attesting_indices.rs#L30) Vec::with_capacity(num_set_bits) pre-Electra
- get_attesting_indices.rs:99 Electra uses vec![] and a HashSet per committee

**Sources.** [prysm#6508](https://github.com/OffchainLabs/prysm/pull/6508)

</details>

<a id="attestation_processing-089"></a>
<details>
<summary><b>attestation_processing-089</b> Fuse index check with pubkey fetch, preallocate — <i>partial · low · S · cpu, memory</i></summary>

**Idea.** When validating indexed attestations, preallocate the pubkey array to the index count and do the sorted/unique check while fetching pubkeys, avoiding intermediate lists and extra passes.

**Gap in Lighthouse.** Preallocation exists, but the sorted check is a separate pass over a copied Vec. Fuse it into indexed_attestation_signature_set's loop and drop the attesting_indices_to_vec() call in is_valid_indexed_attestation.

**Impact.** Saves one Vec&lt;u64&gt; alloc and one pass per attestation in block processing signature setup; small versus BLS cost.

**Best measured result.** 407MB vs 1.17GB allocations; 30% faster (89 to 116 ops/ms) (pr:teku#8941)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_block_processing/signature_sets.rs:306`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/signature_sets.rs#L306) pubkeys Vec::with_capacity(len)
- [`consensus/state_processing/src/per_block_processing/is_valid_indexed_attestation.rs:18`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/is_valid_indexed_attestation.rs#L18) attesting_indices_to_vec copy, then separate sorted pass

**Sources.** [teku#8941](https://github.com/Consensys-Incorporated/teku/pull/8941)

</details>

<a id="attestation_processing-010"></a>
<details>
<summary><b>attestation_processing-010</b> Batch gossip attestation signature verification — <i>implemented · high · cpu</i></summary>

**Idea.** In the beacon processor, collect gossip attestations into batches (time-bounded or greedy) and verify their signatures together to amortise BLS cost.

**Gap in Lighthouse.** 

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/lib.rs:110`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L110) DEFAULT_MAX_GOSSIP_ATTESTATION_BATCH_SIZE = 64
- [`beacon_node/beacon_processor/src/lib.rs:1015-1060`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L1015-L1060) attestation_queue drained greedily into GossipAttestationBatch when 2+ queued
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:316`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L316) process_gossip_attestation_batch calls batch_verify_unaggregated_attestations
- [`beacon_node/beacon_chain/src/attestation_verification/batch.rs:140`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification/batch.rs#L140) single verify_signature_sets, fallback to individual checks

**Sources.** [lighthouse#8285](https://github.com/sigp/lighthouse/pull/8285)

</details>

<a id="attestation_processing-042"></a>
<details>
<summary><b>attestation_processing-042</b> Reject finalized or old-target attestations before state load — <i>implemented · high · cpu, latency, disk, memory</i></summary>

**Idea.** Before loading or regenerating any state or verifying signatures, cheaply reject attestations whose target or slot is at or before finalization (or not descended from finalized), so stale attestations never trigger multi-epoch block replays.

**Gap in Lighthouse.** 

**Best measured result.** avoids replays of up to 32 epochs of blocks stalling processing (pr:nimbus#2361)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/attestation_verification.rs:1244`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1244) verify_head_block_is_known rejects HeadBlockFinalized via fork choice before any state load
- [`beacon_node/beacon_chain/src/attestation_verification.rs:1519`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1519) verify_attestation_is_finalized_checkpoint_or_descendant
- [`beacon_node/beacon_chain/src/attestation_verification.rs:1630-1645`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1630-L1645) map_attestation_committees rejects target.root not in fork choice (UnknownTargetRoot) before with_committee_cache

**Sources.** [lighthouse@4020d1306](https://github.com/sigp/lighthouse/commit/4020d13064fb), [teku#7137](https://github.com/Consensys-Incorporated/teku/pull/7137), [nimbus#2361](https://github.com/status-im/nimbus-eth2/pull/2361), [prysm#1623](https://github.com/OffchainLabs/prysm/pull/1623)

</details>

<a id="attestation_processing-001"></a>
<details>
<summary><b>attestation_processing-001</b> Use cached committees for attesting indices — <i>implemented · medium · cpu, latency</i></summary>

**Idea.** Resolve attesting indices in gossip verification, the op pool, fork choice vote updates and duties from a per-epoch committee/shuffling cache instead of recomputing the shuffling from a BeaconState per attestation. The shuffling is fixed for the epoch, so one computation serves every attestation.

**Gap in Lighthouse.** 

**Best measured result.** 95% reduction in attestation processing time (best case) (pr:lighthouse#841)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/attestation_verification.rs:1547`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1547) obtain_indexed_attestation_and_committees_per_slot
- [`beacon_node/beacon_chain/src/attestation_verification.rs:1617`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1617) map_attestation_committees -&gt; chain.with_committee_cache
- [`beacon_node/beacon_chain/src/beacon_chain.rs:7593`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L7593) with_committee_cache backed by shuffling_cache

**Sources.** [nimbus@74dc2fffa](https://github.com/status-im/nimbus-eth2/commit/74dc2fffa60f), [nimbus#1126](https://github.com/status-im/nimbus-eth2/pull/1126), [lighthouse@3b92b6902](https://github.com/sigp/lighthouse/commit/3b92b6902802), [lodestar@59eba5ce2](https://github.com/ChainSafe/lodestar/commit/59eba5ce2246), [prysm#2265](https://github.com/OffchainLabs/prysm/pull/2265), [lighthouse#841](https://github.com/sigp/lighthouse/pull/841)

</details>

<a id="attestation_processing-002"></a>
<details>
<summary><b>attestation_processing-002</b> Shuffling cache keyed by epoch and dependent root — <i>implemented · medium · cpu, memory, latency</i></summary>

**Idea.** Key the committee/shuffling cache (and per-committee aggregate pubkeys) by (target epoch, shuffling decision/dependent root) so entries are correct across forks and shared by attestation verification, block production and API. Compute each shuffling once (at epoch transition or slot tick, deduplicating concurrent computations) so attestation committees come from the cache without recomputing the shuffling or needing a full state.

**Gap in Lighthouse.** Per-committee aggregate pubkeys are not cached (batch.rs builds aggregates per signature set), but the keyed/deduplicated shuffling cache is present.

**Best measured result.** single verify ~+100ns of ~70us; batch same or cheaper (pr:silver#329)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/shuffling_cache.rs:129`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L129) cache: HashMap&lt;AttestationShufflingId, CacheItem&gt;, key is (epoch, shuffling decision root)
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:105`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L105) CacheItem::Promise dedups concurrent computations
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:315`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L315) with_cached_shuffling falls back to a state only on a miss

**Sources.** [silver#329](https://github.com/gattaca-com/silver/pull/329), [prysm#4270](https://github.com/OffchainLabs/prysm/pull/4270), [lodestar#6030](https://github.com/ChainSafe/lodestar/pull/6030), [lodestar#1178](https://github.com/ChainSafe/lodestar/pull/1178), [silver#189](https://github.com/gattaca-com/silver/pull/189)

</details>

<a id="attestation_processing-013"></a>
<details>
<summary><b>attestation_processing-013</b> Compute block attestations&#x27; target state once — <i>implemented · medium · cpu, memory, disk</i></summary>

**Idea.** Process a block's attestations in order (sorted by slot, sequentially) so the first one loads or computes the needed target checkpoint state and blocks, and the rest reuse it. This avoids concurrent or per-attestation reads and regenerations of the same state.

**Gap in Lighthouse.** 

**Best measured result.** "reduce time in processing a block" (no numbers) (pr:prysm#2370)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/consensus_context.rs:161`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/consensus_context.rs#L161) get_indexed_attestation uses the one block pre-state and its committee caches, memoised by attestation root
- gossip_methods.rs:2827 area: gossip attestations use shared shuffling/committee cache via chain.with_committee_cache (attestation_verification.rs:1076)

**Sources.** [prysm#2370](https://github.com/OffchainLabs/prysm/pull/2370), [lodestar@268ef36df](https://github.com/ChainSafe/lodestar/commit/268ef36df6e7)

</details>

<a id="attestation_processing-022"></a>
<details>
<summary><b>attestation_processing-022</b> Verify aggregates before unaggregated attestations — <i>implemented · medium · cpu, latency</i></summary>

**Idea.** In the attestation verification queue, prioritise aggregate-and-proof messages over unaggregated attestations so limited verification CPU goes to the more valuable, time-critical messages first.

**Gap in Lighthouse.** 

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/lib.rs:960`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L960) aggregate_queue popped before attestation_queue with comment about value
- [`beacon_node/beacon_processor/src/lib.rs:1030`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L1030) then unaggregated attestation_queue

**Sources.** [grandine@bf3b57760](https://github.com/grandinetech/grandine/commit/bf3b57760e46)

</details>

<a id="attestation_processing-031"></a>
<details>
<summary><b>attestation_processing-031</b> Verify single attestations in native form — <i>implemented · medium · cpu, latency</i></summary>

**Idea.** Receive and verify unaggregated SingleAttestation gossip messages in their native form and convert to a full attestation only after verification, removing a separate conversion work event.

**Gap in Lighthouse.** 

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:284`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L284) process_gossip_attestation takes Box&lt;SingleAttestation&gt;
- [`beacon_node/beacon_chain/src/attestation_verification.rs:1143`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1143) single_attestation_to_attestation called inside verification after committee check
- [`beacon_node/beacon_processor/src/lib.rs:373`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L373) GossipAttestationBatch is Vec&lt;GossipAttestationPackage&lt;SingleAttestation&gt;&gt;

**Sources.** [lighthouse#7444](https://github.com/sigp/lighthouse/pull/7444)

</details>

<a id="attestation_processing-032"></a>
<details>
<summary><b>attestation_processing-032</b> Convert attestations on worker, not async thread — <i>implemented · medium · cpu, latency</i></summary>

**Idea.** Do the single-attestation to committee-attestation conversion (committee lookup) on a beacon processor worker instead of an async runtime thread so the runtime is not blocked.

**Gap in Lighthouse.** 

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/attestation_verification.rs:1076`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1076) committee lookup and conversion run in verify_unaggregated_attestation_for_gossip
- [`beacon_node/network/src/network_beacon_processor/mod.rs:86`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/mod.rs#L86) send_unaggregated_attestation wraps process_gossip_attestation as beacon processor Work

**Sources.** [lighthouse#6934](https://github.com/sigp/lighthouse/pull/6934)

</details>

<a id="attestation_processing-038"></a>
<details>
<summary><b>attestation_processing-038</b> Cache checkpoint states by target checkpoint — <i>implemented · medium · cpu, disk, latency</i></summary>

**Idea.** Keep an in-memory checkpoint-state cache keyed by target checkpoint, fill it with the state regenerated on a miss, and use it for attestation verification. Many attestations to the same target then share one state regeneration instead of a database load or regen each.

**Gap in Lighthouse.** 

**Impact.** Already shares one regeneration across all attestations with the same shuffling; keyed by shuffling rather than checkpoint state, which is cheaper than caching full states.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/shuffling_cache.rs:315`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L315) with_cached_shuffling keys by AttestationShufflingId (epoch + decision root)
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:309`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L309) update_head_shuffling_ids pins head shufflings
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:437`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L437) insert_committee_cache after miss

**Sources.** [lodestar#1401](https://github.com/ChainSafe/lodestar/pull/1401), [prysm#9282](https://github.com/OffchainLabs/prysm/pull/9282), [prysm#3345](https://github.com/OffchainLabs/prysm/pull/3345)

</details>

<a id="attestation_processing-039"></a>
<details>
<summary><b>attestation_processing-039</b> Validate attestations on head state when shuffling matches — <i>implemented · medium · cpu, memory, latency</i></summary>

**Idea.** When the attestation's target epoch committees are already determined in the head (or another in-memory) state, i.e. the shuffling dependent root matches, verify it against that state and its committee cache, also for previous- and next-epoch targets. This avoids loading, regenerating or advancing the exact target checkpoint state.

**Gap in Lighthouse.** 

**Impact.** Cache hit needs only fork choice lookup plus shuffling cache read; no target state load. Previous-epoch ids are None in BlockShufflingIds here, so a previous-epoch target not already cached falls to a disk state load, a minor gap.

**Best measured result.** Attestation processing 1 sec -&gt; 54 ms (pr:caplin#10020)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/shuffling_cache.rs:330`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L330) shuffling id taken from fork-choice ProtoBlock current/next epoch ids, no state needed
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:359`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L359) head state used directly for committee build when block is head
- [`beacon_node/beacon_chain/src/attestation_verification.rs:1627`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1627) map_attestation_committees calls with_committee_cache(target.root, attestation_epoch)

**Sources.** [teku#5482](https://github.com/Consensys-Incorporated/teku/pull/5482), [lodestar#5500](https://github.com/ChainSafe/lodestar/pull/5500), [prysm#17649](https://github.com/OffchainLabs/prysm/pull/17649), [prysm#17441](https://github.com/OffchainLabs/prysm/pull/17441), [prysm#16109](https://github.com/OffchainLabs/prysm/pull/16109), [prysm#16095](https://github.com/OffchainLabs/prysm/pull/16095), [teku#5822](https://github.com/Consensys-Incorporated/teku/pull/5822), [prysm#15095](https://github.com/OffchainLabs/prysm/pull/15095), [caplin#10020](https://github.com/erigontech/erigon/pull/10020)

</details>

<a id="attestation_processing-040"></a>
<details>
<summary><b>attestation_processing-040</b> On shuffling miss, use epoch-boundary target state — <i>implemented · medium · cpu, latency</i></summary>

**Idea.** On a shuffling cache miss, load the attestation's target (epoch-boundary) state to compute committees instead of the block-root state, avoiding replay of blocks and skip slots to a mid-epoch state.

**Gap in Lighthouse.** 

**Impact.** Miss path already loads a state near the epoch boundary rather than replaying blocks and skip slots; this is the saving of PR 4235.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/shuffling_cache.rs:383`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L383) target_slot = max(start of epoch before shuffling_epoch, head_block.slot)
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:392`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L392) get_advanced_hot_state(head_block_root, target_slot, ..) loads an epoch-boundary-advanced state instead of replaying

**Sources.** [lighthouse#4235](https://github.com/sigp/lighthouse/pull/4235)

</details>

<a id="attestation_processing-043"></a>
<details>
<summary><b>attestation_processing-043</b> Drop attestations older than previous epoch early — <i>implemented · medium · cpu, memory, bandwidth</i></summary>

**Idea.** Drop received attestations older than about one epoch (previous epoch) before queueing, fork-choice processing, pool insertion or re-gossip, rather than using the finalized slot as cutoff. This keeps queues and the pool small when finality lags.

**Gap in Lighthouse.** 

**Impact.** Old attestations are rejected at the first gossip check, before queueing into fork choice or pool; keeps work bounded when finality lags.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/attestation_verification.rs:1295`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1295) verify_propagation_slot_range drops attestations older than one epoch (or previous-epoch start under Deneb) with PastSlot
- [`beacon_node/beacon_chain/src/attestation_verification.rs:1334`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1334) PastSlot error
- [`beacon_node/beacon_chain/src/attestation_verification.rs:907`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L907) called in verify_early_checks before any state or pool work

**Sources.** [lodestar@e1021e36b](https://github.com/ChainSafe/lodestar/commit/e1021e36b14a), [prysm#1905](https://github.com/OffchainLabs/prysm/pull/1905)

</details>

<a id="attestation_processing-044"></a>
<details>
<summary><b>attestation_processing-044</b> Reject far-future target epochs by clock — <i>implemented · medium · cpu, latency</i></summary>

**Idea.** Reject attestations whose target epoch is beyond the current clock epoch before loading or advancing the target state, so a crafted attestation cannot force processing many empty slots.

**Gap in Lighthouse.** 

**Impact.** Far-future target epochs are rejected by two cheap checks before any state load or advance, so no empty-slot processing can be forced.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/attestation_verification.rs:909`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L909) target.epoch must equal attestation slot epoch (InvalidTargetEpoch)
- [`beacon_node/beacon_chain/src/attestation_verification.rs:1303`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1303) slot must be &lt;= clock slot plus disparity (FutureSlot)
- [`beacon_node/beacon_chain/src/attestation_verification.rs:548`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L548) same check for aggregates

**Sources.** [prysm#7169](https://github.com/OffchainLabs/prysm/pull/7169)

</details>

<a id="attestation_processing-045"></a>
<details>
<summary><b>attestation_processing-045</b> Check target block in fork choice before work — <i>implemented · medium · cpu</i></summary>

**Idea.** Before processing a queued attestation, check that its target/beacon block is known to fork choice and skip work that is certain to fail.

**Gap in Lighthouse.** 

**Impact.** Unknown head or target blocks fail with UnknownHeadBlock/UnknownTargetRoot before the shuffling cache or any state read.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/attestation_verification.rs:1244`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1244) verify_head_block_is_known via fork choice get_block, in verify_early_checks before committees
- [`beacon_node/beacon_chain/src/attestation_verification.rs:1627`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1627) map_attestation_committees checks fork choice contains_block(target.root) first
- [`beacon_node/beacon_chain/src/attestation_verification.rs:1379`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1379) verify_attestation_target_root against the head block

**Sources.** [prysm#15547](https://github.com/OffchainLabs/prysm/pull/15547)

</details>

<a id="attestation_processing-054"></a>
<details>
<summary><b>attestation_processing-054</b> Queue unknown-block attestations, release on block import — <i>implemented · medium · cpu, latency, bandwidth</i></summary>

**Idea.** Hold attestations whose block root is unknown in a bounded queue indexed by missing root (and wake-up slot), reusing decoded data, request the block, and release them on block import or slot tick. This replaces dropping them or retrying each on a fixed timer.

**Gap in Lighthouse.** 

**Impact.** none needed

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:84`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L84) MAXIMUM_QUEUED_ATTESTATIONS 16384 bound
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:329`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L329) awaiting_attestations_per_root indexed by missing root
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:2874-2886`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L2874-L2886) UnknownHeadBlock sends UnknownBlockHashFromAttestation lookup and queues attestation
- work_reprocessing_queue.rs:53 QUEUED_ATTESTATION_DELAY 12s expiry

**Sources.** [lodestar@bf2b3d061](https://github.com/ChainSafe/lodestar/commit/bf2b3d061c12), [lodestar#5286](https://github.com/ChainSafe/lodestar/pull/5286), [lighthouse#2319](https://github.com/sigp/lighthouse/pull/2319), [prysm#16909](https://github.com/OffchainLabs/prysm/pull/16909), [prysm#9679](https://github.com/OffchainLabs/prysm/pull/9679)

</details>

<a id="attestation_processing-065"></a>
<details>
<summary><b>attestation_processing-065</b> Attest as soon as the head block is processed — <i>implemented · medium · latency, bandwidth</i></summary>

**Idea.** Produce and publish own attestations as soon as the slot's head block is processed, removing artificial waits for the fixed attestation time in the slot, to cut propagation latency.

**Gap in Lighthouse.** 

**Impact.** none needed

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/beacon_node_fallback/src/beacon_head_monitor.rs:64`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/beacon_node_fallback/src/beacon_head_monitor.rs#L64) head_event_or_deadline returns on the current-slot head SSE event
- [`validator_client/validator_services/src/attestation_service.rs:212`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/attestation_service.rs#L212) attestation service uses it to attest before the 1/3 deadline
- [`validator_client/validator_services/src/attestation_service.rs:273-308`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/attestation_service.rs#L273-L308) uses attestation data from the head event

**Sources.** [lodestar#764](https://github.com/ChainSafe/lodestar/pull/764), [lodestar#788](https://github.com/ChainSafe/lodestar/pull/788), [caplin#14128](https://github.com/erigontech/erigon/pull/14128)

</details>

<a id="attestation_processing-070"></a>
<details>
<summary><b>attestation_processing-070</b> Use cached state of attested block root for validation — <i>implemented · medium · cpu, memory</i></summary>

**Idea.** For gossip attestations, look up the state of the attestation's beacon_block_root in the state cache and validate against it (when it can serve the target's committees) rather than regenerating a checkpoint state for the target epoch, avoiding extra epoch transitions.

**Gap in Lighthouse.** 

**Impact.** Lighthouse keys a shuffling cache by decision root and epoch, so no checkpoint state is regenerated per target; this gives the same effect.

**Best measured result.** "6-7 epoch transitions in just 2 minutes" before; "exactly 1 epoch transition per epoch" after (pr:lodestar#3532)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/attestation_verification.rs:1617-1655`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1617-L1655) map_attestation_committees calls with_committee_cache(target.root, epoch)
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:315-353`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L315-L353) shuffling id derived from the block in fork choice (proto-array shuffling ids), cache hit needs no state
- shuffling_cache.rs:433 head state reused, else shuffling_cache.rs:436 get_advanced_hot_state only on a miss

**Sources.** [lodestar#3532](https://github.com/ChainSafe/lodestar/pull/3532), [teku#7142](https://github.com/Consensys-Incorporated/teku/pull/7142)

</details>

<a id="attestation_processing-071"></a>
<details>
<summary><b>attestation_processing-071</b> Validate attestations against a few shared states — <i>implemented · medium · cpu, memory</i></summary>

**Idea.** Pick the validation state from a small shared set (head, justified, finalized, or earliest state per fork with the needed committees) rather than one state per attested block, so only about three states, at most one per fork per epoch, are needed.

**Gap in Lighthouse.** 

**Impact.** Attestations on many blocks that share a decision root map to one cached committee cache, which is the same outcome as the shared-state set.

**Best measured result.** up to 32x fewer states required (pr:teku#5205)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/shuffling_cache.rs:335-345`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L335-L345) BlockShufflingIds yields one shuffling id per (decision root, epoch)
- shuffling_cache.rs:31 DEFAULT_CACHE_SIZE 16 entries shared across blocks with the same decision root

**Sources.** [teku#5205](https://github.com/Consensys-Incorporated/teku/pull/5205)

</details>

<a id="attestation_processing-075"></a>
<details>
<summary><b>attestation_processing-075</b> Dedupe concurrent same-target checkpoint state computations — <i>implemented · medium · cpu, memory, latency</i></summary>

**Idea.** Track in-flight checkpoint (target) state computations per target root, with a per-key lock or promise map, so concurrent attestations sharing a target wait on one computation and reuse its cached result, while different targets proceed in parallel.

**Gap in Lighthouse.** 

**Impact.** none needed

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/shuffling_cache.rs:362-374`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L362-L374) write lock, existing Promise is waited on, else create_promise
- shuffling_cache.rs:105 CacheItem::Promise(Receiver)

**Sources.** [prysm#7659](https://github.com/OffchainLabs/prysm/pull/7659), [prysm#7690](https://github.com/OffchainLabs/prysm/pull/7690), [prysm#7669](https://github.com/OffchainLabs/prysm/pull/7669)

</details>

<a id="attestation_processing-091"></a>
<details>
<summary><b>attestation_processing-091</b> Skip aggregates whose bits are a subset of seen — <i>implemented · medium · cpu, bandwidth</i></summary>

**Idea.** Track observed aggregation bits per attestation data (OR-ed or per aggregator) and treat an aggregate as redundant if its bits are a subset of already seen ones, rejecting it before BLS verification.

**Gap in Lighthouse.** 

**Impact.** Already avoids BLS verification for redundant aggregates.

**Best measured result.** "~1 ms three-signature batch verify" skipped for redundant aggregates; no totals given (pr:silver#170)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/attestation_verification.rs:566`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L566) is_known_subset on observed_attestations in verify_early_checks, before BLS
- [`beacon_node/beacon_chain/src/observed_aggregates.rs:277`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/observed_aggregates.rs#L277) subset/superset handling per attestation data
- [`beacon_node/beacon_chain/src/observed_aggregates.rs:127`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/observed_aggregates.rs#L127) is_subset on aggregation bits

**Sources.** [prysm#4669](https://github.com/OffchainLabs/prysm/pull/4669), [silver#170](https://github.com/gattaca-com/silver/pull/170)

</details>

<a id="attestation_processing-093"></a>
<details>
<summary><b>attestation_processing-093</b> Use pre-advanced current-slot state for attestation checks — <i>implemented · medium · cpu, latency</i></summary>

**Idea.** Validate gossip attestations and build aggregation against a state already advanced to the current/next slot (state-advance cache) instead of slot-processing the head state per attestation near epoch boundaries.

**Gap in Lighthouse.** 

**Impact.** Gossip checks use cached committees keyed by shuffling, so epoch-boundary slot processing is not repeated per attestation.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/attestation_verification.rs:1617`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1617) map_attestation_committees uses with_committee_cache (shuffling cache), no per-attestation slot processing
- [`beacon_node/beacon_chain/src/beacon_chain.rs:7593`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L7593) with_committee_cache
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:109`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L109) head state pre-advanced before next slot

**Sources.** [prysm#12239](https://github.com/OffchainLabs/prysm/pull/12239), [grandine@18a073146](https://github.com/grandinetech/grandine/commit/18a073146c50), [grandine#206](https://github.com/grandinetech/grandine/pull/206)

</details>

<a id="attestation_processing-102"></a>
<details>
<summary><b>attestation_processing-102</b> Parallel verification of block attestations — <i>implemented · medium · cpu, latency</i></summary>

**Idea.** Verify the attestations included in a block in parallel across a thread pool, short-circuiting on the first failure, so block validation latency drops with core count.

**Gap in Lighthouse.** 

**Impact.** Block attestations are verified in one random-linear-combination batch that blst parallelises; equivalent effect (no explicit rayon over attestations, and failure is batch-level).

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_block_processing/block_signature_verifier.rs:296`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/block_signature_verifier.rs#L296) all block attestation sets collected into one batch
- [`consensus/state_processing/src/per_block_processing/block_signature_verifier.rs:459`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/block_signature_verifier.rs#L459) verify() with comment that blst spreads work across cores
- [`crypto/bls/src/impls/blst.rs:113`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L113) verify_multiple_aggregate_signatures batch

**Sources.** [lighthouse@b92d88d42](https://github.com/sigp/lighthouse/commit/b92d88d42bb5)

</details>

<a id="attestation_processing-106"></a>
<details>
<summary><b>attestation_processing-106</b> Skip re-verifying gossip-verified attestation signatures — <i>implemented · medium · cpu</i></summary>

**Idea.** Mark attestations whose signature passed gossip validation and skip signature verification for them on later block import or fork choice paths.

**Gap in Lighthouse.** 

**Impact.** Gossip-verified attestations go to fork choice without a second signature check; block attestations are verified once in the block batch.

**Best measured result.** ~1000ms spent validating signatures wastefully (pr:lodestar#2259)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:2573`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2573) apply_attestation_to_fork_choice takes a VerifiedAttestation and calls fork_choice.on_attestation without re-verifying
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2579`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2579) on_attestation call

**Sources.** [teku#3252](https://github.com/Consensys-Incorporated/teku/pull/3252), [lodestar#2259](https://github.com/ChainSafe/lodestar/pull/2259)

</details>

<a id="attestation_processing-111"></a>
<details>
<summary><b>attestation_processing-111</b> Refuse attestation production for slots before head — <i>implemented · medium · memory, disk</i></summary>

**Idea.** Reject attestation production requests for slots earlier than the head instead of loading an old full state from disk, avoiding memory blowups.

**Gap in Lighthouse.** 

**Impact.** Equivalent effect: no old full-state load from disk; pre-finalization slots are rejected and earlier slots use the head state or the hot state cache.

**Best measured result.** Pyrmont: allocations about host physical memory size caused OOM kills (pr:lighthouse#2130)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:2065`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2065) AttestingToFinalizedSlot error for request_slot before finalized
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2076`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2076) AttestingToAncientSlot
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2095`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2095) earlier slots served from head state block roots
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2150`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2150) get_advanced_hot_state only when epoch differs (state cache, hot state)

**Sources.** [lighthouse#2130](https://github.com/sigp/lighthouse/pull/2130)

</details>

<a id="attestation_processing-112"></a>
<details>
<summary><b>attestation_processing-112</b> Reject attestations with heads many skipped slots behind — <i>implemented · medium · cpu, memory</i></summary>

**Idea.** Ignore gossip attestations whose head block is more than a bounded number of skipped slots behind the attestation slot, so state regeneration is never triggered for old heads.

**Gap in Lighthouse.** 

**Impact.** Already rejects such attestations, so no regeneration for far-behind heads.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/attestation_verification.rs:1260`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1260) max_skip_slots check returns TooManySkippedSlots
- [`beacon_node/beacon_chain/src/attestation_verification.rs:260`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L260) Error::TooManySkippedSlots

**Sources.** [lodestar#5390](https://github.com/ChainSafe/lodestar/pull/5390)

</details>

<a id="attestation_processing-113"></a>
<details>
<summary><b>attestation_processing-113</b> Check head descends from target before loading target — <i>implemented · medium · S · cpu, disk</i></summary>

**Idea.** For aggregates, check that the attestation's head block descends from its target before loading the target block/state, so old targets are never loaded and advanced.

**Gap in Lighthouse.** 

**Impact.** Already avoids loading old targets; nothing to gain.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/attestation_verification.rs:1379`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1379) verify_attestation_target_root derives expected target from head ProtoBlock, no block/state load
- attestation_verification.rs:1244 verify_head_block_is_known uses fork choice, checks finalized-descendant at :1514

**Sources.** [lighthouse#1702](https://github.com/sigp/lighthouse/pull/1702)

</details>

<a id="attestation_processing-114"></a>
<details>
<summary><b>attestation_processing-114</b> Drop old-target attestations not on any known chain — <i>implemented · medium · S · cpu, memory</i></summary>

**Idea.** Ignore attestations whose target is old and was never a checkpoint on any known chain instead of replaying state for them, and skip slot processing on the state used for aggregate selection proof checks.

**Gap in Lighthouse.** 

**Impact.** Targets older than finalization are dropped and committees come from the shuffling cache, so no state advance for stale targets.

**Evidence (Lighthouse @ 928b61e719).**

- attestation_verification.rs:1633 map_attestation_committees drops attestations whose target.root is not in fork choice or early attester cache (UnknownTargetRoot)
- attestation_verification.rs:1645 with_committee_cache uses the shuffling cache, no state replay or slot processing

**Sources.** [prysm#12387](https://github.com/OffchainLabs/prysm/pull/12387)

</details>

<a id="attestation_processing-003"></a>
<details>
<summary><b>attestation_processing-003</b> Compute committee length without building committee — <i>implemented · low · S · cpu</i></summary>

**Idea.** When only a committee's size is needed (attestation validation, attesting info), compute it arithmetically from the cached active validator count instead of shuffling and materialising the committee. Avoids the shuffle and the allocation.

**Gap in Lighthouse.** 

**Impact.** Committee size comes from the cached shuffling without allocation; the saving is already taken.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:2151`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2151) get_beacon_committee(..).committee.len() reads length from cached committee, no shuffle
- [`consensus/types/src/state/committee_cache.rs:202`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/committee_cache.rs#L202) get_beacon_committee returns borrowed slice

**Sources.** [prysm#7664](https://github.com/OffchainLabs/prysm/pull/7664), [lighthouse#4609](https://github.com/sigp/lighthouse/pull/4609), [nimbus#1363](https://github.com/status-im/nimbus-eth2/pull/1363)

</details>

<a id="attestation_processing-049"></a>
<details>
<summary><b>attestation_processing-049</b> Size attestation queues for many-validator bursts — <i>implemented · low · S · cpu, memory, latency</i></summary>

**Idea.** Size the pending, gossip attestation, aggregate and reprocess queues for the validator set and subnet subscriptions (configurable), so bursts are not dropped, and drain queues in batches when idle.

**Gap in Lighthouse.** 

**Impact.** Queues already scale with validator set; bursts are absorbed and batches drained up to 64 at a time.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/scheduler/work_queue.rs:357`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_queue.rs#L357) attestation_queue sized from active validator count / slots_per_epoch (from_state :335)
- [`beacon_node/beacon_processor/src/lib.rs:82`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L82) DEFAULT_MAX_WORK_EVENT_QUEUE_LEN configurable; work_reprocessing_queue.rs:84 MAXIMUM_QUEUED_ATTESTATIONS 16384
- aggregate_queue fixed 4096 at work_queue.rs:350

**Sources.** [prysm#12485](https://github.com/OffchainLabs/prysm/pull/12485), [teku#9229](https://github.com/Consensys-Incorporated/teku/pull/9229), [lighthouse#2535](https://github.com/sigp/lighthouse/pull/2535), [nimbus#2268](https://github.com/status-im/nimbus-eth2/pull/2268), [lighthouse#2506](https://github.com/sigp/lighthouse/pull/2506)

</details>

<a id="attestation_processing-052"></a>
<details>
<summary><b>attestation_processing-052</b> Deduplicate pending aggregates in queue — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Do not queue a pending aggregate if an equal one (same data and aggregation bits, any aggregator index) is already queued for that block root, so one aggregate per committee is processed and rebroadcast.

**Gap in Lighthouse.** 

**Impact.** Already drops duplicate/subset aggregates before verification and rebroadcast.

**Best measured result.** Reduces queue from one aggregate per aggregator to at best 64 (MAX_COMMITTEES_PER_SLOT); no timing numbers (pr:prysm#16153)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/observed_aggregates.rs:127`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/observed_aggregates.rs#L127) is_subset on AttestationData root + bits (is_known_subset:308)

**Sources.** [prysm#7326](https://github.com/OffchainLabs/prysm/pull/7326), [prysm#16153](https://github.com/OffchainLabs/prysm/pull/16153)

</details>

<a id="attestation_processing-056"></a>
<details>
<summary><b>attestation_processing-056</b> Cache new head&#x27;s attestation data before import finishes — <i>implemented · low · S · latency</i></summary>

**Idea.** Cache the block, attestation data and checkpoints for a block about to become head so attestations can be produced (and blocks served) before DB import or the head state update completes.

**Gap in Lighthouse.** 

**Impact.** Attestations can be produced before head import completes.

**Best measured result.** Head state update took up to a second (pr:caplin#12856)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:2026`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2026) early_attester_cache.try_attest
- beacon_chain.rs:4572 add_head_block before DB import

**Sources.** [caplin#12856](https://github.com/erigontech/erigon/pull/12856), [lighthouse#2872](https://github.com/sigp/lighthouse/pull/2872)

</details>

<a id="attestation_processing-058"></a>
<details>
<summary><b>attestation_processing-058</b> Cache attestation committee schedule per epoch — <i>implemented · low · S · cpu</i></summary>

**Idea.** When producing attestations for many validators, compute the committee/attestation schedule once per epoch and slot and reuse it instead of recomputing per validator.

**Gap in Lighthouse.** 

**Impact.** Committee schedule is cached in the state's committee cache and shuffling cache; no per-validator recompute.

**Best measured result.** 330 s to ~17 s per block, 1.5M validators (pr:teku#7491)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:2010`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2010) produce_unaggregated_attestation uses early cache/head snapshot; committees come from state committee cache ([`consensus/state_processing`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing) get_beacon_committees_at_slot)

**Sources.** [teku#7491](https://github.com/Consensys-Incorporated/teku/pull/7491)

</details>

<a id="attestation_processing-073"></a>
<details>
<summary><b>attestation_processing-073</b> Skip state roots when advancing state for shuffling — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** When a state must be advanced to a future slot only to obtain shuffling for attestation production, run per-slot processing without computing state roots, and serve attestation production from cached head data.

**Gap in Lighthouse.** 

**Impact.** Attestation production uses cached head data and skips state-root hashing when advancing.

**Best measured result.** orders of magnitude faster attestation production in best case (pr:lighthouse#838)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:2160`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2160) get_advanced_hot_state + partial_state_advance with known state root
- [`consensus/state_processing/src/state_advance.rs:72`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/state_advance.rs#L72)

**Sources.** [lighthouse#838](https://github.com/sigp/lighthouse/pull/838)

</details>

<a id="attestation_processing-077"></a>
<details>
<summary><b>attestation_processing-077</b> Avoid coarse locks around attestation state work — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Do not hold a global/service mutex across attestation processing or pre-state fetch; do state lookup and committee computation outside the lock and hold it only for small shared updates, relying on thread-safe caches, so concurrent gossip attestations do not serialize.

**Gap in Lighthouse.** 

**Impact.** Gossip attestations verify concurrently in the beacon processor workers; only short caches locks.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/attestation_verification.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs) (no global mutex held across verification; head via lock-free head_snapshot)

**Sources.** [prysm#3399](https://github.com/OffchainLabs/prysm/pull/3399), [prysm#7656](https://github.com/OffchainLabs/prysm/pull/7656), [prysm#16197](https://github.com/OffchainLabs/prysm/pull/16197)

</details>

<a id="attestation_processing-088"></a>
<details>
<summary><b>attestation_processing-088</b> Linear-pass sorted/unique check for indexed attestations — <i>implemented · low · S · cpu</i></summary>

**Idea.** Check that indexed attestation indices are sorted and unique with a single linear pass comparing neighbours, instead of sorting, copying, or building a set.

**Gap in Lighthouse.** None; the check is already one neighbour pass. A small Vec copy remains from attesting_indices_to_vec.

**Impact.** Negligible.

**Best measured result.** 227693 ns/op -&gt; 827 ns/op (pr:prysm#7458)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_block_processing/is_valid_indexed_attestation.rs:30`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/is_valid_indexed_attestation.rs#L30) tuple_windows linear sorted+unique check

**Sources.** [prysm#3015](https://github.com/OffchainLabs/prysm/pull/3015), [prysm#3060](https://github.com/OffchainLabs/prysm/pull/3060), [prysm#7458](https://github.com/OffchainLabs/prysm/pull/7458)

</details>

<a id="attestation_processing-100"></a>
<details>
<summary><b>attestation_processing-100</b> Only process unaggregated attestations for duty subnets — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Process and store single gossip attestations only for subnets/committees where a local validator has aggregation duty, so the signature pool and aggregation work shrink by the subnet count.

**Gap in Lighthouse.** None; with should_process false the attestation is only verified for propagation, not stored.

**Impact.** Already saves naive-pool inserts.

**Best measured result.** "Only N/C (250)" of 1000 signatures stored; ~3MB to ~750KB per round at 4 subnets (pr:ethlambda#221)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/subnet_service/mod.rs:353`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/subnet_service/mod.rs#L353) should_process_attestation true only for subnets with aggregator duty at that slot
- [`beacon_node/network/src/service.rs:572`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/service.rs#L572) passes should_process to handle_gossip
- [`beacon_node/network/src/service.rs:1445`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/service.rs#L1445) forwarded to send_unaggregated_attestation

**Sources.** [caplin#11906](https://github.com/erigontech/erigon/pull/11906), [ethlambda#221](https://github.com/lambdaclass/ethlambda/pull/221)

</details>

<a id="attestation_processing-117"></a>
<details>
<summary><b>attestation_processing-117</b> Running counter for pending attestation cap — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Keep a running count of pending attestations updated on insert/prune/delete instead of scanning the whole pending map under lock to enforce the cap.

**Gap in Lighthouse.** None; no scan of a pending map under lock to enforce the cap.

**Impact.** None.

**Best measured result.** limit check from ~184us to ~8ns (pr:prysm#17178)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:595`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L595) cap check uses attestations_delay_queue.len() (O(1))
- [`beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs:84`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/scheduler/work_reprocessing_queue.rs#L84) MAXIMUM_QUEUED_ATTESTATIONS

**Sources.** [prysm#17178](https://github.com/OffchainLabs/prysm/pull/17178)

</details>

<a id="attestation_processing-125"></a>
<details>
<summary><b>attestation_processing-125</b> Hoist base_reward_per_increment out of attestation loop — <i>implemented · low · S · cpu</i></summary>

**Idea.** Compute base_reward_per_increment once per block and reuse it for every attestation in process_attestations instead of recomputing it per attestation.

**Gap in Lighthouse.** None; per-attestation work is a cached lookup, nothing recomputed.

**Impact.** None.

**Best measured result.** process_attestations share of block_sim 1.5% -&gt; 0.25% (pr:nimbus#2704)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/epoch_cache.rs:96`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/epoch_cache.rs#L96) base_reward_per_increment computed once per epoch cache build
- [`consensus/state_processing/src/per_block_processing/process_operations.rs:280`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/process_operations.rs#L280) state.get_base_reward(index) is a table lookup

**Sources.** [nimbus#2704](https://github.com/status-im/nimbus-eth2/pull/2704)

</details>

<a id="attestation_processing-069"></a>
<details>
<summary><b>attestation_processing-069</b> Bound ancestry walks with canonical slot index — <i>n/a · low · S · cpu, latency, disk</i></summary>

**Idea.** Replace unbounded parent-chain walks in attestation validation with an O(1) check against a canonical slot-to-root index, stopping at the first canonical block above the ancestor's slot.

**Gap in Lighthouse.** 

**Impact.** Ancestry walks run on the in-memory proto-array node vector, not DB header reads, so the pathological cost does not occur.

**Best measured result.** ~119,000 header reads per attestation when finality lagged (pr:ethlambda#610)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/fork_choice/src/fork_choice.rs:509`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/fork_choice/src/fork_choice.rs#L509) get_ancestor on in-memory proto_array
- [`consensus/proto_array/src/proto_array_fork_choice.rs:1284`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array_fork_choice.rs#L1284)

**Sources.** [ethlambda#610](https://github.com/lambdaclass/ethlambda/pull/610)

</details>

<a id="attestation_processing-084"></a>
<details>
<summary><b>attestation_processing-084</b> Lightweight non-SSZ indexed attestation on hot paths — <i>n/a · low · S · cpu, memory</i></summary>

**Idea.** Represent indexed attestations on hot paths (validation, fork choice, pools, caches) as a plain struct with a vector of indices instead of a tree-backed SSZ object, skip sorting at construction, and convert to SSZ only when needed.

**Gap in Lighthouse.** 

**Impact.** IndexedAttestation is a flat ssz_types VariableList, not a persistent tree, so Teku's tree-backed cost does not exist.

**Best measured result.** Allocations in 50s window 15.56 GB to 12.97 GB (-16.6%); getIndexedAttestation 472 MB to 17 MB (-96.4%); ~52 MB/s less garbage (pr:teku#10599)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/common/get_attesting_indices.rs:25`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/common/get_attesting_indices.rs#L25) builds a plain VariableList Vec, not a tree-backed milhouse list

**Sources.** [teku#10599](https://github.com/Consensys-Incorporated/teku/pull/10599)

</details>

<a id="attestation_processing-121"></a>
<details>
<summary><b>attestation_processing-121</b> Fast-path single-bit merges and skip subgroup check — <i>n/a · low · S · cpu, latency</i></summary>

**Idea.** When packing the pool, merge single-bit attestations directly instead of running max-cover, and skip the BLS subgroup check when deserializing already-verified signatures.

**Gap in Lighthouse.** Lighthouse merges single-bit attestations on insert and keeps decoded AggregateSignature in the pool, so packing does no deserialization or subgroup check; a max-cover fast path would save little.

**Impact.** Packing already runs prev/curr epochs in parallel via rayon::join.

**Best measured result.** 7s batch: 1905ms to 789ms mean; 9s: 142ms to 86ms; 11s: 17ms to 9ms (pr:prysm#12350)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/operation_pool/src/attestation_storage.rs:457`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/attestation_storage.rs#L457) insert aggregates into stored aggregates at insert time
- [`beacon_node/operation_pool/src/lib.rs:345`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/operation_pool/src/lib.rs#L345) get_attestations runs maximum_cover over already-aggregated compact items
- [`crypto/bls/src/impls/blst.rs:74`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L74) subgroup check only in signature batch verification

**Sources.** [prysm#12350](https://github.com/OffchainLabs/prysm/pull/12350)

</details>

