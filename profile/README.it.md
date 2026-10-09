<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/AxonOS-org/.github/raw/main/profile/assets/hero-dark.svg">
  <img alt="AxonOS — infrastruttura deterministica per interfacce cervello-computer" src="https://github.com/AxonOS-org/.github/raw/main/profile/assets/hero-light.svg" width="100%">
</picture>

### Infrastruttura deterministica per interfacce cervello-computer.

<sub>Questa pagina riassume la [pagina inglese](./README.md). La pagina inglese è quella canonica; versioni, repository ed evidenze si trovano lì.</sub>

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

## Che cos'è AxonOS

AxonOS è lo strato hard real-time tra l'hardware neurale e le applicazioni che lo usano: un kernel open source in Rust `#![no_std]` per ARM Cortex-M. È progettato perché i tempi di risposta nel caso peggiore siano analizzati prima dell'esecuzione, non misurati dopo, e perché la privacy sia imposta **sotto il livello applicativo**, dove nessuna applicazione può aggirarla.

> Le applicazioni ricevono eventi di intenzione tipizzati e vincolati al consenso — mai flussi neurali grezzi.

## Che cosa è dimostrato oggi

Tre proprietà sono dimostrate con il model checker limitato Kani, ciascuna su un dominio dichiarato (livello **L1**):

- l'ammissione e la selezione Earliest-Deadline-First dello scheduler;
- l'anello a produttore singolo e consumatore singolo: andata e ritorno esatti, inserimento senza cicli, ordine FIFO;
- il consenso: nessun cambio di stato senza firma verificata, nessuna sequenza ammessa due volte, una revoca è definitiva.

**Oggi non si rivendica alcun valore temporale.** I 1 000 µs dello Standard sono un requisito, non un risultato: non esistono ancora né una dimostrazione di un tempo di risposta né una misura pubblicata sull'hardware di riferimento. Lo stato autorevole è nel [catalogo delle affermazioni](https://github.com/AxonOS-org/axonos-standard/blob/main/CLAIMS.md).

## Repository

Tutti i repository sono pubblici: codice sotto Apache-2.0 OR MIT, specifiche sotto CC-BY-SA-4.0. L'elenco completo con le versioni attuali è sulla [pagina inglese](./README.md) e su [github.com/AxonOS-org](https://github.com/AxonOS-org).

---

<div align="center">

© The AxonOS Project / Denis Yermakou

[connect@axonos.org](mailto:connect@axonos.org) · [security@axonos.org](mailto:security@axonos.org) · [LinkedIn](https://www.linkedin.com/in/axonos) · [axonos.org](https://axonos.org)

<sub>Uffici e una sede sono in valutazione per il futuro.</sub>

</div>
