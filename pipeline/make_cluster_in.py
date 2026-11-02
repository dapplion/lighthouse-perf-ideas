#!/usr/bin/env python3
"""Collect is_perf extract records into data/derived/records.jsonl and per-component chunks for clustering."""
import json, glob, os, collections
recs = {}
for f in sorted(glob.glob("data/derived/extract/*.jsonl")):
    for l in open(f):
        if l.strip():
            r = json.loads(l)
            if isinstance(r.get("id"), str):
                recs[r["id"]] = r
perf = [r for r in recs.values() if r.get("is_perf") is True and r.get("idea")]
with open("data/derived/records.jsonl", "w") as f:
    for r in perf:
        f.write(json.dumps(r) + "\n")
by = collections.defaultdict(list)
for r in perf:
    by[r.get("component") or "other"].append(r)
os.makedirs("data/derived/cluster-in", exist_ok=True)
plan = []
for comp, rs in sorted(by.items()):
    rs.sort(key=lambda r: (r.get("mechanism") or "", r["id"]))  # similar mechanisms land in the same chunk
    n = -(-len(rs) // 160)
    size = -(-len(rs) // n)
    files = []
    for k in range(n):
        p = f"data/derived/cluster-in/{comp}-{k}.jsonl"
        with open(p, "w") as f:
            for r in rs[k * size:(k + 1) * size]:
                f.write(json.dumps({x: r.get(x) for x in ("id", "idea", "mechanism", "measured", "landed", "resources")}) + "\n")
        files.append(p)
    plan.append({"component": comp, "files": files, "records": len(rs)})
json.dump(plan, open("data/derived/cluster-in/plan.json", "w"))
print(len(recs), "records,", len(perf), "perf;", sum(len(p["files"]) for p in plan), "chunks over", len(plan), "components")
