# state_cache (part 1 of 2)

249 ideas: 20 not, 29 partial, 119 implemented, 81 n/a; 19 actionable (high or medium value, verdict `not` or `partial`). [Back to the summary](../README.md).

Pages: [part 1](state_cache.md) · [part 2](state_cache-2.md)

| id | idea | verdict | value | effort | resources |
|---|---|---|---|---|---|
| [state_cache-001](#state_cache-001) | Reference-counted copy-on-write sharing of state fields | implemented | high | L | memory, cpu |
| [state_cache-002](#state_cache-002) | Lazy copy-on-write merkle hash caches with diff overlay | implemented | high | L | memory, cpu |
| [state_cache-003](#state_cache-003) | Share one pubkey-to-index map across state copies | partial | low | M | cpu, memory, latency |
| [state_cache-004](#state_cache-004) | Bundle state with epoch context and derived caches | implemented | low | S | cpu, latency, memory |
| [state_cache-005](#state_cache-005) | Cache validators view on cached state | n/a | low | S | cpu |
| [state_cache-006](#state_cache-006) | State cache holds shared references, clones only on mutation | implemented | low | S | cpu, memory, latency |
| [state_cache-007](#state_cache-007) | Read-only callers use state references, not copies | implemented | medium | S | cpu, memory, latency |
| [state_cache-008](#state_cache-008) | Load or copy states into reused preallocated objects | not | low | L | cpu, memory, latency |
| [state_cache-009](#state_cache-009) | Eliminate redundant second state copy on head paths | n/a | medium |  | cpu, latency, memory |
| [state_cache-010](#state_cache-010) | Send only needed head fields to network service | n/a | low | S | memory, cpu |
| [state_cache-011](#state_cache-011) | Hand-written state copy instead of reflection clone | n/a | low | S | cpu, memory |
| [state_cache-012](#state_cache-012) | Copy validator trie rather than move on recompute | n/a | low | S | cpu, latency |
| [state_cache-013](#state_cache-013) | Dedupe dirty indices before full field-trie rebuild | n/a | low | S | cpu |
| [state_cache-014](#state_cache-014) | Defragment copy-on-write state lists periodically | n/a | low | S | cpu, latency, memory |
| [state_cache-015](#state_cache-015) | Pointer-free fixed-size validator records | n/a | low | S | memory |
| [state_cache-016](#state_cache-016) | Drop duplicate flat validator caches beside state | implemented | low | S | memory, cpu |
| [state_cache-017](#state_cache-017) | Per-state validator deltas over shared finalized registry | implemented | medium | S | memory |
| [state_cache-018](#state_cache-018) | Compress effective balances and use iterator committees | partial | low | S | memory, cpu, startup, disk |
| [state_cache-019](#state_cache-019) | Avoid allocations in exit queue and head update | n/a | low | S | memory, cpu |
| [state_cache-020](#state_cache-020) | One shared append-only decompressed validator key list | implemented | low | S | memory, cpu |
| [state_cache-021](#state_cache-021) | LRU eviction for checkpoint state cache | n/a | medium |  | cpu, latency |
| [state_cache-022](#state_cache-022) | LRU eviction for committee/shuffling cache | implemented | low | S | cpu |
| [state_cache-023](#state_cache-023) | Hash maps for state cache indices | n/a | low | S | cpu, memory |
| [state_cache-024](#state_cache-024) | Key checkpoint cache by (epoch, root) without hashing | n/a | low |  | cpu |
| [state_cache-025](#state_cache-025) | Index checkpoint cache variants per root compactly | n/a | low | S | cpu, memory |
| [state_cache-026](#state_cache-026) **★** | Compute past shuffling from reference state plus RANDAO | not | medium | M | cpu, latency, disk |
| [state_cache-027](#state_cache-027) | Cache active validator indices per epoch | implemented | low | S | cpu |
| [state_cache-028](#state_cache-028) | Compute committee shuffling once per epoch and cache | implemented | medium | S | cpu, memory |
| [state_cache-029](#state_cache-029) | Cache proposer indices per epoch | implemented | low | S | cpu, latency |
| [state_cache-030](#state_cache-030) | Correct committee cache validity checks | implemented | medium | S | cpu |
| [state_cache-031](#state_cache-031) | Cache total active balance with shuffling | implemented | low | S | cpu |
| [state_cache-032](#state_cache-032) | Array-indexed pubkey cache without locks | partial | low | M | cpu, latency |
| [state_cache-033](#state_cache-033) | Node-wide decompressed pubkey cache | partial | low | S | cpu, memory, startup |
| [state_cache-034](#state_cache-034) | Fill committee cache asynchronously | not | low | L | latency, cpu |
| [state_cache-035](#state_cache-035) | Run epoch cache priming off the slot thread | implemented | medium | S | latency |
| [state_cache-036](#state_cache-036) | Shuffling cache holds in-flight promises | implemented | medium | S | cpu, latency, disk |
| [state_cache-037](#state_cache-037) **★** | Single-flight state regeneration and loads | partial | medium | M | cpu, memory, latency |
| [state_cache-038](#state_cache-038) | Compact per-checkpoint attestation verification cache | implemented | low | S | memory, cpu |
| [state_cache-039](#state_cache-039) | Avoid pinning old head states in attestation workers | implemented | low | S | memory |
| [state_cache-040](#state_cache-040) | Select verification state by shuffling dependent root | implemented | medium | S | cpu, memory, latency |
| [state_cache-041](#state_cache-041) | Epoch-indexed checkpoint cache bounded by epoch count | n/a | medium |  | memory, latency |
| [state_cache-042](#state_cache-042) | Spill older checkpoint states to disk, reload on miss | implemented | high | S | memory, disk, cpu |
| [state_cache-043](#state_cache-043) **★** | Cap number of persisted checkpoint states on disk | partial | medium | M | disk |
| [state_cache-044](#state_cache-044) | Bounded hot states with replay regeneration | implemented | medium | S | memory, cpu |
| [state_cache-045](#state_cache-045) | Bounded smaller in-memory hot block cache | implemented | low | S | memory |
| [state_cache-046](#state_cache-046) | Bound state cache by measured bytes | not | low | M | memory |
| [state_cache-047](#state_cache-047) | Configurable smaller snapshot cache size | implemented | low | S | memory |
| [state_cache-048](#state_cache-048) | Size state caches to cover forks and late blocks | implemented | medium | S | cpu, latency |
| [state_cache-049](#state_cache-049) | Size state cache from real preset | n/a | low | S | cpu |
| [state_cache-050](#state_cache-050) | Replay-window-sized cache during historical regeneration | implemented | low | S | startup, cpu |
| [state_cache-051](#state_cache-051) | Committees API uses configurable shuffling cache | implemented | low | S | cpu, latency |
| [state_cache-052](#state_cache-052) | Limit validator-triggered head advance during sync | n/a | medium |  | memory |
| [state_cache-053](#state_cache-053) | Disable full-state checkpoint cache by default | n/a | low | S | memory |
| [state_cache-054](#state_cache-054) | Remove skip-slot state cache | n/a | low | S | memory |
| [state_cache-055](#state_cache-055) | Pooled buffer for state serialization | not | low | M | cpu, memory |
| [state_cache-056](#state_cache-056) | Serve head state from cache, bypass regen queue | implemented | low | S | latency, cpu |
| [state_cache-057](#state_cache-057) | Attestation pre-state from checkpoint cache first | implemented | medium | S | cpu, latency, disk |
| [state_cache-058](#state_cache-058) **★** | Cache slot-advanced states keyed by (root, slot) | partial | medium | M | cpu, latency, memory |
| [state_cache-059](#state_cache-059) | Cache intermediate empty-slot states | not | low | S | cpu, latency |
| [state_cache-060](#state_cache-060) | Cheap skip-slot cache key without state hashing | implemented | low | S | cpu, memory |
| [state_cache-061](#state_cache-061) | Use skip-slot cache only when ahead of input | n/a | low | S | cpu |
| [state_cache-062](#state_cache-062) | Write cache only if entry is newer | implemented | low | S | cpu, memory |
| [state_cache-063](#state_cache-063) | Correct next-slot cache key after payload | partial | low | S | cpu, latency |
| [state_cache-064](#state_cache-064) | Gate state advance behind its feature flag | n/a | low | S | cpu |
| [state_cache-065](#state_cache-065) | Cache every epoch-boundary state produced during import | implemented | medium | S | cpu, disk, sync, memory |
| [state_cache-066](#state_cache-066) | Bounded boundary-only cache during initial sync | partial | low | S | memory, sync |
| [state_cache-067](#state_cache-067) | Slot to epoch-boundary-root index | implemented | low | S | latency, cpu |
| [state_cache-068](#state_cache-068) | Read balances from checkpoint balances cache | not | low | S | latency, disk |
| [state_cache-069](#state_cache-069) **★** | Batch-load replay blocks concurrently | not | medium | S | latency, disk |
| [state_cache-070](#state_cache-070) | Read state cache file in one buffered read | n/a | low | S | disk, latency |
| [state_cache-071](#state_cache-071) | Batch summary writes and cheaper replay base in sync | n/a | medium |  | sync, disk |
| [state_cache-072](#state_cache-072) | In-memory cache of recent blocks and states | implemented | low | S | disk, latency |
| [state_cache-073](#state_cache-073) | Boot from persisted unfinalized checkpoint state | implemented | medium | S | sync, startup |
| [state_cache-074](#state_cache-074) | Keep genesis state in hot cache | not | low | S | disk, latency |
| [state_cache-075](#state_cache-075) | Keep head state resident in memory | implemented | low | S | cpu, latency, disk |
| [state_cache-076](#state_cache-076) | Insert DB-loaded states into state cache | implemented | low | S | disk, latency |
| [state_cache-077](#state_cache-077) | State cache owns slot processing with store option | n/a | low | L | cpu, memory |
| [state_cache-078](#state_cache-078) | Avoid duplicate states across caches | n/a | low | S | memory, disk |
| [state_cache-079](#state_cache-079) **★** | Regenerate from nearest cached ancestor state | partial | medium | S | disk, cpu, latency |
| [state_cache-080](#state_cache-080) **★** | Cancel state replay on request cancellation | not | medium | M | cpu, latency |
| [state_cache-081](#state_cache-081) | Read anchor state fields from bytes before decode | not | low | S | startup, memory, cpu |
| [state_cache-082](#state_cache-082) | Fall back to cached checkpoint state for parent | implemented | medium | S | latency, cpu |
| [state_cache-083](#state_cache-083) | Store checkpoints in fork choice nodes | implemented | low | S | latency, memory, cpu |
| [state_cache-084](#state_cache-084) | Clear parent derived caches on transfer to child | n/a | low | S | memory |
| [state_cache-085](#state_cache-085) | Keep late-block pre-state in snapshot cache | implemented | medium | S | latency, cpu |
| [state_cache-086](#state_cache-086) | Dedicated temporary state for duty catch-up | n/a | low | S | latency, memory |
| [state_cache-087](#state_cache-087) | Skip re-persisting unchanged head state | implemented | low | S | disk, cpu, latency |
| [state_cache-088](#state_cache-088) | Defer state cache pruning off slot start | n/a | low | S | latency, cpu |
| [state_cache-089](#state_cache-089) | Denser state snapshots for reorg replay | not | low | S | latency, disk |
| [state_cache-090](#state_cache-090) | Derive cached state block root from state itself | implemented | low | S | memory, cpu, latency, disk |
| [state_cache-091](#state_cache-091) | Diff-layered state storage with snapshots and LRU | implemented | medium | L | disk, memory, latency |
| [state_cache-092](#state_cache-092) | Do not retain epoch processing results per state | implemented | low | S | memory |
| [state_cache-093](#state_cache-093) | Bound epoch/shuffling refs to recent blocks | implemented | low | S | memory |
| [state_cache-094](#state_cache-094) | Early return when replay is unnecessary | implemented | low | S | cpu, latency |
| [state_cache-095](#state_cache-095) | Stop reverse state-root iteration past target slot | implemented | low | S | cpu, disk |
| [state_cache-096](#state_cache-096) | Release refcount lock without defer | n/a | low |  | cpu |
| [state_cache-097](#state_cache-097) | Never scan or clone all cached states | implemented | low | S | cpu, latency, memory |
| [state_cache-098](#state_cache-098) | Cache post-execution-payload state | n/a | low |  | latency, memory |
| [state_cache-099](#state_cache-099) | Dedicated small cache of epoch-boundary states | implemented | medium | M | memory, disk, latency, cpu |
| [state_cache-100](#state_cache-100) | Shared per-epoch context object attached to blocks | implemented | medium | M | cpu, memory, latency |
| [state_cache-101](#state_cache-101) | Prune state cache often during sync and replay | implemented | medium | S | memory, startup |
| [state_cache-102](#state_cache-102) | Keep secondary epoch index in sync on eviction | implemented | low | S | memory |
| [state_cache-103](#state_cache-103) | Drop finalized and older states on finalization | implemented | medium | S | memory |
| [state_cache-104](#state_cache-104) **★** | Keep one epoch of states for far non-canonical forks | partial | medium | S | memory |
| [state_cache-105](#state_cache-105) | Prune state cache relative to head slot | implemented | low | S | memory |
| [state_cache-106](#state_cache-106) | Cache finalized states keyed by slot for API | implemented | medium | S | cpu, latency, disk |
| [state_cache-107](#state_cache-107) **★** | Preload finalized epoch states into API cache | not | medium | S | latency |
| [state_cache-108](#state_cache-108) | Pubkey-to-index hashmap cache | implemented | low | S | cpu, latency |
| [state_cache-109](#state_cache-109) | Pubkey index cache only for finalized validators | n/a | low | S | cpu |
| [state_cache-110](#state_cache-110) | Persist decompressed pubkey cache across restarts | implemented | low | S | startup |
| [state_cache-111](#state_cache-111) | Warm pubkey cache at genesis start | implemented | low | S | startup |
| [state_cache-112](#state_cache-112) | Preallocate pubkey cache capacity | partial | low | S | startup, memory |
| [state_cache-113](#state_cache-113) | Serve pubkeys from in-memory head state | implemented | low | S | disk, cpu, memory |
| [state_cache-114](#state_cache-114) | Reader-writer locks for state reads | n/a | low | S | cpu, latency |
| [state_cache-115](#state_cache-115) | Read lock on shuffling cache hits | implemented | medium | S | cpu, latency |
| [state_cache-116](#state_cache-116) | Never evict possibly-finalizable epoch-boundary states | implemented | medium | S | memory, cpu, disk |
| [state_cache-117](#state_cache-117) **★** | Fork-aware state cache eviction by chain | not | medium | L | memory |
| [state_cache-118](#state_cache-118) **★** | Preserve fork-choice tip states when pruning | not | medium | S | cpu, memory |
| [state_cache-119](#state_cache-119) **★** | Head state never evicted; cap regen replay | partial | medium | S | cpu, memory |
| [state_cache-120](#state_cache-120) | Finalized state root fast path | implemented | low | S | latency, disk |
| [state_cache-121](#state_cache-121) | Genesis state shortcut for zero root | implemented | low | S | latency |
| [state_cache-122](#state_cache-122) | Evict shuffling cache by smallest epoch | implemented | low | S | latency |
| [state_cache-123](#state_cache-123) | Load shuffling cache for correct epochs | implemented | low | S | cpu |
| [state_cache-124](#state_cache-124) | Global shuffling cache keyed by epoch and decision root | implemented | medium | S | cpu, disk, latency, memory |
| [state_cache-125](#state_cache-125) | Precompute next-epoch caches in the state-advance task | implemented | medium | S | cpu, latency |
| [state_cache-126](#state_cache-126) | Preheat n+1 shuffling at end of n-1 | implemented | medium | S | latency, cpu |
| [state_cache-127](#state_cache-127) | Seed sync committee cache from known committee | implemented | low | S | cpu, sync |
| [state_cache-128](#state_cache-128) | Free per-state auxiliary maps on drop | n/a | low | S | memory |
| [state_cache-129](#state_cache-129) | Move field tries into the copy, not clone | n/a | low | S | memory, cpu |
| [state_cache-130](#state_cache-130) | Move snapshots out of cache instead of cloning | n/a | medium |  | cpu, memory, sync |
| [state_cache-131](#state_cache-131) | Multi-value lists: shared base plus per-state diffs | implemented | low | L | memory, cpu |
| [state_cache-132](#state_cache-132) | Persistent structurally shared tree-backed beacon states | implemented | low | S | memory, cpu |
| [state_cache-133](#state_cache-133) **★** | Rebase updated lists onto old tree | not | medium | M | memory |
| [state_cache-134](#state_cache-134) | Load states onto an existing in-memory tree | partial | low | M | memory, cpu, startup |
| [state_cache-135](#state_cache-135) | Native struct state instead of protobuf wrapper | n/a | low | S | memory, cpu |
| [state_cache-136](#state_cache-136) | Pool and reuse large state field buffers | n/a | low |  | memory, cpu |
| [state_cache-137](#state_cache-137) | Pool tree-hash leaves and compression writers | n/a | low | S | memory, cpu |
| [state_cache-138](#state_cache-138) | No state copies on head save and init sync | n/a | medium |  | memory, sync |
| [state_cache-139](#state_cache-139) | Read-only field accessors without state copy | implemented | low | S | memory, cpu |
| [state_cache-140](#state_cache-140) | Read-only epoch context handout | implemented | low | S | cpu, memory |
| [state_cache-141](#state_cache-141) | In-place forked state assignment | n/a | low | S | cpu, memory |
| [state_cache-142](#state_cache-142) | Grow reused buffers without full zeroing | n/a | low | S | cpu, memory |
| [state_cache-143](#state_cache-143) | Validator set as one flat buffer | n/a | low |  | memory, cpu |
| [state_cache-144](#state_cache-144) | Compact flattened checkpoint state | n/a | medium |  | memory, cpu |
| [state_cache-145](#state_cache-145) | Primitive int arrays for cached committees | n/a | low |  | memory, cpu |
| [state_cache-146](#state_cache-146) | Preallocate epoch cache hashmaps | n/a | low |  | memory, cpu |
| [state_cache-147](#state_cache-147) | Reserve spare capacity on state list growth | n/a | low |  | memory, cpu |
| [state_cache-148](#state_cache-148) | Keep validator cache capacity on transfer | n/a | low |  | cpu, memory |
| [state_cache-149](#state_cache-149) | In-memory LRU of recent hot states | implemented | medium | S | memory, latency, disk, cpu |
| [state_cache-150](#state_cache-150) | Tune hot state cache size | implemented | low | S | cpu, latency, memory, startup |
| [state_cache-151](#state_cache-151) | Store sparse states, regenerate by replay | implemented | low | S | memory, disk, cpu, latency |
| [state_cache-152](#state_cache-152) | Do not pin disk-loaded states in cache | implemented | low | S | memory, disk |
| [state_cache-153](#state_cache-153) | Periodic hot state snapshots in long non-finality | implemented | medium | S | memory, disk |
| [state_cache-154](#state_cache-154) | Prune before persisting checkpoint states | n/a | low |  | disk, memory |
| [state_cache-155](#state_cache-155) | Prune on-disk states one epoch behind finality | implemented | low | S | disk |
| [state_cache-156](#state_cache-156) | Cache of historical cold states | implemented | low | S | latency, cpu, disk |
| [state_cache-157](#state_cache-157) **★** | Historical state regen on dedicated worker | partial | medium | M | cpu, latency |
| [state_cache-158](#state_cache-158) | Opt-in historical state regeneration | implemented | low | S | cpu, latency |
| [state_cache-159](#state_cache-159) | State cache during initial sync | implemented | medium | S | sync |
| [state_cache-160](#state_cache-160) | Free sync caches after range sync | n/a | low |  | memory |
| [state_cache-161](#state_cache-161) | Fewer state dumps during forward sync | implemented | low | S | memory, cpu |
| [state_cache-162](#state_cache-162) **★** | Pre-advance head state and serve consumers from it | partial | high | S | latency, cpu, memory |
| [state_cache-163](#state_cache-163) | Precompute state one epoch ahead at epoch end | implemented | low | S | latency, cpu |
| [state_cache-164](#state_cache-164) | Prefer in-memory regen base within tolerance | partial | low | M | memory, disk |
| [state_cache-165](#state_cache-165) | Choose regen base without loading block | n/a | low | S | disk, latency |
| [state_cache-166](#state_cache-166) | Late binding of regen base state | n/a | low | S | memory |
| [state_cache-167](#state_cache-167) | State existence check without reading state | not | low | S | latency, disk |
| [state_cache-168](#state_cache-168) | Evict hot block bodies, reload on demand | implemented | low | S | memory |
| [state_cache-169](#state_cache-169) | Advance clone before storing checkpoint state | n/a | medium | S | cpu, memory |
| [state_cache-170](#state_cache-170) | Past-epoch block root lookup in checkpoint processing | n/a | high |  | memory |
| [state_cache-171](#state_cache-171) **★** | Global active validator cache across state copies | partial | medium | S | cpu, memory |
| [state_cache-172](#state_cache-172) | Keep previous head state for reorgs | implemented | low | S | disk, memory, latency |
| [state_cache-173](#state_cache-173) | Dedicated justified state cache for fork choice | implemented | low | S | cpu, latency |
| [state_cache-174](#state_cache-174) | Lazy validators/balances load for API states | n/a | low | S | memory |
| [state_cache-175](#state_cache-175) | Tree-hash leaves from iterator, bounded fork ring | n/a | low | S | memory |
| [state_cache-176](#state_cache-176) | Limit speculative proposer-prediction replays | n/a | low |  | latency, cpu, disk |
| [state_cache-177](#state_cache-177) | Resolve block roots from state block_roots | implemented | low | S | sync, startup |
| [state_cache-178](#state_cache-178) | Non-blocking try-lock in cache pruning | n/a | low | S | latency, cpu |
| [state_cache-179](#state_cache-179) | Run state cache pruning off the store lock | implemented | medium | S | latency |
| [state_cache-180](#state_cache-180) | Pass state cache through rewind steps | implemented | low | S | cpu |
| [state_cache-181](#state_cache-181) | Transfer hash caches only to imported clone | n/a | medium |  | cpu |
| [state_cache-182](#state_cache-182) | Prune grandparent snapshot after insert | partial | low | S | memory |
| [state_cache-183](#state_cache-183) | Epoch-matching state cache for attestations | implemented | medium | S | sync, cpu |
| [state_cache-184](#state_cache-184) | Rebase clearance state on head during chain stall | implemented | low | S | latency |
| [state_cache-185](#state_cache-185) | Refresh next-slot cache when execution payload arrives late | implemented | low | S | latency |
| [state_cache-186](#state_cache-186) | Bound the number of full states held in memory | implemented | high | S | memory |
| [state_cache-187](#state_cache-187) **★** | Do expensive state work outside the cache lock | partial | medium | M | latency, cpu |
| [state_cache-188](#state_cache-188) | Check in-memory caches before DB state loads | implemented | medium | S | latency, disk, cpu |
| [state_cache-189](#state_cache-189) | Advance epoch caches once per epoch transition | implemented | low | S | cpu |
| [state_cache-190](#state_cache-190) | Drop fork-aware finalized pubkey cache | n/a | low |  | memory, cpu |
| [state_cache-191](#state_cache-191) | Remove redundant lock around thread-safe cache | n/a | low |  | latency, cpu |
| [state_cache-192](#state_cache-192) | Remove per-state caches that pin old states | n/a | low |  | memory |
| [state_cache-193](#state_cache-193) | Consult checkpoint cache only for viable non-canonical targets | n/a | low |  | cpu |
| [state_cache-194](#state_cache-194) | Keep persisted-file key when re-adding reloaded states | n/a | low |  | disk |
| [state_cache-195](#state_cache-195) | Rebuild pruned pre-state for delayed sidecar blocks | n/a | medium |  | sync |
| [state_cache-196](#state_cache-196) | Reuse the block post-state as new head state | implemented | medium | S | cpu, latency |
| [state_cache-197](#state_cache-197) | Use head state for prior-epoch data column validation | partial | low | S | cpu, latency |
| [state_cache-198](#state_cache-198) **★** | Archive persisted checkpoint bytes without re-serializing | not | medium | S | cpu, disk |
| [state_cache-199](#state_cache-199) | Cache block post-states for block production | partial | low | M | cpu, latency |
| [state_cache-200](#state_cache-200) | Reuse prebuilt pubkey cache from anchor state | implemented | low | S | startup, cpu |
| [state_cache-201](#state_cache-201) | Reuse pubkey map allocation when reinitializing caches | n/a | low |  | memory, cpu |
| [state_cache-202](#state_cache-202) | Load startup state once and share across services | implemented | low | S | startup, memory |
| [state_cache-203](#state_cache-203) | Keep future-epoch info and per-block state cache | n/a | low | S | cpu |
| [state_cache-204](#state_cache-204) | Persist skipped-slot states using state_roots | implemented | low | S | cpu |
| [state_cache-205](#state_cache-205) | Store shuffling once, derive committees and duties | implemented | low | S | memory, cpu |
| [state_cache-206](#state_cache-206) | Do not preallocate state cache tables | n/a | low | S | memory |
| [state_cache-207](#state_cache-207) | Store next-slot cache hit into checkpoint cache | partial | low | S | cpu |
| [state_cache-208](#state_cache-208) | Drop pubkey map and scan the registry | n/a | low | S | memory |
| [state_cache-209](#state_cache-209) | Segmented page pool for lock-free state readers | n/a | low | S | memory, latency |
| [state_cache-210](#state_cache-210) | Dedicated clearance state for block sync | n/a | medium | S | sync, cpu |
| [state_cache-211](#state_cache-211) | Process block attestations in target order | n/a | medium | S | cpu |
| [state_cache-212](#state_cache-212) | Serve finalized-state lookups from the in-memory copy | implemented | low | S | cpu, disk |
| [state_cache-213](#state_cache-213) | Cheap presence check on shuffling cache | implemented | low | S | cpu |
| [state_cache-214](#state_cache-214) | Predict next-epoch duties without state advance | implemented | low | S | cpu |
| [state_cache-215](#state_cache-215) | Single shared head state buffer for services | n/a | low |  | memory |
| [state_cache-216](#state_cache-216) | Replay only blocks after base state on regen | partial | low | S | disk, cpu |
| [state_cache-217](#state_cache-217) | State cache eviction policy and insertion rules | implemented | low | S | memory, cpu |
| [state_cache-218](#state_cache-218) | Store few checkpoint states while syncing | partial | low | M | disk, sync |
| [state_cache-219](#state_cache-219) | Delay next-epoch duty lookahead into the epoch | n/a | low |  | cpu |
| [state_cache-220](#state_cache-220) | Skip parent regen at genesis on startup | n/a | low |  | startup |
| [state_cache-221](#state_cache-221) | Cache decompressed pubkeys only for active validators | not | low | M | memory |
| [state_cache-222](#state_cache-222) | Exact state cache hit skips epoch transition | implemented | low | S | cpu, disk |
| [state_cache-223](#state_cache-223) | Skip state-root check when replaying stored blocks | implemented | low | S | cpu |
| [state_cache-224](#state_cache-224) | Skip block validation when replaying local blocks | implemented | low | S | cpu |
| [state_cache-225](#state_cache-225) | In-memory cache of diff base/snapshot states | implemented | low | S | disk, cpu, latency |
| [state_cache-226](#state_cache-226) | Reclaimable soft/weak references for cached states | n/a | low | L | memory |
| [state_cache-227](#state_cache-227) | Sparse checkpoint replay at attestation pool init | n/a | low | L | startup, cpu |
| [state_cache-228](#state_cache-228) | Replay from last block at or before slot | implemented | low | S | cpu, disk |
| [state_cache-229](#state_cache-229) | Shared state cache keyed by state root | implemented | low | S | cpu, disk |
| [state_cache-230](#state_cache-230) | Central state regenerator serving all pre-states | partial | low | M | cpu |
| [state_cache-231](#state_cache-231) | Store states as deltas over a base | implemented | medium | S | disk, memory |
| [state_cache-232](#state_cache-232) | Compact backing-tree layout for balances and validators | n/a | low | L | memory |
| [state_cache-233](#state_cache-233) | Committee caches embedded in the state | implemented | low | S | memory, cpu |
| [state_cache-234](#state_cache-234) **★** | Struct-of-arrays validators with shared pubkey list | partial | medium | M | memory, cpu |
| [state_cache-235](state_cache-2.md#state_cache-235) | Copy head state outside lock, swap pointer | implemented | low | S | latency |
| [state_cache-236](state_cache-2.md#state_cache-236) | Faster persistent collection library | n/a | low | L | cpu, memory |
| [state_cache-237](state_cache-2.md#state_cache-237) | Synchronous in-memory state cache access | n/a | low | S | latency, cpu |
| [state_cache-238](state_cache-2.md#state_cache-238) | Fill only proposer indices on proposer cache miss | implemented | low | S | cpu |
| [state_cache-239](state_cache-2.md#state_cache-239) | Tiered retention for persisted checkpoint states | partial | low | M | disk |
| [state_cache-240](state_cache-2.md#state_cache-240) | One-entry state cache during range sync | not | low | S | memory, sync |
| [state_cache-241](state_cache-2.md#state_cache-241) | Justified balances from epoch-boundary cache | implemented | low | S | cpu |
| [state_cache-242](state_cache-2.md#state_cache-242) | Proposer caches from stored proposer lookahead | implemented | low | S | cpu, startup |
| [state_cache-243](state_cache-2.md#state_cache-243) | Vec-indexed committee cache without clones | implemented | medium | S | cpu, memory |
| [state_cache-244](state_cache-2.md#state_cache-244) | Whole-list swap-or-not shuffle | implemented | high | S | cpu |
| [state_cache-245](state_cache-2.md#state_cache-245) | Persist block-and-slot to state-root index for rewinds | partial | low | M | cpu, disk |
| [state_cache-246](state_cache-2.md#state_cache-246) | Bound state replay horizon for non-finalized-only queries | implemented | low | S | cpu, latency, disk |
| [state_cache-247](state_cache-2.md#state_cache-247) | Cache native state field reads in a wrapper | n/a | low |  | cpu |
| [state_cache-248](state_cache-2.md#state_cache-248) | Reuse cached weak-subjectivity state in light client proofs | n/a | low |  | cpu |
| [state_cache-249](state_cache-2.md#state_cache-249) | Ring buffer of in-place state deltas for unfinalized forks | n/a | low |  | latency, cpu, memory |

★ actionable. Click an id for the full record.

## Ideas

<a id="state_cache-001"></a>
<details>
<summary><b>state_cache-001</b> Reference-counted copy-on-write sharing of state fields — <i>implemented · high · L · memory, cpu</i></summary>

**Idea.** Make BeaconState clones share large fields (validators, balances, roots, participation, randao, individual validator records) by reference count and copy a field only when a shared one is mutated, releasing references correctly when a state is dropped. Check whether state copies in the state cache and block processing are O(changed) rather than O(state size).

**Impact.** State clone is O(1)-ish and mutation copies only changed paths; even non-spec caches are persistent structures or Arc.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:76`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L76) (Validators is a milhouse List)
- [`consensus/types/src/state/beacon_state.rs:825`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L825) (committee_caches: [Arc&lt;CommitteeCache&gt;; _])
- [`consensus/types/src/state/pubkey_cache.rs:8-14`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/pubkey_cache.rs#L8-L14) (rpds HashTrieMap)
- [`consensus/types/src/state/slashings_cache.rs:10-14`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/slashings_cache.rs#L10-L14) (HashTrieSet)
- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/tree.rs (Arc nodes, path copy on write)

**Skeptic check.** Verified all large spec fields are milhouse trees and the caches use Arc or rpds persistent maps, so clones in the state cache and block processing share structure.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#4785](https://github.com/OffchainLabs/prysm/pull/4785), [prysm#6341](https://github.com/OffchainLabs/prysm/pull/6341), [prysm#5245](https://github.com/OffchainLabs/prysm/pull/5245), [lodestar@8a0621fb2](https://github.com/ChainSafe/lodestar/commit/8a0621fb23ac), [prysm#10483](https://github.com/OffchainLabs/prysm/pull/10483), [prysm#4751](https://github.com/OffchainLabs/prysm/pull/4751), [prysm#6322](https://github.com/OffchainLabs/prysm/pull/6322), [prysm#7840](https://github.com/OffchainLabs/prysm/pull/7840), [prysm#4789](https://github.com/OffchainLabs/prysm/pull/4789), [prysm#6012](https://github.com/OffchainLabs/prysm/pull/6012), [prysm#6015](https://github.com/OffchainLabs/prysm/pull/6015), [prysm#4825](https://github.com/OffchainLabs/prysm/pull/4825), [prysm#4828](https://github.com/OffchainLabs/prysm/pull/4828), [prysm#14252](https://github.com/OffchainLabs/prysm/pull/14252), [prysm#8397](https://github.com/OffchainLabs/prysm/pull/8397), [prysm#11864](https://github.com/OffchainLabs/prysm/pull/11864)

</details>


<a id="state_cache-002"></a>
<details>
<summary><b>state_cache-002</b> Lazy copy-on-write merkle hash caches with diff overlay — <i>implemented · high · L · memory, cpu</i></summary>

**Idea.** Share per-field merkle trie (tree-hash cache) layers between state copies with refcounted copy-on-write, deferring any deep copy until the first mutation and storing a modified copy as a diff over the base trie until the diff grows. This avoids duplicating hash caches per cached state.

**Impact.** Hash caches live inside the shared Arc nodes, so cached states share them and only modified paths are rehashed; there is no per-state hash cache to duplicate.

**Best measured result.** On Hoodi supernode saves ~200-350MB heap (~6.5-9.5%) (pr:prysm#16512)

**Evidence (Lighthouse @ 928b61e719).**

- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/leaf.rs:12 (hash: RwLock&lt;Hash256&gt; stored in node)
- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/packed_leaf.rs:13,30 (cached hash per packed leaf)
- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/tree.rs:507,542 (cached internal-node hash; rayon::join over uncached subtrees)

**Skeptic check.** The Prysm diff-overlay is a workaround for separate per-field tries; LH achieves the same memory sharing structurally via milhouse node-embedded hashes.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#16512](https://github.com/OffchainLabs/prysm/pull/16512), [prysm#16513](https://github.com/OffchainLabs/prysm/pull/16513)

</details>


<a id="state_cache-003"></a>
<details>
<summary><b>state_cache-003</b> Share one pubkey-to-index map across state copies — <i>partial · low · M · cpu, memory, latency</i></summary>

**Idea.** Keep the validator pubkey-to-index map shared by reference across state copies, as an append-only map or an immutable base plus a small per-state delta, extended incrementally rather than rebuilt or copied when a state is copied or loaded.

**Gap in Lighthouse.** The hot path is complete: an rpds persistent map, extended incrementally, rebased on the finalized state by StateCache::rebase_on_finalized. Cold states are not covered. A state built from an HDiffBuffer (HistoricStateCache::get_state, HDiffBuffer::as_state) starts with an empty PubkeyCache, and nothing rebases it. Then load_cold_state_by_slot_using_replay -&gt; replay_blocks -&gt; process_operations (Electra update_pubkey_cache), and single_pass epoch processing, rebuild the whole 1M+ entry map from index 0 for each new snapshot or diff base. The API endpoints validator_inclusion and sync_committee_rewards do the same on states they load.

**Impact.** Archive and historic-state API queries and cold replays pay a full pubkey-map rebuild, an estimated hundreds of ms for 1M+ validators, per fresh cold base state. Block import, gossip and hot loads are not affected.

**Best measured result.** copy into reused spare, 1.14M validators: Fulu ~81 -&gt; 11.7 ms, Gloas ~80 -&gt; 11.1 ms (pr:caplin#25151)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/pubkey_cache.rs:8`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/pubkey_cache.rs#L8)
- [`consensus/types/src/state/beacon_state.rs:2979`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2979)
- [`consensus/types/src/state/beacon_state.rs:3515`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L3515)
- [`beacon_node/store/src/hot_cold_store.rs:1988`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1988)
- [`beacon_node/store/src/historic_state_cache.rs:63`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/historic_state_cache.rs#L63)
- [`beacon_node/store/src/hot_cold_store.rs:2358`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2358)
- [`consensus/state_processing/src/per_block_processing/process_operations.rs:76`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/process_operations.rs#L76)
- [`beacon_node/http_api/src/validator_inclusion.rs:71`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validator_inclusion.rs#L71)

**Skeptic check.** The persistent shared map and incremental extension are real on hot states, so the earlier evidence is right for the hot path. It missed that cold or diff-loaded states never inherit a base cache. A fix would need a prefix-bounded share, because the finalized cache is longer than the historic validator count and rebase_caches_on rejects it.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [caplin#25151](https://github.com/erigontech/erigon/pull/25151), [prysm#4713](https://github.com/OffchainLabs/prysm/pull/4713), [prysm#6910](https://github.com/OffchainLabs/prysm/pull/6910), [lodestar#1028](https://github.com/ChainSafe/lodestar/pull/1028), [prysm#8860](https://github.com/OffchainLabs/prysm/pull/8860), [prysm#13943](https://github.com/OffchainLabs/prysm/pull/13943), [grandine@f603cf04a](https://github.com/grandinetech/grandine/commit/f603cf04a6db), [prysm#17286](https://github.com/OffchainLabs/prysm/pull/17286), [caplin#18527](https://github.com/erigontech/erigon/pull/18527)

</details>


<a id="state_cache-004"></a>
<details>
<summary><b>state_cache-004</b> Bundle state with epoch context and derived caches — <i>implemented · low · S · cpu, latency, memory</i></summary>

**Idea.** Store the epoch context and derived caches (shufflings, proposers, pubkey caches) together with the state tree in one object used by the state transition, whose clone is cheap, so block import, API and gossip reuse them instead of recomputing them from the state.

**Impact.** BeaconState carries its derived caches: committee caches (Arc), pubkey (rpds), slashings (rpds), exit, progressive balances, total active balance and epoch cache (Arc). Cloning the state clones them cheaply. The chain-level proposer and shuffling caches add sharing across states by decision root.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:825`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L825)
- [`consensus/types/src/state/beacon_state.rs:831`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L831)
- [`consensus/types/src/state/beacon_state.rs:837`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L837)
- [`consensus/types/src/state/beacon_state.rs:849`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L849)
- [`consensus/types/src/state/epoch_cache.rs:22`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/epoch_cache.rs#L22)
- [`consensus/types/src/state/slashings_cache.rs:10`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/slashings_cache.rs#L10)

**Skeptic check.** Checked the cache fields and their clone cost. They travel with the state object that the state transition, import and API use. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar@cdb79c222](https://github.com/ChainSafe/lodestar/commit/cdb79c222142), [lodestar#1997](https://github.com/ChainSafe/lodestar/pull/1997), [lodestar#2172](https://github.com/ChainSafe/lodestar/pull/2172)

</details>


<a id="state_cache-005"></a>
<details>
<summary><b>state_cache-005</b> Cache validators view on cached state — <i>n/a · low · S · cpu</i></summary>

**Idea.** Keep the validators list wrapper/view built once on the cached state rather than rebuilding it on each access.

**Impact.** None for a mainnet node: Validators are a milhouse List inside the state; the tree and its cached hashes are part of the state itself, so there is no wrapper to rebuild.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/validator/validator.rs:21`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/validator/validator.rs#L21) Validator is a plain struct stored in milhouse List
- Validators are a milhouse List inside the state; the tree and its cached hashes are part of the state itself, so there is no wrapper to rebuild.

**Sources.** [lodestar#2330](https://github.com/ChainSafe/lodestar/pull/2330)

</details>


<a id="state_cache-006"></a>
<details>
<summary><b>state_cache-006</b> State cache holds shared references, clones only on mutation — <i>implemented · low · S · cpu, memory, latency</i></summary>

**Idea.** Hold cached states as reference-counted pointers and have state and checkpoint caches hand out a shared reference, cloning only when the caller will run a state transition. Inserting and reading entries then does not duplicate full states.

**Impact.** Cached states are milhouse persistent trees, and their caches are Arc or rpds. get_by_state_root and put_state clones only copy roots and pointers, and the data is copied on write when a state transition mutates it.

**Best measured result.** removes one extra state copy that was getting really expensive (pr:prysm#5584)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/state_cache.rs:215`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L215)
- [`beacon_node/store/src/state_cache.rs:275`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L275)
- [`consensus/types/src/state/beacon_state.rs:825`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L825)

**Skeptic check.** The clone in the state cache shares structure, in effect a shared reference with copy-on-mutation. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#5584](https://github.com/OffchainLabs/prysm/pull/5584), [lighthouse#775](https://github.com/sigp/lighthouse/pull/775), [lodestar#6512](https://github.com/ChainSafe/lodestar/pull/6512), [lodestar#4279](https://github.com/ChainSafe/lodestar/pull/4279), [nimbus#1007](https://github.com/status-im/nimbus-eth2/pull/1007)

</details>


<a id="state_cache-007"></a>
<details>
<summary><b>state_cache-007</b> Read-only callers use state references, not copies — <i>implemented · medium · S · cpu, memory, latency</i></summary>

**Idea.** Paths that only read the head, finalized or cached states (committee/duty APIs, RPC, monitors, pubkey lookups, attestation production, slot advance) should use a shared read-only reference or view, or pass only the needed values, instead of deep-copying the state or validator registry, and fetch it once per call.

**Impact.** Read paths take an Arc snapshot of the head; remaining state clones are cheap milhouse tree clones.

**Best measured result.** 400x improvement on mainnet config node (pr:prysm#4328)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/canonical_head.rs:728`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L728)
- [`beacon_node/beacon_chain/src/canonical_head.rs:748`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L748)
- [`beacon_node/http_api/src/state_id.rs:218`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/state_id.rs#L218)
- [`beacon_node/http_api/src/state_id.rs:184`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/state_id.rs#L184)

**Skeptic check.** Verified head_snapshot is an Arc clone, and the HTTP API map_state_and_execution_optimistic_and_finalized passes &amp;head state without a copy; StateId::state clones the head only through a milhouse structural clone. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#4328](https://github.com/OffchainLabs/prysm/pull/4328), [caplin#11854](https://github.com/erigontech/erigon/pull/11854), [lodestar@af6d704dc](https://github.com/ChainSafe/lodestar/commit/af6d704dca9a), [prysm#10101](https://github.com/OffchainLabs/prysm/pull/10101), [prysm#2368](https://github.com/OffchainLabs/prysm/pull/2368), [prysm#16745](https://github.com/OffchainLabs/prysm/pull/16745), [prysm#17424](https://github.com/OffchainLabs/prysm/pull/17424), [prysm#17055](https://github.com/OffchainLabs/prysm/pull/17055), [prysm#16511](https://github.com/OffchainLabs/prysm/pull/16511), [prysm#17425](https://github.com/OffchainLabs/prysm/pull/17425), [prysm#17716](https://github.com/OffchainLabs/prysm/pull/17716), [prysm#12326](https://github.com/OffchainLabs/prysm/pull/12326), [prysm#8303](https://github.com/OffchainLabs/prysm/pull/8303), [lodestar#8728](https://github.com/ChainSafe/lodestar/pull/8728)

</details>


<a id="state_cache-008"></a>
<details>
<summary><b>state_cache-008</b> Load or copy states into reused preallocated objects — <i>not · low · L · cpu, memory, latency</i></summary>

**Idea.** When loading a state from the DB or cache, or producing a new head or checkpoint copy, decode or copy into a preallocated spare state object that is reused, instead of allocating a fresh BeaconState each time. This removes heap allocations and full copies.

**Gap in Lighthouse.** No spare-object reuse: HDiffBuffer::as_state, load_hot_state and load_cold_state_by_slot allocate a new BeaconState and tree per load. Would need a state pool with in-place decode, which conflicts with milhouse immutable Arc trees.

**Impact.** Possibly smaller allocation churn and RSS during state loads (not the block import hot path); gain unclear since states are Arc trees, not flat arrays.

**Best measured result.** alloc 96 -&gt; 22 MB/s, anon RSS 18.2 -&gt; 12.4 GB, flush+commit p50 76 -&gt; 60 ms (pr:caplin#25003)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hdiff.rs:210`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs#L210) as_state builds a new BeaconState from SSZ bytes each time
- [`beacon_node/store/src/hot_cold_store.rs:1949`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1949) load_hot_state allocates a fresh state
- [`beacon_node/store/src/hot_cold_store.rs:2306`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2306) load_cold_state_by_slot allocates and clones into historic cache

**Sources.** [nimbus#937](https://github.com/status-im/nimbus-eth2/pull/937), [nimbus#942](https://github.com/status-im/nimbus-eth2/pull/942), [nimbus#5881](https://github.com/status-im/nimbus-eth2/pull/5881), [caplin#25003](https://github.com/erigontech/erigon/pull/25003), [caplin#8020](https://github.com/erigontech/erigon/pull/8020), [caplin#13797](https://github.com/erigontech/erigon/pull/13797)

</details>


<a id="state_cache-009"></a>
<details>
<summary><b>state_cache-009</b> Eliminate redundant second state copy on head paths — <i>n/a · medium · cpu, latency, memory</i></summary>

**Idea.** Where a privately copied head state is handed on (to synced-data holders or the next-slot advance), transfer ownership or skip the up-front copy when already at the target slot, so each head update or payload-attributes advance does at most one state copy.

**Impact.** Full-state copies cost ~ms in Caplin; in Lighthouse BeaconState clone is a persistent-tree clone, so a second copy is negligible.

**Best measured result.** second copy p50 38 -&gt; 0 ms; total p50 189 -&gt; 150 ms; anon mem 9.0-9.5 -&gt; 8.0-8.4 GB (pr:caplin#25237)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/canonical_head.rs:284`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L284) head snapshot shared via Arc
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:273`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L273) advance_head clones from cache via get_advanced_hot_state

**Sources.** [caplin#25237](https://github.com/erigontech/erigon/pull/25237), [prysm#16836](https://github.com/OffchainLabs/prysm/pull/16836)

</details>


<a id="state_cache-010"></a>
<details>
<summary><b>state_cache-010</b> Send only needed head fields to network service — <i>n/a · low · S · memory, cpu</i></summary>

**Idea.** On head change, pass the network/p2p service just the head fields it uses instead of the whole beacon state, avoiding a large clone or transfer per head update.

**Impact.** None for a mainnet node: The network service gets no head state on head change; it only receives small messages and the state is Arc/tree-shared anyway.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/network/src/service.rs:139`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/service.rs#L139) NetworkMessage variants carry small fields, no BeaconState
- [`beacon_node/beacon_chain/src/canonical_head.rs:751`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L751) state clone is a cheap milhouse clone
- The network service gets no head state on head change; it only receives small messages and the state is Arc/tree-shared anyway.

**Sources.** [grandine@262885200](https://github.com/grandinetech/grandine/commit/2628852009ee), [grandine#431](https://github.com/grandinetech/grandine/pull/431)

</details>


<a id="state_cache-011"></a>
<details>
<summary><b>state_cache-011</b> Hand-written state copy instead of reflection clone — <i>n/a · low · S · cpu, memory</i></summary>

**Idea.** Replace generic reflection-based clones of states and checkpoints with specialized copy methods, which are cheaper per copy.

**Impact.** None for a mainnet node: Rust Clone is derived and monomorphic; milhouse clones are structural-sharing Arc bumps, no reflection.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/exit_cache.rs:12`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/exit_cache.rs#L12) plain derived Clone
- Rust Clone is derived and monomorphic; milhouse clones are structural-sharing Arc bumps, no reflection.

**Sources.** [prysm#4806](https://github.com/OffchainLabs/prysm/pull/4806)

</details>


<a id="state_cache-012"></a>
<details>
<summary><b>state_cache-012</b> Copy validator trie rather than move on recompute — <i>n/a · low · S · cpu, latency</i></summary>

**Idea.** When a validator field trie is recomputed, copy it instead of transferring it, so a late block at a registry change does not recompute all validator roots from scratch.

**Impact.** None for a mainnet node: No field-trie ownership transfer exists; milhouse persistent trees share nodes via Arc and clones never lose cached hashes.

**Best measured result.** avoids expensive full root recompute; slight memory increase (pr:prysm#13661)

**Evidence (Lighthouse @ 928b61e719).**

- milhouse d67aabd src/tree.rs persistent tree
- No field-trie ownership transfer exists; milhouse persistent trees share nodes via Arc and clones never lose cached hashes.

**Sources.** [prysm#13661](https://github.com/OffchainLabs/prysm/pull/13661)

</details>


<a id="state_cache-013"></a>
<details>
<summary><b>state_cache-013</b> Dedupe dirty indices before full field-trie rebuild — <i>n/a · low · S · cpu</i></summary>

**Idea.** When the dirty-index count of a field trie reaches its rebuild limit, deduplicate the indices first and rebuild the whole trie only if still over the limit.

**Impact.** None for a mainnet node: Milhouse uses an update map applied to the tree and rehashes only dirty subtrees; no dirty-index limit/rebuild threshold.

**Evidence (Lighthouse @ 928b61e719).**

- milhouse d67aabd src/update_map.rs, src/interface.rs
- Milhouse uses an update map applied to the tree and rehashes only dirty subtrees; no dirty-index limit/rebuild threshold.

**Sources.** [prysm#13660](https://github.com/OffchainLabs/prysm/pull/13660)

</details>


<a id="state_cache-014"></a>
<details>
<summary><b>state_cache-014</b> Defragment copy-on-write state lists periodically — <i>n/a · low · S · cpu, latency, memory</i></summary>

**Idea.** Rebuild copy-on-write multi-value state lists into a fresh base once they accumulate many per-index modification layers, so reads on long-running nodes stay fast.

**Impact.** None for a mainnet node: Milhouse persistent trees have no per-index modification layers; updates are applied into the tree by apply_updates, so no layers accumulate.

**Best measured result.** non-trivial effect on block processing for nodes running weeks (no numbers) (pr:prysm#13444)

**Evidence (Lighthouse @ 928b61e719).**

- milhouse d67aabd src/interface.rs, src/update_map.rs
- Milhouse persistent trees have no per-index modification layers; updates are applied into the tree by apply_updates, so no layers accumulate.

**Sources.** [prysm#13444](https://github.com/OffchainLabs/prysm/pull/13444)

</details>


<a id="state_cache-015"></a>
<details>
<summary><b>state_cache-015</b> Pointer-free fixed-size validator records — <i>n/a · low · S · memory</i></summary>

**Idea.** Store validators in memory as fixed-size structs with inline pubkey and withdrawal credential arrays, without slice headers, pointers or per-validator allocations, cutting memory per validator.

**Impact.** None for a mainnet node: Validator is already a fixed-size Rust struct with inline pubkey bytes and Hash256, stored packed in tree leaves without pointers.

**Best measured result.** Removes ~8B ptr, 24B*2 slice headers, ~16B*3 malloc overhead, protobuf fields per validator (table in PR) (pr:prysm#16535)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/validator/validator.rs:21-31`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/validator/validator.rs#L21-L31) Validator fields inline
- Validator is already a fixed-size Rust struct with inline pubkey bytes and Hash256, stored packed in tree leaves without pointers.

**Sources.** [prysm#16535](https://github.com/OffchainLabs/prysm/pull/16535)

</details>


<a id="state_cache-016"></a>
<details>
<summary><b>state_cache-016</b> Drop duplicate flat validator caches beside state — <i>implemented · low · S · memory, cpu</i></summary>

**Idea.** Do not keep a flat array copy of validator data next to the state tree; represent validator leaves compactly in the tree and keep only a small effective-balance array for hot reads, so each cached state holds validator data once.

**Impact.** Cached states hold validator data once, in the tree.

**Best measured result.** 658MB less per state (1593MB -&gt; 935MB); hashing ~x2 slower, epoch +8ms with full deposits (pr:lodestar#3046)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:542`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L542)
- [`consensus/types/src/state/epoch_cache.rs:33`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/epoch_cache.rs#L33)
- [`beacon_node/store/src/hdiff.rs:102`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs#L102)

**Skeptic check.** Validators are a single milhouse List per state; the flat Vec&lt;Validator&gt; exists only in HDiffBuffer for diffing, not next to each cached state. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#3046](https://github.com/ChainSafe/lodestar/pull/3046), [lodestar#3009](https://github.com/ChainSafe/lodestar/pull/3009)

</details>


<a id="state_cache-017"></a>
<details>
<summary><b>state_cache-017</b> Per-state validator deltas over shared finalized registry — <i>implemented · medium · S · memory</i></summary>

**Idea.** Keep the immutable validator data (pubkey, credentials) in one shared finalized registry and store only per-state deltas of mutable fields, instead of a full validator array per state.

**Impact.** Structural sharing plus rebase_on gives per-state deltas over the finalized registry.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/state_cache.rs:197`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L197)
- [`consensus/types/src/state/beacon_state.rs:3416`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L3416)
- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:24`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L24)

**Skeptic check.** milhouse shares unchanged validator subtrees between states, and rebase_on_finalized re-shares states loaded from disk. A mutated leaf copies the whole Validator including its pubkey, not only the mutable fields, but the memory effect is close to the same. Upheld.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [silver#34](https://github.com/gattaca-com/silver/pull/34)

</details>


<a id="state_cache-018"></a>
<details>
<summary><b>state_cache-018</b> Compress effective balances and use iterator committees — <i>partial · low · S · memory, cpu, startup, disk</i></summary>

**Idea.** Store effective balances in compressed form in memory, use iterator-based committee and participation computation to avoid small allocations, and avoid DB reads when rewinding to head on in-memory states.

**Gap in Lighthouse.** Tree-states (milhouse) share validators structurally and EpochCache gives O(1) balance lookups, so the memory problem is mostly solved differently. Effective balances remain Vec&lt;u64&gt;; could be Vec&lt;u8&gt; increments in EpochCache::new.

**Impact.** Small memory saving (8x on one Vec per cached epoch, ~1MB at 1M validators); epoch processing already uses single_pass.

**Best measured result.** medalla unfinalized 4gb -&gt; 1gb; 40% speedup on epoch processing (pr:nimbus#1899)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/epoch_cache.rs:36`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/epoch_cache.rs#L36) EpochCache effective_balances Vec&lt;u64&gt; (uncompressed, Arc-shared)
- [`consensus/types/src/state/committee_cache.rs:26`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/committee_cache.rs#L26) CommitteeCache plain Vec&lt;usize&gt; shuffling

**Sources.** [nimbus#1899](https://github.com/status-im/nimbus-eth2/pull/1899)

</details>


<a id="state_cache-019"></a>
<details>
<summary><b>state_cache-019</b> Avoid allocations in exit queue and head update — <i>n/a · low · S · memory, cpu</i></summary>

**Idea.** Reuse the exit-queue vector instead of reallocating it, skip fetching the state cache on head update when unneeded, and drop allocating live validator counts.

**Impact.** None for a mainnet node: ExitCache is three scalars (initialized, max_exit_epoch, churn), so there is no exit-queue vector to reuse; head update has no live-validator-count allocation to drop.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/exit_cache.rs:13-20`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/exit_cache.rs#L13-L20) scalar-only cache
- ExitCache is three scalars (initialized, max_exit_epoch, churn), so there is no exit-queue vector to reuse; head update has no live-validator-count allocation to drop.

**Sources.** [nimbus#1939](https://github.com/status-im/nimbus-eth2/pull/1939)

</details>


<a id="state_cache-020"></a>
<details>
<summary><b>state_cache-020</b> One shared append-only decompressed validator key list — <i>implemented · low · S · memory, cpu</i></summary>

**Idea.** Since the validator key list is append-only along a chain, keep one decompressed pubkey list shared by all per-epoch caches (older caches point to the newest longer list) instead of each cached epoch reference owning a copy.

**Impact.** One chain-wide decompressed pubkey list; states do not own copies.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:24`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L24)
- [`consensus/types/src/state/pubkey_cache.rs:9`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/pubkey_cache.rs#L9)

**Skeptic check.** ValidatorPubkeyCache is one append-only Vec of decompressed keys for the whole chain; the per-state pubkey_cache is a persistent pubkey-to-index map, not decompressed keys. Upheld.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#1562](https://github.com/status-im/nimbus-eth2/pull/1562), [nimbus#1486](https://github.com/status-im/nimbus-eth2/pull/1486), [nimbus@abe0d7b4a](https://github.com/status-im/nimbus-eth2/commit/abe0d7b4aeee)

</details>


<a id="state_cache-021"></a>
<details>
<summary><b>state_cache-021</b> LRU eviction for checkpoint state cache — <i>n/a · medium · cpu, latency</i></summary>

**Idea.** Evict checkpoint state cache entries by least-recent use rather than insertion order, so checkpoint states that attestations keep targeting stay cached instead of being recomputed via epoch processing.

**Impact.** No checkpoint state cache exists; hot states live in an LRU keyed by state root and attestations are served by the shuffling cache, so there is no insertion-order eviction to fix.

**Best measured result.** hit ratio 70% to 95% without validators; 25% to 70% with 512 validators (pr:prysm#7010)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/state_cache.rs:43`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L43) states is an LruCache by state root, with cull() at :357 favouring LRU

**Sources.** [prysm#7010](https://github.com/OffchainLabs/prysm/pull/7010)

</details>


<a id="state_cache-022"></a>
<details>
<summary><b>state_cache-022</b> LRU eviction for committee/shuffling cache — <i>implemented · low · S · cpu</i></summary>

**Idea.** Use LRU rather than FIFO eviction in the committee/shuffling cache, so historical state regeneration touching old epochs does not evict hot shufflings.

**Impact.** Inserting old-epoch shufflings during regen evicts the oldest-epoch entries, never recent or head-protected ones, which meets the goal of the LRU change.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/shuffling_cache.rs:256-283`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L256-L283) (prune_cache sorts by shuffling_epoch, evicts lowest, skips head prev/current/next ids)
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:128-131`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L128-L131) (HashMap keyed by AttestationShufflingId)

**Skeptic check.** Not LRU literally, but epoch-ordered eviction with head protection prevents the FIFO failure the Prysm PR fixed; earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#8996](https://github.com/OffchainLabs/prysm/pull/8996)

</details>


<a id="state_cache-023"></a>
<details>
<summary><b>state_cache-023</b> Hash maps for state cache indices — <i>n/a · low · S · cpu, memory</i></summary>

**Idea.** Index state and checkpoint caches with proper hash maps keyed by root and by epoch rather than generic object dictionaries, for cheaper insert, delete and size.

**Impact.** Rust already uses typed HashMap/BTreeMap indexes; the JS object-dictionary problem does not exist.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/state_cache.rs:28`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L28) BlockMap is a HashMap&lt;Hash256,SlotMap&gt;; states is LruCache keyed by root

**Sources.** [lodestar@c047d388a](https://github.com/ChainSafe/lodestar/commit/c047d388a6ab)

</details>


<a id="state_cache-024"></a>
<details>
<summary><b>state_cache-024</b> Key checkpoint cache by (epoch, root) without hashing — <i>n/a · low · cpu</i></summary>

**Idea.** Use the (epoch, root) tuple directly as the checkpoint state cache key instead of computing a hash tree root of the checkpoint container per access.

**Impact.** Lighthouse has no checkpoint state cache keyed by hashed checkpoint; keys are existing roots, no per-access hashing.

**Best measured result.** add/get/delete 146us/op to 49.8us/op (6836 to 20073 ops/s) (pr:lodestar#2745)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/state_cache.rs:43`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L43) states LruCache keyed by state_root Hash256
- no checkpoint-state cache found (grep CheckpointCache)

**Sources.** [lodestar#2745](https://github.com/ChainSafe/lodestar/pull/2745)

</details>


<a id="state_cache-025"></a>
<details>
<summary><b>state_cache-025</b> Index checkpoint cache variants per root compactly — <i>n/a · low · S · cpu, memory</i></summary>

**Idea.** For checkpoint states that exist in several variants per root (e.g. payload present or not), track which variants exist per root per epoch with a small bitmask index so lookups and pruning touch only existing variants without probing all of them.

**Impact.** Lighthouse has no checkpoint-state cache with per-root payload variants; hot states are keyed by state root so variants are distinct keys.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/state_cache.rs:40`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L40) states keyed by state_root, no per-root checkpoint variant cache

**Sources.** [lodestar#9006](https://github.com/ChainSafe/lodestar/pull/9006), [lodestar#9019](https://github.com/ChainSafe/lodestar/pull/9019)

</details>


<a id="state_cache-026"></a>
<details>
<summary><b>state_cache-026</b> Compute past shuffling from reference state plus RANDAO — <i>not · medium · M · cpu, latency, disk</i></summary>

**Idea.** On a shuffling cache miss, or for the randao endpoint, compute the shuffling from any available state with the locked-in active validator set plus a RANDAO mix recovered from intermediate reveals or payloads, instead of loading and replaying a full state to the epoch.

**Gap in Lighthouse.** No path builds a shuffling or answers the randao endpoint from a reference state plus a RANDAO mix recovered from blocks/payloads. The miss path always loads (and may replay) a full state; partial_state_advance only skips state-root hashing.

**Impact.** Avoids multi-second state loads/replays on old-epoch or deep-fork shuffling misses and randao queries; rare on a healthy node.

**Best measured result.** replay can take several seconds (pr:nimbus#4911)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/shuffling_cache.rs:432`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L432) miss path loads a full state with store.get_advanced_hot_state
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:453`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L453) then partial_state_advance and committee cache build on that state
- [`consensus/types/src/state/beacon_state.rs:2373`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2373) get_seed reads randao_mixes only from the state itself; no API takes an external mix
- [`beacon_node/http_api/src/beacon/states.rs:412`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/beacon/states.rs#L412) randao endpoint reads get_randao_mix on a fully loaded state

**Second check.** Grepped all get_randao_mix/get_seed/set_randao_mix users in beacon_node and consensus types; every caller works on a loaded state, none splices a mix into a cached state.

**Verdict history.** not (checked) → not (refuted)

**Sources.** [nimbus#4959](https://github.com/status-im/nimbus-eth2/pull/4959), [nimbus#5190](https://github.com/status-im/nimbus-eth2/pull/5190), [nimbus#8608](https://github.com/status-im/nimbus-eth2/pull/8608), [nimbus#5197](https://github.com/status-im/nimbus-eth2/pull/5197), [nimbus#4911](https://github.com/status-im/nimbus-eth2/pull/4911)

</details>


<a id="state_cache-027"></a>
<details>
<summary><b>state_cache-027</b> Cache active validator indices per epoch — <i>implemented · low · S · cpu</i></summary>

**Idea.** Cache get_active_validator_indices per epoch in a fork-safe per-state cache, keyed consistently so it hits, since it is called many times per epoch.

**Impact.** Active indices are cached per epoch in CommitteeCache and shared through the shuffling cache.

**Best measured result.** Epoch 1024 validators 2.053-&gt;0.613 s/op; 3072: 16.2-&gt;2.7 s/op (pr:teku#1111)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/committee_cache.rs:135`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/committee_cache.rs#L135)
- [`consensus/types/src/state/beacon_state.rs:1163`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L1163)
- [`consensus/state_processing/src/consensus_context.rs:104`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/consensus_context.rs#L104)
- [`consensus/state_processing/src/block_replayer.rs:259`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/block_replayer.rs#L259)

**Skeptic check.** The uncached get_active_validator_indices still runs in the pre-Fulu get_beacon_proposer_index, in get_beacon_proposer_indices and in sync committee selection. These run once per epoch or period, or are skipped because ConsensusContext and BlockReplayer take the proposer index from the block, so the hot paths are covered. Upheld.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#1111](https://github.com/Consensys-Incorporated/teku/pull/1111), [caplin#18542](https://github.com/erigontech/erigon/pull/18542)

</details>


<a id="state_cache-028"></a>
<details>
<summary><b>state_cache-028</b> Compute committee shuffling once per epoch and cache — <i>implemented · medium · S · cpu, memory</i></summary>

**Idea.** Compute the shuffling and committees once per epoch (previous, current, next) and keep them in an always-on cache reused by all callers (attestations, block operations, proposer and duty lookups), instead of rebuilding per slot or per call.

**Impact.** Committees are built once per epoch and shared via the shuffling cache.

**Best measured result.** 8192 validators: 4661218 ns/op, 1.6MB, 229 allocs uncached vs 99.5 ns/op, 0 allocs cached (pr:prysm#2095)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/shuffling_cache.rs:112`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L112)
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:326`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L326)
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:409`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L409)
- [`consensus/state_processing/src/per_epoch_processing/altair.rs:30`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/altair.rs#L30)

**Skeptic check.** Verified previous, current and next committee caches are built in epoch processing, and the ShufflingCache keyed by AttestationShufflingId serves attestation and duty callers. Upheld.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#1112](https://github.com/Consensys-Incorporated/teku/pull/1112), [lighthouse@779b6266a](https://github.com/sigp/lighthouse/commit/779b6266a5da), [prysm#4522](https://github.com/OffchainLabs/prysm/pull/4522), [prysm#2095](https://github.com/OffchainLabs/prysm/pull/2095), [lighthouse@944ac73ef](https://github.com/sigp/lighthouse/commit/944ac73ef9be), [lighthouse@94a39c3cb](https://github.com/sigp/lighthouse/commit/94a39c3cb6c0), [caplin#12778](https://github.com/erigontech/erigon/pull/12778)

</details>


<a id="state_cache-029"></a>
<details>
<summary><b>state_cache-029</b> Cache proposer indices per epoch — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Compute the proposer index list for an epoch once (at epoch transition or on first miss) and cache it so proposer lookups do not rerun the shuffle per call.

**Impact.** Proposers are computed once per (epoch, decision root); post-Fulu they come from the proposer_lookahead in the state.

**Best measured result.** "Fixes #4500"; flame improvement (pr:prysm#4528)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_proposer_cache.rs:85`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_proposer_cache.rs#L85)
- [`consensus/types/src/state/beacon_state.rs:1642`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L1642)

**Skeptic check.** BeaconProposerCache caches EpochBlockProposers per epoch and decision root; after Fulu get_beacon_proposer_index reads proposer_lookahead with no shuffle. Upheld.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#4528](https://github.com/OffchainLabs/prysm/pull/4528)

</details>


<a id="state_cache-030"></a>
<details>
<summary><b>state_cache-030</b> Correct committee cache validity checks — <i>implemented · medium · S · cpu</i></summary>

**Idea.** Check committee/epoch cache freshness against the actual epoch requested (and load the cache for the current state epoch while applying slots), so valid caches are hit rather than rebuilt.

**Impact.** Cache validity is checked against the requested epoch.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:2824`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2824)
- [`consensus/types/src/state/beacon_state.rs:2955`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2955)
- [`consensus/types/src/state/committee_cache.rs:175`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/committee_cache.rs#L175)
- [`consensus/types/src/state/beacon_state.rs:2887`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2887)

**Skeptic check.** build_committee_cache and committee_cache both call is_initialized_at with the requested relative epoch, and advance_caches rotates the caches at the epoch boundary so valid caches carry over. Upheld.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse@64dca6fba](https://github.com/sigp/lighthouse/commit/64dca6fba70b), [nimbus@b11da2cb3](https://github.com/status-im/nimbus-eth2/commit/b11da2cb3476)

</details>


<a id="state_cache-031"></a>
<details>
<summary><b>state_cache-031</b> Cache total active balance with shuffling — <i>implemented · low · S · cpu</i></summary>

**Idea.** Store total active balance in the shuffling/committee cache entry, computed alongside the active indices, so block processing does not scan validators for it.

**Impact.** Block processing (sync aggregate rewards, slashings, churn) reads total active balance in O(1) from the state cache. Single-pass epoch processing fills it for the next epoch. A full scan only happens when a state loaded from disk builds its caches once.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:819`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L819)
- [`consensus/types/src/state/beacon_state.rs:2682`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2682)
- [`consensus/types/src/state/beacon_state.rs:2703`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2703)
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:482`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L482)
- [`consensus/types/src/state/beacon_state.rs:2838`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2838)

**Skeptic check.** Confirmed. Lighthouse keeps the cache on the state as (Epoch, u64), not in the shuffling cache like Prysm, but the effect is the same: block processing does not scan validators. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#9187](https://github.com/OffchainLabs/prysm/pull/9187)

</details>


<a id="state_cache-032"></a>
<details>
<summary><b>state_cache-032</b> Array-indexed pubkey cache without locks — <i>partial · low · M · cpu, latency</i></summary>

**Idea.** Store validator public keys in an array indexed by validator index (contiguous, growable without blocking) with a concurrent map for pubkey-to-index, instead of a synchronized LRU or loading validator state, removing lock contention.

**Gap in Lighthouse.** Array-indexed and decompressed, but guarded by a RwLock and the map is a plain HashMap, so writers (block import) block readers. Could use an append-only chunked/ArcSwap structure and concurrent map.

**Impact.** Removes read-lock contention on gossip signature verification during block import; likely minor since writes are short.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:24`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L24) Vec&lt;PublicKey&gt; indexed by validator index plus HashMap&lt;PublicKeyBytes,usize&gt;
- beacon_chain.rs holds it under a RwLock

**Sources.** [teku#10527](https://github.com/Consensys-Incorporated/teku/pull/10527), [teku#10528](https://github.com/Consensys-Incorporated/teku/pull/10528), [caplin#8774](https://github.com/erigontech/erigon/pull/8774)

</details>


<a id="state_cache-033"></a>
<details>
<summary><b>state_cache-033</b> Node-wide decompressed pubkey cache — <i>partial · low · S · cpu, memory, startup</i></summary>

**Idea.** Keep one node-wide cache of decompressed BLS public keys so signature checks and committee work never redo point decompression and per-state key caches are unnecessary.

**Gap in Lighthouse.** Gossip and API verification of voluntary exits, proposer slashings and attester slashings (verify_voluntary_exit_for_gossip, verify_proposer_slashing_for_gossip and verify_attester_slashing_for_gossip, through ObservedOperations::verify_and_observe and then VerifyOperation::validate) calls verify_exit, verify_proposer_slashing and verify_attester_slashing with VerifySignatures::True. Those use get_pubkey_from_state, which runs pubkey.decompress() on every signer from state.validators. One attester slashing can need hundreds to thousands of decompressions. The paranoid_block_proposal re-check at beacon_chain.rs:6002 does the same. Fix: build the signature sets with the ValidatorPubkeyCache closure, as block_verification does.

**Impact.** Low. Blocks, attestations, aggregates and sync messages already use the node-wide cache. Only rare gossip operations, mainly attester slashings, pay for decompression (about 50us per key).

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:24`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L24)
- [`beacon_node/beacon_chain/src/block_verification.rs:2215`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L2215)
- [`consensus/state_processing/src/per_block_processing/signature_sets.rs:61`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/signature_sets.rs#L61)
- [`consensus/state_processing/src/verify_operation.rs:222`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/verify_operation.rs#L222)
- [`consensus/state_processing/src/verify_operation.rs:237`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/verify_operation.rs#L237)
- [`consensus/state_processing/src/verify_operation.rs:261`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/verify_operation.rs#L261)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2872`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2872)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:6002`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L6002)

**Skeptic check.** The node-wide ValidatorPubkeyCache is real and is used on the hot paths (blocks, attestations, sync). The earlier verdict missed that the VerifyOperation gossip path for exits and slashings still decompresses keys from the state. The per-state PubkeyCache maps keys to indices only, so it is not a decompression cache.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [grandine#243](https://github.com/grandinetech/grandine/pull/243)

</details>


<a id="state_cache-034"></a>
<details>
<summary><b>state_cache-034</b> Fill committee cache asynchronously — <i>not · low · L · latency, cpu</i></summary>

**Idea.** Build the committee cache in the background from the active-indices getters, so callers that only need indices or counts are not blocked on the build and cancellation does not abort it.

**Gap in Lighthouse.** Would need committee-cache building moved to a background task from active-index getters; Lighthouse state accessors are synchronous and take &amp;mut self, so this is a redesign for little gain.

**Impact.** Would save a little latency for callers needing only counts; Lighthouse builds caches once per epoch so gain is marginal.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:2768`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2768) build_all_committee_caches synchronous
- [`consensus/types/src/state/beacon_state.rs:2824`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2824) build_committee_cache synchronous
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:352`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L352) miss path computes inline under a promise

**Sources.** [prysm#16814](https://github.com/OffchainLabs/prysm/pull/16814)

</details>


<a id="state_cache-035"></a>
<details>
<summary><b>state_cache-035</b> Run epoch cache priming off the slot thread — <i>implemented · medium · S · latency</i></summary>

**Idea.** Run epoch cache priming on an async executor, also when the state is already cached, so it never blocks the slot tick.

**Impact.** Priming never runs on the timer task, even when the head state is cached.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/state_advance_timer.rs:163`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L163) advance_head spawned via executor.spawn_blocking, timer only sleeps
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:332`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L332) committee caches built inside the blocking task
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:356`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L356) proposer/attester cache priming in the same task

**Skeptic check.** Verified advance_head (state fetch, committee cache builds, proposer and shuffling cache priming) always runs in spawn_blocking, independent of whether the state is cached. Earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#6214](https://github.com/Consensys-Incorporated/teku/pull/6214)

</details>


<a id="state_cache-036"></a>
<details>
<summary><b>state_cache-036</b> Shuffling cache holds in-flight promises — <i>implemented · medium · S · cpu, latency, disk</i></summary>

**Idea.** On a shuffling cache miss insert a promise into the cache so concurrent requests for the same shuffling wait on the first computation instead of each loading a state and recomputing it.

**Impact.** On a miss, with_cached_shuffling creates a promise while it holds the write lock, and later callers wait on it. Attestation verification and duties reach it through with_committee_cache.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/shuffling_cache.rs:102`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L102)
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:287`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L287)
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:314`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L314)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:7602`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L7602)

**Skeptic check.** Confirmed that the promise is created under the write lock and that waiters call cache_item.wait(). This is Lighthouse's own PR #3574, and the earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#9664](https://github.com/OffchainLabs/prysm/pull/9664), [lighthouse#3574](https://github.com/sigp/lighthouse/pull/3574)

</details>


<a id="state_cache-037"></a>
<details>
<summary><b>state_cache-037</b> Single-flight state regeneration and loads — <i>partial · medium · M · cpu, memory, latency</i></summary>

**Idea.** Route state regeneration and hot or diff-buffer loads through a promise cache or queue that registers a shared result immediately, coalesces duplicate requests and starts from the nearest cached or in-flight state, so one state triggers one computation.

**Gap in Lighthouse.** Shuffling and proposer computations are single-flight, and replay caches epoch-boundary states and hdiff buffers for later reuse, but concurrent get_hot_state/get_advanced_hot_state/load_hot_hdiff_buffer/cold loads for the same root each run the full load or replay. Add an in-flight map (OnceCell/oneshot) keyed by state root.

**Impact.** Saves duplicate state loads/replays when several requests hit the same uncached state; modest on a healthy node.

**Best measured result.** Removing shuffling cache costs ~10ms (rare) to 20-50ms (rapid) per request on author machine (pr:lighthouse#5313)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/shuffling_cache.rs:36`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L36) CacheItem::Promise single-flights shuffling computation
- [`beacon_node/beacon_chain/src/beacon_proposer_cache.rs:197`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_proposer_cache.rs#L197) proposer duties single-flight via Arc&lt;OnceCell&gt;::get_or_try_init
- [`beacon_node/store/src/hot_cold_store.rs:1124`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1124) get_advanced_hot_state: cache check then uncoordinated load_hot_state
- [`beacon_node/store/src/hot_cold_store.rs:1812`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1812) get_hot_state: same, no in-flight registry
- [`beacon_node/store/src/hot_cold_store.rs:1861`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1861) load_hot_hdiff_buffer checks cache then loads without coalescing
- [`beacon_node/store/src/hot_cold_store.rs:2041`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2041) replay caches epoch-boundary states so later loads can start from them

**Second check.** Beyond the earlier review, found the proposer cache OnceCell single-flight and the replay hook that caches epoch-boundary states; searched store and beacon_chain for OnceCell/Promise/Notify/shared futures and found no in-flight coalescing for state loads.

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [teku#2589](https://github.com/Consensys-Incorporated/teku/pull/2589), [teku#2628](https://github.com/Consensys-Incorporated/teku/pull/2628), [teku#2690](https://github.com/Consensys-Incorporated/teku/pull/2690), [prysm#4597](https://github.com/OffchainLabs/prysm/pull/4597), [teku#2629](https://github.com/Consensys-Incorporated/teku/pull/2629), [lighthouse#5313](https://github.com/sigp/lighthouse/pull/5313)

</details>


<a id="state_cache-038"></a>
<details>
<summary><b>state_cache-038</b> Compact per-checkpoint attestation verification cache — <i>implemented · low · S · memory, cpu</i></summary>

**Idea.** Verify attestation signatures from a compact per-checkpoint cache holding only committees/shuffling and pubkeys, rather than retaining a full beacon state per checkpoint, which lets the state cache shrink.

**Impact.** Attestation verification keeps only committee caches plus the global pubkey cache; no per-checkpoint state.

**Best measured result.** reduces memory usage by 400-600MB (pr:prysm#7098)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/shuffling_cache.rs:315`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L315) with_cached_shuffling returns CachedShuffling (committees) keyed by shuffling id
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:351`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L351) read-lock hit path, no state
- [`beacon_node/beacon_chain/src/beacon_chain.rs:7593`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L7593) with_committee_cache used by attestation verification

**Skeptic check.** Confirmed attestation verification reads committees from the shuffling cache and pubkeys from the validator pubkey cache; a state is loaded only on a miss to build the committee cache, then dropped. Earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#7098](https://github.com/OffchainLabs/prysm/pull/7098), [prysm#7048](https://github.com/OffchainLabs/prysm/pull/7048), [prysm#7070](https://github.com/OffchainLabs/prysm/pull/7070)

</details>


<a id="state_cache-039"></a>
<details>
<summary><b>state_cache-039</b> Avoid pinning old head states in attestation workers — <i>implemented · low · S · memory</i></summary>

**Idea.** Take the previous-epoch attestation pre-state from the checkpoint state cache rather than having each concurrent worker hold the old head state, so old head states can be freed.

**Impact.** Workers hold only committee caches, so old head states are not pinned.

**Best measured result.** Avg RSS 9,417 vs 10,594 MB (-11%); avg HeapLive 1,411 vs 1,939 MB (-27%); peak RSS -1,839 MB (pr:prysm#16426)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/shuffling_cache.rs:351`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L351) cache hit returns Arc'd CachedShuffling without touching any state
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:399`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L399) head state cloned only on a miss and only to build the committee cache

**Skeptic check.** Confirmed workers hold a CachedShuffling, not a state; the miss path clones the head state only briefly to build the cache (and milhouse sharing makes the clone cheap). Earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#16426](https://github.com/OffchainLabs/prysm/pull/16426)

</details>


<a id="state_cache-040"></a>
<details>
<summary><b>state_cache-040</b> Select verification state by shuffling dependent root — <i>implemented · medium · S · cpu, memory, latency</i></summary>

**Idea.** Choose the state for attestation, sidecar and block validation by the shuffling decision (dependent) root rather than the target checkpoint root, so the head state is reused on sibling forks with the same shuffling and no parent state is loaded and advanced.

**Impact.** Attestations, blocks and columns on sibling forks with the same decision root share cache entries; no parent state load.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/shuffling_cache.rs:336`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L336) shuffling id from fork choice block decision roots
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:351`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L351) hit returns without a state
- [`beacon_node/beacon_chain/src/block_verification.rs:1027`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1027) gossip block proposer lookup keyed by proposer_shuffling_root_for_child_block
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1743`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1743) column proposer lookup keyed by decision root, state only on miss

**Skeptic check.** Verified attestations (shuffling cache), gossip blocks and data columns (proposer cache) all key by dependent/decision root, so a sibling fork reuses the cached entry. Full block signature verification loads the parent state, but import needs that state anyway. Earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#15996](https://github.com/OffchainLabs/prysm/pull/15996)

</details>


<a id="state_cache-041"></a>
<details>
<summary><b>state_cache-041</b> Epoch-indexed checkpoint cache bounded by epoch count — <i>n/a · medium · memory, latency</i></summary>

**Idea.** Index the checkpoint state cache by epoch and cap it by number of epochs or entries (never evicting justified/finalized), pruning eagerly even on skipped-slot checkpoints, so memory is bounded in non-finality, pruning needs no scan, and lookups can return the latest state for a root at or below an epoch.

**Impact.** Lighthouse has no checkpoint state cache; its hot state cache is capacity-bounded and culled, so non-finality memory is already bounded.

**Best measured result.** ~18-22 MB per entry at 1M validators (pr:caplin#24902)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/state_cache.rs:39`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L39) StateCache bounded by capacity, keyed by state root with cull() and finalization pruning at :127
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:111`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L111) shuffling cache capped at 16 and never evicts head ids

**Sources.** [caplin#24902](https://github.com/erigontech/erigon/pull/24902), [lodestar#3586](https://github.com/ChainSafe/lodestar/pull/3586), [lodestar#1538](https://github.com/ChainSafe/lodestar/pull/1538), [silver#258](https://github.com/gattaca-com/silver/pull/258), [lodestar@fa9f7ed50](https://github.com/ChainSafe/lodestar/commit/fa9f7ed506c5), [grandine@6fd918031](https://github.com/grandinetech/grandine/commit/6fd9180316a9), [lodestar#7497](https://github.com/ChainSafe/lodestar/pull/7497), [lodestar@69ea8676b](https://github.com/ChainSafe/lodestar/commit/69ea8676b843)

</details>


<a id="state_cache-042"></a>
<details>
<summary><b>state_cache-042</b> Spill older checkpoint states to disk, reload on miss — <i>implemented · high · S · memory, disk, cpu</i></summary>

**Idea.** Keep only a bounded set of recent block and checkpoint states in memory and persist older unfinalized states to disk, reloading them on demand (onto a shared base tree), so memory stays flat during long non-finality.

**Impact.** Unfinalized states are persisted to the hot DB and reloaded on miss; memory is bounded by the state cache size.

**Best measured result.** Used heap 4.7-5.7 GB to 3.2-3.8 GB (2 epochs, 32 states) and 2.8-3.4 GB (0 epochs, 4 states); reload ~2s (pr:lodestar#6008)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:1949`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1949) load_hot_state rebuilds unfinalized states from hot hdiffs or replay
- [`beacon_node/store/src/hot_cold_store.rs:1987`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1987) rebase_on_finalized for structural sharing
- [`beacon_node/store/src/state_cache.rs:357`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L357) cull bounds the in-memory state set
- [`beacon_node/store/src/config.rs:23`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/config.rs#L23) DEFAULT_STATE_CACHE_SIZE=128

**Skeptic check.** Confirmed hot states are stored on disk (hdiff/snapshot/replay summaries), the in-memory cache is a count-bounded LRU with culling, and reloaded states are rebased on the finalized state. Earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#6008](https://github.com/ChainSafe/lodestar/pull/6008), [lodestar#6176](https://github.com/ChainSafe/lodestar/pull/6176), [lodestar#6538](https://github.com/ChainSafe/lodestar/pull/6538), [teku#2308](https://github.com/Consensys-Incorporated/teku/pull/2308), [lodestar#6250](https://github.com/ChainSafe/lodestar/pull/6250), [caplin#8546](https://github.com/erigontech/erigon/pull/8546), [grandine@27e16fb69](https://github.com/grandinetech/grandine/commit/27e16fb69b0a), [grandine#86](https://github.com/grandinetech/grandine/pull/86), [lodestar#6359](https://github.com/ChainSafe/lodestar/pull/6359)

</details>


<a id="state_cache-043"></a>
<details>
<summary><b>state_cache-043</b> Cap number of persisted checkpoint states on disk — <i>partial · medium · M · disk</i></summary>

**Idea.** Delete old persisted checkpoint states so only a fixed count or number of epochs stays on disk, so long non-finality does not use hundreds of GB.

**Gap in Lighthouse.** Disk growth in non-finality is already small because hot states are stored as hierarchical diffs, and an operator can bound the hot DB by hand with POST /lighthouse/finalize (manual migration + prune_hot_db). There is no automatic cap or cull of hot summaries/diffs older than N epochs before finalization.

**Impact.** Only matters in long non-finality; diffs plus the manual-finalize endpoint already cover most of the risk, so an automatic cap would add little.

**Best measured result.** Stated: 250MB per state, over 56GB per day (pr:lodestar#7510)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:1661`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1661) store_hot_state writes summaries plus hdiff/snapshot only at hierarchy slots, not a full state per checkpoint
- [`beacon_node/store/src/hot_cold_store.rs:1771`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1771) store_hot_state_as_diff stores compressed diffs
- [`beacon_node/beacon_chain/src/migrate.rs:509`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L509) prune_hot_db runs only on a (real or manual) finalization notification
- [`beacon_node/http_api/src/lib.rs:2860`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L2860) POST lighthouse/finalize lets an operator force a migration/prune during non-finality
- [`beacon_node/beacon_chain/src/beacon_chain.rs:1837`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1837) manually_finalize_state -&gt; migrate.rs:293 run_manual_migration

**Second check.** Beyond the earlier review I found the manual finalization path (http_api lighthouse/finalize -&gt; manually_finalize_state -&gt; run_manual_migration -&gt; prune_hot_db). It is an operator-triggered equivalent, not an automatic cap, so the verdict stays partial.

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [lodestar#7510](https://github.com/ChainSafe/lodestar/pull/7510), [lodestar#8582](https://github.com/ChainSafe/lodestar/pull/8582)

</details>


<a id="state_cache-044"></a>
<details>
<summary><b>state_cache-044</b> Bounded hot states with replay regeneration — <i>implemented · medium · S · memory, cpu</i></summary>

**Idea.** Keep a bounded set of hot states (e.g. checkpoint states) in memory and regenerate an evicted state on demand by replaying blocks from the nearest retained ancestor state.

**Impact.** Evicted states regenerate from the nearest stored base state by block replay.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/state_cache.rs:357`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L357) cull: bounded LRU, keeps recent epoch boundary states
- [`beacon_node/store/src/hot_cold_store.rs:1993`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1993) ReplayFrom loads nearest base state
- [`beacon_node/store/src/hot_cold_store.rs:2031`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2031) load_hot_state_using_replay replays blocks

**Skeptic check.** Confirmed the bounded cache plus replay from the nearest stored base state (and caches intermediate epoch boundary states during replay). Earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#2065](https://github.com/Consensys-Incorporated/teku/pull/2065), [teku#2007](https://github.com/Consensys-Incorporated/teku/pull/2007), [lodestar#1514](https://github.com/ChainSafe/lodestar/pull/1514)

</details>


<a id="state_cache-045"></a>
<details>
<summary><b>state_cache-045</b> Bounded smaller in-memory hot block cache — <i>implemented · low · S · memory</i></summary>

**Idea.** Keep only a small bounded set of recent hot blocks in memory and load others from the DB on demand, so memory does not grow with unfinalized chain length and the node fits a small heap.

**Impact.** Hot blocks are not held in memory by default.

**Best measured result.** default cache sizes make Teku struggle to run within 1Gb heap (pr:teku#2329)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/config.rs:22`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/config.rs#L22) DEFAULT_BLOCK_CACHE_SIZE=0
- [`beacon_node/store/src/hot_cold_store.rs:229`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L229) block cache created only when size &gt; 0, else blocks read from DB

**Skeptic check.** Confirmed the block cache is disabled by default and blocks load from the DB on demand. Earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#2271](https://github.com/Consensys-Incorporated/teku/pull/2271), [teku#2329](https://github.com/Consensys-Incorporated/teku/pull/2329)

</details>


<a id="state_cache-046"></a>
<details>
<summary><b>state_cache-046</b> Bound state cache by measured bytes — <i>not · low · M · memory</i></summary>

**Idea.** Limit the hot state cache by measured memory (deduplicating structurally shared nodes) instead of state count, re-measuring periodically and pruning in batches.

**Gap in Lighthouse.** Add a MemoryTracker-based (milhouse) byte measurement to StateCache::put_state with periodic re-measure and a byte ceiling alongside the count capacity; PR 7803 was closed as stale.

**Impact.** Hot state cache would adapt to actual structural sharing instead of a fixed count; mainnet default count is small so memory savings are modest and mainly help tuning.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/state_cache.rs:41`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L41) states: LruCache with count capacity
- [`beacon_node/store/src/config.rs:39`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/config.rs#L39) state_cache_size count-based
- grep for max_bytes/MemorySize in store, beacon_chain: no hits (PR 7803 closed unmerged)

**Sources.** [lighthouse#7803](https://github.com/sigp/lighthouse/pull/7803)

</details>


<a id="state_cache-047"></a>
<details>
<summary><b>state_cache-047</b> Configurable smaller snapshot cache size — <i>implemented · low · S · memory</i></summary>

**Idea.** Make the snapshot/state cache size configurable and default it lower to reduce memory held by cached states.

**Impact.** The state cache size can be set with --state-cache-size. Tree-states share structure, so each cached state costs little memory.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/src/cli.rs:833`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/cli.rs#L833)
- [`beacon_node/store/src/config.rs:23`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/config.rs#L23)
- [`beacon_node/store/src/hot_cold_store.rs:232`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L232)

**Skeptic check.** Confirmed the flag and the default. This is Lighthouse's own PR #5270. The snapshot cache it tuned was replaced by the configurable StateCache.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#5270](https://github.com/sigp/lighthouse/pull/5270)

</details>


<a id="state_cache-048"></a>
<details>
<summary><b>state_cache-048</b> Size state caches to cover forks and late blocks — <i>implemented · medium · S · cpu, latency</i></summary>

**Idea.** Size the block-state and checkpoint-state caches to cover concurrent forks and late or orphaned blocks (e.g. 64 blocks, 3+ epochs), so misses do not force epoch transitions, state roots or disk regeneration.

**Impact.** Cache covers about 4 epochs of block states across forks, larger than the Lodestar 64-block fix.

**Best measured result.** Hit ratio 97.9% to 99.9%, saving ~2000 hash tree roots and epoch transitions (pr:prysm#4818)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/config.rs:23`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/config.rs#L23) DEFAULT_STATE_CACHE_SIZE=128
- [`beacon_node/store/src/state_cache.rs:18`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L18) EPOCH_FINALIZATION_LIMIT=4, boundary states that could finalize culled last
- [`beacon_node/store/src/state_cache.rs:316`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L316) get_by_block_root serves any fork and ancestor slot

**Skeptic check.** Confirmed 128 states, fork-agnostic lookup by block root, and culling that drops advanced and mid-epoch states before possibly-finalizing boundary states. Earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#4818](https://github.com/OffchainLabs/prysm/pull/4818), [lodestar#7104](https://github.com/ChainSafe/lodestar/pull/7104)

</details>


<a id="state_cache-049"></a>
<details>
<summary><b>state_cache-049</b> Size state cache from real preset — <i>n/a · low · S · cpu</i></summary>

**Idea.** Derive the state cache size from the active network preset (several epochs of slots) so sync does not regenerate states because the cache is too small.

**Impact.** Teku bug was a hard-coded size too small for the preset; Lighthouse sync does not use the hot state cache and 128 is CLI-tunable (--state-cache-size).

**Best measured result.** cache size 40 instead of 160 wasted CPU during sync (pr:teku#3459)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/config.rs:23`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/config.rs#L23) fixed 128 states (4 mainnet epochs)
- [`beacon_node/store/src/state_cache.rs:357`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L357) cull() keeps recent epochs

**Sources.** [teku#3459](https://github.com/Consensys-Incorporated/teku/pull/3459)

</details>


<a id="state_cache-050"></a>
<details>
<summary><b>state_cache-050</b> Replay-window-sized cache during historical regeneration — <i>implemented · low · S · startup, cpu</i></summary>

**Idea.** When regenerating archived states, size the temporary state cache to cover the replay window and free it afterwards, so regeneration reuses states without leaving garbage.

**Impact.** load_cold_state_by_slot looks through replay_from_range(slot) for a cached prior state and replays from it. Consecutive cold-state loads reuse the previous state, and the bounded LRU leaves no garbage.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:2306`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2306)
- [`beacon_node/store/src/hot_cold_store.rs:2312`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2312)
- [`beacon_node/store/src/config.rs:26`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/config.rs#L26)
- [`beacon_node/store/src/historic_state_cache.rs:15`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/historic_state_cache.rs#L15)

**Skeptic check.** The mechanism is different (a persistent, bounded LRU plus a search over the replay window, not a temporary cache sized to the window), but it has the same effect: no repeated replay and no memory left behind. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#5613](https://github.com/OffchainLabs/prysm/pull/5613)

</details>


<a id="state_cache-051"></a>
<details>
<summary><b>state_cache-051</b> Committees API uses configurable shuffling cache — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Have the committees HTTP API consult (and fill) the shuffling cache, with configurable size, before rebuilding a shuffling, so repeated queries for old epochs are not recomputed.

**Impact.** The committees endpoint reads from and fills a configurable LRU of CommitteeCache, keyed by shuffling id or finalized epoch, so it does not compute the shuffling again for repeated epochs.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/caches.rs:22`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/caches.rs#L22)
- [`beacon_node/http_api/src/beacon/states.rs:632`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/beacon/states.rs#L632)
- [`beacon_node/http_api/src/beacon/states.rs:680`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/beacon/states.rs#L680)
- [`beacon_node/http_api/src/lib.rs:153`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L153)

**Skeptic check.** Confirmed the get and insert around CommitteeCache::initialized. The cache is consulted only inside map_state_and_execution_optimistic_and_finalized, so the state is still loaded for every request. That cost is outside this idea, which is about not recomputing the shuffling.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#4007](https://github.com/sigp/lighthouse/pull/4007), [lighthouse#4081](https://github.com/sigp/lighthouse/pull/4081)

</details>


<a id="state_cache-052"></a>
<details>
<summary><b>state_cache-052</b> Limit validator-triggered head advance during sync — <i>n/a · medium · memory</i></summary>

**Idea.** Cap how far validator requests may advance the head state (e.g. one epoch) so the checkpoint cache does not fill with divergent advanced states and OOM near sync.

**Gap in Lighthouse.** Validator-triggered advances are not inserted into the state cache (only state_advance_timer's one-slot advance is stored), so divergent advanced states cannot fill it; CPU cost of far advances is a separate issue (closed PR 10453).

**Best measured result.** avoids OOM (pr:lodestar#3169)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:2161`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2161) attestation_data uses get_advanced_hot_state then partial_state_advance on a local copy, result not stored
- [`beacon_node/http_api/src/attester_duties.rs:50`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/attester_duties.rs#L50) rejects request_epoch &gt; current_epoch+1
- [`beacon_node/http_api/src/proposer_duties.rs:81-124`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/proposer_duties.rs#L81-L124) epoch gating
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:38`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L38) MAX_ADVANCE_DISTANCE=256

**Sources.** [lodestar#3169](https://github.com/ChainSafe/lodestar/pull/3169)

</details>


<a id="state_cache-053"></a>
<details>
<summary><b>state_cache-053</b> Disable full-state checkpoint cache by default — <i>n/a · low · S · memory</i></summary>

**Idea.** Do not enable a full-state checkpoint cache by default when it retains too much memory; rely on compact caches instead.

**Impact.** Lighthouse's state cache holds structurally shared tree states, so the memory problem of a full-state checkpoint cache does not arise; there is no separate checkpoint state cache to disable.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/state_cache.rs:215`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L215) put_state stores states as shared-tree milhouse (no pending mutations)
- [`beacon_node/store/src/hot_cold_store.rs:232`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L232) cache always on

**Sources.** [prysm#7560](https://github.com/OffchainLabs/prysm/pull/7560)

</details>


<a id="state_cache-054"></a>
<details>
<summary><b>state_cache-054</b> Remove skip-slot state cache — <i>n/a · low · S · memory</i></summary>

**Idea.** Do not keep a separate skip-slot state cache holding several full states: during sync it retains many states, fast hashing makes it of little value, and a next-slot (pre-advanced head) cache serves the same requests.

**Impact.** Lighthouse has no separate skip-slot cache; the unified state cache plus the state-advance timer already play the suggested role.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/state_advance_timer.rs:98`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L98) spawn_state_advance_timer pre-advances head
- [`beacon_node/store/src/hot_cold_store.rs:1124`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1124) get_advanced_hot_state

**Sources.** [prysm#5829](https://github.com/OffchainLabs/prysm/pull/5829), [prysm#12235](https://github.com/OffchainLabs/prysm/pull/12235)

</details>


<a id="state_cache-055"></a>
<details>
<summary><b>state_cache-055</b> Pooled buffer for state serialization — <i>not · low · M · cpu, memory</i></summary>

**Idea.** Serialize states for persistence and reload into a preallocated growable buffer from a pool, returned after use, instead of allocating a fresh state-sized buffer each time.

**Gap in Lighthouse.** Add a reusable Vec&lt;u8&gt; pool (or ssz encode into a pre-sized buffer) used by HDiffBuffer::from_state and store_hot_state_as_snapshot/store_cold_state_as_snapshot.

**Impact.** Saves a state-sized allocation (~250MB on mainnet) per snapshot/diff buffer; small CPU gain, mostly lower allocator churn and peak RSS.

**Best measured result.** now takes less than 300ms to serialize a mainnet state (pr:lodestar#7109)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hdiff.rs:197`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs#L197) HDiffBuffer::from_state calls as_ssz_bytes() with a fresh Vec
- [`beacon_node/store/src/hot_cold_store.rs:2148`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2148) store_cold_state_as_snapshot as_ssz_bytes then compress copy
- grep found no buffer pool in store/src

**Sources.** [lodestar#7109](https://github.com/ChainSafe/lodestar/pull/7109), [lodestar#6269](https://github.com/ChainSafe/lodestar/pull/6269), [caplin#23152](https://github.com/erigontech/erigon/pull/23152)

</details>


<a id="state_cache-056"></a>
<details>
<summary><b>state_cache-056</b> Serve head state from cache, bypass regen queue — <i>implemented · low · S · latency, cpu</i></summary>

**Idea.** Get the head (or epoch-correct) state directly from the state cache and only go through the state regeneration queue on a real miss, so cache-answerable requests never wait in or get dropped from the queue.

**Impact.** None: no regen queue exists; cache hits and head reads never wait.

**Best measured result.** voluntary_exit validation sometimes took up to 4s waiting on regen (pr:lodestar#5401)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:1124`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1124) get_advanced_hot_state returns get_advanced_hot_state_from_cache hit before any DB load
- [`beacon_node/http_api/src/state_id.rs:179`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/state_id.rs#L179) head state id served from cached_head snapshot clone
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2845`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2845) verify_voluntary_exit_for_gossip uses head snapshot state directly

**Skeptic check.** Verified the cache-first lookup and that head state reads (API, exit validation) use the in-memory head snapshot. Lighthouse has no regen queue to bypass, so the earlier evidence is right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#5401](https://github.com/ChainSafe/lodestar/pull/5401), [lodestar#1946](https://github.com/ChainSafe/lodestar/pull/1946), [lodestar@1b132eb0c](https://github.com/ChainSafe/lodestar/commit/1b132eb0c62d), [lodestar#2486](https://github.com/ChainSafe/lodestar/pull/2486), [lodestar#1723](https://github.com/ChainSafe/lodestar/pull/1723)

</details>


<a id="state_cache-057"></a>
<details>
<summary><b>state_cache-057</b> Attestation pre-state from checkpoint cache first — <i>implemented · medium · S · cpu, latency, disk</i></summary>

**Idea.** Cache the state advanced to each attestation target checkpoint and look it up before processing slots or reading the DB, so repeated attestations for the same target do not redo slot processing.

**Impact.** Repeated attestations for a target hit the shuffling cache; slot processing runs once per shuffling id.

**Best measured result.** 10x improvement (flame graph) (pr:prysm#4688)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/shuffling_cache.rs:349`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L349) read-locked shuffling cache hit by shuffling id
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:375`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L375) promise dedups concurrent misses
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:432`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L432) miss path uses head snapshot or get_advanced_hot_state then partial_state_advance
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:395`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L395) primes next-epoch shuffling

**Skeptic check.** Lighthouse caches the derived committees, not the advanced checkpoint state. Attestation validation only needs the committees, so the effect is the same. Concurrent misses are deduped by a promise. Earlier verdict holds.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#4688](https://github.com/OffchainLabs/prysm/pull/4688), [teku#2599](https://github.com/Consensys-Incorporated/teku/pull/2599), [prysm#3333](https://github.com/OffchainLabs/prysm/pull/3333)

</details>


<a id="state_cache-058"></a>
<details>
<summary><b>state_cache-058</b> Cache slot-advanced states keyed by (root, slot) — <i>partial · medium · M · cpu, latency, memory</i></summary>

**Idea.** Cache states advanced through empty slots keyed by (block/state root, slot), hitting also when the cached state is already at the requested slot, and share them between gossip validation, duties and block production so process_slots and epoch transitions run once.

**Gap in Lighthouse.** Lighthouse shares the single-slot advanced head state through the state cache, and caches what is derived from it (committees with promise dedup, proposers), so most repeated epoch transitions are avoided. Multi-slot partial advances, which have no state root, are still not cached as states. attestation_data across epochs, block production on a stale head, and shuffling-cache misses each re-run process_slots. The fix is a small (root, slot) to partial-advanced-state cache, as in closed PR 10453.

**Impact.** Saves repeated epoch transitions only when the head is behind by one or more epochs (skipped slots, outages). No change in normal operation.

**Best measured result.** Epoch transition run 4 times for first block of epoch; 3 of 4 removed (pr:teku#3265)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/state_cache.rs:316`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L316) get_by_block_root returns cached state at or below max_slot for a block root
- [`beacon_node/store/src/hot_cold_store.rs:1124`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1124) get_advanced_hot_state checks the state cache first (shared by block verification, block production, duties, gossip)
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:455`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L455) advanced head state put into the store/state cache; :355,:409 primes proposer and shuffling caches
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:106`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L106) Promise items dedup concurrent committee computations keyed by (epoch, decision root)
- [`beacon_node/beacon_chain/src/beacon_proposer_cache.rs:175`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_proposer_cache.rs#L175) with_proposer_cache caches proposer duties, advancing at :346 only on miss
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2161`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2161) attestation_data partial_state_advance result not cached
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5454`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5454) block production partial advance not cached

**Second check.** I also checked the shuffling cache promise dedup and the proposer cache. Both are equivalents for the derived data, not for the advanced state. All partial_state_advance call sites still discard the advanced state.

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [prysm#9077](https://github.com/OffchainLabs/prysm/pull/9077), [lighthouse#10453](https://github.com/sigp/lighthouse/pull/10453), [prysm#4694](https://github.com/OffchainLabs/prysm/pull/4694), [prysm#5279](https://github.com/OffchainLabs/prysm/pull/5279), [prysm#5280](https://github.com/OffchainLabs/prysm/pull/5280), [prysm#10447](https://github.com/OffchainLabs/prysm/pull/10447), [prysm#3879](https://github.com/OffchainLabs/prysm/pull/3879), [teku#3265](https://github.com/Consensys-Incorporated/teku/pull/3265), [grandine@6ebe3d723](https://github.com/grandinetech/grandine/commit/6ebe3d723206), [prysm#9422](https://github.com/OffchainLabs/prysm/pull/9422)

</details>


<a id="state_cache-059"></a>
<details>
<summary><b>state_cache-059</b> Cache intermediate empty-slot states — <i>not · low · S · cpu, latency</i></summary>

**Idea.** When advancing a state through skipped slots, process slot by slot and cache the intermediate (block, slot) states so later requests for them need no recomputation.

**Gap in Lighthouse.** get_advanced_hot_state / BlockReplayer could put_state each intermediate empty-slot state during advance so later requests at an earlier slot skip work. Only helps rare long-skip paths.

**Impact.** Saves recomputing a few slot transitions on rare skipped-slot requests; negligible on a mainnet node.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:1124-1186`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1124-L1186) get_advanced_hot_state caches only the final advanced state
- [`beacon_node/store/src/state_cache.rs:316`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L316) get_by_block_root finds nearest ancestor slot

**Sources.** [nimbus@7efd113a7](https://github.com/status-im/nimbus-eth2/commit/7efd113a757a)

</details>


<a id="state_cache-060"></a>
<details>
<summary><b>state_cache-060</b> Cheap skip-slot cache key without state hashing — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Key the skip-slot/advanced-state cache by a cheap unique identifier (latest block header root plus slot) instead of the full state hash tree root, keeping the key unique per state.

**Impact.** Advanced-state lookups cost map accesses, not a tree hash.

**Best measured result.** BenchmarkCacheKey 3261 ns/op -&gt; 174.7 ns/op (about 18x) (pr:prysm#11441)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/state_cache.rs:313`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L313) get_by_block_root looks up block_map[block_root] then the nearest slot &lt;= max_slot, no hashing
- [`beacon_node/store/src/hot_cold_store.rs:1196`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1196) get_advanced_hot_state_from_cache

**Skeptic check.** Confirmed the advanced-state cache is keyed by (block_root, slot) and the lookup computes no tree hash root.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#11441](https://github.com/OffchainLabs/prysm/pull/11441), [prysm#4391](https://github.com/OffchainLabs/prysm/pull/4391), [prysm#8443](https://github.com/OffchainLabs/prysm/pull/8443)

</details>


<a id="state_cache-061"></a>
<details>
<summary><b>state_cache-061</b> Use skip-slot cache only when ahead of input — <i>n/a · low · S · cpu</i></summary>

**Idea.** Start from a skip-slot cache entry only if its slot is ahead of the state passed in, so the code never rewinds to it, reprocesses slots and rewrites the cache.

**Impact.** No skip-slot cache exists; lookups are keyed by block root and never rewind past the requested max slot.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/state_cache.rs:327`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L327) get_by_block_root only picks entries with slot &lt;= requested slot, keyed by block root
- [`beacon_node/store/src/hot_cold_store.rs:1130`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1130) cache lookup before load

**Sources.** [prysm#13728](https://github.com/OffchainLabs/prysm/pull/13728)

</details>


<a id="state_cache-062"></a>
<details>
<summary><b>state_cache-062</b> Write cache only if entry is newer — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Write a state to the advanced-state cache only when the cached entry's slot is lower than the newly computed one, so equal or stale states do not churn the cache.

**Impact.** States are keyed by state root and also indexed as block_root -&gt; slot -&gt; state_root. A lower-slot state cannot overwrite an advanced one, a duplicate is rejected before any clone or cull, and get_by_block_root returns the closest state at or below the requested slot.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/state_cache.rs:236`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L236)
- [`beacon_node/store/src/state_cache.rs:270`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L270)
- [`beacon_node/store/src/state_cache.rs:316`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L316)

**Skeptic check.** Prysm's guard protects a single-entry skip-slot cache. Lighthouse's design makes that overwrite impossible, and put_state returns Duplicate early, so the effect (no stale overwrite and no churn on duplicates) holds.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#3913](https://github.com/OffchainLabs/prysm/pull/3913)

</details>


<a id="state_cache-063"></a>
<details>
<summary><b>state_cache-063</b> Correct next-slot cache key after payload — <i>partial · low · S · cpu, latency</i></summary>

**Idea.** Key state saves and the next-slot cache by the right access root (execution block hash when parent payload is full) so lookups hit instead of recomputing slot processing.

**Gap in Lighthouse.** Cache lookup is keyed by (block_root, slot), so an empty-payload and a full-payload state of the same block at the same slot map to one slot_map entry. Gloas path should be checked for collisions; may need payload status in the SlotMap key.

**Impact.** Avoids wrongly missed or wrong next-slot cache hits on Gloas only; nothing on today's mainnet.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/state_cache.rs:316`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L316) get_by_block_root picks state by block_root then slot only
- [`beacon_node/store/src/hot_cold_store.rs:1124`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1124) get_advanced_hot_state takes block_root+state_root

**Sources.** [prysm#16459](https://github.com/OffchainLabs/prysm/pull/16459)

</details>


<a id="state_cache-064"></a>
<details>
<summary><b>state_cache-064</b> Gate state advance behind its feature flag — <i>n/a · low · S · cpu</i></summary>

**Idea.** Skip the trailing-slot state advance wherever it is invoked when its cache is disabled, so no advance work is wasted.

**Gap in Lighthouse.** Lighthouse has no flag that disables the state advance cache; the timer always runs and the advanced state is used by block production and attestation, so there is nothing to gate.

**Impact.** None; no wasted work from a disabled feature.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/client/src/builder.rs:768`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/client/src/builder.rs#L768) spawn_state_advance_timer is always called
- [`beacon_node/beacon_chain/src/state_advance_timer.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs)

**Sources.** [prysm#8376](https://github.com/OffchainLabs/prysm/pull/8376)

</details>


<a id="state_cache-065"></a>
<details>
<summary><b>state_cache-065</b> Cache every epoch-boundary state produced during import — <i>implemented · medium · S · cpu, disk, sync, memory</i></summary>

**Idea.** While processing blocks (including batch sync), keep each epoch-boundary state as a checkpoint state in memory, so attestation validation, regen, justified/finalized lookups and migration find it instead of replaying.

**Impact.** Skipped-slot epoch-boundary states and block post-states stay in memory, with boundary states culled last.

**Best measured result.** state copying was 1/4 to 1/3 of rewind time (pr:nimbus#906)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:1609`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1609) per-slot loop stores every new intermediate (skip-slot) state via store_hot_state, for gossip and chain-segment import alike
- [`beacon_node/store/src/hot_cold_store.rs:1667`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1667) store_hot_state puts the state into state_cache
- [`beacon_node/store/src/hot_cold_store.rs:2048`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2048) replay hook caches states during reconstruction
- [`beacon_node/store/src/state_cache.rs:347`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L347) cull evicts advanced and mid-epoch states before epoch-boundary states

**Skeptic check.** Verified that the skip-slot boundary state (target block advanced to the epoch start) is stored and cached when the next block is imported, and that a boundary block's post-state is cached on import. One small detail: if the state summary already exists, store_hot_state is skipped, so that state is not re-cached. This does not change the verdict.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#12579](https://github.com/OffchainLabs/prysm/pull/12579), [prysm#6541](https://github.com/OffchainLabs/prysm/pull/6541), [lodestar#1516](https://github.com/ChainSafe/lodestar/pull/1516), [prysm#6542](https://github.com/OffchainLabs/prysm/pull/6542), [lodestar@b3dc98b1a](https://github.com/ChainSafe/lodestar/commit/b3dc98b1a560), [nimbus#906](https://github.com/status-im/nimbus-eth2/pull/906)

</details>


<a id="state_cache-066"></a>
<details>
<summary><b>state_cache-066</b> Bounded boundary-only cache during initial sync — <i>partial · low · S · memory, sync</i></summary>

**Idea.** During initial sync cache only epoch boundary states, cap the cache and flush to disk when full, and pool randao arrays, to bound memory while avoiding DB state reads.

**Gap in Lighthouse.** Lighthouse bounds the state cache with LRU and prefers keeping boundary states when culling, but it caches all states during sync, with no sync-specific boundary-only mode. Full-sync batch import could skip caching non-boundary states in put_state.

**Impact.** Slightly less cache churn and memory during range sync; states are persisted via hdiff anyway, so small gain.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/state_cache.rs:355`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L355) culling prefers epoch-boundary states
- [`beacon_node/store/src/state_cache.rs:39`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L39) bounded LRU StateCache with headroom

**Sources.** [prysm#4844](https://github.com/OffchainLabs/prysm/pull/4844)

</details>


<a id="state_cache-067"></a>
<details>
<summary><b>state_cache-067</b> Slot to epoch-boundary-root index — <i>implemented · low · S · latency, cpu</i></summary>

**Idea.** Keep a map from slot/epoch to epoch-boundary block root so finding a replay base for any slot needs no DB scan.

**Impact.** For hot states, the HotStateSummary of each state root names its diff base or snapshot. For cold states, cold_storage_strategy(slot) finds the base by arithmetic. Neither path scans the DB.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:3867`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3867)
- [`beacon_node/store/src/hot_cold_store.rs:1961`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1961)
- [`beacon_node/store/src/hot_cold_store.rs:2307`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2307)

**Skeptic check.** Confirmed that load_hot_state reads diff_base_state from the summary, and that cold loads compute the replay base from the slot. This is an equivalent index, so the earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#4993](https://github.com/OffchainLabs/prysm/pull/4993)

</details>


<a id="state_cache-068"></a>
<details>
<summary><b>state_cache-068</b> Read balances from checkpoint balances cache — <i>not · low · S · latency, disk</i></summary>

**Idea.** On finalization, read effective balances (e.g. for custody updates) from the checkpoint balances cache instead of loading the finalized state from disk.

**Gap in Lighthouse.** Lighthouse does not load the finalized state on finalization to compute custody; custody context is updated from validator registrations, so no disk read exists to remove.

**Impact.** Nothing to save; the expensive path does not exist.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_fork_choice_store.rs:59`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_fork_choice_store.rs#L59) BalancesCache exists only for justified balances
- [`beacon_node/beacon_chain/src/custody_context.rs:99`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/custody_context.rs#L99) cgc uses balances registered from validator registrations, not finalized state

**Sources.** [lodestar#8243](https://github.com/ChainSafe/lodestar/pull/8243)

</details>


<a id="state_cache-069"></a>
<details>
<summary><b>state_cache-069</b> Batch-load replay blocks concurrently — <i>not · medium · S · latency, disk</i></summary>

**Idea.** During state regeneration load all blocks to replay from the DB in one concurrent batch instead of one by one.

**Gap in Lighthouse.** Blocks for replay are read and SSZ-decoded one at a time by following parent roots. No batch read, no parallel decode, and the LRU block_cache is not used. A fix could get the block roots from hot state summaries, then batch-read and decode them in parallel with rayon.

**Impact.** Small. Hot DB reads are local. The gain is in the decode cost when a state cache miss replays up to one diff layer of blocks.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:2514`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2514) load_blocks_to_replay walks ParentRootBlockIterator one block at a time
- [`beacon_node/store/src/hot_cold_store.rs:663`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L663) get_blinded_block is a single hot_db.get_bytes + decode, no batching, no block_cache use
- [`beacon_node/store/src/hot_cold_store.rs:2042`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2042) load_hot_state_using_replay calls it synchronously

**Second check.** I checked get_blinded_block/get_block_with, the store's BlockCache, and the store for any multi_get or par_iter. Nothing batches or parallelizes the replay block loading.

**Verdict history.** not (checked) → not (refuted)

**Sources.** [lodestar#7033](https://github.com/ChainSafe/lodestar/pull/7033)

</details>


<a id="state_cache-070"></a>
<details>
<summary><b>state_cache-070</b> Read state cache file in one buffered read — <i>n/a · low · S · disk, latency</i></summary>

**Idea.** When loading a state's caches from disk, read the whole file at once and decode from memory instead of many small reads.

**Gap in Lighthouse.** Lighthouse stores states and caches in LevelDB/redb key-value values read in one get, not as files with many small reads.

**Impact.** None.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:2212`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2212) states stored as DB values, not files

**Sources.** [caplin#13056](https://github.com/erigontech/erigon/pull/13056)

</details>


<a id="state_cache-071"></a>
<details>
<summary><b>state_cache-071</b> Batch summary writes and cheaper replay base in sync — <i>n/a · medium · sync, disk</i></summary>

**Idea.** During sync, batch-save state summaries, read a block rather than a full state for its slot, and replay from the latest stored state at a slot rather than an epoch boundary.

**Impact.** Lighthouse writes a hot state summary for every imported block atomically with the block, so there is no lazy summary or block-read-for-slot problem.

**Best measured result.** 30-40% higher blocks per second (pr:prysm#5241)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:4752`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4752) PutState in same atomic batch as block
- [`beacon_node/store/src/hot_cold_store.rs:1661`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1661) store_hot_state writes summary+diff per block

**Sources.** [prysm#5241](https://github.com/OffchainLabs/prysm/pull/5241)

</details>


<a id="state_cache-072"></a>
<details>
<summary><b>state_cache-072</b> In-memory cache of recent blocks and states — <i>implemented · low · S · disk, latency</i></summary>

**Idea.** Keep an in-memory cache of recent blocks and states so block processing does not hit the DB repeatedly.

**Impact.** In-memory block and state caches front the DB on block import, API and fork-choice paths.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/state_cache.rs:39-49`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L39-L49) StateCache (LRU states + block_map + finalized_state)
- [`beacon_node/store/src/hot_cold_store.rs:74`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L74) block_cache: Option&lt;Mutex&lt;BlockCache&lt;E&gt;&gt;&gt;
- [`beacon_node/store/src/hot_cold_store.rs:96-139`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L96-L139) BlockCache LruCache of SignedBeaconBlock
- [`beacon_node/store/src/hot_cold_store.rs:1817`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1817) get_hot_state checks state_cache first
- [`beacon_node/store/src/hot_cold_store.rs:1130`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1130) get_advanced_hot_state checks cache first

**Skeptic check.** Verified the block LRU and the state LRU are both consulted before disk on the hot read paths. The earlier evidence is correct; the idea is the LH PR itself.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#677](https://github.com/sigp/lighthouse/pull/677)

</details>


<a id="state_cache-073"></a>
<details>
<summary><b>state_cache-073</b> Boot from persisted unfinalized checkpoint state — <i>implemented · medium · S · sync, startup</i></summary>

**Idea.** On restart, start from the last safe persisted unfinalized checkpoint state kept locally, rather than the finalized state, to cut resync time.

**Impact.** Restart resumes at the persisted head, with no resync from finalized.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/builder.rs:245`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/builder.rs#L245) resume_from_db loads persisted fork choice
- [`beacon_node/beacon_chain/src/builder.rs:783`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/builder.rs#L783) head state loaded from hot DB via get_advanced_hot_state
- [`beacon_node/store/src/hot_cold_store.rs:1661`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1661) all unfinalized states persisted in hot DB

**Skeptic check.** Lodestar#7509 fixed its own restart from the finalized state. Lighthouse already resumes from the persisted unfinalized head, so it gets the same effect by a stronger mechanism. Booting a fresh node from an externally supplied unfinalized state is a separate feature (part of the holesky-rescue work), not a restart speed-up.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#7509](https://github.com/ChainSafe/lodestar/pull/7509)

</details>


<a id="state_cache-074"></a>
<details>
<summary><b>state_cache-074</b> Keep genesis state in hot cache — <i>not · low · S · disk, latency</i></summary>

**Idea.** Keep the genesis state cached in memory instead of reading it from disk on each lookup.

**Gap in Lighthouse.** No dedicated in-memory genesis state; it is read from the cold DB on demand. Lookups are rare (genesis API, backfill to genesis) so a cache would help little.

**Impact.** Negligible; only occasional API requests for genesis state.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:2542`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2542) genesis state loaded from DB when needed
- [`beacon_node/beacon_chain/src/beacon_chain.rs:966`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L966) only genesis_state_root kept in memory

**Sources.** [prysm#11911](https://github.com/OffchainLabs/prysm/pull/11911)

</details>


<a id="state_cache-075"></a>
<details>
<summary><b>state_cache-075</b> Keep head state resident in memory — <i>implemented · low · S · cpu, latency, disk</i></summary>

**Idea.** Keep the head block and head state in memory in the chain/block pool and serve head, attestation, RPC and sync reads from it, avoiding a DB read, decode and replay.

**Impact.** Head reads are served from memory.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/canonical_head.rs:463`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L463) cached_head holds the head BeaconSnapshot
- [`beacon_node/beacon_chain/src/beacon_snapshot.rs:20`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_snapshot.rs#L20) snapshot contains beacon_state
- [`beacon_node/http_api/src/state_id.rs:179`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/state_id.rs#L179) head API reads from snapshot
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:400`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L400) attestation miss path prefers head snapshot state

**Skeptic check.** Confirmed the head block and state are kept in memory and used by the API, gossip validation and committee computation.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus@b994da78a](https://github.com/status-im/nimbus-eth2/commit/b994da78a7c4), [prysm#3279](https://github.com/OffchainLabs/prysm/pull/3279), [prysm#1775](https://github.com/OffchainLabs/prysm/pull/1775)

</details>


<a id="state_cache-076"></a>
<details>
<summary><b>state_cache-076</b> Insert DB-loaded states into state cache — <i>implemented · low · S · disk, latency</i></summary>

**Idea.** Put states loaded from storage on demand into the state cache so repeated requests do not reload and rebuild them.

**Impact.** Repeat requests for the same hot state hit the cache, API included.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:1812-1846`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1812-L1846) get_hot_state puts the disk-loaded state in state_cache when update_cache
- [`beacon_node/store/src/hot_cold_store.rs:1169-1182`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1169-L1182) get_advanced_hot_state puts the loaded state
- [`beacon_node/store/src/hot_cold_store.rs:2050-2066`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2050-L2066) replay hook caches epoch-boundary ancestors
- [`beacon_node/store/src/hot_cold_store.rs:1921-1924`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1921-L1924) load_hot_hdiff_buffer caches loaded buffers
- [`beacon_node/http_api/src/state_id.rs:197`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/state_id.rs#L197) API get_state passes update_cache=true
- [`beacon_node/beacon_chain/src/beacon_chain.rs:1597`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1597) state_at_slot caches with update_cache=true

**Skeptic check.** Confirmed get_hot_state and get_advanced_hot_state insert disk-loaded states, and the HTTP API path asks for caching. The earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [grandine#160](https://github.com/grandinetech/grandine/pull/160)

</details>


<a id="state_cache-077"></a>
<details>
<summary><b>state_cache-077</b> State cache owns slot processing with store option — <i>n/a · low · L · cpu, memory</i></summary>

**Idea.** Let the state cache perform slot processing itself, with an option to store the result only when forward synced, so the cache is used everywhere without memory churn during sync.

**Gap in Lighthouse.** Lighthouse separates slot processing (state advance timer) from the store cache; cheap milhouse clones avoid the churn the idea targets.

**Impact.** Marginal; design differs.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/state_advance_timer.rs:258-330`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L258-L330) advance_head runs per_slot_processing on a head-state clone
- [`beacon_node/store/src/state_cache.rs:215`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L215) put_state is insert-only

**Sources.** [grandine@a8e2ec391](https://github.com/grandinetech/grandine/commit/a8e2ec391183)

</details>


<a id="state_cache-078"></a>
<details>
<summary><b>state_cache-078</b> Avoid duplicate states across caches — <i>n/a · low · S · memory, disk</i></summary>

**Idea.** Before inserting into the checkpoint state cache, check only the in-memory hot/boundary caches and skip insertion when the same state is already held there, so states are not duplicated across caches.

**Gap in Lighthouse.** Lighthouse has no separate checkpoint state cache; one root-keyed LRU dedups and states share structure via milhouse.

**Impact.** None.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/state_cache.rs:226-229`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L226-L229) put_state returns Duplicate if root already cached
- [`beacon_node/store/src/hot_cold_store.rs:82`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L82),87 one hot StateCache plus historic cache

**Sources.** [prysm#7691](https://github.com/OffchainLabs/prysm/pull/7691), [prysm#7037](https://github.com/OffchainLabs/prysm/pull/7037)

</details>


<a id="state_cache-079"></a>
<details>
<summary><b>state_cache-079</b> Regenerate from nearest cached ancestor state — <i>partial · medium · S · disk, cpu, latency</i></summary>

**Idea.** When rebuilding a state (block replay or hierarchical diff chain), find the closest available ancestor in the in-memory caches (then the DB) and use it as base, only advancing slots or replaying blocks/diffs from there.

**Gap in Lighthouse.** Hot ReplayFrom path always replays from the diff-layer base (cached only as an hdiff buffer, which must be converted back to a state); it never looks in the full-state cache for that base or for a nearer cached ancestor (e.g. the parent's state) on the same chain. Look up state_cache by root for the base and walk back the block chain for the closest cached state before replaying.

**Impact.** Cheaper hot-state regeneration on cache miss (deep reorgs, API queries for old unfinalized states); rare on a healthy node.

**Best measured result.** Said to improve recent states a lot, little for old ones (pr:prysm#17580)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:2306`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2306) load_cold_state_by_slot searches historic_state_cache over replay_from_range(slot).rev() for the nearest prior cached state, then replays
- [`beacon_node/store/src/hot_cold_store.rs:2423`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2423) cold load_hdiff_buffer_for_slot checks hdiff buffer cache at every diff layer before going to disk
- [`beacon_node/store/src/hot_cold_store.rs:1860`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1860) hot load_hot_hdiff_buffer checks state_cache hdiff buffer cache at every layer (Snapshot/DiffFrom/ReplayFrom base)
- [`beacon_node/store/src/hot_cold_store.rs:1817`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1817) get_hot_state checks full-state cache only for the exact requested root
- [`beacon_node/store/src/hot_cold_store.rs:1987`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1987) hot ReplayFrom base loaded via load_hot_state (no full-state cache lookup, no nearer ancestor)
- [`beacon_node/store/src/hot_cold_store.rs:1124`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1124) get_advanced_hot_state uses get_by_block_root cache first

**Second check.** Beyond the earlier review, confirmed the hot hdiff buffer cache is consulted at every diff layer, so a cached ancestor is used as a buffer; the cold side fully implements the idea. The hot full-state nearest-ancestor lookup is still missing.

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [prysm#17580](https://github.com/OffchainLabs/prysm/pull/17580), [prysm#7063](https://github.com/OffchainLabs/prysm/pull/7063), [prysm#5475](https://github.com/OffchainLabs/prysm/pull/5475), [lodestar#1547](https://github.com/ChainSafe/lodestar/pull/1547)

</details>


<a id="state_cache-080"></a>
<details>
<summary><b>state_cache-080</b> Cancel state replay on request cancellation — <i>not · medium · M · cpu, latency</i></summary>

**Idea.** Check for request cancellation inside state loading and replay loops so long replays stop when the triggering API request is cancelled or times out.

**Gap in Lighthouse.** Pass a cancellation signal (for example tx.is_closed() on the oneshot, or a CancellationToken) from http_api task_spawner into get_state/load_*_state and the BlockReplayer hooks; at minimum skip queued blocking tasks whose receiver is already dropped.

**Impact.** Saves CPU and beacon-processor workers when clients time out on expensive historic state queries; only matters under API load.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/task_spawner.rs:60`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/task_spawner.rs#L60) blocking_task runs func unconditionally; the dropped receiver only makes tx.send fail after the work is done
- [`beacon_node/http_api/src/task_spawner.rs:198`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/task_spawner.rs#L198) send_to_beacon_processor has no cancellation path to the queued or running task
- [`beacon_node/http_api/src/beacon/execution_payload_envelopes.rs:248`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/beacon/execution_payload_envelopes.rs#L248) comment states blocking work is not cancelled
- [`beacon_node/store/src/hot_cold_store.rs:2555`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2555) replay_blocks has no cancellation check

**Second check.** Also checked the http_api TaskSpawner and beacon-processor dispatch: there is no early-exit on a dropped receiver even before the task starts, and the code base itself states that no work is cancelled.

**Verdict history.** not (checked) → not (refuted)

**Sources.** [prysm#7596](https://github.com/OffchainLabs/prysm/pull/7596)

</details>


<a id="state_cache-081"></a>
<details>
<summary><b>state_cache-081</b> Read anchor state fields from bytes before decode — <i>not · low · S · startup, memory, cpu</i></summary>

**Idea.** At startup read genesis, slot, validator stats and weak-subjectivity data directly from the serialized anchor state, fail fast on stale checkpoints, and deserialize the chosen state once.

**Gap in Lighthouse.** Checkpoint state is fully decoded before checks; would need to peek at SSZ bytes in the client builder before decoding (weak_subjectivity_state caller).

**Impact.** Saves seconds on checkpoint-sync startup in the stale-checkpoint failure case only.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/builder.rs:406-470`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/builder.rs#L406-L470) weak_subjectivity_state takes an already decoded BeaconState and checks genesis_validators_root after decoding

**Sources.** [lodestar#10200](https://github.com/ChainSafe/lodestar/pull/10200), [lodestar#10229](https://github.com/ChainSafe/lodestar/pull/10229)

</details>


<a id="state_cache-082"></a>
<details>
<summary><b>state_cache-082</b> Fall back to cached checkpoint state for parent — <i>implemented · medium · S · latency, cpu</i></summary>

**Idea.** When the parent post-state is missing, use the latest cached checkpoint state for the parent root and advance it, instead of failing or regenerating from far back.

**Impact.** A parent state cached at any slot (advanced or checkpoint) is reused and advanced.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/state_cache.rs:313`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L313) get_by_block_root returns the latest cached state for block_root at slot &lt;= max_slot
- [`beacon_node/store/src/hot_cold_store.rs:1130`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1130) get_advanced_hot_state cache first, then hot DB load
- [`beacon_node/beacon_chain/src/block_verification.rs:2063`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L2063) load_parent calls get_advanced_hot_state(parent_root, block.slot, ...)
- [`beacon_node/beacon_chain/src/block_verification.rs:1609`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1609) remaining slots advanced with per_slot_processing

**Skeptic check.** Compared with lodestar 92c65ba5a210, which falls back to the latest checkpoint state for the parent root. The Lighthouse lookup is by block root and the nearest slot, which covers that case. A full cache miss loads the state from the hot DB rather than failing.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar@92c65ba5a](https://github.com/ChainSafe/lodestar/commit/92c65ba5a210)

</details>


<a id="state_cache-083"></a>
<details>
<summary><b>state_cache-083</b> Store checkpoints in fork choice nodes — <i>implemented · low · S · latency, memory, cpu</i></summary>

**Idea.** Store justified and finalized checkpoints in each fork-choice node so queries need not load pruned beacon states from disk.

**Impact.** Fork choice and the debug/fork_choice endpoint never load states for checkpoints.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/proto_array/src/proto_array.rs:109-111`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L109-L111) ProtoNode justified_checkpoint/finalized_checkpoint
- [`consensus/proto_array/src/proto_array.rs:646-653`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/proto_array/src/proto_array.rs#L646-L653),711-715 filled on node insert
- [`beacon_node/http_api/src/lib.rs:2289-2298`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L2289-L2298) GET debug/fork_choice reads node.justified_checkpoint()/finalized_checkpoint() with no state load

**Skeptic check.** The grandine commit targeted the debug/fork_choice endpoint. LH serves it straight from the proto nodes, so the earlier evidence holds.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [grandine@07abe4ca2](https://github.com/grandinetech/grandine/commit/07abe4ca281f)

</details>


<a id="state_cache-084"></a>
<details>
<summary><b>state_cache-084</b> Clear parent derived caches on transfer to child — <i>n/a · low · S · memory</i></summary>

**Idea.** When a child state takes over cached derived views from its parent, clear them in the parent so retained hot states do not each hold a full set.

**Impact.** Derived caches are Arc-shared or live in structurally shared milhouse trees, so cloned states do not duplicate them.

**Best measured result.** 390 consecutive states: 414 MB -&gt; 226 MB; 130 states: 229 -&gt; 172 MB; no change in TransitionBenchmark (pr:teku#2061)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:825`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L825) committee_caches are Arc&lt;CommitteeCache&gt;, shared on clone
- milhouse tree-hash caches live in shared tree nodes

**Sources.** [teku#2061](https://github.com/Consensys-Incorporated/teku/pull/2061)

</details>


<a id="state_cache-085"></a>
<details>
<summary><b>state_cache-085</b> Keep late-block pre-state in snapshot cache — <i>implemented · medium · S · latency, cpu</i></summary>

**Idea.** When a block arrives late, clone its pre-state rather than moving it out of the snapshot cache, so a reorg to a sibling block imports without reloading state from disk.

**Impact.** A sibling block (reorg) finds the parent pre-state still cached.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/state_cache.rs:281`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L281) get_by_state_root clones the state and leaves the LRU entry in place
- [`beacon_node/store/src/state_cache.rs:313`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L313) get_by_block_root clones too
- [`beacon_node/beacon_chain/src/block_verification.rs:2063`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L2063) load_parent takes a clone via get_advanced_hot_state

**Skeptic check.** The snapshot cache from #2832 was replaced by the tree-states state_cache. That cache always clones, and with milhouse the clone is cheap, so the pre-state is never moved out of the cache. Same effect on every path.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#2832](https://github.com/sigp/lighthouse/pull/2832)

</details>


<a id="state_cache-086"></a>
<details>
<summary><b>state_cache-086</b> Dedicated temporary state for duty catch-up — <i>n/a · low · S · latency, memory</i></summary>

**Idea.** Use a dedicated scratch state for advancing to wall clock for duties, instead of borrowing head or clearance states that block imports reset.

**Gap in Lighthouse.** Lighthouse clones (cheap CoW tree) rather than borrowing head/clearance states, so no import-blocking contention.

**Impact.** None.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:1196`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1196) get_advanced_hot_state_from_cache returns a clone
- [`beacon_node/beacon_chain/src/canonical_head.rs:1329`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1329) duty paths use clones

**Sources.** [nimbus#6131](https://github.com/status-im/nimbus-eth2/pull/6131)

</details>


<a id="state_cache-087"></a>
<details>
<summary><b>state_cache-087</b> Skip re-persisting unchanged head state — <i>implemented · low · S · disk, cpu, latency</i></summary>

**Idea.** Remember the (block root, slot) of the last persisted head state and skip re-encoding and writing it when the same head is processed again.

**Impact.** Re-storing an already-persisted state costs one summary read instead of re-encoding diffs; no change.

**Best measured result.** A head-state dump takes ~405 ms p50; up to 8 redundant dumps per epoch avoided on Gloas (by code reasoning) (pr:caplin#25539)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:1681`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1681) PutStateOutcome::Duplicate falls through to summary check
- [`beacon_node/store/src/hot_cold_store.rs:1697`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1697) store_hot_state returns early when load_hot_state_summary(state_root) is Some, skipping summary+diff encoding

**Skeptic check.** Verified store_hot_state skips diff computation and writes when the state summary already exists in the DB. Earlier evidence was right; LH keys this on state root via a DB lookup rather than an in-memory (root, slot) memo, same effect.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [caplin#25539](https://github.com/erigontech/erigon/pull/25539)

</details>


<a id="state_cache-088"></a>
<details>
<summary><b>state_cache-088</b> Defer state cache pruning off slot start — <i>n/a · low · S · latency, cpu</i></summary>

**Idea.** Run state cache pruning later in the slot, not at slot start, so it does not compete with block import and attestation work.

**Gap in Lighthouse.** Pruning is event-driven (finalization / insert), not slot-start timed.

**Impact.** None.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/state_cache.rs:121-170`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L121-L170) update_finalized_state prunes on finalization
- state_cache.rs:357 cull only runs on insert over capacity

**Sources.** [grandine@5cdcb0d72](https://github.com/grandinetech/grandine/commit/5cdcb0d721a5)

</details>


<a id="state_cache-089"></a>
<details>
<summary><b>state_cache-089</b> Denser state snapshots for reorg replay — <i>not · low · S · latency, disk</i></summary>

**Idea.** Persist full states more often (e.g. every 4 slots instead of 32) so rebuilding a state on reorg replays fewer blocks.

**Gap in Lighthouse.** Lowering the hot diff interval (epochs_per_state_diff / hierarchy exponents) would shorten replay on a cache miss, at disk cost; reorgs normally hit the 128-state cache.

**Impact.** Helps only rare deep cache-miss reorgs; costs disk writes.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/config.rs:21`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/config.rs#L21) DEFAULT_EPOCHS_PER_STATE_DIFF=8
- [`beacon_node/store/src/hdiff.rs:622`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs#L622) exponents [5,9,11,13,16,18,21]
- [`beacon_node/store/src/hot_cold_store.rs:2031`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2031) load_hot_state_using_replay

**Sources.** [caplin#9796](https://github.com/erigontech/erigon/pull/9796)

</details>


<a id="state_cache-090"></a>
<details>
<summary><b>state_cache-090</b> Derive cached state block root from state itself — <i>implemented · low · S · memory, cpu, latency, disk</i></summary>

**Idea.** Derive the latest block root of a cached head state from the state's own header instead of a separately tracked field, avoiding stale-tracking mismatches that force state reloads.

**Impact.** The block root is derived from the state header; no separately tracked field can go stale.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:1882-1890`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L1882-L1890) get_latest_block_root derives from latest_block_header
- [`beacon_node/store/src/hot_cold_store.rs:1667-1670`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1667-L1670) store_hot_state keys cache by state.get_latest_block_root
- [`beacon_node/store/src/hot_cold_store.rs:2056`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2056) replay hook uses get_latest_block_root
- [`beacon_node/store/src/state_cache.rs:386`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L386) cull head check uses get_latest_block_root

**Skeptic check.** Verified that cache keys and the head-protection check derive the block root from the state itself. The earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#3507](https://github.com/status-im/nimbus-eth2/pull/3507), [caplin#9373](https://github.com/erigontech/erigon/pull/9373)

</details>


<a id="state_cache-091"></a>
<details>
<summary><b>state_cache-091</b> Diff-layered state storage with snapshots and LRU — <i>implemented · medium · L · disk, memory, latency</i></summary>

**Idea.** Store a compact parent-linked diff per state plus periodic full snapshots, rebuild states by applying diffs from the nearest snapshot, and front it with a small LRU of recent states.

**Impact.** Hierarchical diffs with snapshots in both hot and cold DB, fronted by an LRU state cache; no change.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hdiff.rs:33`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs#L33) HierarchyConfig
- [`beacon_node/store/src/hdiff.rs:98`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs#L98) HDiffBuffer
- [`beacon_node/store/src/hot_cold_store.rs:1741`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1741) store_hot_state_diffs (Snapshot / DiffFrom / ReplayFrom strategies)
- [`beacon_node/store/src/state_cache.rs:215`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L215) put_state LRU of full states plus hdiff buffer cache

**Skeptic check.** Verified hot states are stored as snapshot, diff from an ancestor layer, or replay-from per the hierarchy, and an LRU state cache plus HDiffBuffer cache sits in front. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [ethlambda#444](https://github.com/lambdaclass/ethlambda/pull/444)

</details>


<a id="state_cache-092"></a>
<details>
<summary><b>state_cache-092</b> Do not retain epoch processing results per state — <i>implemented · low · S · memory</i></summary>

**Idea.** Drop per-epoch processing intermediate data after the state transition, passing only what fork choice needs, so cached states do not each retain it.

**Impact.** Epoch processing intermediates are transient; per-epoch caches in BeaconState are Arc-shared, not duplicated per cached state.

**Best measured result.** 31MB per state; memory 1.6-1.9GB during sync (pr:lodestar#1693)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing.rs) EpochProcessingSummary returned, not stored in BeaconState
- [`consensus/types/src/state/epoch_cache.rs:22`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/epoch_cache.rs#L22) EpochCache is Option&lt;Arc&lt;Inner&gt;&gt; shared across states of the same epoch/decision block
- [`consensus/types/src/state/beacon_state.rs:825`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L825) committee_caches are Arc&lt;CommitteeCache&gt;

**Skeptic check.** Verified the epoch summary is a transient return value and the per-epoch data kept on states (EpochCache, committee caches) is behind Arc so cached states share one copy. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#1693](https://github.com/ChainSafe/lodestar/pull/1693), [lodestar@c5b201467](https://github.com/ChainSafe/lodestar/commit/c5b201467a1b)

</details>


<a id="state_cache-093"></a>
<details>
<summary><b>state_cache-093</b> Bound epoch/shuffling refs to recent blocks — <i>implemented · low · S · memory</i></summary>

**Idea.** Bound the per-epoch shuffling/epoch-info cache to a fixed count and do not attach epoch refs to every stored block, keeping them only for recent blocks.

**Impact.** Shuffling and proposer caches are fixed-size LRUs keyed by (epoch, decision root); blocks/proto-nodes carry no epoch refs.

**Best measured result.** mainnet memory down ~160-180MB; epoch cache from ~950MB to 600-700MB (pr:nimbus#2403)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/shuffling_cache.rs:25`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L25) DEFAULT_CACHE_SIZE = 16
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:36`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L36) MAX_CONCURRENT_PROMISES = 2
- [`beacon_node/beacon_chain/src/beacon_proposer_cache.rs:26`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_proposer_cache.rs#L26) CACHE_SIZE = 16 LruCache

**Skeptic check.** Verified both epoch-level caches are bounded at 16 entries and are looked up by shuffling id rather than attached to blocks. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#2403](https://github.com/status-im/nimbus-eth2/pull/2403), [nimbus#1645](https://github.com/status-im/nimbus-eth2/pull/1645)

</details>


<a id="state_cache-094"></a>
<details>
<summary><b>state_cache-094</b> Early return when replay is unnecessary — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** When the base state found for a load is already the target (zero slot diff or the finalized state itself), return it immediately without entering replay.

**Impact.** Replay is skipped when the base is already the target.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:2038-2040`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2038-L2040) load_hot_state_using_replay returns base_state when base.slot()==slot
- [`beacon_node/store/src/state_cache.rs:275-280`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L275-L280) get_by_state_root returns the finalized state directly
- [`beacon_node/store/src/hot_cold_store.rs:1152-1156`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1152-L1156) get_advanced_hot_state uses split state root for the split block

**Skeptic check.** Confirmed the zero-slot-diff early return and the finalized-state short-circuit. The earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#7853](https://github.com/OffchainLabs/prysm/pull/7853), [prysm#13198](https://github.com/OffchainLabs/prysm/pull/13198)

</details>


<a id="state_cache-095"></a>
<details>
<summary><b>state_cache-095</b> Stop reverse state-root iteration past target slot — <i>implemented · low · S · cpu, disk</i></summary>

**Idea.** When searching the reverse state-root iterator for a past slot, stop once the iterator passes the target slot instead of scanning the whole history.

**Impact.** Past-slot root lookups are bounded; no full-history scans on hot paths.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:1583-1589`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1583-L1589) state_at_slot uses forwards_iter_state_roots_until(slot,slot) + take_while
- [`beacon_node/beacon_chain/src/beacon_chain.rs:964-1010`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L964-L1010) state_root_at_slot: head fast path, then a bounded forwards iterator
- [`beacon_node/beacon_chain/src/canonical_head.rs:1689-1698`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1689-L1698) finalization find_map always hits (iterator yields every slot)

**Skeptic check.** Hot lookups now use bounded forwards iterators, which is stronger than take_while. The only unbounded find is root_at_slot_from_state (beacon_chain.rs:1716), and it runs only once, for weak-subjectivity verification at startup, with a slot below finality.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse@4fccec158](https://github.com/sigp/lighthouse/commit/4fccec158aaf)

</details>


<a id="state_cache-096"></a>
<details>
<summary><b>state_cache-096</b> Release refcount lock without defer — <i>n/a · low · cpu</i></summary>

**Idea.** Release the reference-count lock inline rather than via defer in hot state-copy paths.

**Impact.** Go defer overhead (about 1.6ns per op) has no Rust equivalent; Rust drops guards at no extra cost.

**Best measured result.** 30.4ns -&gt; 28.8ns per op (pr:prysm#6520)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/state_cache.rs:1`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L1) state cache is a plain LruCache behind one parking_lot Mutex; no refcount lock with defer

**Sources.** [prysm#6520](https://github.com/OffchainLabs/prysm/pull/6520)

</details>


<a id="state_cache-097"></a>
<details>
<summary><b>state_cache-097</b> Never scan or clone all cached states — <i>implemented · low · S · cpu, latency, memory</i></summary>

**Idea.** Do not iterate, deserialize or clone every cached state in a hot path (to find an epoch's first state or to prune); use keyed lookups and clone only the needed state.

**Impact.** No hot path scans or clones all cached states; the only full key listing is state_roots() in invariants.rs (debug).

**Best measured result.** processing time reduced from ~2500ms to ~200ms (pr:lodestar#1123)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/state_cache.rs:316`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L316) get_by_block_root uses block_map keyed lookup
- [`beacon_node/store/src/state_cache.rs:275`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L275) get_by_state_root clones only the requested state (structural-sharing clone)
- [`beacon_node/store/src/state_cache.rs:372`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L372) cull iterates by reference with early termination

**Skeptic check.** Verified lookups are keyed through block_map/LRU and cull inspects states by reference without cloning; state_roots() is only used by invariants checks. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#1123](https://github.com/ChainSafe/lodestar/pull/1123), [lodestar@df5c91a07](https://github.com/ChainSafe/lodestar/commit/df5c91a075be)

</details>


<a id="state_cache-098"></a>
<details>
<summary><b>state_cache-098</b> Cache post-execution-payload state — <i>n/a · low · latency, memory</i></summary>

**Idea.** Cache the post-payload state beside block states, pruned on finalization, so it is not regenerated.

**Impact.** Post-execution-payload state is a Gloas ePBS feature and this cache has no such state yet; revisit when Gloas state handling lands.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/state_cache.rs:36`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L36) StateCache holds only BeaconState values keyed by state root; no post-payload state concept in the cache

**Sources.** [teku#10302](https://github.com/Consensys-Incorporated/teku/pull/10302)

</details>


<a id="state_cache-099"></a>
<details>
<summary><b>state_cache-099</b> Dedicated small cache of epoch-boundary states — <i>implemented · medium · M · memory, disk, latency, cpu</i></summary>

**Idea.** Keep a separate small in-memory cache of epoch-boundary (checkpoint) states, retrievable by slot or block root, in front of the database. Epoch transitions, attestation target checks and hot-to-cold migration then read these states without DB loads or replay, and the main hot cache can shrink.

**Impact.** Boundary states are retained preferentially inside the single state cache rather than a separate one; attestation target checks use the shuffling cache, not states.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/state_cache.rs:357`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L357) cull evicts advanced, then old boundary, then mid-epoch, keeping finalizable epoch-boundary states last
- [`beacon_node/store/src/state_cache.rs:316`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L316) get_by_block_root(block_root, slot) returns the state at or before slot
- [`beacon_node/store/src/hot_cold_store.rs:2045`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2045) load_hot_state_using_replay hook caches epoch-boundary states during replay

**Skeptic check.** LH has no separate boundary-state cache, but the unified cache's cull order and the replay hook give boundary states priority and lookup by block root+slot, so the effect matches. Earlier evidence was right on mechanism; the 'dedicated cache' form differs.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#6460](https://github.com/OffchainLabs/prysm/pull/6460), [prysm#6486](https://github.com/OffchainLabs/prysm/pull/6486), [teku#7388](https://github.com/Consensys-Incorporated/teku/pull/7388), [teku#7359](https://github.com/Consensys-Incorporated/teku/pull/7359), [prysm#6464](https://github.com/OffchainLabs/prysm/pull/6464), [prysm#6488](https://github.com/OffchainLabs/prysm/pull/6488)

</details>


<a id="state_cache-100"></a>
<details>
<summary><b>state_cache-100</b> Shared per-epoch context object attached to blocks — <i>implemented · medium · M · cpu, memory, latency</i></summary>

**Idea.** Keep one shared epoch context per epoch (shuffling, proposers, validator key refs) referenced by blocks or cached states and used to prefill the state cache. Attestation and gossip validation look it up instead of rewinding a state, recomputing shuffling or allocating per block.

**Impact.** Gossip attestation validation reads Arc&lt;CommitteeCache&gt; from the shuffling cache primed at import; state loads only on a miss, rate-limited by promises.

**Best measured result.** "drastically speed up processing in times of long non-finality, cut memory usage by 10x" (pr:nimbus#1527)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/shuffling_cache.rs:21`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L21) ShufflingCache keyed by AttestationShufflingId with promise dedup
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5198`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5198) import_block_update_shuffling_cache primes committee caches at import
- [`beacon_node/beacon_chain/src/beacon_proposer_cache.rs:85`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_proposer_cache.rs#L85) BeaconProposerCache
- [`consensus/types/src/state/epoch_cache.rs:22`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/epoch_cache.rs#L22) Arc-shared EpochCache

**Skeptic check.** Verified committee/proposer data is shared per (epoch, decision root) and primed during block import, and validator pubkeys come from the global pubkey cache. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#1527](https://github.com/status-im/nimbus-eth2/pull/1527), [lodestar#1084](https://github.com/ChainSafe/lodestar/pull/1084), [nimbus#1449](https://github.com/status-im/nimbus-eth2/pull/1449), [nimbus@46c94a18b](https://github.com/status-im/nimbus-eth2/commit/46c94a18ba50)

</details>


<a id="state_cache-101"></a>
<details>
<summary><b>state_cache-101</b> Prune state cache often during sync and replay — <i>implemented · medium · S · memory, startup</i></summary>

**Idea.** Run state cache pruning on every epoch change and several times per epoch while syncing or replaying blocks at startup, not only when synced or finalized. Memory stays bounded during long replays and non-finality.

**Impact.** The cache is bounded by count on every insert regardless of sync state or finality, so long replays and non-finality cannot grow it past the cap.

**Best measured result.** heap stable 1.5-2.5GB on main thread; 4-7 states retained (pr:lodestar#7241)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/state_cache.rs:252`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L252) put_state culls when len &gt;= capacity, on every insert
- [`beacon_node/store/src/state_cache.rs:357`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L357) cull
- [`beacon_node/store/src/config.rs:23`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/config.rs#L23) DEFAULT_STATE_CACHE_SIZE = 128
- [`beacon_node/store/src/hot_cold_store.rs:2045`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2045) replay only caches epoch-boundary states

**Skeptic check.** Verified pruning is capacity-driven on each put, not tied to finalization or sync status, and replay inserts only boundary states. Earlier evidence was right; the trigger differs (on insert, not per epoch) but the memory bound is the same.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [grandine@64428a70f](https://github.com/grandinetech/grandine/commit/64428a70f37d), [grandine@c8febe6c5](https://github.com/grandinetech/grandine/commit/c8febe6c5253), [lodestar#7241](https://github.com/ChainSafe/lodestar/pull/7241), [lodestar#1494](https://github.com/ChainSafe/lodestar/pull/1494)

</details>


<a id="state_cache-102"></a>
<details>
<summary><b>state_cache-102</b> Keep secondary epoch index in sync on eviction — <i>implemented · low · S · memory</i></summary>

**Idea.** When a state is evicted from the hot state cache, by delete or size prune, also remove it from any secondary (per-epoch) index. Otherwise the index grows without bound with dead keys.

**Impact.** The block/slot index stays in sync on every normal eviction path; dead keys are bounded by finalization pruning.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/state_cache.rs:336-339`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L336-L339) delete_state removes from states and block_map
- [`beacon_node/store/src/state_cache.rs:341-347`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L341-L347) delete_block_states removes both
- [`beacon_node/store/src/state_cache.rs:252-259`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L252-L259) cull makes room before insert
- [`beacon_node/store/src/state_cache.rs:149-177`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L149-L177) finalization prunes block_map and states together
- ~/.cargo/registry/src/*/hashlink-0.11.1/src/lru_cache.rs:108-114 insert silently remove_lru when over capacity

**Skeptic check.** Upheld for the default capacity (128, headroom 1): cull always frees a slot before insert. One edge case: hashlink insert evicts silently and returns only the replaced value, so the deleted-state push at state_cache.rs:262 never fires. With --state-cache-size 1-2, cull can free nothing and leave dead block_map keys until finalization.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar@e51fa9ec5](https://github.com/ChainSafe/lodestar/commit/e51fa9ec5e0b)

</details>


<a id="state_cache-103"></a>
<details>
<summary><b>state_cache-103</b> Drop finalized and older states on finalization — <i>implemented · medium · S · memory</i></summary>

**Idea.** On each finalization, remove all states (and non-canonical blocks) at or before the finalized epoch from in-memory caches and stores, instead of relying only on a size cap. Old finalized states share little structure with the head and pin unique memory.

**Impact.** Finalization already removes pre-finalized states from the hot state cache and abandoned forks from the hot DB.

**Best measured result.** Memory regression fix; first LRU eviction took almost 5h without it (graph only) (pr:prysm#16458)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/state_cache.rs:127`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L127) update_finalized_state
- [`beacon_node/store/src/state_cache.rs:421`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L421) BlockMap::prune drops every state with slot &lt; finalized_slot
- [`beacon_node/store/src/hot_cold_store.rs:3665`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3665) called at the end of every freezer migration
- [`beacon_node/beacon_chain/src/migrate.rs:509`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L509) prune_hot_db deletes abandoned-fork states and blocks

**Skeptic check.** Confirmed that update_finalized_state prunes the block map by finalized slot and removes those states from the LRU on each migration. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#16458](https://github.com/OffchainLabs/prysm/pull/16458), [lodestar#2053](https://github.com/ChainSafe/lodestar/pull/2053), [teku#1225](https://github.com/Consensys-Incorporated/teku/pull/1225), [teku#2006](https://github.com/Consensys-Incorporated/teku/pull/2006), [lodestar@dffde1287](https://github.com/ChainSafe/lodestar/commit/dffde1287b4a), [teku#764](https://github.com/Consensys-Incorporated/teku/pull/764)

</details>


<a id="state_cache-104"></a>
<details>
<summary><b>state_cache-104</b> Keep one epoch of states for far non-canonical forks — <i>partial · medium · S · memory</i></summary>

**Idea.** For non-canonical chains far ahead of finality, keep only about one epoch of beacon states in memory. Cache growth stays bounded during long non-finality with many forks.

**Gap in Lighthouse.** Cache growth is bounded by a count cap and cull priority, but there is no per-fork policy that keeps only about one epoch for far non-canonical forks. Needs fork-distance logic in StateCache::cull using block_map and the head root.

**Impact.** Marginal: memory is already capped; it changes only which states survive in long non-finality with many forks.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/state_cache.rs:356`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L356) cull: LRU with advanced &gt; old boundary &gt; mid-epoch &gt; could-finalize order, no fork awareness
- [`beacon_node/store/src/state_cache.rs:375`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L375) only head_block_root is exempt; no canonical/fork distinction
- [`beacon_node/store/src/state_cache.rs:420`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L420) BlockMap::prune drops only pre-finalized-slot states
- [`beacon_node/store/src/config.rs:23`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/config.rs#L23) count cap 128

**Second check.** Re-read cull and BlockMap::prune: the only fork-related input is head_block_root (exempt from mid-epoch culling); no ancestry or distance check exists anywhere in state_cache.rs.

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [grandine#201](https://github.com/grandinetech/grandine/pull/201), [grandine@fc5638e3c](https://github.com/grandinetech/grandine/commit/fc5638e3cfe8)

</details>


<a id="state_cache-105"></a>
<details>
<summary><b>state_cache-105</b> Prune state cache relative to head slot — <i>implemented · low · S · memory</i></summary>

**Idea.** Compute the state-cache prune cutoff from the head slot rather than another reference point, so stale states are evicted and memory stays bounded.

**Impact.** Memory is bounded by a hard count plus finalization pruning; the cull already ranks age relative to the newest epoch.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/state_cache.rs:127-181`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L127-L181) update_finalized_state prunes states below the finalized slot
- [`beacon_node/store/src/state_cache.rs:250`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L250) max_epoch tracks the newest inserted state's epoch (head-relative)
- [`beacon_node/store/src/state_cache.rs:357-412`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L357-L412) cull prioritises states more than 4 epochs behind max_epoch and protects the head
- [`beacon_node/store/src/config.rs:23`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/config.rs#L23) DEFAULT_STATE_CACHE_SIZE 128 hard bound

**Skeptic check.** LH does not use grandine's head-slot cutoff. It bounds the cache by count and ranks cull candidates against max_epoch, which tracks the head. Stale states cannot pile up, so the earlier verdict holds in effect.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [grandine#146](https://github.com/grandinetech/grandine/pull/146)

</details>


<a id="state_cache-106"></a>
<details>
<summary><b>state_cache-106</b> Cache finalized states keyed by slot for API — <i>implemented · medium · S · cpu, latency, disk</i></summary>

**Idea.** Keep a cache of finalized states keyed by slot for beacon API queries. Repeated requests for the same finalized slot are served from memory instead of reloading and replaying from the freezer.

**Impact.** Mechanism present. Default capacity is 1, so repeated API queries over many slots need --historic-state-cache-size.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/historic_state_cache.rs:15`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/historic_state_cache.rs#L15) HistoricStateCache keyed by Slot
- [`beacon_node/store/src/hot_cold_store.rs:2306`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2306) load_cold_state_by_slot checks the cache (exact hit or prior slot plus replay)
- [`beacon_node/store/src/hot_cold_store.rs:2403`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2403) put_state after load
- [`beacon_node/store/src/config.rs:26`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/config.rs#L26) DEFAULT_HISTORIC_STATE_CACHE_SIZE = 1

**Second check.** The mechanism is exactly a slot-keyed cache of finalized (freezer) states on the API load path, with a CLI flag to size it and a 16-entry hdiff buffer cache behind it. A small default is a tuning choice, not a missing mechanism.

**Skeptic check.** Confirmed a slot-keyed cache of freezer states on the load_cold_state path that the API uses. The only difference is a small default size, which is a tuning choice.

**Verdict history.** partial (checked) → implemented (refuted) → implemented (skeptic)

**Sources.** [grandine@f208e64dc](https://github.com/grandinetech/grandine/commit/f208e64dc866), [grandine#234](https://github.com/grandinetech/grandine/pull/234)

</details>


<a id="state_cache-107"></a>
<details>
<summary><b>state_cache-107</b> Preload finalized epoch states into API cache — <i>not · medium · S · latency</i></summary>

**Idea.** When archiving finalized blocks, preload the states of the first and last block of the previous epoch into the state-by-slot cache. Common API queries then hit the cache instead of regenerating states.

**Gap in Lighthouse.** After migrate_database, put the epoch-boundary states of the just-archived epoch into HistoricStateCache::put_state (this needs capacity above 1).

**Impact.** Small: the first API query for a just-archived state avoids a freezer reconstruction. Matters only for state-API nodes.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:3603`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3603) migrate_database stores cold states ('There is no reason to cache this state') and never touches historic_state_cache
- [`beacon_node/store/src/hot_cold_store.rs:2103`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2103) store_cold_state writes the DB only and does no cache population
- [`beacon_node/store/src/state_cache.rs:127`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L127) update_finalized_state keeps only the new finalized checkpoint state hot

**Second check.** Checked migrate_database and store_cold_state for any cache warming: there is none. The only near-equivalent is that the finalized checkpoint state stays in the hot StateCache, so 'finalized' state_id queries already hit memory.

**Verdict history.** not (checked) → not (refuted)

**Sources.** [grandine#593](https://github.com/grandinetech/grandine/pull/593), [grandine@8edb1815c](https://github.com/grandinetech/grandine/commit/8edb1815cc21)

</details>


<a id="state_cache-108"></a>
<details>
<summary><b>state_cache-108</b> Pubkey-to-index hashmap cache — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Keep a pubkey-to-validator-index hashmap (filled from the state or finalized state) so deposit processing and API index lookups are O(1) instead of scanning the validator registry.

**Impact.** O(1) pubkey-&gt;index lookups in deposit processing and API already.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:1105`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L1105) get_validator_index -&gt; update_pubkey_cache + pubkey_cache().get
- [`consensus/types/src/state/beacon_state.rs:2979`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2979) update_pubkey_cache incremental from pubkey_cache.len()
- [`consensus/state_processing/src/per_block_processing/process_operations.rs:76`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/process_operations.rs#L76),805 deposits/requests use pubkey_cache
- [`beacon_node/http_api/src/validator_inclusion.rs:78`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/validator_inclusion.rs#L78) API uses state.get_validator_index
- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:24`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L24) chain-level pubkey-&gt;index HashMap

**Skeptic check.** Verified BeaconState carries an incrementally-updated PubkeyCache HashMap used by deposit and deposit-request processing and API lookups; earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#14146](https://github.com/OffchainLabs/prysm/pull/14146), [lighthouse@6cd3c4bd1](https://github.com/sigp/lighthouse/commit/6cd3c4bd1a65)

</details>


<a id="state_cache-109"></a>
<details>
<summary><b>state_cache-109</b> Pubkey index cache only for finalized validators — <i>n/a · low · S · cpu</i></summary>

**Idea.** Cache pubkey-to-index mappings only for finalized validators, whose indices cannot change (EIP-6110), and scan non-finalized ones uncached. The cache stays correct across forks without per-fork copies.

**Impact.** Lighthouse has a single process-wide append-only cache, not per-fork copies, so the Teku fork-copy problem does not exist; finalized-only would only save memory.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:28`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L28) append-only Vec+HashMap of all validators
- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:81`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L81) import_new_pubkeys only appends new indices

**Sources.** [teku#8165](https://github.com/Consensys-Incorporated/teku/pull/8165)

</details>


<a id="state_cache-110"></a>
<details>
<summary><b>state_cache-110</b> Persist decompressed pubkey cache across restarts — <i>implemented · low · S · startup</i></summary>

**Idea.** Write the decompressed validator pubkey cache to a flat file on clean shutdown and load it at boot with a spot-check against the anchor state. This avoids decompressing every validator pubkey at startup.

**Impact.** Startup does not decompress pubkeys. A one-blob layout instead of about 2M per-index DB reads could save a small amount of I/O time.

**Best measured result.** ~7.8s saved per restart on mainnet (9.4s to 1.6s for the cache step; 42.7s to 34.7s to metrics server); load 53-56ms for 2.37M entries (pr:lodestar#10152)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:55`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L55) load_from_store
- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:230`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L230) DatabasePubkey::from_pubkey stores serialize_uncompressed
- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:236`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L236) as_pubkey uses deserialize_uncompressed
- [`crypto/bls/src/impls/blst.rs:141`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/src/impls/blst.rs#L141) deserialize_uncompressed

**Second check.** Traced the load path down to blst: the persisted keys are uncompressed affine points and deserialize does only an on-curve parse (no sqrt, no subgroup check), so this is the same mechanism Lodestar added. compress() of an affine point is plain serialization.

**Skeptic check.** Confirmed that the pubkey cache is persisted as uncompressed affine points and loaded without sqrt decompression; compress() at load is only serialization. The earlier evidence was correct.

**Verdict history.** partial (checked) → implemented (refuted) → implemented (skeptic)

**Sources.** [lodestar#10152](https://github.com/ChainSafe/lodestar/pull/10152)

</details>


<a id="state_cache-111"></a>
<details>
<summary><b>state_cache-111</b> Warm pubkey cache at genesis start — <i>implemented · low · S · startup</i></summary>

**Idea.** Populate the validator pubkey cache when starting from genesis instead of returning early, so the first lookups do not miss.

**Impact.** Cache is full from the genesis state at startup; no early-return miss.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/builder.rs:854-877`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/builder.rs#L854-L877) validator_pubkey_cache built via ValidatorPubkeyCache::new(&amp;head_snapshot.beacon_state) when none was loaded (genesis start)
- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:37-50`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L37-L50) new() imports all validators from the state

**Skeptic check.** Confirmed the builder falls back to ValidatorPubkeyCache::new over the head (genesis) state, importing every key; earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#14995](https://github.com/OffchainLabs/prysm/pull/14995)

</details>


<a id="state_cache-112"></a>
<details>
<summary><b>state_cache-112</b> Preallocate pubkey cache capacity — <i>partial · low · S · startup, memory</i></summary>

**Idea.** Reserve the pubkey cache arrays to their final size (plus registry growth headroom) when building it, reuse the loaded validators array, and skip writes of identical pubkeys. This avoids repeated reallocation and needless mutation of the shared cache.

**Gap in Lighthouse.** load_from_store could size pubkeys/indices/pubkey_bytes from a known validator count (or state validators len) and reserve small growth headroom; import already reserves exactly the delta.

**Impact.** Slightly less realloc/rehash at startup (~1M validators HashMap rehashes); minor and one-off.

**Best measured result.** ~31MB virtual, ~0 resident reservation (pr:lodestar#9640)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:111`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L111) reserve(len) in import for new keys
- validator_pubkey_cache.rs:55 load_from_store pushes in loop with no pre-sizing; new() starts with vec![]

**Sources.** [lodestar#7010](https://github.com/ChainSafe/lodestar/pull/7010), [lodestar#9640](https://github.com/ChainSafe/lodestar/pull/9640)

</details>


<a id="state_cache-113"></a>
<details>
<summary><b>state_cache-113</b> Serve pubkeys from in-memory head state — <i>implemented · low · S · disk, cpu, memory</i></summary>

**Idea.** Answer validator pubkey lookups from the in-memory head state instead of a separate DB table with its own sync routines.

**Impact.** Lookups served from memory; DB is only a persistence layer.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:24-29`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L24-L29) in-memory pubkeys/indices/pubkey_bytes
- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:56-80`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L56-L80) DB read only in load_from_store at startup
- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:89`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L89) import_new_pubkeys topped up from imported states

**Skeptic check.** Lighthouse keeps a dedicated in-memory cache (not the head state itself) with DB persistence only written at import and read at startup, so the effect of avoiding DB lookups is the same; earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [caplin#13030](https://github.com/erigontech/erigon/pull/13030)

</details>


<a id="state_cache-114"></a>
<details>
<summary><b>state_cache-114</b> Reader-writer locks for state reads — <i>n/a · low · S · cpu, latency</i></summary>

**Idea.** Guard the beacon state and its field tries with finer-grained reader-writer locks, and take only the read lock in read-only accessors, so concurrent readers do not serialize.

**Impact.** BeaconState is an owned persistent tree (milhouse, Arc nodes); readers clone cheaply and there are no state or field-trie locks to split.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:503`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L503) states are plain milhouse values; no state-level lock

**Sources.** [prysm#4733](https://github.com/OffchainLabs/prysm/pull/4733), [prysm#8588](https://github.com/OffchainLabs/prysm/pull/8588)

</details>


<a id="state_cache-115"></a>
<details>
<summary><b>state_cache-115</b> Read lock on shuffling cache hits — <i>implemented · medium · S · cpu, latency</i></summary>

**Idea.** Serve shuffling cache hits under a read lock and take the write lock only on a miss, since nearly all lookups are hits.

**Impact.** Attestation/payload-attestation/IL gossip hits take only the read lock.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/shuffling_cache.rs:347-354`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L347-L354) with_cached_shuffling reads under shuffling_cache_lock.read().get_shuffling_if_cached
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:196`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L196) get_shuffling_if_cached(&amp;self)
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:356-377`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L356-L377) write lock only for promise/miss
- [`beacon_node/beacon_chain/src/beacon_chain.rs:7602`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L7602) attestation committee path uses with_cached_shuffling

**Skeptic check.** Confirmed all with_cached_shuffling callers (attestations, payload attestations, inclusion lists, execution proofs) hit the read-lock fast path; earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#9615](https://github.com/sigp/lighthouse/pull/9615)

</details>


<a id="state_cache-116"></a>
<details>
<summary><b>state_cache-116</b> Never evict possibly-finalizable epoch-boundary states — <i>implemented · medium · S · memory, cpu, disk</i></summary>

**Idea.** In state cache eviction, protect epoch-boundary states that could become finalized (checked before other conditions like is_advanced, and robust to skipped slots). Finalization migration then does not rebuild them and keeps structural sharing with recent states.

**Impact.** This is Lighthouse's own PRs 4762/4833. They are present.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/state_cache.rs:18`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L18) EPOCH_FINALIZATION_LIMIT = 4
- [`beacon_node/store/src/state_cache.rs:376`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L376) cull classifies is_boundary before is_advanced; could-finalize boundary states are culled last

**Skeptic check.** In cull, is_boundary uses state.slot() so advanced skipped-slot boundary states count as boundary, and good boundary states are culled last. This matches the idea.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#4762](https://github.com/sigp/lighthouse/pull/4762), [lighthouse#4833](https://github.com/sigp/lighthouse/pull/4833)

</details>


<a id="state_cache-117"></a>
<details>
<summary><b>state_cache-117</b> Fork-aware state cache eviction by chain — <i>not · medium · L · memory</i></summary>

**Idea.** Track ancestry in the state cache, evict the least recently accessed chain first, and cap states per chain. Many forks cannot push useful head-chain states out.

**Gap in Lighthouse.** Add ancestry tracking (parent links) to StateCache, evict the least recently accessed chain first and cap states per chain in cull()/put_state().

**Impact.** Under long non-finality or many forks, fork states could push head-chain states out and cause reloads/replays; small on a healthy mainnet node.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/state_cache.rs:27-36`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L27-L36) BlockMap is block_root-&gt;slot-&gt;state_root only, no parent/chain links
- [`beacon_node/store/src/state_cache.rs:357-412`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L357-L412) cull() is LRU with state-kind buckets (advanced, old boundary, mid-epoch, good boundary), no per-chain grouping or cap
- [`beacon_node/store/src/state_cache.rs:228-285`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L228-L285) put_state() has no per-chain limit
- [`beacon_node/store/src/hot_cold_store.rs:1586`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1586) only fork pruning on finalization deletes abandoned-fork states (delete_block_states), not eviction priority

**Second check.** Checked all state_cache.lock() callers in store and beacon_chain, and the finalization fork pruning path; nothing groups or limits cached states by chain.

**Verdict history.** not (checked) → not (refuted)

**Sources.** [lighthouse#7069](https://github.com/sigp/lighthouse/pull/7069)

</details>


<a id="state_cache-118"></a>
<details>
<summary><b>state_cache-118</b> Preserve fork-choice tip states when pruning — <i>not · medium · S · cpu, memory</i></summary>

**Idea.** When pruning the state cache, keep the states of all unfinalized fork-choice tips so they are not evicted and later recomputed or reloaded.

**Gap in Lighthouse.** Pass all fork-choice leaf block roots (proto-array heads) to StateCache and skip their states in cull().

**Impact.** Avoids reloading/replaying states for competing tips during fork-heavy periods; negligible with one tip.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/state_cache.rs:184-189`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L184-L189) update_head_block_root stores a single head root
- [`beacon_node/store/src/state_cache.rs:392-395`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L392-L395) cull() exempts only the unadvanced head-block state
- [`beacon_node/beacon_chain/src/canonical_head.rs:1515`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1515) the only caller passes only the canonical head

**Second check.** Grepped store, canonical_head and migrate for any heads/tips/leaves set fed to the cache; only the single head root reaches it.

**Verdict history.** not (checked) → not (refuted)

**Sources.** [grandine@c2470af9a](https://github.com/grandinetech/grandine/commit/c2470af9a163)

</details>


<a id="state_cache-119"></a>
<details>
<summary><b>state_cache-119</b> Head state never evicted; cap regen replay — <i>partial · medium · S · cpu, memory</i></summary>

**Idea.** Hold the fork-choice head state through a strong reference that cache eviction cannot drop, and fail fast when regenerating a state would replay too many blocks.

**Gap in Lighthouse.** Head-state strong reference is done. Missing: an explicit fail-fast cap on replayed blocks/slots in load_blocks_to_replay/replay_blocks (replay is bounded only by the hierarchy layout config, and slot advancing for stale-fork attestations is uncapped unless import_max_skip_slots is set).

**Impact.** Head-state half already present; the cap only guards pathological configs or long skip-slot advances, so the remaining gain is small.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/canonical_head.rs:284`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L284) CachedHead holds snapshot: Arc&lt;BeaconSnapshot&gt; with the head BeaconState, a strong reference outside the evictable StateCache
- [`beacon_node/store/src/state_cache.rs:392-395`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L392-L395) cull() never evicts the unadvanced head state
- [`beacon_node/store/src/hdiff.rs:622`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs#L622) and [`beacon_node/store/src/config.rs:254`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/config.rs#L254) default hierarchy smallest exponent 5: hot ReplayFrom is at most 31 slots of blocks by layout
- [`beacon_node/store/src/hot_cold_store.rs:1992-2014`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1992-L2014) load_hot_state ReplayFrom from the nearest diff layer
- [`beacon_node/store/src/hot_cold_store.rs:2031-2040`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2031-L2040) load_hot_state_using_replay / 2514 load_blocks_to_replay have no explicit block-count check or fail-fast error
- [`beacon_node/beacon_chain/src/chain_config.rs:151`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/chain_config.rs#L151) import_max_skip_slots defaults to None (attestation skip cap is opt-in)

**Second check.** Confirmed that the hdiff hierarchy bounds hot replay to under 32 blocks by default (not a runtime check), and checked import_max_skip_slots and MAX_ADVANCE_DISTANCE as alternative caps; neither is a regen replay fail-fast.

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [lodestar#4944](https://github.com/ChainSafe/lodestar/pull/4944), [lodestar#1703](https://github.com/ChainSafe/lodestar/pull/1703)

</details>


<a id="state_cache-120"></a>
<details>
<summary><b>state_cache-120</b> Finalized state root fast path — <i>implemented · low · S · latency, disk</i></summary>

**Idea.** In state-root-at-slot lookups, return the cached finalized/split state root directly for the finalized slot instead of walking back through state loads.

**Impact.** This is Lighthouse PR 8353. It is present.

**Best measured result.** prepare_beacon_proposer took 5-10s in non-finality; no after numbers (pr:lighthouse#8353)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:977`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L977) state_root_at_slot returns split.state_root when request_slot == split.slot

**Skeptic check.** Confirmed that the split-slot fast path in state_root_at_slot runs before the head lookup and the forwards iterator.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#8353](https://github.com/sigp/lighthouse/pull/8353)

</details>


<a id="state_cache-121"></a>
<details>
<summary><b>state_cache-121</b> Genesis state shortcut for zero root — <i>implemented · low · S · latency</i></summary>

**Idea.** Short-circuit state lookups for the zero block root by returning the stored genesis state directly.

**Impact.** Zero root resolves to genesis block/state via alias; rare path.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/builder.rs:331-339`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/builder.rs#L331-L339) genesis block stored under Hash256::zero() alias

**Skeptic check.** Lighthouse aliases the zero root to the genesis block, so zero-root lookups resolve to genesis rather than failing or replaying; not a dedicated state shortcut but Lighthouse rarely issues zero-root state lookups, so the effect is equivalent.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#5223](https://github.com/OffchainLabs/prysm/pull/5223)

</details>


<a id="state_cache-122"></a>
<details>
<summary><b>state_cache-122</b> Evict shuffling cache by smallest epoch — <i>implemented · low · S · latency</i></summary>

**Idea.** Prune the shuffling cache by smallest epoch instead of insertion order, and do not fill it during block verification, so shufflings needed for attestation packing stay cached.

**Impact.** Eviction already by smallest epoch with head shufflings pinned.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/shuffling_cache.rs:250-279`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L250-L279) prune_cache sorted_by_key(shuffling_epoch) excluding head_shuffling_ids
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5211-5232`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5211-L5232) fill at import skips if already contained

**Skeptic check.** Verified prune_cache evicts the oldest epochs first and never prunes the head's shuffling ids, which protects the shufflings needed for packing; earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#10294](https://github.com/ChainSafe/lodestar/pull/10294)

</details>


<a id="state_cache-123"></a>
<details>
<summary><b>state_cache-123</b> Load shuffling cache for correct epochs — <i>implemented · low · S · cpu</i></summary>

**Idea.** When filling the shuffling cache during state advance, load it for the state's current epoch and every slot/block jump, and look up both distinct epochs, so hits replace recomputation.

**Impact.** Both epochs primed at import and state advance; misses compute and insert.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:5211-5232`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5211-L5232) import primes Current and Next epoch shufflings
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:398-412`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L398-L412) state advance inserts Next epoch shuffling
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:335-345`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L335-L345) lookups keyed by id_for_epoch from fork-choice block

**Skeptic check.** Confirmed import primes both current and next shufflings, and state advance primes next; lookups use the correct per-epoch shuffling id; earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#2631](https://github.com/status-im/nimbus-eth2/pull/2631)

</details>


<a id="state_cache-124"></a>
<details>
<summary><b>state_cache-124</b> Global shuffling cache keyed by epoch and decision root — <i>implemented · medium · S · cpu, disk, latency, memory</i></summary>

**Idea.** Cache shufflings in one shared cache keyed by (epoch, shuffling decision root) and use it for committee assignments and every attestation, so attestations on forks or across epoch boundaries hit the cache instead of memoizing per state or forcing state reads and recomputation.

**Impact.** One shared cache keyed by (epoch, decision root) serves gossip attestations and duties.

**Best measured result.** OOM kill each startup before (screenshot) (pr:lodestar#9569)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/attestation/shuffling_id.rs:23`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/attestation/shuffling_id.rs#L23) AttestationShufflingId {shuffling_epoch, shuffling_decision_block}
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:315`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L315) with_cached_shuffling with promise dedup
- [`beacon_node/beacon_chain/src/beacon_chain.rs:7593`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L7593) with_committee_cache
- [`beacon_node/beacon_chain/src/attestation_verification.rs:1645`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/attestation_verification.rs#L1645) gossip attestations use with_committee_cache
- [`beacon_node/beacon_chain/src/beacon_chain.rs:1747`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1747) attester duties use with_committee_cache

**Skeptic check.** Confirmed that the attestation verification and duty paths both go through the global ShufflingCache. Fork or cross-epoch attestations hit it by shuffling ID and do not memoize per state.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#1492](https://github.com/sigp/lighthouse/pull/1492), [nimbus#2463](https://github.com/status-im/nimbus-eth2/pull/2463), [nimbus#2614](https://github.com/status-im/nimbus-eth2/pull/2614), [lodestar#9569](https://github.com/ChainSafe/lodestar/pull/9569)

</details>


<a id="state_cache-125"></a>
<details>
<summary><b>state_cache-125</b> Precompute next-epoch caches in the state-advance task — <i>implemented · medium · S · cpu, latency</i></summary>

**Idea.** Before an epoch boundary (last slot, even when skipped), build the next epoch's committee, shuffling and proposer caches, ideally in the same background task that pre-advances the head state, so the epoch transition is computed once and the first block and duties of the new epoch do not miss.

**Impact.** The epoch transition is done once in the advance task, and the proposer and attester caches are warm for slot 0.

**Best measured result.** Avoids extra 500ms-1s latency on slot 0 proposal (pr:prysm#12651)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/state_advance_timer.rs:290`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L290) per_slot_processing on the head state in the background timer
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:333`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L333) builds Current and Next committee caches
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:347`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L347) primes the proposer cache for the current and next epoch on epoch crossing
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:409`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L409) inserts the next-epoch shuffling into shuffling_cache
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:38`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L38) MAX_ADVANCE_DISTANCE = 256 covers skipped slots

**Skeptic check.** Confirmed that the advance runs every slot, also when slots are skipped (up to 256 slots behind). On an epoch crossing it primes the proposer and shuffling caches from the same advanced state.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#12667](https://github.com/OffchainLabs/prysm/pull/12667), [lighthouse@c82bad760](https://github.com/sigp/lighthouse/commit/c82bad7602ba), [prysm#12651](https://github.com/OffchainLabs/prysm/pull/12651), [prysm#12661](https://github.com/OffchainLabs/prysm/pull/12661), [caplin#12227](https://github.com/erigontech/erigon/pull/12227), [prysm#12679](https://github.com/OffchainLabs/prysm/pull/12679), [prysm#12500](https://github.com/OffchainLabs/prysm/pull/12500), [prysm#12678](https://github.com/OffchainLabs/prysm/pull/12678), [prysm#13383](https://github.com/OffchainLabs/prysm/pull/13383), [prysm#12666](https://github.com/OffchainLabs/prysm/pull/12666)

</details>


<a id="state_cache-126"></a>
<details>
<summary><b>state_cache-126</b> Preheat n+1 shuffling at end of n-1 — <i>implemented · medium · S · latency, cpu</i></summary>

**Idea.** Compute the shuffling for epoch n+1 at the last slot of epoch n-1, when its dependent root is known, so validator duty requests at the start of epoch n hit a warm cache.

**Impact.** The n+1 attester shuffling is cached during the last slot of n-1, before duty requests at the start of epoch n.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/state_advance_timer.rs:398`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L398) AttestationShufflingId::new(head_block_root, &amp;state, RelativeEpoch::Next) after advancing into epoch n
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:409`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L409) insert_committee_cache

**Skeptic check.** Confirmed that the advance at the end of epoch n-1 moves the head into n and inserts the RelativeEpoch::Next (n+1) shuffling under its decision root. Only the Gloas fork-boundary epoch skips this.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#8835](https://github.com/status-im/nimbus-eth2/pull/8835)

</details>


<a id="state_cache-127"></a>
<details>
<summary><b>state_cache-127</b> Seed sync committee cache from known committee — <i>implemented · low · S · cpu, sync</i></summary>

**Idea.** When applying blocks, seed the sync committee index cache with the known committee and cache total active balance per epoch, avoiding full validator traversals per block during sync.

**Impact.** Per-block sync aggregate processing does no validator traversal and no per-block total balance sum.

**Best measured result.** 20-30% sync speedup post-altair, plus ~10% from cached total active balances (pr:nimbus#4592)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:1753`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L1753) get_sync_committee_indices: incremental update_pubkey_cache then 512 pubkey-cache lookups, no validator scan
- [`consensus/state_processing/src/per_block_processing/altair/sync_committee.rs:50`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/altair/sync_committee.rs#L50) process_sync_aggregate uses it
- [`consensus/state_processing/src/per_block_processing/altair/sync_committee.rs:91`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/altair/sync_committee.rs#L91) compute_sync_aggregate_rewards reads cached get_total_active_balance
- [`consensus/types/src/state/beacon_state.rs:2682`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2682) get_total_active_balance_at_epoch epoch-keyed cache
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:482`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L482) set_total_active_balance from epoch processing

**Skeptic check.** Confirmed both parts on the block import path: the sync committee indices come from the incremental pubkey cache and the total active balance is cached per epoch and filled by single-pass epoch processing. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#4592](https://github.com/status-im/nimbus-eth2/pull/4592)

</details>


<a id="state_cache-128"></a>
<details>
<summary><b>state_cache-128</b> Free per-state auxiliary maps on drop — <i>n/a · low · S · memory</i></summary>

**Idea.** Free per-state auxiliary structures (leaf caches, dirty-index maps, shared refs) when a state is dropped, use compact bool sets for dirty fields, and export a gauge of live state objects to find leaks.

**Impact.** None; no finalizer-style cleanup needed.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:825`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L825) caches are Arc/owned, freed by Drop

**Sources.** [prysm#8742](https://github.com/OffchainLabs/prysm/pull/8742)

</details>


<a id="state_cache-129"></a>
<details>
<summary><b>state_cache-129</b> Move field tries into the copy, not clone — <i>n/a · low · S · memory, cpu</i></summary>

**Idea.** When copying a state whose source will be discarded, move its cached Merkle field tries to the new state instead of deep-copying them; the old state rebuilds lazily if needed.

**Impact.** None.

**Best measured result.** general memory usage of the beacon node has dropped 30% (pr:prysm#10884)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:77`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L77) validators/balances are milhouse Lists
- beacon_state.rs:825 Arc&lt;CommitteeCache&gt;

**Sources.** [prysm#5221](https://github.com/OffchainLabs/prysm/pull/5221), [prysm#10884](https://github.com/OffchainLabs/prysm/pull/10884)

</details>


<a id="state_cache-130"></a>
<details>
<summary><b>state_cache-130</b> Move snapshots out of cache instead of cloning — <i>n/a · medium · cpu, memory, sync</i></summary>

**Idea.** Make the block-processing snapshot/state cache move the pre-state out rather than clone it when it will not be reused (head import, sync block import), reducing clones and memory fragmentation.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_snapshot.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_snapshot.rs) only a type remains; snapshot cache removed
- [`beacon_node/store/src/state_cache.rs:275`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L275) get_by_state_root clones the state, which is O(1) via milhouse structural sharing

**Sources.** [lighthouse#863](https://github.com/sigp/lighthouse/pull/863), [lighthouse#3271](https://github.com/sigp/lighthouse/pull/3271)

</details>


<a id="state_cache-131"></a>
<details>
<summary><b>state_cache-131</b> Multi-value lists: shared base plus per-state diffs — <i>implemented · low · L · memory, cpu</i></summary>

**Idea.** Store large state lists (validators, balances, roots, randao mixes, inactivity scores) as one shared base array plus per-state diffs, so many cached state copies share memory and copies are cheap.

**Impact.** Persistent Merkle trees with structural sharing give cheap state clones and shared memory.

**Best measured result.** "better runtime improvement on memory usage by beacon states" (pr:prysm#14398)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:77-80`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L77-L80) Validators/Balances are milhouse List
- [`consensus/types/src/state/beacon_state.rs:516`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L516),563,627 block_roots/randao_mixes Vector, inactivity_scores List
- Cargo.lock:6570 milhouse 0.9.0

**Skeptic check.** Lighthouse uses milhouse persistent trees for all large state lists, which shares unchanged subtrees between states (a different mechanism from Prysm's base+diff with the same effect); earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#12312](https://github.com/OffchainLabs/prysm/pull/12312), [prysm#14398](https://github.com/OffchainLabs/prysm/pull/14398), [prysm#15292](https://github.com/OffchainLabs/prysm/pull/15292), [prysm#12616](https://github.com/OffchainLabs/prysm/pull/12616), [prysm#12549](https://github.com/OffchainLabs/prysm/pull/12549), [prysm#15414](https://github.com/OffchainLabs/prysm/pull/15414)

</details>


<a id="state_cache-132"></a>
<details>
<summary><b>state_cache-132</b> Persistent structurally shared tree-backed beacon states — <i>implemented · low · S · memory, cpu</i></summary>

**Idea.** Represent the beacon state in memory as persistent structurally shared trees (and diffs on disk), so clones share unchanged subtrees and cached hash roots and the state cache can hold many more states for similar memory.

**Impact.** Already the core design (tree-states).

**Best measured result.** holds 32x more states for around the same memory cost (pr:lighthouse#5533)

**Evidence (Lighthouse @ 928b61e719).**

- Cargo.lock:6570 milhouse 0.9.0
- [`consensus/types/src/state/beacon_state.rs:3416`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L3416) BeaconState::rebase_on over milhouse trees
- [`beacon_node/store/src/state_cache.rs:215`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L215) put_state stores state.clone() (structurally shared)
- [`beacon_node/store/src/hot_cold_store.rs:1771`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1771) store_hot_state_as_diff hierarchical diffs on disk

**Skeptic check.** Lighthouse's own tree-states work (#5533, #3206) is the origin of this idea. The milhouse-backed state and the hdiff storage are both present.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#5533](https://github.com/sigp/lighthouse/pull/5533), [lodestar@cf71a0110](https://github.com/ChainSafe/lodestar/commit/cf71a0110082), [lighthouse#3206](https://github.com/sigp/lighthouse/pull/3206)

</details>


<a id="state_cache-133"></a>
<details>
<summary><b>state_cache-133</b> Rebase updated lists onto old tree — <i>not · medium · M · memory</i></summary>

**Idea.** After bulk-updating a list such as inactivity_scores, rebase the new tree onto the old one to reuse identical subtrees, instead of duplicating the whole list in memory each update.

**Gap in Lighthouse.** #7062's List::intra_rebase call after the epoch-transition inactivity_scores update is not in unstable. During a leak or recovery every non-zero score is rewritten, so each post-epoch state carries a fresh ~80MB inactivity_scores tree. Re-add intra_rebase (or rebase_on against the pre-state list) after process_epoch_single_pass once the milhouse intra_rebase dedup bug is fixed.

**Impact.** During non-finality, about 70MB+ to about 4-5MB per inactivity_scores update per cached state (measured on Holesky in #7062); no effect when all scores are 0 (mainnet steady state), because zero scores already skip mutation.

**Best measured result.** ~70MB+ per update to ~4-5MB; rebase time 47ms (pr:lighthouse#7062)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:245`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L245) inactivity_scores.iter_cow(), no intra_rebase/rebase after the pass
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:646-650`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L646-L650) zero scores skip make_mut (avoids copies only in the all-zero common case, not the leak/recovery case #7062 targets)
- ~/.cargo/git/checkouts/milhouse-572e092edb163991/d67aabd/src/list.rs:356 List::intra_rebase exists; only caller is milhouse src/tests/proptest/operations.rs:389, with a FIXME bug note at :394
- [`beacon_node/store/src/state_cache.rs:197-208`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L197-L208) rebase_on_finalized and [`beacon_node/beacon_chain/src/beacon_chain.rs:7840`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L7840) rebase_on are whole-state rebases against another state for disk-loaded states, not after epoch updates

**Second check.** Searched for intra_rebase, rebase_on and .rebase( across the repo and milhouse d67aabd. The only related mechanisms are the zero-score make_mut skip and whole-state rebase_on for states loaded from disk. Neither dedups a list that was rewritten in bulk.

**Verdict history.** not (checked) → not (refuted)

**Sources.** [lighthouse#7062](https://github.com/sigp/lighthouse/pull/7062)

</details>


<a id="state_cache-134"></a>
<details>
<summary><b>state_cache-134</b> Load states onto an existing in-memory tree — <i>partial · low · M · memory, cpu, startup</i></summary>

**Idea.** When deserializing a state (diff application, checkpoint-sync anchor), build it onto an already loaded related state's tree, reusing unchanged subtrees and applying only modified entries, so loaded states share memory and are not re-hashed.

**Gap in Lighthouse.** Hot loads build a full transient tree and then rebase it onto the finalized state, so deserialisation and allocation stay full cost. Cold loads (load_cold_state_by_slot via HDiffBuffer::as_state, used by the historic API and reconstruction) are never rebased, so states loaded from different diff points share no memory and keep no hashes. Two hot states loaded a diff apart only share with the finalized state, not with each other (the caveat in #4416).

**Impact.** Hot path memory sharing works. The cold and historic path holds unshared trees, but the default historic_state_cache_size is 1, so the cost is small.

**Best measured result.** startup blocking of ~24s removed after download (pr:lodestar#7056)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hdiff.rs:210`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs#L210) HDiffBuffer::as_state builds a full fresh tree from SSZ plus the lists
- [`beacon_node/store/src/hot_cold_store.rs:1984-1988`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1984-L1988) hot snapshot/diff loads rebase_on_finalized after building
- [`beacon_node/store/src/hot_cold_store.rs:2009-2013`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2009-L2013) hot replay base rebased
- [`beacon_node/store/src/state_cache.rs:197-212`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L197-L212) rebase_on_finalized is a no-op for states before the finalized slot
- [`beacon_node/store/src/hot_cold_store.rs:2306-2356`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2306-L2356) load_cold_state_by_slot: as_state then put_both into the historic cache, with no rebase
- ~/.cargo/git/checkouts/milhouse-*/d67aabd/src/tree.rs:270 Tree::rebase_on compares leaf values and reuses cached hashes

**Skeptic check.** Confirmed rebase_on_finalized on both hot load paths, and that milhouse rebase reuses base subtrees and cached hashes. The earlier verdict ignored the cold-state path, which has no rebase, and it already noted the transient full build. The Lodestar startup case (DB state plus checkpoint state) does not apply, because Lighthouse does not checkpoint-sync onto an existing DB.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [lodestar#6057](https://github.com/ChainSafe/lodestar/pull/6057), [lighthouse#4416](https://github.com/sigp/lighthouse/pull/4416), [lodestar#7056](https://github.com/ChainSafe/lodestar/pull/7056)

</details>


<a id="state_cache-135"></a>
<details>
<summary><b>state_cache-135</b> Native struct state instead of protobuf wrapper — <i>n/a · low · S · memory, cpu</i></summary>

**Idea.** Use a native struct beacon state representation rather than a protobuf/serialization-backed one, to cut memory and copy overhead.

**Impact.** None.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:539`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L539) native superstruct BeaconState

**Sources.** [prysm#10898](https://github.com/OffchainLabs/prysm/pull/10898), [prysm#10880](https://github.com/OffchainLabs/prysm/pull/10880)

</details>


<a id="state_cache-136"></a>
<details>
<summary><b>state_cache-136</b> Pool and reuse large state field buffers — <i>n/a · low · memory, cpu</i></summary>

**Idea.** Pool released large per-state arrays (randao mixes, 2D byte slices, COW buffers) and reuse them when a state field must be copied, instead of allocating new ones.

**Impact.** Tree-backed states copy only modified leaves, so pooling large flat arrays does not apply.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs): fields are milhouse persistent Lists/Vectors, clone shares nodes; no large per-state arrays copied
- no buffer pool found in store/src/state_cache.rs

**Sources.** [prysm#4824](https://github.com/OffchainLabs/prysm/pull/4824), [prysm#4903](https://github.com/OffchainLabs/prysm/pull/4903), [prysm#4896](https://github.com/OffchainLabs/prysm/pull/4896), [prysm#4811](https://github.com/OffchainLabs/prysm/pull/4811)

</details>


<a id="state_cache-137"></a>
<details>
<summary><b>state_cache-137</b> Pool tree-hash leaves and compression writers — <i>n/a · low · S · memory, cpu</i></summary>

**Idea.** Separate the transient state cache from the tree, and pool validator hash leaves and snappy writers, removing a high-memory parallel hash.

**Impact.** None.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:77`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L77) milhouse caches tree-hash in nodes

**Sources.** [caplin#7433](https://github.com/erigontech/erigon/pull/7433)

</details>


<a id="state_cache-138"></a>
<details>
<summary><b>state_cache-138</b> No state copies on head save and init sync — <i>n/a · medium · memory, sync</i></summary>

**Idea.** Do not copy the state when saving it as the head, and during initial sync (linear chain) return cached states without cloning and skip the skip-slot cache.

**Impact.** Prysm's deep-copy cost does not exist in Lighthouse: cloning a milhouse-backed state is cheap and there is no skip-slot cache.

**Best measured result.** Memory reduction down from 3GB to 600MB (pr:prysm#5778)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs): BeaconState uses milhouse persistent trees, clone is Arc-shared
- [`beacon_node/store/src/state_cache.rs:236`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L236) put_state clones the state (cheap structural share); no skip-slot cache module in [`beacon_node/beacon_chain/src`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src)

**Sources.** [prysm#5760](https://github.com/OffchainLabs/prysm/pull/5760), [prysm#5778](https://github.com/OffchainLabs/prysm/pull/5778)

</details>


<a id="state_cache-139"></a>
<details>
<summary><b>state_cache-139</b> Read-only field accessors without state copy — <i>implemented · low · S · memory, cpu</i></summary>

**Idea.** Provide read-only accessors on the state for validators and balance sums, so callers needing a few fields do not deep-copy the validator list or whole state.

**Impact.** Borrowing accessors exist, and a milhouse clone is O(1) anyway.

**Best measured result.** many times faster and doesn't require making copies (pr:prysm#13782)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:2408`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2408) get_validator returns &amp;Validator
- [`consensus/types/src/state/beacon_state.rs:2677`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2677) get_total_active_balance cached read
- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs) validators().iter_from(n) borrows

**Skeptic check.** The accessors borrow from milhouse lists and the balance sums are cached. A state or list clone is a cheap structurally shared copy, so the deep-copy problem in Prysm does not exist here.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#16355](https://github.com/OffchainLabs/prysm/pull/16355), [prysm#13782](https://github.com/OffchainLabs/prysm/pull/13782)

</details>


<a id="state_cache-140"></a>
<details>
<summary><b>state_cache-140</b> Read-only epoch context handout — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Hand out a read-only reference to the epoch context instead of a copy, avoiding cloning big caches per call.

**Impact.** Epoch-level caches are behind Arc or persistent structures and accessors return references, so no per-call deep copy of an epoch context.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/epoch_cache.rs:22-24`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/epoch_cache.rs#L22-L24) EpochCache { inner: Option&lt;Arc&lt;Inner&gt;&gt; }
- [`consensus/types/src/state/beacon_state.rs:825`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L825) committee_caches: [Arc&lt;CommitteeCache&gt;; CACHED_EPOCHS]
- [`consensus/types/src/state/beacon_state.rs:837`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L837) pubkey_cache (persistent map)

**Skeptic check.** Confirmed EpochCache and committee caches are Arc-shared and handed out by reference. The earlier evidence was right; smaller caches (exit/slashings) clone with the state but that is not a per-call handout.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#1032](https://github.com/ChainSafe/lodestar/pull/1032)

</details>


<a id="state_cache-141"></a>
<details>
<summary><b>state_cache-141</b> In-place forked state assignment — <i>n/a · low · S · cpu, memory</i></summary>

**Idea.** When assigning a forked (multi-variant) state, switch variant and copy-assign fields in place without a temporary copy.

**Impact.** None.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:539`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L539) superstruct enum, Rust moves

**Sources.** [nimbus#6055](https://github.com/status-im/nimbus-eth2/pull/6055)

</details>


<a id="state_cache-142"></a>
<details>
<summary><b>state_cache-142</b> Grow reused buffers without full zeroing — <i>n/a · low · S · cpu, memory</i></summary>

**Idea.** When growing a reused validator-set buffer, zero only the newly added region instead of the whole new capacity before copying.

**Impact.** None.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/pubkey_cache.rs:9`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/pubkey_cache.rs#L9) persistent map, no reused zeroed validator buffer

**Sources.** [caplin#23795](https://github.com/erigontech/erigon/pull/23795)

</details>


<a id="state_cache-143"></a>
<details>
<summary><b>state_cache-143</b> Validator set as one flat buffer — <i>n/a · low · memory, cpu</i></summary>

**Idea.** Store the validator set as one flat buffer instead of per-validator objects, cutting allocation and GC pressure and making copies cheap.

**Impact.** Validators live in a structurally shared milhouse tree; a flat buffer would lose cheap COW clones and tree-hash caching. Does not apply.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs): validators is a milhouse List (persistent tree, packed leaves)
- Cargo.lock: milhouse 0.9.0 git d67aabd

**Sources.** [caplin#7591](https://github.com/erigontech/erigon/pull/7591)

</details>


<a id="state_cache-144"></a>
<details>
<summary><b>state_cache-144</b> Compact flattened checkpoint state — <i>n/a · medium · memory, cpu</i></summary>

**Idea.** Keep checkpoint states in a compact form: a pubkey array shared with the anchor state, balances only, active/slashed bitsets and one shuffled set.

**Impact.** Checkpoint states are structurally shared clones (validators list, pubkey cache), so a separate flattened compact form would add little.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/state_cache.rs:46-55`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L46-L55) cache holds full BeaconState values that share tree nodes via milhouse
- [`consensus/types/src/state/beacon_state.rs:3515`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L3515) rebase_caches_on shares pubkey and committee caches between states

**Sources.** [caplin#8482](https://github.com/erigontech/erigon/pull/8482)

</details>


<a id="state_cache-145"></a>
<details>
<summary><b>state_cache-145</b> Primitive int arrays for cached committees — <i>n/a · low · memory, cpu</i></summary>

**Idea.** Store cached committee assignments and validator index lists as primitive integer arrays, not boxed lists.

**Impact.** The idea is a JVM boxed-list problem. Rust Vec&lt;usize&gt; is already a primitive array.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/committee_cache.rs:155`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/committee_cache.rs#L155) shuffling_positions is a Vec of NonZeroUsize; active indices are Vec&lt;usize&gt; (line 447)

**Sources.** [teku#4259](https://github.com/Consensys-Incorporated/teku/pull/4259)

</details>


<a id="state_cache-146"></a>
<details>
<summary><b>state_cache-146</b> Preallocate epoch cache hashmaps — <i>n/a · low · memory, cpu</i></summary>

**Idea.** Preallocate hashmaps in the epoch cache builder with the known capacity to avoid rehashing.

**Impact.** The old epoch-cache hashmap is gone; the remaining caches use presized Vecs or a persistent map that cannot be presized. Nothing left to gain.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/epoch_cache.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/epoch_cache.rs): no HashMap in the epoch cache any more
- [`consensus/types/src/state/committee_cache.rs:155`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/committee_cache.rs#L155),447 vectors presized
- [`consensus/types/src/state/pubkey_cache.rs:13`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/pubkey_cache.rs#L13) rpds HashTrieMap (persistent, no capacity)

**Sources.** [lighthouse@815439711](https://github.com/sigp/lighthouse/commit/81543971142c)

</details>


<a id="state_cache-147"></a>
<details>
<summary><b>state_cache-147</b> Reserve spare capacity on state list growth — <i>n/a · low · memory, cpu</i></summary>

**Idea.** When appending to or copy-on-write copying state lists (validators, participation), allocate spare capacity (e.g. max deposits per block) so appends do not reallocate.

**Impact.** Milhouse lists are persistent trees with batched pending updates, not contiguous Vecs; there is no array to reallocate on append. Does not apply.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_block_processing/process_operations.rs:741`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/process_operations.rs#L741),774,873,1184 push into milhouse Lists
- milhouse list.rs:178 push goes through the interface with pending updates

**Sources.** [prysm#13068](https://github.com/OffchainLabs/prysm/pull/13068), [prysm#12832](https://github.com/OffchainLabs/prysm/pull/12832)

</details>


<a id="state_cache-148"></a>
<details>
<summary><b>state_cache-148</b> Keep validator cache capacity on transfer — <i>n/a · low · cpu, memory</i></summary>

**Idea.** When transferring a validator cache to a new state, reinitialise its arrays at the original size, not a small default, avoiding repeated growth.

**Impact.** Teku-specific quirk where a transferred cache re-grew from a small default; Lighthouse caches are cloned or rebuilt at the right size.

**Best measured result.** epochTransition 2.447 -&gt; 2.684 ops/s (pr:teku#5794)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/committee_cache.rs:155`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/committee_cache.rs#L155) caches are rebuilt/cloned with exact sizes
- [`beacon_node/store/src/state_cache.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs): states cloned via structural sharing

**Sources.** [teku#5794](https://github.com/Consensys-Incorporated/teku/pull/5794)

</details>


<a id="state_cache-149"></a>
<details>
<summary><b>state_cache-149</b> In-memory LRU of recent hot states — <i>implemented · medium · S · memory, latency, disk, cpu</i></summary>

**Idea.** Keep recent unfinalized post-states in an in-memory cache keyed by block root, so block import and duties do not read, write or replay states from the database.

**Impact.** Block import and duties hit the in-memory cache, with the disk path as fallback.

**Best measured result.** hit ratio &gt;99% (cited from #4834) (pr:prysm#5004)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/state_cache.rs:46-55`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L46-L55) LRU StateCache with block_map
- [`beacon_node/store/src/state_cache.rs:316`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L316) get_by_block_root finds the state at the slot or the nearest ancestor
- [`beacon_node/store/src/state_cache.rs:215`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L215) put_state
- [`beacon_node/store/src/hot_cold_store.rs:1661`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1661) store_hot_state fills the cache on import
- [`beacon_node/store/src/hot_cold_store.rs:1812`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1812) get_hot_state checks the cache first

**Skeptic check.** Verified that the cache is keyed by state root, has a block-root to slot map, and is filled on import and on disk loads. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#5004](https://github.com/OffchainLabs/prysm/pull/5004), [lodestar#910](https://github.com/ChainSafe/lodestar/pull/910), [nimbus#654](https://github.com/status-im/nimbus-eth2/pull/654)

</details>


<a id="state_cache-150"></a>
<details>
<summary><b>state_cache-150</b> Tune hot state cache size — <i>implemented · low · S · cpu, latency, memory, startup</i></summary>

**Idea.** Size the hot state cache large enough (e.g. 32 entries, larger at startup with many forks) to keep the miss rate low and avoid replay-based regeneration.

**Impact.** The default of 128 is 4x the size suggested, and it is configurable.

**Best measured result.** hot state miss rate ~4% to 2% (pr:prysm#6033)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/config.rs:23`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/config.rs#L23) DEFAULT_STATE_CACHE_SIZE=128
- [`beacon_node/store/src/state_cache.rs:357`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L357) cull with priority ordering and headroom
- [`beacon_node/store/src/hot_cold_store.rs:1817-1824`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1817-L1824) get_hot_state warns on miss

**Skeptic check.** The default size is far above the Prysm/Teku numbers and can be set with --state-cache-size. The cull keeps boundary states that could finalize, which lowers replay cost further.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#7340](https://github.com/OffchainLabs/prysm/pull/7340), [prysm#6033](https://github.com/OffchainLabs/prysm/pull/6033), [teku#2591](https://github.com/Consensys-Incorporated/teku/pull/2591)

</details>


<a id="state_cache-151"></a>
<details>
<summary><b>state_cache-151</b> Store sparse states, regenerate by replay — <i>implemented · low · S · memory, disk, cpu, latency</i></summary>

**Idea.** Persist only periodic archive/restore-point states plus summaries and regenerate any other state by loading the nearest saved state and replaying blocks forward, instead of storing every state.

**Impact.** Hot and cold states are stored sparsely, as snapshots and diffs plus summaries, and are regenerated by replay.

**Best measured result.** exp pods used 500MB less (from related flag PRs) (pr:prysm#6087)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:1949`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1949) load_hot_state: summary then snapshot/diff/replay
- [`beacon_node/store/src/hot_cold_store.rs:1968`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1968) hot_storage_strategy(slot)
- [`beacon_node/store/src/hot_cold_store.rs:2306`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2306) load_cold_state_by_slot hdiff then replay
- [`beacon_node/store/src/hot_cold_store.rs:1722`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1722) store_hot_state_summary

**Skeptic check.** Confirmed that both hot and cold paths store sparse states and replay blocks. This goes further than Prysm's restore points because it uses hierarchical diffs.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#6087](https://github.com/OffchainLabs/prysm/pull/6087), [prysm#4834](https://github.com/OffchainLabs/prysm/pull/4834), [prysm#5393](https://github.com/OffchainLabs/prysm/pull/5393), [prysm#5108](https://github.com/OffchainLabs/prysm/pull/5108), [prysm#4877](https://github.com/OffchainLabs/prysm/pull/4877), [prysm#5100](https://github.com/OffchainLabs/prysm/pull/5100), [prysm#5101](https://github.com/OffchainLabs/prysm/pull/5101)

</details>


<a id="state_cache-152"></a>
<details>
<summary><b>state_cache-152</b> Do not pin disk-loaded states in cache — <i>implemented · low · S · memory, disk</i></summary>

**Idea.** Keep states loaded from storage in the cache only on demand rather than pinning them, so cold states do not hold memory.

**Impact.** Disk-loaded states go into the evictable cache on demand. Nothing is pinned.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:1812-1858`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1812-L1858) get_hot_state inserts disk-loaded states into the LRU only when update_cache is true
- [`beacon_node/store/src/state_cache.rs:357-400`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L357-L400) cull evicts LRU, exempting only the head and the most-recently-used fraction

**Skeptic check.** The Grandine commit routes storage loads through state_cache.get_or_insert_with, an evictable cache. Lighthouse's get_hot_state does the same with put_state into the culled LRU, and callers can skip caching. Upheld.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [grandine@ce7476aa0](https://github.com/grandinetech/grandine/commit/ce7476aa0a0d)

</details>


<a id="state_cache-153"></a>
<details>
<summary><b>state_cache-153</b> Periodic hot state snapshots in long non-finality — <i>implemented · medium · S · memory, disk</i></summary>

**Idea.** During long non-finality persist a hot state every N slots so regeneration replays stay short, and delete them after finalization.

**Impact.** Hot replays bounded to under one epoch even in long non-finality; pruned at finalization.

**Best measured result.** about 2GB extra disk on Medalla; memory spikes from replay otherwise (pr:prysm#7597)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hdiff.rs:619-624`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs#L619-L624) default exponents [5,...]: hot diff layer every 32 slots
- [`beacon_node/store/src/hot_cold_store.rs:407`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L407) hot_storage_strategy from anchor slot
- [`beacon_node/store/src/hot_cold_store.rs:1706-1707`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1706-L1707) store_hot_state_summary + store_hot_state_diffs on every stored hot state
- [`beacon_node/beacon_chain/src/migrate.rs:509`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L509) prune_hot_db deletes non-canonical/non-grid hot states at finalization

**Skeptic check.** Verified the hot hdiff grid writes a diff or snapshot every 32 slots independent of finality, and prune_hot_db removes them after finalization. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#7597](https://github.com/OffchainLabs/prysm/pull/7597)

</details>


<a id="state_cache-154"></a>
<details>
<summary><b>state_cache-154</b> Prune before persisting checkpoint states — <i>n/a · low · disk, memory</i></summary>

**Idea.** Prune finalized checkpoint states before persisting in one serialized flow, so a racing prune cannot orphan files and soon-pruned states are not serialized.

**Impact.** Lighthouse has no separate on-disk checkpoint-state file store (states go in DB with summaries), so there are no orphan files to race with pruning.

**Best measured result.** persisted checkpoint states grew ~197MB per orphan file (screenshot) (pr:lodestar#9463)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:1068`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1068) put_state writes to hot/cold DB, not per-checkpoint files
- [`beacon_node/store/src/state_cache.rs:127`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L127) update_finalized_state prunes in-memory

**Sources.** [lodestar#9463](https://github.com/ChainSafe/lodestar/pull/9463)

</details>


<a id="state_cache-155"></a>
<details>
<summary><b>state_cache-155</b> Prune on-disk states one epoch behind finality — <i>implemented · low · S · disk</i></summary>

**Idea.** Prune stored fork states up to one epoch behind the finalized slot (cutoff from the highest slot with a stored state), then drop fork-graph blocks older than the oldest stored state.

**Impact.** Hot state and fork block pruning at finalization already exists; Caplin's exact one-epoch cutoff is an implementation detail.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/migrate.rs:509-720`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/migrate.rs#L509-L720) prune_hot_db prunes conflicting and pre-finalized hot states, keeps hdiff layer points (closest_layer_points:641) and blocks descendant of finalized checkpoint
- [`beacon_node/store/src/hot_cold_store.rs:424`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L424) update_finalized_state prunes the in-memory state cache

**Skeptic check.** prune_hot_db does the same job (drop on-disk fork states and blocks behind finality) via the state summaries DAG. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [caplin#11219](https://github.com/erigontech/erigon/pull/11219), [caplin#11472](https://github.com/erigontech/erigon/pull/11472)

</details>


<a id="state_cache-156"></a>
<details>
<summary><b>state_cache-156</b> Cache of historical cold states — <i>implemented · low · S · latency, cpu, disk</i></summary>

**Idea.** Cache reconstructed historical (freezer) states so repeated historical lookups do not rebuild them each time.

**Impact.** Repeated historical lookups reuse cached states/hdiff buffers; archive/API nodes only.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/historic_state_cache.rs:15`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/historic_state_cache.rs#L15) HistoricStateCache
- [`beacon_node/store/src/hot_cold_store.rs:2306-2355`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2306-L2355) load_cold_state_by_slot uses the cache
- [`beacon_node/store/src/config.rs:26`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/config.rs#L26) DEFAULT_HISTORIC_STATE_CACHE_SIZE

**Skeptic check.** This is Lighthouse's own PR #4228 and the cache is present on the cold-state load path. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#4228](https://github.com/sigp/lighthouse/pull/4228)

</details>


<a id="state_cache-157"></a>
<details>
<summary><b>state_cache-157</b> Historical state regen on dedicated worker — <i>partial · medium · M · cpu, latency</i></summary>

**Idea.** Serve historical state requests from a separate worker thread with its own regen queue and persisted pubkey index, so old-state API work does not block the main thread.

**Gap in Lighthouse.** Historic state requests are bounded and deprioritised in the shared beacon processor P1 queue with their own historic state cache, but they still run on the shared worker pool; no dedicated historic-state worker or separate regen queue. Lodestar's main-thread problem does not apply to multi-threaded Lighthouse.

**Impact.** Only matters for nodes serving heavy historical state API load; a long cold-state replay can hold one shared worker.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/task_spawner.rs:22`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/task_spawner.rs#L22) API work goes into beacon processor ApiRequestP0/P1 queues
- [`beacon_node/beacon_processor/src/lib.rs:1153`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_processor/src/lib.rs#L1153) api_request_p1_queue popped only after gossip/import work
- [`beacon_node/http_api/src/lib.rs:588`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/lib.rs#L588) state endpoints use Priority::P1
- [`beacon_node/store/src/hot_cold_store.rs:2310`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2310) separate historic_state_cache for cold states

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [lodestar#6033](https://github.com/ChainSafe/lodestar/pull/6033)

</details>


<a id="state_cache-158"></a>
<details>
<summary><b>state_cache-158</b> Opt-in historical state regeneration — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Make historical state regeneration opt-in so staking nodes do not pay its cost.

**Impact.** Non-archive (staking) nodes do not retain or reconstruct historic states, so no historical regen cost.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/src/cli.rs:1301-1309`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/src/cli.rs#L1301-L1309) --archive (alias reconstruct-historic-states)
- [`beacon_node/beacon_chain/src/builder.rs:363`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/builder.rs#L363) retain_historic_states = chain_config.archive
- [`beacon_node/store/src/hot_cold_store.rs:3583-3586`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3583-L3586) states below state_upper_limit (STATE_UPPER_LIMIT_NO_RETAIN) not stored on non-archive nodes

**Skeptic check.** Verified that the archive flag controls retention and reconstruction; without it the freezer holds no historic states to regenerate. The mechanism differs from Lodestar's serve flag but the effect is the same.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#7799](https://github.com/ChainSafe/lodestar/pull/7799)

</details>


<a id="state_cache-159"></a>
<details>
<summary><b>state_cache-159</b> State cache during initial sync — <i>implemented · medium · S · sync</i></summary>

**Idea.** Keep states in a cache between consecutive blocks during initial sync, avoiding DB saves and loads per block.

**Impact.** Consecutive blocks in range sync get the parent state from memory, not from disk.

**Best measured result.** "significant increase to sync speed" (pr:prysm#4938)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/state_cache.rs:215`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L215) put_state keeps post-states in memory (128 default, config.rs:23)
- [`beacon_node/store/src/hot_cold_store.rs:1661-1671`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1661-L1671) store_hot_state puts state in cache first
- [`beacon_node/beacon_chain/src/block_verification.rs:2065`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L2065) load_parent uses get_advanced_hot_state, served from the cache

**Skeptic check.** Checked block import and chain-segment parent loading both go through get_advanced_hot_state on the state cache. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#4938](https://github.com/OffchainLabs/prysm/pull/4938)

</details>


<a id="state_cache-160"></a>
<details>
<summary><b>state_cache-160</b> Free sync caches after range sync — <i>n/a · low · memory</i></summary>

**Idea.** Clear initial-sync state caches once range sync finishes, to release memory.

**Impact.** Lighthouse has no separate initial-sync state cache; range sync uses the one bounded LRU state cache that culls on finalization.

**Best measured result.** States were using 600mb in memory after sync (pr:prysm#4817)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/state_cache.rs:127`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L127) update_finalized_state / :357 cull bound the shared state cache
- [`beacon_node/store/src/state_cache.rs:45`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L45) single capped LRU, no separate sync-state cache

**Sources.** [prysm#4817](https://github.com/OffchainLabs/prysm/pull/4817)

</details>


<a id="state_cache-161"></a>
<details>
<summary><b>state_cache-161</b> Fewer state dumps during forward sync — <i>implemented · low · S · memory, cpu</i></summary>

**Idea.** During forward sync save or dump states only at epoch-multiple slots and prune finalized cache entries later, cutting per-block state copies.

**Impact.** Per-block full state dumps are already avoided during forward sync.

**Best measured result.** 10x less memory allocs during forward sync (pr:caplin#11815)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:1706-1707`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1706-L1707) only summary per slot; diffs/snapshots only on grid slots via hot_storage_strategy:407
- [`beacon_node/store/src/hot_cold_store.rs:1697`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1697) skips storage if summary already present
- [`beacon_node/store/src/hot_cold_store.rs:424`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L424) update_finalized_state prunes cached pre-finalized states

**Skeptic check.** Non-grid slots write only a HotStateSummary (ReplayFrom), so the per-block dump cost Caplin removed does not exist. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [caplin#11815](https://github.com/erigontech/erigon/pull/11815)

</details>


<a id="state_cache-162"></a>
<details>
<summary><b>state_cache-162</b> Pre-advance head state and serve consumers from it — <i>partial · high · S · latency, cpu, memory</i></summary>

**Idea.** Before the next slot, advance the head state through the empty slot (and epoch transition) in the background and cache it, then serve block import, proposal, gossip validation, payload attributes, sync committee and duty lookups from it, so these paths skip slot processing on the critical path. Watch its memory cost.

**Gap in Lighthouse.** Payload-attributes path: compute_withdrawals_for_payload_attributes (called by prepare_beacon_proposer) does not use the pre-advanced state from the state cache; it clones the head state and runs partial_state_advance to proposal_slot, which repeats epoch processing at an epoch boundary. The pre-Gloas optimisation (stop at epoch boundary) was removed per the TODO.

**Impact.** Removes a duplicate slot/epoch transition on the proposer-prep/fcU path for the next proposer, mostly at epoch boundaries (~100ms+ of epoch processing on mainnet).

**Best measured result.** 30% memory increase seen on develop, suspected cause (pr:prysm#8855)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/state_advance_timer.rs:258-300`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L258-L300) advance_head advances head via per_slot_processing (epoch transition included)
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:380-450`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L380-L450) primes proposer/attester caches and put_state of the advanced state
- [`beacon_node/beacon_chain/src/block_verification.rs:2065`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L2065) block import uses get_advanced_hot_state
- [`beacon_node/beacon_chain/src/block_production/mod.rs:89`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_production/mod.rs#L89) block production uses get_advanced_hot_state
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5396-5487`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5396-L5487) compute_withdrawals_for_payload_attributes clones cached head state and runs partial_state_advance; TODO(gloas) at 5443 says to use get_advanced_hot_state
- [`beacon_node/beacon_chain/src/beacon_chain.rs:6989`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L6989) called from prepare_beacon_proposer

**Skeptic check.** Block import, block production, gossip and duties are served from the advanced state and primed caches as claimed, but the payload attributes withdrawals path advances its own copy; the earlier verdict missed this consumer.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [prysm#10110](https://github.com/OffchainLabs/prysm/pull/10110), [prysm#8855](https://github.com/OffchainLabs/prysm/pull/8855), [prysm#12233](https://github.com/OffchainLabs/prysm/pull/12233), [prysm#8830](https://github.com/OffchainLabs/prysm/pull/8830), [prysm#8357](https://github.com/OffchainLabs/prysm/pull/8357), [prysm#16454](https://github.com/OffchainLabs/prysm/pull/16454), [prysm#16439](https://github.com/OffchainLabs/prysm/pull/16439), [prysm#8398](https://github.com/OffchainLabs/prysm/pull/8398), [prysm#9167](https://github.com/OffchainLabs/prysm/pull/9167), [prysm#9200](https://github.com/OffchainLabs/prysm/pull/9200), [lighthouse#4415](https://github.com/sigp/lighthouse/pull/4415), [prysm#12286](https://github.com/OffchainLabs/prysm/pull/12286), [prysm#12288](https://github.com/OffchainLabs/prysm/pull/12288), [prysm#12287](https://github.com/OffchainLabs/prysm/pull/12287), [prysm#9884](https://github.com/OffchainLabs/prysm/pull/9884)

</details>


<a id="state_cache-163"></a>
<details>
<summary><b>state_cache-163</b> Precompute state one epoch ahead at epoch end — <i>implemented · low · S · latency, cpu</i></summary>

**Idea.** On the last slot of an epoch allow precomputing states one epoch further ahead, so the next epoch-boundary state is ready earlier.

**Impact.** Next epoch-boundary state and next-next-epoch shuffling are ready before the epoch starts.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/state_advance_timer.rs:258`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L258) advance_head crosses the epoch boundary on the last slot and caches the state
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:345-420`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L345-L420) primes current/next epoch proposer caches and next-epoch attester shuffling
- [`beacon_node/http_api/src/attester_duties.rs:30`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/attester_duties.rs#L30) tolerant_current_epoch
- [`beacon_node/http_api/src/proposer_duties.rs:69`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/proposer_duties.rs#L69) same tolerance

**Skeptic check.** Grandine PR has no diff available; read as relaxing the future-epoch limit at the last slot, which Lighthouse covers via the epoch-crossing advance and tolerant epoch in the duty APIs.

**Verdict history.** partial (checked) → implemented (refuted) → implemented (skeptic)

**Sources.** [grandine#269](https://github.com/grandinetech/grandine/pull/269)

</details>


<a id="state_cache-164"></a>
<details>
<summary><b>state_cache-164</b> Prefer in-memory regen base within tolerance — <i>partial · low · M · memory, disk</i></summary>

**Idea.** For state regeneration prefer an in-memory base state if it is within the hot-state storage interval of the on-disk one, avoiding a disk load.

**Gap in Lighthouse.** load_hot_state always picks the on-disk summary's diff base and does not look for a newer cached state of the same block chain (within the hot diff interval) to replay from. A search in StateCache for the nearest cached ancestor state with slot &lt;= target would avoid hdiff load plus extra replay.

**Impact.** Only helps a state-cache miss on a non-head state (reorg, API/historic-ish hot lookups); head path already served from cache, so small on mainnet nodes.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:1949-2040`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1949-L2040) load_hot_state: ReplayFrom recurses into load_hot_state for the epoch-boundary base, which loads an hdiff buffer (checks cache only for hdiff buffer, line ~1863)
- hot_cold_store.rs:1196 get_advanced_hot_state_from_cache picks a cached state by block root and max_slot
- hot_cold_store.rs:1817 get_hot_state checks cache by exact state root only

**Sources.** [teku#3024](https://github.com/Consensys-Incorporated/teku/pull/3024)

</details>


<a id="state_cache-165"></a>
<details>
<summary><b>state_cache-165</b> Choose regen base without loading block — <i>n/a · low · S · disk, latency</i></summary>

**Idea.** Pick the regeneration base state using block summary data (root, slot) only, without loading the base block from the DB.

**Impact.** Base state is chosen from the hot state summary and the slot hierarchy; no base block is read, so there is nothing to save.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:1966`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1966) hot_storage_strategy(slot) picks base from slot alone
- [`beacon_node/store/src/hot_cold_store.rs:1993`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1993) base root from summary diff_base_state.get_root
- [`beacon_node/store/src/hot_cold_store.rs:2514`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2514) load_blocks_to_replay only loads blocks between base and target

**Sources.** [teku#3259](https://github.com/Consensys-Incorporated/teku/pull/3259)

</details>


<a id="state_cache-166"></a>
<details>
<summary><b>state_cache-166</b> Late binding of regen base state — <i>n/a · low · S · memory</i></summary>

**Idea.** Choose the regeneration base state when the task runs rather than when it is queued, so queued requests do not hold references to large states.

**Impact.** Regen is not queued as tasks holding states; the base is resolved when the load runs, so queued requests hold no large states.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:1949`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1949) load_hot_state is synchronous, base chosen inside the call
- [`beacon_node/store/src/hot_cold_store.rs:1812`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1812) get_hot_state checks state_cache first

**Sources.** [teku#3007](https://github.com/Consensys-Incorporated/teku/pull/3007)

</details>


<a id="state_cache-167"></a>
<details>
<summary><b>state_cache-167</b> State existence check without reading state — <i>not · low · S · latency, disk</i></summary>

**Idea.** Implement has_state as a pure existence check: look in the cache without touching LRU order, then probe DB keys, never reading and decoding a full state.

**Gap in Lighthouse.** A cheap state-exists helper would check state_cache without LRU promotion and then probe the hot state summary key; no production caller currently needs it and none does a full state load just to test existence, so it is a minor API gap.

**Impact.** Negligible on a mainnet node: no hot-path caller found that decodes a state merely to check existence.

**Best measured result.** has_state guard p50 180 ms, p90 332 ms, max 536 ms on the block after each epoch's first block; 0-1 ms on most others (pr:ethlambda#658)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:3000`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3000) load_hot_state_summary exists (summary-only read)
- [`beacon_node/store/src/hot_cold_store.rs:1087`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1087) get_state fully loads state; grep for has_state/state_exists found only test helpers
- [`beacon_node/store/src/state_cache.rs:275`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L275) get_by_state_root touches LRU order

**Sources.** [ethlambda#658](https://github.com/lambdaclass/ethlambda/pull/658)

</details>


<a id="state_cache-168"></a>
<details>
<summary><b>state_cache-168</b> Evict hot block bodies, reload on demand — <i>implemented · low · S · memory</i></summary>

**Idea.** Keep only block roots tree in memory and drop hot block bodies, reloading them from the DB when needed (e.g. for regeneration).

**Impact.** Hot block bodies are not held in memory by default; replay reads them from disk.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/config.rs:22`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/config.rs#L22) DEFAULT_BLOCK_CACHE_SIZE = 0
- [`beacon_node/store/src/config.rs:108`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/config.rs#L108) block_cache_size default
- [`beacon_node/store/src/hot_cold_store.rs:2521`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2521) replay loads blocks from DB

**Skeptic check.** Confirmed the default block LRU is disabled and fork choice keeps only proto-array nodes. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#2211](https://github.com/Consensys-Incorporated/teku/pull/2211)

</details>


<a id="state_cache-169"></a>
<details>
<summary><b>state_cache-169</b> Advance clone before storing checkpoint state — <i>n/a · medium · S · cpu, memory</i></summary>

**Idea.** In the checkpoint-state cache, clone the base state before advancing slots and store the advanced copy, so later attestations hit the cache and skip clone plus process_slots.

**Gap in Lighthouse.** Lighthouse has no checkpoint-state cache: attestation verification uses the shuffling cache keyed by decision root, so there is no target-state clone plus process_slots on that path.

**Impact.** None for gossip attestation verification; production path (produce_unaggregated_attestation) could cache the advanced state, minor.

**Best measured result.** Flame graph: clone much smaller after fix; no number (pr:prysm#4288)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/shuffling_cache.rs:128`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L128) ShufflingCache serves attestation verification without a target state
- [`beacon_node/beacon_chain/src/beacon_chain.rs:7593`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L7593) with_committee_cache
- [`beacon_node/beacon_chain/src/beacon_chain.rs:2164`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2164) only attestation production advances a clone

**Sources.** [prysm#4288](https://github.com/OffchainLabs/prysm/pull/4288)

</details>


<a id="state_cache-170"></a>
<details>
<summary><b>state_cache-170</b> Past-epoch block root lookup in checkpoint processing — <i>n/a · high · memory</i></summary>

**Idea.** Handle past-epoch processing so block-root lookups in checkpoint-state processing near head do not fail and trigger regeneration loops that OOM.

**Impact.** Lodestar-specific bug in persistent checkpoint cache regen; Lighthouse has no checkpoint state cache or regen loop.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:1124`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1124) get_advanced_hot_state: states looked up by block root and advanced, no checkpoint-state cache
- [`beacon_node/store/src/hot_cold_store.rs:2031`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2031) load_hot_state_using_replay uses roots from stored state/iterators

**Sources.** [lodestar#7505](https://github.com/ChainSafe/lodestar/pull/7505)

</details>


<a id="state_cache-171"></a>
<details>
<summary><b>state_cache-171</b> Global active validator cache across state copies — <i>partial · medium · S · cpu, memory</i></summary>

**Idea.** Share a process-wide active-validator-index and total-active-balance cache keyed by epoch and dependent root across all state copies, filled even without balances, so the full validator scan runs once per epoch per fork.

**Gap in Lighthouse.** Active indices are shared globally and total active balance comes free from single-pass epoch processing, but the balance value is per state; states rebuilt from disk without the cache rescan validators. Would add a process-wide (epoch, decision root) -&gt; total_active_balance map.

**Impact.** Saves one O(validators) scan per reloaded state per epoch; minor.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/shuffling_cache.rs:128`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L128) global shuffling cache keyed by (epoch, decision root) holds active indices
- [`consensus/state_processing/src/per_epoch_processing/single_pass.rs:482`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/single_pass.rs#L482) epoch transition sets next-epoch total active balance without an extra scan
- [`consensus/types/src/state/beacon_state.rs:2724`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2724) force_build_total_active_balance_cache full scan for states without the cache

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [caplin#18525](https://github.com/erigontech/erigon/pull/18525), [caplin#18554](https://github.com/erigontech/erigon/pull/18554)

</details>


<a id="state_cache-172"></a>
<details>
<summary><b>state_cache-172</b> Keep previous head state for reorgs — <i>implemented · low · S · disk, memory, latency</i></summary>

**Idea.** Keep the head-1 state in memory, updated by copy-into, for fast 1-block reorgs, replacing a disk-backed merkle cache.

**Impact.** Head parent and recent fork states stay in memory with milhouse sharing, so 1-block reorgs hit cache.

**Best measured result.** less I/O and less RAM + faster reorg speed (pr:caplin#13671)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/state_cache.rs:45`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L45) in-memory state cache keyed by block root (128 default)
- [`beacon_node/store/src/state_cache.rs:357-390`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L357-L390) cull never prunes the head state, LRU keeps recent parents
- [`beacon_node/store/src/hot_cold_store.rs:1196`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1196) get_advanced_hot_state_from_cache by block root

**Skeptic check.** Recent states including head-1 remain in the LRU state cache; there is no disk-backed merkle cache to replace. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [caplin#13671](https://github.com/erigontech/erigon/pull/13671)

</details>


<a id="state_cache-173"></a>
<details>
<summary><b>state_cache-173</b> Dedicated justified state cache for fork choice — <i>implemented · low · S · cpu, latency</i></summary>

**Idea.** Keep a dedicated cached state for the justified checkpoint used by fork choice, and skip scheduled per-slot work when the node is behind the clock.

**Impact.** Fork choice only needs justified balances, which are cached; per-slot advance is skipped while behind.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_fork_choice_store.rs:58-75`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_fork_choice_store.rs#L58-L75) BalancesCache of epoch-boundary justified balances
- [`beacon_node/beacon_chain/src/beacon_fork_choice_store.rs:341-368`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_fork_choice_store.rs#L341-L368) set_justified_checkpoint uses cache, loads state only on miss
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:38`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L38),269 skip advance when head &gt;256 slots behind

**Skeptic check.** Lighthouse fork choice needs only justified balances, and BalancesCache supplies them without a state load; the skip-when-behind half is the MAX_ADVANCE_DISTANCE check. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus@e7b36c438](https://github.com/status-im/nimbus-eth2/commit/e7b36c438952)

</details>


<a id="state_cache-174"></a>
<details>
<summary><b>state_cache-174</b> Lazy validators/balances load for API states — <i>n/a · low · S · memory</i></summary>

**Idea.** Do not eagerly materialize all validators and balances when loading a state for API use; preload only for the checkpoint cache.

**Impact.** Lodestar's cost is converting a tree to materialized validator arrays; Lighthouse states keep validators as milhouse tree nodes. API loads can skip caching but still build caches (small).

**Best measured result.** Fixes main-thread memory spike; no numbers (pr:lodestar#9245)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:1830`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1830) get_hot_state: update_cache=false skips cache insert
- [`beacon_node/store/src/hot_cold_store.rs:1975`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1975) buffer.as_state then rebase_on_finalized to share tree nodes
- milhouse-0.9.0/src/builder.rs streaming tree builder; validators stay in the tree, no separate materialized array

**Sources.** [lodestar#9245](https://github.com/ChainSafe/lodestar/pull/9245)

</details>


<a id="state_cache-175"></a>
<details>
<summary><b>state_cache-175</b> Tree-hash leaves from iterator, bounded fork ring — <i>n/a · low · S · memory</i></summary>

**Idea.** Build tree-hash leaf stores from a leaf iterator rather than an intermediate flat buffer, and bound the per-slot fork ring so non-finality cannot overflow it.

**Impact.** Milhouse already builds trees from an iterator and caches hashes in tree nodes; there is no per-slot fork ring in Lighthouse.

**Evidence (Lighthouse @ 928b61e719).**

- milhouse-0.9.0/src/builder.rs:39 push builds tree incrementally with a stack, no flat buffer
- milhouse-0.9.0/src/list.rs:88 try_from_iter

**Sources.** [silver#154](https://github.com/gattaca-com/silver/pull/154)

</details>


<a id="state_cache-176"></a>
<details>
<summary><b>state_cache-176</b> Limit speculative proposer-prediction replays — <i>n/a · low · latency, cpu, disk</i></summary>

**Idea.** Skip the speculative next-epoch proposer prediction that replays states except in the last slot of the epoch.

**Impact.** Lighthouse primes proposer shuffling from the single state-advance copy, with no speculative multi-state replay.

**Best measured result.** 5s+ replays each slot on Holesky (replayDur=5s418ms) (pr:nimbus#7072)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/state_advance_timer.rs:355-390`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L355-L390) proposer cache primed from the already-advanced head state
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:373`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L373) next-epoch shuffling taken from the state (Fulu lookahead), no replay

**Sources.** [nimbus#7072](https://github.com/status-im/nimbus-eth2/pull/7072)

</details>


<a id="state_cache-177"></a>
<details>
<summary><b>state_cache-177</b> Resolve block roots from state block_roots — <i>implemented · low · S · sync, startup</i></summary>

**Idea.** After checkpoint sync, answer block-at-slot queries from block_roots of in-memory states (up to SLOTS_PER_HISTORICAL_ROOT back) so dependent roots resolve before backfill.

**Impact.** Block-at-slot queries within SLOTS_PER_HISTORICAL_ROOT of head resolve from the in-memory head state, so they work right after checkpoint sync, before backfill.

**Best measured result.** accelerates the first couple minutes of checkpoint sync on mainnet (pr:nimbus#5869)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:1050-1082`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1050-L1082) block_root_at_slot_skips_none reads request and prev roots from head_state.block_roots before any DB/oldest_block_slot check
- [`beacon_node/beacon_chain/src/beacon_chain.rs:1124-1142`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1124-L1142) block_root_at_slot_skips_prev fast path from head state
- [`beacon_node/beacon_chain/src/beacon_chain.rs:832-838`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L832-L838) forwards iterator falls back to head state

**Skeptic check.** Verified that both block_root_at_slot variants try head.beacon_state.get_block_root first, ahead of the oldest_block_slot range check. Earlier evidence was right; the more direct proof is the fast path at 1060-1082, not only the forwards iterator.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#5869](https://github.com/status-im/nimbus-eth2/pull/5869)

</details>


<a id="state_cache-178"></a>
<details>
<summary><b>state_cache-178</b> Non-blocking try-lock in cache pruning — <i>n/a · low · S · latency, cpu</i></summary>

**Idea.** During state cache pruning use try-lock and skip busy entries (retrying at next prune) instead of waiting with a timeout, and remove emptied entries under a single lock acquisition.

**Impact.** None: states are owned values in a HashMap under one mutex, there are no per-entry locks to wait on; prune is a single in-memory pass.

**Best measured result.** waiting 1.5 s per busy entry adds up to minutes (commit:grandine@2ec9f905fd7e)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:82`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L82) state_cache is one parking_lot Mutex&lt;StateCache&gt;, plain lock()
- [`beacon_node/store/src/state_cache.rs:127-170`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L127-L170) update_finalized_state prunes block_map and states synchronously under that one lock; no per-entry locks
- [`beacon_node/store/src/state_cache.rs:421`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L421) BlockMap::prune is a retain pass

**Sources.** [grandine@2ec9f905f](https://github.com/grandinetech/grandine/commit/2ec9f905fd7e), [grandine#950](https://github.com/grandinetech/grandine/pull/950)

</details>


<a id="state_cache-179"></a>
<details>
<summary><b>state_cache-179</b> Run state cache pruning off the store lock — <i>implemented · medium · S · latency</i></summary>

**Idea.** Spawn state cache pruning as a separate task instead of running it while holding the fork-choice store lock, so other fork-choice operations are not blocked.

**Impact.** State cache pruning at finalization runs on the BackgroundMigrator thread, not under the fork-choice lock.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/canonical_head.rs:1725`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1725) after_finalization hands pruning to store_migrator.process_finalization
- [`beacon_node/store/src/hot_cold_store.rs:3665`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3665) migrate_database -&gt; update_finalized_state on migrator thread
- [`beacon_node/store/src/hot_cold_store.rs:424-439`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L424-L439) only the state_cache mutex is held
- [`beacon_node/beacon_chain/src/canonical_head.rs:1738`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1738) the only work under fork_choice_write_lock is proto-array prune

**Skeptic check.** Verified that after_finalization only enqueues the migration, and that state-cache pruning happens in migrate_database. The fork-choice write lock covers only ForkChoice::prune. Earlier evidence was correct.

**Verdict history.** partial (checked) → implemented (refuted) → implemented (skeptic)

**Sources.** [grandine#522](https://github.com/grandinetech/grandine/pull/522), [grandine@c726d6341](https://github.com/grandinetech/grandine/commit/c726d6341b3c)

</details>


<a id="state_cache-180"></a>
<details>
<summary><b>state_cache-180</b> Pass state cache through rewind steps — <i>implemented · low · S · cpu</i></summary>

**Idea.** Build the per-state cache once and pass it through slot advance and block application during a rewind, rather than rebuilding it per step.

**Impact.** Committee, tree-hash and pubkey caches live in the state and carry through every replay step.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/block_replayer.rs:215`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/block_replayer.rs#L215) apply_blocks mutates one state via per_slot_processing/per_block_processing
- [`beacon_node/store/src/hot_cold_store.rs:2031`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2031) load_hot_state_using_replay

**Skeptic check.** Lighthouse caches are fields of BeaconState, so rewinds never rebuild them per step; this is the Nimbus fix's effect by design.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#1612](https://github.com/status-im/nimbus-eth2/pull/1612)

</details>


<a id="state_cache-181"></a>
<details>
<summary><b>state_cache-181</b> Transfer hash caches only to imported clone — <i>n/a · medium · cpu</i></summary>

**Idea.** On block import, give the tree-hash/serialization caches only to the state clone that is imported, not throwaway clones for validation, production or next-slot prep.

**Impact.** Tree-hash caches live inside the milhouse persistent tree, so state clones share them structurally; there is no per-clone cache to hand over, nothing to save.

**Best measured result.** motivated by metrics showing the SSZ cache almost never populated; no numbers (pr:lodestar#5172)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:1148`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1148) update_tree_hash_cache on loaded state
- [`beacon_node/store/src/state_cache.rs:253`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L253) put_state clones state

**Sources.** [lodestar#5172](https://github.com/ChainSafe/lodestar/pull/5172)

</details>


<a id="state_cache-182"></a>
<details>
<summary><b>state_cache-182</b> Prune grandparent snapshot after insert — <i>partial · low · S · memory</i></summary>

**Idea.** After inserting a block into the snapshot cache, prune the grandparent snapshot, which is safe from one-block reorgs, so skipped slots do not leave extra states cached.

**Gap in Lighthouse.** Snapshot cache is gone; StateCache::put_state does not drop the grandparent state after insert. Eviction only happens at capacity via cull(), which prefers advanced states.

**Impact.** Saves a few cached states' memory (milhouse shares most nodes) on skipped-slot runs; marginal.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/state_cache.rs:357`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L357) cull() evicts advanced states first, protects head, keeps cull_exempt most recent
- beacon_chain/src: snapshot_cache.rs no longer exists (only metric name in metrics.rs:102)
- [`beacon_node/store/src/state_cache.rs:215`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L215) put_state has no grandparent prune

**Sources.** [lighthouse#2917](https://github.com/sigp/lighthouse/pull/2917)

</details>


<a id="state_cache-183"></a>
<details>
<summary><b>state_cache-183</b> Epoch-matching state cache for attestations — <i>implemented · medium · S · sync, cpu</i></summary>

**Idea.** In attestation handling check the target epoch before rewinding, let the state cache match by epoch rather than exact slot, and store the updated state so repeated lookups hit.

**Impact.** Attestation committee lookups match by epoch/decision root and the result is cached, so repeated lookups do not rewind or replay states.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/shuffling_cache.rs:330-353`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L330-L353) keyed by AttestationShufflingId (epoch + decision root), read-lock hit
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:398-447`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L398-L447) miss uses the head state when possible, else get_advanced_hot_state, and only partial-advances when the epoch requires it
- [`beacon_node/store/src/state_cache.rs:316`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L316) get_by_block_root returns highest slot &lt;= max_slot

**Skeptic check.** with_cached_shuffling checks the epoch need before advancing and caches the committee rather than the advanced state, which gives the same effect for attestations. Earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#1348](https://github.com/status-im/nimbus-eth2/pull/1348)

</details>


<a id="state_cache-184"></a>
<details>
<summary><b>state_cache-184</b> Rebase clearance state on head during chain stall — <i>implemented · low · S · latency</i></summary>

**Idea.** When the chain stalls, rebase the block clearance/advance state on the fork-choice head so a proposer does not have to catch up a long run of empty slots before it can propose.

**Impact.** Lighthouse has no separate clearance state that can drift from the head. The advance timer and block production both build on the fork-choice head.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/state_advance_timer.rs:277-284`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L277-L284) advance_head always starts from the fork-choice head_snapshot block root
- [`beacon_node/beacon_chain/src/block_production/mod.rs:84-96`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_production/mod.rs#L84-L96) proposer uses get_advanced_hot_state on the head block root
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:38`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L38),269 MAX_ADVANCE_DISTANCE=256 stops advancing during very long stalls

**Skeptic check.** Nimbus #6108 fixed a clearanceState that tracked the latest resolved block instead of the canonical head. Lighthouse always advances and proposes from head_snapshot. One small caveat: after a stall of more than 256 slots, the timer stops and the proposer replays the empty slots itself.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#6108](https://github.com/status-im/nimbus-eth2/pull/6108)

</details>


<a id="state_cache-185"></a>
<details>
<summary><b>state_cache-185</b> Refresh next-slot cache when execution payload arrives late — <i>implemented · low · S · latency</i></summary>

**Idea.** When a late execution payload changes the post-state, recompute the next-slot cache and boundary caches from it (and send forkchoice update if proposing next slot) so the next proposer has a warm pre-state.

**Impact.** Nothing left to gain. Lighthouse follows the deferred-payload Gloas spec: verify_execution_payload_envelope does not change the state, and process_parent_execution_payload applies the parent payload's effects inside the next block's processing. So the state the advance timer pre-advanced (keyed on the block state root) is already the right pre-state for the next proposer, Full or Empty. A late envelope runs recompute_head_at_current_slot. The head changes on a payload-status change alone, and that sends forkchoiceUpdated.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/envelope_processing.rs:97-107`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/envelope_processing.rs#L97-L107)
- [`consensus/state_processing/src/per_block_processing.rs:135-138`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing.rs#L135-L138)
- [`consensus/state_processing/src/per_block_processing.rs:562-595`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing.rs#L562-L595)
- [`beacon_node/beacon_chain/src/payload_envelope_verification/mod.rs:374-393`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/payload_envelope_verification/mod.rs#L374-L393)
- [`beacon_node/network/src/network_beacon_processor/gossip_methods.rs:4083-4085`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/network/src/network_beacon_processor/gossip_methods.rs#L4083-L4085)
- [`beacon_node/beacon_chain/src/canonical_head.rs:1106-1137`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1106-L1137)
- [`beacon_node/beacon_chain/src/canonical_head.rs:1884-1913`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1884-L1913)
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:276-296`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L276-L296)

**Second check.** The earlier screen said no_feature (Gloas-specific). I checked the Lighthouse Gloas code: envelope verification does not mutate state (execution requests are applied via process_parent_execution_payload in the next block). Gossip envelope import calls recompute_head_at_current_slot, which rebuilds the head snapshot on a payload-status change from get_advanced_hot_state and runs the FCU. The idea is therefore covered by an equivalent mechanism, and the Prysm next-slot-cache refresh has no counterpart to do.

**Skeptic check.** Checked that envelope verification is pure (it uses a cloned header and never writes the state) and that the deferred requests are applied in per_block_processing. So Prysm's next-slot cache refresh has nothing to fix in Lighthouse. Checked that canonical_head rebuilds the cached head when new_payload_status differs and spawns the EL forkchoice update. The earlier evidence was right.

**Verdict history.** not (checked) → implemented (refuted) → implemented (skeptic)

**Sources.** [prysm#16460](https://github.com/OffchainLabs/prysm/pull/16460)

</details>


<a id="state_cache-186"></a>
<details>
<summary><b>state_cache-186</b> Bound the number of full states held in memory — <i>implemented · high · S · memory</i></summary>

**Idea.** Cap the hot state/checkpoint cache to a small number of full states (fewer entries, every other slot, a bounded number of epochs) and regenerate the rest on demand, because each epoch-boundary state can cost hundreds of MB and unbounded caches OOM during non-finality.

**Impact.** The hot state cache is bounded by count and culls the least useful states, and evicted states are regenerated from disk. Disk-loaded states are rebased on the finalized state to share memory.

**Best measured result.** 128 entries ~20GB; 32 x 180MB ~ 6GB (pr:lighthouse#7055)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/config.rs:23`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/config.rs#L23) DEFAULT_STATE_CACHE_SIZE=128 bounded LRU (--state-cache-size, cli.rs:833)
- [`beacon_node/store/src/state_cache.rs:252-259`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L252-L259) cull on overflow
- [`beacon_node/store/src/state_cache.rs:357-412`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L357-L412) cull order: advanced, old boundary, mid-epoch, then good boundary states
- [`beacon_node/store/src/state_cache.rs:197-210`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L197-L210) rebase_on_finalized for states loaded from disk

**Skeptic check.** The cap is real. The default of 32 from lighthouse#7055/#7101 was reverted to 128 by #7364 (commit 6c8770e80d), which relies on structural sharing and rebase_on_finalized. The bound is a state count, not bytes.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#2294](https://github.com/Consensys-Incorporated/teku/pull/2294), [lighthouse#7055](https://github.com/sigp/lighthouse/pull/7055), [lighthouse#7101](https://github.com/sigp/lighthouse/pull/7101), [nimbus#1290](https://github.com/status-im/nimbus-eth2/pull/1290), [nimbus@fc8502c54](https://github.com/status-im/nimbus-eth2/commit/fc8502c54e35), [grandine#87](https://github.com/grandinetech/grandine/pull/87), [lodestar#452](https://github.com/ChainSafe/lodestar/pull/452)

</details>


<a id="state_cache-187"></a>
<details>
<summary><b>state_cache-187</b> Do expensive state work outside the cache lock — <i>partial · medium · M · latency, cpu</i></summary>

**Idea.** Do not hold the state or shuffling cache lock while computing or waiting for a state, shuffling or diff buffer; release the lock first and share the result through a promise or once-cell, so other threads are not blocked.

**Gap in Lighthouse.** lighthouse#8176 (OnceCell/Arc in HotHDiffBufferCache) was CLOSED, not merged. StateCache::get_hdiff_buffer_by_state_root, StateCache::put_state (pre-finalized branch) and StateCache::update_finalized_state still run HDiffBuffer::from_state (up to about 1s) while holding the state_cache mutex. HistoricStateCache::get_hdiff_buffer and get_state also run from_state/as_state under the historic cache lock. get_hot_state and get_advanced_hot_state have no in-flight promise, so concurrent misses on the same root each replay from disk.

**Impact.** Every state-cache lookup (block import, attestation miss path, API) can stall behind an HDiffBuffer conversion during hdiff loads and finalization.

**Best measured result.** HDiffBuffer::from_state can take up to 1s under lock (pr:lighthouse#8176)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:1817-1858`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1817-L1858) get_hot_state locks only for lookup/put (correct)
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:370-377`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L370-L377) promise then drop lock (correct)
- [`beacon_node/store/src/hot_cold_store.rs:1919-1925`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1919-L1925) load_hot_hdiff_buffer calls get_hdiff_buffer_by_state_root under state_cache.lock()
- [`beacon_node/store/src/state_cache.rs:304-306`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L304-L306) HDiffBuffer::from_state of a cached state while the mutex is held
- [`beacon_node/store/src/state_cache.rs:229`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L229) put_state pre-finalized branch runs HDiffBuffer::from_state under the lock
- [`beacon_node/store/src/state_cache.rs:173`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L173) update_finalized_state converts pruned states to HDiffBuffers under the lock
- [`beacon_node/store/src/historic_state_cache.rs:42`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/historic_state_cache.rs#L42),64 get_hdiff_buffer/get_state run from_state/as_state under historic_state_cache lock (hot_cold_store.rs:2310,2424)

**Skeptic check.** The earlier verdict assumed #8176 was merged. show.py shows it was closed unmerged, and the from_state calls under the mutex are still in the code. The #3589 shuffling-promise part and the disk load outside the lock in get_hot_state are real.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [lighthouse#3589](https://github.com/sigp/lighthouse/pull/3589), [lighthouse#8176](https://github.com/sigp/lighthouse/pull/8176), [teku#2664](https://github.com/Consensys-Incorporated/teku/pull/2664)

</details>


<a id="state_cache-188"></a>
<details>
<summary><b>state_cache-188</b> Check in-memory caches before DB state loads — <i>implemented · medium · S · latency, disk, cpu</i></summary>

**Idea.** On hot state-by-root and block-and-state lookups, check the in-memory state caches (hot cache, finalized state) first and fall back to a database load and replay only on a miss.

**Impact.** In-memory caches (hot cache and finalized state) are checked first. The node loads from the DB and replays blocks only on a miss.

**Best measured result.** avoids a lot of regenerated states (pr:teku#2610)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:1124-1132`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1124-L1132) get_advanced_hot_state checks the cache first
- [`beacon_node/store/src/hot_cold_store.rs:1817`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1817) get_hot_state checks the cache first
- [`beacon_node/store/src/state_cache.rs:275-282`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L275-L282) get_by_state_root serves finalized_state
- [`beacon_node/store/src/hot_cold_store.rs:1087-1110`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1087-L1110) get_state routes through get_hot_state

**Skeptic check.** Verified the cache-first order on both hot lookup entry points and the finalized-state shortcut. Earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#7674](https://github.com/OffchainLabs/prysm/pull/7674), [teku#2610](https://github.com/Consensys-Incorporated/teku/pull/2610)

</details>


<a id="state_cache-189"></a>
<details>
<summary><b>state_cache-189</b> Advance epoch caches once per epoch transition — <i>implemented · low · S · cpu</i></summary>

**Idea.** Build or advance the per-epoch caches (committee, proposer, etc.) exactly once in the slot/epoch processing path rather than twice per epoch transition.

**Impact.** Caches rotate once per epoch transition.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/per_epoch_processing/altair.rs:81`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/altair.rs#L81) single advance_caches
- [`consensus/state_processing/src/per_epoch_processing/base.rs:73`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_epoch_processing/base.rs#L73) single advance_caches
- [`consensus/state_processing/src/per_slot_processing.rs:38-75`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_slot_processing.rs#L38-L75) no second advance after per_epoch_processing

**Skeptic check.** Grep shows advance_caches is called only once per fork's epoch processing; per_slot_processing does not call it again. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse@b88750960](https://github.com/sigp/lighthouse/commit/b88750960736)

</details>


<a id="state_cache-190"></a>
<details>
<summary><b>state_cache-190</b> Drop fork-aware finalized pubkey cache — <i>n/a · low · memory, cpu</i></summary>

**Idea.** Delete a separate finalized pubkey-to-index cache and its maintenance once deposits are guaranteed finalized before validator creation, since one shared map suffices.

**Impact.** Lighthouse has no separate fork-aware finalized pubkey cache; one persistent map per state.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/pubkey_cache.rs:6-12`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/pubkey_cache.rs#L6-L12) single pubkey-&gt;index map
- [`consensus/types/src/state/beacon_state.rs:2979`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2979) update_pubkey_cache

**Sources.** [prysm#14497](https://github.com/OffchainLabs/prysm/pull/14497)

</details>


<a id="state_cache-191"></a>
<details>
<summary><b>state_cache-191</b> Remove redundant lock around thread-safe cache — <i>n/a · low · latency, cpu</i></summary>

**Idea.** Do not wrap an already thread-safe LRU state cache in an extra mutex/RwLock; the outer lock only adds contention.

**Impact.** Go LRU double-locking; Lighthouse uses a single Mutex over its own StateCache.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:1201-1203`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1201-L1203) state_cache is a plain Mutex around a Rust cache, no nested thread-safe LRU

**Sources.** [prysm#11846](https://github.com/OffchainLabs/prysm/pull/11846), [prysm#16469](https://github.com/OffchainLabs/prysm/pull/16469)

</details>


<a id="state_cache-192"></a>
<details>
<summary><b>state_cache-192</b> Remove per-state caches that pin old states — <i>n/a · low · memory</i></summary>

**Idea.** Remove per-state view caches that hold references to views of older state instances when views are already cached at the backing-tree level, so old hot states can be freed.

**Impact.** Teku/JVM view caches; milhouse caches live in the tree nodes, nothing pins old states separately.

**Best measured result.** chart in PR of significantly lower hot state memory; no numbers (pr:teku#2175)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/pubkey_cache.rs:2`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/pubkey_cache.rs#L2) rpds persistent map, no per-state view caches pinning older states
- [`beacon_node/store/src/hot_cold_store.rs:1172-1175`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1172-L1175) states held in one state_cache

**Sources.** [teku#2175](https://github.com/Consensys-Incorporated/teku/pull/2175), [teku#2188](https://github.com/Consensys-Incorporated/teku/pull/2188), [lighthouse@931da1354](https://github.com/sigp/lighthouse/commit/931da13545d7)

</details>


<a id="state_cache-193"></a>
<details>
<summary><b>state_cache-193</b> Consult checkpoint cache only for viable non-canonical targets — <i>n/a · low · cpu</i></summary>

**Idea.** On attestation target-state lookup, read the checkpoint state cache only when the checkpoint is viable and not on the canonical branch, skipping the lookup otherwise.

**Impact.** Lighthouse has no checkpoint state cache; attestation target lookups go through the shuffling cache, so there is no lookup to skip.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/shuffling_cache.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs): attestations use shuffling cache keyed by decision root
- [`beacon_node/beacon_chain/src/data_column_verification.rs:1750-1760`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1750-L1760) proposer cache then get_advanced_hot_state

**Sources.** [prysm#12397](https://github.com/OffchainLabs/prysm/pull/12397)

</details>


<a id="state_cache-194"></a>
<details>
<summary><b>state_cache-194</b> Keep persisted-file key when re-adding reloaded states — <i>n/a · low · disk</i></summary>

**Idea.** When a checkpoint state reloaded from disk is re-added to the in-memory cache, keep its on-disk key so later pruning deletes the file instead of orphaning it.

**Impact.** No on-disk checkpoint state files with an in-memory cache keyed by file; nothing to orphan.

**Evidence (Lighthouse @ 928b61e719).**

- grep checkpoint_cache/CheckpointCache in beacon_node: no matches
- [`beacon_node/store/src/hot_cold_store.rs:1124`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1124) hot states are in DB, not checkpoint files

**Sources.** [lodestar#9557](https://github.com/ChainSafe/lodestar/pull/9557)

</details>


<a id="state_cache-195"></a>
<details>
<summary><b>state_cache-195</b> Rebuild pruned pre-state for delayed sidecar blocks — <i>n/a · medium · sync</i></summary>

**Idea.** When a block delayed on blobs/data columns needs a pre-state that was pruned from cache, rebuild it through the state cache and retry instead of dropping the block.

**Impact.** Lighthouse executes the block (state transition) before waiting for blobs/columns and parks the executed block with its post-state, so no pruned pre-state is needed later; any miss at verification already rebuilds from DB.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:2065`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L2065) pre-state loaded with get_advanced_hot_state (rebuilds on cache miss) at verification time
- [`beacon_node/beacon_chain/src/data_availability_checker.rs:439`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_availability_checker.rs#L439) AvailabilityPendingExecutedBlock keeps already-executed block

**Sources.** [grandine@324854cde](https://github.com/grandinetech/grandine/commit/324854cde1bd)

</details>


<a id="state_cache-196"></a>
<details>
<summary><b>state_cache-196</b> Reuse the block post-state as new head state — <i>implemented · medium · S · cpu, latency</i></summary>

**Idea.** After importing a block, take the new head state from the post-state already in hand (or the clearance state) rather than requesting or replaying it from the state generator, which can also evict the cached pre-state needed next.

**Impact.** The new head state is the cached post-state of the imported block. It is not regenerated, and the head state is never culled.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:4752`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L4752) PutState of the post-state on import
- [`beacon_node/store/src/hot_cold_store.rs:1661-1670`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1661-L1670) store_hot_state inserts into state_cache
- [`beacon_node/beacon_chain/src/canonical_head.rs:1134-1137`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/canonical_head.rs#L1134-L1137) new head state from get_advanced_hot_state (cache hit)
- [`beacon_node/store/src/state_cache.rs:386-388`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L386-L388) head state exempt from cull

**Skeptic check.** Verified the import -&gt; state_cache -&gt; recompute_head path. Separately, recompute_head reloads the full head block from the DB (get_full_block, block cache default 0), but that is outside this state idea.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#1388](https://github.com/status-im/nimbus-eth2/pull/1388), [prysm#6729](https://github.com/OffchainLabs/prysm/pull/6729)

</details>


<a id="state_cache-197"></a>
<details>
<summary><b>state_cache-197</b> Use head state for prior-epoch data column validation — <i>partial · low · S · cpu, latency</i></summary>

**Idea.** When validating a data column whose parent state is the head state from the previous epoch, use the head state directly; on a miss replay only to the target checkpoint state rather than the parent state.

**Gap in Lighthouse.** On a proposer-cache miss Lighthouse loads the parent's (possibly slot-advanced) state rather than the head state or target checkpoint state; no epoch transition replay is done, but a state load from DB can occur when the advanced state is not cached. Could shortcut to canonical head state when parent is head. Change the closure in verify_proposer_and_signature.

**Impact.** Rare cache miss path only; the proposer cache already avoids state access in the common case, so gain is small.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/data_column_verification.rs:1738-1762`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/data_column_verification.rs#L1738-L1762) proposer cache keyed by shuffling root, miss loads parent state via get_advanced_hot_state(parent_root, column_slot)
- [`beacon_node/store/src/hot_cold_store.rs:1124-1184`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1124-L1184) returns cached advanced state or loads parent state and caches it

**Sources.** [prysm#16250](https://github.com/OffchainLabs/prysm/pull/16250)

</details>


<a id="state_cache-198"></a>
<details>
<summary><b>state_cache-198</b> Archive persisted checkpoint bytes without re-serializing — <i>not · medium · S · cpu, disk</i></summary>

**Idea.** When a finalized checkpoint state is already persisted on disk, archive its stored bytes directly instead of deserializing and re-serializing the state.

**Gap in Lighthouse.** In migrate_database, when cold_storage_strategy(slot) is Snapshot and the hot DB holds a BeaconStateHotSnapshot for that root, copy the compressed bytes straight into BeaconStateSnapshot (keyed by slot) plus the cold summary, skipping get_hot_state and re-encode/re-compress. Diff layers cannot reuse bytes (different bases).

**Impact.** Tiny: only archive nodes, only cold-snapshot-layer slots that are also hot snapshots; saves one SSZ encode + zstd compress (and decode on cache miss) per rare snapshot.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:3604-3610`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L3604-L3610) migrate_database calls get_hot_state then store_cold_state for non-replay slots
- [`beacon_node/store/src/hot_cold_store.rs:1817-1819`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1817-L1819) get_hot_state returns state-cache hit (skips decode) but otherwise load_hot_state + tree hash + build_all_caches
- [`beacon_node/store/src/hot_cold_store.rs:2143-2163`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2143-L2163) store_cold_state_as_snapshot always as_ssz_bytes + zstd re-compress
- [`beacon_node/store/src/hot_cold_store.rs:2182-2209`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2182-L2209) hot snapshot already stored zstd-compressed under BeaconStateHotSnapshot (same format)
- [`beacon_node/store/src/hot_cold_store.rs:2212-2232`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2212-L2232) load_hot_state_bytes_as_snapshot exists but only used for decoding (line 2247), never for byte copy

**Second check.** Checked all store_cold_state callers (migrate_database, reconstruct.rs:180, genesis, store_state:1071) and the hot/cold snapshot byte helpers; none copy raw stored bytes. State cache hit only avoids the decode, not the re-serialization/compression.

**Verdict history.** not (checked) → not (refuted)

**Sources.** [lodestar#6504](https://github.com/ChainSafe/lodestar/pull/6504)

</details>


<a id="state_cache-199"></a>
<details>
<summary><b>state_cache-199</b> Cache block post-states for block production — <i>partial · low · M · cpu, latency</i></summary>

**Idea.** Cache post-states (and block rewards) from block processing in a fine-grained-locked cache so block production reuses them rather than re-running state transitions.

**Gap in Lighthouse.** The grandine block processor caches the post-state and block rewards keyed by block root when it processes the produced block, so the import of the node's own block (and a second production of the same block) reuses them. In Lighthouse, complete_partial_beacon_block computes the post-state and then drops it (produce_block.rs `_block_state`). The own block is then processed again from the parent state in the publish -&gt; process_block import path. Block rewards come from a separate compute_beacon_block_reward pass, not from the processing pass.

**Impact.** Saves one per_block_processing pass and one tree-hash pass on the import of each locally proposed block (tens of ms on the proposal critical path). Only proposing nodes gain.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_production/mod.rs:87-89`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_production/mod.rs#L87-L89) parent post-state served from the state cache via get_advanced_hot_state
- [`beacon_node/beacon_chain/src/beacon_chain.rs:6537-6553`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L6537-L6553) complete_partial_beacon_block runs compute_beacon_block_reward as a separate pass, then per_block_processing + update_tree_hash_cache on the produced block
- [`beacon_node/beacon_chain/src/beacon_chain.rs:6589-6595`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L6589-L6595) post-state returned in BeaconBlockResponse
- [`beacon_node/http_api/src/produce_block.rs:101`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/produce_block.rs#L101) _block_state discarded by the HTTP API
- [`beacon_node/http_api/src/build_block_contents.rs:17`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/build_block_contents.rs#L17) BeaconBlockResponse state not kept

**Skeptic check.** Verified: the parent post-state is reused, as the earlier evidence said. But the main mechanism of the source commit, caching the post-state of the produced block for its import, is absent. The earlier check matched only the parent-state half of the idea.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [grandine@67b707828](https://github.com/grandinetech/grandine/commit/67b707828989)

</details>


<a id="state_cache-200"></a>
<details>
<summary><b>state_cache-200</b> Reuse prebuilt pubkey cache from anchor state — <i>implemented · low · S · startup, cpu</i></summary>

**Idea.** At startup, if the anchor state already carries a built pubkey cache, reuse it instead of rebuilding by deserializing all pubkeys.

**Impact.** Restart already skips pubkey decompression. load_from_store is sequential, so parallel loading could save a few seconds at most.

**Best measured result.** ~30 seconds for 350k keys (pr:lodestar#4319)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:53-78`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L53-L78) load_from_store reads persisted uncompressed keys
- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:237-242`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L237-L242) as_pubkey uses deserialize_uncompressed
- [`beacon_node/beacon_chain/src/builder.rs:286`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/builder.rs#L286) persisted cache loaded at restart
- [`beacon_node/beacon_chain/src/builder.rs:875`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/builder.rs#L875) ValidatorPubkeyCache::new from state only when no cache is persisted

**Skeptic check.** Confirmed that the persisted pubkey cache is reused on restart. This has the same effect as the Lodestar change (no expensive rebuild of all pubkeys from the anchor state).

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#4319](https://github.com/ChainSafe/lodestar/pull/4319)

</details>


<a id="state_cache-201"></a>
<details>
<summary><b>state_cache-201</b> Reuse pubkey map allocation when reinitializing caches — <i>n/a · low · memory, cpu</i></summary>

**Idea.** When re-initializing state caches, clear and reuse the existing pubkey-to-index map allocation rather than allocating a new map.

**Impact.** Persistent trie map has no big allocation to reuse; reinit is rare (drop_all_caches only).

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/pubkey_cache.rs:2-12`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/pubkey_cache.rs#L2-L12) rpds HashTrieMap, cloned structurally
- [`consensus/types/src/state/beacon_state.rs:2996`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2996) drop_pubkey_cache just resets to default

**Sources.** [caplin#14461](https://github.com/erigontech/erigon/pull/14461)

</details>


<a id="state_cache-202"></a>
<details>
<summary><b>state_cache-202</b> Load startup state once and share across services — <i>implemented · low · S · startup, memory</i></summary>

**Idea.** Register the startup (genesis/finalized) state once and hand it to all services instead of each service reloading it from the database.

**Impact.** Startup state is loaded once by the builder and shared via the BeaconChain (canonical head / state cache).

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/builder.rs:302-330`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/builder.rs#L302-L330) set_genesis_state builds caches and stores the state once
- [`beacon_node/beacon_chain/src/builder.rs:406`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/builder.rs#L406) weak_subjectivity_state
- [`beacon_node/beacon_chain/src/builder.rs:229`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/builder.rs#L229) resume_from_db

**Skeptic check.** All services take the single BeaconChain object; no service reloads the startup state from the database. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#9900](https://github.com/OffchainLabs/prysm/pull/9900)

</details>


<a id="state_cache-203"></a>
<details>
<summary><b>state_cache-203</b> Keep future-epoch info and per-block state cache — <i>n/a · low · S · cpu</i></summary>

**Idea.** Do not discard cached epoch info for future epochs, and do not build a fresh state cache per block application.

**Impact.** Nimbus separate EpochRef/StateCache design does not exist; caches are part of BeaconState and Next-epoch caches are kept.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:825`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L825) committee_caches live on the state (prev/current/next) and are cloned with it
- [`beacon_node/beacon_chain/src/block_verification.rs:1684`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1684) build_all_committee_caches on the state, no per-block fresh cache object

**Sources.** [nimbus#1610](https://github.com/status-im/nimbus-eth2/pull/1610)

</details>


<a id="state_cache-204"></a>
<details>
<summary><b>state_cache-204</b> Persist skipped-slot states using state_roots — <i>implemented · low · S · cpu</i></summary>

**Idea.** When persisting intermediate skipped-slot states during block processing, derive their roots from the next state's state_roots field instead of tree hashing each one.

**Impact.** Each skipped-slot state is hashed once (needed anyway by slot processing) and reused for persistence; no extra hashing.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:1609-1645`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L1609-L1645) update_tree_hash_cache once per skipped-slot state, stored, then passed as Some(state_root) to per_slot_processing

**Skeptic check.** Verified the root is computed once and reused for both the store and per_slot_processing, and the parent's state root is taken from the block when unadvanced. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse@467852465](https://github.com/sigp/lighthouse/commit/4678524659f4)

</details>


<a id="state_cache-205"></a>
<details>
<summary><b>state_cache-205</b> Store shuffling once, derive committees and duties — <i>implemented · low · S · memory, cpu</i></summary>

**Idea.** Store only the shuffling plus a reverse map (validator index to position) in the committee cache and derive committees and duties on demand, instead of several redundant maps keyed by validator or slot.

**Impact.** Already compact; committees and duties derived from shuffling + shuffling_positions.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/committee_cache.rs:26-34`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/committee_cache.rs#L26-L34)

**Skeptic check.** CommitteeCache struct holds only initialized_epoch, shuffling, shuffling_positions (reverse map), committees_per_slot, slots_per_epoch; earlier evidence correct (this is Lighthouse's own change).

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse@21de9c1cb](https://github.com/sigp/lighthouse/commit/21de9c1cb887), [lighthouse@9eb8c7411](https://github.com/sigp/lighthouse/commit/9eb8c7411f80)

</details>


<a id="state_cache-206"></a>
<details>
<summary><b>state_cache-206</b> Do not preallocate state cache tables — <i>n/a · low · S · memory</i></summary>

**Idea.** Create state cache hash tables small so they do not preallocate many unused full BeaconState slots.

**Impact.** Nim hash table preallocation; Lighthouse uses an LRU sized by capacity that allocates on insert.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/state_cache.rs:89`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L89) LruCache::new(capacity) no preallocated state slots

**Sources.** [nimbus#1002](https://github.com/status-im/nimbus-eth2/pull/1002)

</details>


<a id="state_cache-207"></a>
<details>
<summary><b>state_cache-207</b> Store next-slot cache hit into checkpoint cache — <i>partial · low · S · cpu</i></summary>

**Idea.** When the next-slot cache answers an attestation target-state request, save that state into the checkpoint cache so later attestations for the same target hit directly.

**Gap in Lighthouse.** In the miss path of the attestation data production, after partial_state_advance, put the advanced state into store.state_cache so later requests for the same target hit. The state advance timer already fills the cache in the common case, so this only matters on timer misses.

**Impact.** Avoids repeating an epoch-boundary state advance (tens of ms) on rare cache misses at the first slot of an epoch; marginal.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs:2161`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L2161) get_advanced_hot_state used for attestation data; if state.current_epoch() &lt; request_epoch it runs partial_state_advance (:2164) and drops the result
- [`beacon_node/store/src/hot_cold_store.rs:1172`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1172) get_advanced_hot_state caches only the loaded state, not the advanced one
- [`beacon_node/store/src/state_cache.rs:316`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L316) get_by_block_root returns the latest cached state &lt;= slot

**Sources.** [prysm#12398](https://github.com/OffchainLabs/prysm/pull/12398)

</details>


<a id="state_cache-208"></a>
<details>
<summary><b>state_cache-208</b> Drop pubkey map and scan the registry — <i>n/a · low · S · memory</i></summary>

**Idea.** Remove the per-state pubkey-to-index hash map and find validators by linear registry scan, trading slower deposit processing for no memory spikes.

**Impact.** Prysm per-state full map copies caused spikes; Lighthouse's persistent map shares structure, so there is no spike to remove and a scan would be slower.

**Best measured result.** "completely removes memory spikes" (no numbers) (pr:prysm#8854)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/pubkey_cache.rs:9`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/pubkey_cache.rs#L9) per-state PubkeyCache is a persistent rpds HashTrieMap shared structurally between states
- [`consensus/state_processing/src/per_block_processing/process_operations.rs:76`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/process_operations.rs#L76) update_pubkey_cache adds only new validators

**Sources.** [prysm#8854](https://github.com/OffchainLabs/prysm/pull/8854)

</details>


<a id="state_cache-209"></a>
<details>
<summary><b>state_cache-209</b> Segmented page pool for lock-free state readers — <i>n/a · low · S · memory, latency</i></summary>

**Idea.** Grow the state page pool in fixed pre-zeroed segments with a pre-reserved segment list so growth never moves existing pages and lock-free readers stay valid.

**Impact.** Silver-specific page pool for lock-free readers; Lighthouse state cache is a mutex-guarded LRU of persistent trees.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/state_cache.rs:89`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L89) states are milhouse tree values in an LRU, no page pool

**Sources.** [silver#396](https://github.com/gattaca-com/silver/pull/396)

</details>


<a id="state_cache-210"></a>
<details>
<summary><b>state_cache-210</b> Dedicated clearance state for block sync — <i>n/a · medium · S · sync, cpu</i></summary>

**Idea.** Use a separate state for block clearance so block sync does not alternate one temporary state between attestation and block use, which forces replays.

**Impact.** Lighthouse has no single shared temporary clearance state: each block gets a cloned (structurally shared) parent post-state from the keyed StateCache, so sync and attestation use do not alternate one state and force replays.

**Best measured result.** helps block sync speed a lot (pr:nimbus#1352)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/block_verification.rs:2063`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_verification.rs#L2063) load_parent fetches parent post-state by block root from StateCache
- [`beacon_node/store/src/state_cache.rs:316`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L316) get_by_block_root

**Sources.** [nimbus#1352](https://github.com/status-im/nimbus-eth2/pull/1352)

</details>


<a id="state_cache-211"></a>
<details>
<summary><b>state_cache-211</b> Process block attestations in target order — <i>n/a · medium · S · cpu</i></summary>

**Idea.** Process a block's attestations sequentially ordered by target checkpoint so the first populates the checkpoint state cache and the rest hit it, instead of each recomputing the epoch-boundary state in parallel.

**Impact.** Lighthouse verifies block attestations on the single block pre-state with its committee caches and uses a promise-based ShufflingCache for gossip, so no per-attestation target checkpoint state is regenerated.

**Best measured result.** logs show ~1.8s processSlots repeated per attestation (pr:lodestar#1557)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/shuffling_cache.rs:315`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L315) with_cached_shuffling
- [`consensus/state_processing/src/per_block_processing/process_operations.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/per_block_processing/process_operations.rs) (attestations processed in order on the one pre-state)

**Sources.** [lodestar#1557](https://github.com/ChainSafe/lodestar/pull/1557)

</details>


<a id="state_cache-212"></a>
<details>
<summary><b>state_cache-212</b> Serve finalized-state lookups from the in-memory copy — <i>implemented · low · S · cpu, disk</i></summary>

**Idea.** Serve finalized-state requests (by root, or for deposit pruning) from the finalized checkpoint state already held in memory instead of loading, regenerating or copying it from the database.

**Impact.** API 'finalized' state resolves to slot &gt;= split slot, goes through get_hot_state which returns the held finalized_state clone (cheap milhouse clone); no deposit-pruning path exists.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/state_cache.rs:275-281`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L275-L281)
- [`beacon_node/store/src/hot_cold_store.rs:1812-1819`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1812-L1819)
- [`beacon_node/store/src/hot_cold_store.rs:1087-1110`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1087-L1110)
- [`beacon_node/http_api/src/state_id.rs:41-47`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/state_id.rs#L41-L47)

**Skeptic check.** Verified get_by_state_root checks finalized_state first and both get_state and get_hot_state route through it; earlier evidence right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#10273](https://github.com/ChainSafe/lodestar/pull/10273), [prysm#9985](https://github.com/OffchainLabs/prysm/pull/9985)

</details>


<a id="state_cache-213"></a>
<details>
<summary><b>state_cache-213</b> Cheap presence check on shuffling cache — <i>implemented · low · S · cpu</i></summary>

**Idea.** Give the shuffling cache a has/contains check so callers can test presence without computing or memoizing an expensive shuffling.

**Impact.** Block import skips building committee caches when the shuffling is already cached.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/shuffling_cache.rs:209-211`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L209-L211)
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:196-207`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L196-L207)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5216-5222`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5216-L5222)

**Skeptic check.** ShufflingCache::contains is a plain contains_key under a read lock and is used on the import path before build_committee_cache; get_shuffling_if_cached also non-mutating. Earlier evidence right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#9579](https://github.com/ChainSafe/lodestar/pull/9579)

</details>


<a id="state_cache-214"></a>
<details>
<summary><b>state_cache-214</b> Predict next-epoch duties without state advance — <i>implemented · low · S · cpu</i></summary>

**Idea.** Compute next-epoch attester shuffling and first proposer from the head state before the epoch boundary, skipping the full state advance when no effective balance can change.

**Impact.** Post-Fulu, the proposer_lookahead gives next-epoch proposers without an epoch transition. The attester shuffling already uses the one-epoch lookahead. Before Fulu, a partial_state_advance was still needed for next-epoch proposers, but that path is historical on mainnet.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/shuffling_cache.rs:410-423`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L410-L423) the next-epoch attester shuffling comes from a state advanced only to the start of the previous epoch
- [`beacon_node/beacon_chain/src/beacon_proposer_cache.rs:321-354`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_proposer_cache.rs#L321-L354) ensure_state_can_determine_proposers_for_epoch advances only when the decision slot needs it (post-Fulu, the lookahead makes the advance unnecessary)
- [`beacon_node/http_api/src/proposer_duties.rs:91-109`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/proposer_duties.rs#L91-L109) next-epoch proposer duties are computed from the head
- [`beacon_node/beacon_chain/src/state_advance_timer.rs:342-420`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs#L342-L420) the next-epoch caches are primed off the critical path

**Skeptic check.** Verified the attester and proposer paths. The Nimbus prediction trick (skip the advance when no effective balance can change) is only relevant before Fulu, and Fulu's lookahead removes the need for it.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#5414](https://github.com/status-im/nimbus-eth2/pull/5414)

</details>


<a id="state_cache-215"></a>
<details>
<summary><b>state_cache-215</b> Single shared head state buffer for services — <i>n/a · low · memory</i></summary>

**Idea.** Keep one head state shared with API/services under a read lock with release callback rather than keeping extra full copies for readers.

**Impact.** Rust BeaconState uses persistent tree structure sharing, so readers do not hold full copies.

**Best measured result.** "Reduces memory usage by 600MB too" (pr:caplin#12519)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/state_cache.rs:279`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L279) states are cloned with tree sharing (milhouse), no separate buffer per reader

**Sources.** [caplin#12519](https://github.com/erigontech/erigon/pull/12519)

</details>


<a id="state_cache-216"></a>
<details>
<summary><b>state_cache-216</b> Replay only blocks after base state on regen — <i>partial · low · S · disk, cpu</i></summary>

**Idea.** When regenerating from a stored base state, replay only blocks after it and do not require or fetch the base state's own block.

**Gap in Lighthouse.** load_blocks_to_replay fetches the base-state block (kept deliberately for its state root) and can load one extra older block before take_while stops. Could pass the base state's latest_block_root and stop at it.

**Impact.** Saves one block read per hot-state regen; negligible vs replay cost.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:2514-2549`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2514-L2549) load_blocks_to_replay still loads block at start_slot (and may read one older block) for its state root
- [`beacon_node/store/src/hot_cold_store.rs:2031-2042`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2031-L2042) load_hot_state_using_replay

**Sources.** [teku#3249](https://github.com/Consensys-Incorporated/teku/pull/3249)

</details>


<a id="state_cache-217"></a>
<details>
<summary><b>state_cache-217</b> State cache eviction policy and insertion rules — <i>implemented · low · S · memory, cpu</i></summary>

**Idea.** Tune state cache insertion and eviction: true LRU order, never evict the head, evict old epoch-boundary states first, cache ancestors only on epoch boundaries, and do not insert states read by migration/pruning so they do not evict useful states.

**Impact.** The policy is the merged form of the Lighthouse PRs themselves. No more gain is expected.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/state_cache.rs:357-412`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L357-L412) cull is LRU with extra order: advanced, old boundary, mid-epoch, could-finalize boundary; the head is never culled; the most recent 10% are exempt
- [`beacon_node/store/src/state_cache.rs:275-282`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L275-L282) get_by_state_root uses LruCache::get (promotes)
- [`beacon_node/store/src/hot_cold_store.rs:2031-2060`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2031-L2060) ancestor states are cached only on epoch boundaries and only when update_cache is set

**Skeptic check.** The source PRs are Lighthouse's own. The cull and LRU promotion code matches them.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#7067](https://github.com/sigp/lighthouse/pull/7067), [lighthouse#7095](https://github.com/sigp/lighthouse/pull/7095), [lighthouse#7364](https://github.com/sigp/lighthouse/pull/7364)

</details>


<a id="state_cache-218"></a>
<details>
<summary><b>state_cache-218</b> Store few checkpoint states while syncing — <i>partial · low · M · disk, sync</i></summary>

**Idea.** During sync, skip storing checkpoint states or store them only once per archival interval rather than every epoch.

**Gap in Lighthouse.** Hierarchical diffs already make full storage sparse (diff every 32 slots), but there is no sync-specific skip: every imported block puts its state in state_cache and writes a summary. Could skip caching/diffing while syncing far behind head.

**Impact.** Some CPU/IO saved during range sync from diff computation at grid slots; small since diffs are sparse.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:1661-1720`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1661-L1720) store_hot_state always caches and writes summary per state
- [`beacon_node/store/src/hdiff.rs:660-700`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs#L660-L700) storage_strategy: full diffs only at grid slots, replay otherwise
- [`beacon_node/store/src/config.rs:254`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/config.rs#L254) exponents 5,8,11,...

**Sources.** [grandine#607](https://github.com/grandinetech/grandine/pull/607), [grandine#609](https://github.com/grandinetech/grandine/pull/609)

</details>


<a id="state_cache-219"></a>
<details>
<summary><b>state_cache-219</b> Delay next-epoch duty lookahead into the epoch — <i>n/a · low · cpu</i></summary>

**Idea.** Schedule next-epoch duties a few slots into the epoch so the lookahead state need not be advanced across empty slots to compute shuffling and proposers.

**Impact.** Beacon node answers next-epoch duties from the primed shuffling cache without advancing the state across empty slots; timing of VC lookahead is not a BN state cost.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/http_api/src/attester_duties.rs:187-194`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/attester_duties.rs#L187-L194) next-epoch attester duties use partial_state_advance only on cache miss
- [`beacon_node/beacon_chain/src/beacon_chain.rs:5213-5225`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L5213-L5225) shuffling cache primed for Current and Next epoch on import

**Sources.** [nimbus#5406](https://github.com/status-im/nimbus-eth2/pull/5406)

</details>


<a id="state_cache-220"></a>
<details>
<summary><b>state_cache-220</b> Skip parent regen at genesis on startup — <i>n/a · low · startup</i></summary>

**Idea.** On startup, skip regenerating the parent state when the finalized or head state is genesis.

**Impact.** Lighthouse resumes from persisted fork choice/head and does not regenerate a parent state at startup, so there is nothing to skip.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/builder.rs:245-270`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/builder.rs#L245-L270) resume_from_db loads persisted fork choice and states, no regen of parent at genesis

**Sources.** [prysm#6237](https://github.com/OffchainLabs/prysm/pull/6237)

</details>


<a id="state_cache-221"></a>
<details>
<summary><b>state_cache-221</b> Cache decompressed pubkeys only for active validators — <i>not · low · M · memory</i></summary>

**Idea.** Do not insert decompressed pubkeys into the pubkey cache for validators that are not active, since they produce no consensus messages.

**Gap in Lighthouse.** Cache is a dense Vec indexed by validator index covering all registry entries including pending/inactive; deposits-only validators are decompressed at import. Would need lazy/sparse decompression keyed by activation status in import().

**Impact.** Saves decompression time at first startup and memory for not-yet-active validators (small fraction of ~1M validators; some tens of MB).

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:103-177`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L103-L177) import decompresses every key, parallel on first import
- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:24`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L24) index-addressed Vec of PublicKey

**Sources.** [prysm#13581](https://github.com/OffchainLabs/prysm/pull/13581)

</details>


<a id="state_cache-222"></a>
<details>
<summary><b>state_cache-222</b> Exact state cache hit skips epoch transition — <i>implemented · low · S · cpu, disk</i></summary>

**Idea.** When writing a state, skip slow legacy database reads and skip the epoch transition when an exact state match is already cached.

**Impact.** Cached (advanced) states returned without disk load or slot processing; no legacy DB in Lighthouse.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:1124-1132`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1124-L1132)
- [`beacon_node/store/src/state_cache.rs:308-326`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L308-L326)
- [`beacon_node/store/src/hot_cold_store.rs:1660-1690`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1660-L1690)

**Skeptic check.** get_advanced_hot_state hits the cache first and get_by_block_root returns the newest cached state &lt;= slot; store_hot_state detects Duplicate (still checks summary on disk, cheap). The Nimbus legacy-DB part has no Lighthouse counterpart.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus@60df17786](https://github.com/status-im/nimbus-eth2/commit/60df17786e5e)

</details>


<a id="state_cache-223"></a>
<details>
<summary><b>state_cache-223</b> Skip state-root check when replaying stored blocks — <i>implemented · low · S · cpu</i></summary>

**Idea.** When regenerating a state by replaying stored blocks, skip the per-block post-state hash tree root comparison against block.state_root.

**Impact.** Replay does not check state roots, and it gets per-slot roots without hashing whenever it can.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/state_processing/src/block_replayer.rs:241-283`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/block_replayer.rs#L241-L283) apply_blocks runs per_block_processing and has no post-state root comparison
- [`consensus/state_processing/src/block_replayer.rs:180-213`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/block_replayer.rs#L180-L213) get_state_root takes the state root from state_root_iter or from the previous block's state_root, and hashes only on a miss

**Skeptic check.** Verified in block_replayer.rs: no post-block state-root check, and slot processing takes trusted roots from the blocks or the iterator.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#5316](https://github.com/Consensys-Incorporated/teku/pull/5316)

</details>


<a id="state_cache-224"></a>
<details>
<summary><b>state_cache-224</b> Skip block validation when replaying local blocks — <i>implemented · low · S · cpu</i></summary>

**Idea.** When regenerating states from blocks already validated on import, skip signature and other block validation.

**Impact.** All non-test BlockReplayer sites skip signature verification and most block-root checks.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:2565-2567`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2565-L2567) replay_blocks uses no_signature_verification + minimal_block_root_verification
- [`beacon_node/http_api/src/sync_committee_rewards.rs:69-70`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/src/sync_committee_rewards.rs#L69-L70) the other production replayer also skips signatures
- [`consensus/state_processing/src/block_replayer.rs:262-268`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/state_processing/src/block_replayer.rs#L262-L268) the proposer index is taken from the block and not recomputed

**Skeptic check.** Searched all BlockReplayer uses. Every non-test site disables signature verification, so no replay path verifies signatures.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [teku#2203](https://github.com/Consensys-Incorporated/teku/pull/2203)

</details>


<a id="state_cache-225"></a>
<details>
<summary><b>state_cache-225</b> In-memory cache of diff base/snapshot states — <i>implemented · low · S · disk, cpu, latency</i></summary>

**Idea.** Cache decoded hierarchical-diff base snapshots and buffers in memory (keyed by slot, holding either state or buffer form and converting lazily) so historic state loads skip DB reads and decoding and sequential queries reuse prior work.

**Impact.** Already present (from Lighthouse's own PR #6475). The default sizes are small, so this is only a tuning question.

**Best measured result.** Most sequential queries after the first served in 400-700ms on mainnet (hierarchy exponents 5,7,11) (pr:lighthouse#6475)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/historic_state_cache.rs:14-56`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/historic_state_cache.rs#L14-L56) LRUs of HDiffBuffer and BeaconState keyed by slot, converted lazily
- [`beacon_node/store/src/hot_cold_store.rs:2310-2319`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2310-L2319) cold state loads check the historic cache
- [`beacon_node/store/src/config.rs:26-27`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/config.rs#L26-L27) defaults: 1 state, 16 hdiff buffers

**Skeptic check.** Confirmed that HistoricStateCache exists with lazy buffer/state conversion and is used on cold loads, as the earlier evidence said.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#17573](https://github.com/OffchainLabs/prysm/pull/17573), [prysm#17561](https://github.com/OffchainLabs/prysm/pull/17561), [lighthouse#6475](https://github.com/sigp/lighthouse/pull/6475)

</details>


<a id="state_cache-226"></a>
<details>
<summary><b>state_cache-226</b> Reclaimable soft/weak references for cached states — <i>n/a · low · L · memory</i></summary>

**Idea.** Hold non-head cached states or cached tree views through soft/weak references so the runtime reclaims them under memory pressure, bounding the cache by memory instead of count.

**Impact.** Rust has no soft/weak-reference reclamation by memory pressure; cache is bounded by count and finality.

**Best measured result.** avoids OOM at the expense of possible ~2x state access slowdown (pr:teku#2235)

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/state_cache.rs:43`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L43) states is a count-bounded LruCache; Rust has no GC soft refs

**Sources.** [teku#2235](https://github.com/Consensys-Incorporated/teku/pull/2235), [lodestar#3420](https://github.com/ChainSafe/lodestar/pull/3420)

</details>


<a id="state_cache-227"></a>
<details>
<summary><b>state_cache-227</b> Sparse checkpoint replay at attestation pool init — <i>n/a · low · L · startup, cpu</i></summary>

**Idea.** At startup, replay checkpoint states only for the first block of each long interval rather than for many blocks, keeping only recent blocks exact.

**Impact.** Lighthouse persists fork choice and does not replay checkpoint states to init an attestation pool.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/src/beacon_chain.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs): fork choice is persisted, no attestation-pool EpochRef replay at startup

**Sources.** [nimbus#8578](https://github.com/status-im/nimbus-eth2/pull/8578)

</details>


<a id="state_cache-228"></a>
<details>
<summary><b>state_cache-228</b> Replay from last block at or before slot — <i>implemented · low · S · cpu, disk</i></summary>

**Idea.** To get a state at a slot, load the state of the last block at or before that slot and advance empty slots, rather than replaying from the latest saved state.

**Impact.** State-by-slot resolves the exact state root (summaries exist for skipped slots) and loads from the nearest snapshot/diff, replaying only blocks after it.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:1087-1110`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1087-L1110)
- [`beacon_node/store/src/hot_cold_store.rs:1124-1186`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1124-L1186)
- [`beacon_node/beacon_chain/src/beacon_chain.rs:1531-1560`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/beacon_chain.rs#L1531-L1560)

**Skeptic check.** Lighthouse never replays from 'the latest saved state'; hot loads use per-slot summaries and hdiff bases, cold loads use hierarchical diffs by slot. Earlier evidence right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#8218](https://github.com/OffchainLabs/prysm/pull/8218)

</details>


<a id="state_cache-229"></a>
<details>
<summary><b>state_cache-229</b> Shared state cache keyed by state root — <i>implemented · low · S · cpu, disk</i></summary>

**Idea.** Keep an in-memory state cache keyed by state root used by block processing, attestation handling and block production to avoid DB reloads.

**Impact.** Block import, attestation shuffling and block production all use the shared state-root-keyed cache.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:82`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L82) StateCache keyed by state root behind a Mutex
- [`beacon_node/store/src/state_cache.rs:275`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L275) get_by_state_root
- [`beacon_node/beacon_chain/src/block_production/mod.rs:89`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/block_production/mod.rs#L89) production uses get_advanced_hot_state
- [`beacon_node/beacon_chain/src/shuffling_cache.rs:400-430`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs#L400-L430) the attestation shuffling path uses the head or cached states

**Skeptic check.** Verified that the StateCache is shared and keyed by state root. The earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar@2b026c147](https://github.com/ChainSafe/lodestar/commit/2b026c147049)

</details>


<a id="state_cache-230"></a>
<details>
<summary><b>state_cache-230</b> Central state regenerator serving all pre-states — <i>partial · low · M · cpu</i></summary>

**Idea.** Centralise pre-state lookup in one regenerator that serves block pre-states, attestation target states and duty states from caches and advances slots only when needed.

**Gap in Lighthouse.** Lookups are spread across the store state cache, shuffling cache, proposer cache and state_advance_timer, not one regenerator; unifying them is a refactor with no direct speedup.

**Impact.** Little speed gain; mostly code structure.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hot_cold_store.rs:1124`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1124) get_advanced_hot_state serves block pre-states
- [`beacon_node/beacon_chain/src/shuffling_cache.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/shuffling_cache.rs) and beacon_proposer_cache.rs serve attestation/duty lookups
- [`beacon_node/beacon_chain/src/state_advance_timer.rs`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/state_advance_timer.rs) pre-advances head state

**Sources.** [lodestar@2b40bb266](https://github.com/ChainSafe/lodestar/commit/2b40bb2668ef)

</details>


<a id="state_cache-231"></a>
<details>
<summary><b>state_cache-231</b> Store states as deltas over a base — <i>implemented · medium · S · disk, memory</i></summary>

**Idea.** Define delta types for validator identity and beacon state so stored states are deltas over a base state.

**Impact.** Already done: hot and cold states are stored as hierarchical diffs over snapshots, including a dedicated validators diff.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/src/hdiff.rs:127`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs#L127) HDiff (state_diff, balances_diff, inactivity_scores_diff, validators diff) over a base buffer
- [`beacon_node/store/src/hdiff.rs:622`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs#L622) default exponents [5,9,11,13,16,18,21]
- [`beacon_node/store/src/hot_cold_store.rs:407`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L407) hot_storage_strategy uses the same hierarchy for hot states
- [`beacon_node/store/src/hot_cold_store.rs:1949`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1949) load_hot_state applies diffs from snapshot

**Skeptic check.** Verified HDiff has per-field deltas including validators and is used for both hot (hot_storage_strategy) and cold DBs. Earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [silver#40](https://github.com/gattaca-com/silver/pull/40), [ethlambda#661](https://github.com/lambdaclass/ethlambda/pull/661)

</details>


<a id="state_cache-232"></a>
<details>
<summary><b>state_cache-232</b> Compact backing-tree layout for balances and validators — <i>n/a · low · L · memory</i></summary>

**Idea.** Change the state backing tree layout for balances and validator branch nodes to use fewer nodes, cutting per-state memory.

**Impact.** Teku-specific backing tree layout; milhouse has its own packed leaves for balances and validators.

**Evidence (Lighthouse @ 928b61e719).**

- Cargo.lock milhouse 0.9.0 (sigp/milhouse): Lighthouse uses its own persistent tree layout, not Teku's

**Sources.** [teku#3286](https://github.com/Consensys-Incorporated/teku/pull/3286), [teku#3287](https://github.com/Consensys-Incorporated/teku/pull/3287)

</details>


<a id="state_cache-233"></a>
<details>
<summary><b>state_cache-233</b> Committee caches embedded in the state — <i>implemented · low · S · memory, cpu</i></summary>

**Idea.** Keep committee/shuffling caches as fields on the state, built explicitly and invalidated per epoch, instead of a separate duplicate cached state.

**Impact.** Committee caches are Arc-shared state fields built explicitly per relative epoch.

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/state/beacon_state.rs:825`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L825)
- [`consensus/types/src/state/beacon_state.rs:1039`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L1039)

**Skeptic check.** Lighthouse's own PR #249 origin; field committee_caches: [Arc&lt;CommitteeCache&gt;; CACHED_EPOCHS] confirmed.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#249](https://github.com/sigp/lighthouse/pull/249)

</details>


<a id="state_cache-234"></a>
<details>
<summary><b>state_cache-234</b> Struct-of-arrays validators with shared pubkey list — <i>partial · medium · M · memory, cpu</i></summary>

**Idea.** Split the validator registry into an append-only pubkey list, effective balances and remaining fields, and share the pubkey list structurally between states so a state loaded from disk attaches it instead of copying every key.

**Gap in Lighthouse.** No struct-of-arrays split: pubkeys stay inline in each Validator leaf. Hot loads share nodes only via rebase_on_finalized (extra tree walk); cold/historic loads (load_cold_state_by_slot -&gt; HDiffBuffer::as_state) build a fresh validators List and are never rebased, so every historical state copies all keys. The chain-level ValidatorPubkeyCache is an append-only pubkey list but is not attached to states. Fix: rebase cold-loaded states on a shared base (e.g. finalized or the historic cache entry) or split pubkeys into a shared Arc list.

**Impact.** Lower memory and load time for historical states (API, reconstruction, historic_state_cache); hot path mostly covered by rebase_on_finalized.

**Best measured result.** saves memory loading historical states (commit:grandine@70e0aad900ad)

**Evidence (Lighthouse @ 928b61e719).**

- [`consensus/types/src/validator/validator.rs:22`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/validator/validator.rs#L22) Validator keeps pubkey: PublicKeyBytes inline in each milhouse leaf
- [`consensus/types/src/state/beacon_state.rs:3416`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L3416) rebase_on shares tree nodes (incl. validators) with a base state
- [`beacon_node/store/src/state_cache.rs:197`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/state_cache.rs#L197) rebase_on_finalized used for hot loads
- [`beacon_node/store/src/hot_cold_store.rs:1988`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L1988) hot load rebases on finalized state
- [`beacon_node/store/src/hot_cold_store.rs:2340`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hot_cold_store.rs#L2340) cold load: buffer.as_state with no rebase
- [`beacon_node/store/src/hdiff.rs:226`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/src/hdiff.rs#L226) as_state rebuilds validators via set_validators_from_iter(cloned)
- [`consensus/types/src/state/beacon_state.rs:2198`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/src/state/beacon_state.rs#L2198) set_validators_from_iter builds a fresh List::try_from_iter
- [`beacon_node/beacon_chain/src/validator_pubkey_cache.rs:24`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/src/validator_pubkey_cache.rs#L24) chain-wide append-only pubkey list exists but is not structurally shared into states

**Second check.** Checked load_cold_state_by_slot and the historic state cache path for any rebase (none in store crate besides hot loads), set_validators_from_iter, and the beacon_chain ValidatorPubkeyCache as a possible equivalent shared pubkey list; it is not shared into state structure.

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [grandine#763](https://github.com/grandinetech/grandine/pull/763), [grandine@70e0aad90](https://github.com/grandinetech/grandine/commit/70e0aad900ad)

</details>


