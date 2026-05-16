<div align="center">

<img src="https://rustacean.net/assets/rustacean-flat-happy.svg" width="120" alt="Ferris" />

# AxonOS

### un microkernel Rust en tiempo real para interfaces cerebro–computadora

[![Built with Rust](https://img.shields.io/badge/built%20with-Rust-CE422B?style=for-the-badge&logo=rust&logoColor=white)](https://www.rust-lang.org/)
[![License](https://img.shields.io/badge/license-Apache--2.0%20OR%20MIT-blue?style=for-the-badge)](#license)
[![no_std](https://img.shields.io/badge/no__std-yes-success?style=for-the-badge)](https://docs.rust-embedded.org/book/intro/no-std.html)
[![Kani BMC](https://img.shields.io/badge/Kani-28%20proofs-blueviolet?style=for-the-badge)](https://github.com/model-checking/kani)

[🇬🇧 English](./README.md) ·
[🇯🇵 日本語](./README.ja.md) ·
[🇨🇳 中文](./README.zh.md) ·
[🇩🇪 Deutsch](./README.de.md) ·
[🇪🇸 Español](./README.es.md) ·
[🇫🇷 Français](./README.fr.md) ·
[🇮🇹 Italiano](./README.it.md)

</div>

---


## Qué es esto

AxonOS es un microkernel Rust `#![no_std]` `#![forbid(unsafe_code)]`
para pipelines de señal de interfaces cerebro-computadora (BCI) en
microcontroladores de clase Cortex-M.

Está diseñado para una clase específica de sistema: un dispositivo
pequeño y autónomo que adquiere señales neurales, clasifica la
intención del usuario y pilota un estimulador o interfaz asistencial
en lazo cerrado, con un presupuesto de tiempo real fijo, sin sistema
operativo de propósito general entre el silicio y el paciente.

En este tipo de sistemas, una deadline perdida no es una regresión
de rendimiento — es un evento adverso.

## Por qué existe

El software BCI de tiempo real actual se construye sobre tres
categorías de fundamentos, cada una estructuralmente incompatible
con el problema:

1. **Kernels de propósito general** (Linux, Windows) — diseñados
   para equidad y throughput, no para latencia worst-case acotada.
   El jitter del scheduler de Linux mainline está en el orden de
   milisegundos; PREEMPT_RT lo reduce pero no lo elimina.

2. **RTOS convencionales** (FreeRTOS, Zephyr) — ofrecen scheduling
   de tiempo real basado en prioridades, pero ninguna prueba formal
   de schedulabilidad, ninguna garantía de seguridad de memoria a
   nivel de lenguaje, y ninguna abstracción del dominio BCI.

3. **Sistemas operativos de clase aplicación sobre procesadores de
   aplicación** — traen la superficie de ataque completa y la
   imprevisibilidad de un SO general a un dispositivo médico regulado.

AxonOS llena ese vacío: un kernel pequeño, analíticamente
schedulable, escrito en un lenguaje que elimina los defectos de
seguridad de memoria en tiempo de compilación, con un modelo de
capabilities que impide que los datos neurales en bruto lleguen al
código de aplicación.

## Qué lo distingue

| Propiedad | AxonOS | RTOS mainstream | Linux PREEMPT_RT |
|:---|:---|:---|:---|
| Política de scheduling | EDF (Liu–Layland) | Prioridad fija | CFS + RT |
| Prueba analítica de schedulabilidad | Sí | No | No |
| Seguridad de memoria en tiempo de compilación | Sí (Rust) | No (C) | No (C) |
| Lógica del kernel libre de `unsafe` | Sí | No | No |
| Heap en el hot path | Ninguno | Opcional | Predeterminado |
| Aislamiento por capability BCI | Sí | Ninguno | Ninguno |
| WCET declarado con nivel de evidencia | Sí (L1/L2) | No | No |

**Importante declaración de honestidad.** AxonOS *no* reclama
verificación formal en el sentido de seL4. Utiliza teoría analítica
de scheduling de tiempo real (Liu–Layland) combinada con el sistema
de tipos de Rust y una taxonomía de validación respaldada por
mediciones. Esto es más débil que pruebas de corrección funcional
verificadas por máquina, pero es alcanzable hoy y se alinea con los
requisitos del ciclo de vida del software IEC 62304 Clase C.

## Modelo de evidencia

Cada afirmación de rendimiento en la documentación de AxonOS está
etiquetada con un nivel de evidencia:

- **L1** — Derivada por conteo de instrucciones. Calculada a partir
  del ensamblador compilado contra la referencia de timing por ciclo
  de la ISA objetivo. Conservadora; no requiere ejecución hardware.
- **L2** — Medida en runtime. Observada por instrumento on-chip
  (contador de ciclos DWT) sobre hardware de referencia durante un
  intervalo y una distribución de entrada declarados.
- **L3** — Validada por osciloscopio independiente. Observada por
  un instrumento independiente del dispositivo bajo prueba
  (analizador lógico, puntos de toggle GPIO). Requerida para
  presentación regulatoria.
- **pending** — Medición aún no realizada; fecha objetivo declarada.

Cifras principales actuales:

| Métrica | Valor | Nivel |
|:---|:---|:---|
| WCET de pipeline, época única | 640.2 µs | L1 |
| Utilización de CPU U′ (WCET inflado) | 0.179 | L1 |
| WCRT validado por GPIO (fixture H573) | — | **pending** Q2 2026 |

Hardware: STM32F407 Cortex-M4F @ 168 MHz, ADC ADS1299 de 8 canales 24 bits,
elemento seguro ATECC608B, nRF52840 BLE 5.3, aislamiento galvánico
ISO7741 5 kV.

## Qué contiene esta organización

| Repositorio | Propósito | Estado |
|:---|:---|:---|
| [`axonos-kernels`](https://github.com/AxonOS-org/axonos-kernels) | **Sustrato de kernel verificable** — siete crates, 66 tests, 28 pruebas Kani | Activo · Apache-2.0 OR MIT |
| [`axonos-rfcs`](https://github.com/AxonOS-org/axonos-rfcs) | RFCs de ingeniería que gobiernan decisiones de arquitectura | 6 RFCs · CC-BY-SA-4.0 |
| [`axonos-sdk`](https://github.com/AxonOS-org/axonos-sdk) | SDK de aplicación: intents tipados, capabilities, atestación | Apache-2.0 OR MIT |
| [`axonos-consent`](https://github.com/AxonOS-org/axonos-consent) | Implementación de referencia del AxonOS Consent Protocol | Apache-2.0 OR MIT |
| [`axonos-swarm`](https://github.com/AxonOS-org/axonos-swarm) | Coordinación multi-nodo: Neural PTP, swarm scheduler, fault detector | Apache-2.0 OR MIT |
| [`axon-bci-gateway`](https://github.com/AxonOS-org/axon-bci-gateway) | Gateway de aplicación de referencia (fork, con atribución) | Activo · Apache-2.0 |

Las fixtures de benchmark reproducibles y el código LaTeX del preprint
se publicarán junto a los resultados de la validación L3 en Q2 2026.

## Audiencia

Este proyecto está construido pensando en cuatro audiencias. Si encaja
en una de ellas, empiece donde se indica.

### Investigadores en BCI y procesamiento de señales neurales

Quieren un sustrato de tiempo real que no imponga sus propias opiniones
a su pipeline de señal, con timing predecible que puedan caracterizar
y una separación limpia entre adquisición en bruto y salida de intent
de alto nivel.

Empezar por: [`axonos-rfcs`](https://github.com/AxonOS-org/axonos-rfcs) →
RFC-0001 (arquitectura) y RFC-0004 (contrato dual-core).

### Ingenieros de sistemas embebidos

Quieren un ejemplo funcional de Rust `#![no_std]`
`#![forbid(unsafe_code)]` aplicado a scheduling hard real-time en
Cortex-M, con cifras WCET declaradas que distingan derivadas de medidas.

Empezar por: [`axonos-sdk`](https://github.com/AxonOS-org/axonos-sdk) →
ejemplos en `examples/bare_metal_no_std.rs`.

### Ingenieros de dispositivos médicos y equipos regulatorios

Quieren un sustrato kernel cuyas decisiones de arquitectura estén
documentadas como RFCs versionados, cuyas afirmaciones de rendimiento
estén etiquetadas con niveles de evidencia, y cuya hoja de ruta aborde
explícitamente el alineamiento con IEC 62304 Clase C.

Empezar por: [`axonos-rfcs`](https://github.com/AxonOS-org/axonos-rfcs) →
RFC-0005 (framework de validación) y RFC-0006 (candidato a ABI estable).

### Equipos clínicos y centros de rehabilitación

Quieren software predecible y auditable que ejecute la interfaz de lazo
cerrado para sus pacientes, con un socio que trate los modos de fallo
como documentación de primera clase, no como sorpresas de marketing.

Contacto: [connect@axonos.org](mailto:connect@axonos.org) — conversación
inicial, vía de pilotaje clínico, proceso MOU.

## Hoja de ruta

**Q2 2026 — Fase 1: Validación L3**
- Medición WCRT instrumentada por GPIO sobre fixture STM32H573 con
  Saleae Logic Pro 16
- Medición directa de consumo en la placa de referencia
- RFC-0006 promovido de candidato a estable basado en la ABI validada

**Q3–Q4 2026 — Fase 2: Pilot clínico**
- Primer despliegue del kit clínico de 8 canales
- Pilot en centro de rehabilitación ELA asociado, noreste de EE.UU.
  (MOU en vigor)
- Rendimiento del clasificador online reportado junto al benchmark
  offline

**2027 — Fase 3: Vía regulatoria**
- FDA Pre-Submission (Q-Sub)
- Integración de toolchain Ferrocene cualificada
- Archivo completo de gestión de riesgos ISO 14971

**Continuo**
- Replicación independiente de la metodología de medición animada y
  bienvenida
- Todos los datos brutos de medición publicados con manifests SHA-256

## Principios de ingeniería

Son las reglas por las que vive el proyecto. No son aspiracionales;
son la forma en que se toman las decisiones.

1. **Ninguna afirmación por encima de su nivel de evidencia.** Si lo
   medimos en una placa durante 12 horas, decimos "L2"; no decimos
   "validado".
2. **Ningún `unsafe` en módulos revisables.** El acceso a registros
   hardware vive en crates PAC auditados; todo lo demás es
   `#![forbid(unsafe_code)]`.
3. **Ninguna asignación de heap en el hot path.** Buffers estáticos,
   dimensionados en tiempo de compilación, ajustados al presupuesto
   WCET.
4. **Ninguna recuperación silenciosa de estado inconsistente.**
   Mutexes envenenados, violaciones de reloj y mismatches de
   protocolo emergen como errores, no como defaults.
5. **Ningún lock-in propietario vía el kernel.** La ABI se publica
   como RFC bajo CC-BY-SA-4.0. Implementaciones de terceros son
   bienvenidas.

## Licencia

- **Código fuente** (`axonos-sdk`, `axonos-consent`, `axonos-swarm`):
  Apache-2.0 OR MIT — usted elige.
- **RFCs de ingeniería** (`axonos-rfcs`): CC-BY-SA-4.0.
- **Gateway de aplicación de referencia** (`axon-bci-gateway`):
  Apache-2.0 (con atribución upstream preservada según la licencia
  original).

El uso comercial, la modificación y la redistribución están permitidos
bajo estos términos. No se requiere acuerdo de licencia de contribuyente
(CLA) para pull requests aceptados; los contribuyentes retienen el
copyright sobre sus contribuciones.

## Contacto

- **Correspondencia general:** [info@axonos.org](mailto:info@axonos.org)
- **Divulgaciones de seguridad:** [security@axonos.org](mailto:security@axonos.org)
  (clave GPG bajo petición)
- **Web:** [axonos.org](https://axonos.org)
- **Publicaciones:** [medium.com/@AxonOS](https://medium.com/@AxonOS)

---

<div align="center">

**Autor y mantenedor:** Denis Yermakou · [denis@axonos.org](mailto:denis@axonos.org)

Zurich · Berlin · Milano · San Mateo · Singapore

<sub>Made with 🦀</sub>

</div>
