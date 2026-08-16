<div align="center">

<img src="./banner.jpg" alt="AxonOS — نظام التشغيل المعرفي المفتوح لواجهات الدماغ والحاسوب" width="100%" />

<br/>
<br/>

# **axonos**

### نظام التشغيل المعرفي المفتوح لواجهات الدماغ والحاسوب.

*الصفحة الإنجليزية هي المرجع الرسمي ويتم تحديثها أولاً؛ البيانات الحية والأقسام الأحدث تظهر [هناك](./README.md).*

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

[![SDK](https://img.shields.io/badge/SDK-v0.3.5-0a4a8f?style=flat-square)](https://github.com/AxonOS-org/axonos-sdk)
[![Kernel](https://img.shields.io/badge/Kernel-v0.3.0-0a4a8f?style=flat-square)](https://github.com/AxonOS-org/AxonOS-kernel)
[![ABI](https://img.shields.io/badge/Kernel%20ABI-v1-0a4a8f?style=flat-square)](https://axonos.org/specifications.html)
[![Rust](https://img.shields.io/badge/built%20with-Rust-CE422B?style=flat-square&logo=rust&logoColor=white)](https://www.rust-lang.org/)
[![License](https://img.shields.io/badge/license-Apache--2.0%20OR%20MIT-475569?style=flat-square)](#licensing)

### [🌐 axonos.org](https://axonos.org) · [📐 المواصفات](https://axonos.org/specifications.html) · [🧰 SDK](https://axonos.org/sdk.html) · [📖 المقالات](https://medium.com/@AxonOS) · [💬 connect@axonos.org](mailto:connect@axonos.org)

</div>

---

<div dir="rtl" align="right">

## مشروع AxonOS

<br/>

**AxonOS هو نظام تشغيل عصبي ذو زمن حقيقي صارم لواجهات الدماغ والحاسوب.** نواة مفتوحة المصدر مكتوبة بلغة `#![no_std]` Rust. اضطراب زمني أقل من ميلي ثانية على معالجات ARM Cortex-M التجارية. حدود عليا لزمن الاستجابة في أسوأ الحالات (WCRT) مُتحقق منها رسمياً. خصوصية بنيوية لا يمكن لطبقة التطبيق تجاوزها.

تم بناؤه من أجل المرضى الذين يعتمدون على واجهات مساعدة ذات حلقة مغلقة، ومن أجل المهندسين الذين يرفضون شحنها بجدولة "أفضل جهد ممكن".

<br/>

## لماذا يوجد AxonOS

اليوم، يجب على كل تطبيق لواجهة الدماغ والحاسوب أن يعيد تحليل تنسيق ثنائي خاص لكل جهاز، وأن يعيد تنفيذ آلية بوابات الصلاحيات، وأن يعيد كتابة الشيفرة التكاملية لكل منصة عتاد جديدة.

**يقوم AxonOS بهذه المهام الثلاث مرة واحدة، بلغة `no_std` Rust الآمنة، فوق نواة مصغرة محدودة رسمياً.** أساس واحد قابل للتحقق. سطح واجهة برمجية واحد بأنواع محددة. واجهات خلفية عتادية متعددة.

<br/>

## الالتزامات الأربعة

<br/>

|     | الالتزام                       | ماذا يعني في الممارسة                                                                                                              |
|:---:|:------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------|
| 🦀  | **زمن حقيقي صارم على عتاد تجاري** | Rust `#![no_std]` على ARMv8-M. لا جامع قمامة، لا مُخصِّص ذاكرة في المسار الحرج، لا حالات panic غير محدودة.                          |
| 📐  | **WCRT محدود رسمياً**         | كل عملية في المسار الحرج لها حد أعلى مُتحقَّق منه بواسطة Kani. زمن الاستجابة *مُبرهَن* وليس مُقاساً.                              |
| 🔒  | **خصوصية بنيوية**              | الصلاحيات التي قد تكشف الحالة المعرفية الخام (`RawEEG`، `EmotionState`، `CognitiveProfile`) غير موجودة كأنواع.                  |
| 🌐  | **منظومة مفتوحة**              | Apache-2.0 أو MIT للشيفرة، CC-BY-SA-4.0 للمواصفات. جميع المستودعات عامة. يمكن لأي شخص تدقيق أو نسخ أو استبدال أي طبقة.            |

<br/>

## البداية السريعة

ستون ثانية من الاستنساخ إلى أول ملاحظة نية.

</div>

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

<div dir="rtl" align="right">

SDK هو الربط المرجعي بلغة Rust. روابط C FFI و Python و WebAssembly و JNI و Swift مذكورة في [خارطة الطريق المنشورة](https://axonos.org/sdk.html).

<br/>

## المستودعات

جميع المستودعات الستة عامة. الشيفرة المصدرية تحت Apache-2.0 OR MIT. المواصفات تحت CC-BY-SA-4.0.

|                                                                              | المستودع              | الغرض                                                                              | اللغة    | الأحدث     |
|:----------------------------------------------------------------------------:|:---------------------|:----------------------------------------------------------------------------------|:--------:|:-----------|
| [⬢](https://github.com/AxonOS-org/AxonOS-kernel)                              | **AxonOS-kernel**    | نواة مصغرة ذات زمن حقيقي صارم — 8 صناديق، WCRT محدود رسمياً، 28 أداة تحقق Kani    | Rust     | `v0.3.0`   |
| [⬢](https://github.com/AxonOS-org/axonos-sdk)                                 | **axonos-sdk**       | حدود التطبيق — نوايا مُنوَّعة، بيانات الصلاحيات، ABI النواة v1                    | Rust     | `v0.3.5`   |
| [⬢](https://github.com/AxonOS-org/axonos-consent)                             | **axonos-consent**   | إنفاذ الموافقة على مستوى البروتوكول لاقتران الشبكة المعرفية (MMP)                 | Rust     | `v0.5.0`   |
| [⬢](https://github.com/AxonOS-org/axonos-swarm)                               | **axonos-swarm**     | تنسيق متعدد العقد — مزامنة Neural PTP، جدولة السرب                                | Rust     | `v0.2.1`   |
| [⬢](https://github.com/AxonOS-org/axonos-rfcs)                                | **axonos-rfcs**      | مواصفات هندسية — 8 RFCs مرقمة، معيارية، CC-BY-SA-4.0                              | Markdown | نشط        |
| [⬢](https://github.com/AxonOS-org/axon-bci-gateway)                           | **axon-bci-gateway** | بوابة استحواذ العتاد (فرع من OpenBCI، رخصة MIT محفوظة من المنبع)                 | HTML     | نشط        |

<br/>

## البنية المعمارية

</div>

<br/>

```mermaid
flowchart LR
    A[مستشعرات EEG/EMG<br/>ADS1299 · 24-bit] -->|raw| B[بوابة BCI<br/>nRF52840]
    B -->|filtered| C[نواة AxonOS<br/>Rust no_std<br/>Cortex-M4F]
    C -->|WCRT<br/>≤ 1 ms (L1)| D[المُجدول<br/>المعرفي]
    D -->|typed intent| E[التطبيق<br/>via SDK]
    F[المراقب المعرفي<br/>TrustZone-S] -.->|isolates| C
    G[طبقة الموافقة<br/>MMP protocol] -.->|gates| D

    classDef kernel fill:#0e2a47,stroke:#3b82f6,color:#fff,stroke-width:2px
    classDef secure fill:#0a3d2e,stroke:#10b981,color:#fff,stroke-width:2px
    class C kernel
    class F,G secure
```

<br/>

<div dir="rtl" align="right">

## بالأرقام

<br/>

<table align="center">
<tr>
  <td align="center" width="200">
    <h2>≤ 1 ms</h2>
    <sub>WCRT النواة، مُثبَت (L1)<br/>STM32F407 @ 168 MHz</sub>
  </td>
  <td align="center" width="200">
    <h2>2.1 µs</h2>
    <sub>اضطراب σ في أسوأ الحالات<br/>مقابل Linux 1323 µs</sub>
  </td>
  <td align="center" width="200">
    <h2>630×</h2>
    <sub>عامل التحسين<br/>مقابل Linux mainline</sub>
  </td>
</tr>
<tr>
  <td align="center">
    <h2>30</h2>
    <sub>أدوات تحقق Kani BMC<br/>حدود عليا مُبرهنة</sub>
  </td>
  <td align="center">
    <h2>66+</h2>
    <sub>اختبارات وحدة وتكامل<br/>عبر مساحة العمل بأكملها</sub>
  </td>
  <td align="center">
    <h2>42+</h2>
    <sub>مقالات بنية معمارية<br/>منشورة على Medium</sub>
  </td>
</tr>
</table>

<br/>

## الحالة

<br/>

| المرحلة      | المحتوى                                                                                    | الموعد         |
|:-------------|:-------------------------------------------------------------------------------------------|:---------------|
| **المرحلة 0** | البنية المعمارية، RFCs، واجهة SDK، أدوات تحقق النواة                                          | ✓ مكتمل        |
| **المرحلة 1** | عُدة تطوير سريرية (8 قنوات) · تجربة في مركز ALS                                              | 🟡 الربع الثاني 2026 |
| **المرحلة 2** | FDA 510(k) Q-Sub لـ Cognitive Hypervisor · مساهمة في IEEE P2731                              | 🔵 الربع الثالث 2026 |
| **المرحلة 3** | أول نشر تجاري عبر أعضاء المؤسسة                                                              | 🔵 2027        |

<br/>

## الترخيص

| المُنتَج                              | الترخيص                                            |
|:--------------------------------------|:---------------------------------------------------|
| النواة، SDK، consent، swarm، gateway   | Apache-2.0 OR MIT                                  |
| RFCs والمواصفات                        | CC-BY-SA-4.0                                       |
| `axon-bci-gateway`                    | MIT (محفوظة من المنبع OpenBCI_GUI)                 |

</div>

<br/>
<br/>

---

<div align="center">

<img src="./logo.png" width="72" alt="شعار AxonOS" />

<br/>
<br/>

**بُني وصُين بواسطة Denis Yermakou**

[denis@axonos.org](mailto:denis@axonos.org) · [LinkedIn](https://www.linkedin.com/in/denis-yermakou) · [Medium](https://medium.com/@AxonOS) · [Site](https://axonos.org)

<sub></sub>

<br/>

<sub>مبني بـ Rust. مُتحقَّق منه بـ Kani. مُوجَّه للزمن الحقيقي الصارم.</sub>

</div>
