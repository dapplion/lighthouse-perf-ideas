# gossip_validation (part 2 of 2)

157 ideas: 27 not, 23 partial, 80 implemented, 27 n/a; 25 actionable (high or medium value, verdict `not` or `partial`). [Back to the summary](../README.md).

Pages: [part 1](gossip_validation.md) · [part 2](gossip_validation-2.md)

<a id="gossip_validation-155"></a>
<details>
<summary><b>gossip_validation-155</b> Skip hash tree root computed only for logging — <i>implemented · low · S · cpu</i></summary>

**Idea.** Do not compute hash tree root of attestations or aggregates for log context on every gossip message; log it only on error paths.

**Impact.** No hash tree root is computed only for logging on the success path. The two logging roots sit in slasher error branches, and tracing evaluates them lazily.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/attestation_verification.rs:455-479`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L455-L479)
- [`beacon_node/beacon_chain/src/attestation_verification.rs:562`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L562)

**Skeptic check.** Verified: the root at line 562 is the aggregate dedup key, and gossip_methods.rs computes no tree_hash_root or canonical_root for logging. The earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#2202](https://github.com/ChainSafe/lodestar/pull/2202)

</details>


<a id="gossip_validation-156"></a>
<details>
<summary><b>gossip_validation-156</b> Validate light client gossip against local update, no storage — <i>implemented · low · S · cpu, memory, disk</i></summary>

**Idea.** Validate gossiped light client updates by comparing with the locally computed update without storing received ones, and exit early when no local update exists to compare.

**Impact.** None left; gossiped updates are validated by comparison with the local one and not stored beyond one dedup clone.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/light_client_finality_update_verification.rs:105-108`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/light_client_finality_update_verification.rs#L105-L108) get_latest_finality_update().ok_or(FailedConstructingUpdate) exits early with no local update
- [`beacon_node/beacon_chain/src/light_client_finality_update_verification.rs:119-155`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/light_client_finality_update_verification.rs#L119-L155) equality comparison against the locally built update
- [`beacon_node/beacon_chain/src/light_client_finality_update_verification.rs:157-159`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/light_client_finality_update_verification.rs#L157-L159) only stores the accepted update as the latest-broadcasted dedup marker
- [`beacon_node/beacon_chain/src/light_client_optimistic_update_verification.rs:112-113`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/light_client_optimistic_update_verification.rs#L112-L113),152 same pattern for optimistic updates

**Skeptic check.** Confirmed both finality and optimistic verification compare with the local cache update, exit early when none exists, and keep only the last broadcast copy. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#15783](https://github.com/OffchainLabs/prysm/pull/15783)

</details>


<a id="gossip_validation-157"></a>
<details>
<summary><b>gossip_validation-157</b> Reject subscriptions to unknown gossip topics — <i>implemented · low · S · bandwidth, memory</i></summary>

**Idea.** Keep a precomputed set of valid topics and reject peer subscriptions to any other topic, so the router tracks no mesh state and forwards no traffic for arbitrary topics.

**Impact.** Peer subscriptions to unknown topics are dropped, so no mesh or forwarding state is kept for them.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/service/mod.rs:332`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/mod.rs#L332) MaxCountSubscriptionFilter over a whitelist
- [`beacon_node/lighthouse_network/src/service/utils.rs:268-300`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/service/utils.rs#L268-L300) create_whitelist_filter precomputes topic hashes for all fork digests
- ~/.cargo/git/checkouts/rust-libp2p-b7fa834aec8fc27c/accba72/protocols/gossipsub/src/behaviour.rs:2111 filter_incoming_subscriptions applied before peer topic state is updated
- ~/.cargo/git/checkouts/rust-libp2p-b7fa834aec8fc27c/accba72/protocols/gossipsub/src/subscription_filter.rs:102-130 whitelist and max-count filters

**Skeptic check.** Verified the whitelist hash set is built at startup and the gossipsub behaviour filters incoming subscriptions through it. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#2237](https://github.com/status-im/nimbus-eth2/pull/2237)

</details>


