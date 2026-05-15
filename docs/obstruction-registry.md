# Hodge Obstruction Registry

Status: obstruction registry.  
Claim level: registry / diagnostic; no theorem claim.  
Date: 2026-05-15.  
Primary source of truth:

```text
docs/anti-seed-hodge.md
docs/claim-boundary.md
docs/hodge-origin-registry.md
docs/program-map.md
```

## Purpose

This registry converts the Hodge anti-seed into structured obstruction entries.

It records unsafe promotions, correct downgrades, missing structures, affected lanes, safe uses, and update triggers. The registry is not a proof layer. It is a claim-boundary and diagnostic layer.

The governing rule is:

```text
anti-seed first
preserve Hodge origin
classify distance
prevent unsafe promotion
```

## Registry schema

Each obstruction entry uses the following fields:

```text
ID
Name
Unsafe promotion
Correct downgrade
Required missing structure
Affected lanes
Safe use
Registry update trigger
```

A registry entry does not forbid work. It defines the minimum structure required before a claim may be promoted.

## Core obstruction entries

### OBS-HODGE-001 — Integral Hodge false-positive risk

Unsafe promotion:

```text
integral or torsion class -> algebraic cycle
```

Correct downgrade:

```text
torsion / integral diagnostic object
```

Required missing structure:

1. explicit algebraic cycle;
2. cycle-class map;
3. proof that the integral class is represented by that cycle;
4. obstruction check against Atiyah-Hirzebruch-type K-theoretic failures.

Affected lanes:

```text
core-hodge
hodge-method
hodge-fallout
```

Safe use:

Use torsion or integral data as obstruction diagnostics or finite witnesses only.

Registry update trigger:

Update if an artifact claims algebraicity from torsion, integral, or finite-monodromy data.

### OBS-HODGE-002 — Compact-Kahler / non-projective base risk

Unsafe promotion:

```text
compact Kahler, real, punctured analytic, or lattice base -> smooth complex projective variety
```

Correct downgrade:

```text
analytic / real / lattice test object
```

Required missing structure:

1. smooth complex projective variety `X`;
2. proof of projectivity;
3. comparison between the test object and `X`;
4. preservation of the relevant class under the comparison.

Affected lanes:

```text
core-hodge
hodge-method
hodge-fallout
```

Safe use:

Use non-projective bases as diagnostics, local models, or Hodge-origin fallout only.

Registry update trigger:

Update if a PR introduces a new base space and uses Hodge-conjecture language.

### OBS-HODGE-003 — Generalized-Hodge formulation risk

Unsafe promotion:

```text
broad analogy or slogan -> generalized Hodge-style conjecture
```

Correct downgrade:

```text
program goal / formulation candidate
```

Required missing structure:

1. category;
2. coefficient field;
3. filtration;
4. realization functor;
5. exact statement of the conjecture;
6. known counterexample scan.

Affected lanes:

```text
core-hodge
hodge-arithmetic
hodge-method
hodge-fallout
```

Safe use:

Use generalized statements only as formulation candidates until all structural data are specified.

Registry update trigger:

Update if a new conjectural lane is introduced.

### OBS-HODGE-004 — Deligne cohomology to algebraicity promotion risk

Unsafe promotion:

```text
Deligne class / Deligne unit / tame symbol / cup-product symbol -> algebraic cycle
```

Correct downgrade:

```text
Deligne-adjacent regulator or symbol object
```

Required missing structure:

1. projective variety;
2. rational Hodge class;
3. algebraic cycle;
4. cycle-class equality;
5. regulator or Abel-Jacobi comparison, if used.

Affected lanes:

```text
core-hodge
hodge-method
```

Safe use:

Use Deligne objects as Hodge-method artifacts and bridge candidates only.

Registry update trigger:

Update if a Heller-Godel artifact or other Deligne object is evaluated for Hodge bridge promotion.

### OBS-HODGE-005 — Finite monodromy to Tate data promotion risk

Unsafe promotion:

```text
mu_p character / finite monodromy / torsion shadow -> Tate or Galois data
```

Correct downgrade:

```text
finite-character analogy
```

Required missing structure:

1. arithmetic variety;
2. base field;
3. Galois action;
4. l-adic realization;
5. invariant-cycle or Tate-class statement.

Affected lanes:

```text
hodge-arithmetic
hodge-method
hodge-fallout
```

Safe use:

Use finite monodromy as a finite-phase diagnostic unless arithmetic structure is explicitly constructed.

Registry update trigger:

Update if a finite-character artifact is compared to Tate, Mumford-Tate, Bloch-Kato, or Fontaine-Mazur language.

### OBS-HODGE-006 — Comparison diagram to motive promotion risk

Unsafe promotion:

```text
commuting comparison diagram -> motivic theorem
```

Correct downgrade:

```text
comparison-style test object
```

Required missing structure:

1. motivic category or accepted substitute;
2. objects in that category;
3. realization functors;
4. proof that the diagram is induced by a common motivic object.

Affected lanes:

```text
core-hodge
hodge-arithmetic
hodge-method
hodge-fallout
```

Safe use:

Use comparison diagrams to test coherence across realizations; do not call them motives without a motivic framework.

Registry update trigger:

Update if an artifact uses motivic, realization, or comparison-isomorphism language.

### OBS-HODGE-007 — Regulator symbol to regulator conjecture promotion risk

Unsafe promotion:

```text
local regulator symbol / tame-symbol residue / Beilinson-adjacent number -> Beilinson evidence
```

Correct downgrade:

```text
local regulator-symbol computation
```

Required missing structure:

1. arithmetic variety;
2. motivic cohomology class;
3. regulator map;
4. L-value or special-value statement;
5. comparison theorem connecting the computation to the conjectural framework.

Affected lanes:

```text
hodge-arithmetic
hodge-method
```

Safe use:

Use local regulator computations as source packets or diagnostic evidence only.

Registry update trigger:

Update if a computation is described as Beilinson, Bloch-Kato, or special-value evidence.

### OBS-HODGE-008 — Hodge-origin to Hodge-proof promotion risk

Unsafe promotion:

```text
Hodge-origin registry entry -> Hodge proof or Hodge progress
```

Correct downgrade:

```text
classified Hodge-origin artifact
```

Required missing structure:

1. theorem statement;
2. target category;
3. proof;
4. algebraic-cycle or Hodge-class construction if core Hodge;
5. registry update documenting lane and evidence level.

Affected lanes:

```text
core-hodge
hodge-arithmetic
hodge-method
hodge-fallout
```

Safe use:

Use Hodge-origin as genealogy, not as evidence level.

Registry update trigger:

Update whenever a new artifact enters the Hodge Origin Registry.

## YM / Hodge-fallout diagnostic entries

The following entries capture Yang-Mills analogues raised by Deligne-facing review. They are `hodge-fallout` diagnostics. They are not Hodge evidence and do not modify Clay YM theorem state.

### OBS-YM-001 — Smooth-forms versus currents / grid-versus-Galerkin discrepancy

Unsafe promotion:

```text
grid computation agrees locally -> Galerkin / continuum object agrees globally
```

Correct downgrade:

```text
regularity and weak-limit comparison problem
```

Required missing structure:

1. weak-limit topology;
2. regularity theorem relating grid sampling and Galerkin projection;
3. proof that exact or null directions are preserved under the limit;
4. deterministic comparison across the strong-coupling window.

Affected lanes:

```text
hodge-fallout
```

Safe use:

Use the Deligne smooth-forms/currents equivalence as a template for what a YM grid/Galerkin equivalence theorem would need, not as evidence that the equivalence holds.

Registry update trigger:

Update if a YM artifact claims grid/Galerkin agreement or closes the grid-comparison gate.

### OBS-YM-002 — Filtration versus decomposition in beta families

Unsafe promotion:

```text
eigenvalue tracking -> stable Hodge-style family invariant
```

Correct downgrade:

```text
spectral-filtration diagnostic
```

Required missing structure:

1. spectral filtration definition across beta;
2. continuity or analyticity in beta;
3. first-order transversality or jump-control statement;
4. locus theorem for persistent degeneracies, if claimed.

Affected lanes:

```text
hodge-fallout
```

Safe use:

Track cumulative spectral filtrations rather than only eigenvalue decompositions when using Hodge-family analogies.

Registry update trigger:

Update if YM response diagnostics invoke variation-of-Hodge-structure, Griffiths transversality, or Hodge-locus analogies.

### OBS-YM-003 — Lefschetz completeness versus face-regression consistency

Unsafe promotion:

```text
face regression matches -> lower-dimensional faces generate all higher-dimensional structure
```

Correct downgrade:

```text
restriction consistency result
```

Required missing structure:

1. completeness theorem;
2. proof that all higher-dimensional invariants are generated by face data;
3. treatment of genuinely higher-sector classes for non-product kernels;
4. failure-mode scan modelled on Griffiths-group-style non-finite generation risk.

Affected lanes:

```text
hodge-fallout
```

Safe use:

Use face regression as consistency evidence only; require completeness before inductive closure claims.

Registry update trigger:

Update if YM work claims that N=2 or face data suffice for N=3 or higher structure outside product kernels.

### OBS-YM-004 — Algorithmic Hodge-locus asymmetry

Unsafe promotion:

```text
finite decision procedure -> continuum Hodge / Clay decidability analogue
```

Correct downgrade:

```text
finite analogue of a locus-decision problem
```

Required missing structure:

1. finite parameter space;
2. exact decidable structural predicates;
3. proof of soundness for the finite predicates;
4. explicit statement that no continuum decision algorithm follows.

Affected lanes:

```text
hodge-fallout
```

Safe use:

Use finite YM algorithms as toy tests of structural-locus discipline, not as claims about Hodge or continuum decidability.

Registry update trigger:

Update if finite YM diagnostics are compared to Hodge-locus or CDK-style algebraicity results.

### OBS-YM-005 — Motivated substitute versus Clay-level theorem

Unsafe promotion:

```text
weaker motivated object -> Clay-level mass-gap construction
```

Correct downgrade:

```text
application-sufficient substitute
```

Required missing structure:

1. list of target applications;
2. properties required by each application;
3. proof that the substitute supplies those properties;
4. explicit statement of which Clay requirements remain unmet.

Affected lanes:

```text
hodge-fallout
```

Safe use:

Use motivated substitutes to stratify application strength, not to claim Clay completion.

Registry update trigger:

Update if YM work introduces weakened reconstruction, OS, Wightman, or mass-gap substitutes.

### OBS-YM-006 — Q-rationality and integer representation labels

Unsafe promotion:

```text
complex invariant subspace -> physical rational/integer-labelled sector
```

Correct downgrade:

```text
integer-labelled sector diagnostic
```

Required missing structure:

1. integer or half-integer representation labels;
2. descent criterion from complex invariant subspace to labelled sector;
3. proof that the sector is preserved by the relevant operator;
4. physical interpretation of the labelled sector.

Affected lanes:

```text
hodge-fallout
```

Safe use:

Use rationality analogies to discipline which spectral sectors count as physically labelled sectors.

Registry update trigger:

Update if YM artifacts compare representation labels to rational Hodge classes.

### OBS-YM-007 — Low-degree exact-sequence success risk

Unsafe promotion:

```text
N=2 clean closure -> all-N structural theorem
```

Correct downgrade:

```text
low-degree exact-sequence candidate
```

Required missing structure:

1. exact sequence or algebraic mechanism explaining low-N closure;
2. boundary map or obstruction map;
3. proof that the sequence remains exact at higher N or reason it fails;
4. relation to OS or Wilson-loop algebra if used.

Affected lanes:

```text
hodge-fallout
```

Safe use:

Use clean low-N closures as evidence for an exact-sequence search, not as all-N evidence.

Registry update trigger:

Update if YM work generalizes from N=2 / Jmax=1 closures.

### OBS-YM-008 — Missing falsifiable continuum-uplift test

Unsafe promotion:

```text
rich obstruction survey -> falsifiable continuum theorem
```

Correct downgrade:

```text
methodological gap: no sharp numerical or structural test yet
```

Required missing structure:

1. computable quantity;
2. predicted value or rationality/invariance condition;
3. proof that Clay-level or continuum uplift would imply the condition;
4. counterexample path if the condition fails.

Affected lanes:

```text
hodge-fallout
```

Safe use:

Use Hodge/Tate-style rationality tests as inspiration for creating a YM falsifiability target.

Registry update trigger:

Update if YM work proposes a concrete continuum-uplift falsification test.

### OBS-YM-009 — GAGA-like lattice-to-continuum promotion risk

Unsafe promotion:

```text
finite lattice algebra -> continuum reconstructed algebra
```

Correct downgrade:

```text
GAGA-like equivalence target
```

Required missing structure:

1. source lattice category;
2. target continuum category;
3. reconstruction functor;
4. equivalence or fully-faithfulness theorem;
5. compatibility with reflection positivity and continuum limits.

Affected lanes:

```text
hodge-fallout
```

Safe use:

Use GAGA as a structural template for what lattice-to-continuum equivalence would require.

Registry update trigger:

Update if YM work claims a lattice/continuum category equivalence or reconstruction equivalence.

### OBS-YM-010 — Maximality prediction risk

Unsafe promotion:

```text
some physical sector is realized -> maximal physical sector is realized
```

Correct downgrade:

```text
maximality question
```

Required missing structure:

1. definition of type-compatible sector;
2. definition of physically realized sector;
3. maximality theorem or counterexample;
4. non-product-kernel analysis.

Affected lanes:

```text
hodge-fallout
```

Safe use:

Use maximality framing to distinguish separability success from full realization.

Registry update trigger:

Update if YM work uses maximality language or claims all compatible sectors are physically realized.

## Heller-Godel-specific doctrinal correction

The obstruction registry also records the following correction as active doctrine for Heller-Godel intake:

```text
carry cocycle != Deligne cup-product residue
```

Correct reading:

```text
carry = Bockstein / lifted-index section defect
Deligne cup product = separate regulator-symbol refinement
tame-symbol residue != carry
```

Unsafe promotion:

```text
carry or kappa_L -> Deligne regulator residue
```

Correct downgrade:

```text
finite lifted-index bookkeeping versus separate regulator-symbol branch
```

Registry update trigger:

Update Heller-Godel intake or artifact registry if future Heller-Godel artifacts reintroduce carry/cup-product conflation.

## Nonclaims

This registry does not claim:

1. proof of the Hodge conjecture;
2. progress on the Hodge conjecture;
3. that Heller-Godel artifacts satisfy Hodge bridge primitives;
4. that YM analogues are Hodge evidence;
5. that YM analogues prove or advance the Clay Yang-Mills problem;
6. that finite diagnostics imply continuum theorems;
7. that comparison diagrams are motives;
8. that regulator symbols are regulator conjectures;
9. that obstruction taxonomy removes obstructions;
10. that this registry is exhaustive.

## Update rule

Update this registry when:

1. a new unsafe promotion class is identified;
2. a registry entry is closed by an explicit theorem or construction;
3. a Hodge-origin artifact changes lane or evidence level;
4. Heller-Godel changes Deligne, regulator, finite-character, or Hodge-gap doctrine;
5. YM fallout adds a new Hodge-analogue diagnostic;
6. the program map changes the workstream order;
7. claim-boundary enforcement changes.

Do not update for typo-only, formatting-only, or CI-only changes unless the edit affects obstruction classification or claim-boundary enforcement.
