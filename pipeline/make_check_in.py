#!/usr/bin/env python3
"""Inputs for recheck.js, from PERF_DATA/ideas.final.jsonl (run merge_ideas.py first).
Usage: PERF_DATA=.../data/derived make_check_in.py TAG
Writes check<TAG>-in/uNNN.jsonl (ideas with no verdict) and impl<TAG>-in/iNNN.jsonl (implemented verdicts that no
skeptic has read), 8 ideas per file, and prints the recheck.js args."""
import json, os, sys

D = os.environ["PERF_DATA"]
tag = sys.argv[1]
ideas = [json.loads(l) for l in open(f"{D}/ideas.final.jsonl")]
F = ["cid", "title", "idea", "members", "lighthouse_members", "measured_best"]


def write(rows, d, prefix, extra):
    os.makedirs(f"{D}/{d}", exist_ok=True)
    for k in range(0, len(rows), 8):
        with open(f"{D}/{d}/{prefix}{k // 8:03d}.jsonl", "w") as f:
            for x in rows[k:k + 8]:
                f.write(json.dumps({**{a: x.get(a) for a in F}, **extra(x)}) + "\n")
    return -(-len(rows) // 8)


unchecked = [x for x in ideas if not x.get("history")]
impl = [x for x in ideas if x.get("verdict") == "implemented" and not any(h["stage"] == "skeptic" for h in x["history"])]
check_n = write(unchecked, f"check{tag}-in", "u",
                lambda x: {"prescreen": f"{x.get('applicable')}: {x.get('screen_reason')}" if x.get("screen_reason") else "none"})
impl_n = write(impl, f"impl{tag}-in", "i", lambda x: {a: x.get(a) for a in ("value", "evidence", "gap", "impact")})
print(f"{len(unchecked)} unchecked, {len(impl)} implemented without a skeptic read")
print(json.dumps({"tag": tag, "check_n": check_n, "impl_tag": tag, "impl_n": impl_n}))
