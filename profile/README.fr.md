<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/AxonOS-org/.github/raw/main/profile/assets/hero-dark.svg">
  <img alt="AxonOS — infrastructure déterministe pour les interfaces cerveau-machine" src="https://github.com/AxonOS-org/.github/raw/main/profile/assets/hero-light.svg" width="100%">
</picture>

### Infrastructure déterministe pour les interfaces cerveau-machine.

<sub>Cette page résume la [page anglaise](./README.md). La page anglaise fait foi ; les versions, les dépôts et les preuves s'y trouvent.</sub>

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

## Ce qu'est AxonOS

AxonOS est la couche temps réel strict entre le matériel neuronal et les applications qui l'utilisent : un noyau open source en Rust `#![no_std]` pour ARM Cortex-M. Il est conçu pour que les temps de réponse au pire cas soient analysés avant l'exécution, et non mesurés après coup, et pour que la confidentialité soit imposée **sous la couche applicative**, là où aucune application ne peut la contourner.

> Les applications reçoivent des événements d'intention typés et liés au consentement — jamais de flux neuronaux bruts.

## Ce qui est prouvé aujourd'hui

Trois propriétés sont prouvées avec le vérificateur de modèles borné Kani, chacune sur un domaine déclaré (niveau **L1**) :

- l'admission et la sélection Earliest-Deadline-First de l'ordonnanceur ;
- l'anneau à producteur unique et consommateur unique : aller-retour exact, insertion sans boucle, ordre FIFO ;
- le consentement : aucun changement d'état sans signature vérifiée, aucune séquence admise deux fois, un retrait est définitif.

**Aucun chiffre de temps n'est revendiqué aujourd'hui.** Les 1 000 µs du Standard sont une exigence, pas un résultat : il n'existe encore ni preuve d'un temps de réponse ni mesure publiée sur le matériel de référence. L'état qui fait foi est dans le [catalogue des affirmations](https://github.com/AxonOS-org/axonos-standard/blob/main/CLAIMS.md).

## Dépôts

Tous les dépôts sont publics : code sous Apache-2.0 OR MIT, spécifications sous CC-BY-SA-4.0. La liste complète avec les versions actuelles figure sur la [page anglaise](./README.md) et sur [github.com/AxonOS-org](https://github.com/AxonOS-org).

---

<div align="center">

© The AxonOS Project / Denis Yermakou

[connect@axonos.org](mailto:connect@axonos.org) · [security@axonos.org](mailto:security@axonos.org) · [LinkedIn](https://www.linkedin.com/in/axonos) · [axonos.org](https://axonos.org)

<sub>Des bureaux et un siège sont envisagés pour l'avenir.</sub>

</div>
