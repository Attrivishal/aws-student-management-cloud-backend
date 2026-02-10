# AWS Student Management Cloud Backend

## 📌 Project Overview
This project is a cloud-native backend system built on AWS to manage and monitor student data using a secure, scalable, and production-style architecture.

It demonstrates how modern backend systems are designed using AWS Lambda, API Gateway, Amazon RDS (PostgreSQL), EC2, IAM, and VPC networking, focusing on security, private networking, and observability.

## 🎯 Problem Statement
In real-world applications, backend systems must:
- Securely store data in private databases
- Expose APIs without directly exposing the database
- Handle failures gracefully
- Provide health and monitoring endpoints
- Be scalable and cost-efficient
- Operate inside private networks
- Enable effective debugging and monitoring

This project solves these challenges using AWS-managed services and best practices.

## 🏗️ High-Level Architecture

**Request Flow:**
Client
├──> API Gateway
│ └──> AWS Lambda (inside VPC)
│ └──> Amazon RDS (PostgreSQL - Private Subnet)
│
└──> EC2 (Flask Backend)
└──> Amazon RDS (PostgreSQL - Private Subnet)

**Key Architectural Decisions:**
- RDS runs only in private subnets
- Lambda is attached to VPC for database access
- API Gateway exposes controlled public endpoints
- IAM roles manage permissions (no hardcoded secrets)
- EC2 Flask backend validates direct database connectivity

## 🧱 Technology Stack
- **Cloud Provider**: AWS
- **Compute**: AWS Lambda, EC2
- **API Layer**: Amazon API Gateway (REST)
- **Database**: Amazon RDS (PostgreSQL)
- **Networking**: VPC, Private & Public Subnets, Security Groups
- **Monitoring**: Amazon CloudWatch
- **Backend Framework**: Flask (EC2-based service)
- **Language**: Python
- **Version Control**: Git & GitHub

## 📂 Project Structure
aws-student-management-cloud-backend/
│
├── backend/
│ ├── lambda/
│ │ ├── health_check.py
│ │ ├── student_count.py
│ │ └── requirements.txt
│ │
│ └── flask-app/
│ ├── app.py
│ └── requirements.txt
│
├── database/
│ └── postgresql/
│ ├── schema.sql
│ ├── queries.sql
│ └── README.md
│
├── infrastructure/
│ ├── architecture.md
│ └── security.md
│
├── diagrams/
│ └── aws-architecture.png
│
├── screenshots/
│ └── (deployment & API proof images)
│
└── README.md

## ⚙️ Environment Configuration
```ENV
DB_HOST=your-rds-endpoint
DB_NAME=your_database_name
DB_USER=postgres
DB_PASSWORD=your_password
DB_PORT=5432
🔐 Security Design
PostgreSQL hosted in private subnets

No public access to RDS

Lambda and EC2 access RDS via security groups

IAM roles used for permissions (no secrets in code)

API Gateway controls all public access

Follows least-privilege security principles

🔄 Features Implemented
✅ Student count retrieval using AWS Lambda
✅ Database health check API
✅ API Gateway → Lambda integration
✅ CloudWatch logging for Lambda & API Gateway
✅ Secure VPC networking
✅ PostgreSQL schema design
✅ EC2-hosted Flask backend validation

📊 Monitoring & Observability
Lambda execution logs in CloudWatch

API Gateway access logs

Latency and invocation metrics

Error tracking for database connectivity issues

Real-time troubleshooting capabilities

🧪 Live Execution Proof
This project was fully deployed and tested on AWS in a live environment. All screenshots demonstrating connectivity between services are available in the screenshots/ directory.

🔍 API Testing (Postman)
The API Gateway endpoints were tested using Postman to verify real-time connectivity between external clients and backend services.

Verified:

✅ Successful API Gateway responses

✅ Lambda execution inside private VPC

✅ Live data fetched from PostgreSQL RDS

See: screenshots/postman-api-gateway-health-check.png

🧠 What I Learned From This Project
Designing secure AWS VPC architectures

Connecting Lambda to private RDS instances

Debugging real cloud networking and IAM issues

API Gateway routing and error handling

CloudWatch logging and tracing

Differences between serverless and server-based backends

Real-world IAM role usage

🚀 Why This Project Is Industry-Ready
Uses production-style AWS architecture

Follows least-privilege security principles

Clear separation of concerns (API, compute, database)

Scalable and cost-efficient design

Fully cloud-native deployment

Comprehensive monitoring and observability

🔮 Future Enhancements
Authentication using Amazon Cognito

CI/CD with GitHub Actions

Infrastructure as Code (Terraform)

Read replicas for RDS

Rate limiting and AWS WAF

Frontend integration

Auto-scaling policies

Disaster recovery setup

👤 Author
Vishal Attri
Cloud Engineering Enthusiast
🔗 LinkedIn: https://www.linkedin.com/in/vishalattri/
