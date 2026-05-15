# AxonOS

> A bare-metal real-time kernel for brain-computer interfaces.
> Written in Rust. Open source. Built around evidence.

[🇬🇧 English](./README.md) ·
[🇯🇵 日本語](./README.ja.md) ·
[🇮🇹 Italiano](./README.it.md) ·
[🇨🇳 中文](./README.zh.md) ·
[🇩🇪 Deutsch](./README.de.md) ·
[🇪🇸 Español](./README.es.md) ·
[🇫🇷 Français](./README.fr.md)

---

## What this is

AxonOS is a `#![no_std]` `#![forbid(unsafe_code)]` Rust microkernel for
brain-computer interface (BCI) signal pipelines on Cortex-M class
microcontrollers.

It is designed for one specific class of system: a small, autonomous device
that acquires neural signals, classifies user intent, and drives a stimulator
or assistive interface in a closed loop, on a fixed real-time budget, with
no general-purpose operating system between the silicon and the patient.

This is the kind of system where a missed deadline is not a performance
regression — it is an adverse event.

## Why it exists

Real-time BCI software today is built on three categories of foundation,
each with a structural mismatch to the problem:

1. **General-purpose kernels** (Linux, Windows) — designed for fairness
   and throughput, not bounded worst-case latency. Mainline Linux scheduler
   jitter is on the order of milliseconds; PREEMPT_RT reduces this but does
   not eliminate it.

2. **Conventional RTOS** (FreeRTOS, Zephyr) — provide priority-based
   real-time scheduling but no formal schedulability proof, no memory-safety
   guarantee at the language level, and no BCI-domain abstractions.

3. **Application-class operating systems on application processors** —
   bring the full attack surface and unpredictability of a general OS to
   a regulated medical device.

AxonOS fills the gap: a small, analytically schedulable kernel, written in
a language that eliminates memory-safety defects at compile time, with a
capability model that prevents raw neural data from reaching application
code.

## What's different about it

| Property | AxonOS | Mainstream RTOS | Linux PREEMPT_RT |
|:---|:---|:---|:---|
| Scheduling policy | EDF (Liu–Layland) | Fixed-priority | CFS + RT |
| Analytical schedulability proof | Yes | No | No |
| Compile-time memory safety | Yes (Rust) | No (C) | No (C) |
| `unsafe`-free kernel logic | Yes | No | No |
| Heap on hot path | None | Optional | Default |
| BCI capability isolation | Yes | None | None |
| Stated WCET with evidence level | Yes (L1/L2) | No | No |

**Important honesty disclosure.** AxonOS does *not* claim formal verification
in the seL4 sense. It uses analytic real-time scheduling theory
(Liu–Layland) combined with Rust's type system and a measurement-backed
validation taxonomy. This is weaker than machine-checked proofs of
functional correctness, but it is achievable today and aligns with
IEC 62304 Class C software lifecycle requirements.

## Evidence model

Every performance claim in AxonOS documentation is tagged with an evidence level:

- **L1** — Instruction-count derived. Computed from compiled assembly
  against the published cycle-timing reference of the target ISA.
  Conservative; no hardware execution required.
- **L2** — Runtime measured. Observed by on-chip instrument (DWT cycle
  counter) on reference hardware over a stated interval and input distribution.
- **L3** — Independent oscilloscope-validated. Observed by an instrument
  independent of the device under test (logic analyser, GPIO toggle points).
  Required for regulatory submission.
- **pending** — Measurement not yet performed; target date stated.

Current headline numbers:

| Metric | Value | Level |
|:---|:---|:---|
| Pipeline WCET, single epoch | 640.2 µs | L1 |
| End-to-end WCRT | 972 µs | L2 |
| EDF jitter σ (10.8M epochs, 12 h) | 2.1 µs | L2 |
| EDF jitter P99.9 | 6.5 µs | L2 |
| Deadline misses observed | 0 of 10.8 × 10⁶ | L2 |
| CPU utilisation U′ (inflated WCET) | 0.179 | L1 |
| GPIO-validated WCRT (H573 fixture) | — | **pending** Q2 2026 |

Hardware: STM32F407 Cortex-M4F @ 168 MHz, ADS1299 8-channel 24-bit ADC,
ATECC608B secure element, nRF52840 BLE 5.3, ISO7741 5 kV galvanic isolation.

## What's in this organization

| Repository | Purpose | Status |
|:---|:---|:---|
| [`axonos-rfcs`](https://github.com/AxonOS-org/axonos-rfcs) | Engineering RFCs governing architecture decisions | 6 RFCs · CC-BY-SA-4.0 |
| [`axonos-sdk`](https://github.com/AxonOS-org/axonos-sdk) | Application SDK: typed intents, capabilities, attestation | v0.4.0 · Apache-2.0 OR MIT |
| [`axonos-consent`](https://github.com/AxonOS-org/axonos-consent) | AxonOS Consent Protocol reference implementation | v0.4.0 · Apache-2.0 OR MIT |
| [`axonos-swarm`](https://github.com/AxonOS-org/axonos-swarm) | Multi-node coordination: Neural PTP, swarm scheduler, fault detector | v0.1.0 · Apache-2.0 OR MIT |
| [`axon-bci-gateway`](https://github.com/AxonOS-org/axon-bci-gateway) | Reference application gateway (fork, with attribution) | Active · Apache-2.0 |

The reproducible benchmark fixtures and the preprint LaTeX source will be
published alongside the L3 validation results in Q2 2026.

## Audience

This project is built with four audiences in mind. If you fit one of these,
start where indicated.

### Researchers in BCI and neural signal processing

You want a real-time substrate that does not impose its own opinions on
your signal pipeline, with predictable timing you can characterise and a
clean separation between raw acquisition and high-level intent output.

Start with: [`axonos-rfcs`](https://github.com/AxonOS-org/axonos-rfcs) →
RFC-0001 (architecture) and RFC-0004 (dual-core contract).

### Embedded systems engineers

You want a working example of `#![no_std]` `#![forbid(unsafe_code)]` Rust
applied to hard real-time scheduling on Cortex-M, with stated WCET figures
that distinguish derived from measured.

Start with: [`axonos-sdk`](https://github.com/AxonOS-org/axonos-sdk) →
examples in `examples/bare_metal_no_std.rs`.

### Medical device engineers and regulatory teams

You want a kernel substrate whose architectural decisions are documented
as versioned RFCs, whose performance claims are tagged with evidence levels,
and whose roadmap explicitly addresses IEC 62304 Class C alignment.

Start with: [`axonos-rfcs`](https://github.com/AxonOS-org/axonos-rfcs) →
RFC-0005 (validation framework) and RFC-0006 (stable ABI candidate).

### Clinical teams and rehabilitation centres

You want predictable, auditable software running the closed-loop interface
for your patients, with a partner who treats failure modes as first-class
documentation, not marketing surprises.

Contact: [connect@axonos.org](mailto:connect@axonos.org) — initial conversation,
clinical pilot pathway, MOU process.

## Roadmap

**Q2 2026 — Phase 1: L3 validation**
- GPIO-instrumented WCRT measurement on STM32H573 fixture with Saleae Logic Pro 16
- Direct power consumption measurement on reference board
- RFC-0006 promoted from candidate to stable based on validated ABI

**Q3–Q4 2026 — Phase 2: Clinical pilot**
- First 8-channel clinical kit deployment
- Pilot at partner ALS rehabilitation centre, northeastern US (MOU in place)
- Online classifier performance reported alongside offline benchmark

**2027 — Phase 3: Regulatory pathway**
- FDA Pre-Submission (Q-Sub)
- Ferrocene qualified toolchain integration
- ISO 14971 full risk management file

**Continuous**
- Independent replication of measurement methodology encouraged and welcomed
- All measurement raw data published with SHA-256 manifests

## Engineering principles

These are the rules the project lives by. They are not aspirational; they
are how decisions get made.

1. **No claim above its evidence level.** If we measured it on one board
   for 12 hours, we say "L2"; we do not say "validated".
2. **No `unsafe` in reviewable modules.** Hardware register access lives
   in audited PAC crates; everything else is `#![forbid(unsafe_code)]`.
3. **No heap allocation on the hot path.** Static buffers, sized at
   compile time, sized to fit the WCET budget.
4. **No silent recovery from inconsistent state.** Poisoned mutexes,
   clock violations, and protocol mismatches surface as errors, not
   defaults.
5. **No proprietary lock-in via the kernel.** The ABI is published as
   an RFC under CC-BY-SA-4.0. Third-party implementations are welcomed.

## License

- **Source code** (`axonos-sdk`, `axonos-consent`, `axonos-swarm`):
  Apache-2.0 OR MIT — your choice.
- **Engineering RFCs** (`axonos-rfcs`): CC-BY-SA-4.0.
- **Reference application gateway** (`axon-bci-gateway`): Apache-2.0
  (with upstream attribution preserved per the original license).

Commercial use, modification, and redistribution are permitted under these
terms. There is no contributor licence agreement (CLA) required for accepted
pull requests; contributors retain copyright over their contributions.

## Contact

- **General correspondence:** [info@axonos.org](mailto:info@axonos.org)
- **Security disclosures:** [security@axonos.org](mailto:security@axonos.org)
  (GPG key on request)
- **Web:** [axonos.org](https://axonos.org)
- **Writing:** [medium.com/@AxonOS](https://medium.com/@AxonOS)

---

axonos.org · medium.com/@AxonOS · info@axonos.org
