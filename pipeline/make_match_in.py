#!/usr/bin/env python3
"""Inputs for match.js: perf records that are in no idea yet, per component, plus the existing ideas of that component.
Usage: PERF_DATA=.../data/derived make_match_in.py   (writes PERF_DATA/match-in/, prints the plan for match.js args)"""
import collections, glob, json, os

D = os.environ["PERF_DATA"]
placed = {m for f in glob.glob(f"{D}/ideas/*.jsonl") for l in open(f) if l.strip() for m in json.loads(l)["members"]}
placed |= {json.loads(l)["id"] for f in glob.glob(f"{D}/match-out/*.jsonl") if not f.endswith(".new.jsonl") for l in open(f) if l.strip()}
recs = {}
for f in sorted(glob.glob(f"{D}/extract/*.jsonl")):
    for l in open(f):
        if l.strip():
            r = json.loads(l)
            if isinstance(r.get("id"), str) and r.get("is_perf") is True and r.get("idea") and r["id"] not in placed:
                recs[r["id"]] = r
by = collections.defaultdict(list)
for r in recs.values():
    by[r.get("component") or "other"].append(r)

# existing ideas per component, by cid prefix (ideas/zz_lost.jsonl holds the beacon_api-L ideas)
existing = collections.defaultdict(list)
for f in sorted(glob.glob(f"{D}/ideas/*.jsonl")) + sorted(glob.glob(f"{D}/match-out/*.new.jsonl")):
    for l in open(f):
        if l.strip():
            i = json.loads(l)
            existing[i["cid"].rsplit("-", 1)[0]].append(i)

os.makedirs(f"{D}/match-in", exist_ok=True)
plan = []
for comp, rs in sorted(by.items()):
    rs.sort(key=lambda r: (r.get("mechanism") or "", r["id"]))
    with open(f"{D}/match-in/{comp}.ideas.jsonl", "w") as f:
        for i in existing[comp]:
            f.write(json.dumps({k: i.get(k) for k in ("cid", "title", "idea", "mechanism")}) + "\n")
    files = []
    for k in range(0, len(rs), 120):
        p = f"{D}/match-in/{comp}-{k // 120}.jsonl"
        with open(p, "w") as f:
            for r in rs[k:k + 120]:
                f.write(json.dumps({x: r.get(x) for x in ("id", "idea", "mechanism", "measured", "landed", "resources")}) + "\n")
        files.append(p)
    plan.append({"component": comp, "records": len(rs), "files": files})
json.dump(plan, open(f"{D}/match-in/plan.json", "w"), indent=1)
print(len(recs), "records in", sum(len(p["files"]) for p in plan), "chunks over", len(plan), "components")
