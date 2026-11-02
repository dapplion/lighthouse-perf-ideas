#!/usr/bin/env python3
"""Write registry.csv: every corpus item, how far it got in the pipeline, and its idea id.
Usage: make_registry.py   (reads the corpus DB and PERF_DATA, writes ../registry.csv)

stage values:
  folded     commit of a known PR; the PR stands for it
  dropped    bot author or dependency/release noise (make_batches.py filters)
  rejected   the triage agent did not pass it on
  not_perf   the extract agent read it and found no perf idea
  perf       a perf record; cid is the idea it was clustered into
  new        in the corpus but not yet through the pipeline (scraped after the last run)
make_batches.py --new uses this file to send only new items, and PRs whose state changed, to the next run."""
import csv, glob, json, os, sqlite3
from make_batches import BOTS, NOISE

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.environ["PERF_DATA"]  # the pipeline output directory (data/derived)
DB = os.environ.get("CL_CORPUS_DB", "/mnt/ssd/cl-corpus/corpus.db")

triaged = {l.split("\t", 1)[0] for f in glob.glob(f"{DATA}/triage-in/*.tsv") for l in open(f) if l.strip()}
extracted = {}
for f in glob.glob(f"{DATA}/extract/*.jsonl"):
    for l in open(f):
        if l.strip():
            r = json.loads(l)
            if isinstance(r.get("id"), str):
                extracted[r["id"]] = bool(r.get("is_perf") and r.get("idea"))
cid = {m: i["cid"] for l in open(f"{DATA}/ideas.final.jsonl") for i in [json.loads(l)] for m in i["members"]}


def stage(item, noisy):
    if item in extracted:
        return "perf" if extracted[item] else "not_perf"
    if item in triaged:
        return "rejected"
    return "dropped" if noisy else "new"


c = sqlite3.connect(DB)
rows = []
for repo, num, title, state, author, updated in c.execute(
        "select repo, number, title, state, author, updated_at from prs order by repo, number"):
    i = f"pr:{repo}#{num}"
    rows.append([i, repo, "pr", state, updated, stage(i, bool(BOTS.search(author or "") or NOISE.search(title or ""))), cid.get(i, ""), title])
for repo, sha, subj, date, linked in c.execute(
        "select m.repo, m.sha, m.subject, m.date, exists (select 1 from prs p where p.repo=m.repo and p.number=m.pr_number) "
        "from commits m order by m.repo, m.date"):
    i = f"commit:{repo}@{sha[:12]}"
    rows.append([i, repo, "commit", "", date, "folded" if linked else stage(i, bool(NOISE.search(subj or ""))), cid.get(i, ""), subj])

with open(os.path.join(os.path.dirname(HERE), "registry.csv"), "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["id", "repo", "kind", "state", "updated", "stage", "cid", "title"])
    w.writerows(rows)
counts = {}
for r in rows:
    counts[r[5]] = counts.get(r[5], 0) + 1
print(len(rows), counts)
