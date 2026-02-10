# System Architecture

This folder contains the architectural diagrams for the **AWS Student Management Cloud Backend** project.  
These diagrams explain how different AWS services and backend components interact with each other in a secure and scalable way.

The architecture was designed with a focus on:
- Secure networking
- Controlled database access
- Separation of concerns between services
- Real-world cloud backend practices

---

## 1. System Architecture Diagram

**File:** `01-system-architecture.png`

This diagram represents the overall high-level architecture of the project.

### Components involved:
- Client (Browser / Postman)
- Amazon API Gateway
- AWS Lambda Functions
- EC2 Instance (Flask Backend)
- Amazon RDS (PostgreSQL)
- Amazon VPC (Public & Private Subnets)

### Flow overview:
- Client requests are sent either to:
  - API Gateway (for Lambda-based APIs), or
  - EC2 public IP (for Flask backend APIs)
- Lambda functions and EC2 communicate with the PostgreSQL database hosted on Amazon RDS
- The database remains isolated inside private subnets

This diagram gives a complete bird’s-eye view of the system.

---

## 2. Network Flow Diagram

**File:** `02-network-flow.png`

This diagram explains how network traffic flows inside the AWS VPC.

### Key networking concepts shown:
- VPC with public and private subnets
- EC2 instance deployed in a public subnet
- RDS PostgreSQL deployed in private subnets
- Security Group–based communication

### Network flow:
1. Client sends request to API Gateway or EC2
2. API Gateway invokes Lambda functions
3. Lambda functions access RDS using private network routing
4. EC2 accesses RDS via security group rules
5. RDS never exposes a public endpoint

This diagram highlights how backend services securely access the database without exposing it to the internet.

---

## 3. Security Design Diagram

**File:** `03-security-design.png`

This diagram focuses on security controls applied across the system.

### Security mechanisms used:
- RDS deployed in private subnets
- No public access to PostgreSQL
- Security groups restricting inbound traffic
- IAM roles used for Lambda execution
- Environment variables used for database credentials
- CORS enabled only at backend level where required

### Security goals achieved:
- Database isolation
- Least-privilege access
- Controlled service-to-service communication
- No hardcoded secrets in application code

This diagram demonstrates how security was intentionally designed, not added later.

---

## Why These Diagrams Matter

These architectural diagrams document:
- How the system was planned before implementation
- How AWS services were connected in a real-world scenario
- How networking and security were handled professionally

They serve as technical documentation for anyone reviewing or extending the project.