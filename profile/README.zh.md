<div align="center">

<img src="./banner.jpg" alt="AxonOS — 面向脑机接口的开放认知操作系统" width="100%" />

<br/>
<br/>

# **axonos**

### 面向脑机接口的开放认知操作系统。

*英文页面为权威版本并率先更新；实时数据与最新章节见[英文页面](./README.md)。*

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

### [🌐 axonos.org](https://axonos.org) · [📐 规范](https://axonos.org/specifications.html) · [🧰 SDK](https://axonos.org/sdk.html) · [📖 文章](https://medium.com/@AxonOS) · [💬 connect@axonos.org](mailto:connect@axonos.org)

</div>

---

## 项目 AxonOS

<br/>

**AxonOS 是面向脑机接口的硬实时神经操作系统。** 使用 `#![no_std]` Rust 编写的开源内核。在普通 ARM Cortex-M 上实现亚毫秒级抖动。通过形式化方法证明最坏情况响应时间的上界。应用层无法绕过的结构化隐私。

为依赖闭环辅助接口的患者而构建,为拒绝在"尽力而为"调度上交付产品的工程师而构建。

<br/>

## 为什么需要 AxonOS

当今每一个脑机接口应用都必须为每种设备重新解析专有的二进制格式、重新实现能力门控、并为每一种新硬件平台重新编写集成代码。

**AxonOS 在形式化验证的微内核之上,用安全的 `no_std` Rust 一次性完成这三件事。** 一个可验证的基础。一个类型化的 API 表面。支持多种硬件后端。

<br/>

## 四大承诺

<br/>

|     | 承诺                          | 实际含义                                                                                                                              |
|:---:|:------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------|
| 🦀  | **普通硬件上的硬实时**         | ARMv8-M 上的 `#![no_std]` Rust。无 GC、热路径无分配器、无无界 panic。内存安全是结构化的。                                            |
| 📐  | **形式化验证的 WCRT**         | 每个关键路径操作都有 Kani 验证的上界。延迟是被*证明*的,而非被测量的。                                                              |
| 🔒  | **结构化隐私**                 | 会泄露原始认知状态的能力 (`RawEEG`、`EmotionState`、`CognitiveProfile`) 在类型系统中不存在。                                          |
| 🌐  | **开放生态**                   | 代码采用 Apache-2.0 或 MIT 许可,规范采用 CC-BY-SA-4.0。所有仓库均为公开。任何人都可以审计、分叉、或替换任何层。                      |

<br/>

## 快速开始

从克隆到第一个意图观测仅需 60 秒。

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

SDK 是 Rust 参考绑定。C FFI、Python、WebAssembly、JNI 和 Swift 绑定列在[公开路线图](https://axonos.org/sdk.html)中。

<br/>

## 仓库列表

所有 6 个仓库均已公开。源代码采用 Apache-2.0 OR MIT,规范采用 CC-BY-SA-4.0。

|                                                                              | 仓库                 | 用途                                                                              | 语言     | 最新版本   |
|:----------------------------------------------------------------------------:|:---------------------|:----------------------------------------------------------------------------------|:--------:|:-----------|
| [⬢](https://github.com/AxonOS-org/AxonOS-kernel)                              | **AxonOS-kernel**    | 硬实时微内核 — 8 个 crate,形式化验证的 WCRT,28 个 Kani 验证桩                    | Rust     | `v0.3.0`   |
| [⬢](https://github.com/AxonOS-org/axonos-sdk)                                 | **axonos-sdk**       | 应用边界 — 类型化意图、能力清单、内核 ABI v1                                       | Rust     | `v0.3.5`   |
| [⬢](https://github.com/AxonOS-org/axonos-consent)                             | **axonos-consent**   | 用于认知网格耦合的协议级同意执行 (MMP)                                            | Rust     | `v0.5.0`   |
| [⬢](https://github.com/AxonOS-org/axonos-swarm)                               | **axonos-swarm**     | 多节点协调 — Neural PTP 同步,集群调度                                              | Rust     | `v0.2.1`   |
| [⬢](https://github.com/AxonOS-org/axonos-rfcs)                                | **axonos-rfcs**      | 工程规范 — 8 个编号 RFC,规范性,CC-BY-SA-4.0                                       | Markdown | active     |
| [⬢](https://github.com/AxonOS-org/axon-bci-gateway)                           | **axon-bci-gateway** | 硬件采集网关 (OpenBCI 分叉,从上游保留 MIT)                                        | HTML     | active     |

<br/>

## 架构

<br/>

```mermaid
flowchart LR
    A[EEG/EMG 传感器<br/>ADS1299 · 24-bit] -->|raw| B[BCI 网关<br/>nRF52840]
    B -->|filtered| C[AxonOS 内核<br/>Rust no_std<br/>Cortex-M4F]
    C -->|WCRT<br/>≤ 1 ms (L1)| D[认知<br/>调度器]
    D -->|typed intent| E[应用<br/>via SDK]
    F[Cognitive Hypervisor<br/>TrustZone-S] -.->|isolates| C
    G[同意层<br/>MMP protocol] -.->|gates| D

    classDef kernel fill:#0e2a47,stroke:#3b82f6,color:#fff,stroke-width:2px
    classDef secure fill:#0a3d2e,stroke:#10b981,color:#fff,stroke-width:2px
    class C kernel
    class F,G secure
```

<br/>

## 数字一览

<br/>

<table align="center">
<tr>
  <td align="center" width="200">
    <h2>≤ 1 ms</h2>
    <sub>内核 WCRT 已证明（L1）<br/>STM32F407 @ 168 MHz</sub>
  </td>
  <td align="center" width="200">
    <h2>2.1 µs</h2>
    <sub>最坏抖动 σ<br/>对比 Linux 1323 µs</sub>
  </td>
  <td align="center" width="200">
    <h2>630×</h2>
    <sub>改进倍数<br/>对比 Linux mainline</sub>
  </td>
</tr>
<tr>
  <td align="center">
    <h2>30</h2>
    <sub>Kani BMC 验证桩<br/>上界已证明</sub>
  </td>
  <td align="center">
    <h2>66+</h2>
    <sub>单元与集成测试<br/>覆盖整个工作区</sub>
  </td>
  <td align="center">
    <h2>42+</h2>
    <sub>长篇架构文章<br/>发表于 Medium</sub>
  </td>
</tr>
</table>

<br/>

## 状态

<br/>

| 阶段          | 内容                                                                                              | 时间        |
|:--------------|:--------------------------------------------------------------------------------------------------|:------------|
| **阶段 0**    | 架构、RFC、SDK API、内核验证桩                                                                       | ✓ 完成      |
| **阶段 1**    | 临床级 8 通道开发套件 · ALS 中心临床试点                                                              | 🟡 2026 Q2  |
| **阶段 2**    | Cognitive Hypervisor 的 FDA 510(k) Q-Sub · IEEE P2731 贡献                                          | 🔵 2026 Q3  |
| **阶段 3**    | 首个商业部署                                                                                          | 🔵 2027     |

<br/>

## 许可

| 工件                                  | 许可证                                              |
|:--------------------------------------|:----------------------------------------------------|
| 内核、SDK、consent、swarm、gateway     | Apache-2.0 OR MIT                                   |
| RFC 与规范                             | CC-BY-SA-4.0                                        |
| `axon-bci-gateway`                    | MIT (从上游 OpenBCI_GUI 保留)                       |

<br/>
<br/>

---

<div align="center">

<img src="./logo.png" width="72" alt="AxonOS 标志" />

<br/>
<br/>

**由 Denis Yermakou 构建和维护**

[denis@axonos.org](mailto:denis@axonos.org) · [LinkedIn](https://www.linkedin.com/in/denis-yermakou) · [Medium](https://medium.com/@AxonOS) · [Site](https://axonos.org)

<sub>Singapore · Zurich · Berlin · Milano · San Mateo</sub>

<br/>

<sub>用 Rust 构建。用 Kani 验证。面向硬实时。</sub>

</div>
