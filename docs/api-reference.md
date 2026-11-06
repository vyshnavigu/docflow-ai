
# FlowOps Automation API Reference

## Overview

The FlowOps Automation API allows applications to start automation jobs and check their execution status.

For example, a banking application may use an automation job to process transaction files every night. Once the job starts, the application can check whether the process is still running or has completed.

This API provides two operations:

- Start an automation job.
- Retrieve the status of an automation job.

## Base URL

`https://api.flowops.example/v1`

**Note:** This URL is used for demonstration purposes. It does not connect to a live API.

## Start an automation job

**Endpoint:** `POST /jobs`

Use this endpoint to start an automation job for a specified workflow.

### Request body

| Field | Type | Required | Description |
|---|---|---|---|
| workflowId | string | Yes | Identifies the workflow to execute. |

### Example request

```json
{
  "workflowId": "nightly-transactions"
}
```

### Response

**HTTP 202: Job accepted for processing**

```json
{
  "jobId": "job-1001",
  "status": "running"
}
```

A successful response indicates that the job has been accepted for processing. It does not mean that the job has completed.

## Get automation job status

**Endpoint:** `GET /jobs/{jobId}`

Use this endpoint to retrieve the current status of an automation job.

### Path parameter

| Parameter | Type | Required | Description |
|---|---|---|---|
| jobId | string | Yes | Identifies the automation job. |

### Example request

`GET /jobs/job-1001`

### Response

**HTTP 200: Job status retrieved successfully**

```json
{
  "jobId": "job-1001",
  "status": "running"
}
```

### Job status values

| Status | Description |
|---|---|
| pending | The job is waiting to start. |
| running | The job is currently executing. |
| completed | The job has completed. |
| failed | The job did not complete successfully. |

### Error response

**HTTP 404: Job not found**

The requested job could not be found.

## Important considerations

- A successful job submission does not indicate that processing has completed.
- Check the job status to determine the current execution state.
- Use the `jobId` returned when starting a job to retrieve its status.
- This documentation is based on a fictional API specification created for the DocFlow AI project.
