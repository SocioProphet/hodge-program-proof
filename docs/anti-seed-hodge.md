# Hodge Anti-Seed v0.1

Status: controlling negative seed for the Hodge Program Proof repository.

## Purpose

Anti-seed comes before seed.

Before this repository records positive adjacency, proposed constructions, or conjectural fallout, it records the known ways Hodge-style work goes wrong. This file is the negative-control layer for the program.

The function of the anti-seed is not pessimism. It is boundary discipline: it prevents false formulations, analogy drift, theorem inflation, and category mistakes from entering the program as if they were progress.

## Anti-seed rule

Every positive Hodge-origin artifact must pass through this filter:

1. Does it require algebraic cycles but only produce analytic or topological classes?
2. Does it require rational Hodge classes but only produce integral, torsion, or finite-monodromy shadows?
3. Does it require projectivity but only use compact Kähler, real, lattice, or analytic spaces?
4. Does it require a variation of Hodge structure but only provide a parameter scan?
5. Does it require a Galois representation but only provide finite phase characters?
6. Does it require a regulator theorem but only provide a symbol, residue, or local computation?
7. Does it confuse a comparison diagram with a motivic theorem?
8. Does it mistake obstruction taxonomy for obstruction removal?

If yes, the artifact is not rejected. It is downgraded to the correct status: observation, diagnostic, toy model, obstruction note, or program-goal.

## Known false or unsafe formulations

### A1. Integral Hodge is false

The integral version of the Hodge conjecture is false. Atiyah–Hirzebruch-type K-theoretic obstructions show that an integral Hodge class need not be algebraic.

Program consequence: torsion or integral data in this repo must never be promoted to algebraicity without an explicit cycle construction or cited theorem.

### A2. Compact Kähler is not enough

The classical Hodge conjecture is a statement for smooth projective complex varieties. Compact Kähler analogues are unsafe; non-projective Kähler examples can break naive formulations.

Program consequence: real manifolds, punctured analytic spaces, lattice spaces, and non-projective Kähler spaces are not valid native bases for Hodge-conjecture claims unless an explicit projective algebraic model is supplied.

### A3. Generalized formulations can be trivially false

Grothendieck corrected overly broad Hodge-style formulations because naive generalizations can fail for formal reasons.

Program consequence: every generalized claim must specify the category, coefficient field, filtration, and realization functor. If those are absent, the statement is not a conjecture; it is a slogan.

### A4. Deligne cohomology is not algebraicity

A class in Deligne cohomology can be regulator-ready without being the class of an algebraic cycle.

Program consequence: Deligne classes, cup-product symbols, tame symbols, and finite-monodromy characters are Hodge-adjacent objects, not algebraic cycles.

### A5. Torsion shadows are not Tate data

Finite monodromy characters may resemble finite-level arithmetic shadows. They are not Galois representations unless a field, arithmetic variety, and Galois action are constructed.

Program consequence: `mu_p` characters are not Tate, Mumford–Tate, Fontaine–Mazur, or Bloch–Kato evidence by themselves.

### A6. Comparison diagrams are not motives

A commuting diagram between analytic, topological, and dynamical realizations may be a useful test object. It is not a motivic theorem unless a category of motives or an accepted realization framework is constructed.

Program consequence: Paper I style `mu_2` comparisons remain small comparison tests, not motivic progress.

### A7. Regulator symbols are not regulator conjectures

A Deligne cup-product symbol or tame-symbol residue is a local or symbolic object. Beilinson-style conjectures require motivic cohomology, regulators, and L-value statements over arithmetic varieties.

Program consequence: regulator computations in this repo are local evidence objects, not Beilinson evidence unless connected to a proper arithmetic-geometric setting.

### A8. Hodge-origin is not Hodge-proof

A topic may enter the program through Hodge and remain Hodge-originated. That genealogy does not make it a Hodge theorem.

Program consequence: YM, BSD, RH/L-functions, Lawful Learning, proof dynamics, and Temporal Mechanics may be Hodge-originated in this repository only through a written path. They remain distant fallout unless a specific Hodge-theoretic structure is constructed.

## Default downgrades

| If an artifact says... | downgrade to... |
| --- | --- |
| proves Hodge | proposed program goal, unless a complete proof is present |
| algebraic cycle | analytic/regulator class, unless a cycle is constructed |
| Tate analogue | finite-character analogy, unless Galois action is constructed |
| motivic | comparison-style, unless a motivic category/functor is specified |
| regulator evidence | local regulator-symbol computation, unless L-value structure is proved |
| Hodge locus | parameter locus, unless a polarized VHS is established |
| projective variety | analytic or real test object, unless projectivity is proved |
| obstruction removed | obstruction named, unless a theorem removes it |

## Required first artifact for every lane

Every Hodge-origin lane must begin with an anti-seed block:

```text
Anti-seed:
- What false theorem would this become if overstated?
- Which known Hodge obstruction does it risk violating?
- What category is actually being used?
- What structure is missing for a real Hodge/Tate/Beilinson claim?
- What is the strongest safe statement?
```

## Current controlling state

No positive Hodge-origin registry entry should be merged until it names its anti-seed failure mode.
