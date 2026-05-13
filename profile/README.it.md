# AxonOS

> Un kernel real-time bare-metal per interfacce cervello-computer.
> Scritto in Rust. Open source. Costruito sull'evidenza.

[🇬🇧 English](./README.md) ·
[🇯🇵 日本語](./README.ja.md) ·
[🇮🇹 Italiano](./README.it.md) ·
[🇨🇳 中文](./README.zh.md) ·
[🇩🇪 Deutsch](./README.de.md) ·
[🇪🇸 Español](./README.es.md) ·
[🇫🇷 Français](./README.fr.md)

---

## Che cos'è

AxonOS è un microkernel Rust `#![no_std]` `#![forbid(unsafe_code)]`
per pipeline di segnali di interfacce cervello-computer (BCI)
su microcontrollori di classe Cortex-M.

È progettato per una specifica classe di sistemi: un dispositivo
piccolo e autonomo che acquisisce segnali neurali, classifica
l'intento dell'utente e pilota uno stimolatore o un'interfaccia
assistiva ad anello chiuso, con un budget real-time fisso, senza
alcun sistema operativo general-purpose interposto tra il silicio
e il paziente.

In sistemi di questo tipo, una deadline mancata non è una
regressione di performance — è un evento avverso.

## Perché esiste

Il software BCI real-time odierno si appoggia su tre categorie di
fondamenta, ciascuna strutturalmente inadeguata al problema:

1. **Kernel general-purpose** (Linux, Windows) — progettati per
   equità e throughput, non per latenza worst-case limitata.
   Il jitter dello scheduler di Linux mainline è dell'ordine
   dei millisecondi; PREEMPT_RT lo riduce ma non lo elimina.

2. **RTOS convenzionali** (FreeRTOS, Zephyr) — offrono scheduling
   real-time a priorità ma nessuna prova formale di schedulabilità,
   nessuna garanzia di memory safety a livello di linguaggio, e
   nessuna astrazione di dominio BCI.

3. **Sistemi operativi application-class su processori applicativi** —
   portano l'intera superficie di attacco e l'imprevedibilità di un
   OS generale dentro un dispositivo medicale regolamentato.

AxonOS colma questo vuoto: un kernel piccolo, analiticamente
schedulabile, scritto in un linguaggio che elimina i difetti di
memory safety a tempo di compilazione, con un modello a capability
che impedisce ai dati neurali grezzi di raggiungere il codice
applicativo.

## Cosa lo distingue

| Proprietà | AxonOS | RTOS mainstream | Linux PREEMPT_RT |
|:---|:---|:---|:---|
| Politica di scheduling | EDF (Liu–Layland) | Priorità fissa | CFS + RT |
| Prova analitica di schedulabilità | Sì | No | No |
| Memory safety a tempo di compilazione | Sì (Rust) | No (C) | No (C) |
| Logica kernel `unsafe`-free | Sì | No | No |
| Heap sull'hot path | Nessuno | Opzionale | Default |
| Isolamento per capability BCI | Sì | Nessuno | Nessuno |
| WCET dichiarato con livello di evidenza | Sì (L1/L2) | No | No |

**Importante dichiarazione di onestà.** AxonOS *non* rivendica
verifica formale nel senso di seL4. Utilizza teoria analitica
dello scheduling real-time (Liu–Layland) combinata con il sistema
di tipi di Rust e una tassonomia di validazione supportata da
misurazioni. Questo è più debole di prove di correttezza funzionale
verificate da macchina, ma è raggiungibile oggi e si allinea ai
requisiti del ciclo di vita software IEC 62304 Classe C.

## Modello di evidenza

Ogni affermazione di performance nella documentazione AxonOS è
etichettata con un livello di evidenza:

- **L1** — Derivata da conteggio istruzioni. Calcolata
  dall'assembly compilato rispetto al riferimento di timing
  per ciclo dell'ISA target. Conservativa; non richiede
  esecuzione hardware.
- **L2** — Misurata a runtime. Osservata da uno strumento
  on-chip (contatore di cicli DWT) su hardware di riferimento
  per un intervallo e una distribuzione di input dichiarati.
- **L3** — Validata da oscilloscopio indipendente. Osservata
  da uno strumento indipendente dal dispositivo sotto test
  (analizzatore logico, punti di toggle GPIO). Richiesta per
  submission regolatoria.
- **pending** — Misurazione non ancora eseguita; data target
  dichiarata.

Numeri principali attuali:

| Metrica | Valore | Livello |
|:---|:---|:---|
| WCET pipeline, singola epoca | 640.2 µs | L1 |
| WCRT end-to-end | 972 µs | L2 |
| Jitter EDF σ (10.8M epoche, 12 h) | 2.1 µs | L2 |
| Jitter EDF P99.9 | 6.5 µs | L2 |
| Deadline mancate osservate | 0 su 10.8 × 10⁶ | L2 |
| Utilizzazione CPU U′ (WCET inflazionato) | 0.179 | L1 |
| WCRT validato via GPIO (fixture H573) | — | **pending** Q2 2026 |

Hardware: STM32F407 Cortex-M4F @ 168 MHz, ADC ADS1299 8 canali 24 bit,
elemento sicuro ATECC608B, nRF52840 BLE 5.3, isolamento galvanico
ISO7741 5 kV.

## Cosa contiene questa organizzazione

| Repository | Scopo | Stato |
|:---|:---|:---|
| [`axonos-rfcs`](https://github.com/AxonOS-org/axonos-rfcs) | RFC di ingegneria che regolano le decisioni di architettura | 6 RFC · CC-BY-SA-4.0 |
| [`axonos-sdk`](https://github.com/AxonOS-org/axonos-sdk) | SDK applicativo: intent tipizzati, capability, attestazione | v0.4.0 · Apache-2.0 OR MIT |
| [`axonos-consent`](https://github.com/AxonOS-org/axonos-consent) | Implementazione di riferimento dell'AxonOS Consent Protocol | v0.4.0 · Apache-2.0 OR MIT |
| [`axonos-swarm`](https://github.com/AxonOS-org/axonos-swarm) | Coordinamento multi-nodo: Neural PTP, swarm scheduler, fault detector | v0.1.0 · Apache-2.0 OR MIT |
| [`axon-bci-gateway`](https://github.com/AxonOS-org/axon-bci-gateway) | Gateway applicativo di riferimento (fork, con attribuzione) | Attivo · Apache-2.0 |

Le fixture riproducibili di benchmark e il sorgente LaTeX del preprint
saranno pubblicati insieme ai risultati di validazione L3 nel Q2 2026.

## Pubblico

Il progetto è costruito pensando a quattro audience. Se vi riconoscete
in una di queste, partite dall'indicazione corrispondente.

### Ricercatori in BCI ed elaborazione di segnali neurali

Cercate un substrato real-time che non imponga le proprie opinioni
alla vostra pipeline di segnali, con timing predicibile caratterizzabile
e una netta separazione tra acquisizione grezza e output di intent
ad alto livello.

Inizio: [`axonos-rfcs`](https://github.com/AxonOS-org/axonos-rfcs) →
RFC-0001 (architettura) e RFC-0004 (contratto dual-core).

### Ingegneri di sistemi embedded

Cercate un esempio funzionante di Rust `#![no_std]`
`#![forbid(unsafe_code)]` applicato allo scheduling hard real-time
su Cortex-M, con cifre WCET dichiarate che distinguano derivate da
misurate.

Inizio: [`axonos-sdk`](https://github.com/AxonOS-org/axonos-sdk) →
esempi in `examples/bare_metal_no_std.rs`.

### Ingegneri di dispositivi medicali e team regolatori

Cercate un substrato kernel le cui decisioni di architettura siano
documentate come RFC versionati, le cui affermazioni di performance
abbiano livelli di evidenza, e la cui roadmap affronti esplicitamente
l'allineamento a IEC 62304 Classe C.

Inizio: [`axonos-rfcs`](https://github.com/AxonOS-org/axonos-rfcs) →
RFC-0005 (framework di validazione) e RFC-0006 (candidato ABI stabile).

### Team clinici e centri di riabilitazione

Cercate software predicibile e auditabile che pilota l'interfaccia ad
anello chiuso per i vostri pazienti, con un partner che tratta le
modalità di guasto come documentazione di prima classe, non sorprese
di marketing.

Contatto: [info@axonos.org](mailto:info@axonos.org) — conversazione
iniziale, percorso di pilot clinico, processo MOU.

## Roadmap

**Q2 2026 — Fase 1: Validazione L3**
- Misurazione WCRT strumentata via GPIO su fixture STM32H573 con
  Saleae Logic Pro 16
- Misurazione diretta del consumo energetico sulla scheda di riferimento
- RFC-0006 promosso da candidato a stabile sulla base dell'ABI validata

**Q3–Q4 2026 — Fase 2: Pilot clinico**
- Primo deployment del kit clinico a 8 canali
- Pilot presso centro di riabilitazione SLA partner, nord-est USA
  (MOU in essere)
- Performance del classificatore online riportata insieme al benchmark
  offline

**2027 — Fase 3: Percorso regolatorio**
- FDA Pre-Submission (Q-Sub)
- Integrazione toolchain Ferrocene qualificata
- File completo di risk management ISO 14971

**Continuativo**
- Replicazione indipendente della metodologia di misurazione
  incoraggiata e benvenuta
- Tutti i dati grezzi di misurazione pubblicati con manifest SHA-256

## Principi di ingegneria

Sono le regole su cui vive il progetto. Non sono aspirazionali;
sono il modo in cui si prendono le decisioni.

1. **Nessuna affermazione oltre il suo livello di evidenza.** Se
   l'abbiamo misurato su una scheda per 12 ore, diciamo "L2";
   non diciamo "validato".
2. **Nessun `unsafe` nei moduli rivedibili.** L'accesso ai registri
   hardware vive in crate PAC auditate; tutto il resto è
   `#![forbid(unsafe_code)]`.
3. **Nessuna allocazione heap sull'hot path.** Buffer statici,
   dimensionati a tempo di compilazione, dimensionati per stare nel
   budget WCET.
4. **Nessun recupero silente da stato inconsistente.** Mutex
   avvelenati, violazioni di clock, mismatch di protocollo
   emergono come errori, non come default.
5. **Nessun lock-in proprietario via kernel.** L'ABI è pubblicata
   come RFC sotto CC-BY-SA-4.0. Implementazioni di terze parti
   sono benvenute.

## Licenza

- **Codice sorgente** (`axonos-sdk`, `axonos-consent`, `axonos-swarm`):
  Apache-2.0 OR MIT — a vostra scelta.
- **RFC di ingegneria** (`axonos-rfcs`): CC-BY-SA-4.0.
- **Gateway applicativo di riferimento** (`axon-bci-gateway`):
  Apache-2.0 (con attribuzione upstream preservata secondo
  la licenza originale).

Uso commerciale, modifica e ridistribuzione sono permessi sotto
questi termini. Non è richiesto alcun contributor licence agreement
(CLA) per pull request accettate; i contributori mantengono il
copyright sui propri contributi.

## Contatti

- **Corrispondenza generale:** [info@axonos.org](mailto:info@axonos.org)
- **Divulgazioni di sicurezza:** [security@axonos.org](mailto:security@axonos.org)
  (chiave GPG su richiesta)
- **Partnership cliniche:** [clinical@axonos.org](mailto:clinical@axonos.org)
- **Web:** [axonos.org](https://axonos.org)
- **Pubblicazioni:** [medium.com/@AxonOS](https://medium.com/@AxonOS)

---

axonos.org · medium.com/@AxonOS · info@axonos.org
