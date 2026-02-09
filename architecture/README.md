# System Architecture Documentation

This folder documents the architectural design of the
**AWS Student Management Cloud Backend** project.

The goal of this architecture was to design a **secure, scalable, and production-aligned**
backend system using AWS-managed services while following cloud best practices.

---

## Architectural Goals

The system was designed with the following objectives:

- Keep the database isolated from the public internet
- Separate compute, networking, and data layers
- Support both serverless (Lambda) and server-based (EC2) workloads
- Enable observability and debugging through CloudWatch
- Follow least-privilege security principles

---

## Diagram Breakdown

### 1. System Architecture Diagram

This diagram shows the complete system at a high level:

- Client requests enter through **API Gateway**
- Requests are routed to:
  - AWS Lambda functions for lightweight operations
  - EC2-hosted Flask backend for traditional service patterns
- All data access is handled through **PostgreSQL RDS** hosted in private subnets

This hybrid approach demonstrates real-world architectures where
serverless and EC2-based systems coexist.

---

### 2. Network Flow Diagram

The network flow diagram explains how traffic moves securely through the system:

- Public internet traffic is allowed only to API Gateway and EC2
- Lambda functions operate inside the VPC using private networking
- RDS accepts traffic only from trusted security groups
- No direct internet access to the database is possible

This design prevents common security misconfigurations such as
publicly exposed databases.

---

### 3. Security Design Diagram

The security design focuses on defense-in-depth:

- Security Groups enforce strict inbound rules
- IAM Roles are used instead of static credentials
- Network boundaries isolate sensitive resources
- CloudWatch logging enables auditing and troubleshooting

These controls collectively reduce the attack surface
and align with production security standards.