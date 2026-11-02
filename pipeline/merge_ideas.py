#!/usr/bin/env python3
"""Merge the ideas and every verdict pass into PERF_DATA/ideas.final.jsonl.
Usage: PERF_DATA=.../data/derived merge_ideas.py

Inputs (all under PERF_DATA), applied in this order, a later pass overriding an earlier one:
  ideas/*.jsonl          the clustered ideas
  match-out/             new ideas and new members from match.js
  screen-out/*.jsonl     prescreen: applicable, value guess from the title
  check-out/, check2-out/, check3-out/  first check against Lighthouse (lh-check.js, recheck.js)
  refute-out/, refute2-out/, refute3-out/  second agent trying to disprove not/partial
  impl-out/              skeptic trying to disprove implemented (recheck.js)
Each row keeps `history`: the verdict of every pass that judged it, in order."""
import collections, glob, json, os

D = os.environ["PERF_DATA"]


def rows(pattern):
    out, bad = {}, 0
    for f in sorted(glob.glob(f"{D}/{pattern}")):
        for l in open(f):
            if l.strip():
                try:
                    x = json.loads(l)
                    out[x["cid"]] = x
                except (json.JSONDecodeError, KeyError, TypeError):
                    bad += 1
    if bad:
        print(f"{pattern}: {bad} bad lines")
    return out


ideas = rows("ideas/*.jsonl")
# match.js output: new ideas, and new members for existing ideas
for cid, i in rows("match-out/*.new.jsonl").items():
    ideas.setdefault(cid, i)
for f in sorted(glob.glob(f"{D}/match-out/*.jsonl")):
    if f.endswith(".new.jsonl"):
        continue
    for l in open(f):
        if l.strip():
            m = json.loads(l)
            i = ideas.get(m.get("cid"))
            if i is not None and m["id"] not in i["members"]:
                i["members"] = i["members"] + [m["id"]]
                repo = m["id"].split(":", 1)[1].split("#")[0].split("@")[0]
                i["clients"] = sorted(set(i.get("clients") or []) | {repo})
                if repo == "lighthouse":
                    i["lighthouse_members"] = (i.get("lighthouse_members") or []) + [m["id"]]
screen = rows("screen-out/*.jsonl")
check = {**rows("check-out/*.jsonl"), **rows("check2-out/*.jsonl"), **rows("check3-out/*.jsonl")}
refute = {**rows("refute-out/*.jsonl"), **rows("refute2-out/*.jsonl"), **rows("refute3-out/*.jsonl")}
skeptic = rows("impl-out/*.jsonl")
VALUES = ("high", "medium", "low")

out = []
for cid, i in ideas.items():
    s = screen.get(cid, {})
    row = {"cid": cid, "title": i["title"], "idea": i["idea"], "resources": i.get("resources"),
           "clients": sorted(set(i.get("clients") or [])), "members": i["members"],
           "lighthouse_members": i.get("lighthouse_members") or [], "measured_best": i.get("measured_best"),
           "landed_somewhere": i.get("landed_somewhere"), "applicable": s.get("applicable"),
           "value": s.get("value") if s.get("value") in VALUES else None, "screen_reason": s.get("reason"),
           "stage": "unchecked", "history": []}

    def apply(x, stage, verdict_key, note_key):
        row["history"].append({"stage": stage, "verdict": x.get(verdict_key)})
        keep = (lambda k: x.get(k)) if stage == "checked" else (lambda k: x.get(k) or row.get(k))
        row.update(verdict=x.get(verdict_key), stage=stage, evidence=keep("evidence"), gap=x.get("gap"),
                   effort=keep("effort"), impact=keep("impact"), confidence=x.get("confidence"))
        if x.get("value") in VALUES:
            row["value"] = x["value"]
        if note_key and x.get("note"):
            row[note_key] = x["note"]

    if cid in check:
        apply(check[cid], "checked", "verdict", None)
    if cid in refute:
        apply(refute[cid], "refuted", "final_verdict", "refute_note")
    if cid in skeptic:
        apply(skeptic[cid], "skeptic", "final_verdict", "skeptic_note")
    row["first_verdict"] = row["history"][0]["verdict"] if row["history"] else None
    out.append(row)

with open(f"{D}/ideas.final.jsonl", "w") as f:
    for r in out:
        f.write(json.dumps(r) + "\n")
print(len(out), "ideas;", collections.Counter((r["stage"], r.get("verdict")) for r in out).most_common())
act = [r for r in out if r.get("verdict") in ("not", "partial") and r.get("value") in ("high", "medium")]
print("actionable:", len(act))
