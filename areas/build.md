# build

59 ideas: 7 not, 10 partial, 18 implemented, 24 n/a; 2 actionable (high or medium value, verdict `not` or `partial`). [Back to the summary](../README.md).

| id | idea | verdict | value | effort | resources |
|---|---|---|---|---|---|
| [build-001](#build-001) | Fat LTO and single codegen unit for release binaries | implemented | medium | S | cpu |
| [build-002](#build-002) | LTO for bundled C crypto libraries | not | low | S | cpu |
| [build-003](#build-003) | Shared jobserver for parallel compile and link | n/a | low |  | memory |
| [build-004](#build-004) | Build blst with ADX/BMI2 instead of portable | implemented | low | S | cpu |
| [build-005](#build-005) **★** | Raise target CPU level for release binaries | partial | medium | M | cpu |
| [build-006](#build-006) | ARM builds with native CPU and crypto extensions | partial | low | S | cpu, sync |
| [build-007](#build-007) | Verify SIMD BLS feature reaches release images | n/a | low | S | cpu |
| [build-008](#build-008) | Container libc must not select slower BLS build | partial | low | S | cpu |
| [build-009](#build-009) | Remote build cache in CI | partial | low | M | cpu |
| [build-010](#build-010) | Rely on compiler cache, drop forced rebuilds | n/a | low |  | cpu |
| [build-011](#build-011) | Native arm runners instead of emulated builds | implemented | low | S | startup |
| [build-012](#build-012) | Avoid dependencies that force native C builds | implemented | low | S | startup |
| [build-013](#build-013) | Code optimization plugins in build transform | n/a | low | S | cpu |
| [build-014](#build-014) | Benchmark alternative build toolchains | n/a | low | S |  |
| [build-015](#build-015) | Build CI binaries once, not twice | not | low | M | cpu |
| [build-016](#build-016) | Upgrade compiler and build tool versions | n/a | low | S | cpu |
| [build-017](#build-017) | Exclude unused embedded genesis states from binary | partial | low | S | disk, memory, startup |
| [build-018](#build-018) | Embed genesis states as raw blobs | implemented | low | S | startup |
| [build-019](#build-019) | Cache derived test fixtures between CI runs | n/a | low | S | cpu, startup |
| [build-020](#build-020) | Enable clippy performance lints in CI | implemented | low | S | cpu, memory |
| [build-021](#build-021) | Struct field ordering lint for padding | n/a | low | S | memory |
| [build-022](#build-022) | Lazy string split iteration | partial | low | S | memory |
| [build-023](#build-023) | Continuous benchmarks on every PR | not | low | S | cpu |
| [build-024](#build-024) | Debug builds for CI targets | partial | low | S | startup |
| [build-025](#build-025) | Optimize test builds | implemented | low | S | startup |
| [build-026](#build-026) | Single dependency version per crate | partial | low | M | startup, disk |
| [build-027](#build-027) | Avoid runtime stack-trace collection overhead | n/a | low | S | cpu |
| [build-028](#build-028) | Disable backtrace library in dev builds | n/a | low | S | startup |
| [build-029](#build-029) | Run spec tests without worker parallelism | n/a | low | S | cpu |
| [build-030](#build-030) | Clean package caches in Docker build layer | implemented | low | S | disk |
| [build-031](#build-031) | Multi-stage Docker build with slim runtime image | implemented | low | S | disk |
| [build-032](#build-032) | Prune dev dependencies from images | n/a | low | S | disk |
| [build-033](#build-033) | No race detector in release images | n/a | low | S | disk |
| [build-034](#build-034) | Trim the Docker build context | partial | low | S | startup |
| [build-035](#build-035) | Prebuilt base images and offline dependency mirror | not | low | S | startup |
| [build-036](#build-036) | Reduce debug info in release builds | implemented | low | S | disk, startup |
| [build-037](#build-037) | Disable unused default features of dependencies | implemented | low | S | startup |
| [build-038](#build-038) | Feature-gate heavy optional components | implemented | low | S | startup |
| [build-039](#build-039) | Remove or slim heavy dependencies | n/a | low | S | startup, memory |
| [build-040](#build-040) | Exclude spec artifacts from test discovery | n/a | low | S | startup |
| [build-041](#build-041) | Faster or self-hosted CI runners | implemented | low | S |  |
| [build-042](#build-042) | Faster linker such as mold | not | low | S |  |
| [build-043](#build-043) | Native download and extract of spec tests | n/a | low | S | startup |
| [build-044](#build-044) | Tar many small files before CI upload | n/a | low | S |  |
| [build-045](#build-045) | Narrow formatter file scope | n/a | low | S | cpu |
| [build-046](#build-046) | Fully optimized compilation mode for releases | implemented | low | S | cpu |
| [build-047](#build-047) | Parallelize CI jobs and pipeline steps | implemented | low | S |  |
| [build-048](#build-048) | Split longest test file for parallel runners | implemented | low | S |  |
| [build-049](#build-049) | Run independent build tasks in parallel | n/a | low | S | startup |
| [build-050](#build-050) | Install prebuilt test tools in CI | n/a | low |  |  |
| [build-051](#build-051) **★** | Profile-guided optimization for release builds | not | medium | L | cpu |
| [build-052](#build-052) | Library update to cut compiler peak memory | n/a | low | S | memory |
| [build-053](#build-053) | Trim per-fork generic helper instantiations | not | low | M | memory |
| [build-054](#build-054) | Shrink validator client dependency graph | partial | low | M | startup |
| [build-055](#build-055) | Correct compiler flags for secp256k1 | implemented | low | S | cpu |
| [build-056](#build-056) | Global semaphore for snapshot builder jobs | n/a | low | S | cpu, memory, disk |
| [build-057](#build-057) | Single integration test binary | implemented | low | S |  |
| [build-058](#build-058) | Generate protobuf code once in shared crate | n/a | low | S | startup |
| [build-059](#build-059) | Bump dependency with cheaper generated-table compile | n/a | low | S | startup |

★ actionable. Click an id for the full record.

## Ideas

<a id="build-001"></a>
<details>
<summary><b>build-001</b> Fat LTO and single codegen unit for release binaries — <i>implemented · medium · S · cpu</i></summary>

**Idea.** Build released binaries with a maximum-performance profile (fat/whole-program LTO, one codegen unit) on every platform and in Docker images, so small hot functions in SSZ hashing, state transition and fork choice inline across crate boundaries. Check the Cargo release profile used by CI, Windows releases and Dockerfiles.

**Impact.** Tagged release binaries (linux x64/arm64, macOS) and tagged Docker images use fat LTO with codegen-units=1. Only unstable images and the source Dockerfile (PROFILE=release) do not.

**Best measured result.** pr:nimbus#1661: 40% faster block replay and hashing; apply epoch block 333ms -&gt; 195ms

**Evidence (Lighthouse @ 928b61e719).**

- Cargo.toml:286-290
- [`.github/workflows/release.yml:38-47`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/.github/workflows/release.yml#L38-L47)
- [`.github/workflows/docker.yml:58-60`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/.github/workflows/docker.yml#L58-L60)

**Skeptic check.** Confirmed all release.yml matrix entries use maxperf and docker.yml selects maxperf for tags. Lighthouse ships no Windows release, so that part is n/a. The earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#1661](https://github.com/status-im/nimbus-eth2/pull/1661), [ethlambda#543](https://github.com/lambdaclass/ethlambda/pull/543), [lighthouse#3608](https://github.com/sigp/lighthouse/pull/3608), [lighthouse#4371](https://github.com/sigp/lighthouse/pull/4371), [lighthouse#4237](https://github.com/sigp/lighthouse/pull/4237)

</details>


<a id="build-002"></a>
<details>
<summary><b>build-002</b> LTO for bundled C crypto libraries — <i>not · low · S · cpu</i></summary>

**Idea.** Compile the bundled C/assembly crypto libraries (BLS, secp256k1) with LTO too (cross-language LTO), so calls between client code and the C library can be inlined and optimized.

**Gap in Lighthouse.** Build blst with clang -flto and use -Clinker-plugin-lto in the maxperf profile (build script env CC/CFLAGS and RUSTFLAGS). Gain limited since blst hot paths are large asm functions called over FFI.

**Impact.** Few percent at most on BLS call overhead; asm kernels cannot be inlined anyway.

**Evidence (Lighthouse @ 928b61e719).**

- Cargo.toml:286 maxperf profile has fat LTO but only Rust LTO; default release profile has no [profile.release] LTO
- [`crypto/bls/Cargo.toml:12`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/crypto/bls/Cargo.toml#L12) blst via cc build, no clang/-flto, no linker-plugin-lto
- Makefile:22,31 PROFILE release

**Sources.** [nimbus#1789](https://github.com/status-im/nimbus-eth2/pull/1789)

</details>


<a id="build-003"></a>
<details>
<summary><b>build-003</b> Shared jobserver for parallel compile and link — <i>n/a · low · memory</i></summary>

**Idea.** Drive the C compile, LTO and link steps from one shared jobserver pool, so build parallelism does not oversubscribe processes and the front-end compiler is not held in memory. This caps peak build RSS.

**Best measured result.** pr:nimbus#2095: peak build RSS 2.30 GB -&gt; 1.48 GB (~35%)

**Evidence (Lighthouse @ 928b61e719).**

- Cargo build uses cargo's jobserver already; no Nim-style C compile step

**Sources.** [nimbus#2066](https://github.com/status-im/nimbus-eth2/pull/2066), [nimbus#2095](https://github.com/status-im/nimbus-eth2/pull/2095)

</details>


<a id="build-004"></a>
<details>
<summary><b>build-004</b> Build blst with ADX/BMI2 instead of portable — <i>implemented · low · S · cpu</i></summary>

**Idea.** Build the BLS library (blst) in its non-portable mode with ADX/BMI2 (mulx/adox/adcx) on amd64, at -O3, for the shipped binaries, instead of the portable fallback. Field arithmetic for signature verification is much faster.

**Impact.** Negligible: portable blst links both the ADX (mulx/adox) and the fallback assembly and selects one at runtime, so ADX hardware gets the fast field arithmetic.

**Evidence (Lighthouse @ 928b61e719).**

- [`lighthouse/Cargo.toml:19-21`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/lighthouse/Cargo.toml#L19-L21)
- [`scripts/ci/build-linux.sh:16`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/scripts/ci/build-linux.sh#L16)
- blst-0.3.17/build.rs:160-213
- blst-0.3.17/blst/build/assembly.S:3-20
- blst-0.3.17/build.rs:237

**Skeptic check.** Confirmed that __BLST_PORTABLE__ builds both assembly variants with runtime dispatch, and that the 'modern' feature (force-adx) exists. blst itself caps opt_level at 2, so -O3 is not available to any build. The earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#12564](https://github.com/OffchainLabs/prysm/pull/12564), [prysm#10567](https://github.com/OffchainLabs/prysm/pull/10567), [nimbus#4914](https://github.com/status-im/nimbus-eth2/pull/4914), [caplin#11144](https://github.com/erigontech/erigon/pull/11144)

</details>


<a id="build-005"></a>
<details>
<summary><b>build-005</b> Raise target CPU level for release binaries — <i>partial · medium · M · cpu</i></summary>

**Idea.** Compile release binaries (or an extra 'modern' variant) for a higher CPU baseline such as x86-64-v3 or -march=native, not baseline x86-64, and make sure the flag reaches dependency crates too. Hashing and crypto code can then use AVX2/BMI/SHA instructions.

**Gap in Lighthouse.** Hot crypto (blst under portable, SHA-256 via sha2/cpufeatures) already dispatches to ADX/SHA-NI/AVX2 at runtime, but all other Rust code is compiled for baseline x86-64 and there is no -modern/x86-64-v3 release or Docker variant. Add an opt-in variant with RUSTFLAGS=-C target-cpu=x86-64-v3 in build-linux.sh/docker.yml.

**Impact.** Small (low single-digit % on non-crypto CPU); crypto hot paths already runtime-dispatched.

**Best measured result.** pr:ethlambda#311: aggregation mean 2310 ms -&gt; 745 ms (3.10x)

**Evidence (Lighthouse @ 928b61e719).**

- [`scripts/ci/build-linux.sh:16`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/scripts/ci/build-linux.sh#L16) release/docker builds force the portable feature
- [`scripts/ci/build-linux.sh:32`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/scripts/ci/build-linux.sh#L32) plain cargo build, no RUSTFLAGS/-C target-cpu
- [`.cargo/config.toml:1`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/.cargo/config.toml#L1) only [env] jemalloc/CXX, no [build] rustflags or target-cpu
- [`lighthouse/Cargo.toml:19`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/lighthouse/Cargo.toml#L19) portable/modern features only switch blst ADX (runtime-dispatched under portable)
- [`.github/workflows/release.yml:64`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/.github/workflows/release.yml#L64) maxperf release built via build-linux.sh (portable, baseline x86-64)
- [`.github/workflows/docker.yml:72`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/.github/workflows/docker.yml#L72) docker images built via the same script, no modern variant

**Second check.** Checked .cargo/config.toml, Cross.toml, Dockerfile, Dockerfile.reproducible, release.yml and docker.yml for rustflags/target-cpu: none; only the blst portable/modern switch exists.

**Verdict history.** partial (checked) → partial (refuted)

**Sources.** [ethlambda#311](https://github.com/lambdaclass/ethlambda/pull/311), [nimbus#726](https://github.com/status-im/nimbus-eth2/pull/726), [nimbus@4d487cea1](https://github.com/status-im/nimbus-eth2/commit/4d487cea1fd2), [nimbus#3162](https://github.com/status-im/nimbus-eth2/pull/3162), [lighthouse#2966](https://github.com/sigp/lighthouse/pull/2966), [prysm#10229](https://github.com/OffchainLabs/prysm/pull/10229), [nimbus#3353](https://github.com/status-im/nimbus-eth2/pull/3353)

</details>


<a id="build-006"></a>
<details>
<summary><b>build-006</b> ARM builds with native CPU and crypto extensions — <i>partial · low · S · cpu, sync</i></summary>

**Idea.** For ARM (e.g. Apple M1) builds, pass the correct CPU target (e.g. -mcpu=apple-a13) so the compiler and BLS library use the ARM crypto/SHA extensions instead of generic code.

**Gap in Lighthouse.** Crypto extensions are used via runtime detection, but no -C target-cpu=apple-m1 style flag is passed for general code. Add RUSTFLAGS in release.yml for the aarch64-apple-darwin job.

**Impact.** Minor; Mac/ARM users only, general-code codegen since crypto is already dispatched.

**Best measured result.** pr:nimbus#3202: stated faster initial sync on M1 (screenshot only)

**Evidence (Lighthouse @ 928b61e719).**

- [`.github/workflows/release.yml:74`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/.github/workflows/release.yml#L74) macOS arm64 built with portable, maxperf, no -mcpu
- [`scripts/ci/build-linux.sh:21`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/scripts/ci/build-linux.sh#L21) aarch64 Linux native, no target-cpu
- blst aarch64 asm and sha2/cpufeatures detect crypto extensions at runtime

**Sources.** [nimbus#3205](https://github.com/status-im/nimbus-eth2/pull/3205), [nimbus#3202](https://github.com/status-im/nimbus-eth2/pull/3202)

</details>


<a id="build-007"></a>
<details>
<summary><b>build-007</b> Verify SIMD BLS feature reaches release images — <i>n/a · low · S · cpu</i></summary>

**Idea.** Check that release binaries and container images really enable the SIMD/assembly BLS feature; a default-features change can silently leave the image on the scalar path. Inspect the built binary for the expected instructions.

**Impact.** Lighthouse uses blst assembly with runtime dispatch in portable builds, so no default-feature switch can silently leave the image on a scalar path (silver's problem was a SIMD-specific Cargo feature).

**Best measured result.** pr:silver#393: binary had 0 vpmadd52 instructions before, 264 after

**Evidence (Lighthouse @ 928b61e719).**

- [`lighthouse/Cargo.toml:19-21`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/lighthouse/Cargo.toml#L19-L21) portable/modern features
- blst-0.3.17/build.rs:160-213 feature/ADX selection

**Sources.** [silver#393](https://github.com/gattaca-com/silver/pull/393)

</details>


<a id="build-008"></a>
<details>
<summary><b>build-008</b> Container libc must not select slower BLS build — <i>partial · low · S · cpu</i></summary>

**Idea.** Check that the container base image (glibc vs musl, runtime version) does not make the native BLS library fall back to a slower implementation than a bare-metal build.

**Gap in Lighthouse.** Release and cross-built binaries use the portable blst build, which is slower than ADX builds; Docker image from Dockerfile depends on build host CPU detection. Consider verifying the published image is not portable-by-accident, or document modern builds.

**Impact.** Portable blst is roughly 10-20% slower on pairing and multiplication than ADX; BLS is a modest share of CPU, so small node-wide effect.

**Evidence (Lighthouse @ 928b61e719).**

- Dockerfile:1,15 builder image is glibc rust:bookworm, default features: blst enables ADX if host detects it (blst-0.3.17/build.rs:203)
- [`.github/workflows/release.yml:74`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/.github/workflows/release.yml#L74) release binaries built with --features portable (no ADX path)
- [`lighthouse/Cargo.toml:19-21`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/lighthouse/Cargo.toml#L19-L21) portable/modern features

**Sources.** [lodestar#7004](https://github.com/ChainSafe/lodestar/pull/7004)

</details>


<a id="build-009"></a>
<details>
<summary><b>build-009</b> Remote build cache in CI — <i>partial · low · M · cpu</i></summary>

**Idea.** Use a shared remote build/compiler cache (Bazel remote cache, sccache) in CI so ephemeral runners reuse compiled artifacts instead of rebuilding unchanged code each run.

**Gap in Lighthouse.** Test CI has a persistent cache (rust-cache on WarpBuild snapshot runners), but sccache (#7873) is no longer configured and release/Docker builds (scripts/ci/build-linux.sh runs in a throwaway container) have no cache. Would need sccache or a mounted cargo cache in that script.

**Impact.** CI wall time only; no mainnet node effect.

**Best measured result.** pr:prysm#236: Travis ~12 min -&gt; ~6 min

**Evidence (Lighthouse @ 928b61e719).**

- [`.github/workflows/test-suite.yml:127`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/.github/workflows/test-suite.yml#L127) Swatinem/rust-cache with warpbuild provider
- [`.github/workflows/test-suite.yml:135`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/.github/workflows/test-suite.yml#L135) sccache --show-stats left over
- [`.cargo/config.toml:1`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/.cargo/config.toml#L1) no rustc-wrapper set any more
- [`.github/workflows/docker.yml:88`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/.github/workflows/docker.yml#L88) buildx without cache-from/cache-to

**Sources.** [prysm#8748](https://github.com/OffchainLabs/prysm/pull/8748), [prysm#2294](https://github.com/OffchainLabs/prysm/pull/2294), [prysm#236](https://github.com/OffchainLabs/prysm/pull/236), [prysm#12108](https://github.com/OffchainLabs/prysm/pull/12108), [lighthouse#7873](https://github.com/sigp/lighthouse/pull/7873)

</details>


<a id="build-010"></a>
<details>
<summary><b>build-010</b> Rely on compiler cache, drop forced rebuilds — <i>n/a · low · cpu</i></summary>

**Idea.** Remove forced full rebuilds from the build scripts and rely on an incremental/compiler cache that keys on command-line flags.

**Evidence (Lighthouse @ 928b61e719).**

- Cargo has its own fingerprinting; no forced rebuild in Makefile

**Sources.** [nimbus#8883](https://github.com/status-im/nimbus-eth2/pull/8883)

</details>


<a id="build-011"></a>
<details>
<summary><b>build-011</b> Native arm runners instead of emulated builds — <i>implemented · low · S · startup</i></summary>

**Idea.** Build arm64 images on native arm runners, or build arch-independent parts on the host and only native parts for the target, instead of compiling everything under QEMU emulation.

**Impact.** CI only; arm64 binaries and images (including reproducible ones) build natively, with no QEMU.

**Best measured result.** pr:lodestar#4369: arm64 build roughly equals npm install time; emulated native build was 12-14 min

**Evidence (Lighthouse @ 928b61e719).**

- [`.github/workflows/release.yml:39-40`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/.github/workflows/release.yml#L39-L40)
- [`.github/workflows/docker.yml:46`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/.github/workflows/docker.yml#L46)
- [`.github/workflows/docker-reproducible.yml:55-58`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/.github/workflows/docker-reproducible.yml#L55-L58)
- [`scripts/ci/build-linux.sh:1-7`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/scripts/ci/build-linux.sh#L1-L7),18-27

**Skeptic check.** Confirmed native ubuntu-24.04-arm runners in release, docker and docker-reproducible workflows, and build-linux.sh builds for the host arch only. The earlier evidence is correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#4369](https://github.com/ChainSafe/lodestar/pull/4369), [lodestar#8821](https://github.com/ChainSafe/lodestar/pull/8821)

</details>


<a id="build-012"></a>
<details>
<summary><b>build-012</b> Avoid dependencies that force native C builds — <i>implemented · low · S · startup</i></summary>

**Idea.** Prefer a pure-language implementation of a small primitive (e.g. keccak) over a large crate/package that pulls in a native C library build.

**Impact.** None for keccak. keccak-asm/sha3-asm appear in Cargo.lock but are not compiled for the host target.

**Evidence (Lighthouse @ 928b61e719).**

- Cargo.lock:5621-5628 keccak-hash depends on tiny-keccak (pure Rust)
- ~/.cargo/registry/src/*/alloy-primitives-1.7.3/Cargo.toml:63 keccak-asm (perl+cc native build) is optional behind asm-keccak
- cargo tree -i keccak-asm on the host target prints nothing, so it is not built

**Skeptic check.** Checked that the native-asm keccak (sha3-asm via cc) does not enter the default Linux build, so keccak stays pure Rust. Other native builds (aws-lc-sys, blst, c-kzg) are large primitives and outside this idea. Earlier evidence was right.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#1054](https://github.com/OffchainLabs/prysm/pull/1054)

</details>


<a id="build-013"></a>
<details>
<summary><b>build-013</b> Code optimization plugins in build transform — <i>n/a · low · S · cpu</i></summary>

**Idea.** Add build-time transform plugins that optimize generated code.

**Impact.** No runtime effect.

**Best measured result.** pr:lodestar#1854: ~1s on mainnet sanity tests

**Evidence (Lighthouse @ 928b61e719).**

- Lighthouse is Rust compiled by rustc; no JS build transform exists

**Sources.** [lodestar#1854](https://github.com/ChainSafe/lodestar/pull/1854)

</details>


<a id="build-014"></a>
<details>
<summary><b>build-014</b> Benchmark alternative build toolchains — <i>n/a · low · S</i></summary>

**Idea.** Measure build time of alternative toolchain configurations before choosing one.

**Impact.** No runtime effect; JS toolchain benchmark.

**Evidence (Lighthouse @ 928b61e719).**

- Cargo workspace; toolchain is fixed (cargo/rustc)

**Sources.** [lodestar#1782](https://github.com/ChainSafe/lodestar/pull/1782)

</details>


<a id="build-015"></a>
<details>
<summary><b>build-015</b> Build CI binaries once, not twice — <i>not · low · M · cpu</i></summary>

**Idea.** In CI, build each binary once with the needed feature set (e.g. trace logging) and reuse it, rather than compiling the same target twice with different flags.

**Gap in Lighthouse.** CI uses separate jobs with distinct profiles; sharing artifacts would need cache/artifact reuse across jobs. No trace-logging duplicate build identified.

**Impact.** CI time only; no runtime effect on a mainnet node.

**Evidence (Lighthouse @ 928b61e719).**

- [`.github/workflows/test-suite.yml:131`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/.github/workflows/test-suite.yml#L131) make test-release, 297 make test-debug (separate jobs, different profiles)
- Makefile:333 lint job builds separately

**Sources.** [nimbus#4092](https://github.com/status-im/nimbus-eth2/pull/4092)

</details>


<a id="build-016"></a>
<details>
<summary><b>build-016</b> Upgrade compiler and build tool versions — <i>n/a · low · S · cpu</i></summary>

**Idea.** Upgrade the compiler and build tool (and its plugins) to newer, faster versions and tune build settings to cut compile and CI time.

**Impact.** None at runtime; pure CI/build housekeeping, Lighthouse already tracks a recent pinned toolchain.

**Evidence (Lighthouse @ 928b61e719).**

- Cargo.toml:286 maxperf profile; Dockerfile:1 rust:1.91.0

**Sources.** [teku#359](https://github.com/Consensys-Incorporated/teku/pull/359), [lodestar#4830](https://github.com/ChainSafe/lodestar/pull/4830), [lodestar#8992](https://github.com/ChainSafe/lodestar/pull/8992)

</details>


<a id="build-017"></a>
<details>
<summary><b>build-017</b> Exclude unused embedded genesis states from binary — <i>partial · low · S · disk, memory, startup</i></summary>

**Idea.** Do not embed genesis states and configs of dead or unused networks into the binary, and gate embedded genesis behind a feature for tools that do not need it. The binary is smaller and loads less data.

**Gap in Lighthouse.** Dead testnets are gone and large ones are downloaded, but mainnet/sepolia/gnosis genesis zips are always embedded and there is no cargo feature to omit them for tools like lcli or boot_node. Add a feature gating the IncludedBytes arms in eth2_config/eth2_network_config.

**Impact.** Slightly smaller binary (a few MiB) for tooling; no effect on beacon node runtime.

**Best measured result.** pr:lighthouse#4038: binary 135MiB -&gt; 103MiB (maxperf)

**Evidence (Lighthouse @ 928b61e719).**

- [`common/eth2_config/src/lib.rs:27`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/eth2_config/src/lib.rs#L27),40,53 holesky/hoodi/chiado genesis fetched by URL
- [`common/eth2_config/src/lib.rs:314-342`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/eth2_config/src/lib.rs#L314-L342) mainnet/sepolia/gnosis still IncludedBytes
- [`common/eth2_network_config/Cargo.toml:9`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/eth2_network_config/Cargo.toml#L9) only feature is spec-minimal

**Sources.** [prysm#12244](https://github.com/OffchainLabs/prysm/pull/12244), [lighthouse#4038](https://github.com/sigp/lighthouse/pull/4038)

</details>


<a id="build-018"></a>
<details>
<summary><b>build-018</b> Embed genesis states as raw blobs — <i>implemented · low · S · startup</i></summary>

**Idea.** Embed genesis states as raw byte blobs (incbin/include_bytes) instead of compile-time constants, which are very slow to compile under LTO.

**Impact.** None; genesis is a raw byte blob, not a compile-time constant.

**Evidence (Lighthouse @ 928b61e719).**

- [`common/eth2_config/src/lib.rs:188-196`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/eth2_config/src/lib.rs#L188-L196) include_bytes! macro embeds per-network files
- [`common/eth2_config/src/lib.rs:314`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/eth2_config/src/lib.rs#L314),323,342 GenesisStateSource::IncludedBytes
- [`common/eth2_config/src/lib.rs:27`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/eth2_config/src/lib.rs#L27),40,53 testnets fetch genesis by Url instead of embedding
- [`common/eth2_network_config/build.rs:52`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/eth2_network_config/build.rs#L52) unzips genesis.ssz.zip for include_bytes

**Skeptic check.** Confirmed that genesis states are embedded with include_bytes! as raw bytes, and some networks download theirs by URL. The earlier evidence cited the doc comment in eth2_network_config. The actual macro is in common/eth2_config/src/lib.rs.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#4905](https://github.com/status-im/nimbus-eth2/pull/4905)

</details>


<a id="build-019"></a>
<details>
<summary><b>build-019</b> Cache derived test fixtures between CI runs — <i>n/a · low · S · cpu, startup</i></summary>

**Idea.** Cache expensive deterministic test fixtures (e.g. interop validator pubkeys) between CI runs, keyed by OS, lockfile and helper version, so tests do not regenerate them.

**Impact.** Lighthouse tests use fixed hard-coded keypairs rather than generating interop keys per run; CI cache gain is minor.

**Best measured result.** pr:lodestar#9906: phase0 test 75.7s -&gt; 46.9s (38.1%)

**Evidence (Lighthouse @ 928b61e719).**

- Makefile:184 test-debug
- [`testing/ef_tests`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/testing/ef_tests)

**Sources.** [lodestar#9906](https://github.com/ChainSafe/lodestar/pull/9906)

</details>


<a id="build-020"></a>
<details>
<summary><b>build-020</b> Enable clippy performance lints in CI — <i>implemented · low · S · cpu, memory</i></summary>

**Idea.** Enable clippy's performance lint group in CI so needless clones and allocations are caught.

**Impact.** CI-only; needless clones/allocations flagged by the perf group fail CI.

**Evidence (Lighthouse @ 928b61e719).**

- Makefile:331-344 lint target runs cargo clippy with -D warnings (clippy::perf is warn-by-default, so it becomes fatal)
- Makefile:351-356 lint-full/lint-spec-minimal call lint
- [`.github/workflows/test-suite.yml:436-438`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/.github/workflows/test-suite.yml#L436-L438) CI runs make lint-full and lint-spec-minimal

**Skeptic check.** Verified the lint target denies all warnings and is run in CI, and no -A flag disables any perf lint. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#1286](https://github.com/sigp/lighthouse/pull/1286)

</details>


<a id="build-021"></a>
<details>
<summary><b>build-021</b> Struct field ordering lint for padding — <i>n/a · low · S · memory</i></summary>

**Idea.** Add a static check that orders struct fields to minimise padding, so hot structs use less memory.

**Impact.** Rust already minimises padding for default repr; only repr(C) structs matter and are rare.

**Evidence (Lighthouse @ 928b61e719).**

- rustc reorders fields of repr(Rust) structs automatically to minimise padding

**Sources.** [prysm#5296](https://github.com/OffchainLabs/prysm/pull/5296)

</details>


<a id="build-022"></a>
<details>
<summary><b>build-022</b> Lazy string split iteration — <i>partial · low · S · memory</i></summary>

**Idea.** Iterate string splits lazily in loops instead of allocating an intermediate collection.

**Gap in Lighthouse.** Only one eager split-collect in beacon_node/common/consensus (topics.rs parse of gossip topics); could use iterator/ splitn without Vec in the topic decode function.

**Impact.** Saves one small Vec allocation per received gossip message; negligible.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/lighthouse_network/src/types/topics.rs:266`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/src/types/topics.rs#L266) topic.split('/').collect::&lt;Vec&lt;&amp;str&gt;&gt;()

**Sources.** [prysm#15870](https://github.com/OffchainLabs/prysm/pull/15870)

</details>


<a id="build-023"></a>
<details>
<summary><b>build-023</b> Continuous benchmarks on every PR — <i>not · low · S · cpu</i></summary>

**Idea.** Run the existing criterion benchmarks in CI on every PR under a deterministic CPU simulator (e.g. CodSpeed), so performance regressions are reported automatically.

**Gap in Lighthouse.** Add a CodSpeed (or similar) workflow running the criterion benches on PRs.

**Impact.** No runtime effect; only catches regressions in CI.

**Evidence (Lighthouse @ 928b61e719).**

- Makefile:206 check-benches only typechecks benches
- /.github/workflows/test-suite.yml:441 typecheck benchmark code without running it

**Sources.** [grandine#988](https://github.com/grandinetech/grandine/pull/988)

</details>


<a id="build-024"></a>
<details>
<summary><b>build-024</b> Debug builds for CI targets — <i>partial · low · S · startup</i></summary>

**Idea.** Build CI test targets in debug mode instead of release to cut compile time.

**Gap in Lighthouse.** Only the debug-tests-ubuntu job is a debug build. The compile-with-beta-compiler job runs `make` (PROFILE=release) only to check that the code compiles, and cli-check builds a release binary only to run --help. Both could be debug builds or `cargo check`. The test jobs (test-release, test-beacon-chain, test-network, ef tests) need release for run time, so they are out of scope.

**Impact.** CI wall time only: removes release-optimised compiles from two jobs that never run the binary under load.

**Best measured result.** pr:nimbus#4655: build time 25 -&gt; 15 minutes

**Evidence (Lighthouse @ 928b61e719).**

- [`.github/workflows/test-suite.yml:277-297`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/.github/workflows/test-suite.yml#L277-L297)
- Makefile:183-186
- [`.github/workflows/test-suite.yml:491-503`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/.github/workflows/test-suite.yml#L491-L503)
- Makefile:20-30
- [`.github/workflows/test-suite.yml:504-517`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/.github/workflows/test-suite.yml#L504-L517)
- Makefile:320-321

**Skeptic check.** The earlier evidence (the debug-tests job) is real, but the nimbus change was about building all targets whose output is never benchmarked in debug. Lighthouse still does release builds in the beta-compiler and cli-check jobs.

**Verdict history.** implemented (checked) → partial (skeptic)

**Sources.** [nimbus#4655](https://github.com/status-im/nimbus-eth2/pull/4655)

</details>


<a id="build-025"></a>
<details>
<summary><b>build-025</b> Optimize test builds — <i>implemented · low · S · startup</i></summary>

**Idea.** Compile test binaries with optimization so heavy tests run faster and the total build+test cycle is shorter.

**Impact.** Test cycle only; no runtime effect.

**Evidence (Lighthouse @ 928b61e719).**

- Makefile:176-179 test-release runs cargo nextest --release
- Makefile:228-235 ef_tests and beacon_chain per-fork tests run with --release
- Makefile:310 default test target is test-release

**Skeptic check.** Heavy suites (workspace, ef_tests, beacon_chain per fork) all build in release. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#189](https://github.com/status-im/nimbus-eth2/pull/189)

</details>


<a id="build-026"></a>
<details>
<summary><b>build-026</b> Single dependency version per crate — <i>partial · low · M · startup, disk</i></summary>

**Idea.** Keep a single version of each shared dependency in the tree so duplicate code is not compiled twice and the binary is smaller.

**Gap in Lighthouse.** Dedupe remaining duplicate versions via cargo tree -d and dependency bumps; mostly blocked by upstream crates.

**Impact.** Slightly smaller binary and faster compile; no measurable runtime gain.

**Evidence (Lighthouse @ 928b61e719).**

- Cargo.lock still has ~95 crates with multiple versions (e.g. base64, hashbrown, indexmap, itertools, nix)
- Cargo.toml:296 patch.crates-io section

**Sources.** [prysm#1155](https://github.com/OffchainLabs/prysm/pull/1155), [lighthouse#8452](https://github.com/sigp/lighthouse/pull/8452)

</details>


<a id="build-027"></a>
<details>
<summary><b>build-027</b> Avoid runtime stack-trace collection overhead — <i>n/a · low · S · cpu</i></summary>

**Idea.** Do not pay for runtime stack-trace collection in shipped builds (or for two stack-trace mechanisms at once); it slowed execution heavily on some platforms.

**Impact.** Nim-specific stack trace machinery; Rust release builds do not collect traces unless a panic occurs.

**Best measured result.** pr:nimbus#3466: title claims 66% better performance

**Evidence (Lighthouse @ 928b61e719).**

- Cargo.toml:286-294 release profiles carry no backtrace machinery

**Sources.** [nimbus#8625](https://github.com/status-im/nimbus-eth2/pull/8625), [nimbus#3466](https://github.com/status-im/nimbus-eth2/pull/3466)

</details>


<a id="build-028"></a>
<details>
<summary><b>build-028</b> Disable backtrace library in dev builds — <i>n/a · low · S · startup</i></summary>

**Idea.** Disable the backtrace library in development builds to shorten compilation.

**Impact.** Nim backtrace library; no equivalent in Rust builds.

**Best measured result.** pr:nimbus#1686: compilation 3.31% faster

**Evidence (Lighthouse @ 928b61e719).**

- Cargo.toml:286-294 profiles

**Sources.** [nimbus#1686](https://github.com/status-im/nimbus-eth2/pull/1686)

</details>


<a id="build-029"></a>
<details>
<summary><b>build-029</b> Run spec tests without worker parallelism — <i>n/a · low · S · cpu</i></summary>

**Idea.** Run spec tests in a single process if worker-pool overhead exceeds the parallel gain.

**Impact.** JS spec test runner worker pool; Lighthouse uses nextest with process-per-test.

**Evidence (Lighthouse @ 928b61e719).**

- Makefile:176-195 uses cargo nextest

**Sources.** [lodestar#4776](https://github.com/ChainSafe/lodestar/pull/4776)

</details>


<a id="build-030"></a>
<details>
<summary><b>build-030</b> Clean package caches in Docker build layer — <i>implemented · low · S · disk</i></summary>

**Idea.** Delete the package registry and build caches in the same Docker layer that builds the binary, so they do not end up in the image.

**Impact.** Image size only.

**Evidence (Lighthouse @ 928b61e719).**

- Dockerfile:13-16 cargo registry and target dir are BuildKit cache mounts, not image layers
- Dockerfile:18-24 final ubuntu stage copies only the lighthouse binary and cleans apt lists in the same RUN

**Skeptic check.** The multi-stage build keeps build caches out of the final image, and the apt cache is deleted in the same layer. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#735](https://github.com/sigp/lighthouse/pull/735)

</details>


<a id="build-031"></a>
<details>
<summary><b>build-031</b> Multi-stage Docker build with slim runtime image — <i>implemented · low · S · disk</i></summary>

**Idea.** Use a multi-stage Dockerfile so the runtime image is a minimal base with only the binary, not the toolchain.

**Impact.** Image size only.

**Best measured result.** pr:lighthouse#749: Docker image 1.8gb -&gt; 138mb

**Evidence (Lighthouse @ 928b61e719).**

- Dockerfile:1 rust builder stage
- Dockerfile:18-24 ubuntu:24.04 runtime with only libssl/ca-certificates and the copied lighthouse binary

**Skeptic check.** Verified the Dockerfile is two-stage and the runtime stage copies only /usr/local/cargo/bin/lighthouse; earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#749](https://github.com/sigp/lighthouse/pull/749), [lodestar#354](https://github.com/ChainSafe/lodestar/pull/354), [teku#10290](https://github.com/Consensys-Incorporated/teku/pull/10290)

</details>


<a id="build-032"></a>
<details>
<summary><b>build-032</b> Prune dev dependencies from images — <i>n/a · low · S · disk</i></summary>

**Idea.** Prune dev-only dependencies from container and binary builds.

**Impact.** JS dev dependency pruning; the Rust multi-stage image contains no dev dependencies.

**Best measured result.** pr:lodestar#8765: image and binary size had doubled (2x)

**Evidence (Lighthouse @ 928b61e719).**

- Dockerfile:18-25 final image copies only the lighthouse binary

**Sources.** [lodestar#8765](https://github.com/ChainSafe/lodestar/pull/8765)

</details>


<a id="build-033"></a>
<details>
<summary><b>build-033</b> No race detector in release images — <i>n/a · low · S · disk</i></summary>

**Idea.** Do not build release container binaries with the race detector or similar instrumentation.

**Impact.** Go race detector has no Rust equivalent in release builds.

**Best measured result.** pr:prysm#1215: 49Mb -&gt; 42Mb

**Evidence (Lighthouse @ 928b61e719).**

- Makefile, Dockerfile: no race-detector or sanitizer flags

**Sources.** [prysm#1215](https://github.com/OffchainLabs/prysm/pull/1215)

</details>


<a id="build-034"></a>
<details>
<summary><b>build-034</b> Trim the Docker build context — <i>partial · low · S · startup</i></summary>

**Idea.** Exclude large spec-test and artifact directories from the Docker build context (.dockerignore), so builds copy less.

**Gap in Lighthouse.** Spec tests and target/ are excluded; other large dirs (e.g. book, .git) are not. Add them to .dockerignore.

**Impact.** Marginally faster docker build context transfer.

**Best measured result.** pr:lodestar#10102: excludes a 4.6 GB directory

**Evidence (Lighthouse @ 928b61e719).**

- .dockerignore:1-2 excludes consensus-spec-tests and execution_clients
- Dockerfile:12 COPY . .

**Sources.** [lodestar#10102](https://github.com/ChainSafe/lodestar/pull/10102)

</details>


<a id="build-035"></a>
<details>
<summary><b>build-035</b> Prebuilt base images and offline dependency mirror — <i>not · low · S · startup</i></summary>

**Idea.** Speed up container builds with base images that already contain the build tooling and an offline dependency mirror, so each build does not install and download them.

**Gap in Lighthouse.** Builder stage installs cmake/clang each build and uses stock rust image; publish a prebuilt builder base image with tooling (and vendored deps). Registry cache mount already exists.

**Impact.** Saves tens of seconds of CI image build; none on node runtime.

**Best measured result.** pr:lodestar#6787: docker build 5m22s -&gt; 3m16s

**Evidence (Lighthouse @ 928b61e719).**

- Dockerfile:2 apt-get install per build
- Dockerfile:12-14 uses cargo cache mounts for registry/target only

**Sources.** [lodestar#6787](https://github.com/ChainSafe/lodestar/pull/6787)

</details>


<a id="build-036"></a>
<details>
<summary><b>build-036</b> Reduce debug info in release builds — <i>implemented · low · S · disk, startup</i></summary>

**Idea.** Emit reduced or no debug info in the release profile (e.g. line tables only), so binaries are about half the size and link faster while keeping backtraces.

**Impact.** Release binaries carry no debug info.

**Best measured result.** pr:nimbus#2602: 165MB -&gt; 87MB binary

**Evidence (Lighthouse @ 928b61e719).**

- Cargo.toml:286-290 maxperf inherits release, no debug key
- Cargo.toml:292-294 release-debug opt-in debug=true
- no [profile.release] section, so cargo default debug=0

**Skeptic check.** The LH commit removed [profile.release] debug=true and no release profile now sets debug, so release has debug=0. LH goes further than line-tables-only (backtraces lose line numbers), but the size and link-time effect is achieved.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse@77ac49a55](https://github.com/sigp/lighthouse/commit/77ac49a5536c), [nimbus#2602](https://github.com/status-im/nimbus-eth2/pull/2602), [nimbus@73e9448a1](https://github.com/status-im/nimbus-eth2/commit/73e9448a1a32), [prysm#15774](https://github.com/OffchainLabs/prysm/pull/15774)

</details>


<a id="build-037"></a>
<details>
<summary><b>build-037</b> Disable unused default features of dependencies — <i>implemented · low · S · startup</i></summary>

**Idea.** Turn off unused default features of dependencies (e.g. bundled Snappy in LevelDB) so their bundled C/C++ libraries are not compiled.

**Impact.** Compile time only.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store/Cargo.toml:22`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/Cargo.toml#L22) leveldb 0.8.6 with default-features = false
- ~/.cargo/registry/src/*/leveldb-0.8.6/Cargo.toml:42 default = [leveldb-sys/snappy], which is so disabled
- only [`beacon_node/store`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store) depends on leveldb

**Skeptic check.** Confirmed that the leveldb default feature is bundled snappy, and that the only dependent disables it. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#7235](https://github.com/sigp/lighthouse/pull/7235)

</details>


<a id="build-038"></a>
<details>
<summary><b>build-038</b> Feature-gate heavy optional components — <i>implemented · low · S · startup</i></summary>

**Idea.** Put heavy optional components (slasher backends, kafka) behind cargo features that are off or removable, so normal builds skip compiling them.

**Impact.** Compile time and binary size only.

**Evidence (Lighthouse @ 928b61e719).**

- [`lighthouse/Cargo.toml:15-35`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/lighthouse/Cargo.toml#L15-L35) slasher-mdbx/lmdb/redb and beacon-node-leveldb/redb are cargo features; only lmdb and leveldb are default
- [`slasher/Cargo.toml:9-35`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/slasher/Cargo.toml#L9-L35) backends are optional deps
- [`beacon_node/store/Cargo.toml:8-9`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store/Cargo.toml#L8-L9) leveldb feature

**Skeptic check.** Slasher and DB backends are optional features, and LH has no kafka-type component. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#4638](https://github.com/OffchainLabs/prysm/pull/4638), [lighthouse#3888](https://github.com/sigp/lighthouse/pull/3888)

</details>


<a id="build-039"></a>
<details>
<summary><b>build-039</b> Remove or slim heavy dependencies — <i>n/a · low · S · startup, memory</i></summary>

**Idea.** Remove unused heavy dependencies and replace whole libraries with the small sub-package actually used, to cut build/install time, footprint and startup.

**Impact.** Build/CI-only or other-language tooling; no runtime effect on a Lighthouse node.

**Evidence (Lighthouse @ 928b61e719).**

- Cargo.toml: Rust workspace

**Sources.** [lodestar#2324](https://github.com/ChainSafe/lodestar/pull/2324), [teku#10038](https://github.com/Consensys-Incorporated/teku/pull/10038), [lodestar@4ad860e2a](https://github.com/ChainSafe/lodestar/commit/4ad860e2a4b4), [prysm#16116](https://github.com/OffchainLabs/prysm/pull/16116)

</details>


<a id="build-040"></a>
<details>
<summary><b>build-040</b> Exclude spec artifacts from test discovery — <i>n/a · low · S · startup</i></summary>

**Idea.** Exclude large spec-test artifact directories from the test runner's file scanning.

**Impact.** Build/CI-only or other-language tooling; no runtime effect on a Lighthouse node.

**Evidence (Lighthouse @ 928b61e719).**

- Rust tests run via cargo/nextest

**Sources.** [lodestar#6817](https://github.com/ChainSafe/lodestar/pull/6817)

</details>


<a id="build-041"></a>
<details>
<summary><b>build-041</b> Faster or self-hosted CI runners — <i>implemented · low · S</i></summary>

**Idea.** Run CI on faster or self-hosted runners with a fallback to hosted runners.

**Impact.** CI wall time only.

**Best measured result.** pr:lodestar#5079: total CI 27m -&gt; 17m (-37%)

**Evidence (Lighthouse @ 928b61e719).**

- [`.github/workflows/test-suite.yml:108`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/.github/workflows/test-suite.yml#L108),140,162,281,316,338,404 warp-ubuntu-latest-x64-8x on sigp/lighthouse, else ubuntu-latest

**Skeptic check.** Heavy jobs use WarpBuild 8x runners with a hosted fallback for forks; earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#5079](https://github.com/ChainSafe/lodestar/pull/5079), [lighthouse#4506](https://github.com/sigp/lighthouse/pull/4506)

</details>


<a id="build-042"></a>
<details>
<summary><b>build-042</b> Faster linker such as mold — <i>not · low · S</i></summary>

**Idea.** Use a faster linker (mold/lld) in CI and dev builds to cut link time.

**Gap in Lighthouse.** Add a linker setting (mold or lld) in .cargo/config.toml or CI RUSTFLAGS; the PR's change appears removed or never present.

**Impact.** Only dev and CI link time; no runtime gain on a node.

**Evidence (Lighthouse @ 928b61e719).**

- [`.cargo/config.toml:1-14`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/.cargo/config.toml#L1-L14) sets only jemalloc env and CXX=clang++, no linker/rustflags
- Makefile, .github: grep for mold/lld finds nothing

**Sources.** [lighthouse#3359](https://github.com/sigp/lighthouse/pull/3359)

</details>


<a id="build-043"></a>
<details>
<summary><b>build-043</b> Native download and extract of spec tests — <i>n/a · low · S · startup</i></summary>

**Idea.** Download and extract spec-test archives with native fetch/tar instead of slower library code.

**Impact.** Build/CI-only or other-language tooling; no runtime effect on a Lighthouse node.

**Evidence (Lighthouse @ 928b61e719).**

- Spec test download is a Makefile/Rust step, not JS fetch

**Sources.** [lodestar#7816](https://github.com/ChainSafe/lodestar/pull/7816)

</details>


<a id="build-044"></a>
<details>
<summary><b>build-044</b> Tar many small files before CI upload — <i>n/a · low · S</i></summary>

**Idea.** Bundle many small files (e.g. reference-test data) into one tar before uploading as a CI artifact.

**Impact.** Build/CI-only or other-language tooling; no runtime effect on a Lighthouse node.

**Best measured result.** pr:teku#10460: saves around 14 minutes in referenceTestsPrep

**Evidence (Lighthouse @ 928b61e719).**

- CI artifact upload specific to Teku

**Sources.** [teku#10460](https://github.com/Consensys-Incorporated/teku/pull/10460)

</details>


<a id="build-045"></a>
<details>
<summary><b>build-045</b> Narrow formatter file scope — <i>n/a · low · S · cpu</i></summary>

**Idea.** Exclude resource and data folders from the formatter's file scope so it scans far fewer files.

**Impact.** No runtime effect; cargo fmt only visits files reachable from crate roots.

**Best measured result.** pr:teku#1742: format 4 min -&gt; 30 sec

**Evidence (Lighthouse @ 928b61e719).**

- rustfmt.toml:1 - only edition set; cargo fmt walks Rust module tree, not data dirs

**Sources.** [teku#1742](https://github.com/Consensys-Incorporated/teku/pull/1742)

</details>


<a id="build-046"></a>
<details>
<summary><b>build-046</b> Fully optimized compilation mode for releases — <i>implemented · low · S · cpu</i></summary>

**Idea.** Build release binaries with full optimization instead of the build tool's fast unoptimized default mode.

**Impact.** Release binaries are already fully optimized.

**Best measured result.** pr:prysm#5033: ProcessEpoch 45.1ms -&gt; 38.8ms/op

**Evidence (Lighthouse @ 928b61e719).**

- Makefile:31 PROFILE ?= release
- Dockerfile:4 PROFILE=release
- Cargo.toml has no [profile.release] override, so the default opt-level=3 applies
- Cargo.toml:286-290 maxperf profile with fat LTO and codegen-units=1

**Skeptic check.** make and Docker build with the release profile, and the profile is not weakened. The earlier evidence was correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [prysm#5033](https://github.com/OffchainLabs/prysm/pull/5033), [nimbus@20a016580](https://github.com/status-im/nimbus-eth2/commit/20a016580994)

</details>


<a id="build-047"></a>
<details>
<summary><b>build-047</b> Parallelize CI jobs and pipeline steps — <i>implemented · low · S</i></summary>

**Idea.** Structure the CI pipeline so independent jobs (test suites, spec extraction, image build) run in parallel after a shared build, gated only on what they really need.

**Impact.** CI wall time only.

**Evidence (Lighthouse @ 928b61e719).**

- [`.github/workflows/test-suite.yml:106-540`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/.github/workflows/test-suite.yml#L106-L540) every job needs only check-labels and runs in parallel
- [`.github/workflows/test-suite.yml:556-580`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/.github/workflows/test-suite.yml#L556-L580) test-suite-success gate job

**Skeptic check.** Jobs fan out in parallel and are gated only on check-labels. There is no shared build artifact (each job compiles with cache), but the parallelism the idea is about is present.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#1713](https://github.com/ChainSafe/lodestar/pull/1713), [teku#1833](https://github.com/Consensys-Incorporated/teku/pull/1833), [teku#1989](https://github.com/Consensys-Incorporated/teku/pull/1989), [teku#2043](https://github.com/Consensys-Incorporated/teku/pull/2043)

</details>


<a id="build-048"></a>
<details>
<summary><b>build-048</b> Split longest test file for parallel runners — <i>implemented · low · S</i></summary>

**Idea.** Split the longest test file so the parallel test runner can distribute it across workers.

**Impact.** CI wall time only.

**Best measured result.** pr:lodestar#1719: step 2-3 min shorter

**Evidence (Lighthouse @ 928b61e719).**

- Makefile:176-179 cargo nextest runs each test in its own process, so it schedules per test and not per file
- Makefile:233-235 beacon_chain tests split per fork into separate jobs

**Skeptic check.** nextest gives the per-test distribution that the lodestar file split was used to get. The earlier evidence was correct in effect.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lodestar#1719](https://github.com/ChainSafe/lodestar/pull/1719)

</details>


<a id="build-049"></a>
<details>
<summary><b>build-049</b> Run independent build tasks in parallel — <i>n/a · low · S · startup</i></summary>

**Idea.** Run independent build tasks (code build, type/declaration generation) in parallel.

**Impact.** No separate declaration-generation step in Rust; no runtime effect.

**Evidence (Lighthouse @ 928b61e719).**

- Cargo.toml - Rust workspace; cargo builds independent crates in parallel

**Sources.** [lodestar@92e8ec81b](https://github.com/ChainSafe/lodestar/commit/92e8ec81bcdf), [lodestar#1794](https://github.com/ChainSafe/lodestar/pull/1794)

</details>


<a id="build-050"></a>
<details>
<summary><b>build-050</b> Install prebuilt test tools in CI — <i>n/a · low</i></summary>

**Idea.** Install prebuilt binaries of test tooling (e.g. anvil) in CI instead of compiling them from source each run.

**Impact.** Lighthouse CI no longer builds or installs anvil, so nothing to speed up.

**Best measured result.** pr:lighthouse#4505: ~10 min source build -&gt; ~2 s install

**Evidence (Lighthouse @ 928b61e719).**

- grep for anvil/foundry in .github, Makefile, testing/*/Cargo.toml: no hits

**Sources.** [lighthouse#4505](https://github.com/sigp/lighthouse/pull/4505)

</details>


<a id="build-051"></a>
<details>
<summary><b>build-051</b> Profile-guided optimization for release builds — <i>not · medium · L · cpu</i></summary>

**Idea.** Build release binaries with profile-guided optimization from a CPU profile of a live beacon node, behind a release flag, and refresh the profile periodically.

**Gap in Lighthouse.** No PGO or BOLT anywhere. Add -Cprofile-generate/-Cprofile-use (or cargo-pgo) with a .profdata collected from a live beacon node to the tag build in build-linux.sh, refreshed per release.

**Impact.** Prysm measured ~2% CPU; expect low single-digit % lower CPU, at the cost of profile upkeep and reproducibility.

**Best measured result.** pr:prysm#13035: 2.19% CPU improvement

**Evidence (Lighthouse @ 928b61e719).**

- Cargo.toml:286 profiles only maxperf (fat LTO, codegen-units=1) and release-debug, no PGO
- [`scripts/ci/build-linux.sh:32`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/scripts/ci/build-linux.sh#L32) plain cargo build without -Cprofile-use
- [`.github/workflows/release.yml:41`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/.github/workflows/release.yml#L41) release uses maxperf profile, no instrumented/PGO step

**Second check.** Repo-wide grep (excluding target/.git) for profile-generate, profile-use, profdata, cargo-pgo, llvm-bolt found nothing; maxperf LTO is the only extra release optimization.

**Verdict history.** not (checked) → not (refuted)

**Sources.** [prysm#13035](https://github.com/OffchainLabs/prysm/pull/13035), [prysm#13158](https://github.com/OffchainLabs/prysm/pull/13158), [prysm#14589](https://github.com/OffchainLabs/prysm/pull/14589)

</details>


<a id="build-052"></a>
<details>
<summary><b>build-052</b> Library update to cut compiler peak memory — <i>n/a · low · S · memory</i></summary>

**Idea.** Update a heavy generic library to a version that lowers compiler peak RSS when building the beacon node.

**Impact.** Compiler memory is not a node runtime concern; Rust crates have no equivalent known hotspot here.

**Best measured result.** pr:nimbus#9115: compiler peak RSS 11GB -&gt; 8GB

**Evidence (Lighthouse @ 928b61e719).**

- Cargo.toml:286-294 - Rust build, no Nim generics

**Sources.** [nimbus#9115](https://github.com/status-im/nimbus-eth2/pull/9115)

</details>


<a id="build-053"></a>
<details>
<summary><b>build-053</b> Trim per-fork generic helper instantiations — <i>not · low · M · memory</i></summary>

**Idea.** Reduce code generated per fork by trimming generic debug/helper functions monomorphized for every fork type, cutting compile time and compiler memory.

**Gap in Lighthouse.** Would need to measure monomorphization (cargo llvm-lines) of types/state_processing and drop or dyn-ify debug helpers instantiated per fork and per EthSpec.

**Impact.** Slightly faster Lighthouse builds and lower compiler RSS; no runtime effect.

**Best measured result.** pr:nimbus#9108: peak RSS 6.0GB -&gt; 5.1GB; wall 1034s -&gt; 912s (-12%)

**Evidence (Lighthouse @ 928b61e719).**

- No per-fork debug/helper generics audit found; [`consensus/types`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types) uses superstruct per-fork types with generic E everywhere

**Sources.** [nimbus#9108](https://github.com/status-im/nimbus-eth2/pull/9108), [lighthouse#1989](https://github.com/sigp/lighthouse/pull/1989)

</details>


<a id="build-054"></a>
<details>
<summary><b>build-054</b> Shrink validator client dependency graph — <i>partial · low · M · startup</i></summary>

**Idea.** Keep the validator client from depending on the heavy beacon-node crates: move shared constants and API-client code to lightweight crates so the VC compiles fewer crates.

**Gap in Lighthouse.** VC already avoids beacon_chain, store and lighthouse_network, but eth2 still pulls fork_choice (and via it proto_array/state_processing) plus heavy types. Move fork-choice API types out of eth2 into a lighter crate.

**Impact.** Faster VC-only builds; no runtime effect.

**Best measured result.** pr:nimbus#4825: removes &gt;1000 transitive imports building VC

**Evidence (Lighthouse @ 928b61e719).**

- [`validator_client/Cargo.toml:12-40`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/validator_client/Cargo.toml#L12-L40) VC deps are separate light crates, no beacon_chain/store/network
- [`common/eth2/Cargo.toml:25`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/eth2/Cargo.toml#L25) eth2 depends unconditionally on fork_choice
- [`common/eth2/Cargo.toml:10`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/common/eth2/Cargo.toml#L10) lighthouse feature adds proto_array

**Sources.** [nimbus#4825](https://github.com/status-im/nimbus-eth2/pull/4825), [prysm#14871](https://github.com/OffchainLabs/prysm/pull/14871)

</details>


<a id="build-055"></a>
<details>
<summary><b>build-055</b> Correct compiler flags for secp256k1 — <i>implemented · low · S · cpu</i></summary>

**Idea.** Check the compiler flags used for the bundled secp256k1 library (frame-pointer settings) do not cause slow or wrong code.

**Impact.** No slow-code risk found.

**Evidence (Lighthouse @ 928b61e719).**

- Cargo.lock:8948-8959 secp256k1-sys 0.10.1 and 0.11.0
- ~/.cargo/registry/src/*/secp256k1-sys-0.11.0/build.rs:22-23 only warning-suppression flags, no frame-pointer or optimization overrides

**Skeptic check.** The cc build inherits cargo's opt level and sets no frame-pointer flags. The earlier evidence was right, but it missed the 0.10.1 copy, which uses the same build pattern.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [nimbus#6402](https://github.com/status-im/nimbus-eth2/pull/6402)

</details>


<a id="build-056"></a>
<details>
<summary><b>build-056</b> Global semaphore for snapshot builder jobs — <i>n/a · low · S · cpu, memory, disk</i></summary>

**Idea.** Share one semaphore across all snapshot/archive builders so only a bounded number of heavy build jobs run concurrently.

**Impact.** Lighthouse has no snapshot-file builder pool to bound.

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/store`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/store) - no snapshot builder jobs; no archive/snapshot file builders in Lighthouse

**Sources.** [caplin#9085](https://github.com/erigontech/erigon/pull/9085)

</details>


<a id="build-057"></a>
<details>
<summary><b>build-057</b> Single integration test binary — <i>implemented · low · S</i></summary>

**Idea.** Disable auto-discovery of integration test files so all tests link into one binary, cutting link and compile time.

**Impact.** Faster test builds only.

**Best measured result.** pr:lighthouse#2658: build 1m19s -&gt; 43.5s

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/Cargo.toml:7`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/Cargo.toml#L7) autotests=false with tests/main.rs
- [`beacon_node/http_api/Cargo.toml:6`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/Cargo.toml#L6)
- [`lighthouse/Cargo.toml:6`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/lighthouse/Cargo.toml#L6)
- [`consensus/types/Cargo.toml:6`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/Cargo.toml#L6)
- [`beacon_node/lighthouse_network/Cargo.toml:6`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/Cargo.toml#L6)

**Skeptic check.** Crates with many integration test files set autotests=false and link them through a single tests/main.rs; earlier evidence correct.

**Verdict history.** implemented (checked) → implemented (skeptic)

**Sources.** [lighthouse#2658](https://github.com/sigp/lighthouse/pull/2658)

</details>


<a id="build-058"></a>
<details>
<summary><b>build-058</b> Generate protobuf code once in shared crate — <i>n/a · low · S · startup</i></summary>

**Idea.** Generate protobuf/code-generated sources once in a shared crate instead of in several crates' build scripts.

**Impact.** No protobuf codegen in Lighthouse build scripts (libp2p brings its own prebuilt code).

**Evidence (Lighthouse @ 928b61e719).**

- Cargo.toml - no prost/protobuf dependencies in workspace manifests (grep found none)

**Sources.** [silver#358](https://github.com/gattaca-com/silver/pull/358)

</details>


<a id="build-059"></a>
<details>
<summary><b>build-059</b> Bump dependency with cheaper generated-table compile — <i>n/a · low · S · startup</i></summary>

**Idea.** Update dependencies that embed large generated lookup tables (e.g. an IP-to-ASN table in the libp2p stack) to versions that compile the table more cheaply. Check whether Lighthouse's discv5/libp2p dependencies pull in a similarly heavy generated-table crate.

**Impact.** Rust libp2p has no embedded IP-to-ASN table; this was a go-libp2p issue.

**Evidence (Lighthouse @ 928b61e719).**

- Cargo.lock: no ASN/GeoIP table crate (only ipnet, phf); discv5 0.12.0 and libp2p 0.57.0 pull none

**Sources.** [prysm#13370](https://github.com/OffchainLabs/prysm/pull/13370)

</details>


