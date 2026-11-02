export const meta = {
  name: 'cl-perf-match',
  description: 'Place new perf records into the existing ideas, or into new ideas with new ids, without renumbering existing ideas',
  phases: [
    { title: 'Match', detail: 'per component, chunks of 120 records run one after another so later chunks see the new ideas of earlier ones' },
  ],
}
// args: { root, plan } where plan is match-in/plan.json from make_match_in.py
const D = `${args.root}/data/derived`
const DONE = { type: 'object', properties: { assigned: { type: 'integer' }, existing: { type: 'integer' }, new_ideas: { type: 'integer' } },
  required: ['assigned', 'existing', 'new_ideas'] }

const prompt = (comp, file, k, prev) => `Do not spawn subagents. You place new performance records from the history of Ethereum consensus clients into an existing list of canonical optimization ideas for component "${comp}".

Existing ideas: ${D}/match-in/${comp}.ideas.jsonl (fields cid, title, idea, mechanism).${prev.length ? ` Ideas added by earlier chunks of this run: ${prev.map(p => D + '/match-out/' + p).join(', ')} (same idea fields).` : ''}
New records: ${file} (fields id, idea, mechanism, measured, landed, resources).

For each record, choose:
- an existing idea (or one added by an earlier chunk) when one Lighthouse check answers both: same technique, not just the same subsystem ("cache the shuffling" and "compute the shuffling in parallel" are two ideas);
- otherwise a new idea. Records that share a technique go into the same new idea.

Write ${D}/match-out/${comp}-${k}.jsonl with the Write tool: one line per record, {"id": <record id>, "cid": <the chosen cid>}. Every record gets exactly one line.

Write ${D}/match-out/${comp}-${k}.new.jsonl with the new ideas (write an empty file if there are none), one JSON line each:
- cid: "${comp}-NNN", numbered on from the highest existing number of the plain "${comp}-NNN" ids in all the files above (never reuse an id, never use an "L" id)
- title: at most 10 words
- idea: 1 to 3 sentences, client-agnostic and checkable: what to do, where in a consensus client, and why it is cheaper. An engineer must be able to open the Lighthouse code and say whether it does this.
- mechanism: 2 to 6 words
- resources: subset of cpu, memory, disk, latency, bandwidth, sync, startup
- members: every record id in this new idea
- clients: the distinct client names among the members (the part of the id between ":" and "#" or "@")
- lighthouse_members: the member ids from lighthouse
- measured_best: the strongest measured gain quoted by a member, with its id, or null
- landed_somewhere: true if at least one member has landed true

Return assigned (records written), existing (records placed in an existing or earlier-chunk idea), new_ideas.`

const res = await pipeline(
  args.plan,
  async (p) => {
    const outs = []
    const prev = []
    for (let k = 0; k < p.files.length; k++) {
      const r = await agent(prompt(p.component, p.files[k], k, prev), { label: `match:${p.component}.${k}`, phase: 'Match', schema: DONE, model: 'sonnet' })
      outs.push(r)
      prev.push(`${p.component}-${k}.new.jsonl`)
    }
    return { component: p.component, records: p.records, failed: outs.filter(o => !o).length,
      assigned: outs.filter(Boolean).reduce((a, o) => a + o.assigned, 0), new_ideas: outs.filter(Boolean).reduce((a, o) => a + o.new_ideas, 0) }
  },
)
return res
