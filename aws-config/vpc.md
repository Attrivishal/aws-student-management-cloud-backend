# VPC and Networking Design

A dedicated Virtual Private Cloud (VPC) was created to isolate
all backend resources from other AWS workloads.

---

## Network Structure

The VPC is divided into multiple subnets:

### Public Subnets
- EC2 instance hosting the Flask application
- API Gateway endpoints
- Internet Gateway attached for outbound access

### Private Subnets
- PostgreSQL RDS instance
- No direct internet routing
- Accessible only through security group rules

---

## Why This Matters

Placing the database in a private subnet ensures:

- No accidental public exposure
- Protection from direct port scanning attacks
- Access control enforced at the network level

This design mirrors how production-grade backend systems
are deployed in enterprise environments.
