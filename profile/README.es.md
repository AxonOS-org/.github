<div align="center">

<img src="./banner.jpg" alt="AxonOS — sistema operativo cognitivo abierto para interfaces cerebro-computadora" width="100%" />

<br/>
<br/>

# **axonos**

### El sistema operativo cognitivo abierto para las interfaces cerebro-computadora.

<br/>

[![🇬🇧 English](https://img.shields.io/badge/%F0%9F%87%AC%F0%9F%87%A7-English-012169?style=for-the-badge&labelColor=ffffff)](./README.md)
[![🇯🇵 日本語](https://img.shields.io/badge/%F0%9F%87%AF%F0%9F%87%B5-%E6%97%A5%E6%9C%AC%E8%AA%9E-BC002D?style=for-the-badge&labelColor=ffffff)](./README.ja.md)
[![🇨🇳 中文](https://img.shields.io/badge/%F0%9F%87%A8%F0%9F%87%B3-%E4%B8%AD%E6%96%87-DE2910?style=for-the-badge&labelColor=ffffff)](./README.zh.md)
[![🇮🇹 Italiano](https://img.shields.io/badge/%F0%9F%87%AE%F0%9F%87%B9-Italiano-009246?style=for-the-badge&labelColor=ffffff)](./README.it.md)
[![🇫🇷 Français](https://img.shields.io/badge/%F0%9F%87%AB%F0%9F%87%B7-Fran%C3%A7ais-0055A4?style=for-the-badge&labelColor=ffffff)](./README.fr.md)
[![🇩🇪 Deutsch](https://img.shields.io/badge/%F0%9F%87%A9%F0%9F%87%AA-Deutsch-1A1A1A?style=for-the-badge&labelColor=FFCE00)](./README.de.md)
[![🇪🇸 Español](https://img.shields.io/badge/%F0%9F%87%AA%F0%9F%87%B8-Espa%C3%B1ol-C60B1E?style=for-the-badge&labelColor=FFC400)](./README.es.md)
[![🇸🇦 العربية](https://img.shields.io/badge/%F0%9F%87%B8%F0%9F%87%A6-%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9-006C35?style=for-the-badge&labelColor=ffffff)](./README.ar.md)

<br/>

[![SDK](https://img.shields.io/badge/SDK-v0.3.4-orange?style=flat-square)](https://github.com/AxonOS-org/axonos-sdk)
[![Kernel](https://img.shields.io/badge/Kernel-v0.2.1-orange?style=flat-square)](https://github.com/AxonOS-org/axonos-kernel)
[![ABI](https://img.shields.io/badge/Kernel%20ABI-v1-blueviolet?style=flat-square)](https://axonos.org/specifications.html)
[![Rust](https://img.shields.io/badge/built%20with-Rust-CE422B?style=flat-square&logo=rust&logoColor=white)](https://www.rust-lang.org/)
[![License](https://img.shields.io/badge/license-Apache--2.0%20OR%20MIT-blue?style=flat-square)](#licensing)

### [🌐 axonos.org](https://axonos.org) · [📐 Especificaciones](https://axonos.org/specifications.html) · [🧰 SDK](https://axonos.org/sdk.html) · [📖 Artículos](https://medium.com/@AxonOS) · [💬 connect@axonos.org](mailto:connect@axonos.org)

</div>

---

## Proyecto AxonOS

<br/>

**AxonOS es un sistema operativo neuronal de tiempo real estricto para interfaces cerebro-computadora.** Kernel de código abierto en `#![no_std]` Rust. Jitter sub-milisegundo en ARM Cortex-M comercial. Tiempo de respuesta en el peor caso formalmente acotado. Privacidad estructural que la capa de aplicación no puede eludir.

Construido para los pacientes que dependen de interfaces asistivas de bucle cerrado, y para los ingenieros que se niegan a entregarlos sobre planificación best-effort.

<br/>

## Por qué existe AxonOS

Hoy, cada aplicación BCI debe reparsear un formato binario propio por dispositivo, reimplementar el control de capacidades, y reescribir el código de integración para cada nueva plataforma de hardware.

**AxonOS hace las tres cosas una sola vez, en `no_std` Rust seguro, sobre un microkernel formalmente acotado.** Una base verificable. Una superficie API tipada. Múltiples backends de hardware.

<br/>

## Los cuatro compromisos

<br/>

|     | Compromiso                    | Lo que significa en la práctica                                                                                                    |
|:---:|:------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------|
| 🦀  | **Tiempo real estricto en hardware comercial** | Rust `#![no_std]` en ARMv8-M. Sin GC, sin asignador en el camino caliente, sin panics no acotados.                |
| 📐  | **WCRT formalmente acotado**  | Cada operación crítica tiene un límite superior verificado por Kani. La latencia se *demuestra*, no se mide.                     |
| 🔒  | **Privacidad estructural**    | Las capacidades que filtrarían estado cognitivo crudo (`RawEEG`, `EmotionState`, `CognitiveProfile`) no existen como tipos.       |
| 🌐  | **Ecosistema abierto**        | Apache-2.0 OR MIT para código, CC-BY-SA-4.0 para especificaciones. Todos los repositorios son públicos. Cualquiera puede auditar, bifurcar o reemplazar cualquier capa. |

<br/>

## Inicio rápido

Sesenta segundos desde el clone hasta tu primera observación de intención.

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

El SDK es el binding Rust de referencia. Los bindings C FFI, Python, WebAssembly, JNI y Swift figuran en la [hoja de ruta publicada](https://axonos.org/sdk.html).

<br/>

## Los repositorios

Los seis repositorios son públicos. Código fuente bajo Apache-2.0 OR MIT. Especificaciones bajo CC-BY-SA-4.0.

|                                                                              | Repositorio          | Propósito                                                                          | Lenguaje | Última     |
|:----------------------------------------------------------------------------:|:---------------------|:-----------------------------------------------------------------------------------|:--------:|:-----------|
| [⬢](https://github.com/AxonOS-org/axonos-kernel)                              | **axonos-kernel**    | Microkernel de tiempo real estricto — 8 crates, WCRT formalmente acotado, 28 harnesses Kani | Rust   | `v0.2.1`   |
| [⬢](https://github.com/AxonOS-org/axonos-sdk)                                 | **axonos-sdk**       | Frontera de aplicación — intents tipados, manifiestos de capacidades, ABI del kernel v1 | Rust   | `v0.3.4`   |
| [⬢](https://github.com/AxonOS-org/axonos-consent)                             | **axonos-consent**   | Consentimiento a nivel de protocolo para acoplamiento cognitive mesh (MMP)         | Rust     | `v0.4.0`   |
| [⬢](https://github.com/AxonOS-org/axonos-swarm)                               | **axonos-swarm**     | Coordinación multinodo — sincronización Neural PTP, scheduling de swarm            | Rust     | `v0.2.0`   |
| [⬢](https://github.com/AxonOS-org/axonos-rfcs)                                | **axonos-rfcs**      | Especificaciones de ingeniería — 8 RFC numerados, normativos, CC-BY-SA-4.0          | Markdown | activo     |
| [⬢](https://github.com/AxonOS-org/axon-bci-gateway)                           | **axon-bci-gateway** | Gateway de adquisición de hardware (fork de OpenBCI, MIT preservado del upstream)  | HTML     | activo     |

<br/>

## Arquitectura

<br/>

```mermaid
flowchart LR
    A[Sensores EEG/EMG<br/>ADS1299 · 24-bit] -->|raw| B[Gateway BCI<br/>nRF52840]
    B -->|filtered| C[Kernel AxonOS<br/>Rust no_std<br/>Cortex-M4F]
    C -->|WCRT<br/>972µs| D[Planificador<br/>cognitivo]
    D -->|typed intent| E[Aplicación<br/>via SDK]
    F[Cognitive Hypervisor<br/>TrustZone-S] -.->|isolates| C
    G[Capa de consentimiento<br/>MMP protocol] -.->|gates| D

    classDef kernel fill:#0e2a47,stroke:#3b82f6,color:#fff,stroke-width:2px
    classDef secure fill:#0a3d2e,stroke:#10b981,color:#fff,stroke-width:2px
    class C kernel
    class F,G secure
```

<br/>

## En números

<br/>

<table align="center">
<tr>
  <td align="center" width="200">
    <h2>972 µs</h2>
    <sub>WCRT del kernel, medido<br/>STM32F407 @ 168 MHz</sub>
  </td>
  <td align="center" width="200">
    <h2>2.1 µs</h2>
    <sub>Jitter σ en el peor caso<br/>vs Linux 1323 µs</sub>
  </td>
  <td align="center" width="200">
    <h2>630×</h2>
    <sub>Factor de mejora<br/>vs Linux mainline</sub>
  </td>
</tr>
<tr>
  <td align="center">
    <h2>28</h2>
    <sub>Harnesses Kani BMC<br/>límites superiores probados</sub>
  </td>
  <td align="center">
    <h2>66+</h2>
    <sub>Pruebas unitarias y de integración<br/>en todo el workspace</sub>
  </td>
  <td align="center">
    <h2>42+</h2>
    <sub>Artículos de arquitectura<br/>publicados en Medium</sub>
  </td>
</tr>
</table>

<br/>

## Estado

<br/>

| Fase         | Contenido                                                                                  | Cuándo       |
|:-------------|:-------------------------------------------------------------------------------------------|:-------------|
| **Fase 0**   | Arquitectura, RFCs, API del SDK, harnesses de verificación del kernel                       | ✓ Completado |
| **Fase 1**   | Kit de desarrollo clínico (8 canales) · piloto en centro ALS                               | 🟡 Q2 2026   |
| **Fase 2**   | FDA 510(k) Q-Sub para Cognitive Hypervisor · contribución IEEE P2731                       | 🔵 Q3 2026   |
| **Fase 3**   | Primera implementación comercial vía miembros de la Foundation                              | 🔵 2027      |

<br/>

## Licencias

| Artefacto                             | Licencia                                           |
|:--------------------------------------|:---------------------------------------------------|
| Kernel, SDK, consent, swarm, gateway  | Apache-2.0 OR MIT                                  |
| RFCs y especificaciones               | CC-BY-SA-4.0                                       |
| `axon-bci-gateway`                    | MIT (preservado del upstream OpenBCI_GUI)          |

<br/>
<br/>

---

<div align="center">

<img src="./logo.png" width="72" alt="Logo AxonOS" />

<br/>
<br/>

**Construido y mantenido por Denis Yermakou**

[connect@axonos.org](mailto:connect@axonos.org) · [LinkedIn](https://www.linkedin.com/in/denis-yermakou) · [Medium](https://medium.com/@AxonOS) · [Site](https://axonos.org)

<sub>Singapore · Zurich · Berlin · Milano · San Mateo</sub>

<br/>

<sub>Construido con Rust. Verificado con Kani. Orientado al tiempo real estricto.</sub>

</div>
