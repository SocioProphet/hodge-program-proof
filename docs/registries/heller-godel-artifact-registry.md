# Heller-Godel Artifact Registry

Status: Hodge Program artifact registry.  
Classification default: `hodge-method` unless otherwise noted.  
Date: 2026-05-15.  
Source repo: `SocioProphet/Heller-Godel`.

## Purpose

This registry records Heller-Godel artifacts that should be tracked by the Hodge Program Proof repository as proof fabric, source packets, obstruction controls, or Hodge-method objects.

The registry does not import theorem claims into the Hodge core. It classifies distance and preserves the anti-seed boundary.

## Intake rule

Each registry entry must record:

1. source repository path;
2. artifact type;
3. Hodge Program classification;
4. evidence level;
5. safe use;
6. forbidden promotion.

## Artifact registry

| Source path in Heller-Godel | Artifact type | Classification | Evidence level | Safe use | Forbidden promotion |
| --- | --- | --- | --- | --- | --- |
| `docs/manuscripts/paper_i_deligne_cohomological_phase_characters.md` | D1 manuscript | `hodge-method` | theorem / conjecture / nonclaim mix internal to HG | Deligne-adjacent finite-character proof surface | Do not treat as Hodge proof or algebraic-cycle construction |
| `docs/appendices/appendix_a_chain_catalan_witness.md` | witness appendix | `hodge-method` | theorem / proposition support inside HG | finite witness and Catalan A1 fixture trace | Do not treat finite `mu_2` output as algebraicity |
| `docs/proofs/catalan_a1_realization_equivalence.md` | theorem-support vocabulary | `hodge-method` | definition / support | realization-equivalence vocabulary for finite output | Do not promote to proof-class moduli or Hodge realization independence |
| `docs/proofs/hodge_clay_target_gap_ledger.md` | Clay-facing gap ledger | `core-hodge` as target ledger; no proof claim | program-goal / nonclaim | maps missing Hodge objects | Do not treat ledger as construction of `X`, `alpha`, or cycles |
| `docs/proofs/beilinson_regulator_catalan_motzkin_artifact.md` | local regulator-symbol artifact | `hodge-method` | workbench computation / nonclaim | repo-grade input for `HODGE-EVAL-001`; local Catalan and Motzkin regulator-symbol values | Do not treat as Beilinson conjecture evidence, Hodge target datum, algebraic cycle, or regulator-conjecture closure |
| `docs/proofs/p3_source_inventory.md` | p = 3 inventory | `hodge-method` | observation / nonclaim | records absence of p = 3 support surface | Do not treat as odd-prime theorem |
| `docs/source-captures/eisenstein_mu3_capture.md` | source capture | `hodge-method` | source support | supports `mu_3` vocabulary | Do not treat as p = 3 fixture or `A_2` realization |
| `docs/proofs/p3_vocabulary_scaffold.md` | vocabulary scaffold | `hodge-method` | definition / scaffold | defines p = 3 primitives | Do not treat as closed p = 3 comparison |
| `docs/proofs/p3_source3_candidate_inventory.md` | candidate inventory | `hodge-method` | observation / review criteria | selection criteria for future `Source_3` work | Do not treat as candidate selection |
| `docs/review-ledgers/D1_RECONCILIATION_LEDGER.md` | reconciliation ledger | `hodge-method` | provenance | records D1 source reconciliation | Do not treat as theorem evidence by itself |
| `docs/governance/heller-godel-readiness-2026-05-14.md` | governance readiness summary | `hodge-method` | governance / validation | summarizes gate state | Do not treat validation as mathematical proof |

## Beilinson regulator artifact precision notes

The Beilinson regulator artifact is repo-grade for Hodge Program evaluation, but not theorem-grade. It carries two explicit precision caveats in the Heller-Godel source artifact:

1. regulator normalization: sign and factors depend on the chosen Deligne / regulator normalization and require convention verification before theorem-grade use;
2. Motzkin auxiliary unit: the value `h(0) = 3/2` is carried from the Drive-side Mode-B computation and should be re-derived before theorem-grade use.

These caveats do not block `HODGE-EVAL-001`; they prevent promotion beyond `hodge-method` classification.

The artifact falls under the following obstruction-registry entries:

```text
OBS-HODGE-004  Deligne cohomology to algebraicity promotion risk
OBS-HODGE-007  Regulator symbol to regulator conjecture promotion risk
OBS-HODGE-008  Hodge-origin to Hodge-proof promotion risk
```

## Current Heller-Godel theorem-state summary

The closed Heller-Godel results are:

```text
Theorem 6.1: analytic-topological mu_2 comparison
Proposition A.1: chain null finite-character witness
Proposition A.2: Catalan finite analytic witness
Proposition A.3: Klein-bottle mu_2 local-system witness
Theorem A.4: A1 spin-gate witness, convention A1-sauzin-normalization-v1
Theorem A.7: Catalan A1 encoding closure, convention A1-sauzin-normalization-v1
Theorem A.8: Catalan A1 mu_2 realization independence, output only
Corollary 6.2.C: Catalan A1 closed instance of Theorem 6.2
```

Hodge Program interpretation: these are finite-character, local-system, Deligne-adjacent, and proof-fabric results. They are not Hodge conjecture results.

## Missing Hodge-core structures

The registry confirms the following remain absent from Heller-Godel:

```text
smooth complex projective variety X
rational Hodge class alpha
codimension-k algebraic cycles Z_i
cycle-class equality alpha = sum_i q_i[Z_i]
Deligne-to-Hodge bridge theorem
motivic realization framework
Tate / Beilinson / Bloch-Kato arithmetic theorem
```

## Registry nonclaims

This registry does not claim:

1. Heller-Godel proves or advances the Hodge conjecture;
2. Deligne-unit data are algebraic cycles;
3. finite monodromy is Tate data;
4. comparison diagrams are motives;
5. regulator symbols are Beilinson evidence;
6. proof-fabric validation is mathematical proof;
7. p = 3 scaffolding is an odd-prime theorem.

## Update rule

When Heller-Godel merges a new theorem-facing or proof-fabric PR, this registry should be updated only if the artifact changes one of:

1. Hodge distance classification;
2. evidence level;
3. missing Hodge-core structures;
4. Clay-facing target/gap posture;
5. source-packet or provenance surface.

Routine typo, formatting, or CI-only changes do not need registry updates unless they affect claim-boundary enforcement.
