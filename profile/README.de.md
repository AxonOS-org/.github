# AxonOS

> Ein Bare-Metal-Echtzeitkernel für Brain-Computer-Interfaces.
> Geschrieben in Rust. Open Source. Auf Evidenz aufgebaut.

[🇬🇧 English](./README.md) ·
[🇯🇵 日本語](./README.ja.md) ·
[🇮🇹 Italiano](./README.it.md) ·
[🇨🇳 中文](./README.zh.md) ·
[🇩🇪 Deutsch](./README.de.md) ·
[🇪🇸 Español](./README.es.md) ·
[🇫🇷 Français](./README.fr.md)

---

## Was das ist

AxonOS ist ein `#![no_std]` `#![forbid(unsafe_code)]` Rust-Mikrokernel
für Signalpipelines von Brain-Computer-Interfaces (BCI) auf
Mikrocontrollern der Cortex-M-Klasse.

Es ist für eine spezifische Systemklasse konzipiert: ein kleines,
autonomes Gerät, das neuronale Signale erfasst, die Nutzerintention
klassifiziert und einen Stimulator oder eine assistive Schnittstelle
in einer geschlossenen Regelschleife mit festem Echtzeitbudget
ansteuert — ohne dass ein General-Purpose-Betriebssystem zwischen
Silizium und Patient liegt.

In Systemen dieser Art ist eine verpasste Deadline keine
Leistungsregression — sondern ein unerwünschtes Ereignis.

## Warum es existiert

Echtzeit-BCI-Software basiert heute auf drei Kategorien von Grundlagen,
die jeweils strukturell nicht zum Problem passen:

1. **General-Purpose-Kernel** (Linux, Windows) — für Fairness und
   Durchsatz entworfen, nicht für beschränkte Worst-Case-Latenz.
   Der Scheduler-Jitter von Mainline-Linux liegt im Millisekundenbereich;
   PREEMPT_RT reduziert ihn, aber eliminiert ihn nicht.

2. **Konventionelle RTOS** (FreeRTOS, Zephyr) — bieten
   prioritätsbasiertes Echtzeit-Scheduling, aber keinen formalen
   Schedulierbarkeitsbeweis, keine sprachseitige Speichersicherheits-
   garantie und keine BCI-Domänenabstraktionen.

3. **Application-Class-Betriebssysteme auf Anwendungsprozessoren** —
   bringen die volle Angriffsfläche und Unvorhersehbarkeit eines
   allgemeinen OS in ein reguliertes medizinisches Gerät.

AxonOS schließt diese Lücke: ein kleiner, analytisch schedulierbarer
Kernel, geschrieben in einer Sprache, die Speichersicherheitsdefekte
zur Compilezeit eliminiert, mit einem Capability-Modell, das verhindert,
dass rohe neuronale Daten den Anwendungscode erreichen.

## Was ihn unterscheidet

| Eigenschaft | AxonOS | Mainstream-RTOS | Linux PREEMPT_RT |
|:---|:---|:---|:---|
| Scheduling-Strategie | EDF (Liu–Layland) | Feste Priorität | CFS + RT |
| Analytischer Schedulierbarkeitsbeweis | Ja | Nein | Nein |
| Speichersicherheit zur Compilezeit | Ja (Rust) | Nein (C) | Nein (C) |
| `unsafe`-freie Kernel-Logik | Ja | Nein | Nein |
| Heap auf dem Hot Path | Keiner | Optional | Standard |
| BCI-Capability-Isolation | Ja | Keine | Keine |
| Deklariertes WCET mit Evidenzstufe | Ja (L1/L2) | Nein | Nein |

**Wichtige Ehrlichkeits-Offenlegung.** AxonOS beansprucht *keine*
formale Verifikation im Sinne von seL4. Es verwendet analytische
Echtzeit-Scheduling-Theorie (Liu–Layland) in Kombination mit dem
Typsystem von Rust und einer messungsgestützten Validierungstaxonomie.
Das ist schwächer als maschinell geprüfte Beweise funktionaler
Korrektheit, ist aber heute erreichbar und steht im Einklang mit
den Anforderungen des IEC-62304-Klasse-C-Softwarelebenszyklus.

## Evidenzmodell

Jede Leistungsaussage in der AxonOS-Dokumentation ist mit einer
Evidenzstufe gekennzeichnet:

- **L1** — Aus Instruktionszählung abgeleitet. Berechnet aus dem
  kompilierten Assembly gegen die veröffentlichte Zyklus-Timing-
  Referenz der Ziel-ISA. Konservativ; keine Hardware-Ausführung nötig.
- **L2** — Zur Laufzeit gemessen. Beobachtet durch ein On-Chip-
  Instrument (DWT-Zykluszähler) auf Referenzhardware über einen
  angegebenen Zeitraum und eine angegebene Eingangsverteilung.
- **L3** — Unabhängig oszilloskopisch validiert. Beobachtet durch
  ein Instrument unabhängig vom Prüfgerät (Logikanalysator,
  GPIO-Toggle-Punkte). Erforderlich für regulatorische Einreichung.
- **pending** — Messung noch nicht durchgeführt; Zieldatum angegeben.

Aktuelle Kennzahlen:

| Metrik | Wert | Stufe |
|:---|:---|:---|
| Pipeline-WCET, einzelne Epoche | 640.2 µs | L1 |
| End-to-End-WCRT | 972 µs | L2 |
| EDF-Jitter σ (10.8M Epochen, 12 h) | 2.1 µs | L2 |
| EDF-Jitter P99.9 | 6.5 µs | L2 |
| Beobachtete Deadline-Verletzungen | 0 von 10.8 × 10⁶ | L2 |
| CPU-Auslastung U′ (inflationiertes WCET) | 0.179 | L1 |
| GPIO-validiertes WCRT (H573-Fixture) | — | **pending** Q2 2026 |

Hardware: STM32F407 Cortex-M4F @ 168 MHz, ADS1299 8-Kanal-24-Bit-ADC,
ATECC608B Secure Element, nRF52840 BLE 5.3, ISO7741 5 kV galvanische
Trennung.

## Was diese Organisation enthält

| Repository | Zweck | Status |
|:---|:---|:---|
| [`axonos-rfcs`](https://github.com/AxonOS-org/axonos-rfcs) | Engineering-RFCs zur Steuerung von Architekturentscheidungen | 6 RFCs · CC-BY-SA-4.0 |
| [`axonos-sdk`](https://github.com/AxonOS-org/axonos-sdk) | Application SDK: typisierte Intents, Capabilities, Attestation | v0.4.0 · Apache-2.0 OR MIT |
| [`axonos-consent`](https://github.com/AxonOS-org/axonos-consent) | Referenzimplementierung des AxonOS Consent Protocol | v0.4.0 · Apache-2.0 OR MIT |
| [`axonos-swarm`](https://github.com/AxonOS-org/axonos-swarm) | Multi-Knoten-Koordination: Neural PTP, Swarm-Scheduler, Fault-Detector | v0.1.0 · Apache-2.0 OR MIT |
| [`axon-bci-gateway`](https://github.com/AxonOS-org/axon-bci-gateway) | Referenz-Application-Gateway (Fork, mit Attribution) | Aktiv · Apache-2.0 |

Die reproduzierbaren Benchmark-Fixtures und der LaTeX-Quelltext des
Preprints werden zusammen mit den L3-Validierungsergebnissen im Q2 2026
veröffentlicht.

## Zielgruppen

Dieses Projekt wurde mit vier Zielgruppen im Sinn entwickelt. Wenn Sie
zu einer davon gehören, beginnen Sie an der angegebenen Stelle.

### Forscher in BCI und neuronaler Signalverarbeitung

Sie suchen eine Echtzeit-Grundlage, die Ihrer Signalpipeline ihre
eigenen Meinungen nicht aufzwingt, mit vorhersehbaren, charakterisierbaren
Timings und einer sauberen Trennung zwischen Rohaquisition und Intent-
Ausgabe auf hohem Niveau.

Beginnen Sie mit: [`axonos-rfcs`](https://github.com/AxonOS-org/axonos-rfcs) →
RFC-0001 (Architektur) und RFC-0004 (Dual-Core-Kontrakt).

### Embedded-Systems-Ingenieure

Sie suchen ein funktionierendes Beispiel für `#![no_std]`
`#![forbid(unsafe_code)]` Rust auf Hard-Realtime-Scheduling unter
Cortex-M, mit deklarierten WCET-Zahlen, die abgeleitet von gemessen
unterscheiden.

Beginnen Sie mit: [`axonos-sdk`](https://github.com/AxonOS-org/axonos-sdk) →
Beispiele in `examples/bare_metal_no_std.rs`.

### Medizingeräte-Ingenieure und regulatorische Teams

Sie suchen eine Kernel-Grundlage, deren Architekturentscheidungen als
versionierte RFCs dokumentiert sind, deren Leistungsaussagen mit
Evidenzstufen markiert sind und deren Roadmap die IEC-62304-Klasse-C-
Ausrichtung explizit adressiert.

Beginnen Sie mit: [`axonos-rfcs`](https://github.com/AxonOS-org/axonos-rfcs) →
RFC-0005 (Validierungs-Framework) und RFC-0006 (Stabile-ABI-Kandidat).

### Klinische Teams und Reha-Zentren

Sie suchen vorhersehbare, prüfbare Software, die die geschlossene
Regelschleife für Ihre Patienten betreibt — mit einem Partner, der
Fehlermodi als erstklassige Dokumentation behandelt, nicht als
Marketing-Überraschung.

Kontakt: [connect@axonos.org](mailto:connect@axonos.org) — Erstgespräch,
klinischer Pilot-Pfad, MOU-Prozess.

## Roadmap

**Q2 2026 — Phase 1: L3-Validierung**
- GPIO-instrumentierte WCRT-Messung auf STM32H573-Fixture mit
  Saleae Logic Pro 16
- Direkte Leistungsverbrauchsmessung auf der Referenzplatine
- RFC-0006 wird auf Basis der validierten ABI von Kandidat zu stabil
  erhoben

**Q3–Q4 2026 — Phase 2: Klinischer Pilot**
- Erstes 8-Kanal-Klinikkit-Deployment
- Pilot im ALS-Reha-Partnerzentrum, Nordosten der USA
  (MOU vorhanden)
- Online-Klassifikatorleistung neben Offline-Benchmark berichtet

**2027 — Phase 3: Regulatorischer Pfad**
- FDA Pre-Submission (Q-Sub)
- Integration der Ferrocene-qualifizierten Toolchain
- Vollständige ISO-14971-Risikomanagement-Datei

**Fortlaufend**
- Unabhängige Reproduktion der Messmethodik wird ermutigt und
  begrüßt
- Alle Mess-Rohdaten werden mit SHA-256-Manifesten veröffentlicht

## Engineering-Prinzipien

Dies sind die Regeln, nach denen das Projekt lebt. Sie sind keine
Wünsche; sie sind die Art, wie Entscheidungen getroffen werden.

1. **Keine Aussage über ihrer Evidenzstufe.** Wenn wir es auf einer
   Platine 12 Stunden lang gemessen haben, sagen wir „L2"; wir sagen
   nicht „validiert".
2. **Kein `unsafe` in überprüfbaren Modulen.** Hardware-Register-
   Zugriff lebt in auditierten PAC-Crates; alles andere ist
   `#![forbid(unsafe_code)]`.
3. **Keine Heap-Allokation auf dem Hot Path.** Statische Puffer,
   zur Compilezeit dimensioniert, passend zum WCET-Budget.
4. **Keine stille Wiederherstellung aus inkonsistentem Zustand.**
   Vergiftete Mutexe, Uhrenverletzungen und Protokoll-Diskrepanzen
   erscheinen als Fehler, nicht als Default-Werte.
5. **Kein proprietäres Lock-in über den Kernel.** Die ABI wird als
   RFC unter CC-BY-SA-4.0 veröffentlicht. Drittimplementierungen
   sind willkommen.

## Lizenz

- **Quellcode** (`axonos-sdk`, `axonos-consent`, `axonos-swarm`):
  Apache-2.0 OR MIT — Ihre Wahl.
- **Engineering-RFCs** (`axonos-rfcs`): CC-BY-SA-4.0.
- **Referenz-Application-Gateway** (`axon-bci-gateway`): Apache-2.0
  (mit Upstream-Attribution gemäß Originallizenz erhalten).

Kommerzielle Nutzung, Modifikation und Weiterverteilung sind unter
diesen Bedingungen gestattet. Für akzeptierte Pull Requests ist
keine Contributor Licence Agreement (CLA) erforderlich; Beitragende
behalten das Urheberrecht an ihren Beiträgen.

## Kontakt

- **Allgemeine Korrespondenz:** [info@axonos.org](mailto:info@axonos.org)
- **Sicherheitsoffenlegungen:** [security@axonos.org](mailto:security@axonos.org)
  (GPG-Schlüssel auf Anfrage)
- **Web:** [axonos.org](https://axonos.org)
- **Schriften:** [medium.com/@AxonOS](https://medium.com/@AxonOS)

---

axonos.org · medium.com/@AxonOS · info@axonos.org
