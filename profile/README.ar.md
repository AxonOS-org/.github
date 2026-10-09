<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/AxonOS-org/.github/raw/main/profile/assets/hero-dark.svg">
  <img alt="AxonOS — بنية تحتية حتمية لواجهات الدماغ والحاسوب" src="https://github.com/AxonOS-org/.github/raw/main/profile/assets/hero-light.svg" width="100%">
</picture>

### بنية تحتية حتمية لواجهات الدماغ والحاسوب.

<sub>هذه الصفحة تلخيص [للصفحة الإنجليزية](./README.md). الصفحة الإنجليزية هي المرجع، وفيها الإصدارات والمستودعات والأدلة.</sub>

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

## ما هو AxonOS

<div dir="rtl">

AxonOS هو طبقة الزمن الحقيقي الصارم بين العتاد العصبي والتطبيقات التي تستخدمه: نواة مفتوحة المصدر مكتوبة بلغة Rust بنمط `#![no_std]` لمعالجات ARM Cortex-M. صُممت بحيث تُحلَّل أزمنة الاستجابة في أسوأ الحالات قبل التشغيل لا أن تُقاس بعده، وبحيث تُفرض الخصوصية **تحت طبقة التطبيقات** حيث لا يستطيع أي تطبيق تجاوزها.

> تتلقى التطبيقات أحداث نية محددة النوع ومقيدة بالموافقة — ولا تتلقى أبدًا تدفقات عصبية خامًا.

## ما هو مُثبت اليوم

ثلاث خصائص مُثبتة بأداة التحقق المحدود من النماذج Kani، كلٌّ منها ضمن نطاق مُعلن (المستوى **L1**):

- القبول واختيار المُجدول وفق أقرب موعد نهائي (EDF)؛
- الحلقة ذات المنتج الواحد والمستهلك الواحد: ذهاب وإياب دقيق، وإدراج بلا حلقات، وترتيب FIFO؛
- الموافقة: لا تغيير في الحالة دون توقيع مُتحقق منه، ولا قبول لتسلسل مرتين، والسحب نهائي.

**لا يُدّعى اليوم أي رقم زمني.** قيمة 1000 ميكروثانية في المعيار متطلب وليست نتيجة: لا يوجد بعدُ إثبات لزمن الاستجابة ولا قياس منشور على العتاد المرجعي. الحالة المعتمدة موجودة في [فهرس الادعاءات](https://github.com/AxonOS-org/axonos-standard/blob/main/CLAIMS.md).

## المستودعات

جميع المستودعات عامة: الشيفرة بترخيص Apache-2.0 OR MIT والمواصفات بترخيص CC-BY-SA-4.0. القائمة الكاملة بالإصدارات الحالية موجودة في [الصفحة الإنجليزية](./README.md) وعلى [github.com/AxonOS-org](https://github.com/AxonOS-org).

</div>

---

<div align="center">

© The AxonOS Project / Denis Yermakou

[connect@axonos.org](mailto:connect@axonos.org) · [security@axonos.org](mailto:security@axonos.org) · [LinkedIn](https://www.linkedin.com/in/axonos) · [axonos.org](https://axonos.org)

<sub>يجري النظر في إنشاء مكاتب ومقر رئيسي مستقبلًا.</sub>

</div>
