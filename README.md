# Hodge Program Proof

Hodge-theoretic proof program, evidence ledger, source packet, obstruction registry, and claim-boundary discipline for the SocioProphet research estate.

## Status

Scaffold repository. No theorem claims are active until backed by explicit definitions, fixtures, validators, and review artifacts.

## Boundary principle

Everything in this repo is treated as Hodge-originated: it enters through the Hodge program and remains genealogically attached to that program.

That does not mean every entry is a Hodge theorem, a Hodge-conjecture attack, or a claim about algebraic cycles. The repository separates Hodge-originated material by distance from the mathematical core:

1. **Core Hodge** — Hodge conjecture, generalized Hodge, standard conjectures, algebraic cycles, Lefschetz/Künneth/Hodge-index structures.
2. **Hodge-arithmetic** — Tate, Mumford–Tate, Beilinson, Bloch–Beilinson, Bloch–Kato, Fontaine–Mazur, periods, regulators, torsion obstructions.
3. **Hodge-method** — comparison isomorphisms, regulator maps, finite monodromy, Deligne cohomology, torsion shadows, obstruction registries.
4. **Hodge-fallout / distant descendants** — YM, BSD, RH/L-functions, Temporal Mechanics, Lawful Learning, or other programs whose connection is methodological or genealogical rather than a direct Hodge claim.

The rule is: preserve origin, classify distance, prevent bastardization.

## Anti-seed first

Positive registry work must begin from `docs/anti-seed-hodge.md`.

Anti-seed records known false formulations, category mistakes, unsafe promotions, and failure modes before any positive adjacency map is created. No Hodge-origin lane should be promoted until it names its anti-seed failure mode.

## Framework and PFK dependency

This repository depends on `SocioProphet/Heller-Godel @ 988307215ad38ccb16514311222184a1b757752b` for framework objects (`HG-*`) and canonical PFK operational substrate (`PFK-*`). See `DEPENDENCIES.md`.

PFK schemas are canonically hosted at:

```text
SocioProphet/Heller-Godel/proof_fabric_kernel/schemas/
```

No local schema copy is authoritative. If a local schema directory exists in future work, it must not shadow canonical PFK schema names.

## Non-claims

This repository does **not** claim a proof of the Hodge conjecture.

It does **not** claim progress on the Hodge conjecture unless a specific theorem, construction, or verified obstruction-removal artifact is recorded in the claim ledger.

It does **not** assert algebraicity of any Deligne, Betti, de Rham, torsion, regulator, or finite-monodromy class without an explicit algebraic-cycle construction or a cited theorem that supplies one.

It does **not** treat analogy with Yang–Mills, BSD, RH, proof dynamics, Temporal Mechanics, or Lawful Learning as mathematical evidence for Hodge.

## Initial structure

```text
docs/
  anti-seed-hodge.md
  claim-boundary.md
  program-map.md
  hodge-origin-registry.md
  obstruction-registry.md
references/
  hodge-source-packet.md
scripts/
  check_claim_boundary.py
.github/workflows/
  validate.yml
DEPENDENCIES.md
```

## Current work

The first workstream is the Hodge anti-seed: classify failure modes before classifying positive fallout. The second workstream is a Hodge-origin registry that classifies ranked adjacent problems without collapsing them into one field or overstating what follows from Paper I / Heller-Godel.
