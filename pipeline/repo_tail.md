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

