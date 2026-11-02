# build

22 checked ideas, 2 actionable. [Back to the summary](../README.md).

## Actionable (2)

High or medium value, verdict `not` or `partial`.

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

**Sources.** [prysm#13035](https://github.com/OffchainLabs/prysm/pull/13035), [prysm#13158](https://github.com/OffchainLabs/prysm/pull/13158), [prysm#14589](https://github.com/OffchainLabs/prysm/pull/14589)

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

**Sources.** [ethlambda#311](https://github.com/lambdaclass/ethlambda/pull/311), [nimbus#726](https://github.com/status-im/nimbus-eth2/pull/726), [nimbus@4d487cea1](https://github.com/status-im/nimbus-eth2/commit/4d487cea1fd2), [nimbus#3162](https://github.com/status-im/nimbus-eth2/pull/3162), [lighthouse#2966](https://github.com/sigp/lighthouse/pull/2966)

</details>

## Other checked ideas (20)

Implemented, not applicable, or low value.

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

<a id="build-053"></a>
<details>
<summary><b>build-053</b> Trim per-fork generic helper instantiations — <i>not · low · M · memory</i></summary>

**Idea.** Reduce code generated per fork by trimming generic debug/helper functions monomorphized for every fork type, cutting compile time and compiler memory.

**Gap in Lighthouse.** Would need to measure monomorphization (cargo llvm-lines) of types/state_processing and drop or dyn-ify debug helpers instantiated per fork and per EthSpec.

**Impact.** Slightly faster Lighthouse builds and lower compiler RSS; no runtime effect.

**Best measured result.** pr:nimbus#9108: peak RSS 6.0GB -&gt; 5.1GB; wall 1034s -&gt; 912s (-12%)

**Evidence (Lighthouse @ 928b61e719).**

- No per-fork debug/helper generics audit found; [`consensus/types`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types) uses superstruct per-fork types with generic E everywhere

**Sources.** [nimbus#9108](https://github.com/status-im/nimbus-eth2/pull/9108)

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

<a id="build-001"></a>
<details>
<summary><b>build-001</b> Fat LTO and single codegen unit for release binaries — <i>implemented · medium · S · cpu</i></summary>

**Idea.** Build released binaries with a maximum-performance profile (fat/whole-program LTO, one codegen unit) on every platform and in Docker images, so small hot functions in SSZ hashing, state transition and fork choice inline across crate boundaries. Check the Cargo release profile used by CI, Windows releases and Dockerfiles.

**Gap in Lighthouse.** 

**Impact.** Already done for tagged releases; only unstable/branch images and plain make use the thin-LTO release profile.

**Best measured result.** pr:nimbus#1661: 40% faster block replay and hashing; apply epoch block 333ms -&gt; 195ms

**Evidence (Lighthouse @ 928b61e719).**

- Cargo.toml:286 profile.maxperf fat LTO, codegen-units=1
- [`.github/workflows/release.yml:41`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/.github/workflows/release.yml#L41) release binaries use maxperf
- [`.github/workflows/docker.yml:60`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/.github/workflows/docker.yml#L60) tag Docker builds use maxperf

**Sources.** [nimbus#1661](https://github.com/status-im/nimbus-eth2/pull/1661), [ethlambda#543](https://github.com/lambdaclass/ethlambda/pull/543), [lighthouse#3608](https://github.com/sigp/lighthouse/pull/3608), [lighthouse#4371](https://github.com/sigp/lighthouse/pull/4371), [lighthouse#4237](https://github.com/sigp/lighthouse/pull/4237)

</details>

<a id="build-004"></a>
<details>
<summary><b>build-004</b> Build blst with ADX/BMI2 instead of portable — <i>implemented · medium · S · cpu</i></summary>

**Idea.** Build the BLS library (blst) in its non-portable mode with ADX/BMI2 (mulx/adox/adcx) on amd64, at -O3, for the shipped binaries, instead of the portable fallback. Field arithmetic for signature verification is much faster.

**Gap in Lighthouse.** 

**Impact.** Negligible further gain; the modern feature (bls/supranational-force-adx) exists and would only drop a runtime dispatch check.

**Evidence (Lighthouse @ 928b61e719).**

- [`lighthouse/Cargo.toml:19`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/lighthouse/Cargo.toml#L19) portable feature
- [`scripts/ci/build-linux.sh:16`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/scripts/ci/build-linux.sh#L16) release builds use portable
- [`book/src/installation_source.md:167`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/book/src/installation_source.md#L167) portable uses runtime CPU feature detection
- blst-0.3.17/build.rs:166 portable defines __BLST_PORTABLE__ (asm picks ADX at runtime); build.rs:237 forces opt_level 2

**Sources.** [prysm#12564](https://github.com/OffchainLabs/prysm/pull/12564), [prysm#10567](https://github.com/OffchainLabs/prysm/pull/10567), [nimbus#4914](https://github.com/status-im/nimbus-eth2/pull/4914), [caplin#11144](https://github.com/erigontech/erigon/pull/11144)

</details>

<a id="build-011"></a>
<details>
<summary><b>build-011</b> Native arm runners instead of emulated builds — <i>implemented · low · S · startup</i></summary>

**Idea.** Build arm64 images on native arm runners, or build arch-independent parts on the host and only native parts for the target, instead of compiling everything under QEMU emulation.

**Gap in Lighthouse.** 

**Impact.** CI only; already native, no QEMU.

**Best measured result.** pr:lodestar#4369: arm64 build roughly equals npm install time; emulated native build was 12-14 min

**Evidence (Lighthouse @ 928b61e719).**

- [`.github/workflows/release.yml:40`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/.github/workflows/release.yml#L40) aarch64 builds on ubuntu-24.04-arm
- [`.github/workflows/docker.yml:46`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/.github/workflows/docker.yml#L46) native arm runner for aarch64 images
- [`scripts/ci/build-linux.sh:3`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/scripts/ci/build-linux.sh#L3) replaces cross; each arch built natively

**Sources.** [lodestar#4369](https://github.com/ChainSafe/lodestar/pull/4369), [lodestar#8821](https://github.com/ChainSafe/lodestar/pull/8821)

</details>

<a id="build-024"></a>
<details>
<summary><b>build-024</b> Debug builds for CI targets — <i>implemented · low · S · startup</i></summary>

**Idea.** Build CI test targets in debug mode instead of release to cut compile time.

**Gap in Lighthouse.** 

**Impact.** CI compile time only.

**Best measured result.** pr:nimbus#4655: build time 25 -&gt; 15 minutes

**Evidence (Lighthouse @ 928b61e719).**

- [`.github/workflows/test-suite.yml:277-297`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/.github/workflows/test-suite.yml#L277-L297) debug-tests-ubuntu runs make test-debug
- Makefile:184 test-debug

**Sources.** [nimbus#4655](https://github.com/status-im/nimbus-eth2/pull/4655)

</details>

<a id="build-031"></a>
<details>
<summary><b>build-031</b> Multi-stage Docker build with slim runtime image — <i>implemented · low · S · disk</i></summary>

**Idea.** Use a multi-stage Dockerfile so the runtime image is a minimal base with only the binary, not the toolchain.

**Gap in Lighthouse.** 

**Impact.** Image size only.

**Best measured result.** pr:lighthouse#749: Docker image 1.8gb -&gt; 138mb

**Evidence (Lighthouse @ 928b61e719).**

- Dockerfile:1 builder stage
- Dockerfile:18-24 ubuntu:24.04 runtime copies only the binary

**Sources.** [lighthouse#749](https://github.com/sigp/lighthouse/pull/749), [lodestar#354](https://github.com/ChainSafe/lodestar/pull/354)

</details>

<a id="build-036"></a>
<details>
<summary><b>build-036</b> Reduce debug info in release builds — <i>implemented · low · S · disk, startup</i></summary>

**Idea.** Emit reduced or no debug info in the release profile (e.g. line tables only), so binaries are about half the size and link faster while keeping backtraces.

**Gap in Lighthouse.** 

**Impact.** Release binaries already carry no debug info.

**Best measured result.** pr:nimbus#2602: 165MB -&gt; 87MB binary

**Evidence (Lighthouse @ 928b61e719).**

- Cargo.toml:286-294 no debug set in release/maxperf (cargo default debug=0)
- Cargo.toml:292 release-debug opt-in profile with debug=true
- Makefile:123 remap-path-prefix

**Sources.** [lighthouse@77ac49a55](https://github.com/sigp/lighthouse/commit/77ac49a5536c), [nimbus#2602](https://github.com/status-im/nimbus-eth2/pull/2602), [nimbus@73e9448a1](https://github.com/status-im/nimbus-eth2/commit/73e9448a1a32)

</details>

<a id="build-041"></a>
<details>
<summary><b>build-041</b> Faster or self-hosted CI runners — <i>implemented · low</i></summary>

**Idea.** Run CI on faster or self-hosted runners with a fallback to hosted runners.

**Gap in Lighthouse.** 

**Impact.** CI wall time only; no node effect.

**Best measured result.** pr:lodestar#5079: total CI 27m -&gt; 17m (-37%)

**Evidence (Lighthouse @ 928b61e719).**

- [`.github/workflows/test-suite.yml:108`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/.github/workflows/test-suite.yml#L108) warp 8x runner when repo is sigp/lighthouse, else ubuntu-latest fallback

**Sources.** [lodestar#5079](https://github.com/ChainSafe/lodestar/pull/5079), [lighthouse#4506](https://github.com/sigp/lighthouse/pull/4506)

</details>

<a id="build-047"></a>
<details>
<summary><b>build-047</b> Parallelize CI jobs and pipeline steps — <i>implemented · low</i></summary>

**Idea.** Structure the CI pipeline so independent jobs (test suites, spec extraction, image build) run in parallel after a shared build, gated only on what they really need.

**Gap in Lighthouse.** 

**Impact.** CI wall time only.

**Evidence (Lighthouse @ 928b61e719).**

- [`.github/workflows/test-suite.yml:106`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/.github/workflows/test-suite.yml#L106) jobs depend only on check-labels and run in parallel
- [`.github/workflows/test-suite.yml:559`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/.github/workflows/test-suite.yml#L559) final gate job

**Sources.** [lodestar#1713](https://github.com/ChainSafe/lodestar/pull/1713), [teku#1833](https://github.com/Consensys-Incorporated/teku/pull/1833), [teku#1989](https://github.com/Consensys-Incorporated/teku/pull/1989), [teku#2043](https://github.com/Consensys-Incorporated/teku/pull/2043)

</details>

<a id="build-057"></a>
<details>
<summary><b>build-057</b> Single integration test binary — <i>implemented · low</i></summary>

**Idea.** Disable auto-discovery of integration test files so all tests link into one binary, cutting link and compile time.

**Gap in Lighthouse.** 

**Impact.** Faster test builds only.

**Best measured result.** pr:lighthouse#2658: build 1m19s -&gt; 43.5s

**Evidence (Lighthouse @ 928b61e719).**

- [`beacon_node/beacon_chain/Cargo.toml:7`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/beacon_chain/Cargo.toml#L7) autotests=false
- [`beacon_node/http_api/Cargo.toml:6`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/http_api/Cargo.toml#L6)
- [`lighthouse/Cargo.toml:6`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/lighthouse/Cargo.toml#L6)
- [`consensus/types/Cargo.toml:6`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/consensus/types/Cargo.toml#L6)
- [`beacon_node/lighthouse_network/Cargo.toml:6`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/beacon_node/lighthouse_network/Cargo.toml#L6)

**Sources.** [lighthouse#2658](https://github.com/sigp/lighthouse/pull/2658)

</details>

<a id="build-007"></a>
<details>
<summary><b>build-007</b> Verify SIMD BLS feature reaches release images — <i>n/a · low · S · cpu</i></summary>

**Idea.** Check that release binaries and container images really enable the SIMD/assembly BLS feature; a default-features change can silently leave the image on the scalar path. Inspect the built binary for the expected instructions.

**Gap in Lighthouse.** 

**Impact.** Lighthouse uses blst assembly with runtime dispatch in portable builds, so no default-feature switch can silently leave the image on a scalar path (silver's problem was a SIMD-specific Cargo feature).

**Best measured result.** pr:silver#393: binary had 0 vpmadd52 instructions before, 264 after

**Evidence (Lighthouse @ 928b61e719).**

- [`lighthouse/Cargo.toml:19-21`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/lighthouse/Cargo.toml#L19-L21) portable/modern features
- blst-0.3.17/build.rs:160-213 feature/ADX selection

**Sources.** [silver#393](https://github.com/gattaca-com/silver/pull/393)

</details>

<a id="build-016"></a>
<details>
<summary><b>build-016</b> Upgrade compiler and build tool versions — <i>n/a · low · S · cpu</i></summary>

**Idea.** Upgrade the compiler and build tool (and its plugins) to newer, faster versions and tune build settings to cut compile and CI time.

**Gap in Lighthouse.** 

**Impact.** None at runtime; pure CI/build housekeeping, Lighthouse already tracks a recent pinned toolchain.

**Evidence (Lighthouse @ 928b61e719).**

- Cargo.toml:286 maxperf profile; Dockerfile:1 rust:1.91.0

**Sources.** [teku#359](https://github.com/Consensys-Incorporated/teku/pull/359), [lodestar#4830](https://github.com/ChainSafe/lodestar/pull/4830), [lodestar#8992](https://github.com/ChainSafe/lodestar/pull/8992)

</details>

<a id="build-019"></a>
<details>
<summary><b>build-019</b> Cache derived test fixtures between CI runs — <i>n/a · low · S · cpu, startup</i></summary>

**Idea.** Cache expensive deterministic test fixtures (e.g. interop validator pubkeys) between CI runs, keyed by OS, lockfile and helper version, so tests do not regenerate them.

**Gap in Lighthouse.** 

**Impact.** Lighthouse tests use fixed hard-coded keypairs rather than generating interop keys per run; CI cache gain is minor.

**Best measured result.** pr:lodestar#9906: phase0 test 75.7s -&gt; 46.9s (38.1%)

**Evidence (Lighthouse @ 928b61e719).**

- Makefile:184 test-debug
- [`testing/ef_tests`](https://github.com/sigp/lighthouse/blob/928b61e719c39f7fe8c074767b594fb99f4379bd/testing/ef_tests)

**Sources.** [lodestar#9906](https://github.com/ChainSafe/lodestar/pull/9906)

</details>

<a id="build-050"></a>
<details>
<summary><b>build-050</b> Install prebuilt test tools in CI — <i>n/a · low</i></summary>

**Idea.** Install prebuilt binaries of test tooling (e.g. anvil) in CI instead of compiling them from source each run.

**Gap in Lighthouse.** 

**Impact.** Lighthouse CI no longer builds or installs anvil, so nothing to speed up.

**Best measured result.** pr:lighthouse#4505: ~10 min source build -&gt; ~2 s install

**Evidence (Lighthouse @ 928b61e719).**

- grep for anvil/foundry in .github, Makefile, testing/*/Cargo.toml: no hits

**Sources.** [lighthouse#4505](https://github.com/sigp/lighthouse/pull/4505)

</details>

