# Hodge Bridge Requirements Scaffold

Status: requirements scaffold.  
Classification: `hodge-method`.  
Claim level: `definition` / `program-goal`; no theorem claim.  
Date: 2026-05-15.  
Depends on:

```text
docs/anti-seed-hodge.md
docs/claim-boundary.md
docs/intake/heller-godel-proof-fabric-intake.md
docs/registries/heller-godel-artifact-registry.md
```

Related workbench artifact:

```text
SocioProphet/Heller-Godel: docs/proofs/hodge_clay_target_gap_ledger.md
```

## Purpose

This scaffold defines the minimal requirement vocabulary for evaluating whether any Heller-Godel / Hodge-method artifact could ever be promoted toward a Hodge-facing construction.

It does not claim that any such promotion is currently possible. It defines the objects that would have to exist before a claim could be reviewed.

The scope envelope for this scaffold is not duplicated locally. It is inherited from:

```text
docs/anti-seed-hodge.md
docs/claim-boundary.md
```

In particular, Deligne cohomology is not algebraicity, torsion shadows are not Tate data, comparison diagrams are not motives, and regulator symbols are not regulator conjectures.

## Anti-seed block

Anti-seed:

- What false theorem would this become if overstated?
  - "A Deligne-unit, finite-character, or comparison-diagram artifact from Heller-Godel supplies a Hodge class or an algebraic cycle."
- Which known Hodge obstruction does it risk violating?
  - Deligne cohomology is not algebraicity.
  - Compact analytic or real test spaces are not smooth complex projective varieties.
  - Finite monodromy is not Tate data.
  - Comparison diagrams are not motives.
- What category is actually being used?
  - This scaffold uses requirement vocabulary only. It does not construct varieties, Hodge classes, cycles, or motivic categories.
- What structure is missing for a real Hodge claim?
  - A smooth complex projective variety, rational Hodge class, algebraic cycle family, cycle-class equality, and bridge theorem.
- What is the strongest safe statement?
  - The scaffold defines review obligations for any future Deligne-to-Hodge bridge attempt.

## Primitive 1 — Hodge target datum

A `Hodge target datum` is a record

```text
H = (X, k, alpha)
```

where:

1. `X` is intended to be a nonsingular complex projective variety;
2. `k` is a codimension / Hodge-degree index;
3. `alpha` is intended to be a rational Hodge class

```text
alpha in H^{2k}(X,Q) cap H^{k,k}.
```

A Hodge target datum is not valid until the following are supplied:

1. a definition of `X`;
2. a proof that `X` is nonsingular;
3. a proof that `X` is complex projective;
4. a definition of `alpha` as a rational cohomology class;
5. a proof that `alpha` has Hodge type `(k,k)`.

This scaffold does not supply such a datum. It only defines what one would have to contain.

## Primitive 2 — cycle realization datum

A `cycle realization datum` is a record

```text
C = (Z_i, q_i, cl(Z_i))_{i in I}
```

where:

1. each `Z_i` is intended to be an algebraic subvariety or algebraic cycle of codimension `k` on `X`;
2. each `q_i` is a rational coefficient;
3. `cl(Z_i)` is the cohomology class of `Z_i` in `H^{2k}(X,Q)`.

A cycle realization datum is not valid until the following are supplied:

1. definitions of the cycles `Z_i`;
2. a proof that each `Z_i` is algebraic;
3. a proof that each `Z_i` has codimension `k`;
4. a definition of the cycle class map being used;
5. rational coefficients `q_i`.

This scaffold does not construct algebraic cycles.

## Primitive 3 — cycle equality obligation

A `cycle equality obligation` is the proof target

```text
alpha = sum_i q_i cl(Z_i)
```

inside `H^{2k}(X,Q)`.

This obligation is not satisfied by:

1. producing a Deligne cohomology class;
2. producing a finite monodromy character;
3. producing a regulator symbol;
4. producing a tame-symbol residue;
5. producing a comparison diagram;
6. producing a proof-fabric validation report.

It requires an actual equality between the rational Hodge class and rational algebraic-cycle classes in the specified cohomology group.

## Primitive 4 — Deligne-to-Hodge bridge obligation

A `Deligne-to-Hodge bridge obligation` is a proposed route from Heller-Godel-style data to a Hodge target datum.

It must specify:

```text
current Deligne-unit / finite-character / regulator-symbol data
  -> candidate Hodge target datum (X, k, alpha)
```

A bridge obligation is not a bridge theorem. It is a checklist of missing constructions.

To become theorem-grade, a bridge must supply:

1. the target variety `X`;
2. the class `alpha`;
3. the Hodge-type proof for `alpha`;
4. a comparison or realization theorem explaining why the Heller-Godel data define `alpha`;
5. a cycle realization datum;
6. a cycle equality proof.

A proposed bridge may validly conclude negatively. For example, an evaluation may show that a Heller-Godel Deligne-unit artifact has no current route to a rational Hodge class.

## Evaluation table for current Heller-Godel artifacts

| Requirement | Current Heller-Godel status | Hodge Program interpretation |
| --- | --- | --- |
| Hodge target datum `(X,k,alpha)` | Not present | Missing |
| Smooth complex projective variety `X` | Not present | Missing |
| Rational Hodge class `alpha` | Not present | Missing |
| Cycle realization datum | Not present | Missing |
| Cycle equality obligation | Not present | Missing |
| Deligne-to-Hodge bridge theorem | Not present | Missing |
| Deligne-unit / finite-character artifacts | Present in Heller-Godel | Hodge-method input only |
| Catalan A1 comparison fixtures | Present in Heller-Godel | Hodge-method / finite comparison only |
| p = 3 scaffold | Present in Heller-Godel | Hodge-method / finite phase vocabulary only |

## Nonclaims

This scaffold does not claim:

1. a proof of the Hodge conjecture;
2. progress on the Hodge conjecture;
3. construction of a smooth complex projective variety `X`;
4. construction of a rational Hodge class `alpha`;
5. construction of algebraic cycles;
6. proof of a cycle-class equality;
7. construction of a Deligne-to-Hodge bridge;
8. that any Heller-Godel artifact satisfies a Hodge primitive;
9. that the four primitives are exhaustive;
10. that the four primitives are independent.

## Future work

The next Hodge Program evaluation artifact should test the current Heller-Godel Deligne-unit construction against these four primitives.

That evaluation must be allowed to conclude:

```text
No valid Hodge target datum currently follows.
```

If the evaluation does identify a candidate, it must update the artifact registry and add a specific anti-seed block before any positive claim is promoted.
