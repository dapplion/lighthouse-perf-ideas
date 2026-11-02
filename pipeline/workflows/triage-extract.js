export const meta = {
  name: 'cl-perf-triage-extract',
  description: 'Triage every CL client PR/commit for perf relevance, then extract client-agnostic optimization ideas',
  phases: [
    { title: 'Triage', detail: 'recall-first scan of 300 items per batch (190 batches) + forced keyword hits', model: 'sonnet' },
    { title: 'Extract', detail: 'read full PR/commit (+diff when thin), write structured idea records', model: 'sonnet' },
  ],
}

const ROOT = args.root  // the directory that holds data/derived/
const idx = args.idx || Array.from({ length: args.n }, (_, i) => i)
const batches = idx.map(i => ({ i, path: `data/derived/triage-in/batch-${String(i).padStart(3, '0')}.tsv` }))

const TRIAGE = {
  type: 'object',
  properties: {
    lines_read: { type: 'integer' },
    candidates: { type: 'array', items: { type: 'object', properties: {
      id: { type: 'string' }, hint: { type: 'string' } }, required: ['id', 'hint'] } },
  },
  required: ['lines_read', 'candidates'],
}
const EXTRACT = {
  type: 'object',
  properties: { written: { type: 'integer' }, perf: { type: 'integer' }, path: { type: 'string' } },
  required: ['written', 'perf', 'path'],
}

const triagePrompt = (path) => `Read the file ${ROOT}/${path} with the Read tool (all of it; it has about 300 lines). Each line is one pull request or commit from an Ethereum consensus client, tab-separated: id, state (M merged, C closed or commit, O open; a leading * means a keyword matched), title, [labels], start of the body.

Select every line that might be a PERFORMANCE change or a performance idea. This is the recall stage: when in doubt, select it. A later stage reads the full text and drops the false positives, but a line you skip here is lost for good.

Performance means anything that changes the use of CPU, memory, disk (size, IO, compaction, pruning), latency or timing (block import, block production, attestation, head, sync speed, startup, API response time), or network bandwidth (gossip, RPC, duplicates, compression). Examples: caching, batching, parallelism, lock contention, fewer allocations or clones, data structure changes, lazy evaluation, SIMD and assembly, faster hashing, BLS and KZG batching, database layout, state storage and diffs, pruning, memory leaks, OOM fixes, timeouts and deadlines, queue and backpressure tuning, peer and mesh tuning, benchmarks and profiling work, perf regressions and their fixes, "speed up", "reduce", "avoid", "optimize", "faster", "slow".

Always select every line whose state starts with *. Do not select: pure refactors, docs, CI, tests only, dependency bumps, renames, features without a perf aspect, spec conformance fixes without a perf aspect.

For each selected line, return its id exactly as written in the first column and a hint of 2 to 6 words (resource and mechanism). Also return lines_read: the number of lines you read. Read the whole file; if the Read tool truncates it, read the rest with offset.`

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
  batches,
  (b) => agent(triagePrompt(b.path), { label: `triage:${b.i}`, phase: 'Triage', schema: TRIAGE, model: 'sonnet' }),
  async (tri, b) => {
    const i = b.i
    if (!tri) return null
    const cands = tri.candidates
    const path = b.path
    const chunks = []
    for (let k = 0; k < cands.length; k += 50) chunks.push(cands.slice(k, k + 50))
    const outs = await parallel(chunks.map((ch, k) => () => agent(
      extractPrompt(ch, `${ROOT}/data/derived/extract/b${String(i).padStart(3, '0')}-${k}.jsonl`),
      { label: `extract:${i}.${k}`, phase: 'Extract', schema: EXTRACT, model: 'sonnet' })))
    return { batch: path, lines_read: tri.lines_read, candidates: cands.length,
      chunks: chunks.length, failed_chunks: outs.filter(o => !o).length,
      written: outs.filter(Boolean).reduce((a, o) => a + o.written, 0),
      perf: outs.filter(Boolean).reduce((a, o) => a + o.perf, 0) }
  },
)
const ok = results.filter(Boolean)
log(`batches done ${ok.length}/${batches.length}; candidates ${ok.reduce((a, r) => a + r.candidates, 0)}; perf ${ok.reduce((a, r) => a + r.perf, 0)}`)
return { per_batch: results }
