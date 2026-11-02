export const meta = {
  name: 'cl-perf-cluster',
  description: 'Cluster 6.4k extracted perf records into canonical client-agnostic optimization ideas per component',
  phases: [
    { title: 'Cluster', detail: 'one agent per chunk of <=160 records' },
    { title: 'Merge', detail: 'merge chunk clusters of the same component' },
  ],
}
const ROOT = args.root  // the directory that holds data/derived/
const plan = args.plan
const DONE = { type: 'object', properties: { ideas: { type: 'integer' }, members: { type: 'integer' }, path: { type: 'string' } }, required: ['ideas', 'members', 'path'] }

const FIELDS = `Each output line is one JSON object:
- cid: "<component>-NNN" (NNN from 001, unique in the file)
- title: at most 10 words
- idea: 1 to 3 sentences, client-agnostic and checkable: what to do, where in a consensus client, and why it is cheaper. An engineer must be able to open the Lighthouse code and say whether it does this.
- mechanism: 2 to 6 words
- resources: subset of cpu, memory, disk, latency, bandwidth, sync, startup
- members: every record id in this cluster
- clients: the distinct client names among the members (the part of the id between ":" and "#" or "@")
- lighthouse_members: the member ids from lighthouse (these suggest Lighthouse already did it, or did a version of it)
- measured_best: the strongest measured gain quoted by a member, with its id, or null
- landed_somewhere: true if at least one member has landed true`

const clusterPrompt = (comp, file, out, single) => `Do not spawn subagents. Read ${ROOT}/${file} (JSON lines: extracted performance changes from Ethereum consensus clients, all in component "${comp}"; fields id, idea, mechanism, measured, landed, resources).

Group the records into canonical optimization ideas. Records that describe the same technique belong together, also when they come from different clients or years. Two records belong together only if one Lighthouse check answers both. Keep different techniques apart even if they touch the same subsystem: "cache the shuffling" and "compute the shuffling in parallel" are two ideas. Every record goes in exactly one idea. A record with a unique technique becomes its own idea; do not drop it. Do not merge ideas only to make the list shorter.

Write the ideas to ${out} as JSON lines with the Write tool.${single ? '' : ' This file is one chunk of the component; a later step merges the chunks.'}
${FIELDS}

Before you write, check that the member count over all ideas equals the number of input lines. Return ideas, members and path.`

const mergePrompt = (comp, files, out) => `Do not spawn subagents. These files hold canonical optimization ideas for component "${comp}" of Ethereum consensus clients. Each file was clustered from a different chunk of the records, so the same idea can appear in several files:
${files.map(f => '- ' + ROOT + '/' + f).join('\n')}

Merge them into one list. Join two ideas only if one Lighthouse check answers both; then union their members, clients and lighthouse_members, keep the better measured_best, and rewrite title and idea to cover both. Keep all other ideas as they are. No member may be lost or duplicated. Number the cids again from ${comp}-001.

Write the result to ${out} as JSON lines with the Write tool.
${FIELDS}

Check that the total member count equals the sum over the input files. Return ideas, members and path.`

const results = await pipeline(
  plan,
  async (p) => {
    const single = p.files.length === 1
    const outs = await parallel(p.files.map((f, k) => () => agent(
      clusterPrompt(p.component, f, single ? `data/derived/ideas/${p.component}.jsonl` : `data/derived/clusters/${p.component}-${k}.jsonl`, single)
        .replace(/ data\/derived\//g, ` ${ROOT}/data/derived/`),
      { label: `cluster:${p.component}.${k}`, phase: 'Cluster', schema: DONE })))
    return { single, outs }
  },
  async (r, p) => {
    if (!r || r.outs.some(o => !o)) return { component: p.component, error: 'cluster chunk failed' }
    if (r.single) return { component: p.component, records: p.records, ideas: r.outs[0].ideas, members: r.outs[0].members }
    const files = p.files.map((_, k) => `data/derived/clusters/${p.component}-${k}.jsonl`)
    const m = await agent(mergePrompt(p.component, files, `${ROOT}/data/derived/ideas/${p.component}.jsonl`),
      { label: `merge:${p.component}`, phase: 'Merge', schema: DONE })
    return m ? { component: p.component, records: p.records, ideas: m.ideas, members: m.members } : { component: p.component, error: 'merge failed' }
  },
)
return results
