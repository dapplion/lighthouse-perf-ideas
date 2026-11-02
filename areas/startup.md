# startup

5 ideas: 5 implemented; 0 actionable (high or medium value, verdict `not` or `partial`). [Back to the summary](../README.md).

Ids missing from the sequence are ideas that have not been checked against Lighthouse yet.

| id | idea | verdict | value | effort | resources |
|---|---|---|---|---|---|
| [startup-002](#startup-002) | Release the startup state after initialisation | implemented | medium |  | memory |
| [startup-003](#startup-003) | Timeout on the initial checkpoint state download | implemented | low |  | startup |
| [startup-006](#startup-006) | Resume from locally persisted finalized state, not remote checkpoint | implemented | medium |  | startup, sync |
| [startup-007](#startup-007) | Skip replay of unfinalized blocks on restart | implemented | medium |  | startup, memory, sync |
| [startup-008](#startup-008) | Start from the persisted head state | implemented | medium |  | startup, sync |

★ actionable. Click an id for the full record.

## Ideas

<a id="startup-002"></a>
<details>
<summary><b>startup-002</b> Release the startup state after initialisation — <i>implemented · medium · memory</i></summary>

**Idea.** After the finalized or anchor state loaded at startup has initialised fork choice and caches, drop every long-lived reference to it so the memory can be freed. This lowers steady-state heap use by one full beacon state.

**Impact.** No long-lived reference to the anchor state is kept by the builder; the store state cache is a bounded LRU. Nothing further to gain.

**Best measured result.** None (pr:prysm#13637)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/builder.rs:559`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/builder.rs#L559) checkpoint state is cloned (milhouse, structurally shared) into the store; the local snapshot/state go out of scope when weak_subjectivity_state returns
- [`beacon_node/beacon_chain/src/builder.rs:783`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/builder.rs#L783) after start, head state is reloaded from the store via get_advanced_hot_state

**Sources.** [prysm#13637](https://github.com/OffchainLabs/prysm/pull/13637)

</details>


<a id="startup-003"></a>
<details>
<summary><b>startup-003</b> Timeout on the initial checkpoint state download — <i>implemented · low · startup</i></summary>

**Idea.** Put a bounded timeout (for example 2 minutes) on the HTTP download of the initial checkpoint-sync state. Startup then fails fast with a clear error instead of hanging forever on a stalled remote.

**Impact.** Already bounded (180s, configurable); startup fails with a clear error on a stalled remote.

**Best measured result.** None (pr:teku#6598)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/client/src/builder.rs:435`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/client/src/builder.rs#L435) Timeouts::set_all(checkpoint_sync_url_timeout) on the remote client
- [`beacon_node/src/cli.rs:1280`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/cli.rs#L1280) --checkpoint-sync-url-timeout default 180s

**Sources.** [teku#6598](https://github.com/Consensys-Incorporated/teku/pull/6598)

</details>


<a id="startup-006"></a>
<details>
<summary><b>startup-006</b> Resume from locally persisted finalized state, not remote checkpoint — <i>implemented · medium · startup, sync</i></summary>

**Idea.** Persist the node's own finalized state periodically (atomic temp file plus rename), and on restart resume from it when it is inside the data-availability retention window. This avoids fetching a fresh remote checkpoint that lies ahead of the execution layer and forces a history backfill before the node can serve.

**Impact.** On restart Lighthouse resumes from its own DB and never contacts a remote checkpoint, so no backfill is forced.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/builder.rs:229`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/builder.rs#L229) resume_from_db loads PersistedBeaconChain and fork choice from the local DB
- [`beacon_node/beacon_chain/src/builder.rs:783`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/builder.rs#L783) head state from the hot DB
- [`beacon_node/client/src/builder.rs:435`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/client/src/builder.rs#L435) checkpoint sync URL only used on a fresh DB

**Sources.** [caplin#22746](https://github.com/erigontech/erigon/pull/22746)

</details>


<a id="startup-007"></a>
<details>
<summary><b>startup-007</b> Skip replay of unfinalized blocks on restart — <i>implemented · medium · startup, memory, sync</i></summary>

**Idea.** On restart, restore only the finalized state and rebuild fork choice from stored block summaries, instead of re-executing every unfinalized block through the state transition. This avoids duplicate block processing and the memory spike that can cause OOM.

**Impact.** Restart does not re-execute unfinalized blocks; fork choice is restored from its persisted proto-array. Only a few-slot head advance from the nearest hot state is replayed.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/builder.rs:243`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/builder.rs#L243) BeaconChain::load_fork_choice loads the persisted fork choice (PersistedForkChoice) instead of replaying blocks
- [`beacon_node/beacon_chain/src/builder.rs:768`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/builder.rs#L768) head chosen from fork choice, only head block+state loaded

**Sources.** [lodestar#1527](https://github.com/ChainSafe/lodestar/pull/1527)

</details>


<a id="startup-008"></a>
<details>
<summary><b>startup-008</b> Start from the persisted head state — <i>implemented · medium · startup, sync</i></summary>

**Idea.** Persist the head state and, on restart, load it directly as the starting state instead of loading the finalized state and replaying blocks up to the head. This removes the replay cost from finalized to head at startup.

**Impact.** Head state is loaded from the hot DB at startup; replay is at most from the latest stored hot state/diff, not from finalized to head.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/builder.rs:783`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/builder.rs#L783) store.get_advanced_hot_state(head_block_root,...) loads the head state directly
- [`beacon_node/store/src/hot_cold_store.rs:1124`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1124) get_advanced_hot_state uses cache or load_hot_state

**Sources.** [prysm#4906](https://github.com/OffchainLabs/prysm/pull/4906)

</details>


