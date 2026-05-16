<div align="center">

<img src="https://rustacean.net/assets/rustacean-flat-happy.svg" width="120" alt="Ferris" />

# AxonOS

### 面向脑–机接口的实时 Rust 微内核

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


## 这是什么

AxonOS 是一个 `#![no_std]` `#![forbid(unsafe_code)]` 的 Rust 微内核,
用于在 Cortex-M 级微控制器上运行脑机接口 (BCI) 信号管道。

它面向一类特定的系统:一个小型自主设备,采集神经信号、分类用户意图,
并在固定的实时预算下,以闭环方式驱动刺激器或辅助接口,
硅片与患者之间不介入任何通用操作系统。

在此类系统中,错过截止期不是性能退化——而是不良事件。

## 为何存在

当今的实时 BCI 软件构建于三类基础之上,每一类都与问题存在结构性失配:

1. **通用内核** (Linux, Windows) — 为公平性和吞吐量设计,而非
   有界最坏情况延迟。主线 Linux 调度器抖动在毫秒量级;
   PREEMPT_RT 减少了这一抖动,但不能消除。

2. **传统 RTOS** (FreeRTOS, Zephyr) — 提供基于优先级的实时调度,
   但无形式化可调度性证明、无语言级内存安全保证,亦无 BCI 领域抽象。

3. **应用处理器上的应用级操作系统** — 将通用操作系统的全部攻击面和
   不可预测性引入受监管的医疗设备。

AxonOS 填补这一空白:一个小型的、可分析调度的内核,以一种在编译期
消除内存安全缺陷的语言编写,具备防止原始神经数据到达应用代码的
能力 (Capability) 模型。

## 与众不同之处

| 特性 | AxonOS | 主流 RTOS | Linux PREEMPT_RT |
|:---|:---|:---|:---|
| 调度策略 | EDF (Liu–Layland) | 固定优先级 | CFS + RT |
| 解析式可调度性证明 | 是 | 否 | 否 |
| 编译期内存安全 | 是 (Rust) | 否 (C) | 否 (C) |
| 无 `unsafe` 的内核逻辑 | 是 | 否 | 否 |
| 热路径上的堆分配 | 无 | 可选 | 默认 |
| BCI 能力隔离 | 是 | 无 | 无 |
| 带证据级别的 WCET 声明 | 是 (L1/L2) | 否 | 否 |

**重要的诚实声明。** AxonOS **不**主张 seL4 意义上的形式验证。
它使用解析式实时调度理论 (Liu–Layland),结合 Rust 类型系统和
基于测量的验证分类法。这弱于机器检验的功能正确性证明,但今日可达,
并与 IEC 62304 C 类软件生命周期要求相一致。

## 证据模型

AxonOS 文档中的每一项性能声明都附有证据级别:

- **L1** — 从指令计数导出。基于编译后的汇编,与目标 ISA 已发布的
  周期时序参考相乘计算。保守;无需硬件执行。
- **L2** — 运行时测量。在指定的时间段和输入分布下,
  通过参考硬件上的片上仪表 (DWT 周期计数器) 观测得到。
- **L3** — 独立示波器验证。由独立于被测设备的仪器 (逻辑分析仪、
  GPIO 翻转点) 观测。监管申报所必需。
- **pending** — 测量尚未执行;目标日期已声明。

当前主要数据:

| 度量 | 取值 | 级别 |
|:---|:---|:---|
| 单个 epoch 流水线 WCET | 640.2 µs | L1 |
| CPU 利用率 U′ (膨胀 WCET) | 0.179 | L1 |
| GPIO 验证 WCRT (H573 测试夹具) | — | **pending** 2026 Q2 |

硬件: STM32F407 Cortex-M4F @ 168 MHz、ADS1299 8 通道 24 位 ADC、
ATECC608B 安全元件、nRF52840 BLE 5.3、ISO7741 5 kV 电气隔离。

## 本组织包含的仓库

| 仓库 | 用途 | 状态 |
|:---|:---|:---|
| [`axonos-kernels`](https://github.com/AxonOS-org/axonos-kernels) | **可验证的内核基础** — 七个 crate、66 个测试、28 个 Kani 证明 | 活跃 · Apache-2.0 OR MIT |
| [`axonos-rfcs`](https://github.com/AxonOS-org/axonos-rfcs) | 管理架构决策的工程 RFC | 6 个 RFC · CC-BY-SA-4.0 |
| [`axonos-sdk`](https://github.com/AxonOS-org/axonos-sdk) | 应用 SDK:类型化 intent、能力、认证 | Apache-2.0 OR MIT |
| [`axonos-consent`](https://github.com/AxonOS-org/axonos-consent) | AxonOS 同意协议参考实现 | Apache-2.0 OR MIT |
| [`axonos-swarm`](https://github.com/AxonOS-org/axonos-swarm) | 多节点协调:Neural PTP、群调度器、故障检测器 | Apache-2.0 OR MIT |
| [`axon-bci-gateway`](https://github.com/AxonOS-org/axon-bci-gateway) | 参考应用网关 (fork,带署名) | 活跃 · Apache-2.0 |

可复现的基准夹具与预印本 LaTeX 源码将与 2026 Q2 的 L3 验证结果
一并发布。

## 受众

本项目面向四类受众。如果您符合其中之一,请从指定位置开始。

### BCI 与神经信号处理研究人员

您需要一个不强加自身意见于您信号管道的实时底座,具有您可表征的
可预测时序,以及在原始采集与高层意图输出之间的清晰分离。

入门: [`axonos-rfcs`](https://github.com/AxonOS-org/axonos-rfcs) →
RFC-0001 (架构) 与 RFC-0004 (双核契约)。

### 嵌入式系统工程师

您需要一个将 `#![no_std]` `#![forbid(unsafe_code)]` Rust 应用于
Cortex-M 硬实时调度的可工作示例,并具有区分推导与测量的 WCET 声明。

入门: [`axonos-sdk`](https://github.com/AxonOS-org/axonos-sdk) →
`examples/bare_metal_no_std.rs` 中的示例。

### 医疗设备工程师与监管团队

您需要一个内核底座,其架构决策以版本化 RFC 形式记录,其性能声明带有
证据级别,且其路线图明确针对 IEC 62304 C 类对齐。

入门: [`axonos-rfcs`](https://github.com/AxonOS-org/axonos-rfcs) →
RFC-0005 (验证框架) 与 RFC-0006 (稳定 ABI 候选)。

### 临床团队与康复中心

您需要可预测、可审计的软件来运行您患者的闭环接口,需要一个将故障
模式视为一等公民文档(而非营销惊喜)的合作伙伴。

联系: [connect@axonos.org](mailto:connect@axonos.org) — 初次沟通、
临床先导路径、MOU 流程。

## 路线图

**2026 Q2 — 第一阶段:L3 验证**
- 使用 Saleae Logic Pro 16 在 STM32H573 夹具上进行 GPIO 仪器化
  WCRT 测量
- 参考板上的直接功耗测量
- 基于已验证 ABI,将 RFC-0006 从候选提升为稳定

**2026 Q3–Q4 — 第二阶段:临床先导**
- 首个 8 通道临床套件部署
- 在美国东北部合作 ALS 康复中心进行先导 (MOU 已签订)
- 与离线基准并列报告在线分类器性能

**2027 — 第三阶段:监管路径**
- FDA 预提交 (Q-Sub)
- 集成 Ferrocene 合格工具链
- ISO 14971 完整风险管理文件

**持续进行**
- 欢迎并鼓励独立复现测量方法
- 所有测量原始数据与 SHA-256 清单一同公开

## 工程原则

这些是项目所遵循的规则。它们不是愿景;它们是决策的方式。

1. **声明不得超越其证据级别。** 若我们在一块板上测量了 12 小时,
   我们说 "L2";不说 "已验证"。
2. **可审查模块中无 `unsafe`。** 硬件寄存器访问位于已审计的 PAC
   crate 内;其余全部为 `#![forbid(unsafe_code)]`。
3. **热路径上无堆分配。** 静态缓冲区,编译期定尺寸,大小适配 WCET
   预算。
4. **不沉默地从不一致状态恢复。** 中毒的互斥锁、时钟违规、协议失配
   都作为错误浮现,而非默认值。
5. **不通过内核实施专有锁定。** ABI 以 CC-BY-SA-4.0 作为 RFC 公开
   发布。欢迎第三方实现。

## 许可

- **源代码** (`axonos-sdk`, `axonos-consent`, `axonos-swarm`):
  Apache-2.0 OR MIT — 由您选择。
- **工程 RFC** (`axonos-rfcs`): CC-BY-SA-4.0。
- **参考应用网关** (`axon-bci-gateway`): Apache-2.0
  (按原许可保留上游署名)。

在上述条款下允许商业使用、修改与再分发。已接受的合并请求不要求
贡献者许可协议 (CLA);贡献者保留对其贡献的著作权。

## 联系方式

- **一般通信:** [info@axonos.org](mailto:info@axonos.org)
- **安全披露:** [security@axonos.org](mailto:security@axonos.org)
  (按需提供 GPG 密钥)
- **网站:** [axonos.org](https://axonos.org)
- **文章:** [medium.com/@AxonOS](https://medium.com/@AxonOS)

---

<div align="center">

**作者与维护者:** Denis Yermakou · [denis@axonos.org](mailto:denis@axonos.org)

Zurich · Berlin · Milano · San Mateo · Singapore

<sub>Made with 🦀</sub>

</div>
