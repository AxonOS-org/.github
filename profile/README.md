<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/AxonOS-org/.github/raw/main/profile/assets/hero-dark.svg">
  <img alt="AxonOS — deterministic infrastructure for brain–computer interfaces. Hard real-time by design, no_std Rust, Kani-checked logic, consent below the application layer." src="https://github.com/AxonOS-org/.github/raw/main/profile/assets/hero-light.svg" width="100%">
</picture>

**[axonos.org](https://axonos.org)** · **[DY-WCET](https://github.com/DYResearch/dy-wcet)** · **[Radar](https://axonos-bci.github.io/axonos-community-radar/)** · **[DY Research](https://dyresearch.github.io)** · **[DY PROOF](https://dy-proof.github.io)** · **[Specifications](https://axonos.org/specifications.html)** · **[Articles](https://medium.com/@AxonOS)**

[![Kernel](https://img.shields.io/github/v/tag/AxonOS-org/axonos-kernel?sort=semver&style=flat-square&label=kernel&labelColor=0d1117&color=1f8fae)](https://github.com/AxonOS-org/axonos-kernel/releases)
[![Consent](https://img.shields.io/github/v/tag/AxonOS-org/axonos-consent?sort=semver&style=flat-square&label=consent&labelColor=0d1117&color=1f8fae)](https://github.com/AxonOS-org/axonos-consent/releases)
[![Protocol](https://img.shields.io/github/v/tag/AxonOS-org/axonos-protocol?sort=semver&style=flat-square&label=protocol&labelColor=0d1117&color=1f8fae)](https://github.com/AxonOS-org/axonos-protocol/releases)
[![Standard](https://img.shields.io/github/v/tag/AxonOS-org/axonos-standard?sort=semver&style=flat-square&label=standard&labelColor=0d1117&color=1f8fae)](https://github.com/AxonOS-org/axonos-standard/releases)
[![Kani](https://img.shields.io/badge/properties%20proven-Kani-2ea043?style=flat-square&labelColor=0d1117)](#the-numbers-and-where-each-one-comes-from)
[![License](https://img.shields.io/badge/license-Apache--2.0%20OR%20MIT-8b949e?style=flat-square&labelColor=0d1117)](#licensing)
[![Ecosystem pulse](https://img.shields.io/endpoint?url=https%3A%2F%2Faxonos-bci.github.io%2Faxonos-community-radar%2Fdata%2Fbadge-ecosystem.json&style=flat-square&labelColor=0d1117)](https://axonos-bci.github.io/axonos-community-radar/)
[![AxonOS Radar](https://img.shields.io/badge/AxonOS%20Radar-open%20neurotech%20map-1f8fae?style=flat-square&labelColor=0b1220)](https://axonos-bci.github.io/axonos-community-radar/)

</div>

AxonOS is the hard real-time layer between neural hardware and the applications
that use it: an open-source kernel in `#![no_std]` Rust on ARM Cortex-M, designed
so that worst-case response times are **analysed before they run, not benchmarked
after**, and
privacy enforced **below the application layer**, where no application can
bypass it.

> Applications receive typed, consent-bound intent events — never raw neural streams.

It is not an AI-agent framework, a chatbot runtime or a token project. Every
guarantee it makes is specified, openly licensed, and built to be checked by
someone else.

> [!NOTE]
> **The AxonOS Reference BCI.** One command carries synthetic EEG through every
> AxonOS component, withdraws consent mid-session and counts, at the application,
> what still arrives: **zero**. Building it found the gap that would have made it
> twelve — a withdrawal that stopped intents while derived data kept flowing under
> a live grant. Fixed, kept as a test that must fail, and proposed as a requirement
> for every implementation in [RFC-0012](https://github.com/AxonOS-org/axonos-rfcs/blob/main/rfcs/0012-consent-withdrawal-reaches-every-disclosure-channel.md).
> **[Long read](https://gist.github.com/AxonOS-BCI/b5cf55b5ce6a901bbeb0a34faaa1fd8a)** ·
> **[axonos-stack 0.4.0](https://github.com/AxonOS-org/axonos-stack/releases/tag/v0.4.0)**

> [!NOTE]
> **axonos-consent 0.9.2.** Consent now changes only on a verified Ed25519
> signature, never twice for the same sequence number, and a withdrawal is final
> the instant it is stored. Ten Kani proofs, three loom models, twenty
> conformance vectors and three fuzz targets run on every push. The line closes
> [AXC-2026-001](https://github.com/AxonOS-org/axonos-consent/blob/main/docs/advisories/AXC-2026-001.md), a critical advisory
> against our own consent layer, published with its fix.
> **[Release notes](https://github.com/AxonOS-org/axonos-consent/releases/tag/v0.9.2)** ·
> **[Specification](https://github.com/AxonOS-org/axonos-consent/blob/main/SPEC.md)**

---

## The ecosystem

<table>
<tr>
<td width="50%" valign="top">

**Build — [AxonOS](https://axonos.org)**<br>
The operating layer: kernel, signal pipeline, consent, protocol and SDK.
Specified openly, verified by machine.

</td>
<td width="50%" valign="top">

**Measure — [DY-WCET](https://github.com/DYResearch/dy-wcet)**<br>
Worst-case response-time analysis in integer arithmetic. Zero dependencies,
eight Kani proofs, every one closing in CI.

</td>
</tr>
<tr>
<td width="50%" valign="top">

**Discover — [Radar](https://axonos-bci.github.io/axonos-community-radar/)**<br>
A living map of open neurotech: over a hundred projects, scored from public
evidence and refreshed every three hours.

</td>
<td width="50%" valign="top">

**Verify — [DY Research](https://dyresearch.github.io)**<br>
Independent technical due diligence for investors, founders and engineering
teams. A written verdict on what the evidence supports.

</td>
</tr>
<tr>
<td colspan="2" valign="top">

**Prove — [DY PROOF](https://dy-proof.github.io)**<br>
Independent technology diagnostics: where a running system breaks under load,
located and reproduced.

</td>
</tr>
</table>

---

## In focus · DY-WCET

**Timing analysis that refuses rather than rounds.** Worst-case response time
for real-time systems, computed exactly in integer arithmetic — and a named
refusal wherever a bound cannot be justified.

Two tasks. A runs 100 µs every 400 µs at higher priority; B runs 200 µs every
1,000 µs. The common answer for B is 400 µs. The correct one is **300 µs** —
and with other periods, the same mistake reports a deadline as met that is
missed on hardware.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/AxonOS-org/.github/raw/main/profile/assets/dywcet-schedule-dark.svg">
  <img alt="The schedule for the two tasks: A preempts B at the start, B runs from 100 to 300 microseconds and finishes long before its 1,000 microsecond deadline." src="https://github.com/AxonOS-org/.github/raw/main/profile/assets/dywcet-schedule-light.svg" width="100%">
</picture>

<sub>The schedule, drawn by simulating the scheduler rather than the formula. On 5,000 random task pairs it lands exactly on the analysis's answer.</sub>

<table>
<tr><td align="right"><b>0</b></td><td>dependencies, and no floating point anywhere</td></tr>
<tr><td align="right"><b>8</b></td><td>Kani proofs, every one closing in CI</td></tr>
<tr><td align="right"><b>100</b></td><td>tests, fifteen of them derived by hand</td></tr>
<tr><td align="right"><b>6</b></td><td>named refusals — a bound is never guessed</td></tr>
</table>

**[Try it live →](https://dyresearch.github.io/wcet/)** · [Source](https://github.com/DYResearch/dy-wcet) · [The method](https://gist.github.com/AxonOS-BCI/3bef2ff217a3ece45e4958fac2c16c4a) · [The bounty](https://github.com/DYResearch/dy-wcet/blob/main/BOUNTY.md)

---

## The architecture

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/AxonOS-org/.github/raw/main/profile/assets/architecture-dark.svg">
  <img alt="The AxonOS stack from electrodes to applications: hardware abstraction, signal pipeline, kernel designed to a 1,000 microsecond response-time target and a 0.5 microsecond IPC target, consent that changes only on a verified signature and whose withdrawal is final, SDK and protocol, then a privacy boundary that raw neural data never crosses, then applications." src="https://github.com/AxonOS-org/.github/raw/main/profile/assets/architecture-light.svg" width="100%">
</picture>

---

## The numbers, and where each one comes from

Every figure published here, its evidence level, and the artefact it derives
from. **L1** formally proven · **L2** measured on reference hardware · **L3**
independently reproduced · **CI** checked mechanically on every push.
Graded as in
[`CLAIMS.md`](https://github.com/AxonOS-org/axonos-standard/blob/main/CLAIMS.md), which this table follows. A figure
absent from this table is not claimed.

| Figure | Value | Source |
|:--|:--|:--|
| End-to-end WCRT | **not claimed** | ≤ 1,000 µs is the Standard's DC1 requirement, not a result: no proof of it and no reference-hardware trace exist yet. The [scheduler harnesses](https://github.com/AxonOS-org/axonos-kernel/blob/main/axonos-scheduler/kani-proofs/src/main.rs) prove admission and EDF selection, not a time |
| IPC slot latency | **not claimed** | ≤ 0.5 µs is the DC3 requirement. The [SPSC harnesses](https://github.com/AxonOS-org/axonos-kernel/blob/main/axonos-spsc/kani-proofs/src/main.rs) prove the slot loop-free and FIFO, not a time |
| Consent changes only on an authenticated frame; withdrawal is final | proven · **L1** | [`src/proofs.rs`](https://github.com/AxonOS-org/axonos-consent/blob/main/src/proofs.rs) · ten harnesses, a blocking CI job · *the former `kani/` harnesses never compiled and are removed* |
| Consent withdrawal, transition time | **retracted** at consent 0.9.0 | the 1,648-cycle figure was derived for a tag path that no longer exists; Ed25519 verification now dominates admission · [SPEC §4.1](https://github.com/AxonOS-org/axonos-consent/blob/main/SPEC.md#41-the-transition) |
| Kani proofs re-run in CI | 57 · **L1** | consent 10 · signal pipeline 9 · DY-WCET 8 as blocking jobs on every push · kernel 30 on every push as advisory jobs and as a blocking gate on release tags |
| `unsafe` in the kernel | one crate · **CI** | confined to `axonos-spsc`; `#![forbid(unsafe_code)]` in consent, protocol and five kernel crates |
| Wire format, reference against SDK | byte-identical · **CI** | [conformance](https://github.com/AxonOS-org/axonos-conformance): Python reference and Rust SDK on every push; C header by `_Static_assert` |
| Post-withdrawal leakage, reference BCI | 0 · **CI** | [`reference-bci-7.txt`](https://github.com/AxonOS-org/axonos-stack/blob/main/reference/reference-bci-7.txt) · counted at the application on a host, synthetic input · no timing claimed |
| Projects on the live map | 100+ · live | [`data/radar.json`](https://github.com/AxonOS-BCI/axonos-community-radar/blob/main/data/radar.json), refreshed every 3 h |

**No timing figure is claimed.** A proof of a property, a proof of a time and a
measurement are different kinds of statement, and only the first exists today.
The first reference-hardware trace will land in
[`axonos-validation`](https://github.com/AxonOS-org/axonos-validation), raw, whatever
it shows; until then no microsecond figure appears in this table.
**L3 independent reproduction is not claimed for anything.**

<sub>Not in this table, and therefore not claimed: classification accuracy, information transfer rate, power draw, on-hardware latency in a deployment, session length, electrode count in real use.</sub>

---

## Verify it yourself

One command, ninety seconds, no account:

```sh
git clone https://github.com/AxonOS-org/axonos-stack && cd axonos-stack
cargo run --locked --bin session -- --seed 7 --frames 3000 | diff - reference/session-7.txt
```

Silence means the whole chain — electrode to conditioning to privacy boundary
to the right to act — reproduced byte for byte on your machine. The session is
not a happy path: an electrode lifts partway through, and the transcript records
the system withdrawing the right to actuate 96 ms later while it keeps recording.

Then the consent boundary, counted where the data arrives:

```sh
cargo run --locked --release --bin reference_bci | tail -1
```

`RESULT: VERIFIED` means that after consent is withdrawn at second 36, nothing —
no raw sample, no derived reading, no decoded intent — reached the application,
and that a second run reproduced every digest. [How it works, and what it does not show →](https://gist.github.com/AxonOS-BCI/b5cf55b5ce6a901bbeb0a34faaa1fd8a)

<details>
<summary><b>More to run</b> — the path, the kernel proofs, the signal chain, the timing analysis</summary>

<br>

```sh
# the full path, electrode to typed intent, verified bit for bit
git clone https://github.com/AxonOS-org/axonos-e2e-demo && cd axonos-e2e-demo && ./run.sh --verify

# the kernel: its tests, then a machine-checked proof
git clone https://github.com/AxonOS-org/axonos-kernel && cd axonos-kernel
cargo test --workspace
cargo kani setup && ( cd axonos-spsc/kani-proofs && cargo kani )

# the signal chain, bit-exact against conformance vectors
git clone https://github.com/AxonOS-org/axonos-signal-pipeline && cd axonos-signal-pipeline && cargo test

# the timing analysis, and every number it states against its source
git clone https://github.com/DYResearch/dy-wcet && cd dy-wcet && cargo test && ./audit.sh
```

</details>

<details>
<summary><b>Where to push, if you want to prove this wrong</b></summary>

<br>

- **The scheduler.** The harnesses prove admission and EDF selection for two tasks with periods up to 8; a counterexample from Kani within that domain refutes them outright. The 1,000 µs bound is a requirement the kernel has yet to meet with evidence, so there is no timing claim to refute.
- **Consent.** Run `cargo kani` in `axonos-consent`: the ten harnesses in [`src/proofs.rs`](https://github.com/AxonOS-org/axonos-consent/blob/main/src/proofs.rs), the job CI runs on every push. Or forge a frame: the `auth_forgery` fuzz target verifies against a key whose secret no one holds, so any frame it admits is a forgery.
- **dy-wcet.** Find a task set where it returns a bound the recurrence does not support. There is [a bounty](https://github.com/DYResearch/dy-wcet/blob/main/BOUNTY.md) for the first one.
- **The Radar's scores.** Every score is published with the evidence it rests on. Recompute any of them.

</details>

---

## The open BCI field, live

<!-- RADAR:START -->
A living map of every open-source brain–computer-interface project, tool and team,
scored from public evidence and refreshed every three hours. AxonOS is ranked by the same
formula as everyone else, with no boosting.

<p align="center"><img src="https://img.shields.io/badge/projects-120-1f8fae?style=flat-square&labelColor=0d1117" alt="projects: 120"> <img src="https://img.shields.io/badge/active_30d-115-2ea043?style=flat-square&labelColor=0d1117" alt="active 30d: 115"> <img src="https://img.shields.io/badge/total_stars-47.9k-1f8fae?style=flat-square&labelColor=0d1117" alt="total stars: 47.9k"> <img src="https://img.shields.io/badge/builders-8-1f8fae?style=flat-square&labelColor=0d1117" alt="builders: 8"></p>

<p align="center"><a href="https://axonos-bci.github.io/axonos-community-radar/report.html"><b>The State of Open BCI — read the full report →</b></a></p>

<p align="center"><sub>Leading by reach: <code>omi</code> · <code>wukong-robot</code> · <code>mne-python</code> · <code>NeuroKit</code> · 17 languages · last refreshed <b>10 Oct 2026, 06:24 UTC</b></sub></p>
<!-- RADAR:END -->

---

## Work with DY Research

The discipline behind AxonOS, applied to your system. DY Research carries out
independent technical due diligence for investors, founders and engineering
teams: every claim traced to its code, its tests and its evidence, ending in a
written verdict.

| Engagement | The question it answers |
|:--|:--|
| **Snapshot** · 5 business days | What does this technology actually do, and what does its evidence support? |
| **Focused Audit** · 2–3 weeks | Does one critical property — timing, determinism, concurrency — actually hold? |
| **Due Diligence** · 3–4 weeks | Is the technology what the company says it is, and what could break the investment? |

Fixed scope, agreed in writing before any work begins; pricing on request. Revenue
funds AxonOS. **[Engagements and full scope →](https://dyresearch.github.io/#engagements)**

---

## Repositories

| Repository | Role |
|:--|:--|
| [`axonos-kernel`](https://github.com/AxonOS-org/axonos-kernel) | Scheduler, lock-free SPSC IPC, capabilities, intent, time — `#![no_std]` |
| [`axonos-signal-pipeline`](https://github.com/AxonOS-org/axonos-signal-pipeline) | Conditioning, DSP and classification, bit-exact against conformance vectors |
| [`axonos-consent`](https://github.com/AxonOS-org/axonos-consent) | Consent enforced by the kernel: Ed25519-authenticated, replay-proof, final the instant it is withdrawn |
| [`axonos-protocol`](https://github.com/AxonOS-org/axonos-protocol) · [`axonos-sdk`](https://github.com/AxonOS-org/axonos-sdk) | The wire format and the application interface |
| [`axonos-hal`](https://github.com/AxonOS-org/axonos-hal) | Hardware abstraction for ARM Cortex-M |
| [`axonos-stack`](https://github.com/AxonOS-org/axonos-stack) · [`axonos-e2e-demo`](https://github.com/AxonOS-org/axonos-e2e-demo) | The layers running as one system, reproducible from a seed |
| [`axonos-standard`](https://github.com/AxonOS-org/axonos-standard) · [`axonos-rfcs`](https://github.com/AxonOS-org/axonos-rfcs) | The specification, its claims ledger and its design records |
| [`axonos-conformance`](https://github.com/AxonOS-org/axonos-conformance) · [`axonos-validation`](https://github.com/AxonOS-org/axonos-validation) | Test vectors and bindings; measurement campaigns and their traces |
| [`DYResearch/dy-wcet`](https://github.com/DYResearch/dy-wcet) | Worst-case response-time analysis, standalone |
| [`AxonOS-BCI/axonos-community-radar`](https://github.com/AxonOS-BCI/axonos-community-radar) | The live map of open neurotech |

---

## Stated plainly

AxonOS does not currently claim, and this organisation must not be read as
claiming: FDA clearance, CE marking or medical-device approval in any
jurisdiction; clinical efficacy or independent clinical validation; certified
medical-device status or production-implant readiness; complete compliance with
IEC 62304, ISO 14971 or ISO 13485. These are possible future milestones, not
present facts.

<details>
<summary><b>Five problems nobody has solved, AxonOS included</b></summary>

<br>

- Calibration-free decoding across subjects
- Worst-case execution time on a modern core
- Long-session non-stationarity
- Enforcing consent at the point of use
- Establishing that a signal is voluntary

</details>

---

## Cite this work

```bibtex
@article{axonos2026microkernel,
  title   = {An Analytical Microkernel Design for Safety-Critical
             Brain--Computer Interfaces: Schedulability, Capability
             Isolation, and Falsifiable Predictions},
  author  = {Yermakou, Denis},
  year    = {2026},
  doi     = {10.5281/zenodo.20552007},
  url     = {https://doi.org/10.5281/zenodo.20552007},
  note    = {Analytical bounds; predictions P1--P5; no measurement claims},
  license = {CC-BY-4.0}
}
```

Every repository exposes **Cite this repository** through [`CITATION.cff`](https://github.com/AxonOS-org/.github/blob/main/CITATION.cff).

## Licensing

| Artefact | License |
|:--|:--|
| Kernel, SDK, consent, swarm, gateway | Apache-2.0 OR MIT |
| RFCs and specifications | CC-BY-SA-4.0 |
| `axon-bci-gateway` | MIT, preserved from upstream OpenBCI_GUI |
| `neural-boundary-game` | AGPL-3.0-only OR AxonOS Commercial |

---

<div align="center">

© The AxonOS Project / Denis Yermakou

[connect@axonos.org](mailto:connect@axonos.org) · [security@axonos.org](mailto:security@axonos.org) · [LinkedIn](https://www.linkedin.com/in/axonos) · [axonos.org](https://axonos.org)

<sub>Offices and a headquarters are under consideration for the future.</sub>

<sub>[日本語](https://github.com/AxonOS-org/.github/blob/main/profile/README.ja.md) · [中文](https://github.com/AxonOS-org/.github/blob/main/profile/README.zh.md) · [Italiano](https://github.com/AxonOS-org/.github/blob/main/profile/README.it.md) · [Français](https://github.com/AxonOS-org/.github/blob/main/profile/README.fr.md) · [Deutsch](https://github.com/AxonOS-org/.github/blob/main/profile/README.de.md) · [Español](https://github.com/AxonOS-org/.github/blob/main/profile/README.es.md) · [العربية](https://github.com/AxonOS-org/.github/blob/main/profile/README.ar.md) — translations summarise this page; the English page is canonical.</sub>

</div>
