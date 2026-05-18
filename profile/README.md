# **axonos**

The open neural operating system for brain-computer interfaces. Hard real-time, formally verified, hardware-agnostic.

![AxonOS](./banner.png)

[![License](https://img.shields.io/badge/license-Apache--2.0%20OR%20MIT-blue?style=flat-square)](https://github.com/AxonOS-org/AxonOS-kernel/blob/main/LICENSE-APACHE)
[![Articles](https://img.shields.io/badge/medium-42%2B%20articles-black?style=flat-square&logo=medium)](https://medium.com/@AxonOS)
[![Rust](https://img.shields.io/badge/built%20with-Rust-CE422B?style=flat-square&logo=rust&logoColor=white)](https://www.rust-lang.org/)
[![Kernel](https://img.shields.io/badge/kernel-v0.1.9-orange?style=flat-square)](https://github.com/AxonOS-org/AxonOS-kernel)
[![SDK](https://img.shields.io/badge/sdk-v0.1.7-orange?style=flat-square)](https://github.com/AxonOS-org/axonos-sdk)

### [Site](https://axonos.org) | [Research](https://axonos.org/research) | [Articles](https://medium.com/@AxonOS) | [Specs (RFCs)](https://github.com/AxonOS-org/axonos-rfcs) | [Get in Touch](mailto:connect@axonos.org)

---

## 🚀 Quick Start for Developers (2 min)

```sh
# 1. Try the SDK
git clone https://github.com/AxonOS-org/axonos-sdk.git
cd axonos-sdk
cargo test --features std

# 2. Read the kernel
git clone https://github.com/AxonOS-org/AxonOS-kernel.git
cd AxonOS-kernel
cargo test --workspace
```

## What problem AxonOS solves

| Capability | BCI2000 (research) | Synchron / Neuralink / NeuroXess (proprietary) | **AxonOS** |
|:---|:---:|:---:|:---:|
| Hard real-time (<1 ms jitter) | ✗ | ✓ proprietary | **✓ open, verified** |
| Cross-hardware HAL | ✗ | ✗ locked to own HW | **✓** |
| Formal privacy architecture | ✗ | ✗ | **✓ structural minimisation** |
| FDA-viable regulatory posture | ✗ | partial | **✓ IEC 62304 Class C alignment** |
| Open source kernel + SDK | ✓ | ✗ | **✓ Apache-2.0 OR MIT** |

Today, application code that consumes a real-time neural classifier has to re-parse a bespoke binary wire format per device, re-implement capability gating, and re-write integration boilerplate for every new BCI platform. AxonOS does all three once, in safe `#![no_std]` Rust, on top of a formally-bounded microkernel.

## In this org

The full AxonOS stack spans several repositories. The kernel is the verifiable substrate; the SDK is the application boundary; the RFCs are the standards that bind them.

| Repository | What it is | Language | Status |
|:---|:---|:---|:---|
| **[AxonOS-kernel](https://github.com/AxonOS-org/AxonOS-kernel)** | Hard real-time microkernel — 7 crates, 66 tests, 28 Kani BMC harnesses | Rust | v0.1.9 |
| **[axonos-sdk](https://github.com/AxonOS-org/axonos-sdk)** | Application-side SDK: typed intents, capability manifests, ABI v1 | Rust | v0.1.7 |
| **[axonos-rfcs](https://github.com/AxonOS-org/axonos-rfcs)** | Engineering specifications (RFC-0001 through RFC-0006) | Markdown | Active |
| **[axonos-consent](https://github.com/AxonOS-org/axonos-consent)** | Protocol-level consent for cognitive mesh coupling (MMP) | Rust | v0.4.0 |
| **[axonos-swarm](https://github.com/AxonOS-org/axonos-swarm)** | Multi-node coordination — Neural PTP, swarm scheduling | Rust | Pre-release |
| **[axon-bci-gateway](https://github.com/AxonOS-org/axon-bci-gateway)** | Hardware acquisition gateway (fork of OpenBCI_GUI) | HTML / Java | Active |

> Proprietary ML modules and certain hardware-specific firmware are maintained in private repositories until the Phase-1 measurement preprint is published.

## Architectural pillars

**The four bets AxonOS makes that distinguish it from every competing approach:**

1. **`#![no_std]` Rust on ARMv8-M** — no allocator on the hot path, no garbage collector, no unbounded panics. Memory safety is structural, not runtime-checked.
2. **Sub-millisecond WCRT guarantees** — formally bounded via Bounded Model Checking (Kani). Phase-1 measurement campaign on STM32H573 produces L2 evidence on real hardware.
3. **Layered protocol stack** — Axon Protocol (transport), Cognitive Hypervisor (isolation), ZeroCalib (zero-shot transfer learning), Federated Riemannian Learning (privacy-preserving cohort training). Each layer is independently auditable.
4. **Structural privacy** — capabilities that would leak raw cognitive state (RawEEG, EmotionState, CognitiveProfile) **do not exist** in the type system. Misuse is impossible at compile time, not policed at runtime.

## Reference hardware

| Component | Part | Why |
|:---|:---|:---|
| ADC | ADS1299 · 8-channel · 24-bit · 250 SPS | Open spec, research grade |
| DSP core | STM32F407 · Cortex-M4F · 168 MHz | Available, formally bounded |
| App core | Cortex-A53 · 1.2 GHz | Standard Linux + isolated DSP |
| Wireless | nRF52840 · BLE 5.3 | Secure pairing, mesh capable |
| Secure element | ATECC608B | Ed25519 attestation root |
| Isolation | ISO7741 · 5 kV galvanic | Medical-grade patient barrier |

Full design: [RFC-0005 — Hardware Reference Design](https://github.com/AxonOS-org/axonos-rfcs/blob/main/rfcs/0005-hardware-reference-design.md).

## For whom this is built

| Audience | What they find here |
|:---|:---|
| **Application developers** building closed-loop assistive interfaces | A typed `IntentObservation` decoder, a compile-time `Manifest` declaration, and an iterator-style stream API over the kernel's IPC output. |
| **Research scientists** writing custom BCI experiments | A drop-in SDK without re-implementing wire-format parsing or capability handshaking. |
| **Hardware OEMs** (Synchron, Paradromics, OpenBCI, NeuroXess) | A standard reference platform the kernel runs on, so applications written for AxonOS run on your hardware too. |
| **Regulators** (FDA, EMA, MHRA) | Source-available kernel with documented WCRT envelope, capability-based privacy proof, and audit trail. |
| **Standards bodies** (IEEE P2731, IETF) | A reference implementation that backs each RFC with running code. |

## Documentation

- **[Research overview](https://axonos.org/research)** — the project from 30,000 ft
- **[Medium series (42 articles)](https://medium.com/@AxonOS)** — long-form deep dives, one per architectural decision
- **[RFCs](https://github.com/AxonOS-org/axonos-rfcs)** — engineering specifications
- **[axonos-sdk README](https://github.com/AxonOS-org/axonos-sdk#readme)** — application developer entry point
- **[AxonOS-kernel README](https://github.com/AxonOS-org/AxonOS-kernel#readme)** — kernel internals

## Contributing

- **Code contributions:** see [CONTRIBUTING.md](https://github.com/AxonOS-org/AxonOS-kernel/blob/main/CONTRIBUTING.md) in the kernel repo
- **Specification contributions:** open an RFC via [pull request to axonos-rfcs](https://github.com/AxonOS-org/axonos-rfcs/pulls)
- **Bugs:** the relevant repo's Issues tab
- **Security:** [security@axonos.org](mailto:security@axonos.org) — please do not open public issues for security-sensitive matters

## Licensing

| Artifact | Licence |
|:---|:---|
| `AxonOS-kernel`, `axonos-sdk`, `axonos-consent`, `axonos-swarm` | Apache-2.0 OR MIT |
| `axonos-rfcs` | CC-BY-SA-4.0 |
| `axon-bci-gateway` | MIT (preserved from upstream OpenBCI_GUI) |

See the LICENSE file in each repository.

## Engagement

- **Clinical partnerships:** [connect@axonos.org](mailto:connect@axonos.org)
- **Investor discussion:** [connect@axonos.org](mailto:connect@axonos.org)
- **Press:** [info@axonos.org](mailto:info@axonos.org)
- **Security disclosures:** [security@axonos.org](mailto:security@axonos.org)
- **Speaking / technical talks:** [info@axonos.org](mailto:info@axonos.org)

---

<div align="center">

**Founder and lead engineer:** Denis Yermakou · [denis@axonos.org](mailto:denis@axonos.org)

Zurich · Berlin · Milano · San Mateo · Singapore

[axonos.org](https://axonos.org) · [medium.com/@AxonOS](https://medium.com/@AxonOS)

<sub>
<img src="https://rustacean.net/assets/rustacean-flat-happy.svg" width="32" alt="Ferris, the Rust mascot" align="absmiddle" />
&nbsp; Built with Rust. Verified with Kani. Aimed at hard real-time.
</sub>

</div>
