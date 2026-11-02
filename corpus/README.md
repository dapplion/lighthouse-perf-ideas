# cl-corpus

Every PR and every commit of the Ethereum consensus clients, in one SQLite database with full-text search.
It is a general corpus. Use it for any sweep across the history of the clients: perf ideas, security fixes, spec changes, regressions.

## Layout

| Path | What |
|---|---|
| `corpus.py` | The only tool: `update`, `stats`, `search`, `export` |
| `repos.json` | The repos in the corpus. Edit this to add a client |
| `git/<name>.git` | Blobless bare mirrors (commits and trees, no file contents), one branch each. Not in git: `update` clones them |
| `data/<name>.prs.jsonl`, `data/<name>.commits.jsonl` | The snapshot of the DB that is in git, written by `export data` |
| `/mnt/ssd/cl-corpus/corpus.db` | The database. Override the path with `CL_CORPUS_DB` |

## Repos

lighthouse, prysm, teku, nimbus, lodestar, grandine, silver (gattaca), ethlambda (lambdaclass, lean consensus), caplin (erigon, `cl/` only).

For caplin, the corpus has only the commits that touch `cl/` and the PRs that those commits reference. Other erigon PRs are about the EL.

## Update

```
./corpus.py update              # all repos
./corpus.py update prysm teku   # some repos
./corpus.py stats
```

The update is incremental. You can run it at any time, and you can run it again if it stops.

- **PRs**: the tool reads the PRs in order of `updatedAt`, newest first. It stops when it gets to a PR older than the watermark of the last run, minus 2 hours. Thus it also gets old PRs that changed: merged, closed, edited, relabelled. A row is replaced by its newest version. If a run stops, it continues from its saved cursor. It moves the watermark only when the run is complete.
- **Commits**: the tool fetches the branch and reads `last_head..new_head`. If the branch history was rewritten, it reads all of it again, and the primary key removes the duplicates. Only the configured branch is in the corpus, and merge commits are not. The tool uses `--no-renames`: rename detection on a blobless mirror downloads blobs one by one.
- At the end, the tool rebuilds the full-text indexes.

The first full run takes approximately 1 to 2 hours, because of the GitHub GraphQL rate limit (5000 points per hour, shared with all other `gh` use on this machine). The tool waits when the remaining limit goes below 200.

## Schema

- `prs(repo, number, title, body, state, author, labels[json], created_at, updated_at, merged_at, closed_at, url, additions, deletions, changed_files, base_ref, head_ref, fetched_at)`
- `commits(repo, sha, date, author, subject, body, files[json], pr_number)`. `pr_number` comes from `(#123)` in the subject, so it is empty for most direct pushes.
- `prs_fts(title, body)` and `commits_fts(subject, body)` are FTS5 indexes. Join on `rowid`.
- `prs_landed`: a view of the PRs whose code is on the branch. `state = 'MERGED'` is not enough: Lighthouse merged through bors for years, which closes the PR and pushes the commit (1552 Lighthouse PRs are `CLOSED` but landed). Grandine does not put `(#N)` in commit subjects, so the commit link misses most of its PRs; its `merged_at` is correct.
- `meta(repo, key, value)`: `pr_watermark`, `commits_head`, `last_update`, and the resume cursor of a run that did not complete.

## Query

```
./corpus.py search 'cache NEAR alloc' --repo prysm --kind pr
./corpus.py search '"use after free" OR overflow OR panic OR dos' --limit 100
sqlite3 /mnt/ssd/cl-corpus/corpus.db "select repo, count(*) from prs where merged_at is not null group by repo"
./corpus.py export data         # JSONL snapshots, one file per repo and table
```

For the FTS5 query syntax, see https://sqlite.org/fts5.html#full_text_query_syntax.

## Add a repo

Add an entry to `repos.json`: `name`, `gh` (owner/repo), `branch`. Optional: `paths` (limits the commits to these paths) and `"prs": "from-commits"` (gets only the PRs that the in-scope commits reference, for monorepos). Then run `./corpus.py update <name>`.

## Not in the corpus

PR review comments, issue threads, and the file list of each PR. You can add them to the PR GraphQL query in `corpus.py` if a sweep needs them. The file list of a merged PR is already in `commits.files` for squash-merge repos.
