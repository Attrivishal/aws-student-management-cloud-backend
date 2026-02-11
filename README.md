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
↓
API Gateway (REST API)
↓
AWS Lambda (Serverless backend)
↓
Amazon RDS (PostgreSQL) – Private Subnet


**Key architectural decisions:**
- RDS runs in private subnets
- Lambda connects to RDS via VPC
- API Gateway exposes controlled endpoints
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

## 🔐 Security Design
- Database hosted in private subnets
- No public access to RDS
- Lambda accesses RDS via VPC + Security Groups
- IAM roles used instead of static credentials
- API Gateway controls external access

## 🔄 Features Implemented
✅ Student count retrieval using AWS Lambda  
✅ Database health check API  
✅ API Gateway integration  
✅ CloudWatch logging enabled  
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

## 🚀 Why This Project Is Industry-Ready
- Uses production-like AWS architecture
- Follows least-privilege security
- Separates concerns (API, DB, compute)
- Scalable and cost-efficient design
- Fully cloud-native

## 🔮 Future Enhancements
- Authentication using Amazon Cognito
- CI/CD with GitHub Actions
- Infrastructure as Code (Terraform)
- Read replicas for RDS
- Rate limiting and WAF
- Frontend integration

## Live Execution Proof 

THis project is fully deployed and tested on AWS. 
Here are some real screenshots proving live connectivity between API Gateway, AWS Lambda, EC2, and RDS PostgreSQL.
And all the screenshots are available in the `screenshots/` directory.

## API Testing (Postman)

The API Gateway endpoints were tested using postman to verify real-time connectivity between external clients and backend services.

The Screenshot below demonstrates:
-> Successful API Gateway invocation
-> AWS Lambda execution inside VPC
-> Live Data fetched form PostgreSQL RDS

see:
`screenshots/postman-api-gateway-health-check.png`

## 👤 Author
**Vishal Attri**  
Cloud  Enthusiast  
LinkedIn: https://www.linkedin.com/in/vishalattri/
