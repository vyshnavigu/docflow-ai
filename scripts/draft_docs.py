
from pathlib import Path
from datetime import datetime, timezone
import os
import yaml
from groq import Groq

# Locate the project files.
ROOT = Path(__file__).resolve().parents[1]

TICKET_FILE = ROOT / "tickets" / "FLOW-101.md"
SPEC_FILE = ROOT / "spec" / "openapi.yaml"
RULES_FILE = ROOT / "config" / "drafting-rules.md"
OUTPUT_FILE = ROOT / "drafts" / "FLOW-101-draft.md"

MODEL = "openai/gpt-oss-120b"


def read_file(path):
    return path.read_text(encoding="utf-8")


def create_draft():
    # Check that the API key is available.
    if not os.getenv("GROQ_API_KEY"):
        raise RuntimeError(
            "GROQ_API_KEY is missing. "
            "Configure it securely before running the script."
        )

    # Read the source documents.
    ticket = read_file(TICKET_FILE)
    specification = read_file(SPEC_FILE)
    rules = read_file(RULES_FILE)

    # Check whether the proposed operation exists.
    spec = yaml.safe_load(specification)
    cancellation = (
        spec.get("paths", {})
        .get("/jobs/{jobId}/cancel", {})
        .get("post")
    )

    feature_confirmed = cancellation is not None

    print("Source files loaded successfully.")
    print(f"Cancellation endpoint defined: {feature_confirmed}")

    # Prepare the instructions for the model.
    instructions = f"""
You are preparing a technical documentation draft.

Follow these documentation rules:

{rules}

The ticket describes a proposed feature.
The OpenAPI specification represents the currently
documented API.

Cancellation endpoint defined in OpenAPI:
{feature_confirmed}

Treat the feature as unverified unless the provided
sources establish that it has been implemented.

Do not invent implementation details.

Use clear language, correct grammar and punctuation,
and practical examples. Do not use em dashes.

Include an Items Requiring Verification section.

Return Markdown only.
"""

    source_content = f"""
JIRA TICKET:
{ticket}

CURRENT OPENAPI SPECIFICATION:
{specification}
"""

    client = Groq()

    response = client.chat.completions.create(
        model=MODEL,
        temperature=0.2,
        messages=[
            {
                "role": "system",
                "content": instructions
            },
            {
                "role": "user",
                "content": source_content
            }
        ]
    )

    draft = response.choices[0].message.content

    if not draft or not draft.strip():
        raise RuntimeError("The model returned an empty draft.")

    # Record the sources used to prepare the draft.
    generated_at = datetime.now(
        timezone.utc
    ).isoformat(timespec="seconds")

    header = f"""<!--
Draft status: Requires human review
Ticket: tickets/FLOW-101.md
API source: spec/openapi.yaml
Drafting rules: config/drafting-rules.md
Model: {MODEL}
Generated at: {generated_at}
-->

> **Draft for review:** This document describes a
> proposed feature. It is not approved product documentation.

"""

    OUTPUT_FILE.parent.mkdir(
        parents=True, exist_ok=True
    )

    OUTPUT_FILE.write_text(
        header + draft.strip() + "\n",
        encoding="utf-8"
    )

    print(f"Draft saved to: {OUTPUT_FILE}")
    print("Human review required before publication.")


if __name__ == "__main__":
    create_draft()
