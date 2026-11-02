#!/usr/bin/env python3
"""Print full corpus records. Usage: show.py [--diff] ID [ID ...]   IDs: pr:<repo>#<n> or commit:<repo>@<sha-prefix>"""
import json, os, re, sqlite3, subprocess, sys
c = sqlite3.connect(os.environ.get("CL_CORPUS_DB", "/mnt/ssd/cl-corpus/corpus.db"))
GIT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "corpus", "git")
diff = "--diff" in sys.argv
for i in [a for a in sys.argv[1:] if a != "--diff"]:
    print("=" * 100, "\n" + i)
    m = re.match(r"pr:(\w+)#(\d+)$", i) or re.match(r"commit:(\w+)@([0-9a-f]+)$", i)
    if not m:
        print("bad id"); continue
    repo, key = m.groups()
    if i.startswith("pr:"):
        r = c.execute("select state, merged_at, title, labels, additions, deletions, changed_files, url, body from prs where repo=? and number=?", (repo, int(key))).fetchone()
        if not r: print("not found"); continue
        print(f"state={r[0]} merged={r[1]} +{r[4]}/-{r[5]} files={r[6]} {r[7]}\nlabels={r[3]}\nTITLE: {r[2]}\n{(r[8] or '')[:6000]}")
        rows = c.execute("select sha, subject, files from commits where repo=? and pr_number=?", (repo, int(key))).fetchall()
    else:
        rows = c.execute("select sha, subject, files, body from commits where repo=? and sha like ?", (repo, key + "%")).fetchall()
        for r in rows: print(f"BODY: {r[3][:4000]}")
    for r in rows:
        files = json.loads(r[2])
        print(f"commit {r[0][:12]} {r[1]}\n  files ({len(files)}): {', '.join(files[:40])}")
        if diff:
            out = subprocess.run(["git", "-C", f"{GIT}/{repo}.git", "show", "--no-renames", "--format=", "--stat", "-p", r[0]],
                                 capture_output=True, text=True, errors="replace").stdout
            print(out[:15000] + ("\n[diff truncated]" if len(out) > 15000 else ""))
