<div align="center">

<img src="./banner.jpg" alt="AxonOS — offenes kognitives Betriebssystem für Gehirn-Computer-Schnittstellen" width="100%" />

<br/>
<br/>

# **axonos**

### Das offene kognitive Betriebssystem für Gehirn-Computer-Schnittstellen.

*Die englische Seite ist kanonisch und wird zuerst aktualisiert; Live-Daten und die neuesten Abschnitte erscheinen [dort](./README.md).*

<br/>

[![English](https://img.shields.io/badge/%F0%9F%87%AC%F0%9F%87%A7-English-012169?style=for-the-badge&labelColor=ffffff)](./README.md)
[![日本語](https://img.shields.io/badge/%F0%9F%87%AF%F0%9F%87%B5-%E6%97%A5%E6%9C%AC%E8%AA%9E-BC002D?style=for-the-badge&labelColor=ffffff)](./README.ja.md)
[![中文](https://img.shields.io/badge/%F0%9F%87%A8%F0%9F%87%B3-%E4%B8%AD%E6%96%87-DE2910?style=for-the-badge&labelColor=ffffff)](./README.zh.md)
[![Italiano](https://img.shields.io/badge/%F0%9F%87%AE%F0%9F%87%B9-Italiano-009246?style=for-the-badge&labelColor=ffffff)](./README.it.md)
[![Français](https://img.shields.io/badge/%F0%9F%87%AB%F0%9F%87%B7-Fran%C3%A7ais-0055A4?style=for-the-badge&labelColor=ffffff)](./README.fr.md)
[![Deutsch](https://img.shields.io/badge/%F0%9F%87%A9%F0%9F%87%AA-Deutsch-1A1A1A?style=for-the-badge&labelColor=FFCE00)](./README.de.md)
[![Español](https://img.shields.io/badge/%F0%9F%87%AA%F0%9F%87%B8-Espa%C3%B1ol-C60B1E?style=for-the-badge&labelColor=FFC400)](./README.es.md)
[![العربية](https://img.shields.io/badge/%F0%9F%87%B8%F0%9F%87%A6-%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9-006C35?style=for-the-badge&labelColor=ffffff)](./README.ar.md)

<br/>

[![SDK](https://img.shields.io/badge/SDK-v0.3.5-0a4a8f?style=flat-square)](https://github.com/AxonOS-org/axonos-sdk)
[![Kernel](https://img.shields.io/badge/Kernel-v0.3.0-0a4a8f?style=flat-square)](https://github.com/AxonOS-org/AxonOS-kernel)
[![ABI](https://img.shields.io/badge/Kernel%20ABI-v1-0a4a8f?style=flat-square)](https://axonos.org/specifications.html)
[![Rust](https://img.shields.io/badge/built%20with-Rust-CE422B?style=flat-square&logo=rust&logoColor=white)](https://www.rust-lang.org/)
[![License](https://img.shields.io/badge/license-Apache--2.0%20OR%20MIT-475569?style=flat-square)](#lizenzierung)

### [axonos.org](https://axonos.org) · [Spezifikationen](https://axonos.org/specifications.html) · [SDK](https://axonos.org/sdk.html) · [Artikel](https://medium.com/@AxonOS) · [connect@axonos.org](mailto:connect@axonos.org)

</div>

---

## Projekt AxonOS

<br/>

**AxonOS ist ein harter Echtzeit-Neural-Betriebssystem für Gehirn-Computer-Schnittstellen.** Open-Source-Kernel in `#![no_std]` Rust. Sub-Millisekunden-Jitter auf handelsüblichen ARM Cortex-M. Worst-Case-Response-Time formal beschränkt. Strukturelle Privatsphäre, die die Anwendungsschicht nicht umgehen kann.

Gebaut für Patienten, die auf closed-loop-Assistenzschnittstellen angewiesen sind, und für Ingenieure, die sich weigern, sie auf Best-Effort-Scheduling auszuliefern.

<br/>

## Warum AxonOS existiert

Heute muss jede BCI-Anwendung pro Gerät ein eigenes binäres Wire-Format neu parsen, Capability-Gating neu implementieren und Integrations-Boilerplate für jede neue Hardware-Plattform neu schreiben.

**AxonOS erledigt alle drei Aufgaben einmalig in sicherem `no_std` Rust auf einem formal beschränkten Mikrokernel.** Eine verifizierbare Basis. Eine typisierte API-Oberfläche. Viele Hardware-Backends.

<br/>

## Die vier Zusagen

<br/>

|  | Zusage | Was das in der Praxis bedeutet |
|:---:|:---|:---|
| | **Harter Echtzeitbetrieb auf Standardhardware** | `#![no_std]` Rust auf ARMv8-M. Kein GC, kein Allokator im Hot Path, keine unbeschränkten Panics. |
| | **Formal beschränkte WCRT** | Jede Critical-Path-Operation hat eine Kani-verifizierte Obergrenze. Latenz wird nicht gemessen, sondern *bewiesen*. |
| | **Strukturelle Privatsphäre** | Capabilities, die rohe kognitive Daten leaken würden (`RawEEG`, `EmotionState`, `CognitiveProfile`), existieren nicht als Typen. |
| | **Offenes Ökosystem** | Apache-2.0 OR MIT für Code, CC-BY-SA-4.0 für Spezifikationen. Alle Repositorien sind öffentlich. Jede Schicht ist auditierbar, forkbar, austauschbar. |

<br/>

## Schnellstart

Sechzig Sekunden vom Klon bis zur ersten Intent-Beobachtung.

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

Das SDK ist das Rust-Referenz-Binding. C-FFI-, Python-, WebAssembly-, JNI- und Swift-Bindings stehen auf der [veröffentlichten Roadmap](https://axonos.org/sdk.html).

<br/>

## Die Repositorien

Alle sechs Repositorien sind öffentlich. Quellcode unter Apache-2.0 OR MIT. Spezifikationen unter CC-BY-SA-4.0.

|  | Repository | Zweck | Sprache | Aktuell |
|:---:|:---|:---|:---:|:---|
| [⬢](https://github.com/AxonOS-org/AxonOS-kernel) | **AxonOS-kernel** | Hartes Echtzeit-Mikrokernel — 8 Crates, formal beschränkte WCRT, 28 Kani-Harnesses | Rust | `v0.3.0` |
| [⬢](https://github.com/AxonOS-org/axonos-sdk) | **axonos-sdk** | Anwendungsgrenze — typisierte Intents, Capability-Manifests, Kernel-ABI v1 | Rust | `v0.3.5` |
| [⬢](https://github.com/AxonOS-org/axonos-consent) | **axonos-consent** | Consent-Enforcement auf Protokollebene für Cognitive Mesh Coupling (MMP) | Rust | `v0.5.0` |
| [⬢](https://github.com/AxonOS-org/axonos-swarm) | **axonos-swarm** | Multi-Node-Koordination — Neural-PTP-Synchronisation, Swarm-Scheduling | Rust | `v0.2.1` |
| [⬢](https://github.com/AxonOS-org/axonos-rfcs) | **axonos-rfcs** | Engineering-Spezifikationen — 8 nummerierte RFCs, normativ, CC-BY-SA-4.0 | Markdown | aktiv |
| [⬢](https://github.com/AxonOS-org/axon-bci-gateway) | **axon-bci-gateway** | Hardware-Akquise-Gateway (OpenBCI-Fork, MIT vom Upstream erhalten) | HTML | aktiv |

<br/>

## Architektur

<br/>

```mermaid
flowchart LR
    A[EEG/EMG-Sensoren<br/>ADS1299 · 24-bit] -->|raw| B[BCI-Gateway<br/>nRF52840]
    B -->|filtered| C[AxonOS-Kernel<br/>Rust no_std<br/>Cortex-M4F]
    C -->|WCRT<br/>≤ 1 ms (L1)| D[Kognitiver<br/>Scheduler]
    D -->|typed intent| E[Anwendung<br/>via SDK]
    F[Cognitive Hypervisor<br/>TrustZone-S] -.->|isolates| C
    G[Consent-Schicht<br/>MMP protocol] -.->|gates| D

    classDef kernel fill:#0e2a47,stroke:#3b82f6,color:#fff,stroke-width:2px
    classDef secure fill:#0a3d2e,stroke:#10b981,color:#fff,stroke-width:2px
    class C kernel
    class F,G secure
```

<br/>

## In Zahlen

<br/>

<table align="center">
<tr>
  <td align="center" width="200">
    <h2>≤ 1 ms</h2>
    <sub>Kernel-WCRT, bewiesen (L1)<br/>STM32F407 @ 168 MHz</sub>
  </td>
  <td align="center" width="200">
    <h2>2.1 µs</h2>
    <sub>Worst-Case-Jitter σ<br/>vs Linux 1323 µs</sub>
  </td>
  <td align="center" width="200">
    <h2>630×</h2>
    <sub>Verbesserungsfaktor<br/>vs Linux mainline</sub>
  </td>
</tr>
<tr>
  <td align="center">
    <h2>30</h2>
    <sub>Kani-BMC-Harnesses<br/>Obergrenzen bewiesen</sub>
  </td>
  <td align="center">
    <h2>66+</h2>
    <sub>Unit- und Integrationstests<br/>im gesamten Workspace</sub>
  </td>
  <td align="center">
    <h2>42+</h2>
    <sub>Architektur-Artikel<br/>auf Medium veröffentlicht</sub>
  </td>
</tr>
</table>

<br/>

## Status

<br/>

| Phase | Inhalt | Zeitpunkt |
|:---|:---|:---|
| **Phase 0** | Architektur, RFCs, SDK-API, Kernel-Verifikations-Harnesses | Abgeschlossen |
| **Phase 1** | Klinik-Dev-Kit (8 Kanäle) · ALS-Zentrum-Pilot | abhängig von einer instrumentierten Messvorrichtung, die noch nicht beschafft ist; kein Datum, weil es erfunden wäre |
| **Phase 2** | FDA 510(k) Q-Sub für Cognitive Hypervisor · IEEE P2731 Beitrag | nach Phase 1 |
| **Phase 3** | Erste kommerzielle Bereitstellung über Foundation-Mitglieder | nach Phase 2 |

<br/>

## Lizenzierung

| Artefakt | Lizenz |
|:---|:---|
| Kernel, SDK, consent, swarm, gateway | Apache-2.0 OR MIT |
| RFCs und Spezifikationen | CC-BY-SA-4.0 |
| `axon-bci-gateway` | MIT (vom Upstream OpenBCI_GUI erhalten) |

<br/>
<br/>

---

<div align="center">

<img src="./logo.png" width="72" alt="AxonOS-Logo" />

<br/>
<br/>

**Gebaut und gewartet von Denis Yermakou**

[denis@axonos.org](mailto:denis@axonos.org) · [LinkedIn](https://www.linkedin.com/in/denis-yermakou) · [Medium](https://medium.com/@AxonOS) · [Site](https://axonos.org)

<sub>Singapore · Zurich · Berlin · Milano · San Mateo</sub>

<br/>

<sub>Gebaut mit Rust. Verifiziert mit Kani. Auf harten Echtzeitbetrieb ausgerichtet.</sub>

</div>
