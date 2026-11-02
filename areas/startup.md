# startup

8 ideas: 1 partial, 5 implemented, 2 n/a; 0 actionable (high or medium value, verdict `not` or `partial`). [Back to the summary](../README.md).

| id | idea | verdict | value | effort | resources |
|---|---|---|---|---|---|
| [startup-001](#startup-001) | Cache the decoded embedded genesis state process-wide | partial | low | S | cpu, startup |
| [startup-002](#startup-002) | Release the startup state after initialisation | implemented | low | S | memory |
| [startup-003](#startup-003) | Timeout on the initial checkpoint state download | implemented | low | S | startup |
| [startup-004](#startup-004) | Lazily load validator-only libraries in beacon node | n/a | low |  | startup, memory |
| [startup-005](#startup-005) | Start beacon chain before loading validator keys | n/a | low |  | startup |
| [startup-006](#startup-006) | Resume from locally persisted finalized state, not remote checkpoint | implemented | low | S | startup, sync |
| [startup-007](#startup-007) | Skip replay of unfinalized blocks on restart | implemented | low | S | startup, memory, sync |
| [startup-008](#startup-008) | Start from the persisted head state | implemented | low | S | startup, sync |

★ actionable. Click an id for the full record.

## Ideas

<a id="startup-001"></a>
<details>
<summary><b>startup-001</b> Cache the decoded embedded genesis state process-wide — <i>partial · low · S · cpu, startup</i></summary>

**Idea.** Decompress and SSZ-decode the embedded (compiled-in) genesis state once and keep the result in a process-wide lazily initialised value. Every later caller reuses it instead of decompressing and decoding it again, which saves CPU at startup.

**Gap in Lighthouse.** Memoise the decoded BeaconState in a OnceLock on Eth2NetworkConfig (or decode once and return clones) so the four accessors share one decode. Mainnet uses a Url source and is unaffected; only embedded-genesis testnets benefit.

**Impact.** Saves a few repeated SSZ decodes of the genesis state at startup on embedded-genesis networks only; one-time and small.

**Evidence (Lighthouse @ 928b61e719).**

- [`common/eth2_network_config/src/lib.rs:257`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/eth2_network_config/src/lib.rs#L257) get_genesis_state_from_bytes decodes on every call
- [`common/eth2_network_config/src/lib.rs:141`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/eth2_network_config/src/lib.rs#L141) genesis_time, :162 genesis_validators_root, :181 genesis_state_root, :216 genesis_state each decode again
- [`common/eth2_network_config/src/lib.rs:50`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/eth2_network_config/src/lib.rs#L50) bytes held in a plain Option, no OnceLock

**Sources.** [prysm#15673](https://github.com/OffchainLabs/prysm/pull/15673)

</details>


<a id="startup-002"></a>
<details>
<summary><b>startup-002</b> Release the startup state after initialisation — <i>implemented · low · S · memory</i></summary>

**Idea.** After the finalized or anchor state loaded at startup has initialised fork choice and caches, drop every long-lived reference to it so the memory can be freed. This lowers steady-state heap use by one full beacon state.

**Impact.** No startup-only reference survives: the anchor snapshot is consumed by get_forkchoice_store, which keeps only justified balances, and the genesis state in resume_from_db is dropped after genesis_time is read. The anchor stays as StateCache.finalized_state only until the next finalization replaces it. That is the normal finalized-state role, not a leak.

**Best measured result.** None (pr:prysm#13637)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/builder.rs:602`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/builder.rs#L602)
- [`beacon_node/beacon_chain/src/beacon_fork_choice_store.rs:110`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_fork_choice_store.rs#L110)
- [`beacon_node/beacon_chain/src/beacon_fork_choice_store.rs:175`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_fork_choice_store.rs#L175)
- [`beacon_node/beacon_chain/src/builder.rs:260`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/builder.rs#L260)
- [`beacon_node/store/src/state_cache.rs:127`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L127)

**Skeptic check.** Checked weak_subjectivity_state, set_genesis_state, resume_from_db and BeaconForkChoiceStore fields. None of them hold a BeaconState for the long term. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#13637](https://github.com/OffchainLabs/prysm/pull/13637)

</details>


<a id="startup-003"></a>
<details>
<summary><b>startup-003</b> Timeout on the initial checkpoint state download — <i>implemented · low · S · startup</i></summary>

**Idea.** Put a bounded timeout (for example 2 minutes) on the HTTP download of the initial checkpoint-sync state. Startup then fails fast with a clear error instead of hanging forever on a stalled remote.

**Impact.** The checkpoint state, block and blob downloads each use a per-request reqwest timeout that also covers reading the body. The default is 180s and it is configurable, and a stall gives a clear error.

**Best measured result.** None (pr:teku#6598)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/client/src/builder.rs:432`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/client/src/builder.rs#L432)
- [`beacon_node/src/cli.rs:1280`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/cli.rs#L1280)
- [`common/eth2/src/lib.rs:2779`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/eth2/src/lib.rs#L2779)
- [`common/eth2/src/lib.rs:341`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/eth2/src/lib.rs#L341)

**Skeptic check.** Timeouts::set_all sets get_debug_beacon_states, and get_bytes_opt_accept_header applies it with RequestBuilder::timeout, which covers the whole response body. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#6598](https://github.com/Consensys-Incorporated/teku/pull/6598)

</details>


<a id="startup-004"></a>
<details>
<summary><b>startup-004</b> Lazily load validator-only libraries in beacon node — <i>n/a · low · startup, memory</i></summary>

**Idea.** Load libraries that only the validator client needs (for example the keystore file-lock library) lazily at first use, not at process import time. A beacon-node-only process then does not pay their load time, memory, or registered process listeners.

**Impact.** Rust links statically and has no import-time library loading; the VC code is not run in the beacon node process.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/src/lib.rs:8`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/src/lib.rs#L8) validator code is in a separate binary crate

**Sources.** [lodestar@3c0fd84d7](https://github.com/ChainSafe/lodestar/commit/3c0fd84d7917)

</details>


<a id="startup-005"></a>
<details>
<summary><b>startup-005</b> Start beacon chain before loading validator keys — <i>n/a · low · startup</i></summary>

**Idea.** Start the beacon chain and networking services before decrypting and loading validator keys, or load keys in parallel. Slow key loading with many keys then does not delay the node becoming available.

**Impact.** Lighthouse's beacon node does not load validator keys; the VC is a separate process, so key loading cannot delay the beacon chain.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/src/lib.rs:207`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/src/lib.rs#L207) InitializedValidators::from_definitions runs in the separate validator client

**Sources.** [teku#3390](https://github.com/Consensys-Incorporated/teku/pull/3390)

</details>


<a id="startup-006"></a>
<details>
<summary><b>startup-006</b> Resume from locally persisted finalized state, not remote checkpoint — <i>implemented · low · S · startup, sync</i></summary>

**Idea.** Persist the node's own finalized state periodically (atomic temp file plus rename), and on restart resume from it when it is inside the data-availability retention window. This avoids fetching a fresh remote checkpoint that lies ahead of the execution layer and forces a history backfill before the node can serve.

**Impact.** When a chain DB exists, Lighthouse resumes from its own DB: the persisted chain, fork choice and hot/finalized states. It ignores the checkpoint URL, so it never needs a forced backfill on restart.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/client/src/builder.rs:290`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/client/src/builder.rs#L290)
- [`beacon_node/client/src/builder.rs:507`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/client/src/builder.rs#L507)
- [`beacon_node/beacon_chain/src/builder.rs:229`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/builder.rs#L229)
- [`beacon_node/beacon_chain/src/builder.rs:784`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/builder.rs#L784)

**Skeptic check.** Client builder line 290 forces ClientGenesis::FromStore when the chain exists, which leads to resume_from_db. The local finalized/split state is kept atomically in the hot/cold DB. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [caplin#22746](https://github.com/erigontech/erigon/pull/22746)

</details>


<a id="startup-007"></a>
<details>
<summary><b>startup-007</b> Skip replay of unfinalized blocks on restart — <i>implemented · low · S · startup, memory, sync</i></summary>

**Idea.** On restart, restore only the finalized state and rebuild fork choice from stored block summaries, instead of re-executing every unfinalized block through the state transition. This avoids duplicate block processing and the memory spike that can cause OOM.

**Impact.** Fork choice comes back from the persisted proto-array (PersistedForkChoice::from_bytes, then ForkChoice::from_persisted) without executing any block. Only the head state is loaded.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:692`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L692)
- [`beacon_node/beacon_chain/src/builder.rs:245`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/builder.rs#L245)
- [`beacon_node/beacon_chain/src/builder.rs:770`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/builder.rs#L770)

**Skeptic check.** load_fork_choice only deserializes, and no fork-revert replay path remains in beacon_chain/src. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#1527](https://github.com/ChainSafe/lodestar/pull/1527)

</details>


<a id="startup-008"></a>
<details>
<summary><b>startup-008</b> Start from the persisted head state — <i>implemented · low · S · startup, sync</i></summary>

**Idea.** Persist the head state and, on restart, load it directly as the starting state instead of loading the finalized state and replaying blocks up to the head. This removes the replay cost from finalized to head at startup.

**Impact.** The head state is loaded by its own root through load_hot_state, which reads its hot summary and diff base. The replay is bounded by the hot diff layout and does not run from finalized to head.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/builder.rs:783`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/builder.rs#L783)
- [`beacon_node/store/src/hot_cold_store.rs:1124`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1124)
- [`beacon_node/store/src/hot_cold_store.rs:1959`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1959)

**Skeptic check.** get_advanced_hot_state(head_block_root, current_slot, head_block.state_root()) targets the head state directly. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#4906](https://github.com/OffchainLabs/prysm/pull/4906)

</details>


