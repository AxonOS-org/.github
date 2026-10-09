<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/AxonOS-org/.github/raw/main/profile/assets/hero-dark.svg">
  <img alt="AxonOS — infraestructura determinista para interfaces cerebro-computadora" src="https://github.com/AxonOS-org/.github/raw/main/profile/assets/hero-light.svg" width="100%">
</picture>

### Infraestructura determinista para interfaces cerebro-computadora.

<sub>Esta página resume la [página en inglés](./README.md). La página en inglés es la canónica; allí están las versiones, los repositorios y las evidencias.</sub>

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

[![AxonOS Radar](https://img.shields.io/badge/AxonOS%20Radar-open%20neurotech%20map-1f8fae?style=flat-square&labelColor=0b1220)](https://axonos-bci.github.io/axonos-community-radar/)

</div>

## Qué es AxonOS

AxonOS es la capa de tiempo real estricto entre el hardware neuronal y las aplicaciones que lo usan: un núcleo de código abierto en Rust `#![no_std]` para ARM Cortex-M. Está diseñado para que los tiempos de respuesta en el peor caso se analicen antes de ejecutarse, no se midan después, y para que la privacidad se imponga **por debajo de la capa de aplicación**, donde ninguna aplicación puede eludirla.

> Las aplicaciones reciben eventos de intención tipados y sujetos a consentimiento — nunca flujos neuronales en bruto.

## Qué está demostrado hoy

Tres propiedades están demostradas con el verificador de modelos acotado Kani, cada una sobre un dominio declarado (nivel **L1**):

- la admisión y la selección Earliest-Deadline-First del planificador;
- el anillo de un productor y un consumidor: ida y vuelta exacta, inserción sin bucles, orden FIFO;
- el consentimiento: ningún cambio de estado sin firma verificada, ninguna secuencia admitida dos veces, una retirada es definitiva.

**Hoy no se reivindica ninguna cifra de tiempo.** Los 1 000 µs del Estándar son un requisito, no un resultado: aún no existe una demostración de un tiempo de respuesta ni una medición publicada en el hardware de referencia. El estado autorizado está en el [catálogo de afirmaciones](https://github.com/AxonOS-org/axonos-standard/blob/main/CLAIMS.md).

## Repositorios

Todos los repositorios son públicos: código bajo Apache-2.0 OR MIT, especificaciones bajo CC-BY-SA-4.0. La lista completa con las versiones actuales está en la [página en inglés](./README.md) y en [github.com/AxonOS-org](https://github.com/AxonOS-org).

---

<div align="center">

© The AxonOS Project / Denis Yermakou

[connect@axonos.org](mailto:connect@axonos.org) · [security@axonos.org](mailto:security@axonos.org) · [LinkedIn](https://www.linkedin.com/in/axonos) · [axonos.org](https://axonos.org)

<sub>Se contemplan oficinas y una sede para el futuro.</sub>

</div>
