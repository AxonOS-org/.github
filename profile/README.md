<div align="center">

<img src="./banner.jpg" alt="AxonOS — open cognitive operating system for brain–computer interfaces" width="100%" />

<br/>
<br/>

# AxonOS

### The open cognitive operating system for brain–computer interfaces.

<br/>

<sub>🇬🇧 [English](./README.md) · 🇯🇵 [日本語](./README.ja.md) · 🇨🇳 [中文](./README.zh.md) · 🇮🇹 [Italiano](./README.it.md) · 🇫🇷 [Français](./README.fr.md) · 🇩🇪 [Deutsch](./README.de.md) · 🇪🇸 [Español](./README.es.md) · 🇸🇦 [العربية](./README.ar.md)</sub>

<br/>

[![Standard](https://img.shields.io/github/v/tag/AxonOS-org/axonos-standard?sort=semver&style=flat-square&label=Standard&color=0a4a8f)](https://github.com/AxonOS-org/axonos-standard/releases)
[![Kernel](https://img.shields.io/github/v/tag/AxonOS-org/axonos-kernel?sort=semver&style=flat-square&label=Kernel&color=0a4a8f)](https://github.com/AxonOS-org/axonos-kernel/releases)
[![Consent](https://img.shields.io/github/v/tag/AxonOS-org/axonos-consent?sort=semver&style=flat-square&label=Consent&color=0a4a8f)](https://github.com/AxonOS-org/axonos-consent/releases)
[![Protocol](https://img.shields.io/github/v/tag/AxonOS-org/axonos-protocol?sort=semver&style=flat-square&label=Protocol&color=0a4a8f)](https://github.com/AxonOS-org/axonos-protocol/releases)
[![Rust](https://img.shields.io/badge/Built%20with-Rust-CE422B?style=flat-square&logo=rust&logoColor=white)](https://www.rust-lang.org/)
[![License](https://img.shields.io/badge/License-Apache--2.0%20OR%20MIT-475569?style=flat-square)](#licensing)
[![Verified](https://img.shields.io/badge/Verified-Kani%20BMC-0d7a5f?style=flat-square)](https://model-checking.github.io/kani/)

<br/>

**[axonos.org](https://axonos.org)** &nbsp;·&nbsp;
**[Specifications](https://axonos.org/specifications.html)** &nbsp;·&nbsp;
**[SDK](https://axonos.org/sdk.html)** &nbsp;·&nbsp;
**[Research](https://axonos.org/research.html)** &nbsp;·&nbsp;
**[Articles](https://medium.com/@AxonOS)** &nbsp;·&nbsp;
**[connect@axonos.org](mailto:connect@axonos.org)**

</div>

---

## What AxonOS is

AxonOS is a hard real-time neural operating system for brain–computer
interfaces. Open-source kernel in `#![no_std]` Rust on ARM Cortex-M.
Formally bounded worst-case response time. Structural privacy that the
application layer cannot bypass.

It is **not** an AI-agent framework, **not** a chatbot runtime, **not** a
generic Python SDK, and **not** a token project. Everything below the
application — the timing guarantees, the neural-permission model, the
consent state machine — is specified, openly licensed, and built to be
independently verified.

> Applications should receive typed, consent-bound intent events —
> never unrestricted raw neural streams.

---

## The four commitments

|  | Commitment | What it means in practice |
|:---:|:---|:---|
| **1** | **Hard real-time on commodity hardware** | `#![no_std]` Rust on ARMv8-M. No GC, no allocator on the hot path, no unbounded panics. Memory safety is structural. |
| **2** | **Formally bounded WCRT** | Every critical-path operation has a Kani-verified upper bound. Latency is *proven*, not benchmarked. |
| **3** | **Structural privacy** | Capabilities that would leak raw cognitive state (`RawEEG`, `EmotionState`, `CognitiveProfile`) do not exist as types. |
| **4** | **Open ecosystem** | Apache-2.0 OR MIT for code, CC-BY-SA-4.0 for specifications. Every repository is public. Anyone can audit, fork, or replace any layer. |

---

## Where to begin

Three honest paths, depending on what you want.

|  | If you want to … | Start here |
|:---:|:---|:---|
| **A** | Get the idea in two minutes | [Concept video](https://axonos.org) · [3-page engineering memo](https://axonos.org/memo.html) |
| **B** | Read the engineering before judging | [`axonos-standard/STANDARD.md`](https://github.com/AxonOS-org/axonos-standard/blob/main/STANDARD.md) · [`axonos-rfcs`](https://github.com/AxonOS-org/axonos-rfcs) |
| **C** | Build against the substrate | [`axonos-sdk`](https://github.com/AxonOS-org/axonos-sdk) · [SDK overview](https://axonos.org/sdk.html) |

---

## The stack

Every repository is public. Source under Apache-2.0 OR MIT, specifications
under CC-BY-SA-4.0. There are no private repositories. Each repository has one
role.

|  | Repository | Role | Language | Latest |
|:---:|:---|:---|:---:|:---|
| ⬢ | [**`axonos-standard`**](https://github.com/AxonOS-org/axonos-standard) | Normative architecture — the canonical technical standard | Markdown | ![](https://img.shields.io/github/v/tag/AxonOS-org/axonos-standard?sort=semver&style=flat-square&label=&color=0a4a8f) |
| ⬢ | [**`axonos-rfcs`**](https://github.com/AxonOS-org/axonos-rfcs) | Design-change process — numbered engineering RFCs, normative once finalised | Markdown | active |
| ⬢ | [**`axonos-kernel`**](https://github.com/AxonOS-org/axonos-kernel) | Execution substrate — hard real-time microkernel, formally bounded WCRT | Rust | ![](https://img.shields.io/github/v/tag/AxonOS-org/axonos-kernel?sort=semver&style=flat-square&label=&color=0a4a8f) |
| ⬢ | [**`axonos-sdk`**](https://github.com/AxonOS-org/axonos-sdk) | Application boundary — typed intents, capability manifests, kernel ABI v1 | Rust | ![](https://img.shields.io/github/v/tag/AxonOS-org/axonos-sdk?sort=semver&style=flat-square&label=&color=0a4a8f) |
| ⬢ | [**`axonos-sdk-python`**](https://github.com/AxonOS-org/axonos-sdk-python) | Application boundary (Python) — RFC-0006 wire format, byte-compatible with the Rust SDK | Python | ![](https://img.shields.io/github/v/tag/AxonOS-org/axonos-sdk-python?sort=semver&style=flat-square&label=&color=0a4a8f) |
| ⬢ | [**`axonos-consent`**](https://github.com/AxonOS-org/axonos-consent) | Consent / co-authorisation subsystem — `#![no_std]` reference crate | Rust | ![](https://img.shields.io/github/v/tag/AxonOS-org/axonos-consent?sort=semver&style=flat-square&label=&color=0a4a8f) |
| ⬢ | [**`axonos-protocol`**](https://github.com/AxonOS-org/axonos-protocol) | Network-level consent protocol — `no_std`, zero-alloc, bounded CBOR frames and an exhaustive consent state machine | Rust | ![](https://img.shields.io/github/v/tag/AxonOS-org/axonos-protocol?sort=semver&style=flat-square&label=&color=0a4a8f) |
| ⬢ | [**`axonos-conformance`**](https://github.com/AxonOS-org/axonos-conformance) | Byte-exact conformance — RFC-0005 capability manifest &amp; RFC-0006 intent wire format, cross-checked across Rust, Python, C, JavaScript, Java in CI | multi | active |
| ⬢ | [**`axonos-validation`**](https://github.com/AxonOS-org/axonos-validation) | Evidence and trace record — measurement traces and reference post-processing | Python | record |
| ⬢ | [**`axon-bci-gateway`**](https://github.com/AxonOS-org/axon-bci-gateway) | Acquisition bridge — OpenBCI fork, MIT preserved from upstream | HTML | ![](https://img.shields.io/github/v/tag/AxonOS-org/axon-bci-gateway?sort=semver&style=flat-square&label=&color=0a4a8f) |
| ⬢ | [**`axonos-swarm`**](https://github.com/AxonOS-org/axonos-swarm) | Long-horizon distributed timing — multi-node Neural PTP coordination | Rust | ![](https://img.shields.io/github/v/tag/AxonOS-org/axonos-swarm?sort=semver&style=flat-square&label=&color=0a4a8f) |
| ⬢ | [**`AxonOS`**](https://github.com/AxonOS-org/AxonOS) | Public entry point — landing, concept, and links into the stack | — | — |
| ⬢ | [**`become-the-brain-os`**](https://github.com/AxonOS-org/become-the-brain-os) | Community front door — browser game that teaches the runtime, no install | HTML/JS | ![](https://img.shields.io/github/v/tag/AxonOS-org/become-the-brain-os?sort=semver&style=flat-square&label=&color=0a4a8f) |

---

## The full path: electrode to intent

A complete brain–computer interface operating system is a continuous chain — from
a raw electrode signal to a typed, consented intent, and back to a safe failure
state. AxonOS is building that chain in the open. This map is deliberately honest
about what is shipped, what is partial, and what is still ahead.

| Stage | Provided by | Status |
|:---|:---|:---:|
| Electrode acquisition / ADC bridge | `axon-bci-gateway` (OpenBCI) | **partial** |
| Monotonic timestamping | `axonos-kernel` | **live** |
| Deterministic handoff — SPSC IPC, ring buffers | `axonos-kernel` | **live** |
| Signal conditioning / artifact rejection (DSP) | dedicated DSP layer | **planned** |
| On-device intent classification | reference classifier | **planned** |
| Typed intent ABI — RFC-0006 | `axonos-sdk`, `axonos-sdk-python` | **live** |
| Byte-exact conformance | `axonos-conformance` | **live** |
| Consent &amp; capability gate — RFC-0005 | `axonos-consent`, `axonos-protocol`, kernel gate | **live** |
| Application boundary | `axonos-sdk` | **live** |
| Audit &amp; reproducible traces | `axonos-validation` | **live** *(L2 traces pending)* |
| Safe failure state | `axonos-kernel` | **live** |

### What a complete BCI OS still needs

The execution core, the consent and capability layer, and the conformance surface
are in place. To be a full operating system — not only a standard and a kernel —
AxonOS still needs, and is sequencing on its roadmap:

- a dedicated **acquisition driver** and a fixed-point **DSP pipeline** (signal → features), plus a reference **on-device classifier**;
- a deterministic **simulator**, so a developer can run the full path without hardware;
- a structured **safety case** (hazard analysis, FMEA, residual-risk argument) and a formal **threat model** for cognitive data — as engineering artifacts, not regulatory claims;
- a **privacy-vault enforcement layer** that guarantees raw neural data never crosses the application boundary;
- a public **conformance program** and an **independent-implementer challenge**, so a third party can build a compatible kernel and SDK from the specification alone;
- a path from founder-led to **foundation / technical-steering** governance.

These are roadmap items, not present capabilities. They are published here so the
distance between today's reference implementation and a complete, independently
implementable BCI operating system is **visible rather than hidden**.

---

## Architecture

```mermaid
flowchart LR
    A[EEG/EMG sensors<br/>ADS1299 · 24-bit] -->|raw| B[Acquisition gateway<br/>nRF52840]
    B -->|filtered| C[AxonOS kernel<br/>Rust no_std<br/>Cortex-M4F]
    C -->|WCRT ≤1000µs, proven| D[Cognitive scheduler]
    D -->|typed intent| E[Application<br/>via SDK]
    F[Cognitive Hypervisor<br/>TrustZone-S] -.->|isolates| C
    G[Consent FSM<br/>axonos-consent] -.->|gates| D

    classDef kernel fill:#0a4a8f,stroke:#0a4a8f,color:#fff,stroke-width:2px
    classDef secure fill:#0d7a5f,stroke:#0d7a5f,color:#fff,stroke-width:2px
    class C kernel
    class F,G secure
```

Every arrow is a contract. The [Standard](https://github.com/AxonOS-org/axonos-standard)
defines what must hold at each boundary; an implementation is free in
everything else.

---

## By the numbers

<br/>

<table align="center">
<tr>
    <td align="center" width="220">
      <h2>≤ 1000 µs</h2>
      <sub>End-to-end WCRT, upper bound<br/><b>L1 — machine-checked proof</b></sub>
    </td>
    <td align="center" width="220">
      <h2>≤ 0.5 µs</h2>
      <sub>IPC slot latency, upper bound<br/><b>L1 — machine-checked proof</b></sub>
    </td>
    <td align="center" width="220">
      <h2>≤ 1648 cyc</h2>
      <sub>Consent-withdrawal bound<br/><b>L1 — machine-checked proof</b></sub>
    </td>
  </tr>
<tr>
  <td align="center">
    <h2>30+</h2>
    <sub>Kani BMC harnesses<br/>upper bounds proven</sub>
  </td>
  <td align="center">
    <h2>2</h2>
    <sub>Audited `unsafe` operations (kernel)<br/>`forbid(unsafe)` in consent &amp; protocol</sub>
  </td>
  <td align="center">
    <h2>42+</h2>
    <sub>Long-form architecture<br/>articles on Medium</sub>
  </td>
</tr>
</table>

<br/>

The evidence taxonomy — **L1** formally proven, **L2** measured on reference
hardware, **L3** independently validated — is defined in
[`VALIDATION.md`](https://github.com/AxonOS-org/axonos-standard/blob/main/VALIDATION.md),
and every claim is graded in
[`CLAIMS.md`](https://github.com/AxonOS-org/axonos-standard/blob/main/CLAIMS.md).
The bounds above are **L1**: machine-checked proofs, published and proof-linked.
The corresponding **L2** worst-case figures — end-to-end latency, jitter, and the
resulting improvement over a general-purpose OS — come from internal long-duration
soak testing. Until their raw traces are published in `axonos-validation`, **no
measured performance figure is claimed here**; the figures are held as
publication-pending and graded in `CLAIMS.md`. **L3** independent reproduction is
**not claimed**.

---

## Quick start

```sh
git clone https://github.com/AxonOS-org/axonos-sdk
cd axonos-sdk
cargo test --features std
```

```rust
use axonos_sdk::{Capability, IntentStream, Manifest};

let manifest = Manifest::builder()
    .app_id("com.example.cursor")?
    .capability(Capability::Navigation)
    .max_rate_hz(50)
    .build()?;

let mut stream = IntentStream::connect(&manifest)?;
while let Some(obs) = stream.try_next()? {
    println!("{:?} @ {} µs ({}%)",
        obs.kind(),
        obs.timestamp().as_micros(),
        obs.confidence_percent());
}
```

The SDK is the Rust reference binding. C FFI, Python, WebAssembly, JNI,
and Swift bindings are on the [published roadmap](https://axonos.org/sdk.html).

---

## Status

| Phase | What | When |
|:---|:---|:---|
| **Phase 0** | Architecture, RFCs, SDK API surface, kernel verification harnesses | Complete |
| **Phase 1** | Clinical-grade 8-channel development kit · ALS centre pilot | Q2 2026 |
| **Phase 2** | FDA 510(k) Q-Sub for the Cognitive Hypervisor · IEEE P2731 contribution | Q3 2026 |
| **Phase 3** | First commercial deployment via Foundation members | 2027 |

---

## What AxonOS does not claim

AxonOS does not currently claim, and this organisation must not be read
as claiming:

- FDA clearance, CE marking, or medical-device approval in any jurisdiction;
- clinical efficacy, or independent clinical validation;
- certified medical-device status, or production-implant readiness;
- complete compliance with IEC 62304, ISO 14971, or ISO 13485.

These are possible future milestones. They are not present facts, and the
project records them as such.

---

## Documentation

- [**Specifications**](https://axonos.org/specifications.html) — kernel ABI v1, capability catalogue, `IntentObservation` wire format, RFC index
- [**SDK and language bindings**](https://axonos.org/sdk.html) — Rust today; C FFI, Python, WebAssembly, JNI, Swift on the published roadmap
- [**Standards engagement**](https://axonos.org/standards.html) — IEEE P2731 · IEC 62304 · ISO 13485 · FDA 510(k) · EU MDR
- [**Governance**](https://axonos.org/governance.html) — current state, transition plan, trademark policy
- [**Engineering memo**](https://axonos.org/memo.html) — three-page summary for technical readers
- [**Long-form articles**](https://medium.com/@AxonOS) — 42+ pieces, one per major architectural decision

---

## Contributing

| Path | Where |
|:---|:---|
| Bugs and feature requests | the relevant repository's Issues tab |
| Specification proposals | pull request to [`axonos-rfcs`](https://github.com/AxonOS-org/axonos-rfcs) |
| Code contributions | [`axonos-sdk/CONTRIBUTING.md`](https://github.com/AxonOS-org/axonos-sdk/blob/main/CONTRIBUTING.md) |
| Security disclosures | [security@axonos.org](mailto:security@axonos.org) · 90-day coordinated disclosure |
| Clinical partnerships | [connect@axonos.org](mailto:connect@axonos.org) |
| General correspondence | [connect@axonos.org](mailto:connect@axonos.org) |

---

## Licensing

| Artefact | License |
|:---|:---|
| Kernel, SDK, consent, swarm, gateway | Apache-2.0 OR MIT |
| RFCs and specifications | CC-BY-SA-4.0 |
| `axon-bci-gateway` | MIT (preserved from upstream OpenBCI_GUI) |

<br/>
<br/>

---

<div align="center">

<img src="./logo.png" width="64" alt="AxonOS logo" />

<br/>
<br/>

**The AxonOS Project**

[axonos.org](https://axonos.org) &nbsp;·&nbsp;
[connect@axonos.org](mailto:connect@axonos.org) &nbsp;·&nbsp;
[LinkedIn](https://www.linkedin.com/in/denis-yermakou) &nbsp;·&nbsp;
[Medium](https://medium.com/@AxonOS)

<sub>Singapore · Zurich · Berlin · Milano · San Mateo</sub>

<br/>

<sub>Built with Rust. Verified with Kani. Aimed at hard real-time.</sub>

</div>
