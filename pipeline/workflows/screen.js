export const meta = {
  name: 'cl-perf-screen',
  description: 'Prescreen 3675 canonical perf ideas for Lighthouse applicability and expected value',
  phases: [{ title: 'Screen', detail: '120 ideas per agent', model: 'sonnet' }],
}
const ROOT = args.root  // the directory that holds data/derived/
const DONE = { type: 'object', properties: { written: { type: 'integer' }, applicable: { type: 'integer' }, high: { type: 'integer' } }, required: ['written', 'applicable', 'high'] }
const prompt = (i) => `Do not spawn subagents. Read ${ROOT}/data/derived/screen-in/s${i}.jsonl. Each line is a performance optimization idea taken from the history of Ethereum consensus clients (prysm: Go, teku: Java, lodestar: TypeScript, nimbus: Nim, grandine/silver/ethlambda/lighthouse: Rust, caplin: Go). Fields: cid, title, idea, clients, n (number of PRs behind it), lh (how many of those PRs are Lighthouse's own), measured, landed.

Screen each idea for porting to Lighthouse (Rust, tokio + rayon, milhouse persistent trees, LevelDB/redb, rust-libp2p). Judge from your knowledge; do not search code in this step.

For each idea write one JSON line to ${ROOT}/data/derived/screen-out/s${i}.jsonl (Write tool) with:
- cid: unchanged
- applicable: "yes"; "no_runtime" (only about a runtime or language Lighthouse does not have: Go GC or goroutines, JVM, JS event loop or worker threads, Nim GC, protobuf or gRPC plumbing); "no_feature" (about a feature Lighthouse does not have or a fork that is gone, e.g. eth1 deposit polling after Electra, slasher-specific to another client's design); "unclear"
- value: "high" (could change mainnet node CPU, memory, disk, bandwidth or head latency by a visible amount, or fixes a pathological case such as an OOM or a stall), "medium", "low" (a micro tweak, cosmetic, rare path)
- reason: at most 15 words

Do not skip lines: the output line count must equal the input line count. Return written, applicable (count of "yes"), high (count of "high" among the "yes").`
const idx = Array.from({ length: args.n }, (_, i) => String(i).padStart(3, '0'))
const r = await parallel(idx.map(i => () => agent(prompt(i), { label: `screen:${i}`, phase: 'Screen', schema: DONE, model: 'sonnet' })))
return r.map((x, k) => x ? { b: idx[k], ...x } : { b: idx[k], failed: true })
