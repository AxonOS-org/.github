<div align="center">

<img src="https://axonos.org/assets/img/logo-256.png" width="96" alt="AxonOS logo">

# AxonOS

### A real-time Rust kernel for brain-computer interface systems

A `#![no_std]` Rust microkernel for safety-critical BCI applications.  
Deterministic EDF scheduling · Zero-copy signal path · Hardware-gated stimulation interlock  
`#![forbid(unsafe_code)]` · Cortex-M4F / M33 · Singapore

[![Website](https://img.shields.io/badge/axonos.org-111111?style=for-the-badge)](https://axonos.org)
[![RFCs](https://img.shields.io/badge/RFCs-5_active-2d6a9f?style=for-the-badge)](https://github.com/AxonOS-org/axonos-rfcs)
[![Medium](https://img.shields.io/badge/Medium-42_articles-02b875?style=for-the-badge&logo=medium&logoColor=white)](https://medium.com/@AxonOS)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/axonos)
[![Email](https://img.shields.io/badge/info@axonos.org-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:info@axonos.org)

</div>

---

## Repositories

| Repository | Version | Description |
|:---|:---:|:---|
| [`axonos-consent`](https://github.com/AxonOS-org/axonos-consent) | **v0.2.2** | Rust reference implementation of the MMP Consent Extension v0.1.0. `#![no_std]`, zero-alloc critical path, security-bounded CBOR decoder, exhaustive 3×3 state machine. 15/15 interop vectors PASS. |
| [`axonos-sdk`](https://github.com/AxonOS-org/axonos-sdk) | **v0.1.1** | Application-facing SDK — typed intent events, capability manifests, mesh consent facade. `#![no_std]` compatible. |
| [`axonos-rfcs`](https://github.com/AxonOS-org/axonos-rfcs) | **5 active** | Engineering design documents. Every architectural decision is specified in writing before the corresponding code ships. CC-BY-SA-4.0. |
| [`axon-bci-gateway`](https://github.com/AxonOS-org/axon-bci-gateway) | **v1.0.0-axonos** | OpenBCI_GUI integration fork for hardware-in-the-loop testing with the AxonOS signal pipeline. |

All Rust crates are dual-licensed **Apache-2.0 OR MIT**.

---

## Measured performance

Every number below is tagged by the evidence level it rests on, per [RFC-0003](https://github.com/AxonOS-org/axonos-rfcs/blob/main/rfcs/0003-validation-status-framework.md):  
`L1` = instruction-count derived · `L2` = runtime measured on reference hardware · `L3` = oscilloscope-validated (pending Q2 2026)

| Metric | Value | Level |
|:---|:---|:---:|
| Pipeline WCET (M4F · 168 MHz) | 640.2 µs | `L1` |
| End-to-end WCRT | 972 µs | `L2` |
| Sample population | 10.8 M epochs / 12 h continuous | `L2` |
| Deadline misses | 0 | `L2` |
| EDF jitter σ | 2.1 µs | `L2` |
| EDF jitter P99.9 | 6.5 µs | `L2` |
| 4-class motor imagery accuracy | 82.4 % (full calibration) | `L2` |
| 2-class ZeroCalib accuracy (~70 s) | 91.7 % | `L2` |
| Information transfer rate | 40.3 bits/min | `L2` |
| GPIO-validated WCRT (H573 fixture) | — | `pending Q2 2026` |
| `axonos-consent` interop vectors | 15 / 15 PASS | `L2` |

Reference hardware: STM32F407 Cortex-M4F @ 168 MHz · ADS1299 8-channel 24-bit ADC · ATECC608B · nRF52840 BLE 5.3

---

## Engineering RFCs

| RFC | Title | Track |
|:---|:---|:---:|
| [RFC-0001](https://github.com/AxonOS-org/axonos-rfcs/blob/main/rfcs/0001-edf-scheduler-biological-deadlines.md) | EDF Scheduler with Biological Deadlines | scheduling |
| [RFC-0002](https://github.com/AxonOS-org/axonos-rfcs/blob/main/rfcs/0002-zero-copy-ring-buffer.md) | Zero-Copy Ring Buffer for Signal Path | memory |
| [RFC-0003](https://github.com/AxonOS-org/axonos-rfcs/blob/main/rfcs/0003-validation-status-framework.md) | Validation Status Framework (L1 / L2 / L3) | process |
| [RFC-0004](https://github.com/AxonOS-org/axonos-rfcs/blob/main/rfcs/0004-dual-core-real-time-contract.md) | Dual-Core Real-Time Contract | scheduling |
| [RFC-0005](https://github.com/AxonOS-org/axonos-rfcs/blob/main/rfcs/0005-capability-based-app-manifest.md) | Capability-Based Application Manifest | security |

---

## Protocol attribution

AxonOS implements protocol specifications authored by SYM.BOT.

| Specification | Author | License |
|:---|:---|:---:|
| Mesh Memory Protocol (MMP) v0.2.3 | SYM.BOT | CC-BY-4.0 |
| MMP Consent Extension v0.1.0 | SYM.BOT | CC-BY-4.0 |
| Symbolic-Vector Attention Fusion (SVAF) | Hongwei Xu · [arXiv:2604.03955](https://arxiv.org/abs/2604.03955) | — |

`axonos-consent` is the Rust reference implementation of the MMP Consent Extension. The Rust source code is independent work by AxonOS, implemented against the specification authored by SYM.BOT. AxonOS did not author, co-author, or contribute to the specifications above.

---

## Writing

42 long-form technical articles on EDF scheduling, zero-copy signal path, Riemannian transfer learning, dual-core real-time contract, swarm synchronisation, hardware-gated consent, and the clinical deployment path.

Primary: [medium.com/@AxonOS](https://medium.com/@AxonOS) · Mirror: [dev.to/axonosorg](https://dev.to/axonosorg)

---

## Contact

Denis Yermakou — founder and principal engineer. Singapore.

| Purpose | Address |
|:---|:---|
| General | [info@axonos.org](mailto:info@axonos.org) |
| Investors | [invest@axonos.org](mailto:invest@axonos.org) |
| Clinical partnerships | [clinical@axonos.org](mailto:clinical@axonos.org) |
| Security disclosures | [security@axonos.org](mailto:security@axonos.org) |

Full contact directory: [axonos.org/contact](https://axonos.org/contact.html)

---

<div align="center">
<sub>© 2026 Denis Yermakou · AxonOS · Rust crates Apache-2.0 OR MIT · Documentation CC-BY-SA-4.0</sub>
</div>
