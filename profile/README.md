<div align="center">

# AxonOS

### A real-time Rust kernel for brain-computer interface systems

A `#![no_std]` Rust microkernel for safety-critical BCI applications. Deterministic scheduling, bounded worst-case execution, hardware-gated stimulation interlock. 2.1 µs jitter σ. Zero deadline misses over 10.8 M measured epochs. No heap on the hot path. No `unsafe` anywhere.

[![Website](https://img.shields.io/badge/axonos.org-000000?style=for-the-badge&logoColor=white)](https://axonos.org)
[![Medium](https://img.shields.io/badge/Medium-02b875?style=for-the-badge&logo=medium&logoColor=white)](https://medium.com/@AxonOS)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/axonos)
[![dev.to](https://img.shields.io/badge/dev.to-0A0A0A?style=for-the-badge&logo=devdotto&logoColor=white)](https://dev.to/axonosorg)
[![Email](https://img.shields.io/badge/axonosorg%40gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:axonosorg@gmail.com)

</div>

---

## What is here

| Repository | Status | What it is |
|:---|:---:|:---|
| [`axonos-consent`](https://github.com/AxonOS-org/axonos-consent) | **v0.2.2** | The Rust reference implementation of the MMP Consent Extension v0.1.0. `#![no_std]`, zero allocation, 15/15 conformance vectors PASS. |
| [`axonos-sdk`](https://github.com/AxonOS-org/axonos-sdk) | **v0.1.0 pre-release** | Application-facing SDK — typed intent events, capability manifests, mesh consent facade. |

Both crates are dual-licensed Apache-2.0 OR MIT.

## Protocol stack

AxonOS implements the Mesh Memory Protocol (MMP) v0.2.3, an open specification from SYM.BOT (CC-BY-4.0). The MMP Consent Extension v0.1.0 defines a per-peer state machine and wire format for consent enforcement; AxonOS is the Rust reference implementation of that extension on bare-metal Cortex-M hardware.

Enforcement sits at Layer 2, below the SVAF coupling engine specified in arXiv:2604.03955.

## Collaborations

| Partner | Role |
|:---|:---|
| SYM.BOT | MMP specification author (CC-BY-4.0); MMP Consent Extension specification author. AxonOS implemented the Rust reference implementation. |

## Headline metrics (measured on STM32F407 @ 168 MHz)

| | |
|:---|:---|
| Jitter σ | **2.1 µs** (630× better than Linux mainline, 180× better than PREEMPT_RT) |
| WCRT | **972 µs** measured over 12 h / 10.8 M epochs |
| Deadline misses | **0** |
| Zero-calibration classifier accuracy | **91.7 %** 2-class at ~70 s (no labelled training session) |
| `axonos-consent` conformance | **15 / 15** canonical vectors PASS |

Every figure above is either instruction-count derived on published reference hardware or measured over a named interval. No marketing numbers. Full derivation in the [architecture series](https://medium.com/@AxonOS).

## Writing

40+ architecture articles documenting every major design decision: scheduler, zero-copy signal path, Riemannian classifier, dual-core real-time contract, swarm synchronization, hardware interlock, hardware reference design, clinical path, business case.

Primary: [medium.com/@AxonOS](https://medium.com/@AxonOS) · Mirror: [dev.to/axonosorg](https://dev.to/axonosorg)

## Specification attribution

AxonOS implements protocol specifications authored by SYM.BOT.

- **Mesh Memory Protocol (MMP) v0.2.3** — authored by SYM.BOT, published at sym.bot/spec/mmp, CC-BY-4.0.
- **MMP Consent Extension v0.1.0** — specification authored by SYM.BOT, CC-BY-4.0.
- **Symbolic-Vector Attention Fusion (SVAF)** — authored by Hongwei Xu, arXiv:2604.03955.

AxonOS did not author, co-author, or contribute to these specifications. The `axonos-consent` Rust source code is independent work by AxonOS.

## Contact

Denis Yermakou, founder. Singapore.
Engineering questions, research collaboration, commercial support, clinical partnerships — one email address, read personally.

📧 **axonosorg@gmail.com**

Enterprise support tiers (Foundation $5k, Integration $15k, Clinical contact) for teams integrating AxonOS into regulated devices — see [axonos.org/enterprise](https://axonos.org/enterprise.html).

---

<div align="center">
<sub>© 2026 Denis Yermakou · AxonOS · Dual-licensed Apache-2.0 OR MIT</sub>
</div>
