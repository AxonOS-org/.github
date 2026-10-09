<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/AxonOS-org/.github/raw/main/profile/assets/hero-dark.svg">
  <img alt="AxonOS — ブレイン・コンピュータ・インターフェースのための決定論的インフラストラクチャ" src="https://github.com/AxonOS-org/.github/raw/main/profile/assets/hero-light.svg" width="100%">
</picture>

### ブレイン・コンピュータ・インターフェースのための決定論的インフラストラクチャ。

<sub>このページは[英語版ページ](./README.md)の要約です。英語版が正本であり、バージョン、リポジトリ、根拠はそちらに掲載しています。</sub>

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

## AxonOS とは

AxonOS は、ニューラル・ハードウェアとそれを使うアプリケーションの間にあるハード・リアルタイム層です。ARM Cortex-M 向けの `#![no_std]` Rust によるオープンソースのカーネルで、最悪応答時間を実行後に計測するのではなく実行前に解析できるよう設計されています。プライバシーは**アプリケーション層の下**で強制され、どのアプリケーションも迂回できません。

> アプリケーションが受け取るのは、型付けされ同意に拘束された意図イベントだけです。生のニューラル・ストリームは決して渡されません。

## 現時点で証明されていること

有界モデル検査器 Kani により、次の三つの性質がそれぞれ明示した範囲で証明されています（レベル **L1**）。

- スケジューラのアドミッションと Earliest-Deadline-First による選択
- 単一プロデューサ・単一コンシューマのリング：正確な往復、ループのない挿入、FIFO 順序
- 同意：検証済み署名のない状態遷移はなく、同じシーケンスは二度受理されず、撤回は最終的です

**現時点で時間に関する数値は一切主張していません。** 標準の 1 000 µs は要件であって結果ではありません。応答時間の証明も、リファレンス・ハードウェアでの公開済み測定もまだ存在しません。正式な状況は[クレーム・カタログ](https://github.com/AxonOS-org/axonos-standard/blob/main/CLAIMS.md)に記載しています。

## リポジトリ

すべてのリポジトリは公開されています。コードは Apache-2.0 OR MIT、仕様は CC-BY-SA-4.0 です。最新バージョンを含む全一覧は[英語版ページ](./README.md)と [github.com/AxonOS-org](https://github.com/AxonOS-org) にあります。

---

<div align="center">

© The AxonOS Project / Denis Yermakou

[connect@axonos.org](mailto:connect@axonos.org) · [security@axonos.org](mailto:security@axonos.org) · [LinkedIn](https://www.linkedin.com/in/axonos) · [axonos.org](https://axonos.org)

<sub>将来に向けて、オフィスと本社の設置を検討しています。</sub>

</div>
