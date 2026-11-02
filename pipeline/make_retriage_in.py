#!/usr/bin/env python3
"""Inputs for retriage.js: every item that the first triage rejected and no second triage has read yet.
Usage: PERF_DATA=.../data/derived make_retriage_in.py   (reads ../registry.csv and the corpus DB, writes PERF_DATA/retriage-in/)
Each line: id, state, title, [labels], files: up to 15 changed files, body: up to 1,200 characters."""
import csv, json, os, re, sqlite3

D = os.environ["PERF_DATA"]
DB = os.environ.get("CL_CORPUS_DB", "/mnt/ssd/cl-corpus/corpus.db")
REGISTRY = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "registry.csv")
todo = [r["id"] for r in csv.DictReader(open(REGISTRY)) if r["stage"] == "rejected" and not r["retriage"]]


def clean(b):
    b = re.sub(r"<!--.*?-->", " ", b or "", flags=re.S)
    return re.sub(r"\s+", " ", b).strip()[:1200]


def files_text(files):
    return " ".join(files[:15]) + (f" +{len(files) - 15}" if len(files) > 15 else "")


c = sqlite3.connect(DB)
pr_files = {}
for repo, n, files in c.execute("select repo, pr_number, files from commits where pr_number is not null"):
    pr_files.setdefault((repo, n), []).extend(json.loads(files or "[]"))
lines = []
for i in todo:
    if i.startswith("pr:"):
        repo, n = i[3:].split("#")
        t, b, s, l = c.execute("select title, body, state, labels from prs where repo=? and number=?", (repo, int(n))).fetchone()
        lines.append(f"{i}\t{s[0]}\t{t}\t[{','.join(json.loads(l or '[]'))[:80]}]\tfiles: {files_text(pr_files.get((repo, int(n)), []))}\tbody: {clean(b)}")
    else:
        repo, sha = i[7:].split("@")
        sj, b, f = c.execute("select subject, body, files from commits where repo=? and sha like ?", (repo, sha + "%")).fetchone()
        lines.append(f"{i}\tC\t{sj}\t[]\tfiles: {files_text(json.loads(f or '[]'))}\tbody: {clean(b)}")

os.makedirs(f"{D}/retriage-in", exist_ok=True)
start = len([f for f in os.listdir(f"{D}/retriage-in") if f.endswith(".tsv")])
for k in range(0, len(lines), 150):
    open(f"{D}/retriage-in/r{start + k // 150:03d}.tsv", "w").write("\n".join(lines[k:k + 150]) + "\n")
print(f"{len(lines)} items in {-(-len(lines) // 150)} batches, numbered from r{start:03d}; pass idx to retriage.js")
