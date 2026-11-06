
# Documentation Drafting and Review Rules

## Purpose

These rules define how documentation drafts are prepared from
product requirements, Jira tickets, and OpenAPI specifications.

The objective is to prepare accurate documentation while
identifying information that requires technical review.

## Source Documents

Use the following sources:

1. OpenAPI specification for confirmed API operations.
2. Jira tickets for proposed features and requirements.
3. Existing documentation for terminology and structure.

Do not assume that a proposed feature is available in the
product unless it is confirmed in the OpenAPI specification
or another approved implementation source.

## Drafting Rules

1. Use clear and direct language.
2. Explain the purpose of the feature before describing
   the procedure or API operation.
3. Include practical examples where they help the reader.
4. Do not invent endpoints, parameters, response fields,
   or product behavior.
5. Clearly identify proposed or unverified functionality.
6. Do not describe an accepted request as a completed action
   unless the source confirms that behavior.
7. Use consistent terminology throughout the documentation.
8. Do not use em dashes.
9. Avoid unnecessary promotional language.
10. Identify missing information that requires confirmation.

## Required Draft Structure

Each feature documentation draft should include:

1. Overview
2. Use Case
3. API Operation
4. Request Details
5. Response Details
6. Important Considerations
7. Items Requiring Verification

If the source does not provide sufficient information for
a section, state that the details must be confirmed.

## Human Review

A technical writer must verify:

- Whether the feature is implemented.
- Whether the endpoint matches the OpenAPI specification.
- Whether request parameters and responses are accurate.
- Whether the examples match the actual product behavior.
- Whether terminology and instructions are consistent.
- Whether the document is ready for publication.

## Publication Rule

AI-generated drafts must not be published as confirmed
product documentation until the required review is complete.

Drafts containing unverified behavior must remain separate
from published documentation.
