# Database Connection Timeout Issues

This file explains the **most frequent issue I faced** during this project.

---

## Timeout Between Backend and RDS

**Symptoms**
- Flask app and Lambda both showed database connection timeouts.
- No errors in credentials or SQL queries.

**Actual Causes**
- Security groups were not properly linked.
- RDS was in a private subnet and could not be accessed directly.
- EC2 inbound rules were correct, but RDS inbound rules were missing.

**Resolution**
- Verified EC2 and Lambda were inside the same VPC as RDS.
- Allowed PostgreSQL traffic (5432) only from trusted security groups.
- Confirmed subnet routing and VPC association.

This issue helped me understand that **most cloud failures are networking-related,
not code-related so we have to configure or fix them**.