
from pathlib import Path
import yaml

# Locate the project folders.
ROOT = Path(__file__).resolve().parents[1]
SPEC_FILE = ROOT / "spec" / "openapi.yaml"
OUTPUT_FILE = ROOT / "docs" / "generated-api.md"


def generate_docs():
    # Read the OpenAPI specification.
    with SPEC_FILE.open("r", encoding="utf-8") as file:
        spec = yaml.safe_load(file)

    title = spec["info"]["title"]
    version = spec["info"]["version"]

    lines = [
        f"# {title}",
        "",
        f"**API Version:** {version}",
        "",
        "## API Operations",
        "",
    ]

    # Read each endpoint and its supported methods.
    for path, methods in spec["paths"].items():
        for method, details in methods.items():
            if method.lower() not in {
                "get", "post", "put", "patch", "delete"
            }:
                continue

            lines.extend([
                f"## {method.upper()} {path}",
                "",
                details.get("summary", ""),
                "",
                details.get("description", "").strip(),
                "",
            ])

            # Add the response codes.
            responses = details.get("responses", {})
            if responses:
                lines.extend([
                    "### Responses",
                    "",
                    "| HTTP Code | Description |",
                    "|---|---|",
                ])

                for code, response in responses.items():
                    description = response.get("description", "")
                    lines.append(
                        f"| {code} | {description} |"
                    )

                lines.append("")

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(
        "\n".join(lines),
        encoding="utf-8"
    )

    print(f"Documentation generated: {OUTPUT_FILE}")


if __name__ == "__main__":
    generate_docs()
