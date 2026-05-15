# Hodge Program Map

Status: program topology map.  
Claim level: orientation / registry synthesis; no theorem claim.  
Date: 2026-05-15.  
Depends on:

```text
README.md
docs/anti-seed-hodge.md
docs/claim-boundary.md
docs/hodge-origin-registry.md
docs/obstruction-registry.md
docs/intake/heller-godel-proof-fabric-intake.md
docs/registries/heller-godel-artifact-registry.md
docs/scaffolds/hodge_bridge_requirements_scaffold.md
```

## Purpose

This map explains how the current Hodge Program Proof repository pieces fit together.

It maps the repository's scaffold, registry, intake, obstruction, and bridge-requirement layers. It does not create a theorem, claim progress on the Hodge conjecture, or assert that any registered artifact supplies algebraic cycles.

The controlling doctrine remains:

```text
anti-seed first
preserve Hodge origin
classify distance
prevent unsafe promotion
```

## Repository layers

| Layer | Primary document(s) | Role | Claim level |
| --- | --- | --- | --- |
| Charter | `README.md` | Defines repository purpose, status, boundary principle, and initial structure | program-goal / non-claim |
| Negative control | `docs/anti-seed-hodge.md` | Records false formulations, unsafe promotions, and category mistakes before positive work | obstruction / non-claim |
| Claim boundary | `docs/claim-boundary.md` | Defines allowed labels and forbidden promotions | definition / non-claim |
| Origin registry | `docs/hodge-origin-registry.md` | Classifies Hodge-origin material by distance from the Hodge core | registry / classification |
| Obstruction registry | `docs/obstruction-registry.md` | Converts anti-seed risks into structured obstruction entries and hodge-fallout diagnostics | registry / diagnostic |
| External workbench intake | `docs/intake/heller-godel-proof-fabric-intake.md` | Classifies Heller-Godel proof fabric as Hodge-method material | intake / non-claim |
| External artifact registry | `docs/registries/heller-godel-artifact-registry.md` | Tracks Heller-Godel artifacts and forbidden promotions | registry / non-claim |
| Bridge requirements | `docs/scaffolds/hodge_bridge_requirements_scaffold.md` | Defines the four requirements for any future Deligne-to-Hodge bridge attempt | scaffold / definition |

## Dependency graph

```text
README.md
  -> docs/anti-seed-hodge.md
  -> docs/claim-boundary.md
  -> docs/hodge-origin-registry.md
      -> docs/obstruction-registry.md
      -> docs/intake/heller-godel-proof-fabric-intake.md
      -> docs/registries/heller-godel-artifact-registry.md
      -> docs/scaffolds/hodge_bridge_requirements_scaffold.md
  -> docs/program-map.md
```

Operational reading:

1. The README states the repository status and distance-classification model.
2. The anti-seed records what must not be promoted.
3. The claim boundary states which labels are allowed and what promotions are forbidden.
4. The Hodge Origin Registry classifies current artifacts by distance from the Hodge core.
5. The obstruction registry translates anti-seed risks into reviewable obstruction entries and downgrade rules.
6. The Heller-Godel intake and artifact registry handle the current external proof-workbench stream.
7. The bridge requirements scaffold defines what would be required before method artifacts could even be evaluated for Hodge-facing promotion.
8. This program map orients readers and future agents across the whole structure.

## Distance lanes

The active distance lanes are:

```text
core-hodge
hodge-arithmetic
hodge-method
hodge-fallout
```

Current repository state:

| Lane | Current contents | Interpretation |
| --- | --- | --- |
| `core-hodge` | README charter, anti-seed, claim-boundary, Hodge-origin registry, obstruction registry as boundary/control layer | Program structure only; no theorem claim |
| `hodge-arithmetic` | No active theorem artifact | Empty as theorem lane |
| `hodge-method` | Heller-Godel intake, Heller-Godel artifact registry, Hodge bridge scaffold | Method and proof-fabric layer only |
| `hodge-fallout` | YM analogue entries in `docs/obstruction-registry.md` | Diagnostic fallout only; no Hodge or Clay theorem claim |

The fact that an artifact is Hodge-originated does not imply it belongs to `core-hodge` as a theorem.

## Current positive structure

The current positive structure is administrative and methodological:

1. a claim-safe charter;
2. a controlling anti-seed;
3. a claim-boundary doctrine;
4. a Hodge-origin registry;
5. an obstruction registry;
6. a Heller-Godel intake;
7. a Heller-Godel artifact registry;
8. a Hodge bridge requirements scaffold;
9. this program map.

This is a proof-fabric infrastructure layer, not a proof layer.

## Current missing Hodge-core structures

The repository does not yet contain:

```text
validated core Hodge theorem artifact
smooth complex projective variety construction
rational Hodge class construction
algebraic-cycle construction
cycle-class equality proof
Deligne-to-Hodge bridge theorem
obstruction-removal theorem
```

These absences are not defects in the scaffold. They are the reason the scaffold exists.

## Heller-Godel integration point

Heller-Godel enters the Hodge Program through:

```text
docs/intake/heller-godel-proof-fabric-intake.md
docs/registries/heller-godel-artifact-registry.md
```

The current classification is:

```text
hodge-method
```

Heller-Godel is not currently classified as:

```text
core-hodge
hodge-arithmetic
Hodge proof
Hodge progress
```

The controlling anti-seed for the Heller-Godel stream is:

```text
Finite phase characters, Deligne units, or Catalan A1 comparison diagrams must not be promoted into Hodge proof/progress.
```

## Bridge-evaluation path

The only currently authorized route from method artifact to Hodge-facing evaluation is the bridge scaffold:

```text
docs/scaffolds/hodge_bridge_requirements_scaffold.md
```

That scaffold defines four requirements:

```text
Hodge target datum
Cycle realization datum
Cycle equality obligation
Deligne-to-Hodge bridge obligation
```

A future positive bridge evaluation must supply or explicitly fail against those requirements. It is valid for a bridge evaluation to conclude:

```text
No valid Hodge target datum currently follows.
```

## Anti-promotion rules

The following promotions are forbidden unless a future PR supplies explicit constructions or cited theorems that justify them:

| Unsafe promotion | Required replacement |
| --- | --- |
| Deligne class -> algebraic cycle | Construct algebraic cycles or cite a theorem supplying them |
| finite monodromy -> Tate data | Construct arithmetic variety, field, and Galois action |
| comparison diagram -> motive | Specify a motivic category or accepted realization framework |
| regulator symbol -> regulator theorem | Supply motivic cohomology, regulator map, and L-value statement |
| proof-fabric validation -> mathematical proof | Provide mathematical definitions, theorem statements, and proofs |
| Heller-Godel method result -> Hodge progress | Pass through intake, registry, anti-seed, and bridge requirements |

The obstruction registry records these and related downgrade rules in structured form:

```text
docs/obstruction-registry.md
```

## Workstream order

Current recommended workstream order:

1. keep anti-seed and claim-boundary checks green;
2. maintain README-advertised structural documents;
3. maintain the Hodge Origin Registry as artifacts are added;
4. maintain the Obstruction Registry as unsafe-promotion classes are identified or closed;
5. evaluate Heller-Godel artifacts against the Hodge bridge requirements only after the relevant artifact is repo-grade;
6. require explicit constructions before theorem-facing Hodge claims.

## Next structural hardening target

The next structural hardening target is a lightweight checker that verifies:

```text
README-advertised files exist;
program-map dependencies exist;
hodge-origin-registry includes current core artifacts;
obstruction-registry is referenced from the program map;
claim-boundary and anti-seed files are present.
```

This checker should not add theorem claims. It should only prevent topology drift.

## Nonclaims

This program map does not claim:

1. a proof of the Hodge conjecture;
2. progress on the Hodge conjecture;
3. construction of algebraic cycles;
4. construction of a rational Hodge class;
5. construction of a projective variety;
6. a Deligne-to-Hodge bridge theorem;
7. that Heller-Godel artifacts satisfy any Hodge bridge primitive;
8. that registry inclusion upgrades evidence level;
9. that the current map is exhaustive or permanent;
10. that future theorem work is authorized without anti-seed and claim-boundary review.

## Update rule

Update this map when:

1. a README-advertised structural document is added;
2. the Hodge Origin Registry changes its lane model;
3. the Heller-Godel intake classification changes;
4. the bridge scaffold adds or removes a primitive;
5. the obstruction registry adds a new category that affects program flow;
6. a theorem-facing Hodge artifact is added.

Do not update this map for typo-only or formatting-only changes unless they affect artifact topology or claim boundaries.
