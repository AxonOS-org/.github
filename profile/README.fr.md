# AxonOS

> Un noyau temps réel bare-metal pour interfaces cerveau-ordinateur.
> Écrit en Rust. Open source. Construit sur la preuve.

[🇬🇧 English](./README.md) ·
[🇯🇵 日本語](./README.ja.md) ·
[🇮🇹 Italiano](./README.it.md) ·
[🇨🇳 中文](./README.zh.md) ·
[🇩🇪 Deutsch](./README.de.md) ·
[🇪🇸 Español](./README.es.md) ·
[🇫🇷 Français](./README.fr.md)

---

## De quoi s'agit-il

AxonOS est un microkernel Rust `#![no_std]` `#![forbid(unsafe_code)]`
pour pipelines de signaux d'interfaces cerveau-ordinateur (BCI) sur
microcontrôleurs de classe Cortex-M.

Il est conçu pour une classe spécifique de système : un dispositif
petit et autonome qui acquiert des signaux neuronaux, classifie
l'intention de l'utilisateur et pilote un stimulateur ou une interface
d'assistance en boucle fermée, sur un budget temps réel fixe, sans
système d'exploitation généraliste entre le silicium et le patient.

Dans ce type de système, une échéance manquée n'est pas une régression
de performance — c'est un événement indésirable.

## Pourquoi cela existe

Les logiciels BCI temps réel actuels reposent sur trois catégories de
fondations, chacune structurellement inadaptée au problème :

1. **Noyaux généralistes** (Linux, Windows) — conçus pour l'équité et
   le débit, non pour une latence pire-cas bornée. La gigue de
   l'ordonnanceur de Linux mainline est de l'ordre de la milliseconde ;
   PREEMPT_RT la réduit mais ne l'élimine pas.

2. **RTOS conventionnels** (FreeRTOS, Zephyr) — fournissent un
   ordonnancement temps réel à priorités, mais aucune preuve formelle
   d'ordonnançabilité, aucune garantie de sécurité mémoire au niveau
   du langage, et aucune abstraction du domaine BCI.

3. **Systèmes d'exploitation de classe application sur processeurs
   d'application** — apportent la surface d'attaque complète et
   l'imprévisibilité d'un OS généraliste à un dispositif médical
   réglementé.

AxonOS comble ce vide : un noyau petit, analytiquement ordonnançable,
écrit dans un langage qui élimine les défauts de sécurité mémoire à la
compilation, avec un modèle de capabilities qui empêche les données
neuronales brutes d'atteindre le code applicatif.

## Ce qui le distingue

| Propriété | AxonOS | RTOS courants | Linux PREEMPT_RT |
|:---|:---|:---|:---|
| Politique d'ordonnancement | EDF (Liu–Layland) | Priorité fixe | CFS + RT |
| Preuve analytique d'ordonnançabilité | Oui | Non | Non |
| Sécurité mémoire à la compilation | Oui (Rust) | Non (C) | Non (C) |
| Logique noyau sans `unsafe` | Oui | Non | Non |
| Allocation tas sur le chemin chaud | Aucune | Optionnelle | Par défaut |
| Isolation par capability BCI | Oui | Aucune | Aucune |
| WCET déclaré avec niveau de preuve | Oui (L1/L2) | Non | Non |

**Avertissement d'honnêteté important.** AxonOS *ne revendique pas* de
vérification formelle au sens de seL4. Il utilise la théorie analytique
de l'ordonnancement temps réel (Liu–Layland) combinée au système de
types de Rust et à une taxonomie de validation étayée par la mesure.
Cela est plus faible que des preuves de correction fonctionnelle
machine-vérifiées, mais c'est atteignable aujourd'hui et s'aligne avec
les exigences du cycle de vie logiciel IEC 62304 Classe C.

## Modèle de preuve

Chaque affirmation de performance dans la documentation AxonOS est
étiquetée avec un niveau de preuve :

- **L1** — Dérivée du comptage d'instructions. Calculée à partir de
  l'assembleur compilé contre la référence de timing par cycle de
  l'ISA cible. Conservatrice ; aucune exécution matérielle requise.
- **L2** — Mesurée à l'exécution. Observée par un instrument intégré
  (compteur de cycles DWT) sur matériel de référence pendant un
  intervalle et une distribution d'entrée déclarés.
- **L3** — Validée par oscilloscope indépendant. Observée par un
  instrument indépendant du dispositif sous test (analyseur logique,
  points de bascule GPIO). Requise pour soumission réglementaire.
- **pending** — Mesure non encore effectuée ; date cible déclarée.

Chiffres principaux actuels :

| Métrique | Valeur | Niveau |
|:---|:---|:---|
| WCET pipeline, époque unique | 640,2 µs | L1 |
| WCRT bout-en-bout | 972 µs | L2 |
| Gigue EDF σ (10,8M époques, 12 h) | 2,1 µs | L2 |
| Gigue EDF P99,9 | 6,5 µs | L2 |
| Échéances manquées observées | 0 sur 10,8 × 10⁶ | L2 |
| Utilisation CPU U′ (WCET gonflé) | 0,179 | L1 |
| WCRT validé par GPIO (fixture H573) | — | **pending** Q2 2026 |

Matériel : STM32F407 Cortex-M4F @ 168 MHz, CAN ADS1299 8 canaux 24 bits,
élément sécurisé ATECC608B, nRF52840 BLE 5.3, isolation galvanique
ISO7741 5 kV.

## Ce que contient cette organisation

| Dépôt | Objet | État |
|:---|:---|:---|
| [`axonos-rfcs`](https://github.com/AxonOS-org/axonos-rfcs) | RFC d'ingénierie régissant les décisions d'architecture | 6 RFC · CC-BY-SA-4.0 |
| [`axonos-sdk`](https://github.com/AxonOS-org/axonos-sdk) | SDK applicatif : intents typés, capabilities, attestation | v0.4.0 · Apache-2.0 OR MIT |
| [`axonos-consent`](https://github.com/AxonOS-org/axonos-consent) | Implémentation de référence de l'AxonOS Consent Protocol | v0.4.0 · Apache-2.0 OR MIT |
| [`axonos-swarm`](https://github.com/AxonOS-org/axonos-swarm) | Coordination multi-nœuds : Neural PTP, swarm scheduler, détecteur de fautes | v0.1.0 · Apache-2.0 OR MIT |
| [`axon-bci-gateway`](https://github.com/AxonOS-org/axon-bci-gateway) | Passerelle applicative de référence (fork, avec attribution) | Actif · Apache-2.0 |

Les fixtures de benchmark reproductibles et le source LaTeX du
prépublication seront publiés avec les résultats de validation L3
au Q2 2026.

## Publics

Ce projet est conçu pour quatre publics. Si vous correspondez à l'un
d'eux, commencez à l'endroit indiqué.

### Chercheurs en BCI et traitement de signaux neuronaux

Vous voulez un substrat temps réel qui n'impose pas ses propres
opinions à votre pipeline de signaux, avec un timing prévisible
caractérisable et une séparation nette entre acquisition brute et
sortie d'intent de haut niveau.

Commencez par : [`axonos-rfcs`](https://github.com/AxonOS-org/axonos-rfcs) →
RFC-0001 (architecture) et RFC-0004 (contrat dual-core).

### Ingénieurs systèmes embarqués

Vous voulez un exemple fonctionnel de Rust `#![no_std]`
`#![forbid(unsafe_code)]` appliqué à l'ordonnancement hard real-time
sur Cortex-M, avec des chiffres WCET déclarés qui distinguent dérivé
de mesuré.

Commencez par : [`axonos-sdk`](https://github.com/AxonOS-org/axonos-sdk) →
exemples dans `examples/bare_metal_no_std.rs`.

### Ingénieurs de dispositifs médicaux et équipes réglementaires

Vous voulez un substrat noyau dont les décisions d'architecture sont
documentées comme RFC versionnés, dont les affirmations de performance
sont étiquetées avec des niveaux de preuve, et dont la feuille de route
adresse explicitement l'alignement IEC 62304 Classe C.

Commencez par : [`axonos-rfcs`](https://github.com/AxonOS-org/axonos-rfcs) →
RFC-0005 (cadre de validation) et RFC-0006 (candidat ABI stable).

### Équipes cliniques et centres de réadaptation

Vous voulez un logiciel prévisible et auditable exécutant l'interface
en boucle fermée pour vos patients, avec un partenaire qui traite les
modes de défaillance comme une documentation de premier ordre, et non
comme des surprises marketing.

Contact : [info@axonos.org](mailto:info@axonos.org) — entretien
initial, parcours de pilotage clinique, processus MOU.

## Feuille de route

**Q2 2026 — Phase 1 : Validation L3**
- Mesure WCRT instrumentée par GPIO sur fixture STM32H573 avec
  Saleae Logic Pro 16
- Mesure directe de consommation sur la carte de référence
- RFC-0006 promu de candidat à stable sur la base de l'ABI validée

**Q3–Q4 2026 — Phase 2 : Pilote clinique**
- Premier déploiement du kit clinique 8 canaux
- Pilote chez le centre partenaire de réadaptation SLA, nord-est
  des États-Unis (MOU en vigueur)
- Performance du classificateur en ligne reportée aux côtés du
  benchmark hors ligne

**2027 — Phase 3 : Voie réglementaire**
- FDA Pre-Submission (Q-Sub)
- Intégration de la toolchain qualifiée Ferrocene
- Fichier complet de gestion des risques ISO 14971

**Continu**
- Réplication indépendante de la méthodologie de mesure encouragée et
  bienvenue
- Toutes les données brutes de mesure publiées avec manifestes SHA-256

## Principes d'ingénierie

Voici les règles selon lesquelles le projet vit. Elles ne sont pas
ambitieuses ; elles sont la manière dont les décisions sont prises.

1. **Aucune affirmation au-dessus de son niveau de preuve.** Si nous
   l'avons mesuré sur une carte pendant 12 heures, nous disons « L2 » ;
   nous ne disons pas « validé ».
2. **Aucun `unsafe` dans les modules révisables.** L'accès aux registres
   matériels vit dans des crates PAC auditées ; tout le reste est
   `#![forbid(unsafe_code)]`.
3. **Aucune allocation tas sur le chemin chaud.** Tampons statiques,
   dimensionnés à la compilation, ajustés au budget WCET.
4. **Aucune récupération silencieuse d'état incohérent.** Mutex
   empoisonnés, violations d'horloge et désaccords de protocole
   apparaissent comme des erreurs, pas comme des valeurs par défaut.
5. **Aucun verrouillage propriétaire via le noyau.** L'ABI est publiée
   comme RFC sous CC-BY-SA-4.0. Les implémentations tierces sont
   bienvenues.

## Licence

- **Code source** (`axonos-sdk`, `axonos-consent`, `axonos-swarm`) :
  Apache-2.0 OR MIT — à votre choix.
- **RFC d'ingénierie** (`axonos-rfcs`) : CC-BY-SA-4.0.
- **Passerelle applicative de référence** (`axon-bci-gateway`) :
  Apache-2.0 (avec attribution upstream préservée selon la licence
  d'origine).

L'utilisation commerciale, la modification et la redistribution sont
permises selon ces termes. Aucun accord de licence contributeur (CLA)
n'est requis pour les pull requests acceptées ; les contributeurs
conservent les droits d'auteur sur leurs contributions.

## Contact

- **Correspondance générale :** [info@axonos.org](mailto:info@axonos.org)
- **Divulgations de sécurité :** [security@axonos.org](mailto:security@axonos.org)
  (clé GPG sur demande)
- **Partenariats cliniques :** [clinical@axonos.org](mailto:clinical@axonos.org)
- **Web :** [axonos.org](https://axonos.org)
- **Écrits :** [medium.com/@AxonOS](https://medium.com/@AxonOS)

---

axonos.org · medium.com/@AxonOS · info@axonos.org
