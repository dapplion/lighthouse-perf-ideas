export const meta = {
  name: 'cl-perf-retriage',
  description: 'Second triage of every rejected PR/commit on full body + changed files, with a saved decision per item; extract the new perf items',
  phases: [
    { title: 'Retriage', detail: '150 items per agent, one decision + reason per item written to retriage-out/', model: 'sonnet' },
    { title: 'Extract', detail: 'read full PR/commit (+diff when thin) for each new hit, write idea records', model: 'sonnet' },
  ],
}

const ROOT = args.root  // the directory that holds data/derived/
const idx = args.idx || Array.from({ length: args.n }, (_, i) => i)
const pad = (i) => String(i).padStart(3, '0')

const TRIAGE = {
  type: 'object',
  properties: {
    lines_read: { type: 'integer' },
    written: { type: 'integer' },
    hits: { type: 'array', items: { type: 'object', properties: { id: { type: 'string' }, hint: { type: 'string' } }, required: ['id', 'hint'] } },
  },
  required: ['lines_read', 'written', 'hits'],
}
const EXTRACT = {
  type: 'object',
  properties: { written: { type: 'integer' }, perf: { type: 'integer' }, path: { type: 'string' } },
  required: ['written', 'perf', 'path'],
}

const triagePrompt = (inp, out) => `Do not spawn subagents. Read the file ${inp} with the Read tool, all of it (about 150 lines; if the Read tool truncates it, read the rest with offset). Each line is one pull request or commit from an Ethereum consensus client, tab-separated: id, state (M merged, C closed or commit, O open), title, [labels], files: the changed files, body: the start of the description.

An earlier screen judged these items on the title alone and found no performance aspect. Judge each one again, now with the body and the changed files. The goal is recall: find every item that might be a performance change or contain a performance idea.

Performance means anything that changes the use of CPU, memory, disk (size, IO, compaction, pruning), latency or timing (block import, block production, attestation, head, sync speed, startup, API response time), or network bandwidth (gossip, RPC, duplicates, compression). It includes caching, batching, parallelism, lock contention, fewer allocations or clones, data structure changes, lazy evaluation, SIMD and assembly, faster hashing, BLS and KZG batching, database layout, state storage and diffs, pruning, memory leaks, OOM fixes, timeouts and deadlines, queue and backpressure tuning, peer and mesh tuning, benchmarks and profiling work, and performance regressions and their fixes. It also includes a refactor or feature whose body or files show a performance side effect (for example a new cache, a moved hot loop, a changed data structure in a hot path).

Not performance: pure refactors, docs, CI, tests only, dependency bumps, renames, spec conformance fixes, features with no performance aspect. When in doubt, mark it perf: a later stage reads the full PR and drops false positives.

Write one JSON line per input line to ${out} with the Write tool: {"id": <the id exactly as in the first column>, "perf": true or false, "reason": <at most 12 words: why>}. Every input line gets exactly one output line, in input order.

Return lines_read, written (the number of output lines), and hits: for each perf true line, its id and a hint of 2 to 6 words (resource and mechanism).`

const extractPrompt = (ids, out) => `You extract performance optimization ideas from the history of Ethereum consensus clients (lighthouse, prysm, teku, nimbus, lodestar, grandine, silver, ethlambda, caplin). The goal is a list of ideas that could be ported to Lighthouse. Do not spawn subagents.

Items (id: triage hint):
${ids.map(c => `- ${c.id}: ${c.hint}`).join('\n')}

For each item, run \`${args.pipeline}/show.py <id> [<id> ...]\` (you can pass several ids at once) to read the full PR or commit and its file list. When the body is empty or does not explain the mechanism, run it again with \`--diff\` for that item (the diff is truncated at 15 kB; that is enough). Do not guess a mechanism you did not see.

Write exactly one JSON object per item, one per line, to ${out} (create the file with the Write tool; no other output files). Fields:
- id: the item id as a string, exactly as given above (for example "pr:lighthouse#1234" or "commit:nimbus@f9c74bb1e469"), never a number
- is_perf: true only if the change really targets or materially affects performance
- resources: subset of ["cpu","memory","disk","latency","bandwidth","sync","startup"]
- component: one of "state_transition","epoch_processing","tree_hash","ssz","bls","kzg","fork_choice","block_import","block_production","attestation_processing","op_pool","gossip_validation","gossipsub","rpc","discovery_peers","range_sync","lookup_sync","backfill","db_hot","db_cold","state_cache","other_caches","data_availability","beacon_api","validator_client","el_interaction","logging_metrics","allocator_runtime","build","other"
- idea: one or two sentences, CLIENT-AGNOSTIC, saying what to do and why it is faster or smaller, specific enough that an engineer can check whether Lighthouse does it (for example "Cache the committee shuffling per (epoch, decision root) and share it between block import and attestation verification, so it is computed once per fork per epoch"). null if is_perf is false.
- mechanism: 2 to 6 words (for example "batch signature verification")
- measured: the gain the PR states, with its numbers, quoted briefly; null if it gives none
- landed: true if merged or a commit on the branch, false if closed unmerged, "open" if open
- confidence: "high" if the text or diff shows the mechanism, "low" if you inferred it

Then return written (lines written), perf (lines with is_perf true) and path.`

const results = await pipeline(
  idx,
  (i) => agent(triagePrompt(`${ROOT}/data/derived/retriage-in/r${pad(i)}.tsv`, `${ROOT}/data/derived/retriage-out/r${pad(i)}.jsonl`),
    { label: `retriage:${i}`, phase: 'Retriage', schema: TRIAGE, model: 'sonnet' }),
  async (tri, i) => {
    if (!tri) return { i, error: 'retriage failed' }
    const chunks = []
    for (let k = 0; k < tri.hits.length; k += 40) chunks.push(tri.hits.slice(k, k + 40))
    const outs = await parallel(chunks.map((ch, k) => () => agent(
      extractPrompt(ch, `${ROOT}/data/derived/extract/r${pad(i)}-${k}.jsonl`),
      { label: `extract:r${i}.${k}`, phase: 'Extract', schema: EXTRACT, model: 'sonnet' })))
    return { i, lines_read: tri.lines_read, written: tri.written, hits: tri.hits.length,
      failed_chunks: outs.filter(o => !o).length, perf: outs.filter(Boolean).reduce((a, o) => a + o.perf, 0) }
  },
)
const ok = results.filter(r => r && !r.error)
log(`retriage done ${ok.length}/${idx.length}; hits ${ok.reduce((a, r) => a + r.hits, 0)}; perf after extract ${ok.reduce((a, r) => a + r.perf, 0)}`)
return {
  failed: results.filter(r => !r || r.error).map((r, k) => r ? r.i : idx[k]),
  short: ok.filter(r => r.written !== r.lines_read).map(r => r.i),
  failed_extract: ok.filter(r => r.failed_chunks).map(r => r.i),
  hits: ok.reduce((a, r) => a + r.hits, 0),
  perf: ok.reduce((a, r) => a + r.perf, 0),
}
