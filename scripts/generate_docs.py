
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
SPEC_FILE = ROOT / "spec" / "openapi.yaml"
OUTPUT_FILE = ROOT / "docs" / "generated-api.md"


def resolve_schema(schema, spec):
    """Resolve a schema reference from the OpenAPI specification."""
    if "$ref" in schema:
        reference = schema["$ref"]
        if not reference.startswith("#/components/schemas/"):
            raise ValueError(f"Unsupported schema reference: {reference}")

        name = reference.split("/")[-1]
        return spec["components"]["schemas"][name]

    return schema


def add_schema_table(lines, schema, spec):
    """Add a table describing the schema fields."""
    schema = resolve_schema(schema, spec)
    properties = schema.get("properties", {})
    required = schema.get("required", [])

    if not properties:
        return

    lines.extend([
        "| Field | Type | Required | Description |",
        "|---|---|---|---|",
    ])

    for field, details in properties.items():
        field_type = details.get("type", "object")
        is_required = "Yes" if field in required else "No"
        description = details.get("description", "")

        if "enum" in details:
            values = ", ".join(details["enum"])
            description = f"{description} Allowed values: {values}".strip()

        lines.append(
            f"| {field} | {field_type} | {is_required} | {description} |"
        )

    lines.append("")


def generate_docs():
    """Generate API documentation from the OpenAPI specification."""
    with SPEC_FILE.open("r", encoding="utf-8") as file:
        spec = yaml.safe_load(file)

    info = spec["info"]
    servers = spec.get("servers", [])

    lines = [
        f"# {info['title']}",
        "",
        f"**API Version:** {info['version']}",
        "",
        info.get("description", "").strip(),
        "",
    ]

    if servers:
        lines.extend([
            "## Base URL",
            "",
            f"`{servers[0]['url']}`",
            "",
        ])

    lines.extend(["## API Operations", ""])

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

            parameters = details.get("parameters", [])

            if parameters:
                lines.extend([
                    "### Parameters",
                    "",
                    "| Name | Location | Type | Required |",
                    "|---|---|---|---|",
                ])

                for parameter in parameters:
                    lines.append(
                        f"| {parameter['name']} | "
                        f"{parameter['in']} | "
                        f"{parameter.get('schema', {}).get('type', 'string')} | "
                        f"{'Yes' if parameter.get('required') else 'No'} |"
                    )

                lines.append("")

            request_body = details.get("requestBody", {})
            request_content = request_body.get(
                "content", {}
            ).get("application/json", {})

            if "schema" in request_content:
                lines.extend(["### Request Body", ""])
                add_schema_table(
                    lines, request_content["schema"], spec
                )

            responses = details.get("responses", {})

            if responses:
                lines.extend([
                    "### Responses",
                    "",
                    "| HTTP Code | Description |",
                    "|---|---|",
                ])

                for code, response in responses.items():
                    lines.append(
                        f"| {code} | "
                        f"{response.get('description', '')} |"
                    )

                lines.append("")

                for code, response in responses.items():
                    content = response.get("content", {})
                    json_response = content.get(
                        "application/json", {}
                    )

                    if "schema" in json_response:
                        lines.extend([
                            f"### HTTP {code} Response Fields",
                            "",
                        ])

                        add_schema_table(
                            lines, json_response["schema"], spec
                        )

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(
        "\n".join(lines).rstrip() + "\n",
        encoding="utf-8"
    )

    print(f"Documentation generated: {OUTPUT_FILE}")


if __name__ == "__main__":
    generate_docs()
