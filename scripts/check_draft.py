
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]

DEFAULT_DRAFT = ROOT / "drafts" / "FLOW-101-draft.md"


def check_draft(path):
    text = path.read_text(encoding="utf-8")
    findings = []

    # Check the publication status.
    if "Draft status: Requires human review" not in text:
        findings.append(
            "Missing human review status."
        )

    # Check for dash characters used as separators.
    if "\u2014" in text:
        findings.append(
            "Em dash found in documentation."
        )

    if "\u2013" in text:
        findings.append(
            "En dash found. Review punctuation and writing style."
        )

    # Check for executable examples of the proposed endpoint.
    if re.search(
        r"curl\s+.*(?:/cancel|jobs/)",
        text,
        re.IGNORECASE
    ):
        findings.append(
            "Executable API example requires verification."
        )

    # Flag claims about unconfirmed behavior for human review.
    behavior_patterns = [
        r"system may need time",
        r"jobs may be non.interruptible",
        r"clients should poll",
        r"status should be checked separately",
    ]

    for pattern in behavior_patterns:
        if re.search(pattern, text, re.IGNORECASE):
            findings.append(
                f"Unverified behavior requires review: {pattern}"
            )

    print(f"\nReviewing: {path.name}")

    if findings:
        print("\nQuality check findings:\n")

        for number, finding in enumerate(findings, 1):
            print(f"{number}. {finding}")

        print(
            f"\nResult: FAILED ({len(findings)} findings)"
        )
        return False

    print("\nNo configured rule violations detected.")
    print("Automated checks passed. Human review is still required.")
    return True


if __name__ == "__main__":
    path = (
        Path(sys.argv[1])
        if len(sys.argv) > 1
        else DEFAULT_DRAFT
    )

    if not path.exists():
        print(f"Draft not found: {path}")
        sys.exit(1)

    sys.exit(0 if check_draft(path) else 1)
