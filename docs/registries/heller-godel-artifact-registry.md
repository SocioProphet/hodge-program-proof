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
| `docs/proofs/soule_voisin_ah_torsion_witness_artifact.md` | torsion-witness-shaped Mode-A artifact | `hodge-method` | workbench diagnostic / nonclaim | records torsion-witness-shaped `mu_2` data and missing projective/integral-Hodge structures | Do not treat as an Atiyah-Hirzebruch counterexample, integral Hodge class, or Hodge progress |
| `docs/proofs/kuga_satake_k3_technique_transfer_diagnostic.md` | Kuga-Satake / K3 Mode-C diagnostic | `hodge-method` | negative technique-transfer diagnostic / nonclaim | blocks false transfer from finite `mu_2` character to K3/Tate/Hodge-structure machinery | Do not treat as K3, Tate, abelian-variety, or Hodge-conjecture evidence |
| `docs/governance/major_problem_adjacency_taxonomy.md` | adjacency governance taxonomy | `hodge-method` | governance / nonclaim | distinguishes object-, methodology-, and outcome-adjacency for major-problem references | Do not treat methodology-adjacency or outcome-adjacency as mathematical evidence |
| `docs/proofs/proof_class_moduli_bottleneck_consolidation.md` | Mode-convergence consolidation | `hodge-method` | workbench consolidation / nonclaim | records `M_phi` as the central structural bottleneck inferred from Modes A/B/C | Do not treat bottleneck identification as construction of `M_phi` or Hodge progress |
| `docs/proofs/proof_class_moduli_requirements_scaffold.md` | proof-class moduli requirements scaffold | `hodge-method` | requirements / nonclaim | specifies what a future `M_phi` would need to support and defines failure modes for `HG-MODULI-002` | Do not treat requirements as construction, existence proof, joint satisfiability proof, or Hodge progress |
| `docs/proofs/proof_class_moduli_scaffold_diagnostic.md` | proof-class moduli scaffold diagnostic | `hodge-method` | diagnostic evaluation / nonclaim | evaluates current apparatus against `HG-MODULI-001`; sequences `HG-MODULI-002` toward proof-class objects, realization-equivalence, and analytic realization assignment | Do not treat partial support as construction, full support, existence proof, or Hodge progress |
| `docs/proofs/proof_class_moduli_construction_attempt.md` | proof-class moduli construction attempt | `hodge-method` | bounded construction proposal / partial construction / nonclaim | defines candidate proof-class analytic objects, layered realization-equivalence, and D1 analytic realization assignment; identifies parameter-object feasibility as next obstruction | Do not treat as full `M_phi` construction, existence proof, parameter-space construction, Hodge target extraction, or Hodge progress |
| `docs/proofs/proof_class_moduli_parameter_feasibility.md` | proof-class moduli parameter feasibility analysis | `hodge-method` | feasibility analysis / bounded negative finding / nonclaim | establishes that only weak discrete or stratified-discrete registry organization is currently feasible; recommends `HG-MODULI-004` stratified registry construction | Do not treat as parameter-object construction, analytic/algebraic/projective parameter-space support, universal-family support, or Hodge progress |
| `docs/review-ledgers/hg_session_2026_05_14_synthesis.md` | session synthesis ledger | `hodge-method` | provenance / historical record | maps Drive-side session artifacts to repo-grade successors and supersession decisions | Do not treat session history as theorem evidence or doctrine by itself |
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

## Proof-class moduli scaffold notes

The `HG-MODULI-001` requirements scaffold is repo-grade as a specification artifact. It is not a construction attempt. It records:

```text
requirements != construction
bottleneck identification != bottleneck resolution
candidate vocabulary != existence theorem
```

The scaffold explicitly does not prove that `M_phi` exists, that the listed requirements are satisfiable, or that the listed requirements are jointly satisfiable.

The scaffold diagnostic records the current support state:

```text
partial support: 7 requirements
no support: 6 requirements
full support: 0 requirements
contradicted: 0 requirements
overconstrained: 0 requirements
```

The diagnostic recommends that `HG-MODULI-002` begin with:

```text
proof-class objects
realization-equivalence relation
D1 analytic realization assignment
```

The diagnostic explicitly does not construct `M_phi`, prove `M_phi` exists, or promote partial support to full support.

`HG-MODULI-002` partially constructs that starting wedge by defining:

```text
proof-class analytic objects
finite-output / analytic-germ / regulator-seed equivalence layers
D1 analytic realization assignment on decorated objects
```

It does not construct a full `M_phi`, a parameter object, Hodge target data, algebraic cycles, cycle equality, or a Deligne-to-Hodge bridge. Its next identified obstruction is:

```text
parameter-object feasibility for proof-class analytic objects
```

`HG-MODULI-003` analyzes that obstruction and concludes:

```text
weak discrete registry: feasible
stratified discrete registry: feasible and recommended
complex analytic parameter object: unsupported
algebraic parameter object: unsupported
smooth complex projective parameter object: unsupported
universal family / descent object: unsupported
```

It recommends `HG-MODULI-004` as a stratified registry construction and explicitly blocks promotion from weak registry organization to analytic, algebraic, projective, or universal-family structure.

## Drive migration artifact notes

The 2026-05-14 Drive migration is closed on the Heller-Godel side. The following repo-grade artifacts now supersede or consolidate the Drive-side materials:

```text
Mode-A: docs/proofs/soule_voisin_ah_torsion_witness_artifact.md
Mode-B: docs/proofs/beilinson_regulator_catalan_motzkin_artifact.md
Mode-C: docs/proofs/kuga_satake_k3_technique_transfer_diagnostic.md
Taxonomy: docs/governance/major_problem_adjacency_taxonomy.md
Consolidation: docs/proofs/proof_class_moduli_bottleneck_consolidation.md
Session ledger: docs/review-ledgers/hg_session_2026_05_14_synthesis.md
```

The initial Drive-side ranking `HG_MPR_001_v0_1_major_problem_ranking.md` is intentionally not repo-graded because it was superseded by the revised ranking captured in the adjacency taxonomy and session ledger.

The newly registered Drive migration artifacts fall under these obstruction-registry entries:

| Artifact | Obstruction-registry scope |
| --- | --- |
| Mode-A torsion witness | `OBS-HODGE-001`, `OBS-HODGE-008` |
| Mode-C Kuga-Satake diagnostic | `OBS-HODGE-005`, `OBS-HODGE-008` |
| Major-problem adjacency taxonomy | `OBS-HODGE-006`, `OBS-HODGE-008`; methodology-adjacency safeguards |
| Proof-class moduli bottleneck consolidation | `OBS-HODGE-002`, `OBS-HODGE-004`, `OBS-HODGE-005`, `OBS-HODGE-007`, `OBS-HODGE-008` |
| Session synthesis ledger | provenance only; no theorem or obstruction-removal claim |

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
full proof-class moduli M_phi construction
analytic, algebraic, or projective parameter object for proof-class analytic objects
universal family or descent object
```

## Registry nonclaims

This registry does not claim:

1. Heller-Godel proves or advances the Hodge conjecture;
2. Deligne-unit data are algebraic cycles;
3. finite monodromy is Tate data;
4. comparison diagrams are motives;
5. regulator symbols are Beilinson evidence;
6. proof-fabric validation is mathematical proof;
7. p = 3 scaffolding is an odd-prime theorem;
8. proof-class moduli `M_phi` exists;
9. Drive-side reasoning is repo-grade except where consolidated by repo artifacts;
10. requirements scaffolding proves construction, existence, or joint satisfiability;
11. scaffold diagnostics prove construction, full support, existence, or Hodge progress;
12. bounded construction proposals prove full moduli construction, parameter-space existence, or Hodge progress;
13. feasibility analysis proves parameter-object construction, projectivity, universal-family existence, or Hodge progress.

## Known process risk

Substantive Heller-Godel workbench PRs can create a registry-staleness window in this Hodge Program registry. The window should be closed by a registry-update PR within the same review batch as the workbench PRs that created it.

The first structural checker should focus on internal consistency of the Hodge Program repository. Cross-repo staleness detection remains a manual-discipline item until a cross-repo-aware checker is designed.

## Update rule

When Heller-Godel merges a new theorem-facing or proof-fabric PR, this registry should be updated only if the artifact changes one of:

1. Hodge distance classification;
2. evidence level;
3. missing Hodge-core structures;
4. Clay-facing target/gap posture;
5. source-packet or provenance surface.

Routine typo, formatting, or CI-only changes do not need registry updates unless they affect claim-boundary enforcement.
