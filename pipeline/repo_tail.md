## Limits

- **Triage.** 39,960 items were rejected by both triage passes. The second pass read up to 1,200 characters of the body and the file list, not the diff. Its reason for each item is in `registry.csv`. An item whose performance aspect shows only in the code can still be missing.
- **Verdicts.** They are LLM judgements with file and line evidence, and should be read before acting. A second agent re-read every `implemented` verdict and every high or medium `not` or `partial` verdict. The 1,134 `n/a` verdicts and the low-value `not` and `partial` verdicts had one check only.
- **Matching.** The 450 records that joined an existing idea did not trigger a new check of that idea.
- **Measurements.** The replay covers the state transition only. Networking, DB and op-pool numbers come from fleet metrics plus models or benchmarks.
- **Not covered.** The execution layer, the validator client, the slasher, Gloas-only paths, sync throughput, and changes that no client has made.

## Updating

The steps below add the PRs and commits since the snapshot without renumbering any idea. Set `PERF_DATA` to the pipeline's `data/derived/` directory and `LH_CHECKOUT` to the Lighthouse checkout.

1. **Scrape.** `corpus/corpus.py update` reads new and changed PRs, and new commits, of every client into the SQLite DB (`CL_CORPUS_DB`). Then `corpus/corpus.py export corpus/data` refreshes the JSONL files.
2. **Select.** `pipeline/make_batches.py <dir> 300 --new` writes only the items that `registry.csv` does not have, plus PRs whose state changed (for example OPEN to MERGED).
3. **Triage and extract.** Run `pipeline/workflows/triage-extract.js` on those batches. Then `pipeline/make_registry.py` and `pipeline/make_retriage_in.py`, and `pipeline/workflows/retriage.js` on the batches it prints: the items the first triage rejected get a second read on body and files.
4. **Match.** `pipeline/make_match_in.py`, then `pipeline/workflows/match.js` with its plan. New records join an existing idea or form a new idea with the next free id.
5. **Check.** `pipeline/merge_ideas.py`, then `pipeline/make_check_in.py <tag>`, then `pipeline/workflows/recheck.js` with the args it prints. Run the three again until it prints 0 unchecked and 0 implemented without a skeptic read: the checks of one round produce `implemented` verdicts for the skeptic of the next.
6. **Publish.** `pipeline/merge_ideas.py`, `pipeline/make_registry.py` and `pipeline/make_repo.py` rewrite `ideas.final.jsonl`, `registry.csv`, the README, `areas/`, `ideas.csv` and `ideas.jsonl`. Commit and push.

To check every idea against a newer Lighthouse, check out that commit, set `SHA` and `SHA_DATE` in `pipeline/make_repo.py`, and run step 5 on all ideas. `pipeline/workflows/cluster.js`, `screen.js` and `lh-check.js` are the first run's steps: `cluster.js` clusters from scratch and renumbers, so use it only to start over.

The workflows are [Claude Code](https://docs.claude.com/en/docs/claude-code) workflow scripts: each one fans out subagents over batch files. Pass `root` (the directory that holds `data/derived/`), `lh` (the Lighthouse checkout) and `pipeline` (the `pipeline/` directory) in the workflow args.

