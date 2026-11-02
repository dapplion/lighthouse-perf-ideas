export const meta = {
  name: 'cl-perf-lh-check',
  description: 'Check each canonical perf idea against pinned sigp/lighthouse unstable, then adversarially re-check not/partial verdicts',
  phases: [
    { title: 'Check', detail: '8 ideas per agent, code search in the Lighthouse checkout', model: 'sonnet' },
    { title: 'Refute', detail: 'try to find the idea in Lighthouse for every not/partial of medium+ value' },
  ],
}
const ROOT = args.root  // the directory that holds data/derived/
const LH = args.lh  // the Lighthouse checkout to check against
const V = { type: 'object', properties: { items: { type: 'array', items: { type: 'object', properties: {
  cid: { type: 'string' }, verdict: { type: 'string', enum: ['implemented', 'partial', 'not', 'n/a'] }, value: { type: 'string' } },
  required: ['cid', 'verdict', 'value'] } } }, required: ['items'] }

const CTX = `Lighthouse source: ${LH} (a detached checkout of sigp/unstable at 928b61e719, 2026-10-30). Read-only: never edit, build or run git commands that change it. Dependency crates (milhouse, tree_hash, ethereum_hashing, ethereum_ssz, blst, c-kzg, rust_eth_kzg, libp2p and its gossipsub, discv5, leveldb/redb, ...) are part of Lighthouse for this purpose: find the version in ${LH}/Cargo.lock and read the source under ~/.cargo/registry/src/*/<crate>-<version>/ (or the git checkout under ~/.cargo/git/checkouts/ for git dependencies). Use Grep and Read; search by concept, not only by the other client's names. Do not spawn subagents.`

const checkPrompt = (file, out) => `${CTX}

Read ${ROOT}/${file}. Each line is a performance idea found in the history of Ethereum consensus clients (fields: cid, title, idea, value, members = source PR/commit ids, lighthouse_members = Lighthouse's own PRs in the same cluster, measured_best). To read a source PR, run \`${args.pipeline}/show.py <member id>\` (add --diff for the code). A lighthouse_members entry is a strong hint that Lighthouse did it once, but code can be removed later: confirm in the current source.

For each idea decide whether current Lighthouse does it:
- implemented: Lighthouse does this or an equivalent with the same effect
- partial: part of it, or only on some paths; say exactly what is missing
- not: Lighthouse does not do it, and the idea applies
- n/a: it does not apply to Lighthouse's design (say why in one sentence)

Write one JSON line per idea to ${out} (Write tool) with: cid, verdict, evidence (list of "path:line" in ${LH} or crate source, with a few words each; for "not", the places you looked and what the code does instead), gap (for partial/not: what Lighthouse would have to change, 1-3 sentences, naming the functions), effort ("S" under a day, "M" days, "L" weeks or a redesign), impact (1-2 sentences: what would get cheaper on a mainnet node, and roughly by how much if you can tell), confidence ("high" if you read the relevant code, "low" otherwise), value (copy from input).

The output must have exactly one line per input line. Return items: cid, verdict, value for each idea.`

const refutePrompt = (rows, file, out) => `${CTX}

An earlier reviewer concluded that current Lighthouse does NOT do (or only partly does) the ideas below. Your job is to refute that: look hard for an existing implementation or an equivalent mechanism, including in dependency crates, under different names, and in code paths the reviewer may not have searched. Be skeptical of the earlier verdict, but do not invent evidence: if after a real search it is not there, uphold it.

The ideas, with the earlier verdict, evidence and gap, are the lines of ${ROOT}/${file} whose cid is one of: ${rows.map(r => r.cid).join(', ')}. Read those lines. Read the original idea with full context in ${ROOT}/data/derived/check-in/${file.split('/').pop()} and the source PRs with \`${args.pipeline}/show.py <id>\`.

For each idea write one JSON line to ${out} (Write tool) with: cid, final_verdict (implemented | partial | not | n/a), changed (true if different from the earlier verdict), evidence (path:line list supporting the final verdict), gap (updated, for partial/not), effort (S/M/L), impact, confidence (high/low), note (1-2 sentences on what you checked beyond the earlier review). Return items: cid, verdict (= final_verdict), value.`

const files = Array.from({ length: args.n }, (_, k) => `data/derived/check-in/b${String(k).padStart(3, '0')}.jsonl`)
const res = await pipeline(
  files,
  (f) => {
    const name = f.split('/').pop()
    return agent(checkPrompt(f, `${ROOT}/data/derived/check-out/${name}`), { label: `check:${name}`, phase: 'Check', schema: V, model: 'sonnet' })
  },
  async (chk, f) => {
    if (!chk) return { file: f, error: 'check failed' }
    const name = f.split('/').pop()
    const todo = chk.items.filter(x => (x.verdict === 'not' || x.verdict === 'partial') && (x.value === 'high' || x.value === 'medium'))
    if (!todo.length) return { file: f, check: chk.items, refute: [] }
    const ref = await agent(refutePrompt(todo, `data/derived/check-out/${name}`, `${ROOT}/data/derived/refute-out/${name}`),
      { label: `refute:${name}`, phase: 'Refute', schema: V })
    return { file: f, check: chk.items, refute: ref ? ref.items : null }
  },
)
const flat = res.filter(Boolean)
const count = (arr, k) => arr.reduce((m, x) => (m[x[k]] = (m[x[k]] || 0) + 1, m), {})
return {
  batches: flat.length,
  failed: flat.filter(r => r.error || r.refute === null).map(r => r.file),
  check_verdicts: count(flat.flatMap(r => r.check || []), 'verdict'),
  refute_verdicts: count(flat.flatMap(r => r.refute || []), 'verdict'),
  refuted: flat.flatMap(r => (r.refute || []).map(x => ({ x, before: (r.check || []).find(c => c.cid === x.cid) }))).filter(p => p.before && p.before.verdict !== p.x.verdict).length,
}
