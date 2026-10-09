<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/AxonOS-org/.github/raw/main/profile/assets/hero-dark.svg">
  <img alt="AxonOS — deterministische Infrastruktur für Gehirn-Computer-Schnittstellen" src="https://github.com/AxonOS-org/.github/raw/main/profile/assets/hero-light.svg" width="100%">
</picture>

### Deterministische Infrastruktur für Gehirn-Computer-Schnittstellen.

<sub>Diese Seite fasst die [englische Seite](./README.md) zusammen. Die englische Seite ist kanonisch; Versionen, Repositorien und Belege stehen dort.</sub>

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

## Was AxonOS ist

AxonOS ist die harte Echtzeitschicht zwischen neuronaler Hardware und den Anwendungen, die sie nutzen: ein quelloffener Kernel in `#![no_std]`-Rust für ARM Cortex-M. Er ist so entworfen, dass Worst-Case-Antwortzeiten vor der Ausführung analysiert und nicht nachträglich gemessen werden, und dass Datenschutz **unterhalb der Anwendungsschicht** durchgesetzt wird, wo keine Anwendung ihn umgehen kann.

> Anwendungen erhalten typisierte, an Einwilligung gebundene Intent-Ereignisse — niemals rohe neuronale Datenströme.

## Was heute bewiesen ist

Drei Eigenschaften sind mit dem Bounded Model Checker Kani bewiesen, jeweils über einem angegebenen Bereich (Stufe **L1**):

- Zulassung und Earliest-Deadline-First-Auswahl des Schedulers;
- der Single-Producer-Single-Consumer-Ring: exakter Durchlauf, schleifenfreies Einfügen, FIFO-Reihenfolge;
- die Einwilligung: keine Zustandsänderung ohne verifizierte Signatur, keine Sequenz zweimal, ein Widerruf ist endgültig.

**Es wird derzeit keine Zeitangabe beansprucht.** Die 1 000 µs des Standards sind eine Anforderung, kein Ergebnis: Es gibt noch keinen Beweis einer Antwortzeit und keine veröffentlichte Messung auf Referenzhardware. Der maßgebliche Stand steht im [Claims-Katalog](https://github.com/AxonOS-org/axonos-standard/blob/main/CLAIMS.md).

## Repositorien

Alle Repositorien sind öffentlich: Quellcode unter Apache-2.0 OR MIT, Spezifikationen unter CC-BY-SA-4.0. Die vollständige Liste mit aktuellen Versionen steht auf der [englischen Seite](./README.md) und unter [github.com/AxonOS-org](https://github.com/AxonOS-org).

---

<div align="center">

© The AxonOS Project / Denis Yermakou

[connect@axonos.org](mailto:connect@axonos.org) · [security@axonos.org](mailto:security@axonos.org) · [LinkedIn](https://www.linkedin.com/in/axonos) · [axonos.org](https://axonos.org)

<sub>Büros und ein Hauptsitz sind für die Zukunft in Planung.</sub>

</div>
