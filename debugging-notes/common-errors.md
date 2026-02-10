# Common Issues Faced During Development

This file lists the **real issues I encountered** while building this project and
how I resolved them.

---

## 1. RDS Creation Failed Due to Subnet Configuration

**Issue**
- RDS instance creation failed initially.

**Root Cause**
- RDS requires a subnet group with **at least two subnets in different availability zones**.
- I initially selected subnets from the same AZ.

**Fix**
- Created a proper DB subnet group using subnets from **multiple availability zones**.
- Ensured all subnets belonged to the same VPC.

---

## 2. EC2 Could Not Connect to RDS PostgreSQL

**Issue**
- Flask backend on EC2 could not connect to RDS.
- psycopg2 connection timed out.

**Root Cause**
- RDS security group inbound rules were missing.
- EC2 security group was not allowed on PostgreSQL port 5432.

**Fix**
- Updated RDS inbound rules to allow traffic from EC2 security group on port 5432.
- Avoided opening the database to public IPs.

---

## 3. Lambda Unable to Access RDS

**Issue**
- Lambda function failed to connect to RDS even though credentials were correct.

**Root Cause**
- Lambda was not associated with the correct VPC.
- Lambda did not have access to the private subnets where RDS was deployed.

**Fix**
- Attached Lambda to the same VPC as RDS.
- Selected the correct private subnets and security group.

## 4. IAM Role and Permissions Issues

**Issue**
- Services failed even when networking and credentials were correct.
- Lambda execution failed silently or returned permission-related errors.
- EC2 behaved differently when accessed manually vs programmatically.

**Root Cause**
- IAM roles were missing or incorrectly attached.
- Required permissions were not granted explicitly.
- I initially underestimated how strict AWS IAM is.

**What I Learned**
- Every AWS service needs an **IAM role** to perform actions.
- Permissions are not shared automatically between services.
- Even if networking is correct, missing IAM permissions will break the system.

**Fix**
- Created dedicated IAM roles for:
  - AWS Lambda (execution role)
  - EC2 instance (instance role)
- Attached only required permissions (least privilege):
  - CloudWatch Logs access
  - VPC access for Lambda
  - RDS connectivity (network-level + role-based access)
- Removed all hardcoded credentials from code.

This helped me understand that **IAM is the backbone of AWS security**, not an optional configuration.