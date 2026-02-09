# Student Count Lambda

This Lambda function queries the PostgreSQL database
to return the total number of student records.

---

## What It Does

- Executes a COUNT query on the students table
- Returns the total number of records
- Confirms real-time data access via Lambda

---

## Why This Was Implemented

This function demonstrates:
- Read-only database access
- Real-time API-driven data retrieval
- Separation of concerns using small Lambda functions

It also confirms that data returned through API Gateway
is coming directly from the database and not hardcoded.



# Student Count Lambda Function

This AWS Lambda function connects to an RDS PostgreSQL database
and returns the total number of students stored in the `students` table.

## Purpose
- Validate Lambda → RDS connectivity
- Provide a lightweight, serverless read-only API
- Measure query latency

## Trigger
- Invoked via Amazon API Gateway

## Environment Variables
- DB_HOST
- DB_NAME
- DB_USER
- DB_PASSWORD
- DB_PORT

## Response
Returns total student count and execution latency in JSON format.