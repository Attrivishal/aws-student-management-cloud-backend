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
