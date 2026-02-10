# AWS Lambda Functions

This directory contains AWS Lambda functions
used to interact with the PostgreSQL RDS database.

Each function performs a **single, well-defined task**
and is exposed via API Gateway.

---

## Why Lambda Was Used

- To implement serverless database access
- To understand Lambda execution inside a VPC
- To learn API Gateway + Lambda integration
- To observe cold start and latency behavior

---

## Database Connectivity

- Lambda functions run inside the same VPC as RDS
- Database access is controlled using security groups
- psycopg2 is used via a Lambda Layer



## Execution Proof

The following screenshots shows a successful lambda execution connecting to a postgreSQL RDS instance inside a private subnet.

-> Database connection established
-> Student count fetched in real time
-> Execution latency measured

see:
`screenshots/lambda-health-check-success.png`
