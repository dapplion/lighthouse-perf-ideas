#!/usr/bin/env python3
"""Consensus-client PR + commit corpus. See README.md.

  corpus.py update [repo ...]     fetch new/changed PRs and new commits (all repos if none given)
  corpus.py stats                 row counts and watermarks per repo
  corpus.py search 'fts query' [--repo R] [--kind pr|commit] [--limit N]
  corpus.py export DIR            write <repo>.prs.jsonl / <repo>.commits.jsonl snapshots
"""
import argparse, json, os, re, sqlite3, subprocess, sys, time
from datetime import datetime, timedelta, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
DB = os.environ.get("CL_CORPUS_DB", "/mnt/ssd/cl-corpus/corpus.db")
GIT_DIR = os.path.join(HERE, "git")
REPOS = json.load(open(os.path.join(HERE, "repos.json")))
OVERLAP = timedelta(hours=2)  # re-scan this far behind the watermark to tolerate clock skew / slow indexing

SCHEMA = """
create table if not exists prs(
  repo text, number int, title text, body text, state text, author text, labels text,
  created_at text, updated_at text, merged_at text, closed_at text, url text,
  additions int, deletions int, changed_files int, base_ref text, head_ref text,
  fetched_at text, primary key(repo, number));
create table if not exists commits(
  repo text, sha text, date text, author text, subject text, body text, files text, pr_number int,
  primary key(repo, sha));
create table if not exists meta(repo text, key text, value text, primary key(repo, key));
create index if not exists commits_pr on commits(repo, pr_number);
create view if not exists prs_landed as select * from prs p where merged_at is not null
  or exists (select 1 from commits m where m.repo = p.repo and m.pr_number = p.number);
create virtual table if not exists prs_fts using fts5(title, body, content='prs', content_rowid='rowid');
create virtual table if not exists commits_fts using fts5(subject, body, content='commits', content_rowid='rowid');
"""

PR_FIELDS = """number title body state createdAt updatedAt mergedAt closedAt url additions deletions changedFiles
  baseRefName headRefName author{login} labels(first:30){nodes{name}}"""

def db():
    os.makedirs(os.path.dirname(DB), exist_ok=True)
    c = sqlite3.connect(DB)
    c.executescript(SCHEMA)
    return c

def meta_get(c, repo, key):
    r = c.execute("select value from meta where repo=? and key=?", (repo, key)).fetchone()
    return r[0] if r else None

def meta_set(c, repo, key, value):
    if value is None:
        c.execute("delete from meta where repo=? and key=?", (repo, key))
    else:
        c.execute("insert or replace into meta values(?,?,?)", (repo, key, value))
    c.commit()

def gql(query, allow_partial=False, **vars):
    args = ["gh", "api", "graphql", "-f", f"query={query}"]
    for k, v in vars.items():
        if v is not None:
            args += ["-F", f"{k}={v}"]
    for attempt in range(10):
        p = subprocess.run(args, capture_output=True, text=True)
        try:
            d = json.loads(p.stdout)  # gh exits non-zero on partial errors too, but still prints the body
        except ValueError:
            d = {}
        errors = d.get("errors") or []
        # allow_partial: "#N" in a commit subject may be an issue, which GraphQL reports as NOT_FOUND
        if d.get("data") and (not errors or allow_partial and all(e.get("type") == "NOT_FOUND" for e in errors)):
            rl = d["data"].get("rateLimit")
            if rl and rl["remaining"] < 200:
                reset = datetime.fromisoformat(rl["resetAt"].replace("Z", "+00:00"))
                wait = max(30, (reset - datetime.now(timezone.utc)).total_seconds() + 10)
                log(f"rate limit low ({rl['remaining']}), sleeping {wait:.0f}s")
                time.sleep(wait)
            return d["data"]
        time.sleep(min(120, 5 * 2 ** attempt))
    raise RuntimeError(f"graphql failed: {p.stderr[:300]} {p.stdout[:300]}")

def log(msg):
    print(f"{datetime.now(timezone.utc):%H:%M:%S} {msg}", file=sys.stderr, flush=True)

def upsert_prs(c, repo, nodes):
    now = datetime.now(timezone.utc).isoformat(timespec="seconds")
    for n in nodes:
        if not n:
            continue
        c.execute("insert or replace into prs values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (
            repo, n["number"], n["title"], n["body"], n["state"], (n.get("author") or {}).get("login"),
            json.dumps([l["name"] for l in n["labels"]["nodes"]]), n["createdAt"], n["updatedAt"],
            n["mergedAt"], n["closedAt"], n["url"], n["additions"], n["deletions"], n["changedFiles"],
            n["baseRefName"], n["headRefName"], now))
    c.commit()

def update_prs_by_updated(c, r):
    """Walk PRs newest-updated first; stop once older than the watermark. A partial run resumes from its cursor."""
    owner, name = r["gh"].split("/")
    q = f"""query($owner:String!,$name:String!,$cursor:String){{
      repository(owner:$owner,name:$name){{pullRequests(first:50,after:$cursor,orderBy:{{field:UPDATED_AT,direction:DESC}}){{
        pageInfo{{hasNextPage endCursor}} nodes{{{PR_FIELDS}}}}}}}
      rateLimit{{remaining resetAt}}}}"""
    watermark = meta_get(c, r["name"], "pr_watermark")
    stop_before = (datetime.fromisoformat(watermark) - OVERLAP).isoformat() if watermark else None
    cursor = meta_get(c, r["name"], "pr_run_cursor")
    run_max = meta_get(c, r["name"], "pr_run_max_updated")
    seen = 0
    while True:
        prs = gql(q, owner=owner, name=name, cursor=cursor)["repository"]["pullRequests"]
        nodes = prs["nodes"]
        upsert_prs(c, r["name"], nodes)
        seen += len(nodes)
        if nodes and (run_max is None or nodes[0]["updatedAt"] > run_max):
            run_max = nodes[0]["updatedAt"]
            meta_set(c, r["name"], "pr_run_max_updated", run_max)
        cursor = prs["pageInfo"]["endCursor"]
        meta_set(c, r["name"], "pr_run_cursor", cursor)
        if seen % 1000 < 50:
            log(f"{r['name']}: {seen} PRs scanned")
        done = not prs["pageInfo"]["hasNextPage"]
        if stop_before and nodes and nodes[-1]["updatedAt"].replace("Z", "+00:00") < stop_before:
            done = True
        if done:
            break
    if run_max:
        meta_set(c, r["name"], "pr_watermark", run_max.replace("Z", "+00:00"))
    meta_set(c, r["name"], "pr_run_cursor", None)
    meta_set(c, r["name"], "pr_run_max_updated", None)
    log(f"{r['name']}: {seen} PRs scanned, watermark {run_max}")

def update_prs_from_commits(c, r):
    """For monorepos (caplin): fetch only PRs referenced by in-scope commits, plus refresh ones still open."""
    owner, name = r["gh"].split("/")
    wanted = {n for (n,) in c.execute(
        "select distinct pr_number from commits where repo=? and pr_number is not null "
        "and pr_number not in (select number from prs where repo=? and state!='OPEN')", (r["name"], r["name"]))}
    not_prs = set(json.loads(meta_get(c, r["name"], "not_prs") or "[]"))
    wanted = sorted(wanted - not_prs)
    log(f"{r['name']}: fetching {len(wanted)} referenced PRs")
    for i in range(0, len(wanted), 40):
        chunk = wanted[i:i + 40]
        body = " ".join(f"p{n}: pullRequest(number:{n}){{{PR_FIELDS}}}" for n in chunk)
        d = gql(f"""query($owner:String!,$name:String!){{repository(owner:$owner,name:$name){{{body}}}
                    rateLimit{{remaining resetAt}}}}""", allow_partial=True, owner=owner, name=name)
        upsert_prs(c, r["name"], d["repository"].values())
        not_prs |= {n for n in chunk if not d["repository"].get(f"p{n}")}
        meta_set(c, r["name"], "not_prs", json.dumps(sorted(not_prs)))

def git(*args, **kw):
    return subprocess.run(["git", *args], capture_output=True, text=True, errors="replace", check=True, **kw).stdout

def update_commits(c, r):
    path = os.path.join(GIT_DIR, r["name"] + ".git")
    br = r["branch"]
    if not os.path.isdir(path):
        log(f"{r['name']}: cloning blobless mirror")
        git("clone", "-q", "--bare", "--filter=blob:none", "--single-branch", "--branch", br,
            f"https://github.com/{r['gh']}.git", path)
    git("-C", path, "fetch", "-q", "origin", f"+refs/heads/{br}:refs/heads/{br}")
    head = git("-C", path, "rev-parse", br).strip()
    last = meta_get(c, r["name"], "commits_head")
    rng = br
    if last:
        if last == head:
            log(f"{r['name']}: commits up to date")
            return
        if subprocess.run(["git", "-C", path, "merge-base", "--is-ancestor", last, head]).returncode == 0:
            rng = f"{last}..{head}"  # else history was rewritten: rescan everything, insert-or-ignore dedups
    fmt = "%x1e%H%x1f%cI%x1f%an%x1f%s%x1f%b%x1f"
    cmd = ["-C", path, "log", rng, f"--format={fmt}", "--name-only", "--no-renames", "--no-merges"]
    if r.get("paths"):
        cmd += ["--"] + r["paths"]
    n = 0
    for rec in git(*cmd).split("\x1e")[1:]:
        sha, date, author, subj, body, files = rec.split("\x1f")
        m = re.search(r"\(#(\d+)\)\s*$", subj) or re.search(r"#(\d+)", subj)
        c.execute("insert or ignore into commits values(?,?,?,?,?,?,?,?)", (
            r["name"], sha, date, author, subj, body.strip(),
            json.dumps([f for f in files.split("\n") if f.strip()]), int(m.group(1)) if m else None))
        n += 1
    c.commit()
    meta_set(c, r["name"], "commits_head", head)
    log(f"{r['name']}: {n} commits scanned ({rng})")

def rebuild_fts(c):
    c.execute("insert into prs_fts(prs_fts) values('rebuild')")
    c.execute("insert into commits_fts(commits_fts) values('rebuild')")
    c.commit()

def cmd_update(args):
    c = db()
    names = set(args.repos) or {r["name"] for r in REPOS}
    for r in REPOS:
        if r["name"] not in names:
            continue
        if not args.prs_only:
            update_commits(c, r)
        if not args.commits_only:
            (update_prs_from_commits if r.get("prs") == "from-commits" else update_prs_by_updated)(c, r)
        meta_set(c, r["name"], "last_update", datetime.now(timezone.utc).isoformat(timespec="seconds"))
    rebuild_fts(c)
    cmd_stats(args)

def cmd_stats(_):
    c = db()
    print(f"{'repo':12} {'prs':>7} {'merged':>7} {'commits':>8}  pr_watermark               last_update")
    for r in REPOS:
        n = r["name"]
        prs, merged = c.execute("select count(*), sum(merged_at is not null) from prs where repo=?", (n,)).fetchone()
        com = c.execute("select count(*) from commits where repo=?", (n,)).fetchone()[0]
        print(f"{n:12} {prs:>7} {merged or 0:>7} {com:>8}  {meta_get(c, n, 'pr_watermark') or '-':26} {meta_get(c, n, 'last_update') or '-'}")

def cmd_search(args):
    c = db()
    rows = []
    if args.kind in (None, "pr"):
        rows += c.execute("""select 'pr', p.repo, p.number, p.state, substr(p.created_at,1,10), p.title, p.url
            from prs_fts f join prs p on p.rowid=f.rowid where prs_fts match ?
            and (? is null or p.repo=?) order by bm25(prs_fts) limit ?""",
            (args.query, args.repo, args.repo, args.limit)).fetchall()
    if args.kind in (None, "commit"):
        rows += c.execute("""select 'commit', m.repo, substr(m.sha,1,10), m.pr_number, substr(m.date,1,10), m.subject, ''
            from commits_fts f join commits m on m.rowid=f.rowid where commits_fts match ?
            and (? is null or m.repo=?) order by bm25(commits_fts) limit ?""",
            (args.query, args.repo, args.repo, args.limit)).fetchall()
    for row in rows:
        print("\t".join("" if x is None else str(x) for x in row))

def cmd_export(args):
    c = db()
    c.row_factory = sqlite3.Row
    os.makedirs(args.dir, exist_ok=True)
    for r in REPOS:
        for table, order in (("prs", "number"), ("commits", "date")):
            with open(os.path.join(args.dir, f"{r['name']}.{table}.jsonl"), "w") as f:
                for row in c.execute(f"select * from {table} where repo=? order by {order}", (r["name"],)):
                    f.write(json.dumps(dict(row)) + "\n")

def main():
    ap = argparse.ArgumentParser()
    sp = ap.add_subparsers(dest="cmd", required=True)
    u = sp.add_parser("update"); u.add_argument("repos", nargs="*")
    u.add_argument("--prs-only", action="store_true"); u.add_argument("--commits-only", action="store_true")
    u.set_defaults(f=cmd_update)
    sp.add_parser("stats").set_defaults(f=cmd_stats)
    s = sp.add_parser("search"); s.add_argument("query"); s.add_argument("--repo")
    s.add_argument("--kind", choices=["pr", "commit"]); s.add_argument("--limit", type=int, default=30)
    s.set_defaults(f=cmd_search)
    e = sp.add_parser("export"); e.add_argument("dir"); e.set_defaults(f=cmd_export)
    a = ap.parse_args()
    a.f(a)

main()
