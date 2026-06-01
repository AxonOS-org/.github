# Security Policy

AxonOS is pre-clinical, open-source research software. It is **not** a medical
device and is not deployed clinically. Even so, security — and especially the
privacy of neural data and the integrity of consent — is core to why AxonOS
exists, and we take reports seriously.

## Reporting a vulnerability

**Please do not open a public issue for security problems.**

Email **security@axonos.org** with:

- a description of the issue and the affected repository/component,
- steps to reproduce (or a proof of concept),
- the impact you foresee, and
- any suggested remediation.

We will acknowledge your report as quickly as a small team can — typically within
a few days — and keep you updated as we investigate. Please allow reasonable time
for a fix before any public disclosure, and we will coordinate timing with you.

## What we especially want to hear about

Because AxonOS's threat model centres on cognition staying private and consent
being unbypassable, we are particularly interested in:

- any path that could expose **raw neural data** beyond the kernel boundary;
- **capability or consent bypass** (an app obtaining more than its manifest grants,
  or continuing after consent is revoked);
- weaknesses in the wire format, attestation, or isolation boundaries;
- timing or memory-safety issues in the `#![no_std]` real-time paths.

## Scope and rewards

This is an unfunded open-source project, so we cannot offer a paid bug bounty.
We will, however, credit reporters (with your permission) and are grateful for
responsible disclosure.

— The AxonOS Project · [axonos.org](https://axonos.org)
