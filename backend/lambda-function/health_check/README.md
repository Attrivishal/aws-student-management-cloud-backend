# Database Health Check Lambda

This Lambda function verifies whether the PostgreSQL RDS
instance is reachable and operational.

---

## What It Does

- Attempts a connection to PostgreSQL
- Measures connection latency
- Returns database status and metadata

---

## Why This Exists

This function was created to:
- Confirm RDS connectivity from Lambda
- Debug VPC and security group issues
- Validate API Gateway → Lambda → RDS flow

---

## Output

Returns a JSON response containing:
- Database status
- PostgreSQL version
- Connection latency
- Timestamp


# RDS Health Check Lambda Function

This Lambda function performs real-time health checks on a PostgreSQL
database hosted on Amazon RDS.

## Purpose
- Verify database connectivity
- Measure query latency
- Validate application data availability
- Provide serverless monitoring without EC2 dependency

## Function Behavior
- Connects to RDS using environment variables
- Executes a lightweight COUNT query
- Returns database health status and latency

## Environment Variables
- DB_HOST
- DB_NAME
- DB_USER
- DB_PASSWORD
- DB_PORT

## Output Example
```json
{
  "status": "healthy",
  "database": "postgres",
  "total_students": 3,
  "latency_seconds": 0.39
}