# hodge-program-proof ↔ HG-MTH-006 Citation Anchor

The hodge-program-proof operates as the primary consumer of `[HG-MTH-006 @ 2ea5f5162bcc8421840df4b33a51580e2732f391]`, the Universal Bridge specification for the Hodge domain.

## How the hodge-program-proof apparatus sits under the bridge

`HG-MTH-006` specifies the Hodge bridge factorization:

```text
B_Hodge(X, p) = (M_Hodge, R_Hodge, A_Hodge)
```

with `X` a smooth projective complex variety and `p >= 0`:

- `M_Hodge(X, p) = H^{p,p}(X, Q)` — rational `(p,p)` classes;
- `R_Hodge(X, p) = coker(cl^p : CH^p(X)_Q -> H^{2p}(X, Q))` — cokernel of the cycle class map;
- `A_Hodge` — structural obstruction package around Standard Conjectures B/D, regulator interface, Bloch-Beilinson, and Bloch-Kato apparatus.

The Hodge conjecture is the assertion that `R_Hodge(X, p) = 0` for all `X` and `p`. This repo does not claim that assertion.

## Per-tier bridge positioning

| hodge-program-proof tier | Role under HG-MTH-006 |
|---|---|
| Core Hodge | Direct `R_Hodge = 0` claim space; not entered by this repo's current non-claim posture |
| Hodge-arithmetic | Tate, Mumford-Tate, Beilinson, Bloch-Kato; apex-layer structural vocabulary |
| Hodge-method | M_phi proof-class moduli wall; methodology for organizing attempts at apex-tool construction |
| Hodge-fallout | YM, BSD, RH/L-functions; adjacent programs with no proof transfer |

## Specific apparatus positioning

| Object | Distance tier | Role under HG-MTH-006 |
|---|---|---|
| M_phi proof-class moduli wall | Hodge-method | Methodology for typing proof-class moduli; not an apex-tool by itself |
| HG-AH-001 tame-symbol fixture | Hodge-method / fixture | Fixture-grade; does not advance `R_Hodge` |
| HG-BR-001 Beilinson-regulator fixture | Hodge-method / fixture | Fixture-grade apparatus validation; regulator vocabulary is apex-adjacent but the fixture is not Hodge progress |
| Four-tier distance classification | Hodge-method | Organizing principle; not Hodge progress |
| anti-seed-hodge.md | Hodge-method | Failure-mode register; compatible with framework anti-seed |

## Standard Conjectures: diagnostic, not assumptive

Per `[A-HG-MTH-004 @ 2ea5f5162bcc8421840df4b33a51580e2732f391]`, `HG-MTH-006` references Grothendieck Standard Conjectures B and D diagnostically, not as assumptions.

This repository does not assume:

- Standard Conjecture B;
- Standard Conjecture D;
- Bloch-Kato;
- Bloch-Beilinson.

Any future artifact requiring one of those as a theorem premise must declare the assumption explicitly.

## Shared missing machinery

`HG-MTH-006` diagnoses shared missing machinery with classical RH: a Lefschetz-style positivity and algebraicity mechanism at the level of algebraic cycles in characteristic zero or mixed characteristic.

Construction of such machinery for the Hodge domain would not construct it for RH, and vice versa.

## Boundary preservation

Per `[A-HG-MTH-001 @ 2ea5f5162bcc8421840df4b33a51580e2732f391]`, Universal Bridge citation does not transfer proof.

Per `[A-HG-MTH-002 @ 2ea5f5162bcc8421840df4b33a51580e2732f391]`, Catalan / mu2 fixture work is not Clay progress.

Per `[A-HG-MTH-003 @ 2ea5f5162bcc8421840df4b33a51580e2732f391]`, fixture-grade and theorem-grade citations must not be mixed.

Per `[A-HG-MTH-004 @ 2ea5f5162bcc8421840df4b33a51580e2732f391]`, Standard Conjectures are cited diagnostically, not assumed.

## Citation form

```text
[HG-MTH-006 @ 2ea5f5162bcc8421840df4b33a51580e2732f391]
[A-HG-MTH-004 @ 2ea5f5162bcc8421840df4b33a51580e2732f391]
```

All Heller-Godel citations in this repo pin to the same SHA unless a later migration PR advances the pin.
