<div align="center">

# AxonOS

### The deterministic cognitive operating system for brain-computer interfaces

A `#![no_std]` Rust microkernel that converts neural signals into cryptographically attested intent under strict latency, privacy, and consent guarantees. Motor imagery → deterministic intent → silicon-level execution. No garbage collection. No jitter. No cloud.

[![Website](https://img.shields.io/badge/axonos.org-000000?style=for-the-badge&logoColor=white)](https://axonos.org)
[![Medium](https://img.shields.io/badge/Medium-02b875?style=for-the-badge&logo=medium&logoColor=white)](https://medium.com/@AxonOS)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/axonos)
[![Email](https://img.shields.io/badge/axonosorg%40gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:axonosorg@gmail.com)

[![Rust](https://img.shields.io/badge/Rust-no__std-%23dea584?style=flat-square&logo=rust)](https://doc.rust-lang.org/reference/names/preludes.html#the-no_std-attribute)
[![Cortex-M33](https://img.shields.io/badge/Cortex--M33-STM32H573-%2332C3B1?style=flat-square)](https://www.st.com/en/microcontrollers-microprocessors/stm32h573-583.html)
[![WCET](https://img.shields.io/badge/WCET-618µs-success?style=flat-square)](https://medium.com/@AxonOS/axonos-mvp-the-benchmark-report-latency-power-ea6c78d0e091)
[![Jitter](https://img.shields.io/badge/jitter-2.4µs%20RMS-success?style=flat-square)](https://medium.com/@AxonOS/axonos-mvp-the-benchmark-report-latency-power-ea6c78d0e091)
[![MMP](https://img.shields.io/badge/MMP-v0.2.2-purple?style=flat-square)](https://sym.bot/spec/mmp)
[![SVAF](https://img.shields.io/badge/SVAF-arXiv%3A2604.03955-b31b1b?style=flat-square)](https://arxiv.org/abs/2604.03955)
[![License](https://img.shields.io/badge/license-Apache--2.0%20OR%20MIT-blue?style=flat-square)](https://github.com/AxonOS-org/axonos-consent/blob/main/LICENSE-APACHE)
[![UNESCO 2025](https://img.shields.io/badge/UNESCO%202025-aligned-2E86AB?style=flat-square)](https://www.unesco.org/en/articles/ethics-neurotechnology)

</div>

---

## Why AxonOS exists

Most brain-computer interface software runs on Linux, RTOS, or Python stacks — general-purpose platforms with non-deterministic schedulers, garbage collectors, and millisecond-scale jitter. For a system that must close the neural feedback loop within a single 4 ms EEG sampling window and deliver consent withdrawal in under ten microseconds, this is the wrong foundation.

AxonOS is a purpose-built bare-metal microkernel. It runs directly on **STM32H573** (ARM Cortex-M33, 120 MHz), owns every clock cycle, and processes 8-channel EEG from DMA interrupt to signed `IntentObservation` packet in a verified worst-case of **618 µs** — 6× inside the 4 ms sampling window, with **2.4 µs RMS jitter** over 24-hour stress tests.

The output is not raw signal. It is a typed, cryptographically attested intent event that third-party applications receive through a WASM sandbox — with no path to the underlying neural data.

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│  TrustZone Secure World  (STM32H573 SRAM1/2)                    │
│                                                                 │
│  ADC/DMA (250 Hz, 8ch, 16-bit)                                  │
│    └─► Artifact Gate (amplitude threshold → Kalman predict)     │
│    └─► Hanning window → CSP spatial filter (8ch → 2ch)          │
│    └─► RFFT 128pt × 2ch (CMSIS-DSP, FPU, ~312 µs)               │
│    └─► Band-power extraction (mu/beta 8–30 Hz)                  │
│    └─► MDM Riemannian classifier → posterior distribution       │
│    └─► Confidence gate (posterior > θ_user AND rejection check) │
│    └─► IntentObservation { intent_id, posterior_q16,            │
│                            timestamp_us, hmac_sha256 }          │
│                                  │                              │
│              NSC Gateway (only crossing point)                  │
│                                  │                              │
├──────────────────────────────────┼──────────────────────────────┤
│  Non-Secure World                ▼                              │
│                                                                 │
│  SPSC Ring Buffer (lock-free, wait-free)                        │
│    └─► WASM Application Sandbox                                 │
│          └─► Neural Permissions Firewall                        │
│                (capability manifest enforced at load time)      │
│                └─► Third-party application                      │
│                      receives: typed event + confidence         │
│                      cannot access: raw EEG, features, keys     │
└─────────────────────────────────────────────────────────────────┘

BLE 5.2 (nRF52840) — connection interval 7.5 ms, ATT notify
```

### EDF task schedule

Verified feasible on Cortex-M33 NVIC at **19% CPU utilisation** — leaving 81% headroom for application logic and future cognitive hypervisor extensions.

| Task | Period | WCET | Utilisation |
|:---|:---:|:---:|:---:|
| Neural Decoder ISR | 4 ms | 618 µs | 15.5% |
| Intent Dispatcher | 20 ms | 400 µs | 2.0% |
| Session Auth Layer | 100 ms | 1500 µs | 1.5% |
| **Total** | | | **19.0%** |

---

## Hardware target

| Component | Part | Notes |
|:---|:---|:---|
| MCU | [STM32H573IIK3](https://www.st.com/en/microcontrollers-microprocessors/stm32h573-583.html) | Cortex-M33 @ 120 MHz, FPU, AES, TrustZone-M |
| EEG frontend | [ADS1299](https://www.ti.com/product/ADS1299) (8ch) | 24-bit ADC, 250 SPS per channel, SPI to MCU |
| Radio | [nRF52840](https://www.nordicsemi.com/Products/nRF52840) | BLE 5.2, 7.5 ms connection interval, UART bridge |
| Security | [TrustZone-M](https://developer.arm.com/documentation/100690/latest) | Partitioned SRAM: Secure (pipeline) / Non-Secure (apps) |
| Memory | 640 KB SRAM | SRAM1/2 Secure, SRAM3 Non-Secure, no heap in RT path |
| Power | Li-Po 300 mAh | 20–24 h continuous operation at 7.1 mA average |

---

## Performance

Measured on STM32H573 with logic analyser @ 100 MHz and DWT_CYCCNT.

| Metric | Value | Method |
|:---|:---:|:---|
| Pipeline WCET | **618 µs** | 10,000 frames, logic analyser |
| RMS jitter | **2.4 µs** | 10,000 frames, DWT_CYCCNT |
| 24h budget overruns | **0** | Continuous synthetic MI signal |
| Average system current | **7.1 mA** | MCU 5.26 mA + BLE 1.8 mA @ 3.3V |
| Practical battery life | **20–24 h** | 300 mAh Li-Po, measured discharge |
| Artifact frame rate | **18–22%** | Ambulatory use, 5 subjects |
| Decoder accuracy (MI 2-class) | **85–95%** | [Blankertz et al., 2008](https://doi.org/10.1109/MSP.2008.4408441) |
| **Consent withdrawal (E2E)** | **<10 µs** | [axonos-consent](https://github.com/AxonOS-org/axonos-consent) crate |

Full methodology: [Article #12 — Benchmark Report](https://medium.com/@AxonOS/axonos-mvp-the-benchmark-report-latency-power-ea6c78d0e091).

---

## Protocol layer

AxonOS implements the [**Mesh Memory Protocol (MMP) v0.2.2**](https://sym.bot/spec/mmp) — an open specification for peer-to-peer cognitive coupling developed jointly with [SYM.BOT](https://sym.bot). This enables multi-node BCI deployments: swarm robotics control, clinician-patient co-piloting, federated neural mesh networks — without compromising determinism or privacy.

The [**MMP Consent Extension v0.1.0**](https://sym.bot/spec/mmp-consent) — co-designed by AxonOS and SYM.BOT — is the first protocol-level consent primitive for brain-computer interfaces. It operates at Layer 2 (Connection), below the SVAF coupling engine (Layer 4), guaranteeing that a consent-withdraw frame closes the hardware stimulation gate before any higher-layer logic executes. Reference implementation: [`axonos-consent`](https://github.com/AxonOS-org/axonos-consent) (Rust `no_std`).

**15/15 canonical interop vectors PASS** across two independent implementations (Rust + Node.js), validated against the SYM.BOT production mesh (April 2026).

### Protocol stack

| Layer | Role | AxonOS responsibility |
|:---:|:---|:---|
| 7 | Application | WASM sandboxed apps with capability manifests |
| 6 | xMesh (neural) | Per-agent CfC network (future) |
| 5 | Synthetic memory | Memory synthesis (MMP layer) |
| **4** | **Coupling (SVAF)** | [Symbolic-Vector Attention Fusion](https://arxiv.org/abs/2604.03955) — content evaluation |
| 3 | Memory delivery | CMB frame routing (MMP layer) |
| **2** | **Connection + Consent** | [`axonos-consent`](https://github.com/AxonOS-org/axonos-consent) — Layer 2 enforcement |
| 1 | Transport | WebSocket / BLE / relay |
| 0 | Identity | Cryptographic peer identity |

---

## Tech stack

### Kernel (RT pipeline) — `#![no_std]` Rust, bare metal

- No heap allocation in the RT path — all buffers statically allocated
- No OS scheduler — EDF via NVIC priority assignment, WCET-verified
- No blocking calls — DMA-driven acquisition, interrupt-driven processing
- Memory safety enforced by Rust borrow checker + TrustZone SRAM partitioning

### Signal processing

- [CMSIS-DSP](https://github.com/ARM-software/CMSIS-DSP) (`arm_rfft_fast_f32`, `arm_mat_mult_f32`) via Rust FFI
- Common Spatial Patterns (CSP) spatial filter, pre-computed at calibration
- Riemannian MDM classifier — geodesic distance on SPD manifold
- Adaptive Kalman filter with online covariance estimation

### Security

- **TrustZone-M:** raw EEG physically isolated in Secure World SRAM
- **HMAC-SHA256** attestation on every `IntentObservation` (~2 µs overhead)
- **WASM** linear memory isolation for application layer ([Haas et al., 2017](https://doi.org/10.1145/3062341.3062363))
- **Ed25519-signed** capability manifests, kernel-enforced at load time
- **Consent enforcement:** [MMP Consent Extension v0.1.0](https://sym.bot/spec/mmp-consent)

### What is not in the kernel

- ❌ Python — incompatible with `#![no_std]` bare-metal execution
- ❌ Dynamic allocation (`malloc` / `Box` / `Vec` in RT path)
- ❌ Linux, RTOS, or any general-purpose OS layer
- ❌ Cloud connectivity — local-first architecture, neural data never leaves device

---

## Repositories

| Repository | Language | Visibility | Description |
|:---|:---:|:---:|:---|
| [`axonos-consent`](https://github.com/AxonOS-org/axonos-consent) | Rust `no_std` | **Public** | MMP Consent Extension reference implementation — deterministic consent enforcement for BCI |
| [`axonos-sdk`](https://github.com/AxonOS-org/axonos-sdk) | Rust | **Public** | Public SDK: `IntentObservation` types, capability API, WASM host bindings |
| `axonos-kernel` | Rust | Private | Bare-metal microkernel: DMA pipeline, EDF scheduler, TrustZone partition, NSC gateway |
| `axonos-dsp` | Rust | Private | Signal processing: CSP, MDM classifier, Kalman filter, artifact rejection |
| `axonos-sim` | Rust | Private | Hardware-in-the-loop simulator: synthetic MI signal generation, benchmark replay |
| [`axon-bci-gateway`](https://github.com/AxonOS-org/axon-bci-gateway) | — | Public (fork) | OpenBCI GUI fork — used for early hardware bring-up and electrode placement validation |

**Note.** The core kernel and DSP pipeline are maintained in private repositories during the pre-release phase. The [`axonos-sdk`](https://github.com/AxonOS-org/axonos-sdk) contains the public API surface — types, traits, and capability definitions that third-party developers build against. The [`axonos-consent`](https://github.com/AxonOS-org/axonos-consent) crate is the first fully open component, jointly developed with SYM.BOT.

---

## Privacy architecture

Neural data in AxonOS follows one direction and one direction only:

```
Raw EEG (Secure World SRAM)
    │
    ▼  [never crosses this boundary as raw signal]
IntentObservation (typed, signed, confidence-bearing)
    │
    ▼
WASM Application Sandbox
    │
    ▼
Third-party application
    (receives: intent class + confidence + attestation tag)
    (cannot access: electrode voltages, band features, biometric identifiers)
```

Applications declare their capability scope in a signed manifest at install time. The kernel binds only the declared host functions to the WASM instance — an application cannot call a function for a capability it didn't declare, because that function does not exist in its execution environment. Enforcement is **structural, not policy-based**.

### Capability classes

| Available | Accuracy | Notes |
|:---|:---:|:---|
| `NavigationIntents` | 85–95% | Motor imagery 2-class |
| `WorkloadAdvisory` | ~70% | Binary cognitive load |
| `SessionQuality` | Discrete | Electrode contact, signal-to-noise |
| `ArtifactEvents` | Event-based | EMG, eye-blink, motion artifacts |

### Not available as capabilities

| Prohibited | Reason |
|:---|:---|
| `RawEEG` | Architectural boundary — no API exposed |
| `EmotionState` | 60–70% accuracy, insufficient for informed consent |
| `FlowState` | Not reliably detectable in real-time |
| `CognitiveProfile` | Prohibited by design |

Full architecture: [Articles #3, #7, #9, #10](https://medium.com/@AxonOS).

---

## Regulatory alignment

| Framework | Alignment | Status |
|:---|:---|:---:|
| [IEC 62304](https://www.iso.org/standard/71604.html) Class C | Medical device software lifecycle | Architecture aligned |
| [IEC 60601-1](https://www.iso.org/standard/65529.html) | Essential performance, basic safety | StimGuard enforcement |
| [IEC 60601-1-10](https://webstore.iec.ch/publication/22048) | Closed-loop physiologic controllers | Bounded WCET |
| [ISO 14971](https://www.iso.org/standard/72704.html) | Risk management for medical devices | Threat model documented |
| [UNESCO 2025](https://www.unesco.org/en/articles/ethics-neurotechnology) | Ethics of Neurotechnology | Consent sovereignty — "at any time" |
| [Shannon criteria](https://doi.org/10.1109/10.126616) | Charge density safety (k=1.75, ≤30 µC/cm²) | Cognitive Hypervisor |
| [FDA BCI Guidance (2021)](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/implanted-brain-computer-interface-bci-devices-patients-paralysis-or-amputation-non-clinical-testing) | Implanted BCI non-clinical testing | Cybersecurity + safety |

---

## Research & publications

| Venue | Title | Status |
|:---|:---|:---:|
| arXiv `cs.MA` | [Symbolic-Vector Attention Fusion for Collective Intelligence](https://arxiv.org/abs/2604.03955) | **Live** |
| arXiv (joint) | *Protocol-Level Consent for Cognitive Mesh Coupling* (with SYM.BOT) | In preparation |
| Medium | [30-article engineering series](https://medium.com/@AxonOS) | Ongoing |

### Engineering series — selected articles

| # | Title | Topic |
|:---:|:---|:---|
| 1 | [Signal Supremacy](https://medium.com/@AxonOS) | EEG jitter, adaptive Kalman filtering |
| 4 | [Zero-Jitter Microkernel](https://medium.com/@AxonOS) | EDF scheduling, SPSC ring buffers, WCET analysis |
| 7 | [Privacy Protocol](https://medium.com/@AxonOS) | TrustZone memory map, HMAC attestation |
| 10 | [E2E Intent Routing](https://medium.com/@AxonOS) | Curve25519, AES-GCM, SPSC airgap |
| **12** | [**Benchmark Report**](https://medium.com/@AxonOS/axonos-mvp-the-benchmark-report-latency-power-ea6c78d0e091) | **618 µs WCET, 2.4 µs jitter, 20h battery — measured** |
| 13 | [Riemannian Geometry](https://medium.com/@AxonOS) | MDM classifier, session-to-session adaptation |
| 29 | [Cognitive Hypervisor](https://medium.com/@AxonOS) | Shannon-McCreery damage limits, stimulation safety |
| 30 | [Developer Ecosystem](https://medium.com/@AxonOS) | Capability manifest, app signing, SDK onboarding |
| **39** | **When Two Protocols Converged** | **MMP Consent Extension collaboration with SYM.BOT** |

→ [Full 30-article series at medium.com/@AxonOS](https://medium.com/@AxonOS)

---

## Status

**Current phase:** MVP hardware validation + protocol extension ecosystem

| | Milestone |
|:---:|:---|
| ✅ | Bare-metal pipeline verified on STM32H573 — 618 µs WCET, 0 overruns / 24h |
| ✅ | TrustZone partition implemented and tested |
| ✅ | Riemannian MDM classifier — 85–95% accuracy, 2-class MI, 5 subjects |
| ✅ | [`axonos-sdk`](https://github.com/AxonOS-org/axonos-sdk) public API alpha |
| ✅ | [`axonos-consent`](https://github.com/AxonOS-org/axonos-consent) v0.2.2 — 15/15 interop vectors pass |
| ✅ | MMP Consent Extension v0.1.0 published — joint with [SYM.BOT](https://sym.bot) |
| 🔄 | Euclidean Alignment transfer learning — session cold-start <60 s |
| 🔄 | Peripheral FES feedback path + Cognitive Hypervisor (stimulation safety) |
| 🔄 | Joint arXiv paper with SYM.BOT — *Protocol-Level Consent for Cognitive Mesh Coupling* |
| 🔄 | `axonos-cli` + simulator public release |
| ⬜ | AxonOS App Directory + capability manifest registry |
| ⬜ | CE/FDA regulatory pathway — readout-only Class I, bidirectional Class III |

---

## Collaborations

| Partner | Role |
|:---|:---|
| [**SYM.BOT**](https://sym.bot) | MMP protocol co-design · Consent Extension · Joint arXiv paper |
| US ALS rehabilitation center | Clinical deployment discussions (200+ patients, NE US) |

---

## Organisation

| | |
|:---|:---|
| **Founder** | Denis Yermakou |
| **Jurisdiction** | Singapore |
| **R&D** | Remote-first |
| **Contact** | [axonosorg@gmail.com](mailto:axonosorg@gmail.com) |

---

<div align="center">

**AxonOS. Pure signal. Zero noise.**

[axonos.org](https://axonos.org) · [medium.com/@AxonOS](https://medium.com/@AxonOS) · [linkedin.com/in/axonos](https://www.linkedin.com/in/axonos) · [axonosorg@gmail.com](mailto:axonosorg@gmail.com)

</div>
