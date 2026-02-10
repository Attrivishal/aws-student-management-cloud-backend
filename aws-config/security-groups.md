# Security Group Configuration

I configured separate security groups to tightly control traffic between EC2,
Lambda, and Amazon RDS.

## RDS Security Group
- Inbound:
  - PostgreSQL (5432)
  - Source: EC2 Security Group and Lambda Security Group
- Outbound:
  - All traffic (default)

RDS does not allow public access and only accepts connections from trusted
backend services.

## EC2 Security Group
- Inbound:
  - HTTP (80)
  - HTTPS (443)
  - Custom port (5001) for Flask backend
- Outbound:
  - PostgreSQL (5432) to RDS

## Lambda Security Group
- Inbound:
  - Managed internally by AWS
- Outbound:
  - PostgreSQL (5432) to RDS

## Outcome
This setup ensures:
- Database access is restricted
- No public traffic reaches RDS
- Only backend services can communicate with the database