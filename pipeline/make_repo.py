#!/usr/bin/env python3
"""Build README.md, areas/*.md, ideas.csv and ideas.jsonl from PERF_DATA/ideas.final.jsonl and the corpus DB.
Usage: make_repo.py   (the hand-written parts are repo_head.md and repo_tail.md next to this file)
GitHub stops rendering a Markdown file at about 512 KB, so the ideas go in one file per area."""
import collections, csv, html, json, os, re, sqlite3

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.environ["PERF_DATA"]  # the pipeline output directory (data/derived)
DB = os.environ.get("CL_CORPUS_DB", "/mnt/ssd/cl-corpus/corpus.db")
# The Lighthouse checkout the ideas were checked against. A new check run changes both.
SHA = "928b61e719c39f7fe8c074767b594fb99f4379bd"
SHA_DATE = "2026-10-30"
LH = os.environ["LH_CHECKOUT"].rstrip("/") + "/"  # the Lighthouse checkout the check ran in
out = os.path.dirname(HERE)
REPOS = json.load(open(os.path.join(out, "corpus", "repos.json")))
GH = {r["name"]: r["gh"] for r in REPOS}
os.makedirs(os.path.join(out, "areas"), exist_ok=True)

ideas = [json.loads(l) for l in open(os.path.join(DATA, "ideas.final.jsonl"))]
for i in ideas:
    i["verdict"] = i.get("verdict") or "unchecked"
    i["value"] = i.get("value") or "unrated"
VERDICTS = ["not", "partial", "implemented", "n/a", "unchecked"]
VALUES = ["high", "medium", "low", "unrated"]


def measured(i):
    m = i.get("measured_best")
    if isinstance(m, dict):
        return f"{m.get('gain')} ({m.get('id')})"
    return m


def area(i):
    return i["cid"].rsplit("-", 1)[0]


def actionable(i):
    return i["value"] in ("high", "medium") and i["verdict"] in ("not", "partial")


def src_url(m):
    kind, ref = m.split(":", 1)
    if kind == "pr":
        repo, n = ref.split("#")
        return f"{repo}#{n}", f"https://github.com/{GH[repo]}/pull/{n}"
    repo, sha = ref.split("@")
    return f"{repo}@{sha[:9]}", f"https://github.com/{GH[repo]}/commit/{sha}"


def lh_link(path, lines):
    url = f"https://github.com/sigp/lighthouse/blob/{SHA}/{path}"
    if lines:
        a, _, b = lines.partition("-")
        url += f"#L{a}" + (f"-L{b}" if b else "")
    return f"[`{path}{':' + lines if lines else ''}`]({url})"


def plain(s):
    """Path cleanup for the CSV and JSONL."""
    s = s.replace(LH, "")
    s = re.sub(r"/root/\.cargo/(?:registry/src|git/checkouts)/[^/]+/", "", s)
    return s


def md(s):
    """Escape HTML outside backtick spans, so `Vec<u8>` survives and raw <T> does not vanish."""
    parts = re.split(r"(`[^`]*`)", s or "")
    return "".join(p if p.startswith("`") else html.escape(p, quote=False).replace("|", "\\|") for p in parts)


def md_evidence(e):
    """Link every path that exists in the pinned checkout; anything else stays as text."""
    e = re.sub(r"/root/\.cargo/(?:registry/src|git/checkouts)/[^/]+/", "", e.replace(LH, ""))
    res, pos = [], 0
    for m in re.finditer(r"(?<![\w/.])([\w.-]+(?:/[\w.-]+)+)(?::(\d+(?:-\d+)?))?", e):
        path = m.group(1).rstrip(".")
        if not os.path.exists(LH + path):
            continue
        res += [md(e[pos:m.start()]), lh_link(path, m.group(2))]
        pos = m.end()
    return "".join(res) + md(e[pos:])


def sources(i, limit=None):
    ms = i.get("members") or []
    links = [f"[{t}]({u})" for t, u in map(src_url, ms[:limit] if limit else ms)]
    if limit and len(ms) > limit:
        links.append(f"+{len(ms) - limit} more")
    return ", ".join(links)


by_area = collections.defaultdict(list)
for i in ideas:
    by_area[area(i)].append(i)
areas = sorted(by_area, key=lambda a: (-sum(map(actionable, by_area[a])), a))
rank = {v: n for n, v in enumerate(VALUES)}
vrank = {v: n for n, v in enumerate(VERDICTS)}

def detail(i):
    tags = " · ".join(x for x in [i["verdict"], i["value"], i.get("effort") or "", ", ".join(i.get("resources") or [])] if x)
    B = [f'<a id="{i["cid"]}"></a>', "<details>",
         f"<summary><b>{i['cid']}</b> {html.escape(i['title'])} — <i>{html.escape(tags)}</i></summary>", "",
         f"**Idea.** {md(i['idea'])}"]
    if i.get("gap"):
        B += ["", f"**Gap in Lighthouse.** {md(i['gap'])}"]
    if i.get("impact"):
        B += ["", f"**Impact.** {md(i['impact'])}"]
    if measured(i):
        B += ["", f"**Best measured result.** {md(measured(i))}"]
    if i.get("evidence"):
        B += ["", "**Evidence (Lighthouse @ " + SHA[:10] + ").**", ""] + [f"- {md_evidence(e)}" for e in i["evidence"]]
    for key, label in (("refute_note", "Second check"), ("skeptic_note", "Skeptic check")):
        if i.get(key):
            B += ["", f"**{label}.** {md(i[key])}"]
    if len(i.get("history") or []) > 1:
        B += ["", "**Verdict history.** " + " → ".join(f"{h['verdict']} ({h['stage']})" for h in i["history"])]
    return B + ["", f"**Sources.** {sources(i)}", "", "</details>", ""]


def id_key(i):
    n = i["cid"].rsplit("-", 1)[1]
    return (n.startswith("L"), int(n.lstrip("L")))


# GitHub stops rendering a Markdown file at about 512 KB: an area with more text continues on a second page.
LIMIT = 380_000
page = {}
for a in areas:
    g = sorted(by_area[a], key=id_key)
    pages, size = [[]], 0
    for i in g:
        text = "\n".join(detail(i)) + "\n"
        if pages[-1] and size + len(text) > LIMIT:
            pages.append([])
            size = 0
        pages[-1].append((i, text))
        size += len(text)
    names = [f"{a}.md"] + [f"{a}-{k + 1}.md" for k in range(1, len(pages))]
    for name, pg in zip(names, pages):
        for i, _ in pg:
            page[i["cid"]] = name
    c = collections.Counter(i["verdict"] for i in g)
    summary = ", ".join(f"{c[v]} {v}" for v in VERDICTS if c[v])
    for k, (name, pg) in enumerate(zip(names, pages)):
        A = [f"# {a}" + (f" (part {k + 1} of {len(pages)})" if len(pages) > 1 else ""), "",
             f"{len(g)} ideas: {summary}; {sum(map(actionable, g))} actionable (high or medium value, verdict `not` or `partial`). "
             "[Back to the summary](../README.md).", ""]
        top = max(int(i["cid"].rsplit("-", 1)[1]) for i in g if not i["cid"].rsplit("-", 1)[1].startswith("L"))
        listed = sum(1 for i in g if not i["cid"].rsplit("-", 1)[1].startswith("L"))
        if listed < top:
            A += [f"The area has {top} numbered ideas; the {top - listed} ids missing here have not been checked against Lighthouse yet.", ""]
        if len(pages) > 1:
            A += ["Pages: " + " · ".join(f"[part {n + 1}]({nm})" for n, nm in enumerate(names)), ""]
        if k == 0:
            A += ["| id | idea | verdict | value | effort | resources |", "|---|---|---|---|---|---|"]
            for i in g:
                star = " **★**" if actionable(i) else ""
                A.append(f"| [{i['cid']}]({'' if page[i['cid']] == name else page[i['cid']]}#{i['cid']}){star} | {md(i['title'])} | {i['verdict']} "
                         f"| {i['value']} | {i.get('effort') or ''} | {', '.join(i.get('resources') or [])} |")
            A += ["", "★ actionable. Click an id for the full record.", "", "## Ideas", ""]
        A += [t for _, t in pg]
        open(os.path.join(out, "areas", name), "w").write("\n".join(A) + "\n")

head = open(os.path.join(HERE, "repo_head.md")).read().rstrip()
head = re.sub(r"\b([a-z_]+-L?\d{3})\b", lambda m: f"[{m.group(1)}](areas/{page[m.group(1)]}#{m.group(1)})" if m.group(1) in page else m.group(1), head)
db = sqlite3.connect(DB)
meta = {(r, k): v for r, k, v in db.execute("select repo, key, value from meta")}
L = [head, "", "## Data snapshot", "",
     f"The ideas were checked against Lighthouse `unstable` at [`{SHA[:10]}`](https://github.com/sigp/lighthouse/commit/{SHA}) ({SHA_DATE}).", "",
     "The corpus holds every PR and every commit on the main branch of each client, up to:", "",
     "| client | repo | branch | newest PR | PRs | latest commit | commits | scraped |", "|---|---|---|---|---|---|---|---|"]
for r in REPOS:
    n = r["name"]
    npr, nprs = db.execute("select max(number), count(*) from prs where repo=?", (n,)).fetchone()
    head_sha = meta.get((n, "commits_head"), "")
    date, ncommits = db.execute("select max(date), count(*) from commits where repo=?", (n,)).fetchone()
    L.append(f"| {n} | [{r['gh']}](https://github.com/{r['gh']}) | `{r['branch']}`{' (`' + ', '.join(r['paths']) + '/` only)' if r.get('paths') else ''} "
             f"| [#{npr}](https://github.com/{r['gh']}/pull/{npr}) | {nprs:,} "
             f"| [`{head_sha[:10]}`](https://github.com/{r['gh']}/commit/{head_sha}) ({(date or '')[:10]}) | {ncommits:,} | {meta.get((n, 'last_update'), '')[:10]} |")
L += ["", "The full registry is in `corpus/data/` (every PR and commit as JSONL) and `registry.csv` (how far each item got in the pipeline, and its idea id).", ""]
L += ["## Totals", "", "Verdict by value:", "", "| verdict | high | medium | low | unrated | total |", "|---|---|---|---|---|---|"]
for v in VERDICTS:
    row = [sum(1 for i in ideas if i["verdict"] == v and i["value"] == x) for x in VALUES]
    L.append(f"| {v} | " + " | ".join(map(str, row)) + f" | {sum(row)} |")
L.append("| **total** | " + " | ".join(str(sum(1 for i in ideas if i["value"] == x)) for x in VALUES) + f" | {len(ideas)} |")
L += ["", "By area, sorted by actionable count. The area is the prefix of the idea id.", "",
      "| area | ideas | actionable | not | partial | implemented | n/a | unchecked |", "|---|---|---|---|---|---|---|---|"]
for a in areas:
    g = by_area[a]
    c = collections.Counter(i["verdict"] for i in g)
    L.append(f"| [{a}](areas/{a}.md) | {len(g)} | {sum(map(actionable, g))} | " + " | ".join(str(c[v]) for v in VERDICTS) + " |")
L += ["", "Ideas by the client whose PRs or commits produced them (an idea can come from several clients):", "",
      "| client | ideas | actionable |", "|---|---|---|"]
cc = collections.Counter(c for i in ideas for c in set(i.get("clients") or []))
ca = collections.Counter(c for i in ideas if actionable(i) for c in set(i.get("clients") or []))
for c, n in cc.most_common():
    L.append(f"| {c} | {n} | {ca[c]} |")
L += ["", open(os.path.join(HERE, "repo_tail.md")).read().rstrip()]
open(os.path.join(out, "README.md"), "w").write("\n".join(L) + "\n")

with open(os.path.join(out, "ideas.csv"), "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["id", "area", "verdict", "value", "effort", "actionable", "resources", "clients", "title", "gap", "sources"])
    for i in sorted(ideas, key=lambda i: (not actionable(i), rank[i["value"]], vrank[i["verdict"]], i["cid"])):
        gap = plain(i.get("gap") or "")
        w.writerow([i["cid"], area(i), i["verdict"], i["value"], i.get("effort") or "", "yes" if actionable(i) else "",
                    " ".join(i.get("resources") or []), " ".join(sorted(set(i.get("clients") or []))), i["title"],
                    gap if len(gap) <= 220 else gap[:217] + "...", " ".join(src_url(m)[0] for m in i.get("members") or [])])

KEEP = ["cid", "title", "idea", "verdict", "first_verdict", "value", "effort", "confidence", "resources", "clients",
        "members", "lighthouse_members", "landed_somewhere", "measured_best", "evidence", "gap", "impact", "refute_note"]
with open(os.path.join(out, "ideas.jsonl"), "w") as f:
    for i in ideas:
        r = {k: i.get(k) for k in KEEP}
        r["measured_best"] = measured(i)
        r["evidence"] = [plain(e) for e in r["evidence"] or []]
        r["gap"] = plain(r["gap"] or "")
        r["sources"] = [src_url(m)[1] for m in i.get("members") or []]
        f.write(json.dumps(r, ensure_ascii=False) + "\n")

for d in (out, os.path.join(out, "areas")):
    for n in sorted(os.listdir(d)):
        if os.path.isfile(os.path.join(d, n)):
            print(os.path.join(d, n), os.path.getsize(os.path.join(d, n)))
