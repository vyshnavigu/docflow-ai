
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

## API Accuracy Rules

The OpenAPI specification is the source of truth for
the API operations currently documented.

A Jira ticket may describe a proposed feature, but it
does not confirm that the feature is implemented.

When preparing documentation:

1. Do not generate request examples unless the request
   structure is defined in the source documents.

2. Do not generate response examples unless the response
   fields and their values are supported by the source.

3. Do not assume that an API requires authentication,
   authorization headers, or a particular request body.

4. Do not introduce additional job states, error
   conditions, or system behavior without supporting
   information.

5. Do not recommend procedures that depend on
   functionality that has not been confirmed.

6. When the source does not provide enough information,
   identify what needs to be verified.

7. Clearly separate proposed functionality from
   implemented functionality.

8. Do not present an unverified API operation as
   available for customer use.

## Source Verification

Before preparing the draft, compare the Jira ticket
with the OpenAPI specification.

For each API operation, identify:

- Whether the operation exists in the specification.
- Which request parameters are defined.
- Which response codes are supported.
- Which response fields are defined.
- Which details are missing or require confirmation.

Do not fill missing information using assumptions
about common API design practices.

## Writing Style

Use clear and direct language.

Explain the purpose of a feature before providing
technical details.

Use practical examples when they are supported by
the source documents.

Avoid unnecessary technical terminology.

Do not use em dashes. Use commas, periods, or separate
sentences where appropriate.

Use correct grammar, punctuation, and sentence structure.

Do not repeat the same information unnecessarily.

## Draft Review Requirements

Before returning the draft:

1. Check every API example against the source.
2. Remove unsupported request and response examples.
3. Identify any statements that require confirmation.
4. Check that proposed features are clearly labelled.
5. Review terminology and writing style.
6. Add an Items Requiring Verification section.

If the API operation is not implemented, prepare
a proposed documentation draft for internal review.

Do not present the draft as approved documentation.

## Final Accuracy and Style Checks

Before returning a documentation draft:

1. Review each statement about product behavior.
   If the behavior is not supported by the source
   documents, remove it or identify it as an item
   requiring verification.

2. Do not recommend monitoring or verification
   procedures unless the API specification supports
   the procedure and the expected outcome.

3. Do not assume that cancellation introduces a new
   job status or that a running job can be interrupted.

4. Do not use the em dash character (—) anywhere in
   the generated documentation, including headings,
   tables, and verification items.

5. Check the complete draft for unsupported examples
   and statements before returning it.

6. Clearly distinguish information defined in the
   OpenAPI specification from proposed requirements
   described in Jira tickets.

7. Do not describe a proposed feature as available
   for customer use.


