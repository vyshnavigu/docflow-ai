# DocFlow AI: AI-Assisted Documentation Pipeline

## Overview

DocFlow AI is a personal proof-of-concept project that demonstrates how API documentation can be generated, validated, and maintained using Python, OpenAPI, GitHub Actions, and an AI model.

The project uses a fictional automation platform called FlowOps. It provides an API for starting automation jobs and retrieving their status.

The objective is to explore how documentation can be prepared from structured sources while using automated checks and human review to maintain accuracy.

## Why I Built This Project

Technical documentation needs to remain accurate as product features change. When API specifications are updated, the corresponding documentation must also be reviewed and updated.

AI can help prepare documentation drafts, but the generated content may include assumptions that are not supported by the source documents.

I created this project to test a workflow that combines automated documentation generation, AI-assisted drafting, quality checks, and technical writer review.

## Tools and Technologies

| Tool | Purpose |
|---|---|
| Python | Documentation generation and validation |
| OpenAPI | Define API operations and schemas |
| PyYAML | Read the API specification |
| Groq | Run the AI model for documentation drafting |
| GPT-OSS 120B | Prepare documentation drafts |
| GitHub | Version control and pull-request reviews |
| GitHub Actions | Run automated documentation checks |
| Markdown | Store documentation and review materials |
| Google Colab | Develop and test Python scripts |

## How the Project Works

### 1. Generate API Documentation

The Python generator reads the OpenAPI specification and creates a Markdown API reference.

It extracts endpoint descriptions, request fields, response codes, and schema information supported by the current generator.

### 2. Detect Documentation Changes

GitHub Actions runs the documentation generator and compares its output with the version committed to the repository.

If the generated content differs from the saved documentation, the drift check fails.

This indicates that the documentation requires review and an update.

### 3. Prepare AI-Assisted Documentation

A separate Python script reads a simulated Jira ticket, the OpenAPI specification, and the drafting rules.

It sends these sources to an AI model through Groq and saves the generated content as a Markdown draft.

The draft is marked for human review.

### 4. Review Generated Documentation

The technical writer compares the draft with the source documents.

The review checks whether API operations, request parameters, responses, examples, and product behavior are supported by the specification or approved requirements.

Unverified information must be corrected or identified before publication.

### 5. Run Automated Quality Checks

The project includes a Python checker that identifies selected documentation issues, such as unsupported API examples, specific unverified behavior statements, and punctuation that does not follow the project's writing rules.

GitHub Actions tests the checker using known failing and clean documentation samples.

### 6. Review Documentation Through Pull Requests

Documentation changes can be prepared in a separate Git branch and submitted through a pull request.

Automated validation runs before merging. A documentation review checklist supports the human review process.

## Testing and Troubleshooting

### Documentation Drift Detection

During testing, I changed an API description without updating the corresponding Markdown documentation.

The first drift check passed unexpectedly.

After investigating the repository, I found that the generated documentation had been uploaded to the wrong folder. Git was not tracking the file at the location used by the comparison command.

I corrected the file location and reran the workflow.

The check then detected the outdated documentation and failed as expected.

After updating the documentation, the workflow passed.

### AI-Generated Documentation Review

I used a simulated Jira ticket proposing a job cancellation endpoint.

The first AI-generated draft correctly identified the feature as proposed but also included unsupported request headers, a request body, and a response example.

I updated the drafting instructions and regenerated the documentation.

Some unsupported statements continued to appear in later drafts. This demonstrated that drafting instructions alone were not sufficient to ensure accuracy.

I then developed a Python quality checker to identify selected problems before human review.

## Evaluation Results

I tested the automated documentation checker using two controlled samples:

| Test | Purpose | Expected Result | Actual Result |
|---|---|---|---|
| Known-problem baseline | Verify that the checker identifies configured documentation violations | Fail | Passed the negative test by correctly rejecting the sample |
| Clean documentation fixture | Verify that the checker accepts content without the configured violations | Pass | Passed |

Both tests completed successfully in the GitHub Actions evaluation workflow.

### AI-Generated Draft Review

During testing, the AI-generated draft introduced information that was not supported by the source requirements, including authentication details and behaviour for an endpoint that had not been implemented.

I reviewed the draft and ran the automated checker. The latest generated draft still contained four flagged issues and did not pass validation.

This confirmed that the checker could identify some configured documentation problems. However, it does not verify every technical statement or guarantee that generated documentation is accurate.

## Human Review and Publication

AI-generated documentation is treated as a draft, not as approved content.

Before publication, the technical writer must:

1. Compare the draft against the approved API specification and source requirements.
2. Identify unsupported statements, assumed behaviour, and incomplete information.
3. Verify endpoint details, request and response examples, and error-handling instructions.
4. Review the content for clarity, consistency, and the intended audience.
5. Confirm that the documentation is ready for publication.

The repository includes a review checklist to support this process.

The checklist was added through a pull request with passing automated checks and self-review. It has not undergone independent technical approval.

## Current Limitations

DocFlow AI is a personal proof of concept developed using a fictional automation API.

- The OpenAPI specification describes only the implemented sample contract. The proposed cancellation endpoint is not part of the approved specification.
- The automated checker identifies a defined set of documentation violations. It does not perform complete factual verification.
- The evaluation workflow uses controlled fixtures. It does not establish the reliability of AI-generated documentation across different APIs or projects.
- The latest AI-generated draft still requires correction and review.
- The workflow does not automatically create pull requests, approve documentation, or publish AI-generated drafts.
- The project has not been tested or reviewed in a production environment.

## Next Steps

Future improvements could include:

- Expanding the validation rules to cover additional unsupported claims and documentation inconsistencies.
- Evaluating generated drafts against a larger set of test cases.
- Comparing drafts with approved OpenAPI specifications and requirements.
- Introducing an independent technical review stage.
- Exploring automated pull request creation while retaining human approval before publication.
