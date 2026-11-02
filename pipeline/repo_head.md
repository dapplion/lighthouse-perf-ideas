# Consensus client performance ideas

A study of the performance work in the PR and commit history of 9 Ethereum consensus clients: Prysm, Teku, Lodestar, Nimbus, Lighthouse, Grandine, Caplin (Erigon), Silver and ethlambda. The history yields 3,917 distinct performance ideas. Each one was checked against Lighthouse [`unstable` @ `928b61e719`](https://github.com/sigp/lighthouse/tree/928b61e719c39f7fe8c074767b594fb99f4379bd) (2026-10-30). Built 2026-11-02.

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
2. **Triage.** An LLM read 56.8k items, after bot PRs and dependency bumps were removed, from the title and the start of the body. 2,977 items that matched perf keywords were always sent on.
3. **Second triage.** The 43,094 items that the first triage rejected were read again with up to 1,200 characters of body and the changed files. 2,916 were sent on, and 733 of them turned out to be performance changes. Every decision of this pass is saved with a reason in `registry.csv`.
4. **Extraction.** An agent read each item that was sent on in full (with the diff when the text was thin) and wrote a performance record. 7,182 records came out.
5. **Clustering.** The first 6,449 records were merged into 3,675 distinct ideas. The 733 records of the second triage were then matched to those ideas: 450 joined an existing idea, and 283 formed 242 new ideas with new ids.
6. **Check.** For every idea, an agent read the Lighthouse code and gave a verdict with file and line evidence, and rated the value.
7. **Second checks.** Every `not` or `partial` verdict on a high or medium idea went to a second agent that was told to disprove it: 360 ideas, 75 verdicts changed. Every `implemented` verdict went to a skeptic that was told to find where Lighthouse does not do it: 1,842 ideas, 159 verdicts changed (150 to `partial`).

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
| 1 | Batch gossip unaggregated attestations (fire at 8-16 queued or 10 ms) and group signature sets by signing root | about −1.7 cores on a node that subscribes to all subnets | [#9641](https://github.com/sigp/lighthouse/pull/9641), [#9521](https://github.com/sigp/lighthouse/pull/9521) | attestation_processing-123, -006, -007, bls-012, -017 |
| 2 | glibc `M_MMAP_THRESHOLD`=128 KiB (optionally `M_ARENA_MAX`=4) alongside jemalloc | about −1 to −1.5 GB RSS after 2 weeks of uptime | | allocator_runtime-027, -028 |
| 3 | Hot hdiff buffer cache from 1 to 2 entries; do not clone a buffer the cache rejects | −0.7 s on the epoch-boundary import | | db_hot-020, -039, state_cache-187, -225 |
| 4 | Cold hdiff cache keeps only the live base buffers (interim: `--hdiff-buffer-cache-size 6`) | −3.5 to −4.6 GB on archive nodes (cache model) | | db_cold-049 |
| 5 | Serve post-Fulu next-epoch proposer duties from `beacon_proposer_cache` | `process_epoch` runs per epoch 5.2 → ~1.6 | [#10459](https://github.com/sigp/lighthouse/pull/10459) | beacon_api-004 |
| 6 | Batch-affine pubkey addition for signature sets of 64+ keys | −12 ms per block | | bls-064, block_import-097 |
| 7 | Linear `compute_on_chain_aggregate`, plus a timer | −110 to −130 ms of the 200 ms attestation packing | | op_pool-019, -018 |
| 8 | Release the fork-choice lock before encode + zstd on persist | lock hold 0.5 → 0.1 s | | db_hot-101 |
| 9 | `ssz_types` `hash_vec` hashes u8 lists as whole slices | −3.3 ms per block (measured in a bench) | | tree_hash-072, -032 |
| 10 | On an E+2 shuffling miss, build the committee cache from the unadvanced state | miss cost 0.75 → ~0.1 s | | state_cache-026, attestation_processing-037 |
| 11 | Sparse-then-dense update map for `balances` in milhouse | −12 ms per block | | state_transition-001 |
| 12 | 8-pair block swap in `shuffle_list` | −20 ms per shuffle (measured in a bench) | | epoch_processing-086 |
| 13 | Split the parallel tree hash only where both children are dirty | −10 ms CPU per block | | tree_hash-065 |
| 14 | Hash the transactions once; pass the payload header through `ConsensusContext` | −3.4 to −7.6 ms per block | | tree_hash-028 |
| 15 | Collect the E+1 active indices once for the lookahead and the next committee cache | −48 to −95 ms per epoch boundary | | epoch_processing-091, -088 |
| 16 | Batch the released unknown-block attestations | 4.3× faster drain of the reprocess queue | | attestation_processing-011, -009, -104 |
| 17 | milhouse `HashCell` in place of `RwLock<Hash256>` | −3 to −6 ms CPU per block | [milhouse#98](https://github.com/sigp/milhouse/pull/98) | |
| 18 | Compute the hot state DB ops before the fork-choice write lock | lock hold ~1.5 → 0.1 s at the epoch boundary | | db_hot-037, -004, block_import-136 |
| 19 | IDONTWANT threshold at 200 B, A/B with per-path duplicate metrics | −0.3 to −0.65 MB/s inbound (unverified) | | gossipsub-001, -002, -003 |
| 20 | `Arc<HDiffBuffer>` in the hot and cold caches | −70 ms off the epoch-boundary spike | overlaps [#9236](https://github.com/sigp/lighthouse/pull/9236) | state_cache-225 |
| 21 | Per-committee aggregate pubkeys minus the missing members (as Silver and ethlambda do) | −13 ms per block | | bls-025, -093, attestation_processing-060 |
| 22 | hashtree for 64-byte hashes; a `MerkleHasher` that works on digests | −8 to −9 ms CPU per block | | tree_hash-001, -003, -004, -020 |
| 23 | Batch the KZG verification of gossip columns per block; verify the proposer header signature once per block | 3-4× less column job time in Lodestar (unverified for Lighthouse) | | kzg-010, gossip_validation-066, data_availability-035 |
