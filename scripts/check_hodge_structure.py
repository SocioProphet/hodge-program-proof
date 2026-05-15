#!/usr/bin/env python3
"""Structural and negative-path guard for the Hodge Program repository.

This checker is intentionally narrow. It validates repository topology and
synthetic unsafe-promotion examples. It does not semantically scan all prose,
because the repo deliberately contains unsafe phrases inside anti-seed,
nonclaim, and forbidden-promotion contexts.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "README.md",
    "docs/anti-seed-hodge.md",
    "docs/claim-boundary.md",
    "docs/program-map.md",
    "docs/hodge-origin-registry.md",
    "docs/obstruction-registry.md",
    "docs/intake/heller-godel-proof-fabric-intake.md",
    "docs/registries/heller-godel-artifact-registry.md",
    "docs/scaffolds/hodge_bridge_requirements_scaffold.md",
    "docs/evaluations/hodge_eval_001_heller_godel_apparatus.md",
    "docs/strategy/hodge_strategy_spine.md",
    "scripts/check_claim_boundary.py",
]

PROGRAM_MAP_DEPENDENCIES = [
    "README.md",
    "docs/anti-seed-hodge.md",
    "docs/claim-boundary.md",
    "docs/hodge-origin-registry.md",
    "docs/obstruction-registry.md",
    "docs/intake/heller-godel-proof-fabric-intake.md",
    "docs/registries/heller-godel-artifact-registry.md",
    "docs/scaffolds/hodge_bridge_requirements_scaffold.md",
]

REGISTRY_REQUIRED_HEADER = (
    "| Source path in Heller-Godel | Artifact type | Classification | "
    "Evidence level | Safe use | Forbidden promotion |"
)

REQUIRED_REGISTRY_ENTRIES = [
    "docs/proofs/proof_class_moduli_requirements_scaffold.md",
    "docs/proofs/proof_class_moduli_scaffold_diagnostic.md",
    "docs/proofs/proof_class_moduli_construction_attempt.md",
    "docs/proofs/proof_class_moduli_parameter_feasibility.md",
    "docs/proofs/proof_class_moduli_stratified_registry.md",
]

REQUIRED_STRATEGY_PHRASES = [
    "No commitment to a next research direction",
    "registry row -> parameter space",
    "stratified registry -> moduli space",
    "finite monodromy -> Tate data",
    "Deligne unit -> algebraic cycle",
    "local regulator symbol -> Beilinson conjecture evidence",
]


@dataclass(frozen=True)
class UnsafePromotionPattern:
    label: str
    pattern: re.Pattern[str]


UNSAFE_PROMOTION_PATTERNS = [
    UnsafePromotionPattern(
        "Heller-Godel Hodge progress",
        re.compile(r"\bHeller[- ]Godel\b.*\b(proves|advances|progress)\b.*\bHodge\b", re.I | re.S),
    ),
    UnsafePromotionPattern(
        "Deligne unit algebraic cycle",
        re.compile(r"\bDeligne unit\b.*\b(gives|is|yields|produces)\b.*\balgebraic cycle\b", re.I | re.S),
    ),
    UnsafePromotionPattern(
        "finite monodromy Tate data",
        re.compile(r"\bfinite monodromy\b.*\b(is|gives|yields|produces)\b.*\bTate data\b", re.I | re.S),
    ),
    UnsafePromotionPattern(
        "comparison diagram motive",
        re.compile(r"\bcomparison diagram\b.*\b(is|gives|yields|produces)\b.*\bmotive\b", re.I | re.S),
    ),
    UnsafePromotionPattern(
        "regulator symbol Beilinson evidence",
        re.compile(r"\bregulator symbol\b.*\b(proves|is|gives|yields|produces)\b.*\bBeilinson\b", re.I | re.S),
    ),
    UnsafePromotionPattern(
        "M_phi constructed",
        re.compile(r"\bM_phi\b.*\b(is constructed|has been constructed|constructed)\b", re.I | re.S),
    ),
    UnsafePromotionPattern(
        "stratified registry moduli space",
        re.compile(r"\bstratified registry\b.*\b(is|gives|yields|produces)\b.*\bmoduli space\b", re.I | re.S),
    ),
    UnsafePromotionPattern(
        "weak registry projective structure",
        re.compile(r"\bweak registry\b.*\b(has|gives|yields|produces)\b.*\bprojective structure\b", re.I | re.S),
    ),
    UnsafePromotionPattern(
        "Catalan A1 implies Hodge class",
        re.compile(r"\bCatalan A1\b.*\b(implies|gives|yields|produces)\b.*\bHodge class\b", re.I | re.S),
    ),
    UnsafePromotionPattern(
        "bridge primitives satisfied",
        re.compile(r"\bbridge primitives\b.*\b(are|now|all)?\s*(satisfied|closed|complete)\b", re.I | re.S),
    ),
]

NEGATIVE_TEST_CASES = [
    "Heller-Godel proves Hodge progress.",
    "The Deligne unit gives an algebraic cycle.",
    "Finite monodromy is Tate data.",
    "A comparison diagram is a motive.",
    "The regulator symbol proves Beilinson evidence.",
    "M_phi has been constructed.",
    "The stratified registry is a moduli space.",
    "The weak registry has projective structure.",
    "Catalan A1 vocabulary gives a Hodge class.",
    "The bridge primitives are satisfied.",
]


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def fail(message: str, failures: list[str]) -> None:
    failures.append(message)


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def check_required_files(failures: list[str]) -> None:
    for file_path in REQUIRED_FILES:
        if not (ROOT / file_path).exists():
            fail(f"missing required structural file: {file_path}", failures)


def check_program_map(failures: list[str]) -> None:
    program_map = read("docs/program-map.md")
    for dep in PROGRAM_MAP_DEPENDENCIES:
        if dep not in program_map:
            fail(f"program map missing dependency reference: {dep}", failures)
    if "docs/strategy/hodge_strategy_spine.md" not in program_map:
        fail("program map missing strategy spine reference: docs/strategy/hodge_strategy_spine.md", failures)


def check_heller_godel_registry(failures: list[str]) -> None:
    registry = read("docs/registries/heller-godel-artifact-registry.md")
    if REGISTRY_REQUIRED_HEADER not in registry:
        fail("Heller-Godel artifact registry missing required table header", failures)
    for entry in REQUIRED_REGISTRY_ENTRIES:
        if entry not in registry:
            fail(f"Heller-Godel artifact registry missing required entry: {entry}", failures)

    table_lines = [
        line
        for line in registry.splitlines()
        if line.startswith("| `docs/") and not line.startswith("| ---")
    ]
    for line in table_lines:
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) != 6:
            fail(f"registry row does not have 6 cells: {line}", failures)
            continue
        if not cells[2]:
            fail(f"registry row missing classification: {line}", failures)
        if not cells[3]:
            fail(f"registry row missing evidence level: {line}", failures)
        if not cells[5]:
            fail(f"registry row missing forbidden promotion: {line}", failures)


def check_strategy_spine(failures: list[str]) -> None:
    spine = read("docs/strategy/hodge_strategy_spine.md")
    for phrase in REQUIRED_STRATEGY_PHRASES:
        if phrase not in spine:
            fail(f"strategy spine missing required phrase: {phrase}", failures)


def detect_unsafe_promotion(text: str) -> list[str]:
    return [pattern.label for pattern in UNSAFE_PROMOTION_PATTERNS if pattern.pattern.search(text)]


def check_negative_tests(failures: list[str]) -> None:
    for sample in NEGATIVE_TEST_CASES:
        matches = detect_unsafe_promotion(sample)
        if not matches:
            fail(f"negative-path sample was not rejected: {sample}", failures)

    safe_samples = [
        "This registry does not claim Heller-Godel proves Hodge progress.",
        "Finite monodromy must not be promoted to Tate data.",
        "The weak registry is not a moduli space.",
        "Bridge primitives are not satisfied by the current apparatus.",
    ]
    for sample in safe_samples:
        matches = detect_unsafe_promotion(sample)
        if matches:
            fail(f"safe nonclaim sample was rejected by {matches}: {sample}", failures)


def main() -> int:
    failures: list[str] = []
    check_required_files(failures)
    if not failures:
        check_program_map(failures)
        check_heller_godel_registry(failures)
        check_strategy_spine(failures)
        check_negative_tests(failures)

    if failures:
        for failure in failures:
            print(failure, file=sys.stderr)
        return 1

    print("Hodge structural and negative-path checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
