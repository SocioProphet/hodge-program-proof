# Dependencies

## Upstream

| Repository | Commit SHA | Cited content |
|---|---|---|
| `SocioProphet/Heller-Godel` | `2ea5f5162bcc8421840df4b33a51580e2732f391` | Framework objects (`HG-*`) from `docs/framework-core/`; PFK operational substrate from `proof_fabric_kernel/` |

## Cited objects

### Framework-grade (HG-*)

| Identifier | Role | Notes |
|---|---|---|
| `HG-FND-*` | Foundational vocabulary | typing for boundary principle, distance classification, and anti-seed discipline |
| `HG-EX-001` | Catalan / mu2 fixture | applies to Catalan / mu2 fixture-grade comparison work |
| `HG-MTH-005` | Universal Bridge formal specification | parent / general bridge axiom; does not transfer proofs |
| `HG-MTH-006` | Universal Bridge: Hodge domain extension | canonical Hodge bridge spec; hodge-program-proof is the primary consumer |

### PFK operational substrate

| Identifier | Role | Hodge use |
|---|---|---|
| `PFK-OP-001` | Event ingestion family | future receipt emission |
| `PFK-OP-030` | Calibration operator family | numerical-baseline checks for local symbolic computations |
| `PFK-OP-040` | Catalan / mu2 fixture operator | fixture-grade Catalan / mu2 comparison work |
| `PFK-OP-050` | PrimeStatsProtocol family | future descriptive-grade empirical claims, if any |

### PFK schemas

| Identifier | Canonical path | Use |
|---|---|---|
| `PFK-SCHEMA-001` | `proof_fabric_kernel/schemas/claim_ledger_row.schema.json` | claim-ledger rows |
| `PFK-SCHEMA-002` | `proof_fabric_kernel/schemas/event_ir.schema.json` | Event-IR receipts |
| `PFK-SCHEMA-003` | `proof_fabric_kernel/schemas/proof_artifact.schema.json` | proof-step envelopes |
| `PFK-SCHEMA-004` | `proof_fabric_kernel/schemas/calibration_bundle.schema.json` | calibration bundles |

### PFK anti-seed

| Identifier | Failure mode |
|---|---|
| `A-PFK-OP-001` | operator invocation is not evidence |
| `A-PFK-SCHEMA-001` | schema validity is not content validity |
| `A-PFK-SCHEMA-002` | schema-version drift |
| `A-PFK-VAL-001` | validator green status is not audit completion |

### Framework anti-seed

| Identifier | Failure mode |
|---|---|
| `A-HG-MTH-001` | Universal Bridge does not transfer proofs |
| `A-HG-MTH-002` | Catalan / mu2 fixture is not Clay progress |
| `A-HG-MTH-003` | fixture-grade and theorem-grade citations must not be mixed |
| `A-HG-MTH-004` | Standard Conjectures cited diagnostically are not assumed |

## Citation form

```text
[HG-EX-001 @ 2ea5f5162bcc8421840df4b33a51580e2732f391]
[HG-MTH-005 @ 2ea5f5162bcc8421840df4b33a51580e2732f391]
[HG-MTH-006 @ 2ea5f5162bcc8421840df4b33a51580e2732f391]
[PFK-SCHEMA-001 @ 2ea5f5162bcc8421840df4b33a51580e2732f391]
[A-HG-MTH-004 @ 2ea5f5162bcc8421840df4b33a51580e2732f391]
[A-PFK-SCHEMA-001 @ 2ea5f5162bcc8421840df4b33a51580e2732f391]
```

## Forbidden edges

- `hodge-program-proof` -> any other Clay-program repo (no horizontal dependencies)
- `hodge-program-proof` -> Heller-Godel-other-than-pinned-commit (no floating references)
- `hodge-program-proof` -> automorphic / number-theoretic methodology from RH or NP programs except through `HG-MTH-005` and `HG-MTH-006` as method-grade analogy

## Scope discipline unchanged

The four-tier distance classification is preserved:

1. Core Hodge — Hodge conjecture, generalized Hodge, standard conjectures, algebraic cycles.
2. Hodge-arithmetic — Tate, Mumford-Tate, Beilinson, Bloch-Kato, periods, regulators.
3. Hodge-method — comparison isomorphisms, regulator maps, finite monodromy, Deligne cohomology.
4. Hodge-fallout — YM, BSD, RH/L-functions, Temporal Mechanics, Lawful Learning.

This dependency declaration does not claim Hodge progress, does not promote any artifact, and does not advance the M_phi proof-class moduli wall.

## Standard Conjectures discipline

`HG-MTH-006` references Standard Conjectures B and D diagnostically, not assumptively. This repository does not assume SC-B, SC-D, Bloch-Kato, or Bloch-Beilinson unless a future artifact explicitly declares that assumption as a theorem premise.

## Actual-state note

`README.md` previously advertised `schemas/claim-ledger.schema.json`, but that path is not present on current `main`. This migration therefore does not delete a schema file. Instead, CI guards against local canonical-PFK schema name shadowing and verifies that canonical Heller-Godel PFK schema paths resolve under `HELLER_GODEL_ROOT`.
