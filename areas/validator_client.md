# validator_client

186 ideas: 23 not, 26 partial, 77 implemented, 60 n/a; 6 actionable (high or medium value, verdict `not` or `partial`). [Back to the summary](../README.md).

| id | idea | verdict | value | effort | resources |
|---|---|---|---|---|---|
| [validator_client-001](#validator_client-001) | Look up validator statuses via POST body, not batched GET | not | low | S | bandwidth, cpu, latency |
| [validator_client-002](#validator_client-002) | Batch pubkey-to-index and status lookups in large batches | not | low | S | latency, bandwidth, startup |
| [validator_client-003](#validator_client-003) | Batch validator balance/performance queries | n/a | low | S | latency, bandwidth |
| [validator_client-004](#validator_client-004) | Subscribe to head event stream instead of polling | implemented | medium | S | latency, bandwidth, cpu |
| [validator_client-005](#validator_client-005) **★** | SSZ encoding for VC-BN block traffic | partial | medium | S | bandwidth, cpu, latency |
| [validator_client-006](#validator_client-006) | Trigger attestation fetch on head event, not block event | implemented | low | S | latency |
| [validator_client-007](#validator_client-007) | Attest as soon as the slot's head block arrives | implemented | medium | S | latency |
| [validator_client-008](#validator_client-008) **★** | Request blinded blocks from the beacon node | partial | medium | S | bandwidth, latency |
| [validator_client-009](#validator_client-009) | Multi-BN: attest on first perfect attestation data | not | low | M | latency |
| [validator_client-010](#validator_client-010) | Sync committee messages as soon as block seen | implemented | low | S | latency |
| [validator_client-011](#validator_client-011) **★** | Payload timeliness votes on payload-available event | partial | medium | S | latency, cpu |
| [validator_client-012](#validator_client-012) | Slim duties response without full committee lists | implemented | low | S | bandwidth, cpu, latency |
| [validator_client-013](#validator_client-013) | Aggregate/subscribe only for actual duties | implemented | low | S | cpu, bandwidth |
| [validator_client-014](#validator_client-014) | Do not fetch all validators for activation-queue logging | implemented | low | S | latency, bandwidth, cpu |
| [validator_client-015](#validator_client-015) | Block metrics via historic roots, not disk block loads | n/a | low | S | disk, cpu |
| [validator_client-016](#validator_client-016) | Allocation-free auth token check | not | low | S | cpu, memory |
| [validator_client-017](#validator_client-017) | Skip unneeded committee-size fetches in performance tracker | n/a | low | S | cpu, bandwidth |
| [validator_client-018](#validator_client-018) | Prefetch next-epoch duties off the critical path | partial | low | S | latency |
| [validator_client-019](#validator_client-019) | Batch attestation submission per slot | implemented | medium | S | latency, cpu, bandwidth |
| [validator_client-020](#validator_client-020) | Batch aggregate-and-proof submission | implemented | low | S | latency, bandwidth |
| [validator_client-021](#validator_client-021) | Batch slashing-protection checks into one transaction | implemented | medium | S | latency, disk, cpu |
| [validator_client-022](#validator_client-022) | Fewer DB transactions per slashing-protection check | partial | low | M | latency, disk |
| [validator_client-023](#validator_client-023) | Bounded batches for builder registrations | implemented | low | S | bandwidth, latency |
| [validator_client-024](#validator_client-024) | Spread attestation signing across the epoch | n/a | low | S | cpu, latency |
| [validator_client-025](#validator_client-025) | Decrypt validator keystores in parallel at startup | not | low | S | startup, cpu |
| [validator_client-026](#validator_client-026) | Faster crypto for keystore KDF | not | low | S | startup, cpu |
| [validator_client-027](#validator_client-027) | Batch slashing interchange import writes | n/a | low | S | disk, memory, latency |
| [validator_client-028](#validator_client-028) | Deserialize interchange JSON from memory slice | implemented | low | S | cpu, latency |
| [validator_client-029](#validator_client-029) | Bound interchange import target epochs | n/a | low |  | cpu, disk |
| [validator_client-030](#validator_client-030) | Limit min-span lookback in slashing protection | n/a | low | S | disk, latency |
| [validator_client-031](#validator_client-031) | Full fill percent for append-only DB buckets | n/a | low | S | disk |
| [validator_client-032](#validator_client-032) | Range-bound DB iterator for slashing pubkeys | n/a | low | S | memory |
| [validator_client-033](#validator_client-033) | Split large DB migration into small transactions | n/a | low | S | memory, disk |
| [validator_client-034](#validator_client-034) | Fetch attestation data once per slot and reuse | implemented | medium | S | latency, bandwidth, cpu |
| [validator_client-035](#validator_client-035) | Cache builder config per proposer slot | implemented | low | S | cpu, latency |
| [validator_client-036](#validator_client-036) | Cache signed builder registrations | implemented | low | S | cpu, latency |
| [validator_client-037](#validator_client-037) | Resend builder registrations only at epoch start or expiry | implemented | low | S | bandwidth, cpu |
| [validator_client-038](#validator_client-038) | Register only active validators with builders | partial | low | S | cpu, bandwidth |
| [validator_client-039](#validator_client-039) | Move builder registrations and proposer prep past epoch start | not | low | S | latency, cpu |
| [validator_client-040](#validator_client-040) | One encrypted store for all keys, one KDF | implemented | low | S | startup, cpu, memory |
| [validator_client-041](#validator_client-041) | Cache signing domain data per epoch | n/a | low | S | latency, bandwidth |
| [validator_client-042](#validator_client-042) | Cache slashing-protection file paths | n/a | low | S | disk, cpu |
| [validator_client-043](#validator_client-043) | Cache proposer config with shared refresh | n/a | low | S | latency, disk |
| [validator_client-044](#validator_client-044) | Cache aggregator selection proofs | implemented | low | S | cpu, latency |
| [validator_client-045](#validator_client-045) | Prebuild remote signer request URI | n/a | low | S | cpu |
| [validator_client-046](#validator_client-046) | Cache own validator index | implemented | low | S | latency, bandwidth |
| [validator_client-047](#validator_client-047) | Bound concurrent keystore decryptions at startup | implemented | low | S | memory, startup |
| [validator_client-048](#validator_client-048) | Cap skip slots processed for duties | n/a | low | S | cpu, latency |
| [validator_client-049](#validator_client-049) | Cheap KDF for test keystores | n/a | low | S | startup, cpu |
| [validator_client-050](#validator_client-050) | Cheaper per-slot proposer settings push | n/a | low | S | latency, cpu |
| [validator_client-051](#validator_client-051) | Proposer preferences once per epoch | implemented | low | S | cpu, latency |
| [validator_client-052](#validator_client-052) | Start duty services concurrently | n/a | low | S | startup, latency |
| [validator_client-053](#validator_client-053) | Sign duties concurrently, not sequentially | partial | low | S | latency |
| [validator_client-054](#validator_client-054) | Stop long loops on request cancellation | n/a | low | S | cpu |
| [validator_client-055](#validator_client-055) **★** | Refetch duties only when dependent root changes | partial | medium | S | bandwidth, cpu, latency |
| [validator_client-056](#validator_client-056) | Fetch duties once per epoch, serve slots from cache | partial | low | S | bandwidth, latency, cpu |
| [validator_client-057](#validator_client-057) | Short lookahead, per-slot batches for selection proofs | partial | low | S | cpu, bandwidth, latency |
| [validator_client-058](#validator_client-058) | Configurable keystore reload debounce | n/a | low |  | cpu, disk |
| [validator_client-059](#validator_client-059) | Decrypt keystores before waiting for beacon node | implemented | low | S | startup |
| [validator_client-060](#validator_client-060) | Dedicated executor for committee precalculation | n/a | low |  | cpu, latency |
| [validator_client-061](#validator_client-061) | Dedicated executors for remote BN calls | n/a | low |  | latency |
| [validator_client-062](#validator_client-062) | Size VC executor threads and queues to load | n/a | low |  | cpu, latency |
| [validator_client-063](#validator_client-063) | Batch committee subnet subscriptions | implemented | low | S | latency, bandwidth |
| [validator_client-064](#validator_client-064) | Deduplicate subnet subscription messages | partial | low | S | cpu |
| [validator_client-065](#validator_client-065) | One subscription per duty | implemented | low | S | bandwidth |
| [validator_client-066](#validator_client-066) | Deduplicate aggregator work across local keys | partial | low | S | cpu, bandwidth |
| [validator_client-067](#validator_client-067) | Shared periodic fork info fetch | n/a | low |  | bandwidth, latency |
| [validator_client-068](#validator_client-068) | No subnet subscriptions until synced | not | low | S | bandwidth, cpu |
| [validator_client-069](#validator_client-069) | Late next-period sync committee duties/subscriptions | partial | low | S | bandwidth, cpu |
| [validator_client-070](#validator_client-070) | Derive HD keys on demand | n/a | low | L | disk, startup |
| [validator_client-071](#validator_client-071) | Opt-in duty countdown logging | n/a | low | S | cpu |
| [validator_client-072](#validator_client-072) | Subnet subscriptions and selection proofs off duty path | implemented | low | S | latency |
| [validator_client-073](#validator_client-073) | Short-circuit empty duty requests | implemented | low | S | cpu |
| [validator_client-074](#validator_client-074) | Event-driven wait for activation | partial | low | S | latency |
| [validator_client-075](#validator_client-075) | Remove abort listeners after each request | n/a | low | S | memory |
| [validator_client-076](#validator_client-076) | Release performance tracker entries | n/a | low | S | memory |
| [validator_client-077](#validator_client-077) | Parallel keystore decryption for keymanager API imports | not | low | M | cpu, latency |
| [validator_client-078](#validator_client-078) | Decrypt inline when KDF is cheap | n/a | low |  | latency, startup |
| [validator_client-079](#validator_client-079) | Size decrypt pool to min(cores, keystores) | n/a | low |  | cpu, startup |
| [validator_client-080](#validator_client-080) | Cache KDF output for shared salt and password | not | low | M | cpu, startup |
| [validator_client-081](#validator_client-081) | Share keystore decryption cache with import API | partial | low | M | cpu, latency |
| [validator_client-082](#validator_client-082) | Cache decrypted secret keys for signing | implemented | low | S | cpu, latency |
| [validator_client-083](#validator_client-083) | Unencrypted keys for test clusters | partial | low | S | startup |
| [validator_client-084](#validator_client-084) | Skip keystore decrypt when creating validator dirs | implemented | low | S | cpu, startup |
| [validator_client-085](#validator_client-085) | Skip key cache decrypt with no local keystores | implemented | low | S | cpu, memory, latency |
| [validator_client-086](#validator_client-086) | One KDF per key on load | partial | low | S | cpu, startup |
| [validator_client-087](#validator_client-087) | Load validator keys only once at startup | n/a | low |  | cpu, startup |
| [validator_client-088](#validator_client-088) | Derive mnemonic keypairs in parallel | not | low | S | cpu, startup |
| [validator_client-089](#validator_client-089) | Flat directory listing for keystore import | not | low | S | startup |
| [validator_client-090](#validator_client-090) | Poll unknown validator indices once per epoch | implemented | low | S | cpu, latency |
| [validator_client-091](#validator_client-091) | Use validator index from duties response | not | low | S | memory, latency, bandwidth |
| [validator_client-092](#validator_client-092) | Prune slashing protection database | implemented | medium | S | cpu, disk, latency |
| [validator_client-093](#validator_client-093) | Per-entry sorted slashing protection storage | implemented | low | S | cpu, disk, latency, startup |
| [validator_client-094](#validator_client-094) | Min-max span arrays for surround checks | n/a | low |  | cpu, disk |
| [validator_client-095](#validator_client-095) | Minimal slashing protection database | implemented | low | S | disk, startup |
| [validator_client-096](#validator_client-096) | Snappy-compress stored attestation history | n/a | low |  | disk |
| [validator_client-097](#validator_client-097) | Read-only transactions for slashing lookups | n/a | low |  | disk, latency |
| [validator_client-098](#validator_client-098) | SQLite exclusive locking for slashing DB | implemented | low | S | disk, latency |
| [validator_client-099](#validator_client-099) | Skip slashing DB writes for remote-signer keys | implemented | low | S | disk, latency |
| [validator_client-100](#validator_client-100) | Lazy default slashing protection records | implemented | low | S | disk, startup |
| [validator_client-101](#validator_client-101) | Per-validator slashing protection locks | not | low | L | cpu, memory, latency |
| [validator_client-102](#validator_client-102) | Narrow attesting-history lock scope | n/a | low |  | cpu, latency |
| [validator_client-103](#validator_client-103) **★** | Lock-free reads of signer state | partial | medium | M | cpu, latency |
| [validator_client-104](#validator_client-104) | Read-lock check before write lock | not | low | S | latency |
| [validator_client-105](#validator_client-105) | Separate duty locks per role | n/a | low |  | latency |
| [validator_client-106](#validator_client-106) | Take duty lock after waiting | n/a | low |  | latency |
| [validator_client-107](#validator_client-107) | Do not hold locks across beacon node I/O | implemented | low | S | latency |
| [validator_client-108](#validator_client-108) | Sign a slot's attestations in parallel | implemented | medium | S | cpu, latency |
| [validator_client-109](#validator_client-109) | Flatten attestation service task spawning | n/a | low |  | latency |
| [validator_client-110](#validator_client-110) | Parallel per-slot duty broadcast with sent cache | n/a | low |  | latency |
| [validator_client-111](#validator_client-111) | Parallel attestation aggregation across subnets | implemented | low | S | cpu, latency |
| [validator_client-112](#validator_client-112) | Skip aggregate fetch without aggregators | implemented | low | S | cpu, latency |
| [validator_client-113](#validator_client-113) | Fetch duty types and epochs concurrently | partial | low | S | latency |
| [validator_client-114](#validator_client-114) | Check validator roles in parallel | n/a | low |  | latency |
| [validator_client-115](#validator_client-115) | Parallel is-aggregator checks | partial | low | S | cpu, latency |
| [validator_client-116](#validator_client-116) | Share one HTTP client per remote signer | implemented | medium | S | memory |
| [validator_client-117](#validator_client-117) | Remote signer keep-alive below server timeout | implemented | low | S | latency |
| [validator_client-118](#validator_client-118) | Sign block header root, not full block | implemented | low | S | bandwidth |
| [validator_client-119](#validator_client-119) **★** | Throttle concurrent remote signer requests | partial | medium | S | latency, bandwidth |
| [validator_client-120](#validator_client-120) | Prioritize duty signing over registrations | not | low | S | cpu, latency |
| [validator_client-121](#validator_client-121) | Parallel broadcast to fallback nodes with timeout | implemented | low | S | latency |
| [validator_client-122](#validator_client-122) | Return on first successful beacon node | not | low | S | latency |
| [validator_client-123](#validator_client-123) | Per-call slot-fraction timeouts for failover | implemented | low | S | latency |
| [validator_client-124](#validator_client-124) | Primary beacon node first, fallback on error | implemented | low | S | latency |
| [validator_client-125](#validator_client-125) | Reduce readiness polling of failed nodes | not | low | S | cpu, bandwidth |
| [validator_client-126](#validator_client-126) | Targeted beacon node status checks | not | low | M | cpu, latency |
| [validator_client-127](#validator_client-127) | Poll next-epoch duties before boundary | implemented | low | S | latency |
| [validator_client-128](#validator_client-128) | Recompute duties only after reorg ancestor | implemented | low | S | cpu, latency |
| [validator_client-129](#validator_client-129) | Target roots in head event | not | low | M | cpu |
| [validator_client-130](#validator_client-130) | Skip redundant next-epoch duties request | n/a | low | S | latency, bandwidth |
| [validator_client-131](#validator_client-131) | Skip attestation data without duties | implemented | low | S | cpu, latency, bandwidth |
| [validator_client-132](#validator_client-132) | Skip duty requests with no active keys | implemented | low | S | cpu, bandwidth |
| [validator_client-133](#validator_client-133) | Skip empty validators query | n/a | low | S | cpu, bandwidth |
| [validator_client-134](#validator_client-134) | DVT selections once per epoch | implemented | low | S | cpu, latency, bandwidth |
| [validator_client-135](#validator_client-135) | Reuse duty data instead of extra requests | implemented | low | S | latency |
| [validator_client-136](#validator_client-136) | Reuse duty statuses for exit check | n/a | low | S | cpu, bandwidth |
| [validator_client-137](#validator_client-137) | Remove redundant head API call | n/a | low | S | latency |
| [validator_client-138](#validator_client-138) | Memoize genesis from beacon node | implemented | low | S | latency |
| [validator_client-139](#validator_client-139) | Fee recipient calls only for configured keys | implemented | low | S | latency, bandwidth |
| [validator_client-140](#validator_client-140) | No duplicate registration calls at startup | implemented | low | S | bandwidth, startup |
| [validator_client-141](#validator_client-141) | Prune registration cache for inactive keys | partial | low | S | memory |
| [validator_client-142](#validator_client-142) | Skip current-slot sync selection proofs | implemented | low | S | cpu |
| [validator_client-143](#validator_client-143) | Precompute own committee membership ahead | implemented | low | S | cpu, latency |
| [validator_client-144](#validator_client-144) | Staggered subnet subscriptions with retry | implemented | low | S | cpu, bandwidth |
| [validator_client-145](#validator_client-145) | Cache sync duties, skip doppelganger for inactive | implemented | low | S | cpu, bandwidth |
| [validator_client-146](#validator_client-146) | Doppelganger liveness only for due validators | not | low | S | bandwidth |
| [validator_client-147](#validator_client-147) | No-op sync duties without assignments | implemented | low | S | cpu, bandwidth |
| [validator_client-148](#validator_client-148) | Hash map index of local pubkeys | partial | low | S | cpu |
| [validator_client-149](#validator_client-149) | Map lookup for committee selections | implemented | low | S | cpu |
| [validator_client-150](#validator_client-150) | Fixed-size byte array as pubkey map key | implemented | low | S | cpu, memory |
| [validator_client-151](#validator_client-151) | Shared buffer for pubkey hex encoding | n/a | low |  | cpu, memory |
| [validator_client-152](#validator_client-152) | Single-allocation lock key construction | n/a | low |  | cpu, memory |
| [validator_client-153](#validator_client-153) | Preallocate target-epochs slice | n/a | low |  | memory |
| [validator_client-154](#validator_client-154) | Hoist registry scan out of per-key status | n/a | low |  | cpu |
| [validator_client-155](#validator_client-155) | Single-pass multi-key committee assignments | partial | low | S | cpu, memory, latency |
| [validator_client-156](#validator_client-156) | Use epoch committee cache for attestations | n/a | low |  | cpu |
| [validator_client-157](#validator_client-157) | Avoid state copies for selection proof serving | n/a | low | S | cpu, memory, latency |
| [validator_client-158](#validator_client-158) | Status from state for active validators | n/a | low |  | latency, startup |
| [validator_client-159](#validator_client-159) | No state regen for error logging | n/a | low | S | cpu |
| [validator_client-160](#validator_client-160) | VC-side slot timer for attestations | implemented | low | S | latency |
| [validator_client-161](#validator_client-161) | Skip stale duties when behind | implemented | low | S | cpu, latency |
| [validator_client-162](#validator_client-162) | Resolve non-positive sleeps immediately | n/a | low |  | cpu, latency |
| [validator_client-163](#validator_client-163) | Fully async performance tracker | n/a | low |  | cpu, latency |
| [validator_client-164](#validator_client-164) | Multithreaded validator API serving | n/a | low |  | latency |
| [validator_client-165](#validator_client-165) | Short-circuit no-op validator updates | implemented | low | S | cpu, latency |
| [validator_client-166](#validator_client-166) | Prune past-epoch duty maps | implemented | low | S | memory |
| [validator_client-167](#validator_client-167) | Replace sync duties per period | partial | low | S | memory |
| [validator_client-168](#validator_client-168) | Prepare hash-based signing keys off the signing path | n/a | low |  | cpu, latency |
| [validator_client-169](#validator_client-169) | Try SSZ on all beacon nodes before JSON fallback | implemented | low | S | latency |
| [validator_client-170](#validator_client-170) | One sync committee message per validator per slot | implemented | low | S | cpu, bandwidth |
| [validator_client-171](#validator_client-171) | One sync contribution per subcommittee | implemented | low | S | bandwidth, cpu |
| [validator_client-172](#validator_client-172) | Publish sync contribution only if own vote included | not | low | S | bandwidth, cpu |
| [validator_client-173](#validator_client-173) | Use validator count endpoint instead of full list | n/a | low |  | latency, cpu, memory, bandwidth |
| [validator_client-174](#validator_client-174) | Beacon node readiness stream instead of sync polling | n/a | low |  | startup, latency |
| [validator_client-175](#validator_client-175) | Stream duties from beacon node to validator client | n/a | low |  | latency |
| [validator_client-176](#validator_client-176) | Map entry API for single lookup | implemented | low | S | cpu |
| [validator_client-177](#validator_client-177) | One proposer duty query per slot for all validators | implemented | low | S | cpu, latency |
| [validator_client-178](#validator_client-178) | Precompute RANDAO reveal before proposal slot | not | low | S | latency |
| [validator_client-179](#validator_client-179) | Run slashing-protection check once, not in two layers | implemented | low | S | cpu, disk |
| [validator_client-180](#validator_client-180) | Drop redundant zero-root check in slashing protection | n/a | low |  | cpu |
| [validator_client-181](#validator_client-181) | Retry only rejected builder preference entries | partial | low | S | bandwidth |
| [validator_client-182](#validator_client-182) | Run BLS signing in blocking tasks | implemented | medium | S | latency, cpu |
| [validator_client-183](#validator_client-183) | One shared slashing database for all validators | implemented | low | S | disk, startup |
| [validator_client-184](#validator_client-184) | Single unified block production endpoint | implemented | low | S | latency, bandwidth |
| [validator_client-185](#validator_client-185) | Build single-attestation directly | implemented | low | S | cpu |
| [validator_client-186](#validator_client-186) | Stop deprecated registrations after replacing fork | implemented | low | S | bandwidth |

★ actionable. Click an id for the full record.

## Ideas

<a id="validator_client-001"></a>
<details>
<summary><b>validator_client-001</b> Look up validator statuses via POST body, not batched GET — <i>not · low · S · bandwidth, cpu, latency</i></summary>

**Idea.** In the validator client, query the beacon node for validator statuses/indices of many pubkeys with one POST request carrying the ids in the body, instead of many GET requests chunked to stay under URL length limits. Fewer round trips, and the beacon node filters its validator set once.

**Gap in Lighthouse.** Index discovery queries one pubkey per GET. Add a batched POST /eth/v1/beacon/states/head/validators with ids body to eth2 client and use it in poll_validator_indices for all unknown pubkeys.

**Impact.** Only startup and new-key discovery; saves N requests for N unregistered keys, minor.

**Best measured result.** None (pr:lodestar#6897)

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/duties_service.rs:945-975`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L945-L975) poll_validator_indices does one get_beacon_states_validator_id GET per unknown pubkey
- grep post_beacon_states_validators in validator_client: no hits

**Sources.** [lodestar#6897](https://github.com/ChainSafe/lodestar/pull/6897), [teku#7786](https://github.com/Consensys-Incorporated/teku/pull/7786)

</details>


<a id="validator_client-002"></a>
<details>
<summary><b>validator_client-002</b> Batch pubkey-to-index and status lookups in large batches — <i>not · low · S · latency, bandwidth, startup</i></summary>

**Idea.** Resolve validator indices and statuses for all local keys with batched beacon API requests of large size (50-64+ pubkeys, or all at once, with bounded concurrency) instead of one request per validator, small batches of 10, or fetching the full validator set. Cuts round trips and BN load at startup and per epoch with many keys.

**Gap in Lighthouse.** Lookups are serial one-per-pubkey rather than batched. Batch unknown pubkeys into POST requests of large size in poll_validator_indices.

**Impact.** Cuts startup round trips with many keys (thousands of sequential requests); one-off cost.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/duties_service.rs:945-975`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L945-L975) per-pubkey GET, serial loop

**Sources.** [lodestar#2730](https://github.com/ChainSafe/lodestar/pull/2730), [teku#2947](https://github.com/Consensys-Incorporated/teku/pull/2947), [lodestar#2234](https://github.com/ChainSafe/lodestar/pull/2234), [teku#3379](https://github.com/Consensys-Incorporated/teku/pull/3379), [lodestar#5743](https://github.com/ChainSafe/lodestar/pull/5743), [teku#4306](https://github.com/Consensys-Incorporated/teku/pull/4306)

</details>


<a id="validator_client-003"></a>
<details>
<summary><b>validator_client-003</b> Batch validator balance/performance queries — <i>n/a · low · S · latency, bandwidth</i></summary>

**Idea.** Fetch balances/performance for all local validators in one request instead of one RPC per validator.

**Gap in Lighthouse.** The Lighthouse VC does not query per-validator balances or performance; it fetches duties in batch per epoch, so there is no per-validator RPC loop to batch.

**Impact.** None.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/duties_service.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs): duties and indices fetched in batch endpoints
- grep for validator balances in validator_client returned nothing

**Sources.** [prysm#3520](https://github.com/OffchainLabs/prysm/pull/3520)

</details>


<a id="validator_client-004"></a>
<details>
<summary><b>validator_client-004</b> Subscribe to head event stream instead of polling — <i>implemented · medium · S · latency, bandwidth, cpu</i></summary>

**Idea.** Have the validator client subscribe to the beacon node SSE event stream (with reconnect) and cache head slot/root, instead of polling the head block every slot or second. Removes per-slot HTTP requests and learns of heads sooner.

**Impact.** Already realised: head learned via SSE, no per-slot head polling.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/beacon_node_fallback/src/beacon_head_monitor.rs:136`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/beacon_node_fallback/src/beacon_head_monitor.rs#L136) poll_head_event_from_beacon_nodes subscribes to SSE head on all BNs
- [`validator_client/beacon_node_fallback/src/beacon_head_monitor.rs:90`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/beacon_node_fallback/src/beacon_head_monitor.rs#L90) BeaconHeadCache per-BN head cache
- [`validator_client/beacon_node_fallback/src/lib.rs:85-95`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/beacon_node_fallback/src/lib.rs#L85-L95) monitor restarted on stream error (reconnect)
- [`validator_client/src/config.rs:143`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/src/config.rs#L143) enable_beacon_head_monitor defaults true

**Skeptic check.** Verified SSE head subscription with per-BN cache, optimistic-head filtering and restart-on-error loop; on by default. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#13453](https://github.com/OffchainLabs/prysm/pull/13453), [prysm#13354](https://github.com/OffchainLabs/prysm/pull/13354), [lodestar#2824](https://github.com/ChainSafe/lodestar/pull/2824)

</details>


<a id="validator_client-005"></a>
<details>
<summary><b>validator_client-005</b> SSZ encoding for VC-BN block traffic — <i>partial · medium · S · bandwidth, cpu, latency</i></summary>

**Idea.** Request unsigned blocks and submit signed blocks (and other large objects) between validator client and beacon node as SSZ octet-stream instead of JSON, with JSON fallback chosen by content type and remembered after a 406. SSZ is smaller and cheaper to encode/decode, which matters for large blob-carrying blocks.

**Gap in Lighthouse.** Blocks (and Gloas payload attestations, proposer/builder preferences) go SSZ with a per-call JSON fallback, but no per-BN memory of a 406/failed SSZ (every proposal retries SSZ on all nodes first), and attestation data, aggregates, attestation/aggregate POSTs and sync contributions stay JSON even where the eth2 client already has SSZ methods.

**Impact.** Small: avoids one failed SSZ pass against non-SSZ BNs and trims JSON encode/decode on attestation traffic; negligible on localhost.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/block_service.rs:787`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/block_service.rs#L787) SSZ v3 block GET, JSON second pass at 805
- [`validator_client/validator_services/src/block_service.rs:707`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/block_service.rs#L707) SSZ v4 (Gloas) block production
- [`validator_client/validator_services/src/block_service.rs:1110`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/block_service.rs#L1110) post_beacon_blocks_v2_ssz / 1124 post_beacon_blinded_blocks_v2_ssz
- [`validator_client/validator_services/src/proposer_preferences_service.rs:215`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/proposer_preferences_service.rs#L215) SSZ with JSON fallback
- [`validator_client/validator_services/src/attestation_service.rs:284`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/attestation_service.rs#L284) get_validator_attestation_data (JSON) although [`common/eth2/src/lib.rs:3794`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/eth2/src/lib.rs#L3794) get_validator_attestation_data_ssz exists
- [`validator_client/validator_services/src/attestation_service.rs:667`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/attestation_service.rs#L667) JSON aggregate GET although [`common/eth2/src/lib.rs:3976`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/eth2/src/lib.rs#L3976) get_validator_aggregate_attestation_v2_ssz exists
- [`validator_client/validator_services/src/attestation_service.rs:585`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/attestation_service.rs#L585) JSON attestation POST

**Second check.** Searched the VC for any content-type/SSZ-support cache (none) and checked which eth2 SSZ client methods are unused by the VC (attestation data and aggregate SSZ GETs exist but are not called).

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [teku#6575](https://github.com/Consensys-Incorporated/teku/pull/6575), [lighthouse#6523](https://github.com/sigp/lighthouse/pull/6523), [prysm#15645](https://github.com/OffchainLabs/prysm/pull/15645), [teku#5517](https://github.com/Consensys-Incorporated/teku/pull/5517), [nimbus#4999](https://github.com/status-im/nimbus-eth2/pull/4999), [teku#5513](https://github.com/Consensys-Incorporated/teku/pull/5513), [prysm#17355](https://github.com/OffchainLabs/prysm/pull/17355), [prysm#17256](https://github.com/OffchainLabs/prysm/pull/17256)

</details>


<a id="validator_client-006"></a>
<details>
<summary><b>validator_client-006</b> Trigger attestation fetch on head event, not block event — <i>implemented · low · S · latency</i></summary>

**Idea.** When reacting to beacon node events, start attestation data fetch on the head event (after fork choice picks the head) rather than the block event, so data matches the head and reorgs are handled sooner.

**Impact.** Attestation production starts on the head event with a block-root check; falls back to the deadline.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/beacon_node_fallback/src/beacon_head_monitor.rs:164`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/beacon_node_fallback/src/beacon_head_monitor.rs#L164) get_events(&amp;[EventTopic::Head])
- [`validator_client/validator_services/src/attestation_service.rs:273-312`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/attestation_service.rs#L273-L312) fetch attestation data from the BN that sent the head, check beacon_block_root, else wait for deadline
- [`validator_client/src/cli.rs:511`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/src/cli.rs#L511) disable_beacon_head_monitor (enabled by default)

**Skeptic check.** Verified the head monitor subscribes to the Head topic (not Block) and is on by default. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#8875](https://github.com/status-im/nimbus-eth2/pull/8875), [lighthouse#2520](https://github.com/sigp/lighthouse/pull/2520)

</details>


<a id="validator_client-007"></a>
<details>
<summary><b>validator_client-007</b> Attest as soon as the slot&#x27;s head block arrives — <i>implemented · medium · S · latency</i></summary>

**Idea.** Produce and publish attestations as soon as the block for the current slot is imported and becomes head (head/block event) instead of always waiting for the fixed 1/3-slot deadline or an extra delay, keeping the deadline as fallback. Attestations propagate earlier in the slot.

**Impact.** Already realised.

**Best measured result.** None (pr:prysm#4791)

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/attestation_service.rs:212`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/attestation_service.rs#L212) head_event_or_deadline waits for current-slot head event or 1/3-slot deadline
- [`validator_client/validator_services/src/attestation_service.rs:273-310`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/attestation_service.rs#L273-L310) fetches attestation data from the BN that sent the head, checks root, falls back to deadline + first_success
- [`validator_client/beacon_node_fallback/src/beacon_head_monitor.rs:64`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/beacon_node_fallback/src/beacon_head_monitor.rs#L64) head_event_or_deadline

**Skeptic check.** Confirmed attestation production triggers on the current-slot non-optimistic head event with deadline fallback; matches the idea. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#17243](https://github.com/OffchainLabs/prysm/pull/17243), [grandine#955](https://github.com/grandinetech/grandine/pull/955), [lodestar@50f12944f](https://github.com/ChainSafe/lodestar/commit/50f12944fe91), [prysm#4791](https://github.com/OffchainLabs/prysm/pull/4791), [prysm#8827](https://github.com/OffchainLabs/prysm/pull/8827), [teku#2432](https://github.com/Consensys-Incorporated/teku/pull/2432), [grandine@f08b0a49d](https://github.com/grandinetech/grandine/commit/f08b0a49da7f), [prysm#15410](https://github.com/OffchainLabs/prysm/pull/15410), [lodestar#3397](https://github.com/ChainSafe/lodestar/pull/3397), [lighthouse#7892](https://github.com/sigp/lighthouse/pull/7892), [lodestar#4788](https://github.com/ChainSafe/lodestar/pull/4788), [grandine@2506dfffd](https://github.com/grandinetech/grandine/commit/2506dfffd2c6)

</details>


<a id="validator_client-008"></a>
<details>
<summary><b>validator_client-008</b> Request blinded blocks from the beacon node — <i>partial · medium · S · bandwidth, latency</i></summary>

**Idea.** Let the validator client request blinded blocks (also for locally built payloads) so the full execution payload does not travel between beacon node and validator client; the beacon node reassembles it on publish.

**Gap in Lighthouse.** The BN side is complete: GET validator/blinded_blocks blinds locally built payloads, caches them in the EL payload cache, and POST blinded_blocks reassembles from that cache. Only the VC is missing: it has no option to call get_validator_blinded_blocks(_ssz) for local proposals, so v3 sends the full payload. A VC flag that calls the blinded endpoint and posts via the existing blinded SSZ path would close it (pre-Gloas only).

**Impact.** Small: saves the payload+blobs transfer VC&lt;-&gt;BN per proposal; matters only for remote BNs, moot after Gloas.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/produce_block.rs:308`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/produce_block.rs#L308) produce_blinded_block_v2 uses BlockProductionVersion::BlindedV2
- [`beacon_node/execution_layer/src/lib.rs:1003`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/lib.rs#L1003) BlindedV2 path; 1033 blinds a local Full payload into Blinded
- [`beacon_node/execution_layer/src/lib.rs:651`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/execution_layer/src/lib.rs#L651) cache_payload / 1319 get_full_payload_caching stores the local payload
- [`beacon_node/http_api/src/publish_blocks.rs:714`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/publish_blocks.rs#L714) reconstruct_block unblinds from el.get_payload_by_root (local payload cache)
- [`beacon_node/http_api/src/lib.rs:2727`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L2727) GET validator/blinded_blocks route
- [`common/eth2/src/lib.rs:3738`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/eth2/src/lib.rs#L3738) get_validator_blinded_blocks_ssz client method
- [`validator_client/validator_services/src/block_service.rs:794`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/block_service.rs#L794) VC only calls v3 (or v4) produce, never the blinded endpoint

**Second check.** The earlier review looked only at the VC v3 flow; the BN still has the blinded-v2 production path that blinds local payloads and reassembles them from execution_layer payload_cache on publish, and the eth2 client already exposes the method.

**Verdict history.** not (checked) → partial (refuted)

**Sources.** [teku#5030](https://github.com/Consensys-Incorporated/teku/pull/5030), [lodestar#6227](https://github.com/ChainSafe/lodestar/pull/6227)

</details>


<a id="validator_client-009"></a>
<details>
<summary><b>validator_client-009</b> Multi-BN: attest on first perfect attestation data — <i>not · low · M · latency</i></summary>

**Idea.** With several beacon nodes, score attestation data responses and attest as soon as one response is perfectly scored (data slot equals head slot, target=source+1) instead of waiting for all nodes.

**Gap in Lighthouse.** With multiple BNs, only the BN that emitted the head event is queried early; others are tried sequentially at the deadline. Racing all BNs and accepting the first response with slot==head slot and target==source+1 would need a new scored race in attestation_service.rs and beacon_node_fallback.

**Impact.** Reduces attestation latency only in multi-BN setups when the first-choice BN lags; small for the typical single-BN node.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/beacon_node_fallback/src/lib.rs:717`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/beacon_node_fallback/src/lib.rs#L717) first_success awaits candidate futures sequentially in health order
- [`validator_client/validator_services/src/attestation_service.rs:326-338`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/attestation_service.rs#L326-L338) fallback path uses first_success after waiting for the deadline

**Sources.** [nimbus#5101](https://github.com/status-im/nimbus-eth2/pull/5101), [prysm#17552](https://github.com/OffchainLabs/prysm/pull/17552)

</details>


<a id="validator_client-010"></a>
<details>
<summary><b>validator_client-010</b> Sync committee messages as soon as block seen — <i>implemented · low · S · latency</i></summary>

**Idea.** Sign and publish sync committee messages as soon as the slot's block/head event arrives instead of waiting for the 1/3-slot timer, avoiding the busiest moment.

**Impact.** Already realised.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/sync_committee_service.rs:146-153`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/sync_committee_service.rs#L146-L153) head_event_or_deadline triggers sync messages on head event
- [`validator_client/validator_services/src/sync_committee_service.rs:244-249`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/sync_committee_service.rs#L244-L249) uses head event root directly, skipping a block-root fetch

**Skeptic check.** Sync committee messages are signed on the head event with deadline fallback and reuse the event root. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#9675](https://github.com/sigp/lighthouse/pull/9675), [lodestar#4615](https://github.com/ChainSafe/lodestar/pull/4615), [lodestar#4667](https://github.com/ChainSafe/lodestar/pull/4667)

</details>


<a id="validator_client-011"></a>
<details>
<summary><b>validator_client-011</b> Payload timeliness votes on payload-available event — <i>partial · medium · S · latency, cpu</i></summary>

**Idea.** Have the beacon node push payload-available events to validator clients and cast PTC payload attestations as soon as the payload envelope and data columns are seen (deadline as fallback), signing one payload attestation per validator rather than per committee position.

**Gap in Lighthouse.** The BN emits ExecutionPayloadAvailable only from the envelope import path, not when the custody data columns complete later (pending_payload_cache / data column import). When columns arrive after the envelope, the VC's early attempt fails on blob_data_available=false and spawn_payload_attestation_tasks falls back to the deadline instead of waiting for availability. Missing: emit the event from the column-availability path and let the VC retry on a subsequent event.

**Impact.** PTC votes fall back to the deadline whenever columns trail the envelope, losing most of the early-vote gain on blob-carrying slots.

**Best measured result.** PTC vote at 4.51s vs 0.23s of a 6s slot (pr:prysm#17500)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/payload_envelope_verification/import.rs:402-412`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_envelope_verification/import.rs#L402-L412) ExecutionPayloadAvailable emitted only at envelope import, with TODO to also emit from DA resolution
- [`beacon_node/beacon_chain/src/pending_payload_cache/mod.rs:149-161`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/pending_payload_cache/mod.rs#L149-L161) blob data availability tracked independently of envelope import
- [`validator_client/validator_services/src/payload_attestation_service.rs:288-326`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/payload_attestation_service.rs#L288-L326) early path requires payload_present and blob_data_available
- [`validator_client/validator_services/src/payload_attestation_service.rs:173-188`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/payload_attestation_service.rs#L173-L188) early failure sleeps to deadline, never re-waits for a later event
- [`beacon_node/beacon_chain/src/beacon_chain.rs:1771`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1771) compute_ptc_duties yields one PtcDuty per validator

**Skeptic check.** Verified the SSE subscription, early trigger, per-validator signing; but the event is emitted at envelope import only (explicit TODO), so 'as soon as envelope and data columns are seen' holds only when columns already arrived. Earlier evidence missed the BN side.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [grandine@d70201c05](https://github.com/grandinetech/grandine/commit/d70201c053ff), [lighthouse#9434](https://github.com/sigp/lighthouse/pull/9434), [nimbus#9054](https://github.com/status-im/nimbus-eth2/pull/9054), [prysm#17500](https://github.com/OffchainLabs/prysm/pull/17500), [prysm#16906](https://github.com/OffchainLabs/prysm/pull/16906)

</details>


<a id="validator_client-012"></a>
<details>
<summary><b>validator_client-012</b> Slim duties response without full committee lists — <i>implemented · low · S · bandwidth, cpu, latency</i></summary>

**Idea.** Have the validator client get committee length and its committee index from the duties response (or a lighter duties endpoint) instead of fetching full committee member lists or a separate committees API call each epoch, and do not re-check validators missing from state. Smaller responses and fewer state lookups.

**Impact.** Already realised.

**Best measured result.** saves 100-400ms in some cases; similar in the happy case (pr:prysm#15445)

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/duties_service.rs:1448`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L1448) post_validator_duties_attester is the only attester duties call; no committees endpoint used
- [`common/eth2/src/types.rs:865`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/eth2/src/types.rs#L865) AttesterData carries committee_length/index/validator_committee_index
- [`validator_client/validator_services/src/duties_service.rs:936-948`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L936-L948) unknown validators re-queried at most once per epoch

**Skeptic check.** VC never fetches committee lists; committee data comes from the duties response and unknown-index lookups are throttled. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#15380](https://github.com/OffchainLabs/prysm/pull/15380), [prysm#15039](https://github.com/OffchainLabs/prysm/pull/15039), [prysm#15273](https://github.com/OffchainLabs/prysm/pull/15273), [prysm#15445](https://github.com/OffchainLabs/prysm/pull/15445)

</details>


<a id="validator_client-013"></a>
<details>
<summary><b>validator_client-013</b> Aggregate/subscribe only for actual duties — <i>implemented · low · S · cpu, bandwidth</i></summary>

**Idea.** Subscribe to subnets, collect and aggregate attestations only for committees where attached validators actually have duties, rather than every epoch for all, reducing beacon node load.

**Impact.** Subnet subscriptions and aggregation only happen for real duties.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/duties_service.rs:1135-1159`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L1135-L1159) subscriptions built only from local validators' attester duties, is_aggregator from selection_proof, gated by should_send_subscription_at
- [`validator_client/validator_services/src/duties_service.rs:147`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L147) make_selection_proof per duty

**Skeptic check.** Verified the subscriptions come from the attester duty map and are sent at the scheduled subscription_slots offsets, not every slot. The earlier evidence was right, but it was wrong to say they are resent every slot.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#2037](https://github.com/ChainSafe/lodestar/pull/2037)

</details>


<a id="validator_client-014"></a>
<details>
<summary><b>validator_client-014</b> Do not fetch all validators for activation-queue logging — <i>implemented · low · S · latency, bandwidth, cpu</i></summary>

**Idea.** Avoid fetching the full validator set or total validator count from the beacon API just to log activation queue position; these calls are very expensive (15-20s).

**Impact.** Already realised.

**Best measured result.** None (pr:prysm#12471)

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/notifier_service.rs:108`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/notifier_service.rs#L108) total_validator_count from local duties service
- [`validator_client/validator_services/src/duties_service.rs:962`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L962) only per-pubkey get_beacon_states_validator_id lookups

**Skeptic check.** No get/post_beacon_states_validators call exists anywhere in validator_client; the notifier uses local counts. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#12471](https://github.com/OffchainLabs/prysm/pull/12471), [prysm#14600](https://github.com/OffchainLabs/prysm/pull/14600)

</details>


<a id="validator_client-015"></a>
<details>
<summary><b>validator_client-015</b> Block metrics via historic roots, not disk block loads — <i>n/a · low · S · disk, cpu</i></summary>

**Idea.** For block production metrics, store only slot and root and compare with the head state's historic block roots instead of loading full canonical blocks from disk.

**Gap in Lighthouse.** The VC has no database and does not load canonical blocks for metrics, so the Teku optimization has no counterpart.

**Impact.** None.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/block_service.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/block_service.rs): no block-metrics loading of canonical blocks from disk
- validator_client has no store access

**Sources.** [teku#3984](https://github.com/Consensys-Incorporated/teku/pull/3984)

</details>


<a id="validator_client-016"></a>
<details>
<summary><b>validator_client-016</b> Allocation-free auth token check — <i>not · low · S · cpu, memory</i></summary>

**Idea.** In API auth header checks, use prefix checks and slicing and compare lengths before constant-time compare, instead of splitting strings, to avoid per-request allocations.

**Gap in Lighthouse.** Auth filter clones the expected Vec&lt;String&gt; and allocates the header String per request; could borrow via Arc and compare slices (constant-time). Change authorization_header_filter in api_secret.rs.

**Impact.** Saves two or three small allocations per VC HTTP API call; VC API is low-traffic, so unmeasurable.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/http_api/src/api_secret.rs:104`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/http_api/src/api_secret.rs#L104) builds Basic/Bearer strings once at startup
- [`validator_client/http_api/src/api_secret.rs:113`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/http_api/src/api_secret.rs#L113) filter does expected.clone() (Vec&lt;String&gt;) per request, takes header as owned String, then Vec::contains (non-constant-time compare)

**Sources.** [prysm#15793](https://github.com/OffchainLabs/prysm/pull/15793)

</details>


<a id="validator_client-017"></a>
<details>
<summary><b>validator_client-017</b> Skip unneeded committee-size fetches in performance tracker — <i>n/a · low · S · cpu, bandwidth</i></summary>

**Idea.** In the validator performance tracker, skip fetching committee sizes when not needed (pre-Electra) and look them up for the correct slot.

**Impact.** Lighthouse VC has no validator performance tracker, so nothing to skip.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/lib.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/lib.rs) lists services: no performance tracker
- grep committee_size/performance in validator_client finds only a CLI flag at src/cli.rs:101

**Sources.** [teku#9012](https://github.com/Consensys-Incorporated/teku/pull/9012)

</details>


<a id="validator_client-018"></a>
<details>
<summary><b>validator_client-018</b> Prefetch next-epoch duties off the critical path — <i>partial · low · S · latency</i></summary>

**Idea.** Fetch next-epoch duties in the background mid-epoch and promote cached next-epoch duties to current at the boundary, refetching only failed duty types; never await the next-epoch fetch before slot-critical work like block notification. Slot-0 proposals no longer wait on a duties fetch.

**Gap in Lighthouse.** Proposer path still awaits next-epoch proposer fetch before the 'additional proposers' notification (upstream #9952 is still open); attester next-epoch duties are refetched inline rather than cached and promoted. Move the current_epoch+1 fetch in poll_beacon_proposers into a spawned task, and cache next-epoch attester duties and promote at the boundary.

**Impact.** Slot-0 proposals whose duty only arrives from the BN poll start up to one next-epoch request earlier (hundreds of ms in bad cases); no effect on node CPU.

**Best measured result.** None (pr:prysm#17268)

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/duties_service.rs:739-751`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L739-L751) attester polling runs in its own spawned task
- [`validator_client/validator_services/src/duties_service.rs:1092`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L1092) next-epoch attester duties re-fetched every poll, no promotion cache
- [`validator_client/validator_services/src/duties_service.rs:1844-1870`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L1844-L1870) proposer poll notifies from cache first, then awaits current and next epoch fetch in a loop

**Sources.** [lighthouse#9952](https://github.com/sigp/lighthouse/pull/9952), [prysm#17268](https://github.com/OffchainLabs/prysm/pull/17268), [prysm#17036](https://github.com/OffchainLabs/prysm/pull/17036)

</details>


<a id="validator_client-019"></a>
<details>
<summary><b>validator_client-019</b> Batch attestation submission per slot — <i>implemented · medium · S · latency, cpu, bandwidth</i></summary>

**Idea.** Sign all attestations for a slot first, then submit them to the beacon node in one batched request instead of one HTTP request per validator or committee, ideally by default. Cuts round trips and beacon node load.

**Impact.** Already realised.

**Best measured result.** None (pr:prysm#17225)

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/lighthouse_validator_store/src/lib.rs:1022-1088`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/lighthouse_validator_store/src/lib.rs#L1022-L1088) sign_attestations signs all concurrently in a single stream::once batch
- [`validator_client/validator_services/src/attestation_service.rs:568-590`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/attestation_service.rs#L568-L590) one post_beacon_pool_attestations_v2 per batch
- [`validator_client/validator_services/src/attestation_service.rs:249-251`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/attestation_service.rs#L249-L251) one attestation task for all duties of the slot post-Electra

**Skeptic check.** All attestations of the slot are signed together and posted in one request by default. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#7874](https://github.com/status-im/nimbus-eth2/pull/7874), [lodestar#3923](https://github.com/ChainSafe/lodestar/pull/3923), [prysm#17225](https://github.com/OffchainLabs/prysm/pull/17225), [teku#4252](https://github.com/Consensys-Incorporated/teku/pull/4252), [teku#4803](https://github.com/Consensys-Incorporated/teku/pull/4803), [prysm#13809](https://github.com/OffchainLabs/prysm/pull/13809), [teku#4515](https://github.com/Consensys-Incorporated/teku/pull/4515), [lodestar#2416](https://github.com/ChainSafe/lodestar/pull/2416)

</details>


<a id="validator_client-020"></a>
<details>
<summary><b>validator_client-020</b> Batch aggregate-and-proof submission — <i>implemented · low · S · latency, bandwidth</i></summary>

**Idea.** Submit all aggregate-and-proofs for a slot to the beacon node in one batch request with per-item error reporting.

**Impact.** One POST per slot (per attestation-data group) with all aggregates.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/attestation_service.rs:720-745`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/attestation_service.rs#L720-L745) signs all aggregates for the slot and posts the batch slice via post_validator_aggregate_and_proof_v1/v2
- [`validator_client/lighthouse_validator_store/src/lib.rs:1199-1226`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/lighthouse_validator_store/src/lib.rs#L1199-L1226) sign_aggregate_and_proofs returns stream::once (a single batch)

**Skeptic check.** Verified the local store yields one batch, so a single request carries all aggregates for that data. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#4281](https://github.com/Consensys-Incorporated/teku/pull/4281)

</details>


<a id="validator_client-021"></a>
<details>
<summary><b>validator_client-021</b> Batch slashing-protection checks into one transaction — <i>implemented · medium · S · latency, disk, cpu</i></summary>

**Idea.** Sign attestations for a slot first, then check and register them all in the slashing-protection DB in one batched transaction (or a queue flushed periodically), rather than one check-and-write transaction per validator. One fsync per batch and no write-lock contention.

**Impact.** Already done: one exclusive SQLite transaction and one commit per slot for all attestations.

**Best measured result.** None (pr:nimbus#5604)

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/lighthouse_validator_store/src/lib.rs:1027`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/lighthouse_validator_store/src/lib.rs#L1027) sign_attestations signs all attestations of the slot concurrently first
- [`validator_client/lighthouse_validator_store/src/lib.rs:1082`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/lighthouse_validator_store/src/lib.rs#L1082) one spawn_blocking slashing_protect_attestations for the whole batch
- [`validator_client/lighthouse_validator_store/src/lib.rs:670`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/lighthouse_validator_store/src/lib.rs#L670) check_and_insert_attestations called once with all attestations
- [`validator_client/slashing_protection/src/slashing_database.rs:652`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/slashing_protection/src/slashing_database.rs#L652) check_and_insert_attestations: one Exclusive transaction, one commit
- [`validator_client/validator_services/src/attestation_service.rs:554`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/attestation_service.rs#L554) all duties of the slot passed in one sign_attestations call

**Skeptic check.** Verified the sign-then-batch-check flow: all duties for the slot go into one sign_attestations stream, and one Exclusive transaction checks and inserts them all. The earlier evidence was correct. Blocks are one per proposal, so no batching is needed there.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#5695](https://github.com/OffchainLabs/prysm/pull/5695), [lighthouse#8516](https://github.com/sigp/lighthouse/pull/8516), [lighthouse#6219](https://github.com/sigp/lighthouse/pull/6219), [nimbus#5604](https://github.com/status-im/nimbus-eth2/pull/5604), [prysm#8243](https://github.com/OffchainLabs/prysm/pull/8243)

</details>


<a id="validator_client-022"></a>
<details>
<summary><b>validator_client-022</b> Fewer DB transactions per slashing-protection check — <i>partial · low · M · latency, disk</i></summary>

**Idea.** Reduce DB round trips per slashing-protection check: combine check and register, and write the record plus lowest signed source/target updates in one transaction per signing, caching internal ids and relying on unique indexes for duplicates. Shortens write-lock hold time per signature.

**Gap in Lighthouse.** Attestations are batched per transaction and check+insert share a txn, but each item does a validator-id SELECT plus several check SELECTs and no id cache; block proposals are one txn each. Cache validator ids in SlashingDatabase and fold check queries (check_attestation, check_block_proposal).

**Impact.** Shorter write-lock hold per signing batch; matters mainly for VCs with thousands of keys (hundreds of ms per slot at most).

**Best measured result.** None (pr:prysm#8087)

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/slashing_protection/src/slashing_database.rs:652`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/slashing_protection/src/slashing_database.rs#L652) check_and_insert_attestations does a whole batch in one exclusive transaction
- [`validator_client/slashing_protection/src/slashing_database.rs:298`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/slashing_protection/src/slashing_database.rs#L298) get_validator_id_in_txn re-queries the validator row per check
- [`validator_client/slashing_protection/src/slashing_database.rs:732`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/slashing_protection/src/slashing_database.rs#L732) check then insert in the same txn
- [`validator_client/slashing_protection/src/slashing_database.rs:177`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/slashing_protection/src/slashing_database.rs#L177) EXCLUSIVE locking mode

**Sources.** [prysm#8087](https://github.com/OffchainLabs/prysm/pull/8087), [prysm#8100](https://github.com/OffchainLabs/prysm/pull/8100), [nimbus#2528](https://github.com/status-im/nimbus-eth2/pull/2528), [prysm#8196](https://github.com/OffchainLabs/prysm/pull/8196)

</details>


<a id="validator_client-023"></a>
<details>
<summary><b>validator_client-023</b> Bounded batches for builder registrations — <i>implemented · low · S · bandwidth, latency</i></summary>

**Idea.** Send validator registrations to the builder API/relays in bounded, configurable batches (e.g. 200-1000) rather than one huge request, and skip a new run while the previous is in progress, so requests do not time out or hit size limits.

**Impact.** Already done.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/preparation_service.rs:449`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/preparation_service.rs#L449) signed.chunks(validator_registration_batch_size)
- [`validator_client/src/config.rs:145`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/src/config.rs#L145) default batch size 500, :400 rejects 0
- [`validator_client/validator_services/src/preparation_service.rs:224`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/preparation_service.rs#L224) serial loop awaits register_validators before sleeping, so runs cannot overlap
- [`beacon_node/http_api/src/validator/mod.rs:813`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validator/mod.rs#L813) BN forwards each VC batch to the builder as is, so the relay request is bounded too

**Skeptic check.** Confirmed the VC chunks the signed registrations into configurable batches (default 500). The single loop cannot start a new run while one is in progress. The BN forwards each batch unchanged, so the bound also reaches the relay. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#13178](https://github.com/OffchainLabs/prysm/pull/13178), [prysm#14981](https://github.com/OffchainLabs/prysm/pull/14981), [teku#5829](https://github.com/Consensys-Incorporated/teku/pull/5829), [nimbus#4364](https://github.com/status-im/nimbus-eth2/pull/4364), [lighthouse#4399](https://github.com/sigp/lighthouse/pull/4399)

</details>


<a id="validator_client-024"></a>
<details>
<summary><b>validator_client-024</b> Spread attestation signing across the epoch — <i>n/a · low · S · cpu, latency</i></summary>

**Idea.** When many validators have duties, sign attestation duties in slot-spread batches with small delays instead of all at the epoch start, avoiding CPU/signing bursts.

**Impact.** Lighthouse already signs per slot (at 1/3 slot), not at epoch start, and local BLS signing is cheap; there is no epoch-start burst to spread.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/attestation_service.rs:322`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/attestation_service.rs#L322) and :463 sleep_until slot-relative instants
- attestation_service.rs duties are processed per slot, signing a single batch per slot

**Sources.** [teku#9374](https://github.com/Consensys-Incorporated/teku/pull/9374)

</details>


<a id="validator_client-025"></a>
<details>
<summary><b>validator_client-025</b> Decrypt validator keystores in parallel at startup — <i>not · low · S · startup, cpu</i></summary>

**Idea.** At validator client startup, read and run the keystore KDF decryption for each key in parallel across CPU cores (thread pool) instead of serially on the main thread. Each decryption is independent and CPU-heavy, so wall-clock load time drops roughly by core count.

**Gap in Lighthouse.** Cold start (no key cache, or after new keys) decrypts keystores one at a time. Run the decrypt step of from_definition for all enabled LocalKeystore defs concurrently (rayon par_iter or FuturesUnordered of spawn_blocking) in update_validators, then insert results serially.

**Impact.** Only first start or new-key import with many keys: wall-clock load drops roughly by core count (10k keys: hour to ~15 min per upstream estimate). Zero effect on steady state.

**Best measured result.** 10000 keys: about 1 hour serial vs 15 minutes with 8 cores (pr:lighthouse#1699)

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/initialized_validators/src/lib.rs:1262-1283`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/initialized_validators/src/lib.rs#L1262-L1283) serial for loop awaiting InitializedValidator::from_definition per key
- [`validator_client/initialized_validators/src/lib.rs:260`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/initialized_validators/src/lib.rs#L260) spawn_blocking per key but awaited immediately
- [`validator_client/initialized_validators/src/key_cache.rs:187`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/initialized_validators/src/key_cache.rs#L187) key cache decrypts one blob so restarts skip KDF

**Sources.** [lodestar#5274](https://github.com/ChainSafe/lodestar/pull/5274), [grandine@fd640b3d2](https://github.com/grandinetech/grandine/commit/fd640b3d23bc), [grandine#252](https://github.com/grandinetech/grandine/pull/252), [lodestar#5623](https://github.com/ChainSafe/lodestar/pull/5623), [lighthouse#1699](https://github.com/sigp/lighthouse/pull/1699), [lodestar#5357](https://github.com/ChainSafe/lodestar/pull/5357), [prysm#6788](https://github.com/OffchainLabs/prysm/pull/6788), [teku#2437](https://github.com/Consensys-Incorporated/teku/pull/2437)

</details>


<a id="validator_client-026"></a>
<details>
<summary><b>validator_client-026</b> Faster crypto for keystore KDF — <i>not · low · S · startup, cpu</i></summary>

**Idea.** Use an optimized native/assembly (SHA-NI) scrypt/pbkdf2/SHA-256 implementation for keystore decryption instead of a generic one, cutting startup time with many keys (~3x).

**Gap in Lighthouse.** Keystore KDF uses generic RustCrypto pbkdf2/scrypt; no SHA-NI/asm-specific build. Enable sha2 'asm' or swap in an accelerated scrypt/pbkdf2 in eth2_keystore decrypt.

**Impact.** Only cold-start keystore decryption time, up to ~3x faster per key; no steady-state effect.

**Best measured result.** None (pr:lodestar#6253)

**Evidence (Lighthouse @ 928b61e719).**

- [`crypto/eth2_keystore/Cargo.toml:17-19`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/eth2_keystore/Cargo.toml#L17-L19) pbkdf2 0.12 and scrypt 0.11 pure-Rust RustCrypto, default-features=false
- [`crypto/eth2_keystore`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/eth2_keystore) sha2 workspace crate

**Sources.** [lodestar#6956](https://github.com/ChainSafe/lodestar/pull/6956), [lodestar#6253](https://github.com/ChainSafe/lodestar/pull/6253), [nimbus#4301](https://github.com/status-im/nimbus-eth2/pull/4301)

</details>


<a id="validator_client-027"></a>
<details>
<summary><b>validator_client-027</b> Batch slashing interchange import writes — <i>n/a · low · S · disk, memory, latency</i></summary>

**Idea.** When importing a slashing-protection interchange file, save attestations in batched transactions instead of one by one.

**Impact.** Import already runs in one transaction and writes only one max-watermark row per validator, so there are no per-attestation writes to batch.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/slashing_protection/src/slashing_database.rs:827`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/slashing_protection/src/slashing_database.rs#L827) one transaction for entire import
- slashing_database.rs:853-905 import_interchange_record clears rows and inserts a single synthetic attestation and block per validator

**Sources.** [prysm#8304](https://github.com/OffchainLabs/prysm/pull/8304)

</details>


<a id="validator_client-028"></a>
<details>
<summary><b>validator_client-028</b> Deserialize interchange JSON from memory slice — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Read the slashing-protection interchange file fully into memory and deserialize from the slice rather than from a streaming reader, which is much slower in serde_json.

**Impact.** Faster rare interchange import.

**Evidence (Lighthouse @ 928b61e719).**

- [`common/eip_3076/src/lib.rs:68-74`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/eip_3076/src/lib.rs#L68-L74) from_json_reader reads to String then from_json_str
- [`account_manager/src/validator/slashing_protection.rs:87`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/account_manager/src/validator/slashing_protection.rs#L87) import uses it

**Skeptic check.** Verified there is no other interchange path that uses serde_json::from_reader. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#2347](https://github.com/sigp/lighthouse/pull/2347)

</details>


<a id="validator_client-029"></a>
<details>
<summary><b>validator_client-029</b> Bound interchange import target epochs — <i>n/a · low · cpu, disk</i></summary>

**Idea.** Reject imported attestations with target epoch beyond current+1, since span updates do one DB read per epoch and huge targets run effectively forever.

**Gap in Lighthouse.** Lighthouse slashing protection stores only min/max-style records and does no per-epoch span updates on import, so a huge target epoch costs nothing.

**Best measured result.** None (pr:lodestar#10170)

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/slashing_protection/src/slashing_database.rs:853`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/slashing_protection/src/slashing_database.rs#L853) import_interchange_record takes max source/target and writes one synthetic record

**Sources.** [lodestar#10170](https://github.com/ChainSafe/lodestar/pull/10170)

</details>


<a id="validator_client-030"></a>
<details>
<summary><b>validator_client-030</b> Limit min-span lookback in slashing protection — <i>n/a · low · S · disk, latency</i></summary>

**Idea.** Cap the min-span lookback in surround checking (e.g. 4096 epochs) so initial population does not write an entry per epoch back to genesis; DB shrank 4GB to 100MB.

**Impact.** Lighthouse has no min/max span table; it stores signed attestations and queries them, and import collapses history to a single row, so no per-epoch lookback entries are written.

**Best measured result.** None (pr:lodestar#5454)

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/slashing_protection/src/slashing_database.rs:434-492`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/slashing_protection/src/slashing_database.rs#L434-L492) surround checks use SQL queries over signed_attestations plus min-source/min-target watermarks
- slashing_database.rs:853-905 import stores only one max row per validator

**Sources.** [lodestar#5454](https://github.com/ChainSafe/lodestar/pull/5454)

</details>


<a id="validator_client-031"></a>
<details>
<summary><b>validator_client-031</b> Full fill percent for append-only DB buckets — <i>n/a · low · S · disk</i></summary>

**Idea.** Set the B+tree fill percent to 100% for append-only slashing-protection buckets so pages are packed rather than half empty.

**Impact.** Lighthouse uses SQLite, which has no B+tree fill percent tunable of this kind exposed.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/slashing_protection/src/slashing_database.rs:540`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/slashing_protection/src/slashing_database.rs#L540) insert_attestation into SQLite via rusqlite

**Sources.** [prysm#8458](https://github.com/OffchainLabs/prysm/pull/8458)

</details>


<a id="validator_client-032"></a>
<details>
<summary><b>validator_client-032</b> Range-bound DB iterator for slashing pubkeys — <i>n/a · low · S · memory</i></summary>

**Idea.** When loading slashing-protection pubkeys, restrict the DB iterator to the bucket's key range so other buckets' entries are not loaded into memory.

**Impact.** None; Lodestar key-value bucket iterator problem, Lighthouse reads pubkeys with a SQL SELECT on its own table.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/slashing_protection/src/slashing_database.rs:276`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/slashing_protection/src/slashing_database.rs#L276) SELECT from dedicated validators table

**Sources.** [lodestar#5437](https://github.com/ChainSafe/lodestar/pull/5437)

</details>


<a id="validator_client-033"></a>
<details>
<summary><b>validator_client-033</b> Split large DB migration into small transactions — <i>n/a · low · S · memory, disk</i></summary>

**Idea.** Run large validator DB migrations as many small transactions so the DB does not hold all dirty pages in memory (10GB to 140MB).

**Impact.** None; bbolt migration memory issue, SQLite migrations here are small schema changes.

**Best measured result.** None (pr:prysm#8231)

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/slashing_protection/src/slashing_database.rs:158-168`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/slashing_protection/src/slashing_database.rs#L158-L168) SQLite pool of size 1

**Sources.** [prysm#8231](https://github.com/OffchainLabs/prysm/pull/8231)

</details>


<a id="validator_client-034"></a>
<details>
<summary><b>validator_client-034</b> Fetch attestation data once per slot and reuse — <i>implemented · medium · S · latency, bandwidth, cpu</i></summary>

**Idea.** Fetch attestation data once per slot (post-Electra committee index is 0, so it is identical for all committees) and copy it per committee/validator before signing, instead of one beacon API call per validator or committee.

**Impact.** Already done: one attestation_data call per slot.

**Best measured result.** attestation_data calls over 100 slots on minimal: 398 -&gt; 100 (pr:lighthouse#8171)

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/attestation_service.rs:284`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/attestation_service.rs#L284) get_validator_attestation_data(slot, 0) once (head-event path)
- [`validator_client/validator_services/src/attestation_service.rs:332`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/attestation_service.rs#L332) get_validator_attestation_data(slot, 0) once (deadline fallback)
- [`validator_client/validator_services/src/attestation_service.rs:545`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/attestation_service.rs#L545) data cloned per duty
- [`validator_client/validator_services/src/attestation_service.rs:415`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/attestation_service.rs#L415) same data reused for every aggregate committee

**Skeptic check.** Both paths (head event and deadline fallback) fetch attestation data once with index 0. The data is cloned for every duty and reused for aggregation. The earlier evidence was correct. Per-committee aggregate fetches are a different call.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#16236](https://github.com/OffchainLabs/prysm/pull/16236), [lodestar#3917](https://github.com/ChainSafe/lodestar/pull/3917), [lighthouse#8171](https://github.com/sigp/lighthouse/pull/8171), [teku#9620](https://github.com/Consensys-Incorporated/teku/pull/9620), [lodestar#7958](https://github.com/ChainSafe/lodestar/pull/7958), [prysm#15696](https://github.com/OffchainLabs/prysm/pull/15696)

</details>


<a id="validator_client-035"></a>
<details>
<summary><b>validator_client-035</b> Cache builder config per proposer slot — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Cache the computed, signed builder config per proposer/slot so preference publishing and block production do not repeat signing at proposal time.

**Impact.** Signed builder registrations are cached, so they are not re-signed.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/preparation_service.rs:110`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/preparation_service.rs#L110) validator_registration_cache
- [`validator_client/validator_services/src/preparation_service.rs:367-462`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/preparation_service.rs#L367-L462) lookup by key, sign only on miss, insert

**Skeptic check.** Verified the registration cache is keyed on the registration data and signing happens only on a miss. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#11311](https://github.com/Consensys-Incorporated/teku/pull/11311), [grandine@268cc304e](https://github.com/grandinetech/grandine/commit/268cc304ee9e)

</details>


<a id="validator_client-036"></a>
<details>
<summary><b>validator_client-036</b> Cache signed builder registrations — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Cache signed validator registrations per pubkey and only re-sign when fee recipient or gas limit changes, instead of re-creating and re-signing every epoch.

**Impact.** Already done: no re-signing unless fee recipient or gas limit changes.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/preparation_service.rs:124`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/preparation_service.rs#L124) validator_registration_cache keyed by ValidatorRegistrationKey (fee_recipient, gas_limit, pubkey)
- [`validator_client/validator_services/src/preparation_service.rs:394`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/preparation_service.rs#L394) cached signed registration reused, sign only on miss
- [`validator_client/validator_services/src/preparation_service.rs:370`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/preparation_service.rs#L370) only changed keys published between periodic resubmissions

**Skeptic check.** The cache key includes fee_recipient and gas_limit, so a change misses the cache and forces a new signature. Otherwise the stored signed registration is resent. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#4040](https://github.com/status-im/nimbus-eth2/pull/4040), [prysm#11014](https://github.com/OffchainLabs/prysm/pull/11014), [lodestar#4447](https://github.com/ChainSafe/lodestar/pull/4447)

</details>


<a id="validator_client-037"></a>
<details>
<summary><b>validator_client-037</b> Resend builder registrations only at epoch start or expiry — <i>implemented · low · S · bandwidth, cpu</i></summary>

**Idea.** Send builder registrations only at epoch start, on reconnect, for new keys, or when actually expired, and cache validator status per epoch, instead of every slot.

**Impact.** Full re-send only once per epoch, and it reuses cached signed registrations (no re-signing). Other slots send only keys missing from the cache. The per-slot cost is a scan of proposal_data over all keys.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/preparation_service.rs:359-387`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/preparation_service.rs#L359-L387)
- [`validator_client/validator_services/src/preparation_service.rs:395-400`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/preparation_service.rs#L395-L400)
- [`validator_client/validator_services/src/preparation_service.rs:25`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/preparation_service.rs#L25)

**Skeptic check.** Verified that register_validators publishes all keys only when slot % slots_per_epoch == 0, and otherwise only keys not in validator_registration_cache. publish_validator_registration_data reuses cached signatures. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#14371](https://github.com/OffchainLabs/prysm/pull/14371), [nimbus#5663](https://github.com/status-im/nimbus-eth2/pull/5663), [prysm#11005](https://github.com/OffchainLabs/prysm/pull/11005)

</details>


<a id="validator_client-038"></a>
<details>
<summary><b>validator_client-038</b> Register only active validators with builders — <i>partial · low · S · cpu, bandwidth</i></summary>

**Idea.** Filter unknown, pending and exited validators out of builder registrations before signing and sending them.

**Gap in Lighthouse.** Only validators without an index are skipped; pending, exited and withdrawn validators with an index are still registered. Would need status in ProposalData and a filter in collect_validator_registration_keys.

**Impact.** Saves a few BLS signs and builder POST entries for exited validators; negligible.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/preparation_service.rs:294`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/preparation_service.rs#L294) collect_validator_registration_keys skips keys with no validator_index
- [`validator_client/validator_services/src/preparation_service.rs:316`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/preparation_service.rs#L316) collect_proposal_data uses all voting pubkeys

**Sources.** [teku#7423](https://github.com/Consensys-Incorporated/teku/pull/7423), [teku#6313](https://github.com/Consensys-Incorporated/teku/pull/6313), [teku#6100](https://github.com/Consensys-Incorporated/teku/pull/6100), [lighthouse#3441](https://github.com/sigp/lighthouse/pull/3441)

</details>


<a id="validator_client-039"></a>
<details>
<summary><b>validator_client-039</b> Move builder registrations and proposer prep past epoch start — <i>not · low · S · latency, cpu</i></summary>

**Idea.** Schedule builder validator registrations and proposer preparation at a later slot of the epoch (e.g. slot 2, expiry mid-epoch) instead of at epoch start, which is already busy with duties.

**Gap in Lighthouse.** Offset the epoch check in register_validators (e.g. slot % slots_per_epoch == 2) to move the burst off epoch start.

**Impact.** Marginal load smoothing at epoch start; registrations are cached and batched.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/preparation_service.rs:359-387`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/preparation_service.rs#L359-L387) registration fires at first slot of epoch
- [`validator_client/validator_services/src/preparation_service.rs:181-210`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/preparation_service.rs#L181-L210) loop wakes every slot

**Sources.** [teku#6220](https://github.com/Consensys-Incorporated/teku/pull/6220), [teku#6237](https://github.com/Consensys-Incorporated/teku/pull/6237)

</details>


<a id="validator_client-040"></a>
<details>
<summary><b>validator_client-040</b> One encrypted store for all keys, one KDF — <i>implemented · low · S · startup, cpu, memory</i></summary>

**Idea.** Keep all decrypted validator secret keys in one store or cache file encrypted by one password (or the concatenated passwords), so startup runs one KDF instead of one per keystore; verify pubkeys on load and update the cache asynchronously.

**Impact.** Startup KDF runs once instead of once per keystore.

**Best measured result.** None (pr:lighthouse#1695)

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/initialized_validators/src/key_cache.rs:36`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/initialized_validators/src/key_cache.rs#L36) KeyCache: one Crypto (single KDF) over all uuids
- [`validator_client/initialized_validators/src/lib.rs:1211`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/initialized_validators/src/lib.rs#L1211) cache.decrypt(passwords, public_keys) in spawn_blocking, verifies pubkeys
- [`validator_client/initialized_validators/src/lib.rs:252`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/initialized_validators/src/lib.rs#L252) keystore decrypted only on a cache miss
- [`validator_client/initialized_validators/src/lib.rs:1392`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/initialized_validators/src/lib.rs#L1392) modified cache saved in spawn_blocking

**Skeptic check.** One encrypted cache file holds all keypairs, unlocked by the combined passwords with one KDF and checked against the public keys. Only a cache miss falls back to a per-keystore decrypt. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#5043](https://github.com/ChainSafe/lodestar/pull/5043), [lighthouse#1695](https://github.com/sigp/lighthouse/pull/1695), [prysm#6823](https://github.com/OffchainLabs/prysm/pull/6823)

</details>


<a id="validator_client-041"></a>
<details>
<summary><b>validator_client-041</b> Cache signing domain data per epoch — <i>n/a · low · S · latency, bandwidth</i></summary>

**Idea.** Cache signing domains (including selection proof and aggregate domains) per (epoch, domain type) in the validator client instead of asking the beacon node on every signature.

**Impact.** Lighthouse VC never asks the beacon node for domains; computes locally from spec, so there is no round trip to cache.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/lighthouse_validator_store/src/lib.rs:279`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/lighthouse_validator_store/src/lib.rs#L279) signing_context built locally from spec and fork
- [`validator_client/lighthouse_validator_store/src/lib.rs:493`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/lighthouse_validator_store/src/lib.rs#L493) domain_hash computed locally

**Sources.** [prysm#5931](https://github.com/OffchainLabs/prysm/pull/5931), [prysm#5726](https://github.com/OffchainLabs/prysm/pull/5726), [prysm#13263](https://github.com/OffchainLabs/prysm/pull/13263), [prysm#4914](https://github.com/OffchainLabs/prysm/pull/4914)

</details>


<a id="validator_client-042"></a>
<details>
<summary><b>validator_client-042</b> Cache slashing-protection file paths — <i>n/a · low · S · disk, cpu</i></summary>

**Idea.** Cache per-validator slashing-protection file paths and create the base directory once at startup instead of on every write.

**Impact.** None; no per-validator slashing files.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/slashing_protection/src/slashing_database.rs:20-38`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/slashing_protection/src/slashing_database.rs#L20-L38) single SQLite file opened once

**Sources.** [teku#7653](https://github.com/Consensys-Incorporated/teku/pull/7653)

</details>


<a id="validator_client-043"></a>
<details>
<summary><b>validator_client-043</b> Cache proposer config with shared refresh — <i>n/a · low · S · latency, disk</i></summary>

**Idea.** Serve the last loaded proposer config for a TTL and share concurrent refreshes instead of reloading for every request.

**Impact.** None; no remote proposer config reloaded per request.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/lighthouse_validator_store/src/lib.rs:381-420`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/lighthouse_validator_store/src/lib.rs#L381-L420) proposal settings read from in-memory definitions

**Sources.** [teku#5715](https://github.com/Consensys-Incorporated/teku/pull/5715)

</details>


<a id="validator_client-044"></a>
<details>
<summary><b>validator_client-044</b> Cache aggregator selection proofs — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Cache aggregator selection proofs / slot signatures per (validator, slot) or by message in a small bounded cache pruned each epoch, so the same BLS signature is not computed twice.

**Impact.** Each proof is signed once per duty and kept until the duty is pruned.

**Best measured result.** None (pr:lodestar#3897)

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/duties_service.rs:103`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L103) DutyAndProof stores selection_proof
- [`validator_client/validator_services/src/duties_service.rs:1257`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L1257) duties (and so proofs) recomputed only when missing or dependent_root differs
- [`validator_client/validator_services/src/duties_service.rs:1380`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L1380) fill_in_selection_proofs only for new_duties
- [`validator_client/validator_services/src/duties_service.rs:1509`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L1509) proof kept with duty for the same dependent_root

**Skeptic check.** Confirmed that proofs are computed once per new duty and kept on the duty. Only a dependent_root change (a reorg) recomputes them, even when the duty slot is unchanged. That case is rare, so the earlier verdict stands.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#3897](https://github.com/ChainSafe/lodestar/pull/3897), [nimbus#2949](https://github.com/status-im/nimbus-eth2/pull/2949), [lighthouse#3223](https://github.com/sigp/lighthouse/pull/3223)

</details>


<a id="validator_client-045"></a>
<details>
<summary><b>validator_client-045</b> Prebuild remote signer request URI — <i>n/a · low · S · cpu</i></summary>

**Idea.** Build the remote signer request URI once and reuse it instead of rebuilding it per signing call.

**Impact.** None; URL already prebuilt.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/signing_method/src/lib.rs:102`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/signing_method/src/lib.rs#L102),277 signing_url built once at construction, cloned per request

**Sources.** [teku#9656](https://github.com/Consensys-Incorporated/teku/pull/9656)

</details>


<a id="validator_client-046"></a>
<details>
<summary><b>validator_client-046</b> Cache own validator index — <i>implemented · low · S · latency, bandwidth</i></summary>

**Idea.** Fetch the validator index once (startup or duty update) and cache it instead of looking it up before every duty.

**Impact.** Index is cached in memory; no per-duty lookup.

**Best measured result.** None (pr:prysm#4406)

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/duties_service.rs:928`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L928) poll_validator_indices skips pubkeys whose index is known
- [`validator_client/validator_services/src/duties_service.rs:989`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L989) set_validator_index stores the resolved index
- [`validator_client/lighthouse_validator_store/src/lib.rs:844`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/lighthouse_validator_store/src/lib.rs#L844) validator_index reads the in-memory index

**Skeptic check.** The BN is queried only for pubkeys with no index, and unknown pubkeys are rate-limited to once per epoch. All duty code reads the cached index. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#4406](https://github.com/OffchainLabs/prysm/pull/4406), [prysm#1701](https://github.com/OffchainLabs/prysm/pull/1701)

</details>


<a id="validator_client-047"></a>
<details>
<summary><b>validator_client-047</b> Bound concurrent keystore decryptions at startup — <i>implemented · low · S · memory, startup</i></summary>

**Idea.** Bound the number of scrypt/pbkdf2 keystore decryptions running concurrently at validator client startup. Scrypt is memory-hard, so unbounded parallel derivations with many keys exhaust memory and CPU.

**Impact.** Concurrency is 1 (sequential), so memory cannot run out. Startup is slower than a bounded-parallel pool would be, but that is a separate idea.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/initialized_validators/src/lib.rs:1281-1289`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/initialized_validators/src/lib.rs#L1281-L1289)
- [`validator_client/initialized_validators/src/lib.rs:252-293`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/initialized_validators/src/lib.rs#L252-L293)
- [`validator_client/http_api/src/keystores.rs:104-125`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/http_api/src/keystores.rs#L104-L125)
- [`validator_client/http_api/src/keystores.rs:203`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/http_api/src/keystores.rs#L203)

**Skeptic check.** update_validators awaits from_definition one key at a time, and each decrypt runs in one spawn_blocking. The keymanager import API also decrypts in a sequential loop. The decrypted key cache avoids the KDF on restart. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#4174](https://github.com/ChainSafe/lodestar/pull/4174), [teku#2517](https://github.com/Consensys-Incorporated/teku/pull/2517)

</details>


<a id="validator_client-048"></a>
<details>
<summary><b>validator_client-048</b> Cap skip slots processed for duties — <i>n/a · low · S · cpu, latency</i></summary>

**Idea.** Cap the number of skip slots processed (e.g. 128) so long skips do not make requests pile up for large validator sets.

**Impact.** None.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/duties_service.rs:671`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L671) only a comment on skipping; no skip-slot cap found

**Sources.** [lighthouse#618](https://github.com/sigp/lighthouse/pull/618)

</details>


<a id="validator_client-049"></a>
<details>
<summary><b>validator_client-049</b> Cheap KDF for test keystores — <i>n/a · low · S · startup, cpu</i></summary>

**Idea.** Use a cheap KDF mode for test/simulation keystore generation so thousands of keystores are created quickly.

**Impact.** None on mainnet nodes.

**Evidence (Lighthouse @ 928b61e719).**

- [`common/validator_dir/src/insecure_keys.rs:53`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/validator_dir/src/insecure_keys.rs#L53) insecure_kdf() with cheap Scrypt params already used for test keystores

**Sources.** [nimbus@46fc5716a](https://github.com/status-im/nimbus-eth2/commit/46fc5716a44d)

</details>


<a id="validator_client-050"></a>
<details>
<summary><b>validator_client-050</b> Cheaper per-slot proposer settings push — <i>n/a · low · S · latency, cpu</i></summary>

**Idea.** Push proposer settings every slot with a cheap call that avoids collecting full key status each time (0.5-2.8s to 52ms for 5k keys).

**Impact.** None.

**Best measured result.** None (pr:prysm#14155)

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/preparation_service.rs:264`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/preparation_service.rs#L264) prepare_proposers_and_publish; collect_proposal_data at :316 uses voting_pubkeys + proposal_data only (no key status collection)

**Sources.** [prysm#14155](https://github.com/OffchainLabs/prysm/pull/14155)

</details>


<a id="validator_client-051"></a>
<details>
<summary><b>validator_client-051</b> Proposer preferences once per epoch — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Compute the proposer-preference dependent root and publish preferences once per epoch (only new duties), and release the duties lock before signing/RPC I/O, so slot-critical duties are not delayed.

**Impact.** Preferences are signed once per (epoch, dependent_root) and only for new duties. This runs in its own task with the proposers read lock dropped before signing and I/O, so slot-critical duties do not wait for it.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/proposer_preferences_service.rs:74-84`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/proposer_preferences_service.rs#L74-L84)
- [`validator_client/validator_services/src/proposer_preferences_service.rs:138-162`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/proposer_preferences_service.rs#L138-L162)
- [`validator_client/validator_services/src/proposer_preferences_service.rs:168`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/proposer_preferences_service.rs#L168)

**Skeptic check.** Verified that the proposers lock is scoped to a block that clones the duties. The PublishedPreferences map keyed by (epoch, dependent_root) filters to unpublished duties. The dependent root comes from duties_service and is not recomputed. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [grandine#859](https://github.com/grandinetech/grandine/pull/859), [prysm#16611](https://github.com/OffchainLabs/prysm/pull/16611), [grandine@66fae44c5](https://github.com/grandinetech/grandine/commit/66fae44c5ac7)

</details>


<a id="validator_client-052"></a>
<details>
<summary><b>validator_client-052</b> Start duty services concurrently — <i>n/a · low · S · startup, latency</i></summary>

**Idea.** Start block and attestation services concurrently and await the first duty fetch so the first attestation is not missed.

**Impact.** None.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/src/lib.rs:708-745`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/src/lib.rs#L708-L745) start_service spawns each service via executor.spawn, running concurrently; initial duty poll at :646 poll_validator_indices before start

**Sources.** [lodestar@ebdff96e2](https://github.com/ChainSafe/lodestar/commit/ebdff96e2e1e)

</details>


<a id="validator_client-053"></a>
<details>
<summary><b>validator_client-053</b> Sign duties concurrently, not sequentially — <i>partial · low · S · latency</i></summary>

**Idea.** Request signatures for a batch of duties (proposer preferences, payload attestations) concurrently and publish as each completes, so one slow remote signer does not serialize or block others.

**Gap in Lighthouse.** In publish_proposer_preferences, sign with join_all / FuturesUnordered instead of the sequential for loop (optionally publish as signatures complete).

**Impact.** Removes head-of-line blocking of proposer preferences with slow remote signers; none for local keys.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/payload_attestation_service.rs:376-392`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/payload_attestation_service.rs#L376-L392) join_all signs payload attestations concurrently (PR 9756)
- [`validator_client/validator_services/src/proposer_preferences_service.rs:183-200`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/proposer_preferences_service.rs#L183-L200) proposer preferences still signed sequentially in a for loop (PR 9617 closed, not merged)

**Sources.** [lighthouse#9617](https://github.com/sigp/lighthouse/pull/9617), [lighthouse#9756](https://github.com/sigp/lighthouse/pull/9756)

</details>


<a id="validator_client-054"></a>
<details>
<summary><b>validator_client-054</b> Stop long loops on request cancellation — <i>n/a · low · S · cpu</i></summary>

**Idea.** Check request context cancellation inside long loops (e.g. aggregate submission) so work stops when the client disconnects or deadline expires.

**Impact.** None.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/attestation_service.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/attestation_service.rs) and duties_service.rs use async tasks; no long synchronous loops over requests

**Sources.** [prysm#4346](https://github.com/OffchainLabs/prysm/pull/4346)

</details>


<a id="validator_client-055"></a>
<details>
<summary><b>validator_client-055</b> Refetch duties only when dependent root changes — <i>partial · medium · S · bandwidth, cpu, latency</i></summary>

**Idea.** Invalidate and refetch attester/proposer duties only when the duties' dependent root changes (as reported by head events), rotating cached next-epoch duties into current at the boundary and polling otherwise once per epoch, instead of repolling every slot or on every reorg. The dependent root must be computed correctly or duties recompute constantly.

**Gap in Lighthouse.** The dependent root already gates the full refetch. But two probe POSTs (current and next epoch) still go out every slot, and the proposer duties are polled every slot. A head monitor exists, but HeadEvent has no previous_duty_dependent_root/current_duty_dependent_root and duties_service does not subscribe to it. To close the gap: add the dependent roots to HeadEvent, and probe only when they change, with a once-per-epoch fallback.

**Impact.** Saves about 2 small duties POSTs per slot per VC. That is negligible for one VC and matters only for BNs that serve many VCs.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/duties_service.rs:739-760`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L739-L760) attester poll loop runs every slot on a timer
- [`validator_client/validator_services/src/duties_service.rs:1066-1103`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L1066-L1103) probes both current and next epoch every slot
- [`validator_client/validator_services/src/duties_service.rs:1240-1275`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L1240-L1275) small probe of INITIAL_DUTIES_QUERY_SIZE indices; full refetch only if dependent_root differs
- [`validator_client/beacon_node_fallback/src/beacon_head_monitor.rs:17-21`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/beacon_node_fallback/src/beacon_head_monitor.rs#L17-L21) HeadEvent carries only slot and block root, no dependent roots
- [`validator_client/src/lib.rs:439-440`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/src/lib.rs#L439-L440),565,586 head events go only to attestation and sync committee services, not to duties_service

**Second check.** I found the beacon_head_monitor head-event subscription, which the earlier review did not mention. It only drives attestation and sync committee timing, and its event drops the dependent roots, so the verdict stays partial.

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [teku#10384](https://github.com/Consensys-Incorporated/teku/pull/10384), [teku#3434](https://github.com/Consensys-Incorporated/teku/pull/3434), [nimbus#8877](https://github.com/status-im/nimbus-eth2/pull/8877), [lighthouse#4170](https://github.com/sigp/lighthouse/pull/4170), [prysm#16421](https://github.com/OffchainLabs/prysm/pull/16421), [lighthouse#8338](https://github.com/sigp/lighthouse/pull/8338), [lighthouse#9799](https://github.com/sigp/lighthouse/pull/9799), [lodestar#9380](https://github.com/ChainSafe/lodestar/pull/9380), [lodestar#10454](https://github.com/ChainSafe/lodestar/pull/10454)

</details>


<a id="validator_client-056"></a>
<details>
<summary><b>validator_client-056</b> Fetch duties once per epoch, serve slots from cache — <i>partial · low · S · bandwidth, latency, cpu</i></summary>

**Idea.** Fetch attester and proposer duty assignments once per epoch (or when missing or the dependent root changes) and serve per-slot checks and attestation routines from the cache, instead of polling the beacon node every slot.

**Gap in Lighthouse.** Proposer duties are not served from the cache. poll_beacon_proposers calls fetch_and_store_proposer_duties for both the current and next epoch on every slot (2 full GETs per slot, 64 per epoch). It does not skip the call when the cache already holds the epoch with a matching dependent_root. Lighthouse PRs 8905, 9461, 8573 and 8574 proposed this and were all closed unmerged. Only attester duties (poll_beacon_attesters_for_epoch probe) and sync duties avoid the per-slot refetch.

**Impact.** Removes about 62 of 64 proposer-duty HTTP requests per epoch per VC. The BN serves them from the proposer cache, so the saving is small: less BN API load and VC CPU.

**Best measured result.** 32 requests to 1 per epoch (pr:lighthouse#8905)

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/duties_service.rs:1249`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L1249) attester duties: 1-index probe, full fetch only if dependent_root changed or duties missing
- [`validator_client/validator_services/src/duties_service.rs:1882`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L1882) poll_beacon_proposers calls fetch_and_store_proposer_duties for current_epoch and current_epoch+1 every slot, unconditionally
- [`validator_client/validator_services/src/duties_service.rs:1927`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L1927) fetch_and_store_proposer_duties always does a full GET (v2) and overwrites the cache
- [`validator_client/validator_services/src/duties_service.rs:718`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L718) proposer poll loop runs every slot

**Skeptic check.** The earlier evidence covered only the attester path, which uses the dependent_root probe. The proposer path still fetches the full duties for two epochs every slot. Every Lighthouse PR in this cluster that would fix it was closed without merging.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [prysm#2166](https://github.com/OffchainLabs/prysm/pull/2166), [prysm#2412](https://github.com/OffchainLabs/prysm/pull/2412), [lighthouse#9461](https://github.com/sigp/lighthouse/pull/9461), [lighthouse#8573](https://github.com/sigp/lighthouse/pull/8573), [lighthouse#8574](https://github.com/sigp/lighthouse/pull/8574), [lighthouse#8905](https://github.com/sigp/lighthouse/pull/8905)

</details>


<a id="validator_client-057"></a>
<details>
<summary><b>validator_client-057</b> Short lookahead, per-slot batches for selection proofs — <i>partial · low · S · cpu, bandwidth, latency</i></summary>

**Idea.** Precompute aggregator/sync selection proofs only a few slots ahead, signing them in small per-slot batches, instead of 32 slots ahead or thousands of signing tasks at epoch start. Avoids wasted signing, remote signer load and contention with duty signing.

**Gap in Lighthouse.** Attestation selection proofs follow the idea (8-slot lookahead, per-slot batches at mid-slot). Sync committee selection proofs in non-DVT mode precompute 64 slots ahead: on startup and when a new period's duties appear, fill_in_aggregation_proofs signs 64 slots x subnets x sync validators in one burst, not timed to a quiet point in the slot, which is the 32-slot-ahead pattern nimbus#6609 cut to 2. Reduce the sync lookahead (e.g. 1-2 slots) and schedule fill_in_aggregation_proofs at mid-slot like the attestation path.

**Impact.** Removes a burst of ~64*subnets signatures per sync-committee validator at VC start / period start (matters for remote signers); steady state already 1 slot per tick.

**Best measured result.** with 5k validators replaces 5k tasks with 1 task signing ~160 proofs per slot; graphs show lower median signing time (pr:lighthouse#4033)

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/src/lib.rs:68`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/src/lib.rs#L68) SELECTION_PROOF_SLOT_LOOKAHEAD = 8 (attestation)
- [`validator_client/validator_services/src/duties_service.rs:1581-1710`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L1581-L1710) fill_in_selection_proofs signs attestation proofs in per-slot batches at half-slot
- [`validator_client/src/lib.rs:77`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/src/lib.rs#L77) AGGREGATION_PRE_COMPUTE_EPOCHS = 2
- [`validator_client/src/lib.rs:507`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/src/lib.rs#L507) sync selection lookahead_slot = slots_per_epoch * 2 (64 slots) in non-DVT mode
- [`validator_client/validator_services/src/sync.rs:105-150`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/sync.rs#L105-L150) prepare_for_aggregator_pre_compute starts from current slot up to current+64
- [`validator_client/validator_services/src/sync.rs:623-640`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/sync.rs#L623-L640) fill_in_aggregation_proofs loops over all slots start..=pre_compute_slot back-to-back

**Skeptic check.** Earlier evidence was right for attestation selection proofs (and the config default 0 it cited is overridden in lib.rs to 8), but missed that sync selection proofs use a 2-epoch lookahead with a back-to-back burst.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [nimbus#9416](https://github.com/status-im/nimbus-eth2/pull/9416), [nimbus#6609](https://github.com/status-im/nimbus-eth2/pull/6609), [lighthouse#4033](https://github.com/sigp/lighthouse/pull/4033)

</details>


<a id="validator_client-058"></a>
<details>
<summary><b>validator_client-058</b> Configurable keystore reload debounce — <i>n/a · low · cpu, disk</i></summary>

**Idea.** Debounce keystore directory change detection with a configurable interval so bulk imports trigger one reload.

**Impact.** none

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/src/lib.rs:193`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/src/lib.rs#L193) discover_local_keystores called once at startup
- no notify crate in Cargo.toml files
- VC has no keystore directory watcher (no notify dependency); keystores are discovered once at startup and changed via the keymanager API, so there is nothing to debounce.

**Sources.** [prysm#8149](https://github.com/OffchainLabs/prysm/pull/8149)

</details>


<a id="validator_client-059"></a>
<details>
<summary><b>validator_client-059</b> Decrypt keystores before waiting for beacon node — <i>implemented · low · S · startup</i></summary>

**Idea.** Decrypt validator keystores at startup before waiting for the beacon node or genesis so the first slots are not missed.

**Impact.** Keystores are decrypted before waiting for BN/genesis.

**Best measured result.** None (pr:lighthouse#1299)

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/src/lib.rs:207`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/src/lib.rs#L207) InitializedValidators::from_definitions decrypts keystores in ProductionValidatorClient::new
- [`validator_client/src/lib.rs:388-407`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/src/lib.rs#L388-L407) genesis / beacon node wait happens afterwards

**Skeptic check.** Verified ordering in ProductionValidatorClient::new; earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#1299](https://github.com/sigp/lighthouse/pull/1299)

</details>


<a id="validator_client-060"></a>
<details>
<summary><b>validator_client-060</b> Dedicated executor for committee precalculation — <i>n/a · low · cpu, latency</i></summary>

**Idea.** Run own-committee-member precalculation and pruning on a dedicated executor keyed by dependent root so it does not compete with block import and attestation work.

**Impact.** none

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/duties_service.rs:1141`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L1141) duties read from BN-provided attesters map
- Lighthouse VC gets duties from the BN API and does not precompute committees; BN committee caches are separate and tokio-based.

**Sources.** [grandine@7e9c90802](https://github.com/grandinetech/grandine/commit/7e9c90802fd5)

</details>


<a id="validator_client-061"></a>
<details>
<summary><b>validator_client-061</b> Dedicated executors for remote BN calls — <i>n/a · low · latency</i></summary>

**Idea.** Run remote beacon-node API calls and readiness checks on dedicated executors so slow remote calls do not starve the scheduler and local signing.

**Impact.** none

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/beacon_node_fallback`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/beacon_node_fallback)
- JVM executor tuning; Lighthouse VC uses tokio tasks, and BN calls go through beacon_node_fallback with per-call timeouts without a shared pool that signing could starve.

**Sources.** [teku#9605](https://github.com/Consensys-Incorporated/teku/pull/9605)

</details>


<a id="validator_client-062"></a>
<details>
<summary><b>validator_client-062</b> Size VC executor threads and queues to load — <i>n/a · low · cpu, latency</i></summary>

**Idea.** Size validator client executor thread pools from available CPUs and make async/signing queue capacities larger and configurable so duty bursts are not rejected or starved.

**Impact.** none

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/src/lib.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/src/lib.rs)
- JVM thread pool and queue sizing; tokio runtime sizes itself to CPUs and there are no bounded signing queues to reject duties.

**Sources.** [teku#8144](https://github.com/Consensys-Incorporated/teku/pull/8144), [teku#5814](https://github.com/Consensys-Incorporated/teku/pull/5814)

</details>


<a id="validator_client-063"></a>
<details>
<summary><b>validator_client-063</b> Batch committee subnet subscriptions — <i>implemented · low · S · latency, bandwidth</i></summary>

**Idea.** Send all committee subnet subscriptions for a slot/epoch to the beacon node in one batched request instead of one call per duty.

**Impact.** One batched request per poll for both committee and sync subscriptions.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/duties_service.rs:1134-1172`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L1134-L1172) collects all current/next-epoch subscriptions into one Vec and sends one post_validator_beacon_committee_subscriptions
- [`validator_client/validator_services/src/sync_committee_service.rs:618`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/sync_committee_service.rs#L618) sync subscriptions also sent as one slice

**Skeptic check.** Verified the batching; earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#5332](https://github.com/OffchainLabs/prysm/pull/5332), [teku#2990](https://github.com/Consensys-Incorporated/teku/pull/2990), [lodestar@e4ef843f8](https://github.com/ChainSafe/lodestar/commit/e4ef843f8cd8)

</details>


<a id="validator_client-064"></a>
<details>
<summary><b>validator_client-064</b> Deduplicate subnet subscription messages — <i>partial · low · S · cpu</i></summary>

**Idea.** Drop the per-validator index from subnet subscriptions so duplicates collapse, and pass all subscriptions from the HTTP API to the network service in one message.

**Gap in Lighthouse.** post_validator_sync_committee_subscriptions still sends one ValidatorSubscriptionMessage::SyncCommitteeSubscribe per subscription (subscriptions: vec![subscription]) through try_send. The subscriptions keep validator_index, so duplicates for the same subnets are not collapsed before the network service. Only the attestation path (post_validator_beacon_committee_subscriptions) was changed to one BTreeSet message by PR 5311.

**Impact.** Attestation subscriptions, the high-volume path, are already deduplicated and batched. The sync committee path has few subscriptions per node, so the remaining gain is negligible.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/validator/mod.rs:1162-1179`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validator/mod.rs#L1162-L1179)
- [`beacon_node/http_api/src/validator/mod.rs:666-686`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validator/mod.rs#L666-L686)
- [`beacon_node/network/src/service.rs:154-161`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/service.rs#L154-L161)
- [`beacon_node/network/src/service.rs:823-826`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/service.rs#L823-L826)

**Skeptic check.** The attestation path matches PR 5311: a BTreeSet&lt;ValidatorSubscription&gt; without the index, sent as one message. The earlier evidence was right for that path but missed the sync committee subscription handler, which still sends one message per entry.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [lighthouse#5311](https://github.com/sigp/lighthouse/pull/5311)

</details>


<a id="validator_client-065"></a>
<details>
<summary><b>validator_client-065</b> One subscription per duty — <i>implemented · low · S · bandwidth</i></summary>

**Idea.** Send a single subnet subscription per duty rather than separate aggregating and non-aggregating ones.

**Impact.** One BeaconCommitteeSubscription per duty per send, with an is_aggregator flag. The repeated sends from ATTESTATION_SUBSCRIPTION_OFFSETS are redundancy, not split aggregating and non-aggregating subscriptions.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/duties_service.rs:1135-1157`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L1135-L1157)
- [`validator_client/validator_services/src/duties_service.rs:1160-1172`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L1160-L1172)

**Skeptic check.** Verified that the subscription loop pushes one entry per duty, with is_aggregator = selection_proof.is_some(), all in one batched POST. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#2993](https://github.com/Consensys-Incorporated/teku/pull/2993)

</details>


<a id="validator_client-066"></a>
<details>
<summary><b>validator_client-066</b> Deduplicate aggregator work across local keys — <i>partial · low · S · cpu, bandwidth</i></summary>

**Idea.** When several local keys share a (slot, committee), submit one aggregate-and-proof and skip repeat is-aggregator checks and duplicate subscriptions, since results are identical.

**Gap in Lighthouse.** In produce_and_publish_aggregates, after building aggregates_to_sign, keep only the first aggregator per committee so one signed aggregate is published.

**Impact.** Saves a few signatures and publishes only for nodes with many keys in one committee (rare; aggregators are about 16 per committee). Negligible CPU.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/attestation_service.rs:640-700`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/attestation_service.rs#L640-L700) one GET aggregate, then sign per aggregator duty
- [`validator_client/validator_services/src/duties_service.rs:147-162`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L147-L162) per-key selection proof and is_aggregator
- Aggregate fetch is done once per (slot, committee) and subscriptions are deduped in the BN, but each local key with a selection proof still signs and publishes its own aggregate-and-proof; selection proofs are per-key so they cannot be shared.

**Sources.** [prysm#5346](https://github.com/OffchainLabs/prysm/pull/5346), [prysm#5334](https://github.com/OffchainLabs/prysm/pull/5334), [teku#1547](https://github.com/Consensys-Incorporated/teku/pull/1547)

</details>


<a id="validator_client-067"></a>
<details>
<summary><b>validator_client-067</b> Shared periodic fork info fetch — <i>n/a · low · bandwidth, latency</i></summary>

**Idea.** Fetch fork info once per period for all validators instead of each validator issuing its own HTTP request.

**Impact.** none

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/lighthouse_validator_store/src/lib.rs:68`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/lighthouse_validator_store/src/lib.rs#L68),287-306 fork built from spec
- Lighthouse VC does not fetch fork info from the BN; it derives the fork from the chain spec and genesis_validators_root.

**Sources.** [teku#3345](https://github.com/Consensys-Incorporated/teku/pull/3345)

</details>


<a id="validator_client-068"></a>
<details>
<summary><b>validator_client-068</b> No subnet subscriptions until synced — <i>not · low · S · bandwidth, cpu</i></summary>

**Idea.** Do not subscribe to attestation and sync committee subnets until the node is forward synced.

**Gap in Lighthouse.** Add not_while_syncing_filter to the two subscription routes, or have SubnetService::validator_subscriptions ignore them while sync_state is not Synced. Only matters for nodes with validators that are syncing.

**Impact.** Saves a little gossip bandwidth on a syncing node that also has validators attached; nothing on synced nodes.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/validator/mod.rs:1141`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validator/mod.rs#L1141) beacon_committee_subscriptions has no not_while_syncing filter
- [`beacon_node/http_api/src/lib.rs:2815`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L2815) route wired without not_while_syncing_filter
- [`beacon_node/network/src/service.rs:820`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/service.rs#L820) subscriptions forwarded to subnet_service unconditionally
- [`validator_client/validator_services/src/duties_service.rs:1162`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L1162) VC posts subscriptions regardless of BN sync

**Sources.** [grandine@7cddc9110](https://github.com/grandinetech/grandine/commit/7cddc9110bdf)

</details>


<a id="validator_client-069"></a>
<details>
<summary><b>validator_client-069</b> Late next-period sync committee duties/subscriptions — <i>partial · low · S · bandwidth, cpu</i></summary>

**Idea.** Request next-period sync committee duties and subscribe to sync subnets only near the end of the current period (about 2 epochs before), instead of every poll or right away.

**Gap in Lighthouse.** Subscriptions are already late (lookahead window). Duty polling for the next period starts at half period; could be moved to a few epochs before the end, but one request per period makes this negligible.

**Impact.** Essentially nothing: one duties request per validator set per period saved for about 13 hours.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/sync.rs:286`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/sync.rs#L286) next-period duties fetched from half the period (128 epochs), not 2 epochs before the end
- [`validator_client/validator_services/src/sync.rs:379`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/sync.rs#L379) gate on epoch_offset
- [`validator_client/validator_services/src/sync_committee_service.rs:558`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/sync_committee_service.rs#L558) next-period subscriptions only in SUBSCRIPTION_LOOKAHEAD_EPOCHS window

**Sources.** [nimbus#5409](https://github.com/status-im/nimbus-eth2/pull/5409), [lodestar@e041e3c16](https://github.com/ChainSafe/lodestar/commit/e041e3c16e18)

</details>


<a id="validator_client-070"></a>
<details>
<summary><b>validator_client-070</b> Derive HD keys on demand — <i>n/a · low · L · disk, startup</i></summary>

**Idea.** Derive validator keys from the seed on demand instead of storing and loading every derived account from disk.

**Gap in Lighthouse.** Prysm HD wallet design; Lighthouse loads keystores listed in validator_definitions and has no seed-derived wallet at runtime.

**Impact.** None.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/initialized_validators/src/lib.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/initialized_validators/src/lib.rs) keystores are loaded per validator definition

**Sources.** [prysm#6790](https://github.com/OffchainLabs/prysm/pull/6790)

</details>


<a id="validator_client-071"></a>
<details>
<summary><b>validator_client-071</b> Opt-in duty countdown logging — <i>n/a · low · S · cpu</i></summary>

**Idea.** Make per-slot duty countdown logging opt-in so no ticker and logging work run per duty by default.

**Gap in Lighthouse.** Lighthouse has no per-duty countdown ticker; the notifier is a single per-slot task.

**Impact.** None.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/notifier_service.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/notifier_service.rs) per-slot notifier, no per-duty countdown ticker

**Sources.** [prysm#8161](https://github.com/OffchainLabs/prysm/pull/8161)

</details>


<a id="validator_client-072"></a>
<details>
<summary><b>validator_client-072</b> Subnet subscriptions and selection proofs off duty path — <i>implemented · low · S · latency</i></summary>

**Idea.** Compute aggregator selection proofs and send subnet subscription requests in a background task instead of before returning or updating duties, so attestation duties do not wait on signing or the beacon node.

**Impact.** Duties are stored at once without proofs. Selection proofs are computed in a spawned background task, and the subscription POST runs in the separate duties_service_attesters task after the duties are stored. The attestation service reads the map and does not wait on either.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/duties_service.rs:1323-1326`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L1323-L1326)
- [`validator_client/validator_services/src/duties_service.rs:1367-1384`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L1367-L1384)
- [`validator_client/validator_services/src/duties_service.rs:736-757`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L736-L757)
- [`validator_client/validator_services/src/sync.rs:362-370`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/sync.rs#L362-L370)

**Skeptic check.** Verified that new_without_selection_proof inserts duties before fill_in_selection_proofs is spawned. Sync committee aggregation proofs are also spawned (sync.rs). The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#5662](https://github.com/OffchainLabs/prysm/pull/5662), [prysm#8319](https://github.com/OffchainLabs/prysm/pull/8319)

</details>


<a id="validator_client-073"></a>
<details>
<summary><b>validator_client-073</b> Short-circuit empty duty requests — <i>implemented · low · S · cpu</i></summary>

**Idea.** Return empty duties immediately when the requested validator key list is empty.

**Impact.** The Lighthouse VC never sends an empty duties request. The BN handler (cached_attestation_duties) does not short-circuit an empty index list. It still needs the shuffling for dependent_root, which the API requires, so a short-circuit there would not be free.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/duties_service.rs:1226-1232`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L1226-L1232)
- [`validator_client/validator_services/src/sync.rs:437-443`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/sync.rs#L437-L443)
- [`beacon_node/http_api/src/attester_duties.rs:63-79`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/attester_duties.rs#L63-L79)

**Skeptic check.** Teku's PR was a BN-side short-circuit. In Lighthouse the same effect is on the VC side for attester and sync committee polls. The BN still resolves the committee cache for an empty list from a third-party VC, but that is needed for dependent_root. The earlier evidence was correct for the VC.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#1724](https://github.com/Consensys-Incorporated/teku/pull/1724)

</details>


<a id="validator_client-074"></a>
<details>
<summary><b>validator_client-074</b> Event-driven wait for activation — <i>partial · low · S · latency</i></summary>

**Idea.** Wake the wait-for-activation loop on key-change notifications instead of polling every 30s, so new keys are picked up immediately.

**Gap in Lighthouse.** Lighthouse has no 30s wait-for-activation loop; it re-polls unknown validators every slot (12s), not event-driven on key import. A new key waits up to one slot. Could notify the indices task from add_validator_keystore (tokio Notify) to poll immediately.

**Impact.** Negligible on a mainnet node; only shaves up to 12s off picking up a freshly imported key.

**Best measured result.** None (pr:prysm#13448)

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/duties_service.rs:686`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L686) poll_validator_indices loop runs once per slot
- [`validator_client/validator_services/src/duties_service.rs:911`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L911) unknown pubkeys re-queried each slot (once per epoch backoff)
- [`validator_client/src/lib.rs:646`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/src/lib.rs#L646) pre-genesis poll

**Sources.** [prysm#13448](https://github.com/OffchainLabs/prysm/pull/13448)

</details>


<a id="validator_client-075"></a>
<details>
<summary><b>validator_client-075</b> Remove abort listeners after each request — <i>n/a · low · S · memory</i></summary>

**Idea.** Remove abort-signal listeners added per HTTP request after it completes so listeners do not accumulate on long-lived signals.

**Gap in Lighthouse.** JS AbortSignal listener leak; Rust futures have no such mechanism.

**Impact.** None.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/beacon_node_fallback/src/lib.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/beacon_node_fallback/src/lib.rs) uses reqwest futures, no abort-signal listeners

**Sources.** [lodestar#4107](https://github.com/ChainSafe/lodestar/pull/4107)

</details>


<a id="validator_client-076"></a>
<details>
<summary><b>validator_client-076</b> Release performance tracker entries — <i>n/a · low · S · memory</i></summary>

**Idea.** Track attestations in the performance tracker by the aggregated format so entries are released, preventing unbounded memory growth.

**Gap in Lighthouse.** Teku-specific tracker leak; Lighthouse validator monitor summaries and attestation maps are bounded.

**Impact.** None.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/validator_monitor.rs:44`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_monitor.rs#L44) HISTORIC_EPOCHS=10 pruning
- [`beacon_node/beacon_chain/src/validator_monitor.rs:85`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_monitor.rs#L85) unaggregated attestation map capped at 64

**Sources.** [teku#8851](https://github.com/Consensys-Incorporated/teku/pull/8851)

</details>


<a id="validator_client-077"></a>
<details>
<summary><b>validator_client-077</b> Parallel keystore decryption for keymanager API imports — <i>not · low · M · cpu, latency</i></summary>

**Idea.** Decrypt keystores imported through the keymanager API in a queued parallel worker pool rather than serially, keeping the duty path free while KDF work runs.

**Gap in Lighthouse.** In import_keystores / import_single_keystore, run decrypt_keypair for all keystores in parallel (rayon or JoinSet of spawn_blocking), then add the validated keys; also avoid the double decryption by passing the decrypted keypair through.

**Impact.** Bulk keymanager imports of many keys (scrypt ~1s each, done twice) would be several times faster with cores; no effect on steady-state duties.

**Best measured result.** ~5x faster import of many keys (pr:lodestar#5624)

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/http_api/src/keystores.rs:104-131`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/http_api/src/keystores.rs#L104-L131) keystores imported in a serial for loop
- [`validator_client/http_api/src/keystores.rs:198-218`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/http_api/src/keystores.rs#L198-L218) import_single_keystore decrypts once to validate then block_on(add_validator_keystore) decrypts again
- initialized_validators/src/lib.rs:260 spawn_blocking decrypt, one at a time

**Sources.** [lodestar#5624](https://github.com/ChainSafe/lodestar/pull/5624)

</details>


<a id="validator_client-078"></a>
<details>
<summary><b>validator_client-078</b> Decrypt inline when KDF is cheap — <i>n/a · low · latency, startup</i></summary>

**Idea.** Skip the worker thread pool for keystore decryption when KDF parameters are cheap (testnets), since pool spawn and warm-up cost dominates the decryption itself.

**Impact.** Nothing to save; no pool to skip.

**Best measured result.** 64 keystores: ~10-16 s with pool vs ~1 s without in Kurtosis (pr:lodestar#6949)

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/initialized_validators/src/lib.rs:252-290`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/initialized_validators/src/lib.rs#L252-L290) spawn_blocking decrypt_keypair, no pool

**Sources.** [lodestar#6949](https://github.com/ChainSafe/lodestar/pull/6949)

</details>


<a id="validator_client-079"></a>
<details>
<summary><b>validator_client-079</b> Size decrypt pool to min(cores, keystores) — <i>n/a · low · cpu, startup</i></summary>

**Idea.** Size the keystore decryption worker pool to min(CPU cores, number of keystores) so no idle workers are spawned.

**Impact.** Not applicable; the related gap (sequential decrypt of uncached keys) is not this idea.

**Best measured result.** decrypt tests time reduced by at least 50% (pr:lodestar#5608)

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/initialized_validators/src/lib.rs:252-290`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/initialized_validators/src/lib.rs#L252-L290)

**Sources.** [lodestar#5608](https://github.com/ChainSafe/lodestar/pull/5608)

</details>


<a id="validator_client-080"></a>
<details>
<summary><b>validator_client-080</b> Cache KDF output for shared salt and password — <i>not · low · M · cpu, startup</i></summary>

**Idea.** When many keystores share the same KDF salt and password, cache the derived decryption key so the expensive KDF runs once, not per keystore.

**Gap in Lighthouse.** No cache keyed on (salt,password,kdf params). Note keystore KDF output depends on the keystore's own salt and Lighthouse-generated keystores have random salts, so benefit only exists for externally generated keystores sharing salt. Would need a derived-key cache in from_definition / Keystore::decrypt_keypair; the key cache already removes KDF cost on restarts.

**Impact.** Only first startup or first import of many same-salt keystores; restarts already hit the key cache. Seconds per key saved at most.

**Best measured result.** significantly improve decoding performance for keystores with single salt and password (pr:nimbus#4372)

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/initialized_validators/src/lib.rs:229-300`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/initialized_validators/src/lib.rs#L229-L300) from_definition decrypts every keystore independently via decrypt_keypair
- [`validator_client/initialized_validators/src/key_cache.rs:36-80`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/initialized_validators/src/key_cache.rs#L36-L80) KeyCache stores one master-encrypted cache so restarts run only one KDF

**Sources.** [nimbus#4372](https://github.com/status-im/nimbus-eth2/pull/4372)

</details>


<a id="validator_client-081"></a>
<details>
<summary><b>validator_client-081</b> Share keystore decryption cache with import API — <i>partial · low · M · cpu, latency</i></summary>

**Idea.** Reuse the startup keystore decryption cache in the keymanager import path so re-importing already-decrypted keystores skips the password KDF.

**Gap in Lighthouse.** Have the import handler pass the keypair it already decrypted to InitializedValidators (e.g. a cache pre-seed) so update_validators skips the second scrypt; the existing comment says restructuring is not trivial.

**Impact.** Saves one scrypt (~0.5-1 s) per imported keystore via keymanager API; only matters for bulk imports.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/http_api/src/keystores.rs:198-204`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/http_api/src/keystores.rs#L198-L204) double decryption comment and decrypt_keypair check
- [`validator_client/initialized_validators/src/lib.rs:252`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/initialized_validators/src/lib.rs#L252) key_cache.get only in from_definition
- [`validator_client/initialized_validators/src/key_cache.rs:236`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/initialized_validators/src/key_cache.rs#L236) add

**Sources.** [nimbus#5443](https://github.com/status-im/nimbus-eth2/pull/5443)

</details>


<a id="validator_client-082"></a>
<details>
<summary><b>validator_client-082</b> Cache decrypted secret keys for signing — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Keep decrypted secret keys in memory in the key manager so signing never re-derives or re-decrypts a key.

**Impact.** Signing uses an in-memory Arc&lt;Keypair&gt;, so there is no KDF or decryption per signature.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/signing_method/src/lib.rs:96`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/signing_method/src/lib.rs#L96)
- [`validator_client/signing_method/src/lib.rs:184-199`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/signing_method/src/lib.rs#L184-L199)
- [`validator_client/initialized_validators/src/lib.rs:252-295`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/initialized_validators/src/lib.rs#L252-L295)

**Skeptic check.** SigningMethod::LocalKeystore holds voting_keypair, and sign() calls voting_keypair.sk.sign directly. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#6667](https://github.com/OffchainLabs/prysm/pull/6667)

</details>


<a id="validator_client-083"></a>
<details>
<summary><b>validator_client-083</b> Unencrypted keys for test clusters — <i>partial · low · S · startup</i></summary>

**Idea.** Allow unencrypted validator key storage in test/devnet setups to skip KDF decryption at startup.

**Gap in Lighthouse.** The cheap KDF exists only behind the insecure_keys feature for in-process test rigs (node_test_rig, validator_test_rig). The VC itself has no unencrypted-keystore or from-mnemonic mode (cf. lodestar fromMnemonic), so a fresh devnet/Kurtosis VC still runs a full scrypt/pbkdf2 per key, one by one, in InitializedValidators::from_definition before the key cache exists.

**Impact.** Test-cluster startup only: avoids ~N x KDF seconds on first start of a devnet VC; no production effect.

**Evidence (Lighthouse @ 928b61e719).**

- [`common/validator_dir/src/insecure_keys.rs:5`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/validator_dir/src/insecure_keys.rs#L5) #![cfg(feature = "insecure_keys")]
- [`common/validator_dir/src/insecure_keys.rs:53-64`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/validator_dir/src/insecure_keys.rs#L53-L64) insecure_kdf scrypt n=2
- [`testing/node_test_rig/src/lib.rs:169`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/testing/node_test_rig/src/lib.rs#L169) only consumer of build_deterministic_validator_dirs
- [`validator_client/initialized_validators/src/lib.rs:252-293`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/initialized_validators/src/lib.rs#L252-L293) full KDF decrypt per key on first start, key_cache only helps restarts

**Skeptic check.** Verified insecure_kdf is test-feature-only and not reachable by lcli or the VC; the earlier claim that cheap KDF has the same effect holds for LH's own simulators but not for devnet VCs that load externally generated keystores.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [prysm#4439](https://github.com/OffchainLabs/prysm/pull/4439), [lodestar#2835](https://github.com/ChainSafe/lodestar/pull/2835)

</details>


<a id="validator_client-084"></a>
<details>
<summary><b>validator_client-084</b> Skip keystore decrypt when creating validator dirs — <i>implemented · low · S · cpu, startup</i></summary>

**Idea.** When creating validator directories, only decrypt the voting keystore if deposit data must be signed, since decryption is slow.

**Impact.** Builder skips the voting-keystore KDF unless a withdrawal keystore/deposit is needed.

**Evidence (Lighthouse @ 928b61e719).**

- [`common/validator_dir/src/builder.rs:169-180`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/validator_dir/src/builder.rs#L169-L180) voting decrypt only inside `if let Some(withdrawal_keystore)` branch
- [`validator_client/http_api/src/keystores.rs:206-210`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/http_api/src/keystores.rs#L206-L210) import builds dir with store_withdrawal_keystore(false), no withdrawal keystore

**Skeptic check.** Confirmed ValidatorDirBuilder::build decrypts only when a withdrawal keystore is supplied (the deposit case); this is LH's own PR #1184, earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#1184](https://github.com/sigp/lighthouse/pull/1184)

</details>


<a id="validator_client-085"></a>
<details>
<summary><b>validator_client-085</b> Skip key cache decrypt with no local keystores — <i>implemented · low · S · cpu, memory, latency</i></summary>

**Idea.** Do not decrypt or save the keystore key cache (scrypt) when no local keystore validators exist, e.g. only remote-signer keys.

**Impact.** Remote-signer-only setups skip key cache decrypt and save.

**Best measured result.** Excessive CPU / slow PATCH validators with hundreds of keys; no numbers (pr:lighthouse#4126)

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/initialized_validators/src/lib.rs:1245-1261`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/initialized_validators/src/lib.rs#L1245-L1261) update_validators gates decrypt_key_cache on has_local_definitions
- [`validator_client/initialized_validators/src/lib.rs:1391`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/initialized_validators/src/lib.rs#L1391) save only if has_local_definitions &amp;&amp; is_modified
- [`validator_client/initialized_validators/src/lib.rs:684-694`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/initialized_validators/src/lib.rs#L684-L694) delete path decrypts cache only when deleting a local keystore (uuid_opt)

**Skeptic check.** Verified update_validators and the delete path; earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#4126](https://github.com/sigp/lighthouse/pull/4126)

</details>


<a id="validator_client-086"></a>
<details>
<summary><b>validator_client-086</b> One KDF per key on load — <i>partial · low · S · cpu, startup</i></summary>

**Idea.** Detect a wrong password from the decryption failure itself instead of running a separate password-check KDF, and load public keys without decrypting, so startup does one KDF per key.

**Gap in Lighthouse.** Startup is one KDF per key, but keymanager API import (keystores::import_single_keystore) runs decrypt_keypair as a password check and then add_validator_keystore -&gt; InitializedValidators::from_definition decrypts again (key_cache does not get the first result), so imports pay two KDFs per key. Fix: pass the decrypted keypair into the key cache / add_validator_keystore.

**Impact.** Halves KDF time of bulk keystore imports over the keymanager API (seconds per key with default scrypt); startup already optimal.

**Evidence (Lighthouse @ 928b61e719).**

- [`crypto/eth2_keystore/src/keystore.rs:381-389`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/eth2_keystore/src/keystore.rs#L381-L389) single derive_key, checksum mismatch -&gt; InvalidPassword
- [`crypto/eth2_keystore/src/keystore.rs:263`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/eth2_keystore/src/keystore.rs#L263) public_key from JSON without decrypt
- [`validator_client/initialized_validators/src/lib.rs:252-293`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/initialized_validators/src/lib.rs#L252-L293) startup: one decrypt_keypair per key, cached in key_cache
- [`validator_client/http_api/src/keystores.rs:197-204`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/http_api/src/keystores.rs#L197-L204) import: separate decrypt_keypair password check, comment admits double decryption
- [`validator_client/http_api/src/lib.rs:581`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/http_api/src/lib.rs#L581) add-keystore endpoint also decrypts before adding

**Skeptic check.** Startup path confirmed as one KDF per key with pubkey read from JSON; the earlier verdict missed the import path, where the code itself documents the double decryption.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [teku#3621](https://github.com/Consensys-Incorporated/teku/pull/3621)

</details>


<a id="validator_client-087"></a>
<details>
<summary><b>validator_client-087</b> Load validator keys only once at startup — <i>n/a · low · cpu, startup</i></summary>

**Idea.** Ensure validator keys are loaded exactly once at startup, not once async and again sync.

**Impact.** Teku-specific bug; not present.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/initialized_validators/src/lib.rs:535-548`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/initialized_validators/src/lib.rs#L535-L548) from_definitions single update_validators

**Sources.** [teku#6760](https://github.com/Consensys-Incorporated/teku/pull/6760)

</details>


<a id="validator_client-088"></a>
<details>
<summary><b>validator_client-088</b> Derive mnemonic keypairs in parallel — <i>not · low · S · cpu, startup</i></summary>

**Idea.** Derive validator keypairs from a mnemonic in parallel across cores, since each derivation is independent and costly.

**Gap in Lighthouse.** Use rayon par_iter over derivation indices in create_validators and account_manager recover (wallet cloned per index); PR #1900 was closed unmerged.

**Impact.** Only one-off key creation/recovery gets faster (scrypt/pbkdf2 per keystore, near-linear in cores); no steady-state node effect.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_manager/src/create_validators.rs:413`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_manager/src/create_validators.rs#L413) sequential for-loop over derivation indices
- [`account_manager/src/validator/recover.rs:109`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/account_manager/src/validator/recover.rs#L109) sequential loop
- [`lcli/src/mnemonic_validators.rs:38`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/lcli/src/mnemonic_validators.rs#L38) only rayon user (par_iter), lcli tool only

**Sources.** [lighthouse#1900](https://github.com/sigp/lighthouse/pull/1900)

</details>


<a id="validator_client-089"></a>
<details>
<summary><b>validator_client-089</b> Flat directory listing for keystore import — <i>not · low · S · startup</i></summary>

**Idea.** Read the keystore directory with a flat listing instead of a recursive filesystem walk when importing accounts.

**Gap in Lighthouse.** Replace the recursive walk with a flat read_dir for the import --directory path; but the directory-tree layout is also used for VC validator discovery, so it only applies to import.

**Impact.** Negligible: a directory listing during a rare one-off import.

**Evidence (Lighthouse @ 928b61e719).**

- [`common/account_utils/src/validator_definitions.rs:477`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/account_utils/src/validator_definitions.rs#L477) recursively_find_voting_keystores walks recursively
- [`account_manager/src/validator/import.rs:122`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/account_manager/src/validator/import.rs#L122) uses it for --directory

**Sources.** [prysm#6785](https://github.com/OffchainLabs/prysm/pull/6785)

</details>


<a id="validator_client-090"></a>
<details>
<summary><b>validator_client-090</b> Poll unknown validator indices once per epoch — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Poll the beacon node for indices of not-yet-known validators once per epoch (not every slot), avoiding repeated large lookups when many keys are unknown.

**Impact.** Unknown pubkeys are queried about once per epoch instead of every slot.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/duties_service.rs:477`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L477) unknown_validator_next_poll_slots
- [`validator_client/validator_services/src/duties_service.rs:936-950`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L936-L950) skip pubkey if next poll slot not reached
- [`validator_client/validator_services/src/duties_service.rs:996-1003`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L996-L1003) Ok(None) -&gt; next poll = current_slot + slots_per_epoch

**Skeptic check.** Confirmed poll_validator_indices throttles not-yet-on-chain keys to one lookup per epoch; on HTTP error no next-poll slot is recorded so it retries next slot, and lookups are still one request per key, but the idea as stated is implemented.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#5628](https://github.com/sigp/lighthouse/pull/5628), [teku#3023](https://github.com/Consensys-Incorporated/teku/pull/3023)

</details>


<a id="validator_client-091"></a>
<details>
<summary><b>validator_client-091</b> Use validator index from duties response — <i>not · low · S · memory, latency, bandwidth</i></summary>

**Idea.** Take validator indices from the duties response (or include them there) instead of separate per-validator index lookups and a VC-side pubkey-to-index map.

**Gap in Lighthouse.** Duties are requested by index, so the index must be known first; Lighthouse resolves it with one HTTP call per validator. Batch via POST /eth/v1/beacon/states/head/validators with ids=[pubkeys] in poll_validator_indices (chunked), then set_validator_index for each result.

**Impact.** Startup and key-import with thousands of keys drops from thousands of BN requests to a handful; steady state unaffected (known indices are cached).

**Best measured result.** "thousands of requests" avoided (pr:prysm#4567)

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/duties_service.rs:911-1010`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L911-L1010) poll_validator_indices does one GET states/head/validators/{pubkey} per unknown pubkey, sequentially
- [`validator_client/validator_services/src/duties_service.rs:1058`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L1058),1281 indices used to request duties

**Sources.** [prysm#4567](https://github.com/OffchainLabs/prysm/pull/4567), [prysm#4634](https://github.com/OffchainLabs/prysm/pull/4634)

</details>


<a id="validator_client-092"></a>
<details>
<summary><b>validator_client-092</b> Prune slashing protection database — <i>implemented · medium · S · cpu, disk, latency</i></summary>

**Idea.** Periodically (and at startup) prune slashing-protection block/attestation records older than a horizon, relying on low-watermark guards, so tables stay small and signing checks stay fast.

**Impact.** DB pruned every epoch to a 1-epoch horizon, at startup and periodically.

**Best measured result.** about 0.5s for 1000 validators and 54,000 epochs (pr:prysm#8221)

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/lighthouse_validator_store/src/lib.rs:60`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/lighthouse_validator_store/src/lib.rs#L60) SLASHING_PROTECTION_HISTORY_EPOCHS = 1
- [`validator_client/lighthouse_validator_store/src/lib.rs:1372-1415`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/lighthouse_validator_store/src/lib.rs#L1372-L1415) prune_slashing_protection_db prunes attestations and blocks
- [`validator_client/src/lib.rs:474-476`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/src/lib.rs#L474-L476) prune at startup
- [`validator_client/validator_services/src/attestation_service.rs:800-822`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/attestation_service.rs#L800-L822) periodic prune spawned at aggregate time on a blocking thread
- [`validator_client/slashing_protection/src/slashing_database.rs:1029-1132`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/slashing_protection/src/slashing_database.rs#L1029-L1132) prune_all_signed_blocks/attestations

**Skeptic check.** Verified; earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#8522](https://github.com/sigp/lighthouse/pull/8522), [prysm#8221](https://github.com/OffchainLabs/prysm/pull/8221), [nimbus#5551](https://github.com/status-im/nimbus-eth2/pull/5551), [lighthouse#2194](https://github.com/sigp/lighthouse/pull/2194)

</details>


<a id="validator_client-093"></a>
<details>
<summary><b>validator_client-093</b> Per-entry sorted slashing protection storage — <i>implemented · low · S · cpu, disk, latency, startup</i></summary>

**Idea.** Store slashing-protection history as individual ordered key/row entries per validator (by source/target epoch) and scan ordered keys with early stop, instead of reading and rewriting a whole encoded history blob per attestation.

**Impact.** Per-row SQLite storage with index prefix on validator_id; no blob rewrite; per-validator rows kept tiny by per-epoch pruning.

**Best measured result.** surround check 1.9ms, 7us, 2.2ms, 1.2ms in worst cases on BoltDB (pr:prysm#8211)

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/slashing_protection/src/slashing_database.rs:96-105`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/slashing_protection/src/slashing_database.rs#L96-L105) signed_attestations one row per (validator_id,target_epoch), UNIQUE index
- [`validator_client/slashing_protection/src/slashing_database.rs:405-475`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/slashing_protection/src/slashing_database.rs#L405-L475) indexed double-vote lookup, surround queries ORDER BY target DESC LIMIT 1
- [`validator_client/slashing_protection/src/slashing_database.rs:1069-1090`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/slashing_protection/src/slashing_database.rs#L1069-L1090) prune_signed_attestations
- [`validator_client/lighthouse_validator_store/src/lib.rs:60`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/lighthouse_validator_store/src/lib.rs#L60) SLASHING_PROTECTION_HISTORY_EPOCHS = 1, :1372 prune each epoch

**Skeptic check.** Verified schema and queries: each attestation is an INSERT of one row and checks are indexed range queries over a few pruned rows, matching the idea's effect.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#8460](https://github.com/OffchainLabs/prysm/pull/8460), [prysm#7248](https://github.com/OffchainLabs/prysm/pull/7248), [prysm#8212](https://github.com/OffchainLabs/prysm/pull/8212), [prysm#8211](https://github.com/OffchainLabs/prysm/pull/8211), [prysm#8219](https://github.com/OffchainLabs/prysm/pull/8219), [nimbus#2094](https://github.com/status-im/nimbus-eth2/pull/2094)

</details>


<a id="validator_client-094"></a>
<details>
<summary><b>validator_client-094</b> Min-max span arrays for surround checks — <i>n/a · low · cpu, disk</i></summary>

**Idea.** Keep per-validator min/max surround span arrays indexed by epoch plus target-indexed attestations so surround/double-vote checks are O(1) lookups instead of history scans.

**Impact.** Lighthouse's DB is pruned to about one epoch of rows so surround scans touch a handful of rows; span arrays would add nothing.

**Best measured result.** O(1) surround detection (no timings) (pr:lodestar#1674)

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/slashing_protection/src/slashing_database.rs:437`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/slashing_protection/src/slashing_database.rs#L437) surround checks are SQL range queries on the pruned table
- [`validator_client/lighthouse_validator_store/src/lib.rs:60`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/lighthouse_validator_store/src/lib.rs#L60) SLASHING_PROTECTION_HISTORY_EPOCHS = 1

**Sources.** [lodestar#1674](https://github.com/ChainSafe/lodestar/pull/1674), [lodestar@41aeb71d3](https://github.com/ChainSafe/lodestar/commit/41aeb71d3a7e), [lodestar@164afae2c](https://github.com/ChainSafe/lodestar/commit/164afae2ca6a), [lodestar#1677](https://github.com/ChainSafe/lodestar/pull/1677)

</details>


<a id="validator_client-095"></a>
<details>
<summary><b>validator_client-095</b> Minimal slashing protection database — <i>implemented · low · S · disk, startup</i></summary>

**Idea.** Keep only the highest signed block slot and highest source/target attestation epochs per validator, shrinking the DB and making checks constant time.

**Impact.** DB stays at ~1-2 rows per validator, so checks are effectively constant time; a strict single-row design would save only a few indexed SQLite queries.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/slashing_protection/src/slashing_database.rs:479-510`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/slashing_protection/src/slashing_database.rs#L479-L510) MIN(source)/MIN(target) lower-bound checks act as watermark
- [`validator_client/slashing_protection/src/slashing_database.rs:1069-1090`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/slashing_protection/src/slashing_database.rs#L1069-L1090) prune keeps rows &gt;= new_min_target and always the max row
- [`validator_client/lighthouse_validator_store/src/lib.rs:60`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/lighthouse_validator_store/src/lib.rs#L60),1372-1422 prune to 1 epoch of history every epoch

**Skeptic check.** Confirmed per-epoch pruning plus lower-bound watermark gives the minimal-DB effect; the prysm PR itself was closed unmerged.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#12475](https://github.com/OffchainLabs/prysm/pull/12475)

</details>


<a id="validator_client-096"></a>
<details>
<summary><b>validator_client-096</b> Snappy-compress stored attestation history — <i>n/a · low · disk</i></summary>

**Idea.** Compress encoded per-validator attestation history with snappy before writing to the validator DB to cut storage and disk I/O.

**Impact.** There is no encoded history blob to compress; rows are pruned to about one epoch.

**Best measured result.** about 25% reduction in storage and disk I/O (pr:prysm#8129)

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/slashing_protection/src/slashing_database.rs:96`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/slashing_protection/src/slashing_database.rs#L96) plain SQLite rows, no encoded history blob

**Sources.** [prysm#8129](https://github.com/OffchainLabs/prysm/pull/8129)

</details>


<a id="validator_client-097"></a>
<details>
<summary><b>validator_client-097</b> Read-only transactions for slashing lookups — <i>n/a · low · disk, latency</i></summary>

**Idea.** Use read-only DB transactions for read-only slashing-protection lookups so they do not take the single writer lock.

**Impact.** SQLite in deliberate exclusive mode serialises all access for safety; it is not bbolt, and read-only concurrency would defeat the cross-process lock.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/slashing_protection/src/slashing_database.rs:158`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/slashing_protection/src/slashing_database.rs#L158) SQLite pool with locking_mode EXCLUSIVE (apply_pragmas)
- [`validator_client/slashing_protection/src/slashing_database.rs:200`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/slashing_protection/src/slashing_database.rs#L200) with_transaction uses Exclusive behavior

**Sources.** [prysm#8434](https://github.com/OffchainLabs/prysm/pull/8434)

</details>


<a id="validator_client-098"></a>
<details>
<summary><b>validator_client-098</b> SQLite exclusive locking for slashing DB — <i>implemented · low · S · disk, latency</i></summary>

**Idea.** Open the slashing-protection SQLite DB in EXCLUSIVE locking mode since only one process uses it, avoiding per-transaction file lock acquire/release.

**Impact.** Already done; no further gain.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/slashing_protection/src/slashing_database.rs:179-183`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/slashing_protection/src/slashing_database.rs#L179-L183) apply_pragmas locking_mode=EXCLUSIVE
- [`validator_client/slashing_protection/src/slashing_database.rs:24`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/slashing_protection/src/slashing_database.rs#L24) POOL_SIZE = 1
- [`validator_client/slashing_protection/src/slashing_database.rs:162-170`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/slashing_protection/src/slashing_database.rs#L162-L170) pragmas applied via with_init on every connection

**Skeptic check.** Verified the EXCLUSIVE locking pragma is set on every pooled connection with a single-connection pool; earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [grandine@1b3c9819c](https://github.com/grandinetech/grandine/commit/1b3c9819ce99)

</details>


<a id="validator_client-099"></a>
<details>
<summary><b>validator_client-099</b> Skip slashing DB writes for remote-signer keys — <i>implemented · low · S · disk, latency</i></summary>

**Idea.** Offer an option to skip local slashing-protection DB checks and writes for keys whose remote signer enforces slashing protection.

**Impact.** Skips local slashing DB I/O for remote-signer keys when opted in; web3signer setups only.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/src/config.rs:404`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/src/config.rs#L404) sets enable_web3signer_slashing_protection from --disable-slashing-protection-web3signer
- [`validator_client/signing_method/src/lib.rs:131-141`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/signing_method/src/lib.rs#L131-L141) requires_local_slashing_protection false for Web3Signer when disabled
- [`validator_client/lighthouse_validator_store/src/lib.rs:499`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/lighthouse_validator_store/src/lib.rs#L499) block path gate
- [`validator_client/lighthouse_validator_store/src/lib.rs:649-655`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/lighthouse_validator_store/src/lib.rs#L649-L655) batched attestation path marks CheckSlashability::No

**Skeptic check.** Confirmed both slashable signing paths (blocks, batched attestations) consult requires_local_slashing_protection; LH's own PR #4981, earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#4981](https://github.com/sigp/lighthouse/pull/4981)

</details>


<a id="validator_client-100"></a>
<details>
<summary><b>validator_client-100</b> Lazy default slashing protection records — <i>implemented · low · S · disk, startup</i></summary>

**Idea.** Return defaults when a key has no slashing-protection entry instead of pre-writing a default record per key at startup, avoiding N transactions on launch.

**Impact.** No N-transaction startup bottleneck; registration is kept on purpose to detect a missing DB.

**Best measured result.** removes a bottleneck for starting a validator client by no longer creating N validator DB transactions (pr:prysm#5323)

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/src/lib.rs:265-268`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/src/lib.rs#L265-L268) register_validators for all voting pubkeys in one call
- [`validator_client/slashing_protection/src/slashing_database.rs:214-244`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/slashing_protection/src/slashing_database.rs#L214-L244) single exclusive transaction, prepared INSERT, only inserts missing keys (existing enabled keys are a SELECT only)

**Skeptic check.** Mechanism differs (eager registration in one transaction, not lazy defaults), but the cost the idea removes is not present; earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#5323](https://github.com/OffchainLabs/prysm/pull/5323)

</details>


<a id="validator_client-101"></a>
<details>
<summary><b>validator_client-101</b> Per-validator slashing protection locks — <i>not · low · L · cpu, memory, latency</i></summary>

**Idea.** Replace the global lock around slashing-protection check-and-record with per-validator locks so distinct validators sign concurrently; only shared storage writes stay serialized.

**Gap in Lighthouse.** Slashing DB is one SQLite file with pool size 1 and EXCLUSIVE transactions, so all signers serialize on it; no per-validator locks. Would need per-key in-memory state with async flush in SlashingDatabase::check_and_insert_*.

**Impact.** Little on a normal node: attestations are batched into one txn per slot, so the lock is held briefly. Matters only for thousands of keys on slow disks.

**Best measured result.** about 2Gb memory for 1000 validating keys (pr:prysm#8086)

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/slashing_protection/src/slashing_database.rs:20`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/slashing_protection/src/slashing_database.rs#L20) POOL_SIZE=1 single sqlite connection
- [`validator_client/slashing_protection/src/slashing_database.rs:646`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/slashing_protection/src/slashing_database.rs#L646) check_and_insert_attestations: one Exclusive txn per batch
- [`validator_client/slashing_protection/src/slashing_database.rs:589`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/slashing_protection/src/slashing_database.rs#L589) block check also Exclusive txn

**Sources.** [prysm#8083](https://github.com/OffchainLabs/prysm/pull/8083), [prysm#8086](https://github.com/OffchainLabs/prysm/pull/8086), [teku#7819](https://github.com/Consensys-Incorporated/teku/pull/7819), [teku#7858](https://github.com/Consensys-Incorporated/teku/pull/7858)

</details>


<a id="validator_client-102"></a>
<details>
<summary><b>validator_client-102</b> Narrow attesting-history lock scope — <i>n/a · low · cpu, latency</i></summary>

**Idea.** Hold the attesting-history lock only around the in-memory map access (with consistent lock order), not across DB reads or saves, to cut contention with many validators.

**Gap in Lighthouse.** Lighthouse keeps no in-memory attesting-history map or lock; all state is in SQLite, serialised by design for safety.

**Impact.** None.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/slashing_protection/src/slashing_database.rs:191`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/slashing_protection/src/slashing_database.rs#L191) with_transaction (exclusive txn, pool size 1)
- [`validator_client/slashing_protection/src/slashing_database.rs:20`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/slashing_protection/src/slashing_database.rs#L20) POOL_SIZE=1

**Sources.** [prysm#8140](https://github.com/OffchainLabs/prysm/pull/8140), [prysm#7936](https://github.com/OffchainLabs/prysm/pull/7936)

</details>


<a id="validator_client-103"></a>
<details>
<summary><b>validator_client-103</b> Lock-free reads of signer state — <i>partial · medium · M · cpu, latency</i></summary>

**Idea.** Make the signing path read validator signer/key state without a contended lock, e.g. via an atomically swapped immutable snapshot or optimistic read lock, so key-management updates do not block signing.

**Gap in Lighthouse.** Signing reads are short, but key management holds the parking_lot write lock over long async work: LighthouseValidatorStore::add_validator holds InitializedValidators.write() across update_validators(), which runs decrypt_key_cache, InitializedValidator::from_definition (keystore scrypt/pbkdf2 decryption) and KeyCache::save. While that runs, every signing_method/voting_pubkeys/get_index read blocks, and because the lock is synchronous it also blocks the tokio worker threads. The fix is an ArcSwap snapshot of the signing map (as grandine does), or doing the decryption and I/O outside the lock and taking the write lock only to swap the result in.

**Impact.** A runtime key import (keymanager API) can stall all signing on the VC for one key-cache decrypt plus keystore decrypt (seconds), which risks missed or late attestations for every validator. No effect when keys are not changed at runtime.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/lighthouse_validator_store/src/lib.rs:9`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/lighthouse_validator_store/src/lib.rs#L9) parking_lot::RwLock (blocking, not async)
- [`validator_client/lighthouse_validator_store/src/lib.rs:186-213`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/lighthouse_validator_store/src/lib.rs#L186-L213) add_validator: #[allow(clippy::await_holding_lock)] with FIXME; self.validators.write().add_definition_replace_disabled(..).await holds the write guard across the await
- [`validator_client/initialized_validators/src/lib.rs:581-612`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/initialized_validators/src/lib.rs#L581-L612) add_definition_replace_disabled -&gt; add_definition -&gt; update_validators().await then definitions.save()
- [`validator_client/initialized_validators/src/lib.rs:1253-1258`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/initialized_validators/src/lib.rs#L1253-L1258) update_validators decrypts the whole key cache ('a very expensive operation') whenever a local definition exists
- [`validator_client/initialized_validators/src/lib.rs:256-260`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/initialized_validators/src/lib.rs#L256-L260) new keystore decryption 'can take several seconds', awaited while the caller holds the write lock
- [`validator_client/initialized_validators/src/lib.rs:1391-1400`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/initialized_validators/src/lib.rs#L1391-L1400) key cache save awaited under the same lock
- [`validator_client/lighthouse_validator_store/src/lib.rs:243-256`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/lighthouse_validator_store/src/lib.rs#L243-L256) doppelganger_checked_signing_method takes validators.read(), so it blocks for the whole import
- [`validator_client/http_api/src/keystores.rs:272`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/http_api/src/keystores.rs#L272) and http_api/src/remotekeys.rs:160 delete paths hold write() over the per-key loop

**Skeptic check.** The earlier evidence was right that the signing path takes only a short read lock, but wrong that key-management writes block it 'only briefly'. add_validator holds the write lock across keystore and key-cache decryption, and the code itself says so in a FIXME/await_holding_lock allow.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [grandine@287eb79be](https://github.com/grandinetech/grandine/commit/287eb79be7c9), [teku#4739](https://github.com/Consensys-Incorporated/teku/pull/4739)

</details>


<a id="validator_client-104"></a>
<details>
<summary><b>validator_client-104</b> Read-lock check before write lock — <i>not · low · S · latency</i></summary>

**Idea.** In the committee subscription API, check under a read lock whether a validator is already tracked and take the write lock only to insert new ones.

**Gap in Lighthouse.** Add a read-lock pre-check (a &amp;self fn that returns false at once when auto_register is off) and take write() only when a validator needs registering, in the beacon and sync committee subscription handlers.

**Impact.** Removes a write-lock acquire per subscription (hundreds per slot for large VCs) that contends with validator monitor readers; likely sub-millisecond total.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/validator/mod.rs:1165-1168`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validator/mod.rs#L1165-L1168) takes validator_monitor.write() per subscription
- [`beacon_node/http_api/src/validator/mod.rs:668-670`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validator/mod.rs#L668-L670) same for sync subscriptions
- [`beacon_node/beacon_chain/src/validator_monitor.rs:1104`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_monitor.rs#L1104) auto_register_local_validator(&amp;mut self) returns early if !auto_register, otherwise checks maps

**Sources.** [lighthouse#2414](https://github.com/sigp/lighthouse/pull/2414)

</details>


<a id="validator_client-105"></a>
<details>
<summary><b>validator_client-105</b> Separate duty locks per role — <i>n/a · low · latency</i></summary>

**Idea.** Key the VC duty lock per role (attester, proposer) so a late attestation cannot delay a block proposal in the same slot.

**Gap in Lighthouse.** Lighthouse VC has no global per-role duty lock; attestation and block services run as independent tasks.

**Impact.** None.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/duties_service.rs:464-477`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L464-L477) only per-map RwLocks for duties data

**Sources.** [prysm#8347](https://github.com/OffchainLabs/prysm/pull/8347)

</details>


<a id="validator_client-106"></a>
<details>
<summary><b>validator_client-106</b> Take duty lock after waiting — <i>n/a · low · latency</i></summary>

**Idea.** Wait until the attestation deadline (1/3 slot) before taking the attester lock so it is not held while idle and does not block proposals.

**Gap in Lighthouse.** No attester lock exists in the Lighthouse VC, so nothing is held while waiting for the 1/3-slot deadline.

**Impact.** None.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/duties_service.rs:464-477`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L464-L477) no duty lock

**Sources.** [prysm#8348](https://github.com/OffchainLabs/prysm/pull/8348)

</details>


<a id="validator_client-107"></a>
<details>
<summary><b>validator_client-107</b> Do not hold locks across beacon node I/O — <i>implemented · low · S · latency</i></summary>

**Idea.** In the fallback status refresh loop, never hold a write lock on shared beacon-node status while awaiting network I/O; lock only to store results.

**Impact.** Already done; nothing more to gain.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/beacon_node_fallback/src/lib.rs:620-623`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/beacon_node_fallback/src/lib.rs#L620-L623) update_all_candidates clones candidates and drops the read lock before I/O
- [`validator_client/beacon_node_fallback/src/lib.rs:625-635`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/beacon_node_fallback/src/lib.rs#L625-L635) refresh_health futures run concurrently via join_all
- [`validator_client/beacon_node_fallback/src/lib.rs:343-354`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/beacon_node_fallback/src/lib.rs#L343-L354) per-candidate health write lock taken only to store the result after I/O

**Skeptic check.** Confirmed: no candidates or health lock is held across the network calls. Only the per-candidate store takes a write lock, after the result arrives.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#3022](https://github.com/sigp/lighthouse/pull/3022)

</details>


<a id="validator_client-108"></a>
<details>
<summary><b>validator_client-108</b> Sign a slot&#x27;s attestations in parallel — <i>implemented · medium · S · cpu, latency</i></summary>

**Idea.** Issue all per-validator signatures for a slot concurrently (CPU thread pool for local BLS, concurrent requests for a remote signer) instead of one after another, so the last attestation is published sooner.

**Impact.** All attestation signatures for a slot are issued concurrently (rayon for local BLS, concurrent HTTP for web3signer).

**Best measured result.** Sequential 32 votes published from 1.61 s to ~2.3 s into the slot; 2/3-wide aggregate p50 6.49 s vs block build at 6.40 s (pr:ethlambda#655)

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/lighthouse_validator_store/src/lib.rs:1022-1043`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/lighthouse_validator_store/src/lib.rs#L1022-L1043) sign_attestations join_all over all per-validator signing futures
- [`validator_client/signing_method/src/lib.rs:184-198`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/signing_method/src/lib.rs#L184-L198) local keystore signing via spawn_blocking_with_rayon_async(HighPriority)
- [`validator_client/lighthouse_validator_store/src/lib.rs:1079-1088`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/lighthouse_validator_store/src/lib.rs#L1079-L1088) slashing protection batch on a blocking thread

**Skeptic check.** Verified; earlier evidence correct (the rayon dispatch is in signing_method, not lib.rs:1085 which is slashing-protection spawn_blocking).

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [ethlambda#655](https://github.com/lambdaclass/ethlambda/pull/655), [lighthouse#8523](https://github.com/sigp/lighthouse/pull/8523), [teku#2571](https://github.com/Consensys-Incorporated/teku/pull/2571), [lodestar#3926](https://github.com/ChainSafe/lodestar/pull/3926)

</details>


<a id="validator_client-109"></a>
<details>
<summary><b>validator_client-109</b> Flatten attestation service task spawning — <i>n/a · low · latency</i></summary>

**Idea.** Replace nested spawn-await-spawn in the attestation service with one top-level spawn and join_all so per-validator work runs concurrently.

**Gap in Lighthouse.** PR 8568 was closed unmerged; the nested spawn remains but it is a code-quality refactor with no measurable latency effect.

**Impact.** Nothing measurable gets cheaper; task spawn costs microseconds.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/attestation_service.rs:346`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/attestation_service.rs#L346) spawn_handle for publication
- [`validator_client/validator_services/src/attestation_service.rs:395`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/attestation_service.rs#L395) outer spawn awaits handle, then spawns per committee at :416

**Sources.** [lighthouse#8568](https://github.com/sigp/lighthouse/pull/8568)

</details>


<a id="validator_client-110"></a>
<details>
<summary><b>validator_client-110</b> Parallel per-slot duty broadcast with sent cache — <i>n/a · low · latency</i></summary>

**Idea.** Sign and broadcast per-slot duty messages in spawned tasks rather than serially in the slot loop, and keep an epoch-pruned cache of already-sent slots to skip rebroadcast.

**Gap in Lighthouse.** Nimbus-specific serial slot loop; Lighthouse already spawns per-duty tasks and signs concurrently.

**Impact.** None.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/attestation_service.rs:232`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/attestation_service.rs#L232) per-slot tasks
- [`validator_client/lighthouse_validator_store/src/lib.rs:1043`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/lighthouse_validator_store/src/lib.rs#L1043) join_all attestation signing

**Sources.** [nimbus#8438](https://github.com/status-im/nimbus-eth2/pull/8438)

</details>


<a id="validator_client-111"></a>
<details>
<summary><b>validator_client-111</b> Parallel attestation aggregation across subnets — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Run aggregation duties for different subnets/committees concurrently instead of sequentially.

**Impact.** Aggregation per committee runs as concurrent tasks.

**Best measured result.** reduces aggregation time ~80% if you run more than 10 validators (pr:prysm#12699)

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/attestation_service.rs:380-427`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/attestation_service.rs#L380-L427) groups duties by committee_index and spawn_ignoring_error(handle_aggregates) per committee

**Skeptic check.** Verified; earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#12699](https://github.com/OffchainLabs/prysm/pull/12699)

</details>


<a id="validator_client-112"></a>
<details>
<summary><b>validator_client-112</b> Skip aggregate fetch without aggregators — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Fetch the aggregated attestation from the BN only if at least one local validator is an aggregator (reusing precomputed selection proofs), and sign/publish aggregates concurrently.

**Impact.** None left.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/attestation_service.rs:645-652`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/attestation_service.rs#L645-L652) early return when no duty has a selection_proof, before any BN fetch
- [`validator_client/validator_services/src/attestation_service.rs:410-425`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/attestation_service.rs#L410-L425) handle_aggregates spawned per committee index, so committees run concurrently
- [`validator_client/validator_services/src/attestation_service.rs:695-715`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/attestation_service.rs#L695-L715) one aggregate fetch per committee, cloned for each aggregator, using the precomputed selection proofs

**Skeptic check.** Confirmed on the attestation aggregate path. Sync contributions are also produced only for the aggregator subset. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#4774](https://github.com/sigp/lighthouse/pull/4774), [nimbus#2722](https://github.com/status-im/nimbus-eth2/pull/2722)

</details>


<a id="validator_client-113"></a>
<details>
<summary><b>validator_client-113</b> Fetch duty types and epochs concurrently — <i>partial · low · S · latency</i></summary>

**Idea.** Fetch current and next epoch duties, and attester, proposer and sync duties within each, concurrently instead of sequentially.

**Gap in Lighthouse.** Duty types run as independent tasks, but within attesters current and next epoch are fetched one after the other (poll_beacon_attesters), and likewise in poll_beacon_proposers. Wrap the two epoch calls in futures::join!.

**Impact.** Halves duty polling latency at epoch boundaries for large key sets; mostly background, not critical path.

**Best measured result.** reduces the time to fetch duties from ~8-9s to ~2.5s (pr:prysm#13789)

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/duties_service.rs:683-857`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L683-L857) separate spawned tasks for proposers, attesters, sync, PTC, IL
- [`validator_client/validator_services/src/duties_service.rs:1066`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L1066) and :1090 current then next epoch attester fetch awaited sequentially
- [`validator_client/validator_services/src/duties_service.rs:1863`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L1863) proposer epochs fetched in sequential for loop

**Sources.** [prysm#13789](https://github.com/OffchainLabs/prysm/pull/13789)

</details>


<a id="validator_client-114"></a>
<details>
<summary><b>validator_client-114</b> Check validator roles in parallel — <i>n/a · low · latency</i></summary>

**Idea.** Determine each key's roles for a slot in parallel across keys so duties start sooner with many keys.

**Gap in Lighthouse.** Lighthouse has no per-key role check at slot time; duties come from BN polling.

**Impact.** None.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/duties_service.rs:591`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L591) attesters(slot) is a lookup of precomputed duties

**Sources.** [prysm#12409](https://github.com/OffchainLabs/prysm/pull/12409)

</details>


<a id="validator_client-115"></a>
<details>
<summary><b>validator_client-115</b> Parallel is-aggregator checks — <i>partial · low · S · cpu, latency</i></summary>

**Idea.** Compute per-duty selection proof and is_aggregator checks concurrently across duties when subscribing to subnets.

**Gap in Lighthouse.** Selection proofs are signed sequentially unless parallel_sign (DVT) is set. Use the FuturesUnordered branch of fill_in_selection_proofs for all setups.

**Impact.** Only many-key remote-signer nodes; proofs are computed ahead of the slot so no critical-path gain.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/duties_service.rs:1589-1660`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L1589-L1660) fill_in_selection_proofs; parallel_sign branch at :1639, FuturesUnordered at :1652
- [`validator_client/validator_services/src/duties_service.rs:147`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L147) make_selection_proof computes is_aggregator

**Sources.** [prysm#17085](https://github.com/OffchainLabs/prysm/pull/17085)

</details>


<a id="validator_client-116"></a>
<details>
<summary><b>validator_client-116</b> Share one HTTP client per remote signer — <i>implemented · medium · S · memory</i></summary>

**Idea.** Create one HTTP client per remote signer URL and reuse it for all validators and requests, so connections are pooled and memory/sockets do not scale per key.

**Impact.** One pooled reqwest Client per Web3SignerDefinition shared by all validators using that signer.

**Best measured result.** VC with 200 keys on Web3Signer: ~200MB to ~50MB (pr:lighthouse#3335)

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/initialized_validators/src/lib.rs:325-357`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/initialized_validators/src/lib.rs#L325-L357)
- [`validator_client/initialized_validators/src/lib.rs:440-451`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/initialized_validators/src/lib.rs#L440-L451)

**Skeptic check.** Verified: client map keyed by Web3SignerDefinition, a hit clones the Arc-backed reqwest Client, so the connection pool is shared. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#2553](https://github.com/Consensys-Incorporated/teku/pull/2553), [lighthouse#3335](https://github.com/sigp/lighthouse/pull/3335), [teku#3202](https://github.com/Consensys-Incorporated/teku/pull/3202)

</details>


<a id="validator_client-117"></a>
<details>
<summary><b>validator_client-117</b> Remote signer keep-alive below server timeout — <i>implemented · low · S · latency</i></summary>

**Idea.** Set the remote signer HTTP keep-alive timeout below the signer's own idle timeout (e.g. 20s vs 30s) so pooled connections are reused, not dropped.

**Impact.** None left.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/initialized_validators/src/lib.rs:50`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/initialized_validators/src/lib.rs#L50) DEFAULT_WEB3SIGNER_KEEP_ALIVE = 20s
- [`validator_client/initialized_validators/src/lib.rs:447-450`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/initialized_validators/src/lib.rs#L447-L450) Client::builder().pool_idle_timeout(keep_alive_timeout)
- [`validator_client/src/cli.rs:540-547`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/src/cli.rs#L540-L547) --web3-signer-keep-alive-timeout default 20000ms
- [`validator_client/initialized_validators/src/lib.rs:327-356`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/initialized_validators/src/lib.rs#L327-L356) one reqwest Client per Web3SignerDefinition, shared across validators

**Skeptic check.** Confirmed: the pooled idle timeout is 20s, below web3signer's 30s, and clients are shared per signer definition, so connections are reused.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#5587](https://github.com/sigp/lighthouse/pull/5587)

</details>


<a id="validator_client-118"></a>
<details>
<summary><b>validator_client-118</b> Sign block header root, not full block — <i>implemented · low · S · bandwidth</i></summary>

**Idea.** Send only the block header/roots to the signer rather than the full block body, shrinking signing requests.

**Impact.** None left for blocks. Phase0/Altair send the full block, which does not matter on mainnet.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/signing_method/src/web3signer.rs:75-80`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/signing_method/src/web3signer.rs#L75-L80) BeaconBlock has optional block and block_header
- [`validator_client/signing_method/src/web3signer.rs:113-150`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/signing_method/src/web3signer.rs#L113-L150) Bellatrix and later send block_header only

**Skeptic check.** Confirmed for block signing. The Gloas ExecutionPayloadEnvelope signing object carries the full envelope, but its format follows the signer API and is not a block-body path, so the verdict stays implemented.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#5049](https://github.com/OffchainLabs/prysm/pull/5049), [teku#5354](https://github.com/Consensys-Incorporated/teku/pull/5354)

</details>


<a id="validator_client-119"></a>
<details>
<summary><b>validator_client-119</b> Throttle concurrent remote signer requests — <i>partial · medium · S · latency, bandwidth</i></summary>

**Idea.** Queue signing requests to the remote signer and cap in-flight requests, since epoch-boundary selection proofs for all keys arrive in bulk.

**Gap in Lighthouse.** The burst this idea targets (selection proofs for all keys at the epoch boundary) is already removed: default mode signs them serially and spreads them across slots. What is still missing is a general cap on in-flight remote-signer requests. Per-slot attestation and aggregate signing uses join_all with no bound, and the DVT/parallel_sign mode signs selection proofs with no bound. To close the gap, add a Semaphore around the Web3Signer requests in SigningMethod.

**Impact.** Small. The epoch-boundary burst is already gone in default mode. A general cap would only smooth the per-slot signing of about 1/32 of the keys, or help DVT setups.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/duties_service.rs:1596-1625`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L1596-L1625) attestation selection proofs are signed in per-slot batches at mid-slot with a lookahead, not all at the epoch boundary
- [`validator_client/validator_services/src/duties_service.rs:1666-1679`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L1666-L1679) in the default (non-DVT) mode, selection proofs are signed serially (stream::iter().then(), one request in flight)
- [`validator_client/src/lib.rs:68-74`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/src/lib.rs#L68-L74),488-511 defaults: lookahead 8 slots, offset slot/2, parallel_sign=false for non-distributed mode
- [`validator_client/validator_services/src/sync.rs:636-680`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/sync.rs#L636-L680) the FuturesUnordered unbounded path runs only when parallel_sign is set (DVT)
- [`validator_client/initialized_validators/src/lib.rs:448-451`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/initialized_validators/src/lib.rs#L448-L451) the web3signer reqwest client sets only pool_max_idle_per_host, with no in-flight cap
- [`validator_client/lighthouse_validator_store/src/lib.rs:1228-1341`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/lighthouse_validator_store/src/lib.rs#L1228-L1341) attestation signing uses join_all with no cap

**Second check.** The earlier review searched only for Semaphore/buffer_unordered. It missed that fill_in_selection_proofs signs serially and in per-slot batches (lookahead 8, mid-slot), which is a scheduling equivalent of throttling the selection-proof burst.

**Verdict history.** not (checked) → partial (refuted)

**Sources.** [teku#3381](https://github.com/Consensys-Incorporated/teku/pull/3381)

</details>


<a id="validator_client-120"></a>
<details>
<summary><b>validator_client-120</b> Prioritize duty signing over registrations — <i>not · low · S · cpu, latency</i></summary>

**Idea.** Put registration signing behind a bounded queue and give aggregation/duty signing priority so slot-critical signing is not starved.

**Gap in Lighthouse.** Registration signing has no bounded queue or priority versus duty signing. Add bounded concurrency in the loop in preparation_service.rs ~395 and leave duty signing unthrottled.

**Impact.** Helps only remote-signer nodes with thousands of keys when registrations are first signed; cached afterwards.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/preparation_service.rs:395-445`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/preparation_service.rs#L395-L445) registrations signed sequentially, with a signed-data cache
- [`validator_client/validator_services/src/preparation_service.rs:218-246`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/preparation_service.rs#L218-L246) separate registration task

**Sources.** [teku#6301](https://github.com/Consensys-Incorporated/teku/pull/6301)

</details>


<a id="validator_client-121"></a>
<details>
<summary><b>validator_client-121</b> Parallel broadcast to fallback nodes with timeout — <i>implemented · low · S · latency</i></summary>

**Idea.** Send VC requests to all fallback beacon nodes in parallel with a timeout on subscription requests, so one slow node does not delay the others.

**Impact.** Already shipped by #6223.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/beacon_node_fallback/src/lib.rs:826-848`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/beacon_node_fallback/src/lib.rs#L826-L848) broadcast() runs func on all candidates with future::join_all
- [`validator_client/src/config.rs:141`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/src/config.rs#L141) broadcast_topics defaults to [Subscriptions]
- [`validator_client/validator_services/src/duties_service.rs:1166`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L1166) subscriptions use request(ApiTopic::Subscriptions)
- [`validator_client/beacon_node_fallback/src/lib.rs:590-594`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/beacon_node_fallback/src/lib.rs#L590-L594) optimized timeouts when more than one BN
- [`common/eth2/src/lib.rs:142-147`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/eth2/src/lib.rs#L142-L147) attestation_subscriptions timeout = slot/QUOTIENT

**Skeptic check.** Confirmed: subscriptions are broadcast in parallel by default, with a short per-call timeout when fallbacks exist.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#6223](https://github.com/sigp/lighthouse/pull/6223)

</details>


<a id="validator_client-122"></a>
<details>
<summary><b>validator_client-122</b> Return on first successful beacon node — <i>not · low · S · latency</i></summary>

**Idea.** When submitting to multiple beacon nodes, return as soon as one accepts (or after a soft timeout, take the first success) and let the remaining calls finish detached.

**Gap in Lighthouse.** broadcast() could race the futures and return on first Ok, leaving the rest detached; first_success could start the next candidate after a soft timeout instead of waiting for the full timeout.

**Impact.** Only helps multi-BN setups with a slow node: cuts tail latency of broadcast topics from the per-call timeout to the fastest BN. Bounded already by per-call timeouts.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/beacon_node_fallback/src/lib.rs:826-852`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/beacon_node_fallback/src/lib.rs#L826-L852) broadcast waits for join_all of every BN
- [`validator_client/beacon_node_fallback/src/lib.rs:717-765`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/beacon_node_fallback/src/lib.rs#L717-L765) first_success awaits candidates sequentially

**Sources.** [prysm#17629](https://github.com/OffchainLabs/prysm/pull/17629), [nimbus#7276](https://github.com/status-im/nimbus-eth2/pull/7276)

</details>


<a id="validator_client-123"></a>
<details>
<summary><b>validator_client-123</b> Per-call slot-fraction timeouts for failover — <i>implemented · low · S · latency</i></summary>

**Idea.** Give each VC-to-BN HTTP call its own timeout as a fraction of slot time, short only when a fallback exists, so a hung BN is abandoned quickly.

**Impact.** Already shipped.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/beacon_node_fallback/src/lib.rs:590-594`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/beacon_node_fallback/src/lib.rs#L590-L594) Timeouts::use_optimized_timeouts only when the list has more than one BN and long timeouts are off
- [`common/eth2/src/lib.rs:142-164`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/eth2/src/lib.rs#L142-L164) every call type gets base_timeout / its own QUOTIENT
- [`common/eth2/src/lib.rs:176-182`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/eth2/src/lib.rs#L176-L182) the timeouts are stored per BeaconNodeHttpClient

**Skeptic check.** Confirmed: each call has its own timeout, a fraction of the slot, and the short timeouts apply only when a fallback exists.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#2352](https://github.com/sigp/lighthouse/pull/2352)

</details>


<a id="validator_client-124"></a>
<details>
<summary><b>validator_client-124</b> Primary beacon node first, fallback on error — <i>implemented · low · S · latency</i></summary>

**Idea.** Send requests only to the primary beacon node while healthy and use fallbacks only after an error.

**Impact.** Default behaviour sends to the best node and falls back on error. Broadcast is opt-in except for subscriptions.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/beacon_node_fallback/src/lib.rs:717-750`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/beacon_node_fallback/src/lib.rs#L717-L750) first_success awaits lazy futures one at a time in health-sorted order and returns on the first Ok
- [`validator_client/beacon_node_fallback/src/lib.rs:855-866`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/beacon_node_fallback/src/lib.rs#L855-L866) request() uses first_success unless the topic is in broadcast_topics
- [`validator_client/src/config.rs:141`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/src/config.rs#L141) only Subscriptions are broadcast by default

**Skeptic check.** Confirmed: Rust futures are lazy, so building all of them up front still sends only to the first healthy node unless it errors.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#4648](https://github.com/ChainSafe/lodestar/pull/4648)

</details>


<a id="validator_client-125"></a>
<details>
<summary><b>validator_client-125</b> Reduce readiness polling of failed nodes — <i>not · low · S · cpu, bandwidth</i></summary>

**Idea.** Poll readiness of failed secondary beacon nodes rarely (e.g. every 60s), skip overlapping checks, and start assuming only the primary is ready.

**Gap in Lighthouse.** update_all_candidates would need per-candidate state to poll Err candidates less often and skip overlapping checks.

**Impact.** Saves a few failed HTTP attempts per slot for users with a dead fallback; negligible CPU or bandwidth.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/beacon_node_fallback/src/lib.rs:72-150`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/beacon_node_fallback/src/lib.rs#L72-L150) updater loop calls update_all_candidates every slot
- [`validator_client/beacon_node_fallback/src/lib.rs:620-640`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/beacon_node_fallback/src/lib.rs#L620-L640) polls all candidates including failed ones concurrently

**Sources.** [teku#9567](https://github.com/Consensys-Incorporated/teku/pull/9567)

</details>


<a id="validator_client-126"></a>
<details>
<summary><b>validator_client-126</b> Targeted beacon node status checks — <i>not · low · M · cpu, latency</i></summary>

**Idea.** Check only the BN status properties relevant to each API call instead of full checks on every node, allowing optimistic/unsynced nodes where safe.

**Gap in Lighthouse.** Would need per-API-call health requirements (e.g. allow optimistic for duties) in candidate selection instead of one global sort.

**Impact.** Mostly resilience, not speed; minor reduction in status requests.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/beacon_node_fallback/src/lib.rs:291-340`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/beacon_node_fallback/src/lib.rs#L291-L340) refresh_health always runs is_compatible plus check_node_health with all fields
- [`validator_client/beacon_node_fallback/src/beacon_node_health.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/beacon_node_fallback/src/beacon_node_health.rs) health tiers by sync distance, optimistic, EL

**Sources.** [nimbus#4635](https://github.com/status-im/nimbus-eth2/pull/4635)

</details>


<a id="validator_client-127"></a>
<details>
<summary><b>validator_client-127</b> Poll next-epoch duties before boundary — <i>implemented · low · S · latency</i></summary>

**Idea.** Fetch next-epoch proposer duties shortly before the epoch boundary, after the BN precomputes the next-epoch state, so the first-slot proposer is known without delay.

**Impact.** Next-epoch proposer duties are already cached in the VC before the boundary; the BN serves current_epoch+1 from head.

**Best measured result.** polling at epoch start wasted up to 2 s causing missed proposals (pr:lodestar#5794)

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/duties_service.rs:706-718`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L706-L718)
- [`validator_client/validator_services/src/duties_service.rs:1881-1884`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L1881-L1884)
- [`beacon_node/http_api/src/proposer_duties.rs:91-108`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/proposer_duties.rs#L91-L108)

**Skeptic check.** Verified: poll_beacon_proposers runs every slot and fetches current_epoch and current_epoch+1, and the BN answers next-epoch requests via compute_proposer_duties_from_head. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#5794](https://github.com/ChainSafe/lodestar/pull/5794)

</details>


<a id="validator_client-128"></a>
<details>
<summary><b>validator_client-128</b> Recompute duties only after reorg ancestor — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** On reorg, find the common ancestor and recompute duties only for epochs after it; late-block reorgs need no recompute.

**Impact.** Equivalent: only epochs whose dependent_root changed (reorg deeper than the shuffling boundary) get duties and proofs recomputed; late-block reorgs leave the current-epoch dependent root unchanged.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/duties_service.rs:1220-1273`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L1220-L1273) poll_beacon_attesters_for_epoch queries a small sample, compares (epoch, dependent_root) per validator and refetches only mismatches
- [`validator_client/validator_services/src/duties_service.rs:1370-1382`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L1370-L1382) selection proofs recomputed only for new_duties
- [`validator_client/validator_services/src/duties_service.rs:1875-1884`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L1875-L1884) proposer duties also keyed by dependent_root

**Skeptic check.** Verified the dependent_root comparison in poll_beacon_attesters_for_epoch; LH uses dependent roots instead of an explicit common-ancestor search, with the same effect. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#2682](https://github.com/Consensys-Incorporated/teku/pull/2682)

</details>


<a id="validator_client-129"></a>
<details>
<summary><b>validator_client-129</b> Target roots in head event — <i>not · low · M · cpu</i></summary>

**Idea.** Include current and previous target/dependent roots in the head event so VCs recalc duties only when those change.

**Gap in Lighthouse.** Pass SseHead dependent roots through HeadEvent and have the duties service skip the per-slot duties POST when they match the cached roots.

**Impact.** Saves roughly one attester duties request per slot per VC; small on BN load.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/beacon_node_fallback/src/beacon_head_monitor.rs:15-20`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/beacon_node_fallback/src/beacon_head_monitor.rs#L15-L20) HeadEvent has only index, slot, block root
- [`validator_client/validator_services/src/duties_service.rs:1254`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L1254) duties are re-polled each slot and compared by dependent_root
- [`common/eth2/src/types.rs:1212`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/eth2/src/types.rs#L1212) SseHead has current/previous_duty_dependent_root but VC ignores them

**Sources.** [teku#3210](https://github.com/Consensys-Incorporated/teku/pull/3210)

</details>


<a id="validator_client-130"></a>
<details>
<summary><b>validator_client-130</b> Skip redundant next-epoch duties request — <i>n/a · low · S · latency, bandwidth</i></summary>

**Idea.** Do not request next-epoch duties separately when the previous response already contained them.

**Impact.** Standard HTTP API duties are per-epoch, so the next-epoch request is a distinct call; the Prysm saving came from its older RPC that returned both epochs. The PR was closed unmerged.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/duties_service.rs:1085`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L1085) separate next-epoch poll with its own dependent_root check

**Sources.** [prysm#8204](https://github.com/OffchainLabs/prysm/pull/8204)

</details>


<a id="validator_client-131"></a>
<details>
<summary><b>validator_client-131</b> Skip attestation data without duties — <i>implemented · low · S · cpu, latency, bandwidth</i></summary>

**Idea.** Do not request attestation data (or wait for the deadline) in slots with no local attestation duties.

**Impact.** Saves one attestation_data request and the deadline wait per slot without local duties.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/attestation_service.rs:250-263`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/attestation_service.rs#L250-L263) spawn_attestation_tasks returns before any attestation_data request when attesters(slot) is empty
- [`validator_client/validator_services/src/duties_service.rs:591-610`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L591-L610) attesters(slot)

**Skeptic check.** spawn_attestation_tasks is the only attestation production path (post-Electra single task) and the early return precedes the data fetch. Earlier evidence correct (this is LH PR #8559).

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#8962](https://github.com/status-im/nimbus-eth2/pull/8962), [lighthouse#8559](https://github.com/sigp/lighthouse/pull/8559)

</details>


<a id="validator_client-132"></a>
<details>
<summary><b>validator_client-132</b> Skip duty requests with no active keys — <i>implemented · low · S · cpu, bandwidth</i></summary>

**Idea.** Skip all duty requests to the BN when the VC has no active keys.

**Impact.** No duty requests to the BN when the VC has no active keys.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/duties_service.rs:1226-1233`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L1226-L1233) attester poll returns when local_indices empty
- [`validator_client/validator_services/src/duties_service.rs:1875-1884`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L1875-L1884) proposer duties fetched only if local_pubkeys non-empty
- [`validator_client/validator_services/src/sync.rs:428-441`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/sync.rs#L428-L441) sync duty poll returns when local_indices empty

**Skeptic check.** All three duty polls (attester, proposer, sync) short-circuit on empty key sets. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#4380](https://github.com/Consensys-Incorporated/teku/pull/4380)

</details>


<a id="validator_client-133"></a>
<details>
<summary><b>validator_client-133</b> Skip empty validators query — <i>n/a · low · S · cpu, bandwidth</i></summary>

**Idea.** Do not send a POST validators request with an empty id list, since the BN treats it as all validators.

**Impact.** VC never POSTs the validators list with ids, only single-pubkey GETs for unknown keys, so the empty-list pitfall cannot occur.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/duties_service.rs:962`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L962) index resolution uses GET validators/{id} per single pubkey
- [`common/eth2/src/lib.rs:902`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/eth2/src/lib.rs#L902) post_beacon_states_validators exists but VC does not call it

**Sources.** [nimbus#8826](https://github.com/status-im/nimbus-eth2/pull/8826)

</details>


<a id="validator_client-134"></a>
<details>
<summary><b>validator_client-134</b> DVT selections once per epoch — <i>implemented · low · S · cpu, latency, bandwidth</i></summary>

**Idea.** In distributed validator mode, submit beacon committee selections to the selections endpoint once per epoch (current and next) instead of per slot.

**Impact.** DVT only: selections endpoint called once per epoch (current and next) instead of per slot.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/duties_service.rs:1371-1378`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L1371-L1378) selections_endpoint branch spawns fill_in_selection_proofs_selections_endpoint per epoch of new duties
- [`validator_client/validator_services/src/duties_service.rs:1713-1760`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L1713-L1760) one make_beacon_committee_selection call per epoch, retried per slot only on failure
- [`validator_client/validator_services/src/duties_service.rs:171-200`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L171-L200) make_beacon_committee_selection batches all duties of the epoch

**Skeptic check.** Confirmed the per-epoch batching from LH PR #8699; the loop only repeats on error. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#8669](https://github.com/ChainSafe/lodestar/pull/8669), [lighthouse#8699](https://github.com/sigp/lighthouse/pull/8699)

</details>


<a id="validator_client-135"></a>
<details>
<summary><b>validator_client-135</b> Reuse duty data instead of extra requests — <i>implemented · low · S · latency</i></summary>

**Idea.** Use data already in the duty (committees per slot, committee length, aggregator index) for subnet subscription and aggregation rather than re-querying the BN.

**Impact.** Subscriptions and aggregator selection use AttesterData fields; no extra BN queries.

**Best measured result.** reduces the time needed to subscribe from 1-2 seconds to 1 millisecond (pr:prysm#13702)

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/duties_service.rs:152-158`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L152-L158)
- [`validator_client/validator_services/src/duties_service.rs:1135-1157`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L1135-L1157)

**Skeptic check.** Verified: BeaconCommitteeSubscription is built from duty.committee_index/committees_at_slot and is_aggregator uses duty.committee_length. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#13702](https://github.com/OffchainLabs/prysm/pull/13702), [prysm#13711](https://github.com/OffchainLabs/prysm/pull/13711)

</details>


<a id="validator_client-136"></a>
<details>
<summary><b>validator_client-136</b> Reuse duty statuses for exit check — <i>n/a · low · S · cpu, bandwidth</i></summary>

**Idea.** Derive the all-validators-exited check from statuses already in the duties response instead of a separate status query each epoch.

**Impact.** VC has no separate all-validators-exited status query each epoch, so nothing to elide.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/notifier_service.rs:137`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/notifier_service.rs#L137) active/inactive counts computed from local store, no BN query
- duties_service.rs:911 poll_validator_indices only queries unknown pubkeys

**Sources.** [prysm#12505](https://github.com/OffchainLabs/prysm/pull/12505)

</details>


<a id="validator_client-137"></a>
<details>
<summary><b>validator_client-137</b> Remove redundant head API call — <i>n/a · low · S · latency</i></summary>

**Idea.** Drop an extra canonical-head API call before duties fetch; use the wall-clock current slot.

**Impact.** Lighthouse already takes current slot from the wall clock and makes no canonical-head call before fetching duties.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/duties_service.rs:1031`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L1031) poll_beacon_attesters uses slot_clock.now()
- grep of validator_client finds no get_beacon_headers / head call before duties

**Sources.** [prysm#15480](https://github.com/OffchainLabs/prysm/pull/15480)

</details>


<a id="validator_client-138"></a>
<details>
<summary><b>validator_client-138</b> Memoize genesis from beacon node — <i>implemented · low · S · latency</i></summary>

**Idea.** Fetch genesis info once and memoize it rather than requesting it on every call.

**Impact.** Genesis comes from the network config or one startup BN call.

**Best measured result.** for 1024 keys as many as 7 requests per second, becoming 1 total (pr:prysm#13796)

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/src/lib.rs:388-397`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/src/lib.rs#L388-L397)
- [`validator_client/src/lib.rs:834`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/src/lib.rs#L834)

**Skeptic check.** Verified: the only get_beacon_genesis call in the VC is at startup; beacon_node_fallback health checks do not fetch genesis. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#13796](https://github.com/OffchainLabs/prysm/pull/13796)

</details>


<a id="validator_client-139"></a>
<details>
<summary><b>validator_client-139</b> Fee recipient calls only for configured keys — <i>implemented · low · S · latency, bandwidth</i></summary>

**Idea.** Avoid per-validator fee recipient lookups against the BN and send prepare-proposer/registration only for keys with a configured fee recipient.

**Impact.** Fee recipients come from the local validator store; no per-validator BN lookups; only configured keys are sent.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/preparation_service.rs:262-290`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/preparation_service.rs#L262-L290) prepare_proposers_and_publish/collect_preparation_data include only keys with Some(fee_recipient) and an index, skip publish if empty
- [`validator_client/validator_services/src/preparation_service.rs:292-300`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/preparation_service.rs#L292-L300) collect_validator_registration_keys skips keys without index/fee recipient

**Skeptic check.** Verified the fee recipient is read locally via collect_proposal_data and filtered. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#11970](https://github.com/OffchainLabs/prysm/pull/11970)

</details>


<a id="validator_client-140"></a>
<details>
<summary><b>validator_client-140</b> No duplicate registration calls at startup — <i>implemented · low · S · bandwidth, startup</i></summary>

**Idea.** Send validator registrations once at startup, not both explicitly and via an epoch scheduler that fires immediately.

**Impact.** Registrations are sent once at startup (as changed keys) and periodically; no duplicate startup call.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/preparation_service.rs:215-243`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/preparation_service.rs#L215-L243) start_validator_registration_service is the only registration sender
- [`validator_client/validator_services/src/preparation_service.rs:359-386`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/preparation_service.rs#L359-L386) register_validators sends only changed keys or all keys every EPOCHS_PER_VALIDATOR_REGISTRATION_SUBMISSION
- [`validator_client/src/lib.rs:640-655`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/src/lib.rs#L640-L655) pre-genesis loop sends proposer preparations, not registrations

**Skeptic check.** The registration cache makes a second send at startup impossible except on the periodic slot boundary. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#5993](https://github.com/ChainSafe/lodestar/pull/5993)

</details>


<a id="validator_client-141"></a>
<details>
<summary><b>validator_client-141</b> Prune registration cache for inactive keys — <i>partial · low · S · memory</i></summary>

**Idea.** Key the builder registration cache by pubkey and prune entries for validators no longer active.

**Gap in Lighthouse.** Cache is never pruned: old entries for changed fee recipient/gas limit or removed/inactive validators stay. Retain only keys returned by collect_validator_registration_keys in register_validators.

**Impact.** Tiny memory saving on VC with many keys that change config; no CPU or network gain.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/preparation_service.rs:124`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/preparation_service.rs#L124) cache keyed by ValidatorRegistrationKey (fee_recipient,gas_limit,pubkey)
- validator_client/preparation_service.rs:462 only inserts, never removes

**Sources.** [teku#5748](https://github.com/Consensys-Incorporated/teku/pull/5748)

</details>


<a id="validator_client-142"></a>
<details>
<summary><b>validator_client-142</b> Skip current-slot sync selection proofs — <i>implemented · low · S · cpu</i></summary>

**Idea.** Do not compute sync committee selection proofs for the current slot, since aggregation already happened in the previous slot.

**Impact.** Sync selection proofs for the current slot are not computed.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/sync.rs:624-636`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/sync.rs#L624-L636) fill_in_aggregation_proofs starts at current_slot + 1

**Skeptic check.** This is LH PR #7551 itself; the code starts at current_slot + 1 with an explicit comment. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#7551](https://github.com/sigp/lighthouse/pull/7551)

</details>


<a id="validator_client-143"></a>
<details>
<summary><b>validator_client-143</b> Precompute own committee membership ahead — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Compute local validators' committee membership and aggregator selection proofs a few slots ahead once, and reuse it for attesting, aggregating and subscriptions; skip empty subnet updates.

**Impact.** Committee membership and aggregator proofs computed once ahead and reused by attestation, aggregation and subscription paths.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/duties_service.rs:1581-1700`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L1581-L1700) fill_in_selection_proofs computes aggregator selection proofs lookahead_slot ahead and stores them in DutyAndProof
- [`validator_client/validator_services/src/duties_service.rs:591-610`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L591-L610) attesters(slot) reuses stored duties for attesting and aggregating
- [`validator_client/validator_services/src/duties_service.rs:1135-1162`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L1135-L1162) subscriptions built from stored duties, POST skipped when empty
- [`validator_client/validator_services/src/sync.rs:105-130`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/sync.rs#L105-L130) prepare_for_aggregator_pre_compute for sync

**Skeptic check.** Verified duties and proofs are stored once per epoch per dependent_root and reused; empty subscription batches are not posted. Earlier evidence correct (one path cited without the validator_services/src prefix).

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [grandine@0123f8ff4](https://github.com/grandinetech/grandine/commit/0123f8ff455e)

</details>


<a id="validator_client-144"></a>
<details>
<summary><b>validator_client-144</b> Staggered subnet subscriptions with retry — <i>implemented · low · S · cpu, bandwidth</i></summary>

**Idea.** Send each attestation subnet subscription only a few times ahead of the slot and retry only on failure, instead of every slot to every node.

**Impact.** Per-duty staggered subscriptions with retry on failure are in place (this is LH's own PR #4806).

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/duties_service.rs:51`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L51) ATTESTATION_SUBSCRIPTION_OFFSETS [3,4,5,6,7,8,16,32]
- [`validator_client/validator_services/src/duties_service.rs:246-282`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L246-L282) SubscriptionSlots::new/should_send_subscription_at/record_successful_subscription_at
- [`validator_client/validator_services/src/duties_service.rs:1140-1200`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L1140-L1200) only due subscriptions sent; marked sent on success or partial success; retried next slot when all BNs fail

**Skeptic check.** Verified SubscriptionSlots schedules a few sends per duty and only marks them done on success, so a total failure is retried at the next slot. Earlier evidence was right; the second path cited was missing the validator_services/src prefix.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#4806](https://github.com/sigp/lighthouse/pull/4806)

</details>


<a id="validator_client-145"></a>
<details>
<summary><b>validator_client-145</b> Cache sync duties, skip doppelganger for inactive — <i>implemented · low · S · cpu, bandwidth</i></summary>

**Idea.** Cache sync committee duties so subscriptions are not resent every slot, and skip doppelganger checks for not-yet-active validators.

**Impact.** Sync duties are cached per period, and subscriptions go out per epoch, not per slot (except in the 4-epoch lookahead, which is on purpose). Validators that have no index are not queried for doppelganger.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/sync_committee_service.rs:539-560`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/sync_committee_service.rs#L539-L560) publish_subscriptions: current-period subscriptions only on first run and at epoch start; next-period every slot only in the 4-epoch lookahead
- [`validator_client/validator_services/src/sync.rs:88`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/sync.rs#L88) all_duties_known caches duties per period
- [`validator_client/doppelganger_service/src/lib.rs:400-430`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/doppelganger_service/src/lib.rs#L400-L430) compute_detection_indices_map omits validators with no index

**Skeptic check.** Verified the subscription cadence and per-period caching. Pending validators that already have an index still get liveness checks, but that adds one index to a single POST and the detection period finishes while they are pending, so there is no effective gap.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#4240](https://github.com/status-im/nimbus-eth2/pull/4240)

</details>


<a id="validator_client-146"></a>
<details>
<summary><b>validator_client-146</b> Doppelganger liveness only for due validators — <i>not · low · S · bandwidth</i></summary>

**Idea.** Only query liveness for validators whose next doppelganger check epoch is now.

**Gap in Lighthouse.** In compute_detection_indices_map also filter validators whose next_check_epoch is not yet due (previous_epoch &gt;= next_check_epoch, as in lib.rs:566). Lighthouse intentionally polls every slot for fast detection, so this trades detection latency.

**Impact.** Fewer indices in liveness POSTs for the first few epochs after adding keys; negligible on steady-state nodes.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/doppelganger_service/src/lib.rs:243`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/doppelganger_service/src/lib.rs#L243) check every slot at 75%
- validator_client/lib.rs:400 filter only by requires_further_checks, not next_check_epoch
- validator_client/lib.rs:99 two liveness requests (prev+current epoch) per run

**Sources.** [lodestar#5991](https://github.com/ChainSafe/lodestar/pull/5991), [prysm#11835](https://github.com/OffchainLabs/prysm/pull/11835)

</details>


<a id="validator_client-147"></a>
<details>
<summary><b>validator_client-147</b> No-op sync duties without assignments — <i>implemented · low · S · cpu, bandwidth</i></summary>

**Idea.** Treat a sync committee duty as a no-op with no subscriptions when there are no assignments or no head state.

**Impact.** No-op paths exist already.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/sync_committee_service.rs:217-225`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/sync_committee_service.rs#L217-L225) no duties known or empty duties -&gt; return before any work
- [`validator_client/validator_services/src/sync_committee_service.rs:566-597`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/sync_committee_service.rs#L566-L597) no duty slots / empty subscriptions -&gt; no request

**Skeptic check.** Verified the early returns in the sync committee slot task and in publish_subscriptions. Earlier evidence was right; two paths were missing the validator_services/src prefix.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#4376](https://github.com/Consensys-Incorporated/teku/pull/4376)

</details>


<a id="validator_client-148"></a>
<details>
<summary><b>validator_client-148</b> Hash map index of local pubkeys — <i>partial · low · S · cpu</i></summary>

**Idea.** Index local validators by pubkey in a hash map for duty and known-validator checks instead of linear scans.

**Gap in Lighthouse.** poll_beacon_attesters_for_epoch builds validators_to_update as a Vec&lt;&amp;PublicKeyBytes&gt; and filters the response with validators_to_update.contains(&amp;&amp;duty.pubkey). It also filters indices with initial_indices_to_request.contains (a slice). When uninitialized validators exist (startup, newly added keys), both have N entries, so the result is O(N^2): about 1e8 48-byte compares for 10k keys, for both the current and the next epoch. Fix: collect validators_to_update and the initial indices into a HashSet.

**Impact.** Only at startup or when keys are added; on the steady-state path the initial query is a single index and lookups are hashed. Can cost a fraction of a second of CPU per epoch poll for VCs with very large key counts.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/duties_service.rs:325`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L325) AttesterMap HashMap&lt;PublicKeyBytes,..&gt;
- [`validator_client/validator_services/src/duties_service.rs:1050`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L1050),1875,2119 local_pubkeys HashSet used for proposer/sync/ptc filtering
- [`validator_client/validator_services/src/duties_service.rs:1246-1290`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L1246-L1290) poll_beacon_attesters_for_epoch: validators_to_update is a Vec, initial_indices_to_request is a slice; `.contains` inside per-duty filters

**Skeptic check.** The hot per-slot lookups (validator_index, attesters, doppelganger states, initialized validators) are HashMaps, so the earlier evidence is right for them. The earlier check missed the Vec/slice contains scans in poll_beacon_attesters_for_epoch, which go quadratic when all validators are uninitialized.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [nimbus#4590](https://github.com/status-im/nimbus-eth2/pull/4590), [lodestar@bd62a6cf7](https://github.com/ChainSafe/lodestar/commit/bd62a6cf7a37)

</details>


<a id="validator_client-149"></a>
<details>
<summary><b>validator_client-149</b> Map lookup for committee selections — <i>implemented · low · S · cpu</i></summary>

**Idea.** Index combined committee selections in a map keyed by duty rather than scanning a list per duty.

**Impact.** Combined selections are looked up through a HashMap keyed by (validator_index, slot). This is the same as Lodestar #8710, and LH also checks the slot.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/duties_service.rs:1759-1772`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L1759-L1772) selection_hashmap keyed by (validator_index, slot), O(1) remove per duty
- [`validator_client/validator_services/src/duties_service.rs:173-231`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L173-L231) make_beacon_committee_selection one call per epoch

**Skeptic check.** Verified the real mechanism at duties_service.rs:1760, which the earlier evidence did not cite (it cited the selection construction and the attestation_service grouping). The verdict stands.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#8710](https://github.com/ChainSafe/lodestar/pull/8710)

</details>


<a id="validator_client-150"></a>
<details>
<summary><b>validator_client-150</b> Fixed-size byte array as pubkey map key — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Key validator maps by a fixed 48-byte array instead of a string to avoid allocation and marshalling.

**Impact.** Keys are already fixed-size arrays; nothing to gain.

**Evidence (Lighthouse @ 928b61e719).**

- [`crypto/bls/src/generic_public_key_bytes.rs:20-23`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/generic_public_key_bytes.rs#L20-L23) GenericPublicKeyBytes { bytes: [u8; 48] }
- [`validator_client/validator_services/src/duties_service.rs:325`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L325) maps keyed by PublicKeyBytes

**Skeptic check.** Verified that PublicKeyBytes wraps [u8; 48] and that VC maps are keyed by it. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#3716](https://github.com/OffchainLabs/prysm/pull/3716)

</details>


<a id="validator_client-151"></a>
<details>
<summary><b>validator_client-151</b> Shared buffer for pubkey hex encoding — <i>n/a · low · cpu, memory</i></summary>

**Idea.** Reuse one buffer for hex-encoding pubkeys in hot duty paths instead of allocating per call.

**Impact.** Rust keys are fixed byte arrays, not hex strings, on hot duty paths; hex only at API/log edges.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/duties_service.rs:1420`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L1420) only to_string of validator_index in metrics

**Sources.** [lodestar#7569](https://github.com/ChainSafe/lodestar/pull/7569)

</details>


<a id="validator_client-152"></a>
<details>
<summary><b>validator_client-152</b> Single-allocation lock key construction — <i>n/a · low · cpu, memory</i></summary>

**Idea.** Build per-duty lock keys in one allocation instead of formatting and concatenation.

**Impact.** Lighthouse does not build string lock keys per duty.

**Best measured result.** 397 ns/op to 245 ns/op, 432 B/op to 408 B/op (pr:prysm#8349)

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/duties_service.rs:325`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L325) maps keyed by (PublicKeyBytes, Epoch) structurally, no formatted string lock keys

**Sources.** [prysm#8349](https://github.com/OffchainLabs/prysm/pull/8349)

</details>


<a id="validator_client-153"></a>
<details>
<summary><b>validator_client-153</b> Preallocate target-epochs slice — <i>n/a · low · memory</i></summary>

**Idea.** Pre-size collections of target epochs in slashing code to avoid regrowth.

**Impact.** Slashing protection is SQL-backed with no target-epoch vector to preallocate.

**Best measured result.** 'minor improvement' (pr:prysm#8452)

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/slashing_protection/src/slashing_database.rs:411-467`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/slashing_protection/src/slashing_database.rs#L411-L467) uses SQLite queries by target_epoch, no in-memory target epoch slice

**Sources.** [prysm#8452](https://github.com/OffchainLabs/prysm/pull/8452)

</details>


<a id="validator_client-154"></a>
<details>
<summary><b>validator_client-154</b> Hoist registry scan out of per-key status — <i>n/a · low · cpu</i></summary>

**Idea.** When resolving status for many pubkeys, compute the last-active-validator index once per state instead of per pubkey.

**Impact.** The VC resolves pubkey to index per key via the BN pubkey cache; there is no last-active-validator registry scan to hoist.

**Best measured result.** for large operators this is a strain (no numbers) (pr:prysm#12487)

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/duties_service.rs:911-1000`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L911-L1000) resolves index per unknown pubkey via get_beacon_states_validator_id
- [`beacon_node/http_api/src/attester_duties.rs:210`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/attester_duties.rs#L210) pubkey lookups via pubkey cache

**Sources.** [prysm#12487](https://github.com/OffchainLabs/prysm/pull/12487)

</details>


<a id="validator_client-155"></a>
<details>
<summary><b>validator_client-155</b> Single-pass multi-key committee assignments — <i>partial · low · S · cpu, memory, latency</i></summary>

**Idea.** Compute committee assignments for all requested keys in one pass over the epoch's committees instead of per-key scans.

**Gap in Lighthouse.** No O(validators) scan per key (shuffled_position is O(1)), but each index scans up to 2048 committees to find its range. A binary search over compute_committee_range in CommitteeCache::get_attestation_duties would remove it.

**Impact.** Negligible: a few thousand integer comparisons per key per epoch on the BN.

**Best measured result.** 16k validators: 182708160 ns/op, 85 MB/op; previously over 4 minutes for 8k validators (pr:prysm#4294)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/committee_cache.rs:295`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/committee_cache.rs#L295) get_attestation_duties: O(1) shuffled_position then linear scan over committees per validator
- [`beacon_node/http_api/src/attester_duties.rs:15`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/attester_duties.rs#L15) per-index duties from cached CommitteeCache

**Sources.** [prysm#4294](https://github.com/OffchainLabs/prysm/pull/4294)

</details>


<a id="validator_client-156"></a>
<details>
<summary><b>validator_client-156</b> Use epoch committee cache for attestations — <i>n/a · low · cpu</i></summary>

**Idea.** Use cached epoch shuffling/committees when producing attestations instead of recomputing committees from state.

**Impact.** The VC does not compute committees from state; the BN serves duties and attestation data, so the BN's committee cache applies.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/attestation_service.rs:258`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/attestation_service.rs#L258) duties come from BN attester duties API
- [`validator_client/validator_services/src/attestation_service.rs:268`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/attestation_service.rs#L268) attestation data fetched from BN

**Sources.** [nimbus#1478](https://github.com/status-im/nimbus-eth2/pull/1478)

</details>


<a id="validator_client-157"></a>
<details>
<summary><b>validator_client-157</b> Avoid state copies for selection proof serving — <i>n/a · low · S · cpu, memory, latency</i></summary>

**Idea.** Compute active indices and seed from the shared head state rather than copying the state several times per aggregate-selection request.

**Impact.** None: no per-request state copies exist on this path, and BeaconState clones are cheap (milhouse persistent tree).

**Best measured result.** reduces 3 state copies to 1 per call (pr:prysm#5813)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/aggregate_attestation.rs:12`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/aggregate_attestation.rs#L12) get_aggregate_attestation looks up the naive aggregation pool by data root, no state load or copy
- Lighthouse selection proofs are signed in the validator client; the BN endpoint does not compute active indices or seed

**Sources.** [prysm#5813](https://github.com/OffchainLabs/prysm/pull/5813)

</details>


<a id="validator_client-158"></a>
<details>
<summary><b>validator_client-158</b> Status from state for active validators — <i>n/a · low · latency, startup</i></summary>

**Idea.** Derive validator status from the beacon state when the validator is already active, skipping eth1 deposit RPC lookups.

**Impact.** VC resolves validator indices through the BN state API; it makes no eth1 deposit RPC lookups.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/duties_service.rs:477`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L477) unknown_validator_next_poll_slots; index resolved via BN validators endpoint

**Sources.** [prysm#5300](https://github.com/OffchainLabs/prysm/pull/5300)

</details>


<a id="validator_client-159"></a>
<details>
<summary><b>validator_client-159</b> No state regen for error logging — <i>n/a · low · S · cpu</i></summary>

**Idea.** Do not compute committee info (possibly regenerating state) just to log a failed attestation.

**Impact.** Lighthouse does not compute committee info just to log a failed attestation, so the Teku-specific issue does not exist.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs): failure handlers do not compute committee info for logging

**Sources.** [teku#2849](https://github.com/Consensys-Incorporated/teku/pull/2849)

</details>


<a id="validator_client-160"></a>
<details>
<summary><b>validator_client-160</b> VC-side slot timer for attestations — <i>implemented · low · S · latency</i></summary>

**Idea.** Trigger attestation production from the VC's own slot timer rather than BN head events, so the BN need not emit head events for empty slots.

**Impact.** The VC is driven by the slot clock. Head events are only an optional early trigger, so in empty slots it still attests at the deadline.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/attestation_service.rs:196-238`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/attestation_service.rs#L196-L238) loop computes the deadline from the slot clock; head_event_or_deadline
- [`validator_client/validator_services/src/attestation_service.rs:304-330`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/attestation_service.rs#L304-L330) falls back to the deadline sleep then first_success

**Skeptic check.** Verified the loop: the deadline comes from the slot clock, and a head event can only make attestation earlier. The earlier evidence was right (paths were relative).

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#3442](https://github.com/Consensys-Incorporated/teku/pull/3442)

</details>


<a id="validator_client-161"></a>
<details>
<summary><b>validator_client-161</b> Skip stale duties when behind — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Drive duties from a slot tick and drop obsolete attestations/proposals when the node falls behind.

**Impact.** Stale attestations and proposals are dropped; each iteration targets only the current slot.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/attestation_service.rs:218-237`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/attestation_service.rs#L218-L237) re-reads the slot clock and skips if current_slot &lt;= latest_attested_slot
- [`validator_client/validator_services/src/block_service.rs:461-472`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/block_service.rs#L461-L472) do_update skips block production when notification.slot != current slot

**Skeptic check.** Verified the attestation loop, and also the block path, which the earlier check did not cite: BlockService::do_update drops expired-slot notifications with 'Skipping block production for expired slot'.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#197](https://github.com/status-im/nimbus-eth2/pull/197)

</details>


<a id="validator_client-162"></a>
<details>
<summary><b>validator_client-162</b> Resolve non-positive sleeps immediately — <i>n/a · low · cpu, latency</i></summary>

**Idea.** Resolve a sleep with zero or negative delay immediately instead of arming a timer.

**Impact.** Tokio sleep with a zero or elapsed deadline completes on the next poll; this is a JS timer quirk.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/attestation_service.rs:322`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/attestation_service.rs#L322) tokio sleep with zero duration

**Sources.** [lodestar#3908](https://github.com/ChainSafe/lodestar/pull/3908)

</details>


<a id="validator_client-163"></a>
<details>
<summary><b>validator_client-163</b> Fully async performance tracker — <i>n/a · low · cpu, latency</i></summary>

**Idea.** Remove blocking joins on futures in VC performance tracking so slot handlers are not blocked.

**Impact.** Rust async VC does not block on futures in a performance tracker; no such blocking join exists.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/attestation_service.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/attestation_service.rs):spawn_attestation_tasks uses async/await, no blocking joins

**Sources.** [teku#6920](https://github.com/Consensys-Incorporated/teku/pull/6920)

</details>


<a id="validator_client-164"></a>
<details>
<summary><b>validator_client-164</b> Multithreaded validator API serving — <i>n/a · low · latency</i></summary>

**Idea.** Serve validator API requests on a thread pool to cut attestation generation latency (reverted: hurt nodes with many validators).

**Impact.** Idea was reverted upstream, and the VC runs on the tokio multi-threaded runtime with no dedicated pool to add.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/http_api/src/lib.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/http_api/src/lib.rs): VC API is warp on tokio multi-thread runtime already

**Sources.** [teku#2572](https://github.com/Consensys-Incorporated/teku/pull/2572)

</details>


<a id="validator_client-165"></a>
<details>
<summary><b>validator_client-165</b> Short-circuit no-op validator updates — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Return early from no-op validator setting updates before taking locks or O(n) key-cache work.

**Impact.** A no-op PATCH never takes the write lock, never rewrites definitions and never touches the key cache.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/http_api/src/lib.rs:731-771`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/http_api/src/lib.rs#L731-L771) equal_or_none no-op arms return Ok(()) for all settable fields (enabled, gas_limit, builder_boost_factor, builder_proposals, prefer_builder_proposals, graffiti)
- [`validator_client/http_api/src/lib.rs:774-783`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/http_api/src/lib.rs#L774-L783) already-disabled no-op arm
- [`validator_client/http_api/src/lib.rs:785-790`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/http_api/src/lib.rs#L785-L790) RwLockUpgradableReadGuard::upgrade only on a real change, before set_validator_definition_fields

**Skeptic check.** Read the PATCH handler: both no-op arms return before the upgrade to a write lock, and the check covers every field the endpoint can set. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#5064](https://github.com/sigp/lighthouse/pull/5064)

</details>


<a id="validator_client-166"></a>
<details>
<summary><b>validator_client-166</b> Prune past-epoch duty maps — <i>implemented · low · S · memory</i></summary>

**Idea.** Drop per-epoch duty and tracking map entries for past epochs/slots so long-running VC services do not grow without bound.

**Impact.** Every epoch-keyed or slot-keyed duty map in the VC is pruned periodically, so growth is bounded.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/duties_service.rs:38-39`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L38-L39) HISTORICAL_DUTIES_EPOCHS=2
- [`validator_client/validator_services/src/duties_service.rs:1206-1213`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L1206-L1213) attesters per-pubkey epoch maps retained
- [`validator_client/validator_services/src/duties_service.rs:1918-1921`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L1918-L1921) proposers retained
- [`validator_client/validator_services/src/duties_service.rs:2173-2176`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L2173-L2176) lookahead duty maps (PTC/IL) retained
- [`validator_client/validator_services/src/sync.rs:258`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/sync.rs#L258) sync committee periods retained
- [`validator_client/validator_services/src/builder_preferences_service.rs:83-84`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/builder_preferences_service.rs#L83-L84),158-159 slot-keyed caches split_off at current slot
- [`validator_client/validator_services/src/request_auth_cache.rs:102-104`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/request_auth_cache.rs#L102-L104) prune by slot

**Skeptic check.** Grepped all HashMap&lt;Epoch\|Slot&gt;/BTreeMap&lt;Epoch\|Slot&gt; in validator_client: every one has a retain or split_off on the poll path. The earlier evidence was correct and also complete for the newer builder-preference caches.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#9591](https://github.com/ChainSafe/lodestar/pull/9591), [teku#1582](https://github.com/Consensys-Incorporated/teku/pull/1582)

</details>


<a id="validator_client-167"></a>
<details>
<summary><b>validator_client-167</b> Replace sync duties per period — <i>partial · low · S · memory</i></summary>

**Idea.** On a new sync committee duties response for a period, replace the stored duties instead of merging so removed validators drop out.

**Gap in Lighthouse.** Lighthouse never removes validators that disappear from a re-fetched period response; replace the validators map (retain only returned indices) in poll_sync_committee_duties_for_period.

**Impact.** Only matters after a deep reorg changes committee membership; stale duty would be a rare wasted/invalid sync message, no throughput gain.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/sync.rs:477-505`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/sync.rs#L477-L505) merges per-validator duties, replacing only when indices changed

**Sources.** [lodestar#3615](https://github.com/ChainSafe/lodestar/pull/3615)

</details>


<a id="validator_client-168"></a>
<details>
<summary><b>validator_client-168</b> Prepare hash-based signing keys off the signing path — <i>n/a · low · cpu, latency</i></summary>

**Idea.** For stateful hash-based (one-time-signature) keys, advance key preparation windows/subtrees ahead of time, in parallel and on a background thread, only for keys about to sign, so signing never stalls on precomputation.

**Impact.** No hash-based one-time signature keys exist in Lighthouse (BLS only).

**Best measured result.** 64 keys 1.54 s to 33 keys 142 ms (pr:ethlambda#621)

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/sync.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/sync.rs): BLS signing only, no hash-based keys

**Sources.** [ethlambda#332](https://github.com/lambdaclass/ethlambda/pull/332), [ethlambda#621](https://github.com/lambdaclass/ethlambda/pull/621), [ethlambda#622](https://github.com/lambdaclass/ethlambda/pull/622)

</details>


<a id="validator_client-169"></a>
<details>
<summary><b>validator_client-169</b> Try SSZ on all beacon nodes before JSON fallback — <i>implemented · low · S · latency</i></summary>

**Idea.** When publishing or producing blocks across multiple beacon nodes, attempt the SSZ request on every node first and only then JSON, since a node failing SSZ is usually down. This avoids spending a JSON retry on a dead primary before moving on.

**Impact.** Multi-BN setups only; already done.

**Best measured result.** None (pr:lighthouse#9475)

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/block_service.rs:707`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/block_service.rs#L707)
- [`validator_client/validator_services/src/block_service.rs:729-765`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/block_service.rs#L729-L765)
- [`validator_client/validator_services/src/block_service.rs:787-811`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/block_service.rs#L787-L811)
- [`validator_client/validator_services/src/block_service.rs:1097-1130`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/block_service.rs#L1097-L1130)

**Skeptic check.** V3 and V4 block production run a full SSZ pass over all nodes (request_proposers_last), and run the JSON pass only after that fails. Publishing (publish_signed_block_contents) and the envelope paths use SSZ only, with no JSON retry per node. The earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#8186](https://github.com/sigp/lighthouse/pull/8186), [lighthouse#9475](https://github.com/sigp/lighthouse/pull/9475)

</details>


<a id="validator_client-170"></a>
<details>
<summary><b>validator_client-170</b> One sync committee message per validator per slot — <i>implemented · low · S · cpu, bandwidth</i></summary>

**Idea.** Sign and publish a single sync committee message per validator per slot, even if it holds several committee positions or would otherwise send again on block receipt. Duplicates cost signing and gossip and are rejected by the beacon node.

**Impact.** None left.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/sync_committee_service.rs:323-340`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/sync_committee_service.rs#L323-L340)
- [`validator_client/validator_services/src/sync.rs:194-205`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/sync.rs#L194-L205)

**Skeptic check.** get_duties_for_slot pushes one SyncDuty per validator, whatever its number of committee positions. publish_sync_committee_signatures signs one SyncMessageToSign per duty, once per slot, and nothing re-sends on block arrival.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#4414](https://github.com/Consensys-Incorporated/teku/pull/4414), [lodestar#2697](https://github.com/ChainSafe/lodestar/pull/2697)

</details>


<a id="validator_client-171"></a>
<details>
<summary><b>validator_client-171</b> One sync contribution per subcommittee — <i>implemented · low · S · bandwidth, cpu</i></summary>

**Idea.** When several local validators are sync aggregators for the same subcommittee, sign and submit one contribution-and-proof per subcommittee, since the contents are identical. Saves signing, API calls and gossip traffic.

**Impact.** Prysm's duplicate (one validator selected several times in the same subcommittee) cannot happen here.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/sync_committee/sync_duty.rs:83`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/sync_committee/sync_duty.rs#L83)
- [`validator_client/validator_services/src/sync.rs:62`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/sync.rs#L62)
- [`validator_client/validator_services/src/sync.rs:209-218`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/sync.rs#L209-L218)
- [`validator_client/validator_services/src/sync_committee_service.rs:427-470`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/sync_committee_service.rs#L427-L470)

**Skeptic check.** subnet_ids returns a HashSet, and proofs are keyed by (slot, subnet), so each validator signs at most one contribution per subnet. The contribution is fetched once per subnet, as Lodestar #4135 does. Distinct aggregators must sign separately.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#15571](https://github.com/OffchainLabs/prysm/pull/15571), [lodestar#4135](https://github.com/ChainSafe/lodestar/pull/4135)

</details>


<a id="validator_client-172"></a>
<details>
<summary><b>validator_client-172</b> Publish sync contribution only if own vote included — <i>not · low · S · bandwidth, cpu</i></summary>

**Idea.** Publish a sync committee contribution only when a local validator's own vote is part of the aggregate. Redundant contribution messages are then neither signed nor sent.

**Gap in Lighthouse.** In publish_sync_committee_aggregate_for_subnet, skip signing/posting when the fetched contribution's aggregation_bits has none of the local validators' sync committee positions set.

**Impact.** Saves a few signatures and POSTs per slot for aggregators whose own vote is not in the contribution; negligible CPU, small gossip saving, and it risks dropping a useful best aggregate.

**Evidence (Lighthouse @ 928b61e719).**

- validator_services/src/sync_committee_service.rs:425-516 publishes after fetching contribution; no check that own bits are in aggregation_bits (only logs num_signers)
- validator_services/src/sync_committee_service.rs:460-470 signs for every selected aggregator

**Sources.** [grandine#168](https://github.com/grandinetech/grandine/pull/168)

</details>


<a id="validator_client-173"></a>
<details>
<summary><b>validator_client-173</b> Use validator count endpoint instead of full list — <i>n/a · low · latency, cpu, memory, bandwidth</i></summary>

**Idea.** For wait-for-activation and key reload checks, call a validator-count style beacon API instead of fetching every validator. Avoids transferring and parsing the whole validator set.

**Impact.** Lighthouse VC never downloads the whole validator set, so a count endpoint is not needed.

**Evidence (Lighthouse @ 928b61e719).**

- validator_services/src/duties_service.rs:962 resolves unknown validators one pubkey at a time with get_beacon_states_validator_id, never fetching the full validator list
- validator_services/src/duties_service.rs:940 polls rate-limited per unknown pubkey

**Sources.** [prysm#12912](https://github.com/OffchainLabs/prysm/pull/12912)

</details>


<a id="validator_client-174"></a>
<details>
<summary><b>validator_client-174</b> Beacon node readiness stream instead of sync polling — <i>n/a · low · startup, latency</i></summary>

**Idea.** Have the validator client wait on a push stream from the beacon node signalling it is synced and ready, instead of polling sync status on a timer. Startup proceeds as soon as the node is ready.

**Impact.** Prysm used a custom gRPC stream; the standard Beacon API has none. Gain would be a startup delay of seconds once per process start.

**Best measured result.** None (pr:prysm#5465)

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/beacon_node_fallback/src/lib.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/beacon_node_fallback/src/lib.rs) polls get_node_syncing on a timer
- [`common/eth2/src/lib.rs:2649`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/eth2/src/lib.rs#L2649) get_node_syncing
- beacon_node_fallback/src/beacon_head_monitor.rs:164 SSE head events exist but no readiness stream in the standard API

**Sources.** [prysm#5465](https://github.com/OffchainLabs/prysm/pull/5465), [prysm#5366](https://github.com/OffchainLabs/prysm/pull/5366)

</details>


<a id="validator_client-175"></a>
<details>
<summary><b>validator_client-175</b> Stream duties from beacon node to validator client — <i>n/a · low · latency</i></summary>

**Idea.** Push duties from the beacon node to the validator client over a stream, sending next-epoch duties eagerly, so the validator does not poll and has assignments before the epoch's first slot.

**Impact.** Standard Beacon API has no duties stream; Lighthouse already fetches next-epoch duties eagerly, so assignments exist before the epoch starts.

**Evidence (Lighthouse @ 928b61e719).**

- validator_services/src/duties_service.rs:1044-1105 polls current and next epoch attester duties each slot
- validator_services/src/duties_service.rs:675-900 per-slot polling loops

**Sources.** [prysm#5867](https://github.com/OffchainLabs/prysm/pull/5867)

</details>


<a id="validator_client-176"></a>
<details>
<summary><b>validator_client-176</b> Map entry API for single lookup — <i>implemented · low · S · cpu</i></summary>

**Idea.** When building sync committee subscriptions, use the map entry API (or_insert_with) rather than contains_key followed by insert, to do one hash lookup instead of two.

**Impact.** Micro-optimisation only; nothing measurable.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/sync.rs:213`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/sync.rs#L213)
- [`validator_client/validator_services/src/sync_committee_service.rs:663-678`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/sync_committee_service.rs#L663-L678)

**Skeptic check.** The aggregator map uses entry().or_insert_with. subscriptions_from_sync_duties is a plain map with no map lookups. I found no contains_key+insert pair on the sync subscription path.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [grandine@13702d1c9](https://github.com/grandinetech/grandine/commit/13702d1c92bd)

</details>


<a id="validator_client-177"></a>
<details>
<summary><b>validator_client-177</b> One proposer duty query per slot for all validators — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Query proposer duties once per slot for all local validators, backed by a proposer cache on the beacon node, instead of one query per validator per slot. The node no longer recomputes duties per validator.

**Impact.** None left.

**Best measured result.** None (pr:lighthouse#1831)

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/duties_service.rs:1844`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L1844)
- [`validator_client/validator_services/src/duties_service.rs:1926-1958`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/duties_service.rs#L1926-L1958)

**Skeptic check.** fetch_and_store_proposer_duties makes one proposer-duties request per epoch for all validators, and filters by local pubkeys on the client. This is the PR's own mechanism (lighthouse#1831), still present.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#1831](https://github.com/sigp/lighthouse/pull/1831)

</details>


<a id="validator_client-178"></a>
<details>
<summary><b>validator_client-178</b> Precompute RANDAO reveal before proposal slot — <i>not · low · S · latency</i></summary>

**Idea.** Compute and cache the proposer's RANDAO reveal signature about halfway through the slot before the proposal, so block production does not wait on local or remote signing at proposal time.

**Gap in Lighthouse.** Sign and cache the RANDAO reveal for proposers in the previous slot (e.g. in the block service or duties poll) and have get_validator_block_and_publish_block read the cache.

**Impact.** Removes one local BLS sign (~1ms) from the proposal critical path; for remote Web3Signer it removes a network round trip. Only matters for proposers.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/block_service.rs:625`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/block_service.rs#L625) randao_reveal signed at proposal time inside get_validator_block_and_publish_block
- [`validator_client/lighthouse_validator_store/src/lib.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/lighthouse_validator_store/src/lib.rs) randao_reveal; no cache found

**Sources.** [nimbus#5490](https://github.com/status-im/nimbus-eth2/pull/5490)

</details>


<a id="validator_client-179"></a>
<details>
<summary><b>validator_client-179</b> Run slashing-protection check once, not in two layers — <i>implemented · low · S · cpu, disk</i></summary>

**Idea.** Perform each attestation and proposal slashing-protection check once in the validator client instead of repeating it in an outer and an inner layer. Saves duplicate DB reads and comparisons per duty.

**Impact.** None left.

**Best measured result.** None (pr:prysm#7848)

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/lighthouse_validator_store/src/lib.rs:501`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/lighthouse_validator_store/src/lib.rs#L501)
- [`validator_client/lighthouse_validator_store/src/lib.rs:670`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/lighthouse_validator_store/src/lib.rs#L670)
- [`validator_client/slashing_protection/src/slashing_database.rs:623-640`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/slashing_protection/src/slashing_database.rs#L623-L640)

**Skeptic check.** The validator store calls check_and_insert_block_proposal or check_and_insert_attestations once, in one transaction. The preliminary_check_* functions have no callers in validator_client, so there is no second, outer check layer.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#7848](https://github.com/OffchainLabs/prysm/pull/7848)

</details>


<a id="validator_client-180"></a>
<details>
<summary><b>validator_client-180</b> Drop redundant zero-root check in slashing protection — <i>n/a · low · cpu</i></summary>

**Idea.** Remove the separate zero-root check when comparing signing roots in slashing protection, since the earlier exit already covers that case.

**Impact.** Lighthouse's SQL based check has no zero-root comparison to drop.

**Best measured result.** None (pr:lodestar#2869)

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/slashing_protection/src/slashing_database.rs:340`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/slashing_protection/src/slashing_database.rs#L340) check_block_proposal compares signing roots directly, no separate zero-root check

**Sources.** [lodestar#2869](https://github.com/ChainSafe/lodestar/pull/2869)

</details>


<a id="validator_client-181"></a>
<details>
<summary><b>validator_client-181</b> Retry only rejected builder preference entries — <i>partial · low · S · bandwidth</i></summary>

**Idea.** When the beacon node accepts some builder preferences and rejects others, record accepted entries and retry only the failed ones, dropping entries for expired slots. Avoids resending the whole batch.

**Gap in Lighthouse.** Parse per-entry failures from the beacon node response in the post path and only forget/resend rejected entries; fall back to JSON only on HTTP 415 (PR 9929, still open).

**Impact.** Avoids resending already accepted preferences on partial failures; gloas only, small batches, negligible CPU.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/builder_preferences_service.rs:217`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/builder_preferences_service.rs#L217) skips duties with slot &lt; current_slot
- [`validator_client/validator_services/src/builder_preferences_service.rs:246`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/builder_preferences_service.rs#L246) skips entries already published
- [`validator_client/validator_services/src/builder_preferences_service.rs:285-325`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/builder_preferences_service.rs#L285-L325) whole batch posted; on error all entries forgotten and resent next poll; SSZ failure of any kind falls back to JSON

**Sources.** [lighthouse#9929](https://github.com/sigp/lighthouse/pull/9929)

</details>


<a id="validator_client-182"></a>
<details>
<summary><b>validator_client-182</b> Run BLS signing in blocking tasks — <i>implemented · medium · S · latency, cpu</i></summary>

**Idea.** Perform validator signing on a blocking-task pool rather than the core async executor, so CPU-heavy BLS signing does not stall HTTP and DB work.

**Impact.** Done; BLS signing does not block the async executor.

**Best measured result.** None (pr:lighthouse#2522)

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/signing_method/src/lib.rs:190-203`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/signing_method/src/lib.rs#L190-L203)

**Skeptic check.** Local keystore signing runs in spawn_blocking_with_rayon_async on the HighPriority pool. In validator_client, this is the only place that calls sk.sign, so every duty type goes through it.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#2522](https://github.com/sigp/lighthouse/pull/2522)

</details>


<a id="validator_client-183"></a>
<details>
<summary><b>validator_client-183</b> One shared slashing database for all validators — <i>implemented · low · S · disk, startup</i></summary>

**Idea.** Keep slashing-protection data in a single database for all validators instead of one database per validator, so open file descriptors and startup cost do not scale with key count.

**Impact.** One shared slashing DB; file descriptors and startup cost do not scale with key count.

**Best measured result.** None (pr:lighthouse#1116)

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/slashing_protection/src/slashing_database.rs:159`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/slashing_protection/src/slashing_database.rs#L159) open_conn_pool opens one SQLite file with an r2d2 pool for all validators
- [`validator_client/lighthouse_validator_store/src/lib.rs:66`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/lighthouse_validator_store/src/lib.rs#L66) single SlashingDatabase field shared by all keys

**Skeptic check.** Verified a single SlashingDatabase (one sqlite file, pooled connections) serves every validator in the store. Earlier evidence was right; the per-dir slashing.sqlite at lib.rs:1610 is test-only.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#1116](https://github.com/sigp/lighthouse/pull/1116)

</details>


<a id="validator_client-184"></a>
<details>
<summary><b>validator_client-184</b> Single unified block production endpoint — <i>implemented · low · S · latency, bandwidth</i></summary>

**Idea.** Call the unified block production endpoint that returns a full or blinded block in one request, instead of trying a blinded proposal and falling back to a separate full-block request.

**Impact.** One produce request returns full or blinded; no blinded-then-full retry.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/block_service.rs:794`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/block_service.rs#L794) get_validator_blocks_v3_ssz unified endpoint
- [`validator_client/validator_services/src/block_service.rs:821`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/block_service.rs#L821) get_validator_blocks_v3 JSON fallback (same endpoint, encoding fallback only)
- [`validator_client/validator_services/src/block_service.rs:1124`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/block_service.rs#L1124) blinded publish only when v3 returned a blinded block

**Skeptic check.** Verified the pre-Gloas path calls v3 (SSZ then JSON), which is the unified endpoint; the only fallback is encoding, not blinded-&gt;full. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#5292](https://github.com/sigp/lighthouse/pull/5292)

</details>


<a id="validator_client-185"></a>
<details>
<summary><b>validator_client-185</b> Build single-attestation directly — <i>implemented · low · S · cpu</i></summary>

**Idea.** Construct the single-attestation form directly in the validator client instead of building a full attestation and converting it, avoiding conversion work and extra allocations.

**Impact.** Saves a conversion and aggregation-bits allocation per attestation in the VC; negligible.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_store/src/lib.rs:38`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_store/src/lib.rs#L38) AttestationToSign carries AttestationData, committee_index, attester_index
- [`validator_client/validator_services/src/attestation_service.rs:541`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/attestation_service.rs#L541) AttestationToSign built from duty and data
- [`validator_client/lighthouse_validator_store/src/lib.rs:1025`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/lighthouse_validator_store/src/lib.rs#L1025) sign_attestations yields Vec&lt;SingleAttestation&gt;
- [`validator_client/lighthouse_validator_store/src/lib.rs:1051`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/lighthouse_validator_store/src/lib.rs#L1051) SingleAttestation constructed directly from signature

**Skeptic check.** Verified no full Attestation is built for unaggregated signing; SingleAttestation is constructed directly after signing AttestationData. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#9578](https://github.com/sigp/lighthouse/pull/9578)

</details>


<a id="validator_client-186"></a>
<details>
<summary><b>validator_client-186</b> Stop deprecated registrations after replacing fork — <i>implemented · low · S · bandwidth</i></summary>

**Idea.** Stop sending deprecated validator registrations each slot once the fork that replaces them is active, since the beacon node rejects them and the client retries every slot.

**Impact.** Avoids a rejected HTTP request each slot after Gloas.

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/validator_services/src/preparation_service.rs:27`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/preparation_service.rs#L27) should_publish_validator_registrations returns false once gloas_enabled
- [`validator_client/validator_services/src/preparation_service.rs:228`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/validator_services/src/preparation_service.rs#L228) registration loop skips register_validators when gate is false

**Skeptic check.** Verified the registration loop checks the Gloas gate every slot before calling register_validators. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#9939](https://github.com/sigp/lighthouse/pull/9939)

</details>


