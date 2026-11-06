<!--
Draft status: Requires human review
Ticket: tickets/FLOW-101.md
API source: spec/openapi.yaml
Drafting rules: config/drafting-rules.md
Model: openai/gpt-oss-120b
Generated at: 2026-11-06T15:40:18+00:00
-->

> **Draft for review:** This document describes a
> proposed feature. It is not approved product documentation.

# Overview
This draft documents a proposed API for cancelling an automation job. The feature is described in JIRA ticket **FLOW-101** and is not present in the current OpenAPI specification. All details are therefore considered unverified until confirmed against the official API definition.

# Use Case
A user may start an automation job and later discover that the input data is incorrect or that the job is no longer needed. In such cases the user should be able to request that the job be cancelled before it completes, for example when a nightly transaction‑processing job is started with an invalid file.

# API Operation
**Endpoint (proposed)**:  

```
POST /jobs/{jobId}/cancel
```

**Purpose**:  
Submit a request to cancel the job identified by `jobId`.

# Request Details
| Element | Description |
|---------|-------------|
| **Path parameter** `jobId` | Identifier of the job to be cancelled. Must be a string that matches an existing job. |
| **HTTP method** | `POST` (as proposed). |
| **Request body** | The ticket does not specify a request payload. The body may be empty or may contain additional data; this must be confirmed. |
| **Headers** | Typical headers such as `Authorization` and `Content-Type` are expected, but exact requirements are not defined. |

**Example Request**

```http
POST https://api.flowops.example/v1/jobs/job-1001/cancel
Authorization: Bearer <access_token>
Content-Type: application/json

{}
```

*Note: The request body shown is an empty JSON object because the ticket does not define any fields. Verify the required payload.*

# Response Details
The proposed responses are:

| Status Code | Meaning | Response Body (proposed) |
|-------------|---------|--------------------------|
| **202** | Cancellation request accepted. The system will attempt to stop the job. | May include a confirmation object; not defined. |
| **404** | No job with the supplied `jobId` exists. | May include an error object; not defined. |
| **409** | The job cannot be cancelled (e.g., already completed). | May include an error object; not defined. |

**Example Successful Response (202)**

```http
HTTP/1.1 202 Accepted
Content-Type: application/json

{
  "message": "Cancellation request accepted"
}
```

*The exact response schema must be verified.*

# Important Considerations
- Accepting a cancellation request does **not** guarantee that the job has stopped. The job may already be in a terminal state or may finish before the cancellation takes effect.
- Clients should continue to poll the job status endpoint (`GET /jobs/{jobId}`) to confirm the final state.
- If a `409 Conflict` is returned, the job is in a state that cannot be cancelled (e.g., already completed or failed).
- Proper authentication and authorization are required; only users with permission to manage the job should be allowed to cancel it.

# Items Requiring Verification
1. **Endpoint existence** – Confirm that `POST /jobs/{jobId}/cancel` is defined in the official API.  
2. **HTTP method** – Verify that `POST` is the correct method; another method (e.g., `DELETE`) might be used.  
3. **Path parameter name and type** – Ensure the parameter is named `jobId` and is a string.  
4. **Request body** – Determine whether a payload is required and, if so, its schema.  
5. **Response status codes** – Validate that `202`, `404`, and `409` are the actual responses and that no additional codes are used.  
6. **Response schemas** – Obtain the exact JSON structures for success and error responses.  
7. **Headers and authentication** – Confirm required headers, authentication schemes, and any rate‑limiting rules.  
8. **Behavior semantics** – Clarify that a `202` response only indicates acceptance of the request, not completion of cancellation.  

The technical writer should verify each of these items against the finalized OpenAPI specification before the documentation can be published.
