
<!-- Draft status: Requires human review -->

# Job Cancellation Support (Proposed)

## Overview

FLOW-101 proposes adding a job cancellation operation
to the FlowOps Automation API.

The cancellation operation is not defined in the
current OpenAPI specification.

## Use Case

A banking operations team may need to cancel a job
after discovering that the input file contains
incorrect transaction data.

## Proposed API Operation

The ticket proposes the following operation:

`POST /jobs/{jobId}/cancel`

This operation is not currently available in the
documented API.

## Items Requiring Verification

The following information must be confirmed:

- Implementation status of the proposed endpoint.
- Request parameters and required headers.
- Request and response schemas.
- Expected cancellation behavior.
- Method for confirming that cancellation is complete.

This draft requires technical review before publication.
