# Consensus client performance ideas

A study of the performance work in the PR and commit history of 9 Ethereum consensus clients: Prysm, Teku, Lodestar, Nimbus, Lighthouse, Grandine, Caplin (Erigon), Silver and ethlambda. The history yields 1,563 distinct performance ideas. Each one was checked against Lighthouse [`unstable` @ `928b61e719`](https://github.com/sigp/lighthouse/tree/928b61e719c39f7fe8c074767b594fb99f4379bd) (2026-10-30). Built 2026-11-02.

Files:

- `README.md`: this summary: the data snapshot, totals, ranked proposals, and how to update.
- `areas/<area>.md`: every checked idea of one area, actionable ideas first. Click an idea for the gap, the evidence and the sources. The area index is under [Totals](#totals).
- `ideas.csv`: one row per idea. GitHub shows it as a searchable table.
- `ideas.jsonl`: the same ideas with every field, for scripts and agents.
- `registry.csv`: every scraped PR and commit, how far it got in the pipeline, and the idea it became.
- `corpus/`: the scraper (`corpus.py`, `repos.json`, its own README) and the scraped PRs and commits of all 9 clients in `corpus/data/`.
- `pipeline/`: the scripts and the agent workflows that turned the corpus into ideas.

## How the list was made

1. **Corpus.** The full PR and commit histories of the 9 clients: about 49k PRs and 48k commits. For Erigon, only the commits that touch `cl/` and the PRs they reference are included.
2. **Triage.** An LLM read 56.8k items, after bot PRs and dependency bumps were removed. 2,977 items that matched perf keywords were always sent on. 6.4k perf records came out.
3. **Clustering.** The records were merged into 3,675 distinct ideas.
4. **Prescreen.** An idea was kept when it applies to Lighthouse and has high or medium value, has 3 or more sources, or has a measured result. 1,563 ideas were kept.
5. **Check.** For each idea, an agent read the Lighthouse code and gave a verdict with file and line evidence. Every `not` or `partial` verdict on a high or medium idea then went to a second agent that was told to disprove it. That pass changed 73 of 337 verdicts.

## How to read it

| field | meaning |
|---|---|
| verdict `implemented` | Lighthouse already does this, or something equivalent |
| verdict `partial` | Lighthouse does part of it; the gap says what is missing |
| verdict `not` | not in Lighthouse |
| verdict `n/a` | does not apply to Lighthouse's design |
| value | the expected effect on a mainnet node: high, medium or low |
| effort | S, M or L, where the checker gave one |
| actionable | high or medium value, with verdict `not` or `partial` |

**The verdicts are LLM judgements with evidence.** Read the evidence before you act on one. Spot checks found some wrong `implemented` verdicts, so `implemented` contains false positives too.

## Ranked proposals

These come from joining the actionable ideas with measurements: Lighthouse metrics from sigp mainnet nodes (7 days, v8.3.0) and a 128-block mainnet replay of Lighthouse against Silver on the same blocks. In the replay, Lighthouse spends 90.4 ms of comparable work per block and Silver 12.6 ms. The gains are estimates unless marked measured, and they overlap, so they do not add up.

| # | Proposal | Expected gain | Open PR | Ideas |
|---|---|---|---|---|
| 1 | Batch gossip unaggregated attestations (fire at 8-16 queued or 10 ms) and group signature sets by signing root | about −1.7 cores on a node that subscribes to all subnets | [#9641](https://github.com/sigp/lighthouse/pull/9641), [#9521](https://github.com/sigp/lighthouse/pull/9521) | [attestation_processing-123](areas/attestation_processing.md#attestation_processing-123), -006, -007, bls-012, -017 |
| 2 | glibc `M_MMAP_THRESHOLD`=128 KiB (optionally `M_ARENA_MAX`=4) alongside jemalloc | about −1 to −1.5 GB RSS after 2 weeks of uptime | | [allocator_runtime-027](areas/allocator_runtime.md#allocator_runtime-027), -028 |
| 3 | Hot hdiff buffer cache from 1 to 2 entries; do not clone a buffer the cache rejects | −0.7 s on the epoch-boundary import | | [db_hot-020](areas/db_hot.md#db_hot-020), -039, [state_cache-187](areas/state_cache.md#state_cache-187), -225 |
| 4 | Cold hdiff cache keeps only the live base buffers (interim: `--hdiff-buffer-cache-size 6`) | −3.5 to −4.6 GB on archive nodes (cache model) | | db_cold-049 |
| 5 | Serve post-Fulu next-epoch proposer duties from `beacon_proposer_cache` | `process_epoch` runs per epoch 5.2 → ~1.6 | [#10459](https://github.com/sigp/lighthouse/pull/10459) | [beacon_api-004](areas/beacon_api.md#beacon_api-004) |
| 6 | Batch-affine pubkey addition for signature sets of 64+ keys | −12 ms per block | | [bls-064](areas/bls.md#bls-064), [block_import-097](areas/block_import.md#block_import-097) |
| 7 | Linear `compute_on_chain_aggregate`, plus a timer | −110 to −130 ms of the 200 ms attestation packing | | [op_pool-019](areas/op_pool.md#op_pool-019), -018 |
| 8 | Release the fork-choice lock before encode + zstd on persist | lock hold 0.5 → 0.1 s | | [db_hot-101](areas/db_hot.md#db_hot-101) |
| 9 | `ssz_types` `hash_vec` hashes u8 lists as whole slices | −3.3 ms per block (measured in a bench) | | [tree_hash-072](areas/tree_hash.md#tree_hash-072), -032 |
| 10 | On an E+2 shuffling miss, build the committee cache from the unadvanced state | miss cost 0.75 → ~0.1 s | | [state_cache-026](areas/state_cache.md#state_cache-026), [attestation_processing-037](areas/attestation_processing.md#attestation_processing-037) |
| 11 | Sparse-then-dense update map for `balances` in milhouse | −12 ms per block | | [state_transition-001](areas/state_transition.md#state_transition-001) |
| 12 | 8-pair block swap in `shuffle_list` | −20 ms per shuffle (measured in a bench) | | [epoch_processing-086](areas/epoch_processing.md#epoch_processing-086) |
| 13 | Split the parallel tree hash only where both children are dirty | −10 ms CPU per block | | [tree_hash-065](areas/tree_hash.md#tree_hash-065) |
| 14 | Hash the transactions once; pass the payload header through `ConsensusContext` | −3.4 to −7.6 ms per block | | tree_hash-028 |
| 15 | Collect the E+1 active indices once for the lookahead and the next committee cache | −48 to −95 ms per epoch boundary | | [epoch_processing-091](areas/epoch_processing.md#epoch_processing-091), -088 |
| 16 | Batch the released unknown-block attestations | 4.3× faster drain of the reprocess queue | | [attestation_processing-011](areas/attestation_processing.md#attestation_processing-011), -009, -104 |
| 17 | milhouse `HashCell` in place of `RwLock<Hash256>` | −3 to −6 ms CPU per block | [milhouse#98](https://github.com/sigp/milhouse/pull/98) | |
| 18 | Compute the hot state DB ops before the fork-choice write lock | lock hold ~1.5 → 0.1 s at the epoch boundary | | [db_hot-037](areas/db_hot.md#db_hot-037), -004, [block_import-136](areas/block_import.md#block_import-136) |
| 19 | IDONTWANT threshold at 200 B, A/B with per-path duplicate metrics | −0.3 to −0.65 MB/s inbound (unverified) | | [gossipsub-001](areas/gossipsub.md#gossipsub-001), -002, -003 |
| 20 | `Arc<HDiffBuffer>` in the hot and cold caches | −70 ms off the epoch-boundary spike | overlaps [#9236](https://github.com/sigp/lighthouse/pull/9236) | [state_cache-225](areas/state_cache.md#state_cache-225) |
| 21 | Per-committee aggregate pubkeys minus the missing members (as Silver and ethlambda do) | −13 ms per block | | [bls-025](areas/bls.md#bls-025), -093, [attestation_processing-060](areas/attestation_processing.md#attestation_processing-060) |
| 22 | hashtree for 64-byte hashes; a `MerkleHasher` that works on digests | −8 to −9 ms CPU per block | | [tree_hash-001](areas/tree_hash.md#tree_hash-001), -003, -004, -020 |
| 23 | Batch the KZG verification of gossip columns per block; verify the proposer header signature once per block | 3-4× less column job time in Lodestar (unverified for Lighthouse) | | [kzg-010](areas/kzg.md#kzg-010), [gossip_validation-066](areas/gossip_validation.md#gossip_validation-066), [data_availability-035](areas/data_availability.md#data_availability-035) |

## Data snapshot

The ideas were checked against Lighthouse `unstable` at [`928b61e719`](https://github.com/sigp/lighthouse/commit/928b61e719c39f7fe8c074767b594fb99f4379bd) (2026-10-30).

The corpus holds every PR and every commit on the main branch of each client, up to:

| client | repo | branch | newest PR | PRs | latest commit | commits | scraped |
|---|---|---|---|---|---|---|---|
| lighthouse | [sigp/lighthouse](https://github.com/sigp/lighthouse) | `unstable` | [#10512](https://github.com/sigp/lighthouse/pull/10512) | 7,808 | [`928b61e719`](https://github.com/sigp/lighthouse/commit/928b61e719c39f7fe8c074767b594fb99f4379bd) (2026-10-30) | 7,198 | 2026-11-02 |
| prysm | [OffchainLabs/prysm](https://github.com/OffchainLabs/prysm) | `develop` | [#17804](https://github.com/OffchainLabs/prysm/pull/17804) | 14,024 | [`26fad561fb`](https://github.com/OffchainLabs/prysm/commit/26fad561fb82f11cf9ffe2ddd389f5703b4ebf08) (2026-11-01) | 10,779 | 2026-11-02 |
| teku | [Consensys-Incorporated/teku](https://github.com/Consensys-Incorporated/teku) | `master` | [#11604](https://github.com/Consensys-Incorporated/teku/pull/11604) | 8,178 | [`dd3fd1f354`](https://github.com/Consensys-Incorporated/teku/commit/dd3fd1f354f43bbfda60fa7ea7b17590966fa753) (2026-11-02) | 7,178 | 2026-11-02 |
| nimbus | [status-im/nimbus-eth2](https://github.com/status-im/nimbus-eth2) | `unstable` | [#9418](https://github.com/status-im/nimbus-eth2/pull/9418) | 8,062 | [`16d261a258`](https://github.com/status-im/nimbus-eth2/commit/16d261a258bf06ad54f4d8def1ed2a58c6817392) (2026-11-01) | 8,840 | 2026-11-02 |
| lodestar | [ChainSafe/lodestar](https://github.com/ChainSafe/lodestar) | `unstable` | [#10531](https://github.com/ChainSafe/lodestar/pull/10531) | 7,233 | [`8d8efcbf5f`](https://github.com/ChainSafe/lodestar/commit/8d8efcbf5fab80e26f2700d1197154541e1d2f9f) (2026-10-31) | 10,763 | 2026-11-02 |
| grandine | [grandinetech/grandine](https://github.com/grandinetech/grandine) | `develop` | [#1024](https://github.com/grandinetech/grandine/pull/1024) | 755 | [`48ec7eb991`](https://github.com/grandinetech/grandine/commit/48ec7eb99184c37ef29ade716255b1baac7693aa) (2026-10-30) | 1,114 | 2026-11-02 |
| silver | [gattaca-com/silver](https://github.com/gattaca-com/silver) | `main` | [#455](https://github.com/gattaca-com/silver/pull/455) | 437 | [`a5ca677dbe`](https://github.com/gattaca-com/silver/commit/a5ca677dbee0b3618119ee807c84303397e6bdd6) (2026-10-30) | 427 | 2026-11-02 |
| ethlambda | [lambdaclass/ethlambda](https://github.com/lambdaclass/ethlambda) | `main` | [#756](https://github.com/lambdaclass/ethlambda/pull/756) | 599 | [`012dc4f498`](https://github.com/lambdaclass/ethlambda/commit/012dc4f4980520a090a68fe654bc3d610beae5b8) (2026-10-30) | 459 | 2026-11-02 |
| caplin | [erigontech/erigon](https://github.com/erigontech/erigon) | `main` (`cl/` only) | [#25656](https://github.com/erigontech/erigon/pull/25656) | 1,464 | [`4986a2e23a`](https://github.com/erigontech/erigon/commit/4986a2e23aaeb37175dd12623f7627b139069f3f) (2026-11-01) | 1,500 | 2026-11-02 |

The full registry is in `corpus/data/` (every PR and commit as JSONL) and `registry.csv` (how far each item got in the pipeline, and its idea id).

## Totals

Verdict by value:

| verdict | high | medium | low | unrated | total |
|---|---|---|---|---|---|
| not | 7 | 135 | 95 | 0 | 237 |
| partial | 9 | 163 | 102 | 0 | 274 |
| implemented | 49 | 484 | 378 | 0 | 911 |
| n/a | 3 | 64 | 74 | 0 | 141 |
| unchecked | 0 | 0 | 0 | 0 | 0 |
| **total** | 68 | 846 | 649 | 0 | 1563 |

By area, sorted by actionable count. The area is the prefix of the idea id.

| area | ideas | actionable | not | partial | implemented | n/a | unchecked |
|---|---|---|---|---|---|---|---|
| [beacon_api](areas/beacon_api.md) | 129 | 29 | 20 | 25 | 78 | 6 | 0 |
| [data_availability](areas/data_availability.md) | 97 | 28 | 17 | 18 | 55 | 7 | 0 |
| [gossip_validation](areas/gossip_validation.md) | 68 | 23 | 11 | 16 | 39 | 2 | 0 |
| [block_import](areas/block_import.md) | 77 | 21 | 9 | 14 | 49 | 5 | 0 |
| [db_cold](areas/db_cold.md) | 75 | 18 | 13 | 10 | 40 | 12 | 0 |
| [db_hot](areas/db_hot.md) | 69 | 18 | 12 | 15 | 32 | 10 | 0 |
| [state_cache](areas/state_cache.md) | 124 | 17 | 11 | 12 | 79 | 22 | 0 |
| [attestation_processing](areas/attestation_processing.md) | 63 | 16 | 13 | 9 | 38 | 3 | 0 |
| [range_sync](areas/range_sync.md) | 58 | 16 | 11 | 12 | 32 | 3 | 0 |
| [el_interaction](areas/el_interaction.md) | 41 | 15 | 7 | 10 | 20 | 4 | 0 |
| [gossipsub](areas/gossipsub.md) | 55 | 12 | 12 | 8 | 33 | 2 | 0 |
| [block_production](areas/block_production.md) | 55 | 11 | 11 | 6 | 34 | 4 | 0 |
| [rpc](areas/rpc.md) | 45 | 10 | 7 | 10 | 26 | 2 | 0 |
| [bls](areas/bls.md) | 40 | 9 | 11 | 4 | 22 | 3 | 0 |
| [lookup_sync](areas/lookup_sync.md) | 17 | 7 | 2 | 5 | 10 | 0 | 0 |
| [op_pool](areas/op_pool.md) | 39 | 7 | 4 | 10 | 22 | 3 | 0 |
| [other_caches](areas/other_caches.md) | 38 | 7 | 7 | 8 | 20 | 3 | 0 |
| [fork_choice](areas/fork_choice.md) | 63 | 6 | 5 | 9 | 41 | 8 | 0 |
| [tree_hash](areas/tree_hash.md) | 41 | 6 | 9 | 4 | 25 | 3 | 0 |
| [discovery_peers](areas/discovery_peers.md) | 40 | 5 | 5 | 7 | 26 | 2 | 0 |
| [logging_metrics](areas/logging_metrics.md) | 21 | 5 | 2 | 9 | 9 | 1 | 0 |
| [allocator_runtime](areas/allocator_runtime.md) | 18 | 4 | 2 | 6 | 7 | 3 | 0 |
| [kzg](areas/kzg.md) | 25 | 4 | 5 | 2 | 17 | 1 | 0 |
| [ssz](areas/ssz.md) | 23 | 4 | 4 | 6 | 8 | 5 | 0 |
| [validator_client](areas/validator_client.md) | 49 | 4 | 8 | 10 | 27 | 4 | 0 |
| [backfill](areas/backfill.md) | 14 | 3 | 2 | 1 | 11 | 0 | 0 |
| [epoch_processing](areas/epoch_processing.md) | 62 | 3 | 7 | 10 | 41 | 4 | 0 |
| [state_transition](areas/state_transition.md) | 68 | 3 | 5 | 9 | 44 | 10 | 0 |
| [build](areas/build.md) | 22 | 2 | 3 | 6 | 9 | 4 | 0 |
| [other](areas/other.md) | 22 | 1 | 2 | 3 | 12 | 5 | 0 |
| [startup](areas/startup.md) | 5 | 0 | 0 | 0 | 5 | 0 | 0 |

Ideas by the client whose PRs or commits produced them (an idea can come from several clients):

| client | ideas | actionable |
|---|---|---|
| prysm | 604 | 97 |
| lodestar | 460 | 80 |
| lighthouse | 412 | 57 |
| teku | 371 | 82 |
| nimbus | 363 | 78 |
| caplin | 154 | 31 |
| grandine | 128 | 35 |
| ethlambda | 64 | 14 |
| silver | 59 | 19 |

## Limits

- **Triage recall.** A sample of 400 rejected items had 1 minor perf miss, but only 17 of the 400 were read in full. Expect some ideas to be missing.
- **Verdicts.** No one re-read the 911 `implemented` verdicts after the first check. 2,112 more ideas, most of them low value, were never checked against Lighthouse.
- **Measurements.** The replay covers the state transition only. Networking, DB and op-pool numbers come from fleet metrics plus models or benchmarks.
- **Not covered.** The execution layer, the validator client, the slasher, Gloas-only paths, sync throughput, and changes that no client has made.

## Updating

The steps below add the PRs and commits since the snapshot, and re-check ideas against a newer Lighthouse.

1. **Scrape.** `corpus/corpus.py update` reads new and changed PRs, and new commits, of every client into the SQLite DB (`CL_CORPUS_DB`). Then `corpus/corpus.py export corpus/data` refreshes the JSONL files.
2. **Select.** `pipeline/make_batches.py <dir> 300 --new` writes only the items that `registry.csv` does not have, plus PRs whose state changed (for example OPEN to MERGED).
3. **Triage and extract.** Run `pipeline/workflows/triage-extract.js` on those batches, then `pipeline/make_cluster_in.py`.
4. **Cluster.** Run `pipeline/workflows/cluster.js`.
5. **Screen and check.** Run `pipeline/workflows/screen.js`, then `pipeline/workflows/lh-check.js` against a Lighthouse checkout. To re-check everything against a newer Lighthouse, check out that commit, and set `SHA` and `SHA_DATE` in `pipeline/make_repo.py`.
6. **Publish.** Set `PERF_DATA` to the `data/derived/` directory and `LH_CHECKOUT` to the Lighthouse checkout. `pipeline/make_registry.py` rewrites `registry.csv`. `pipeline/make_repo.py` rewrites the README, `areas/`, `ideas.csv` and `ideas.jsonl`. Commit and push.

Steps 1, 2 and 6 are incremental. Steps 3 to 5 are not yet:

- `cluster.js` clusters each area from scratch, so a re-run renumbers the idea ids. An incremental run needs a step that matches new records to the existing ideas first.
- The input files for `screen.js` and `lh-check.js` were built with one-off commands that are not in `pipeline/`.

The workflows are [Claude Code](https://docs.claude.com/en/docs/claude-code) workflow scripts: each one fans out subagents over batch files. Pass `root` (the directory that holds `data/derived/`), `lh` (the Lighthouse checkout) and `pipeline` (this directory) in the workflow args.
