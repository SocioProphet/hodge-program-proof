#!/usr/bin/env python3
"""CI guard for the Hodge anti-seed and claim-boundary doctrine."""

from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
ANTI_SEED = ROOT / "docs" / "anti-seed-hodge.md"
CLAIM_BOUNDARY = ROOT / "docs" / "claim-boundary.md"

REQUIRED_FILES = [README, ANTI_SEED, CLAIM_BOUNDARY]

REQUIRED_README_PHRASES = [
    "Everything in this repo is treated as Hodge-originated",
    "preserve origin, classify distance, prevent bastardization",
    "Anti-seed first",
    "does **not** claim a proof of the Hodge conjecture",
    "does **not** assert algebraicity",
]

REQUIRED_ANTI_SEED_PHRASES = [
    "Anti-seed comes before seed",
    "Integral Hodge is false",
    "Compact Kähler is not enough",
    "Deligne cohomology is not algebraicity",
    "Torsion shadows are not Tate data",
    "Comparison diagrams are not motives",
    "Regulator symbols are not regulator conjectures",
    "Hodge-origin is not Hodge-proof",
    "No positive Hodge-origin registry entry should be merged until it names its anti-seed failure mode",
]

REQUIRED_CLAIM_BOUNDARY_PHRASES = [
    "Preserve origin. Classify distance. Do not bastardize",
    "core-hodge",
    "hodge-arithmetic",
    "hodge-method",
    "hodge-fallout",
    "Hodge-originated material -> proof of Hodge",
    "Deligne cohomology class -> algebraic cycle",
    "finite monodromy / torsion character -> Tate or Mumford–Tate result",
    "No item in this repository currently proves, advances, or materially attacks the Hodge conjecture",
]


def missing_phrases(text: str, phrases: list[str], label: str) -> list[str]:
    return [f"missing {label}: {phrase}" for phrase in phrases if phrase not in text]


def main() -> int:
    failures: list[str] = []
    for path in REQUIRED_FILES:
        if not path.exists():
            failures.append(f"missing required file: {path.relative_to(ROOT)}")

    if failures:
        for failure in failures:
            print(failure, file=sys.stderr)
        return 1

    readme_text = README.read_text(encoding="utf-8")
    anti_seed_text = ANTI_SEED.read_text(encoding="utf-8")
    claim_boundary_text = CLAIM_BOUNDARY.read_text(encoding="utf-8")

    failures.extend(missing_phrases(readme_text, REQUIRED_README_PHRASES, "README boundary phrase"))
    failures.extend(missing_phrases(anti_seed_text, REQUIRED_ANTI_SEED_PHRASES, "anti-seed phrase"))
    failures.extend(missing_phrases(claim_boundary_text, REQUIRED_CLAIM_BOUNDARY_PHRASES, "claim-boundary phrase"))

    if failures:
        for failure in failures:
            print(failure, file=sys.stderr)
        return 1

    print("Hodge anti-seed and claim-boundary guards passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
