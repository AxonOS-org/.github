# Contributing to AxonOS

AxonOS is an open-source, real-time operating system for brain–computer
interfaces — built in the open, carefully, with the receipts attached. It is
early and it is real. Contributions of every size are welcome, from a typo fix
to a kernel proof.

This guide applies across the whole project (every repository in
[github.com/AxonOS-org](https://github.com/AxonOS-org)).

## The project at a glance

| Repository | Role |
|:-----------|:-----|
| `axonos-standard` | Normative architecture and specifications |
| `axonos-rfcs` | Design-change process (propose changes here first) |
| `axonos-kernel` | Hard real-time microkernel (`#![no_std]` Rust) |
| `axonos-sdk` / `axonos-sdk-python` | Application boundary: typed intents, capability manifests, wire format |
| `axonos-consent` | Consent / co-authorisation enforcement |
| `axonos-swarm` | Long-horizon distributed timing |
| `axon-bci-gateway` | Acquisition bridge |
| `become-the-brain-os` | The community front door — an educational game |

## Start here (a few minutes)

- **Run something real, with zero setup** — the Python SDK is dependency-free:
  ```bash
  git clone https://github.com/AxonOS-org/axonos-sdk-python
  cd axonos-sdk-python && python examples/demo.py
  ```
  It builds real intent records, proves the 32-byte wire round-trip, and runs the
  capability gate (including rejecting raw-data access).
- **Feel the ideas** — play [Become the Brain OS](https://github.com/AxonOS-org/become-the-brain-os).
- **Read the design** — start with `axonos-standard`, then browse `axonos-rfcs`.

## Where help is genuinely needed

Honest, concrete places to start:

- **Docs & clarity** — typos, unclear READMEs, missing examples. Always welcome, always a good first PR.
- **Python SDK** — more examples and tests in `axonos-sdk-python`.
- **The game** — balance, accessibility, and bug reports for `become-the-brain-os`.
- **RFC feedback** — read an open RFC and comment; design review is contribution.
- **Validation** — reproducible traces and harnesses in `axonos-validation`.
- **Hardware** — *the biggest need.* AxonOS's timing guarantees are currently
  established analytically; we want them measured on real Cortex-M / BCI hardware.
  If you have a relevant devkit or lab, please open an issue or email us — this is
  the contribution that moves the project furthest.

## The bar

- **Tests pass.** Don't gate work on a full hardware build; gate on the tests and
  checks a repository actually runs in CI.
- **Small, focused PRs** with a clear description beat large ones.
- **Conventional commit** messages where you can (`fix:`, `feat:`, `docs:`…).
- By contributing you agree your work is licensed under the repository's terms —
  **Apache-2.0 OR MIT** for code, **CC-BY-SA-4.0** for specifications.

## The one rule that matters most

AxonOS's credibility is its entire moat. So:

- **Never present an unmeasured number as measured.** Mark results as *analytical*
  vs *measured*. If you ran it on hardware, say which hardware.
- **Cite third-party data**; never fold someone else's results into AxonOS's own.
- When in doubt, claim less. Honest "not yet measured" is always acceptable;
  inflated certainty is not.

## How to contribute

1. Fork the relevant repository and create a branch.
2. Make your change; run the repository's tests/checks locally.
3. Open a pull request describing **what** changed and **why**.
4. For anything that changes the architecture or a public interface, open an
   **RFC** in `axonos-rfcs` first so the design can be discussed.

## Contact

General: **connect@axonos.org** · Security (do **not** open a public issue):
see [`SECURITY.md`](SECURITY.md) → **security@axonos.org**

Thank you for helping build the layer that decides whether brain–computer
interfaces are fast, safe, and private.

— The AxonOS Project · [axonos.org](https://axonos.org)
