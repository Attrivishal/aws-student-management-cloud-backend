# IAM Roles and Permissions

IAM roles were created to allow AWS services to communicate securely
without using static credentials.

---

## Roles Implemented

### Lambda Execution Role
- VPC access permissions
- CloudWatch logging permissions
- Minimal database access scope

### API Gateway Logging Role
- Permission to publish logs to CloudWatch
- Required to debug integration issues

---

## Security Principle

The project strictly follows the **Principle of Least Privilege**:
each role has only the permissions required to function.
