<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/AxonOS-org/.github/raw/main/profile/assets/hero-dark.svg">
  <img alt="AxonOS — 面向脑机接口的确定性基础设施" src="https://github.com/AxonOS-org/.github/raw/main/profile/assets/hero-light.svg" width="100%">
</picture>

### 面向脑机接口的确定性基础设施。

<sub>本页是[英文页面](./README.md)的摘要。英文页面为准；版本、仓库和证据均以英文页面为准。</sub>

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

## AxonOS 是什么

AxonOS 是位于神经硬件与使用它的应用之间的硬实时层：一个面向 ARM Cortex-M、用 `#![no_std]` Rust 编写的开源内核。它的设计目标是在运行之前分析最坏情况响应时间，而不是事后测量；隐私在**应用层之下**强制执行，任何应用都无法绕过。

> 应用收到的是有类型、受同意约束的意图事件——绝不是原始神经数据流。

## 目前已证明的内容

以下三项性质已用有界模型检验器 Kani 在各自声明的范围内证明（**L1** 级）：

- 调度器的准入与最早截止期优先（EDF）选择；
- 单生产者单消费者环形缓冲：往返精确、插入无循环、先进先出顺序；
- 同意：没有经过验证的签名不会发生状态变化，同一序列不会被接受两次，撤回是最终的。

**目前不声称任何时间数值。** 标准中的 1 000 µs 是要求，而不是结果：目前既没有响应时间的证明，也没有在参考硬件上公开的测量。权威状态见[声明目录](https://github.com/AxonOS-org/axonos-standard/blob/main/CLAIMS.md)。

## 仓库

所有仓库均公开：代码采用 Apache-2.0 OR MIT，规范采用 CC-BY-SA-4.0。包含当前版本的完整列表见[英文页面](./README.md)和 [github.com/AxonOS-org](https://github.com/AxonOS-org)。

---

<div align="center">

© The AxonOS Project / Denis Yermakou

[connect@axonos.org](mailto:connect@axonos.org) · [security@axonos.org](mailto:security@axonos.org) · [LinkedIn](https://www.linkedin.com/in/axonos) · [axonos.org](https://axonos.org)

<sub>未来考虑设立办公室和总部。</sub>

</div>
