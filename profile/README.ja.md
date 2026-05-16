<div align="center">

<img src="https://rustacean.net/assets/rustacean-flat-happy.svg" width="120" alt="Ferris" />

# AxonOS

### ブレイン・コンピュータ・インターフェース向けリアルタイム Rust マイクロカーネル

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


## 概要

AxonOS は、Cortex-M クラスのマイクロコントローラ上でブレイン・コンピュータ・
インターフェース (BCI) の信号パイプラインを動作させる、
`#![no_std]` `#![forbid(unsafe_code)]` の Rust マイクロカーネルです。

設計対象は明確です。神経信号を取得し、ユーザの意図を分類し、固定された
リアルタイム予算の中で刺激装置や支援インターフェースを閉ループ駆動する、
小型・自律型のデバイス。シリコンと患者の間に汎用 OS を介在させません。

このようなシステムでは、デッドラインの逸脱はパフォーマンス劣化ではなく
有害事象です。

## 存在意義

現在のリアルタイム BCI ソフトウェアは、いずれも問題と構造的に
不適合な 3 つの基盤の上に構築されています。

1. **汎用カーネル** (Linux, Windows) — 公平性とスループットのために
   設計されており、最悪ケース遅延の有界性は目標ではありません。
   メインライン Linux のスケジューラ・ジッタはミリ秒オーダー、
   PREEMPT_RT で削減できますが除去はできません。

2. **従来型 RTOS** (FreeRTOS, Zephyr) — 優先度ベースのリアルタイム
   スケジューリングは提供しますが、形式的なスケジュラビリティ証明、
   言語レベルのメモリ安全性保証、BCI 領域の抽象化はいずれも
   ありません。

3. **アプリケーションプロセッサ上の汎用 OS** — 汎用 OS の
   攻撃対象範囲と予測不能性を、規制対象の医療機器に持ち込みます。

AxonOS はこのギャップを埋めます。解析的にスケジュール可能な小型カーネル、
コンパイル時にメモリ安全性違反を排除する言語、そしてアプリケーション
コードへの生神経データの到達を防ぐ Capability モデル。

## 何が異なるのか

| 特性 | AxonOS | 主流 RTOS | Linux PREEMPT_RT |
|:---|:---|:---|:---|
| スケジューリング方式 | EDF (Liu–Layland) | 固定優先度 | CFS + RT |
| 解析的スケジュラビリティ証明 | あり | なし | なし |
| コンパイル時メモリ安全性 | あり (Rust) | なし (C) | なし (C) |
| `unsafe` フリーのカーネルロジック | あり | なし | なし |
| ホットパス上のヒープ確保 | なし | 任意 | デフォルト |
| BCI Capability 隔離 | あり | なし | なし |
| エビデンスレベル付き WCET 表明 | あり (L1/L2) | なし | なし |

**重要な誠実性開示。** AxonOS は seL4 の意味での形式検証は
**主張しません**。解析的リアルタイム・スケジューリング理論
(Liu–Layland) を、Rust の型システムおよび測定に裏付けられた検証
タクソノミーと組み合わせて使用します。機械検証された機能正当性証明
よりは弱いですが、今日達成可能であり、IEC 62304 クラス C ソフトウェア
ライフサイクル要件と整合します。

## エビデンスモデル

AxonOS のドキュメント中のあらゆる性能主張には、エビデンス
レベルが付されます。

- **L1** — 命令カウント由来。コンパイル済みアセンブリを
  対象 ISA のサイクル時間リファレンスに対して算出。
  保守的、ハードウェア実行は不要。
- **L2** — ランタイム測定。指定された期間および入力分布下で、
  リファレンスハードウェア上の DWT サイクルカウンタ等の
  オンチップ計器により観測。
- **L3** — 独立オシロスコープ検証。DUT から独立した
  ロジックアナライザ等の計器 (GPIO トグルポイント) により観測。
  規制申請に必須。
- **pending** — 測定未実施。目標日を明記。

現時点の主要な数値:

| 計測項目 | 値 | レベル |
|:---|:---|:---|
| パイプライン WCET、1 エポック | 640.2 µs | L1 |
| CPU 使用率 U′ (インフレ後 WCET) | 0.179 | L1 |
| GPIO 検証 WCRT (H573 固定装置) | — | **pending** 2026 Q2 |

ハードウェア: STM32F407 Cortex-M4F @ 168 MHz、ADS1299 8 チャネル 24 ビット
ADC、ATECC608B セキュアエレメント、nRF52840 BLE 5.3、ISO7741 5 kV
ガルバニック絶縁。

## 組織内のリポジトリ

| リポジトリ | 目的 | ステータス |
|:---|:---|:---|
| [`axonos-kernels`](https://github.com/AxonOS-org/axonos-kernels) | **検証可能なカーネル基盤** — 7 crate、66 テスト、28 Kani 証明 | アクティブ · Apache-2.0 OR MIT |
| [`axonos-rfcs`](https://github.com/AxonOS-org/axonos-rfcs) | アーキテクチャ決定を司るエンジニアリング RFC | 6 RFCs · CC-BY-SA-4.0 |
| [`axonos-sdk`](https://github.com/AxonOS-org/axonos-sdk) | アプリケーション SDK: 型付きインテント、Capability、認証 | Apache-2.0 OR MIT |
| [`axonos-consent`](https://github.com/AxonOS-org/axonos-consent) | AxonOS 同意プロトコル参照実装 | Apache-2.0 OR MIT |
| [`axonos-swarm`](https://github.com/AxonOS-org/axonos-swarm) | マルチノード協調: Neural PTP、スウォームスケジューラ、フォルト検出 | Apache-2.0 OR MIT |
| [`axon-bci-gateway`](https://github.com/AxonOS-org/axon-bci-gateway) | リファレンスアプリケーションゲートウェイ (フォーク、帰属表示付き) | Active · Apache-2.0 |

再現可能なベンチマーク固定装置およびプレプリント LaTeX ソースは、
2026 Q2 の L3 検証結果と併せて公開予定です。

## 対象読者

このプロジェクトは 4 つの読者層を想定しています。以下のいずれかに
該当する方は、指定の場所から始めてください。

### BCI および神経信号処理の研究者

予測可能な、特性評価可能なタイミングと、生取得から高水準意図出力までの
明確な分離を備え、信号パイプラインに独自の意見を押し付けない
リアルタイム基盤が必要な方。

開始点: [`axonos-rfcs`](https://github.com/AxonOS-org/axonos-rfcs) →
RFC-0001 (アーキテクチャ)、RFC-0004 (デュアルコア契約)。

### 組込みシステムエンジニア

Cortex-M 上のハードリアルタイム・スケジューリングに `#![no_std]`
`#![forbid(unsafe_code)]` の Rust を適用した動作する例、および
導出と測定を区別した WCET 値の表明が必要な方。

開始点: [`axonos-sdk`](https://github.com/AxonOS-org/axonos-sdk) →
`examples/bare_metal_no_std.rs`。

### 医療機器エンジニアおよび規制チーム

アーキテクチャ決定がバージョン管理された RFC として文書化され、
性能主張にエビデンスレベルが付与され、ロードマップに IEC 62304
クラス C 整合性が明示的に含まれるカーネル基盤が必要な方。

開始点: [`axonos-rfcs`](https://github.com/AxonOS-org/axonos-rfcs) →
RFC-0005 (検証フレームワーク)、RFC-0006 (安定 ABI 候補)。

### 臨床チームおよびリハビリテーションセンター

患者向けの閉ループ・インターフェースを実行する、予測可能かつ監査可能な
ソフトウェア、および障害モードをマーケティング上のサプライズではなく
第一級のドキュメントとして扱うパートナーが必要な方。

連絡先: [connect@axonos.org](mailto:connect@axonos.org) — 初回相談、
臨床パイロット経路、MOU プロセス。

## ロードマップ

**2026 Q2 — フェーズ 1: L3 検証**
- Saleae Logic Pro 16 による STM32H573 固定装置上の GPIO 計装 WCRT 測定
- リファレンスボード上の直接消費電力測定
- 検証された ABI に基づき RFC-0006 を候補から安定版へ昇格

**2026 Q3–Q4 — フェーズ 2: 臨床パイロット**
- 最初の 8 チャネル臨床キット展開
- 提携 ALS リハビリテーションセンター (米国北東部、MOU 締結済) でのパイロット
- オフラインベンチマークと併せたオンライン分類性能の報告

**2027 — フェーズ 3: 規制経路**
- FDA Pre-Submission (Q-Sub)
- Ferrocene 認定済みツールチェイン統合
- ISO 14971 完全リスクマネジメントファイル

**継続的**
- 測定方法論の独立再現を歓迎
- SHA-256 マニフェスト付きですべての測定生データを公開

## エンジニアリング原則

このプロジェクトが従う規則です。理想ではなく、意思決定の方法です。

1. **エビデンスレベルを超えた主張をしない。** 1 ボード 12 時間で
   測定したのであれば「L2」と表記し、「検証済み」とは言わない。
2. **レビュー可能なモジュールに `unsafe` を入れない。**
   ハードウェアレジスタアクセスは監査済み PAC クレートに局所化、
   他は `#![forbid(unsafe_code)]`。
3. **ホットパスでヒープ確保しない。** WCET 予算に収まる静的バッファを
   コンパイル時にサイジング。
4. **不整合状態からの暗黙の復旧をしない。** 汚染ミューテックス、
   時計違反、プロトコル不一致はデフォルト値ではなくエラーとして
   表面化させる。
5. **カーネルによるプロプライエタリ・ロックインを設けない。**
   ABI は CC-BY-SA-4.0 で RFC として公開。第三者実装を歓迎。

## ライセンス

- **ソースコード** (`axonos-sdk`, `axonos-consent`, `axonos-swarm`):
  Apache-2.0 OR MIT — お選びください。
- **エンジニアリング RFC** (`axonos-rfcs`): CC-BY-SA-4.0。
- **リファレンスアプリケーションゲートウェイ** (`axon-bci-gateway`):
  Apache-2.0 (原ライセンスに従い上流帰属を保持)。

商用利用、改変、再配布はこれらの条件下で許可されます。受理されたプル
リクエストに対する CLA は要求しません。寄稿者は寄稿物の著作権を保持
します。

## 連絡先

- **一般通信:** [info@axonos.org](mailto:info@axonos.org)
- **セキュリティ開示:** [security@axonos.org](mailto:security@axonos.org)
  (GPG 鍵は要請次第)
- **ウェブ:** [axonos.org](https://axonos.org)
- **執筆:** [medium.com/@AxonOS](https://medium.com/@AxonOS)

---

<div align="center">

**著者およびメンテナ:** Denis Yermakou · [denis@axonos.org](mailto:denis@axonos.org)

Zurich · Berlin · Milano · San Mateo · Singapore

<sub>Made with 🦀</sub>

</div>
