# Lessons Learned

This project taught me important real-world AWS lessons:

- RDS requires multiple availability zones for subnet groups
- Private subnets improve security but require correct routing
- Security groups must be configured on BOTH sides (EC2 and RDS)
- Lambda networking inside a VPC is not automatic
- Database timeouts usually indicate network or security issues
- Cloud debugging requires understanding infrastructure, not just logs

These lessons came directly from hands-on troubleshooting, not theory.


## IAM Is Mandatory, Not Optional

One of the biggest takeaways from this project was understanding IAM roles:

- Every AWS service requires explicit permissions
- Lambda cannot access VPC or CloudWatch without an execution role
- EC2 should use instance roles instead of access keys
- Permissions must be granted intentionally and minimally and this is must.
- Missing IAM roles can look like network or application failures

This project made me comfortable working with IAM in real scenarios, not just theory.