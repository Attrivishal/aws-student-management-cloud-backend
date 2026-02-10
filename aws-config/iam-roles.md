# IAM Roles and Permissions

I used IAM roles instead of hardcoded credentials to securely grant permissions
to AWS services.

## Lambda Execution Role
- Permissions:
  - VPC access (CreateNetworkInterface, DescribeNetworkInterfaces)
  - CloudWatch Logs (for monitoring)
- No database credentials stored in code

## EC2 IAM Role
- Basic permissions for instance management and logging
- Database credentials provided using environment variables

## Security Practice
- No AWS credentials are hardcoded
- Least-privilege access is followed
- All secrets are managed using environment variables

## Outcome
This improves security and follows AWS best practices for production systems.