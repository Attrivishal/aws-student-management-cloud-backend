# Backend Implementation

This folder contains the backend components of the
AWS Student Management Cloud Backend project.

The backend was intentionally built using **two approaches**:

1. A traditional **Flask application running on EC2**
2. **AWS Lambda functions** exposed via API Gateway

The purpose was to understand how different backend execution models
interact with the same PostgreSQL RDS database in a real AWS environment.

---

## Components Overview

### 1. Flask Application (EC2-based)
- Runs on an EC2 instance in a public subnet
- Connects to PostgreSQL RDS hosted in private subnets
- Used for testing database connectivity and backend behavior
- Demonstrates VM-based backend architecture

### 2. AWS Lambda Functions (Serverless)
- Runs inside a VPC
- Connects securely to the same PostgreSQL RDS instance
- Exposed using API Gateway
- Used for lightweight database queries and health checks

---

## Key Learning Outcome

This backend setup helped in understanding:
- EC2 vs Lambda execution differences
- VPC networking and security group behavior
- Database connectivity troubleshooting
- Real-world cloud debugging scenarios
