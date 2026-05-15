# Hodge Origin Registry

Status: Hodge-origin registry.  
Claim level: registry / classification; no theorem claim.  
Date: 2026-05-15.  
Depends on:

```text
docs/anti-seed-hodge.md
docs/claim-boundary.md
docs/intake/heller-godel-proof-fabric-intake.md
docs/registries/heller-godel-artifact-registry.md
docs/scaffolds/hodge_bridge_requirements_scaffold.md
```

## Purpose

This registry implements the README boundary principle: preserve Hodge origin, classify distance from the mathematical core, and prevent unsafe promotion.

Everything in this repository is treated as Hodge-originated because it enters through the Hodge Program. That does not mean every entry is a Hodge theorem, Hodge-conjecture attack, algebraic-cycle claim, or proof of progress. The registry records genealogical attachment and distance classification.

## Classification lanes

The registry uses the four README lanes:

| Lane | Meaning | Promotion risk |
| --- | --- | --- |
| `core-hodge` | Hodge conjecture, generalized Hodge, standard conjectures, algebraic cycles, Lefschetz/Kunneth/Hodge-index structures | Mistaking scaffolds for cycle-class proofs |
| `hodge-arithmetic` | Tate, Mumford-Tate, Beilinson, Bloch-Beilinson, Bloch-Kato, Fontaine-Mazur, periods, regulators, torsion obstructions | Mistaking arithmetic analogy or regulator symbols for theorems |
| `hodge-method` | comparison isomorphisms, regulator maps, finite monodromy, Deligne cohomology, torsion shadows, obstruction registries | Mistaking method-adjacent proof fabric for Hodge progress |
| `hodge-fallout` | distant descendant programs whose connection is methodological or genealogical rather than direct Hodge content | Mistaking analogy for mathematical evidence |

## Registry entry schema

Each entry should record:

1. artifact path or source;
2. classification lane;
3. evidence level;
4. safe use;
5. anti-seed failure mode;
6. forbidden promotion;
7. registry update condition.

Evidence levels are:

```text
program-goal
definition
source-capture
intake
registry
scaffold
obstruction
lemma
theorem
non-claim
```

The evidence level does not override the classification lane. A theorem-level artifact can still be `hodge-method` rather than `core-hodge` if it does not construct algebraic cycles or rational Hodge classes.

## Current Hodge-origin entries

| Artifact | Lane | Evidence level | Safe use | Anti-seed failure mode | Forbidden promotion |
| --- | --- | --- | --- | --- | --- |
| `README.md` | `core-hodge` as program charter; no proof claim | program-goal / non-claim | Defines repository purpose, boundary principle, and initial structure | Treating repository existence as proof progress | Do not cite as theorem evidence |
| `docs/anti-seed-hodge.md` | `core-hodge` boundary control | obstruction / non-claim | Records false formulations and unsafe promotions before positive adjacency | Ignoring category mistakes before making claims | Do not bypass anti-seed for positive registry work |
| `docs/claim-boundary.md` | `core-hodge` boundary control | definition / non-claim | Defines allowed labels and forbidden promotions | Label drift from method artifact to Hodge theorem | Do not promote claims outside declared labels |
| `docs/intake/heller-godel-proof-fabric-intake.md` | `hodge-method` | intake / non-claim | Classifies Heller-Godel proof fabric as method-adjacent | Treating finite phase or Deligne-unit work as Hodge proof/progress | Do not classify Heller-Godel as `core-hodge` without new constructions |
| `docs/registries/heller-godel-artifact-registry.md` | `hodge-method` | registry / non-claim | Tracks Heller-Godel artifacts by distance and evidence level | Treating registry inclusion as theorem evidence | Do not treat finite-character artifacts as algebraic cycles |
| `docs/scaffolds/hodge_bridge_requirements_scaffold.md` | `hodge-method` | scaffold / definition | Defines requirements for any future bridge attempt | Treating requirements vocabulary as a bridge theorem | Do not claim any current artifact satisfies the bridge primitives |

## Current registry interpretation

The repository currently contains boundary controls, intake artifacts, registry artifacts, and requirements scaffolds. It does not yet contain:

```text
validated core Hodge theorem artifact
projective variety construction
rational Hodge class construction
algebraic-cycle construction
cycle-class equality proof
Deligne-to-Hodge bridge theorem
obstruction-removal theorem
```

The strongest safe statement is:

```text
The Hodge Program Proof repository has a claim-safe scaffolding and registry layer for Hodge-origin material. It does not yet contain a Hodge proof, Hodge-progress theorem, or algebraic-cycle construction.
```

## Nonclaims

This registry does not claim:

1. that the registry is exhaustive;
2. that registered artifacts constitute Hodge progress;
3. that registered artifacts prove or attack the Hodge conjecture;
4. that `hodge-method` artifacts are algebraic-cycle evidence;
5. that Heller-Godel finite-character artifacts satisfy Hodge bridge primitives;
6. that registry inclusion upgrades evidence level;
7. that the registry is the only source of truth for repository scope;
8. that all future Hodge-origin material must fit the current entries without extension.

## Update rule

Update this registry when a PR adds, removes, or materially changes:

1. an anti-seed or claim-boundary document;
2. an intake artifact;
3. a Hodge-origin source packet;
4. an obstruction registry entry;
5. a Hodge bridge or requirements scaffold;
6. a theorem-facing or conjecture-facing Hodge artifact;
7. a cross-repo proof-fabric artifact whose Hodge distance classification changes.

Do not update this registry for typo-only, formatting-only, or CI-only PRs unless they affect claim-boundary enforcement or artifact classification.

## Relationship to the Heller-Godel artifact registry

The Heller-Godel artifact registry is a specialized registry for one source repository:

```text
docs/registries/heller-godel-artifact-registry.md
```

This Hodge Origin Registry is the repository-level registry of Hodge-origin material. It includes the Heller-Godel intake and registry as `hodge-method` entries, but it does not duplicate the Heller-Godel artifact table.

## Future work

The next README-advertised completion target should be:

```text
docs/program-map.md
```

The program map should summarize this registry, the anti-seed, the claim boundary, the Heller-Godel intake, and the bridge requirements scaffold without adding theorem claims.
