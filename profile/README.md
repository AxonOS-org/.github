<div align="center">

<img src="https://rustacean.net/assets/rustacean-flat-happy.svg" width="120" alt="Ferris, the Rust mascot" />

# AxonOS

### a real-time Rust microkernel for brain–computer interfaces

> Bare-metal. `no_std`. `forbid(unsafe_code)` outside two documented operations. Built around evidence — every claim tagged with the level of proof behind it.

[![Built with Rust](https://img.shields.io/badge/built%20with-Rust-CE422B?style=for-the-badge&logo=rust&logoColor=white)](https://www.rust-lang.org/)
[![License](https://img.shields.io/badge/license-Apache--2.0%20OR%20MIT-blue?style=for-the-badge)](#license)
[![no_std](https://img.shields.io/badge/no__std-yes-success?style=for-the-badge)](https://docs.rust-embedded.org/book/intro/no-std.html)
[![Kani BMC](https://img.shields.io/badge/Kani-28%20proofs-blueviolet?style=for-the-badge)](https://github.com/model-checking/kani)

[![MSRV](https://img.shields.io/badge/MSRV-1.75-orange?style=flat-square)](https://blog.rust-lang.org/2023/12/28/Rust-1.75.0.html)
[![Cortex-M4F](https://img.shields.io/badge/target-Cortex--M4F-purple?style=flat-square)](https://doc.rust-lang.org/rustc/platform-support/thumbv7em-none-eabi.html)
[![Cortex-M33](https://img.shields.io/badge/target-Cortex--M33-purple?style=flat-square)](https://doc.rust-lang.org/rustc/platform-support/thumbv8m.main-none-eabi.html)
[![Stage](https://img.shields.io/badge/stage-pre--measurement-yellow?style=flat-square)](#status)

</div>

<div align="center">

[🇬🇧 English](./README.md) ·
[🇯🇵 日本語](./README.ja.md) ·
[🇨🇳 中文](./README.zh.md) ·
[🇩🇪 Deutsch](./README.de.md) ·
[🇪🇸 Español](./README.es.md) ·
[🇫🇷 Français](./README.fr.md) ·
[🇮🇹 Italiano](./README.it.md)

</div>

---

## What this is

AxonOS is a `#![no_std]` `#![forbid(unsafe_code)]` Rust microkernel for
brain-computer interface (BCI) signal pipelines on Cortex-M class
microcontrollers.

It is designed for one specific class of system: a small, autonomous
device that acquires neural signals, classifies user intent, and drives
a stimulator or assistive interface in a closed loop, on a fixed
real-time budget, with no general-purpose operating system between the
silicon and the patient.

This is the kind of system where a missed deadline is not a performance
regression — it is an adverse event.

## Why it exists

Real-time BCI software today is built on three categories of foundation,
each with a structural mismatch to the problem:

1. **General-purpose kernels** (Linux, Windows) — designed for fairness
   and throughput, not bounded worst-case latency. Mainline scheduler
   jitter is on the order of milliseconds; PREEMPT_RT reduces this but
   does not eliminate it.

2. **Conventional RTOS** (FreeRTOS, Zephyr) — provide priority-based
   real-time scheduling but no formal schedulability proof, no
   memory-safety guarantee at the language level, and no BCI-domain
   abstractions.

3. **Application-class operating systems on application processors** —
   bring the full attack surface and unpredictability of a general OS
   to a regulated medical device.

AxonOS fills the gap: a small, analytically schedulable kernel, written
in a language that eliminates memory-safety defects at compile time,
with a capability model that prevents raw neural data from reaching
application code.

## What's different about it

| Property | AxonOS | Mainstream RTOS | Linux PREEMPT_RT |
|:---|:---|:---|:---|
| Scheduling policy | EDF (Liu–Layland) | Fixed-priority | CFS + RT |
| Analytical schedulability proof | Yes (in code) | No | No |
| Compile-time memory safety | Yes (Rust) | No (C) | No (C) |
| `unsafe` outside reviewable modules | Forbidden | Pervasive | Pervasive |
| Heap on hot path | None | Optional | Default |
| BCI capability isolation | Yes | None | None |
| Stated WCET with evidence level | Yes | No | No |
| Bounded model checking | 28 Kani proofs | No | No |

**Important honesty disclosure.** AxonOS does *not* claim formal
verification in the seL4 sense. It uses analytic real-time scheduling
theory (Liu–Layland), Rust's type system, bounded model checking via
Kani on the safety-critical surfaces, and a measurement-backed
validation taxonomy. This is weaker than machine-checked proofs of
functional correctness, but it is achievable today and aligns with
IEC 62304 Class C software lifecycle requirements.

## Evidence model

Every performance claim in AxonOS documentation is tagged with an
evidence level:

- **L1** — Analytically derived. Computed from algorithm and from the
  cycle-timing reference of the target ISA. Conservative; no hardware
  execution required.
- **L2** — Runtime measured. Observed by on-chip instrument (DWT cycle
  counter) on reference hardware over a stated interval and input
  distribution.
- **L3** — Independent instrument validated. Observed by an instrument
  external to the device under test (logic analyser, GPIO toggle
  points). Required for regulatory submission.
- **pending** — Measurement scheduled; falsification thresholds stated
  in advance.

### Current headline numbers

| Metric | Value | Level |
|:---|---:|:---|
| Pipeline analytical WCET (per epoch) | ≤ 642 µs | **L1** — derived from code |
| Synchronous busy-period response time `R₁` | ≤ 796 µs | **L1** — derived from code |
| CPU utilisation `U` (BCI task set) | 0.174 | **L1** — derived from code |
| Information-theoretic privacy bound (full catalogue) | ≤ 140.85 bits/s | **L1** — derived from code |
| Phase-1 GPIO-validated WCRT on STM32H573 fixture | — | **pending** — Q2 2026 |

All L1 numbers are computed by code in
[`axonos-kernels`](https://github.com/AxonOS-org/axonos-kernels) and
asserted in its test suite. Change the algorithm — the numbers change.
The numbers in the preprint are tied to verifiable computation in the
repository.

## Status

The AxonOS substrate is **pre-measurement**: the analytical foundation
is complete and code-verified; the runtime measurement against real
hardware is scheduled for Phase 1 (Q2 2026) and will be published with
raw waveform manifests, regardless of whether the predictions hold or
are refuted. The five pre-registered predictions (P1–P5) and their
falsification thresholds are documented in the preprint and in
RFC-0003.

## Repositories in this organisation

| Repository | Purpose | Status |
|:---|:---|:---|
| [`axonos-kernels`](https://github.com/AxonOS-org/axonos-kernels) | **Verifiable kernel substrate** — seven crates, 66 tests, 28 Kani proofs | Active · Apache-2.0 OR MIT |
| [`axonos-rfcs`](https://github.com/AxonOS-org/axonos-rfcs) | Engineering RFCs governing architecture decisions | Active · CC-BY-SA-4.0 |
| [`axonos-sdk`](https://github.com/AxonOS-org/axonos-sdk) | Application SDK — typed intents, capabilities, attestation | Active · Apache-2.0 OR MIT |
| [`axonos-consent`](https://github.com/AxonOS-org/axonos-consent) | AxonOS Consent Protocol reference implementation | Active · Apache-2.0 OR MIT |
| [`axonos-swarm`](https://github.com/AxonOS-org/axonos-swarm) | Multi-node coordination — Neural PTP, swarm scheduler | Active · Apache-2.0 OR MIT |

Phase-1 measurement results, reproducible benchmark fixtures, and the
preprint LaTeX source will be published alongside L3 validation
in Q2 2026.

## Audience — where to start

### Researchers in BCI and neural signal processing

You want a real-time substrate that does not impose its own opinions on
your signal pipeline, with predictable timing you can characterise and
a clean separation between raw acquisition and high-level intent output.

**Start with:** [`axonos-rfcs`](https://github.com/AxonOS-org/axonos-rfcs)
→ RFC-0001 (architecture), RFC-0004 (dual-core contract).

### Embedded systems engineers

You want a working example of `#![no_std]` `#![forbid(unsafe_code)]`
Rust applied to hard real-time scheduling on Cortex-M, with stated WCET
figures that distinguish derived from measured.

**Start with:** [`axonos-kernels`](https://github.com/AxonOS-org/axonos-kernels)
→ `cargo test --workspace` (66 tests in 10 seconds), then read the
crate READMEs in order: spsc → scheduler → capability → time → intent
→ kernel-core → firmware-stm32f407.

### Medical device engineers and regulatory teams

You want a kernel substrate whose architectural decisions are
documented as versioned RFCs, whose performance claims are tagged with
evidence levels, and whose roadmap explicitly addresses IEC 62304 Class
C alignment.

**Start with:** [`axonos-rfcs`](https://github.com/AxonOS-org/axonos-rfcs)
→ RFC-0003 (validation framework), RFC-0006 (intent wire format ABI).

### Clinical teams and rehabilitation centres

You want predictable, auditable software running the closed-loop
interface for your patients, with a partner who treats failure modes as
first-class documentation, not marketing surprises.

**Contact:** [connect@axonos.org](mailto:connect@axonos.org) — initial
conversation, clinical pilot pathway, MOU process.

## Roadmap

| Phase | Window | Deliverable |
|:---|:---|:---|
| **Phase 1** | Q2 2026 | GPIO-instrumented WCRT measurement on STM32H573 fixture. Falsification protocol P1–P5 executed and published regardless of outcome. |
| **Phase 2** | Q3–Q4 2026 | First 8-channel clinical kit deployment with the partner ALS rehabilitation centre (northeastern US). |
| **Phase 3** | 2027 | FDA Pre-Submission. Ferrocene-qualified toolchain integration. ISO 14971 risk management file. |

Independent replication of measurement methodology is encouraged and
welcomed. All measurement raw data will be published with SHA-256
manifests.

## Engineering principles

These are the rules the project lives by. They are not aspirational;
they are how decisions get made.

1. **No claim above its evidence level.** If we derived it analytically,
   we say L1. If we measured it on one board for 12 hours, we say L2.
   We do not say "validated" until we have L3.
2. **No `unsafe` in reviewable modules.** The only unsafe in the entire
   kernel substrate is two operations in `axonos-spsc`, each guarded by
   a Kani-verified invariant.
3. **No heap allocation on the hot path.** Static buffers, sized at
   compile time, sized to fit the WCET budget.
4. **No silent recovery from inconsistent state.** Poisoned mutexes,
   clock violations, and protocol mismatches surface as exhaustive
   error enums, not as defaults.
5. **No proprietary lock-in via the kernel.** All ABIs are published as
   RFCs under CC-BY-SA-4.0. Third-party implementations are welcomed.

## Intellectual property and licensing

| Component | Licence | Why |
|:---|:---|:---|
| Source code (`axonos-kernels`, `axonos-sdk`, `axonos-consent`, `axonos-swarm`) | **Apache-2.0 OR MIT** | Permissive dual licence. Use, modify, redistribute, commercialise. |
| Engineering RFCs (`axonos-rfcs`) | **CC-BY-SA-4.0** | Specifications spread further if they spread alike. |

Commercial use, modification, and redistribution are permitted. There
is no contributor licence agreement (CLA); contributions are accepted
under the inbound = outbound model used by the Rust project itself.

The name **"AxonOS"** is an unregistered word mark of Denis Yermakou.
Permission is granted to use the name to refer to the project and to
unmodified releases. Forks may state "based on AxonOS" as a factual
description; forks may not name themselves "AxonOS Pro" or similar in
a way that implies endorsement.

Full attribution requirements and patent grant in the `NOTICE` files
of each repository.

## Contact

- **General correspondence:** [info@axonos.org](mailto:info@axonos.org)
- **Partnership and clinical engagement:** [connect@axonos.org](mailto:connect@axonos.org)
- **Security disclosures:** [security@axonos.org](mailto:security@axonos.org) (GPG key on request)
- **Project website:** [axonos.org](https://axonos.org)
- **Long-form essays:** [medium.com/@AxonOS](https://medium.com/@AxonOS)

---

<div align="center">

**Author and maintainer:** Denis Yermakou · [denis@axonos.org](mailto:denis@axonos.org)

Zurich · Berlin · Milano · San Mateo · Singapore

<sub>Made with 🦀 and a long real-time tick.</sub>

</div>
