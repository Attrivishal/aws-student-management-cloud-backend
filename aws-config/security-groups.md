# Security Group Strategy

Security Groups were used as the primary network firewall mechanism
to control traffic between services.

---

## Database Security Group

Inbound Rules:
- PostgreSQL (5432) allowed only from:
  - EC2 application security group
  - Lambda function security group

Outbound Rules:
- Restricted to required destinations only

---

## Why Security Groups Were Critical

Several connectivity issues (timeouts, refused connections)
were encountered during development.

Resolving these issues required a clear understanding of:
- Source vs destination security groups
- Stateful firewall behavior
- Inbound vs outbound rule precedence

These lessons are documented in the debugging-notes folder.
