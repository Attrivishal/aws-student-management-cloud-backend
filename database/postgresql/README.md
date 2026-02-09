PostgreSQL Database (Amazon RDS)
📌 Purpose of the Database
This PostgreSQL database stores student data for the AWS Student Management Cloud Backend project. It acts as the single source of truth for all student records accessed by backend services running on AWS.

🏗️ Hosting Details
Database Engine: PostgreSQL

AWS Service: Amazon RDS

Region: us-east-1

Network: Private Subnets (VPC)

Public Access: ❌ Disabled

The database is not directly accessible from the internet and can only be reached by authorized backend services within the VPC.

🗂️ Database Schema
The database contains a primary table named students, used to store student information.

📄 Schema definition is available in: schema.sql

students Table Structure
Column Name	Description
id	Primary key
name	Student name
email	Unique email address
course	Enrolled course
created_at	Record creation timestamp
🔄 Data Access Pattern
This PostgreSQL database is accessed by multiple backend components:

1️⃣ Flask Backend (EC2)
Fetch student records

Insert new students

Delete existing students

2️⃣ AWS Lambda Functions
Database health check verification

Counting total number of student records

All database connections use environment variables for credentials and network configuration.

🧾 SQL Queries
Common SQL operations used by backend services are documented in queries.sql.

These include:

Insert student records

Fetch all students

Delete student records

Count total student entries

🔐 Security Considerations
RDS instance deployed in private subnets

No public IP assigned to the database

Access restricted using security groups

Only trusted EC2 and Lambda resources can connect

Database credentials are never hardcoded

Credentials are injected using environment variables

📚 Key Learnings
Designing a relational database schema using PostgreSQL

Deploying a secure PostgreSQL database using Amazon RDS

Connecting RDS with EC2 and AWS Lambda inside a private VPC

Applying security best practices using subnets and security groups

✅ Summary
This database layer provides a secure, scalable, and production-style persistence layer for the project and integrates cleanly with both EC2-based services and serverless AWS Lambda functions.