# FlowOps Automation API

**API Version:** 1.0.0

The FlowOps API allows users to start
automation jobs and check their status.

## Base URL

`https://api.flowops.example/v1`

## API Operations

## POST /jobs

Start an automation job

Starts an automation job using the
specified workflow. The job is queued
for processing after the request is accepted.

### Request Body

| Field | Type | Required | Description |
|---|---|---|---|
| workflowId | string | Yes |  |

### Responses

| HTTP Code | Description |
|---|---|
| 202 | Job accepted for processing |

### HTTP 202 Response Fields

| Field | Type | Required | Description |
|---|---|---|---|
| jobId | string | No |  |
| status | string | No | Allowed values: pending, running, completed, failed |

## GET /jobs/{jobId}

Get automation job status



### Parameters

| Name | Location | Type | Required |
|---|---|---|---|
| jobId | path | string | Yes |

### Responses

| HTTP Code | Description |
|---|---|
| 200 | Job status retrieved successfully |
| 404 | Job not found |

### HTTP 200 Response Fields

| Field | Type | Required | Description |
|---|---|---|---|
| jobId | string | No |  |
| status | string | No | Allowed values: pending, running, completed, failed |
