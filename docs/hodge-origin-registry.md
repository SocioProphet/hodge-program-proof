# Hodge-Origin Registry v0.1

Status: initial positive registry, anti-seed gated. No theorem promotion.

## Purpose

This registry records problems and workstreams that entered the program through the Hodge lane. The registry preserves that genealogy while classifying mathematical distance from the Hodge core.

The registry does **not** flatten all entries into Hodge. It does **not** claim that distant fallout is evidence for Hodge. Every entry must name its anti-seed failure mode before it can name a positive next artifact.

## Classification axes

- **Origin:** how the entry entered the Hodge program.
- **Distance:** `core-hodge`, `hodge-arithmetic`, `hodge-method`, `hodge-fallout`, or `out-of-scope`.
- **Safe status:** observation, diagnostic, toy problem, conjecture, program-goal, or non-claim.
- **Anti-seed failure mode:** the false promotion this entry is most likely to cause.
- **First safe artifact:** the next artifact that can be produced without overclaiming.

## Registry table

| Rank | Entry | Distance | Safe status | Anti-seed failure mode | First safe artifact |
| --- | --- | --- | --- | --- | --- |
| 1 | Atiyah–Hirzebruch / Soulé–Voisin torsion | hodge-arithmetic | diagnostic / toy problem | torsion shadow -> algebraic cycle | torsion-template note for Paper I examples |
| 2 | Beilinson regulator behavior | hodge-arithmetic | diagnostic / toy problem | regulator symbol -> Beilinson evidence | regulator-output note for chain/Catalan |
| 3 | Tate conjecture for K3-type comparison settings | hodge-arithmetic | method comparison | comparison diagram -> Tate result | comparison-template note: K3 vs `mu_2` triple point |
| 4 | Finite-level Mumford–Tate | hodge-arithmetic | diagnostic | finite character -> Mumford–Tate data | finite-character obstruction note |
| 5 | Bloch–Kato Selmer structure | hodge-arithmetic | diagnostic | finite phase data -> Selmer group input | missing-structure note |
| 6 | Fontaine–Mazur lifting | hodge-arithmetic | diagnostic | residual character -> p-adic representation | residual-vs-lift obstruction note |
| 7 | Bloch–Beilinson filtration | hodge-arithmetic | diagnostic | Deligne class -> Chow filtration input | analytic-side-only note |
| 8 | Yang–Mills mass gap program | hodge-fallout | distant fallout / method transfer | obstruction taxonomy -> Hodge evidence | genealogy note only |
| 9 | BSD program | hodge-fallout | distant fallout / method transfer | arithmetic method adjacency -> Hodge evidence | genealogy note only |
| 10 | RH / GRH / automorphic L-function RH | hodge-fallout | distant fallout / diagnostic | regulator/L-function vocabulary -> RH evidence | non-attachment note |
| 11 | Generalized Hodge conjecture | core-hodge | program-goal / non-claim | generalized slogan -> theorem | formulation-boundary note |
| 12 | Standard conjectures on algebraic cycles | core-hodge | program-goal / non-claim | cohomological symmetry -> algebraic correspondence | correspondence-missing note |
| 13 | Grothendieck period conjecture | hodge-arithmetic | diagnostic | period-adjacent number -> period conjecture evidence | toy-period note |
| 14 | Tate–Shafarevich finiteness | hodge-arithmetic | distant arithmetic adjacency | finite torsion vocabulary -> Sha evidence | BSD-separation note |
| 15 | Parity conjecture | hodge-arithmetic | distant arithmetic adjacency | sign/phase analogy -> parity theorem | BSD-separation note |
| 16 | Tate conjecture, general | hodge-arithmetic | non-claim / method comparison | finite character -> Tate class | Tate-boundary note |
| 17 | Hodge conjecture proper | core-hodge | non-claim | Hodge-originated artifact -> Hodge proof | claim-boundary note |
| 18 | abc / Szpiro / Vojta cluster | hodge-fallout | distant fallout | Diophantine adjacency -> Hodge evidence | non-attachment note |
| 19 | Langlands functoriality | hodge-fallout | distant fallout | finite character -> Langlands functoriality | non-attachment note |
| 20 | Sato–Tate generalizations | hodge-fallout | distant fallout | finite-level statistics -> Sato–Tate evidence | non-attachment note |
| 21 | Goldbach / twin prime / k-tuples cluster | out-of-scope | out of Hodge scope | major-problem list proximity -> Hodge relevance | exclusion note |
| 22 | Hilbert's tenth over `Q` | out-of-scope | out of Hodge scope | logic/Diophantine proximity -> Hodge relevance | exclusion note |
| 23 | Jacobian conjecture / Zariski cancellation | out-of-scope | out of Hodge scope | algebraic-geometry vocabulary -> Hodge relevance | exclusion note |
| 24 | Smooth 4D Poincaré / Schoenflies | out-of-scope | out of Hodge scope | topology proximity -> Hodge relevance | exclusion note |
| 25 | Hadwiger / Erdős–Hajnal / union-closed cluster | out-of-scope | out of Hodge scope | famous-problem proximity -> Hodge relevance | exclusion note |

## Detailed anti-seed entries

### 1. Atiyah–Hirzebruch / Soulé–Voisin torsion

Origin: Paper I's finite monodromy and Deligne-cohomology torsion shadows.

Distance: `hodge-arithmetic`.

Safe status: diagnostic toy problem.

Anti-seed:
- false theorem if overstated: torsion Deligne shadow implies algebraic cycle;
- known obstruction: integral Hodge is false;
- actual category: finite monodromy / Deligne-cohomology torsion shadow;
- missing structure: algebraic variety and explicit algebraic cycle;
- strongest safe statement: compare Paper I torsion examples against the Soulé–Voisin / Atiyah–Hirzebruch obstruction template.

First safe artifact: `docs/notes/soule-voisin-torsion-template.md`.

### 2. Beilinson regulator behavior

Origin: Paper I level-1 Deligne unit and level-2 cup-product symbol.

Distance: `hodge-arithmetic`.

Safe status: diagnostic toy problem.

Anti-seed:
- false theorem if overstated: local regulator symbol gives Beilinson-conjecture evidence;
- known obstruction: Beilinson requires motivic cohomology and arithmetic L-values;
- actual category: local Deligne symbol / tame-symbol residue;
- missing structure: arithmetic variety, motivic class, regulator map to an L-value statement;
- strongest safe statement: compute regulator outputs of toy proof-class examples and classify what they are not.

First safe artifact: `docs/notes/beilinson-toy-regulator-output.md`.

### 3. Tate conjecture for K3-type comparison settings

Origin: comparison-isomorphism discipline around the Paper I `mu_2` triple point.

Distance: `hodge-arithmetic`.

Safe status: method comparison.

Anti-seed:
- false theorem if overstated: comparison diagram implies Tate-style algebraic class;
- known obstruction: Tate requires an arithmetic variety, Galois action, and invariant `l`-adic class;
- actual category: finite comparison diagram and monodromy character;
- missing structure: K3 surface or arithmetic variety, Frobenius/Galois action, cycle class map;
- strongest safe statement: compare the shape of K3 comparison methods with the shape of the `mu_2` triple point.

First safe artifact: `docs/notes/k3-tate-comparison-template.md`.

### 4. Finite-level Mumford–Tate

Origin: finite monodromy characters and product constraints.

Distance: `hodge-arithmetic`.

Safe status: diagnostic.

Anti-seed:
- false theorem if overstated: `mu_N` character family is Mumford–Tate data;
- known obstruction: Mumford–Tate concerns algebraic groups attached to Hodge structures and compatible `l`-adic images;
- actual category: finite cyclic characters on punctured analytic spaces;
- missing structure: polarizable Hodge structure, Galois representation, motivic group;
- strongest safe statement: identify exactly which finite-level structures are absent.

First safe artifact: `docs/notes/finite-character-vs-mumford-tate.md`.

### 5. Bloch–Kato / Fontaine–Mazur / Selmer-lift cluster

Origin: finite residual-character analogy around `mu_p` shadows.

Distance: `hodge-arithmetic`.

Safe status: diagnostic.

Anti-seed:
- false theorem if overstated: finite residual character gives Bloch–Kato or Fontaine–Mazur evidence;
- known obstruction: these conjectures require arithmetic Galois representations and local/global conditions;
- actual category: finite monodromy from analytic singularity;
- missing structure: number field, Galois representation, Selmer condition, p-adic lift;
- strongest safe statement: document the missing arithmetic structures.

First safe artifact: `docs/notes/residual-character-missing-arithmetic.md`.

### 6. Hodge proper and generalized Hodge

Origin: core Hodge source packet and Deligne/Voisin/da Silva references.

Distance: `core-hodge`.

Safe status: non-claim / program-goal.

Anti-seed:
- false theorem if overstated: Hodge-originated work is Hodge progress;
- known obstruction: algebraicity of rational `(p,p)` classes is the hard part;
- actual category: scaffold and adjacent test objects;
- missing structure: algebraic-cycle construction or accepted theorem supplying one;
- strongest safe statement: maintain a claim ledger and obstruction registry.

First safe artifact: `docs/obstruction-registry.md`.

### 7. Hodge-fallout corridors: YM, BSD, RH/L-functions

Origin: problems entered through Hodge-adjacent comparison, obstruction, and evidence-ledger discipline.

Distance: `hodge-fallout`.

Safe status: distant fallout / genealogy note.

Anti-seed:
- false theorem if overstated: method transfer gives Hodge evidence;
- known obstruction: different mathematical objects and proof obligations;
- actual category: methodology/genealogy transfer;
- missing structure: explicit Hodge-theoretic object connecting the program back to algebraic cycles or Hodge classes;
- strongest safe statement: preserve genealogy while marking the lane as distant.

First safe artifact: `docs/notes/hodge-fallout-genealogy.md`.

## Merge rule

No future positive registry entry should be accepted unless it contains an anti-seed block with the five required lines:

```text
false theorem if overstated:
known obstruction:
actual category:
missing structure:
strongest safe statement:
```
