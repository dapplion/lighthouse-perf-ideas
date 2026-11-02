#!/usr/bin/env python3
"""Triage input: every PR + every commit not linked to a known PR, as compact lines, split into batch files.
Usage: make_batches.py OUT_DIR [ITEMS_PER_BATCH] [--new]
--new: only items that ../registry.csv does not list, and PRs whose state changed since the registry was written
(for example OPEN -> MERGED). Run it before make_registry.py rewrites the registry."""
import csv, json, os, re, sqlite3, sys

DB = os.environ.get("CL_CORPUS_DB", "/mnt/ssd/cl-corpus/corpus.db")
BOTS = re.compile(r"(bot|dependabot|renovate|mergify|github-actions)", re.I)
NOISE = re.compile(r"^(bump|chore\(deps|build\(deps|update dependency|release v|v\d+\.\d+\.\d+$)", re.I)
REGISTRY = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "registry.csv")


def clean(body):
    body = re.sub(r"<!--.*?-->", " ", body or "", flags=re.S)
    body = re.sub(r"#+ *(Issue Addressed|Proposed Changes|Additional Info|What type of PR is this\?|Description|Motivation)", " ", body, flags=re.I)
    return re.sub(r"\s+", " ", body).strip()[:280]


def main():
    new = "--new" in sys.argv
    args = [a for a in sys.argv[1:] if a != "--new"]
    out, per = args[0], int(args[1]) if len(args) > 1 else 600
    seen = {}
    if new:
        seen = {r["id"]: r for r in csv.DictReader(open(REGISTRY)) if r["stage"] != "new"}
    c = sqlite3.connect(DB)
    items, dropped, skipped = [], 0, 0
    for repo, num, title, body, state, author, labels in c.execute(
            "select repo, number, title, body, state, author, labels from prs order by repo, number"):
        if BOTS.search(author or "") or NOISE.search(title or ""):
            dropped += 1
            continue
        i = f"pr:{repo}#{num}"
        if i in seen and seen[i]["state"] == state:
            skipped += 1
            continue
        lab = ",".join(json.loads(labels or "[]"))[:80]
        items.append(f"{i}\t{state[0]}\t{title}\t[{lab}]\t{clean(body)}")
    for repo, sha, subj, body in c.execute(
            "select m.repo, m.sha, m.subject, m.body from commits m where m.pr_number is null "
            "or not exists (select 1 from prs p where p.repo=m.repo and p.number=m.pr_number) order by m.repo, m.date"):
        if NOISE.search(subj or ""):
            dropped += 1
            continue
        i = f"commit:{repo}@{sha[:12]}"
        if i in seen:
            skipped += 1
            continue
        items.append(f"{i}\tC\t{subj}\t[]\t{clean(body)}")

    os.makedirs(out, exist_ok=True)
    paths = []
    for k in range(0, len(items), per):
        p = os.path.join(out, f"batch-{k // per:03d}.tsv")
        open(p, "w").write("\n".join(items[k:k + per]) + "\n")
        paths.append(p)
    json.dump(paths, open(os.path.join(out, "index.json"), "w"))
    print(f"{len(items)} items in {len(paths)} batches, dropped {dropped} bot/noise, skipped {skipped} already done")


if __name__ == "__main__":
    main()
