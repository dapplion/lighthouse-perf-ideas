export const meta = {
  name: 'cl-perf-recheck',
  description: 'Check the never-checked ideas against Lighthouse (check + refute), and re-check every implemented verdict with a skeptic',
  phases: [
    { title: 'Check', detail: '8 never-checked ideas per agent', model: 'sonnet' },
    { title: 'Refute', detail: 'try to find the idea in Lighthouse for every not/partial of medium+ value' },
    { title: 'Skeptic', detail: '8 implemented verdicts per agent: look for where Lighthouse does NOT do it' },
  ],
}
const ROOT = args.root  // the directory that holds data/derived/
const LH = args.lh  // the Lighthouse checkout to check against
const pad = (i) => String(i).padStart(3, '0')
const T = args.tag || '2'  // check<T>-in -> check<T>-out, refute<T>-out
const V = { type: 'object', properties: { items: { type: 'array', items: { type: 'object', properties: {
  cid: { type: 'string' }, verdict: { type: 'string', enum: ['implemented', 'partial', 'not', 'n/a'] }, value: { type: 'string' } },
  required: ['cid', 'verdict', 'value'] } } }, required: ['items'] }

const CTX = `Lighthouse source: ${LH} (a detached checkout of sigp/unstable at 928b61e719, 2026-10-30). Read-only: never edit, build or run git commands that change it. Dependency crates (milhouse, tree_hash, ethereum_hashing, ethereum_ssz, blst, c-kzg, rust_eth_kzg, libp2p and its gossipsub, discv5, leveldb/redb, ...) are part of Lighthouse for this purpose: find the version in ${LH}/Cargo.lock and read the source under ~/.cargo/registry/src/*/<crate>-<version>/ (or the git checkout under ~/.cargo/git/checkouts/ for git dependencies). Use Grep and Read; search by concept, not only by the other client's names. Do not spawn subagents.`

const checkPrompt = (inp, out) => `${CTX}

Read ${inp}. Each line is a performance idea found in the history of Ethereum consensus clients (fields: cid, title, idea, members = source PR/commit ids, lighthouse_members = Lighthouse's own PRs in the same cluster, measured_best, prescreen = an earlier guess from the title alone about whether it applies and is worth checking). To read a source PR, run \`${args.pipeline}/show.py <member id>\` (add --diff for the code). A lighthouse_members entry is a strong hint that Lighthouse did it once, but code can be removed later: confirm in the current source. Treat the prescreen as a guess, not a fact.

For each idea decide whether current Lighthouse does it:
- implemented: Lighthouse does this or an equivalent with the same effect
- partial: part of it, or only on some paths; say exactly what is missing
- not: Lighthouse does not do it, and the idea applies
- n/a: it does not apply to Lighthouse's design (say why in one sentence)

Also rate value after reading the code: "high" (a clear gain on every mainnet node), "medium" (a real gain on some nodes or paths), "low" (marginal, or only for rare setups).

Write one JSON line per idea to ${out} (Write tool) with: cid, verdict, value, evidence (list of "path:line" in ${LH} or crate source, with a few words each; for "not", the places you looked and what the code does instead), gap (for partial/not: what Lighthouse would have to change, 1-3 sentences, naming the functions), effort ("S" under a day, "M" days, "L" weeks or a redesign), impact (1-2 sentences: what would get cheaper on a mainnet node, and roughly by how much if you can tell), confidence ("high" if you read the relevant code, "low" otherwise).

The output must have exactly one line per input line. Return items: cid, verdict, value for each idea.`

const refutePrompt = (rows, file, inp, out) => `${CTX}

An earlier reviewer concluded that current Lighthouse does NOT do (or only partly does) the ideas below. Your job is to refute that: look hard for an existing implementation or an equivalent mechanism, including in dependency crates, under different names, and in code paths the reviewer may not have searched. Be skeptical of the earlier verdict, but do not invent evidence: if after a real search it is not there, uphold it.

The ideas, with the earlier verdict, evidence and gap, are the lines of ${file} whose cid is one of: ${rows.map(r => r.cid).join(', ')}. Read those lines. Read the original idea in ${inp} and the source PRs with \`${args.pipeline}/show.py <id>\`.

For each idea write one JSON line to ${out} (Write tool) with: cid, final_verdict (implemented | partial | not | n/a), changed (true if different from the earlier verdict), value (high/medium/low, your rating), evidence (path:line list supporting the final verdict), gap (updated, for partial/not), effort (S/M/L), impact, confidence (high/low), note (1-2 sentences on what you checked beyond the earlier review). Return items: cid, verdict (= final_verdict), value.`

const skepticPrompt = (inp, out) => `${CTX}

Read ${inp}. Each line is a performance idea found in the history of Ethereum consensus clients, with an earlier verdict that current Lighthouse already implements it (fields: cid, title, idea, members, lighthouse_members, measured_best, value, and the earlier evidence, gap and impact). Earlier checks were sometimes wrong in this direction: they found a related mechanism and called it the same thing, or found it on one path but not on the hot path.

Your job is to refute "implemented". For each idea, open the code the earlier evidence cites and confirm it does what the idea describes, with the same effect, on the paths that matter (block import, gossip, epoch processing, the API, sync, as the idea implies). Then look for paths where Lighthouse does NOT do it. Read the source PRs with \`${args.pipeline}/show.py <id>\` (add --diff) when you need the exact mechanism. Do not invent gaps: if the implementation is real and complete, uphold it.

For each idea write one JSON line to ${out} (Write tool) with: cid, final_verdict (implemented | partial | not | n/a), changed (true if not "implemented"), value (high/medium/low, your rating), evidence (path:line list supporting the final verdict), gap (for partial/not: what is missing, naming the functions), effort (S/M/L), impact, confidence (high/low), note (1-2 sentences: what you verified, and where the earlier evidence was right or wrong).

The output must have exactly one line per input line. Return items: cid, verdict (= final_verdict), value.`

const D = `${ROOT}/data/derived`
const checks = pipeline(
  Array.from({ length: args.check_n }, (_, i) => i),
  (i) => agent(checkPrompt(`${D}/check${T}-in/u${pad(i)}.jsonl`, `${D}/check${T}-out/u${pad(i)}.jsonl`), { label: `check:u${i}`, phase: 'Check', schema: V, model: 'sonnet' }),
  async (chk, i) => {
    if (!chk) return { kind: 'check', i, error: 'check failed' }
    const todo = chk.items.filter(x => (x.verdict === 'not' || x.verdict === 'partial') && (x.value === 'high' || x.value === 'medium'))
    if (!todo.length) return { kind: 'check', i, check: chk.items, refute: [] }
    const ref = await agent(refutePrompt(todo, `${D}/check${T}-out/u${pad(i)}.jsonl`, `${D}/check${T}-in/u${pad(i)}.jsonl`, `${D}/refute${T}-out/u${pad(i)}.jsonl`),
      { label: `refute:u${i}`, phase: 'Refute', schema: V })
    return { kind: 'check', i, check: chk.items, refute: ref ? ref.items : null }
  },
)
const skeptic = pipeline(
  Array.from({ length: args.impl_n || 0 }, (_, i) => i),
  (i) => agent(skepticPrompt(`${D}/impl-in/i${pad(i)}.jsonl`, `${D}/impl-out/i${pad(i)}.jsonl`), { label: `skeptic:i${i}`, phase: 'Skeptic', schema: V })
    .then(r => r ? { kind: 'skeptic', i, items: r.items } : { kind: 'skeptic', i, error: 'skeptic failed' }),
)
const [c, s] = await Promise.all([checks, skeptic])
const count = (arr, k) => arr.reduce((m, x) => (m[x[k]] = (m[x[k]] || 0) + 1, m), {})
const cf = c.filter(Boolean), sf = s.filter(Boolean)
return {
  check_failed: cf.filter(r => r.error || r.refute === null).map(r => r.i),
  check_verdicts: count(cf.flatMap(r => r.check || []), 'verdict'),
  refute_verdicts: count(cf.flatMap(r => r.refute || []), 'verdict'),
  skeptic_failed: sf.filter(r => r.error).map(r => r.i),
  skeptic_verdicts: count(sf.flatMap(r => r.items || []), 'verdict'),
}
