
# FLOW-101: Add job cancellation support

## Issue Type
Story

## Status
Proposed

## Description

Users need an option to cancel an automation job when it is no longer required.

For example, a banking operations team may start a nightly transaction processing job and later realize that the input file contains incorrect data.

The team should be able to request cancellation before the job completes.

## Proposed API Change

Introduce a new endpoint:

`POST /jobs/{jobId}/cancel`

## Expected Behavior

- Accept a cancellation request for an existing job.
- Return HTTP 202 when the cancellation request is accepted.
- Return HTTP 404 when the specified job does not exist.
- Return HTTP 409 when the job cannot be cancelled.

## Documentation Requirements

- Explain when users may need to cancel a job.
- Document the proposed endpoint.
- Describe the expected responses.
- Explain that accepting a cancellation request does not guarantee that the job has stopped.

## Acceptance Criteria

- A documentation draft is prepared from this ticket.
- All proposed API behavior is identified as unverified until confirmed against the OpenAPI specification.
- The technical writer reviews the draft before publication.
