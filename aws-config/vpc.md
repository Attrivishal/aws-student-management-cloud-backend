# VPC Configuration

I created a custom VPC in the `us-east-1` region to securely isolate all backend
resources used in this project.

## VPC Details
- Region: us-east-1
- CIDR Block: 10.0.0.0/16

## Subnets

### Public Subnet
- Used for: EC2 instance (Flask backend)
- Public IP: Enabled
- Purpose: Allow external HTTP/HTTPS access to backend APIs

### Private Subnets
- Used for: AWS Lambda functions and Amazon RDS
- Public IP: Disabled
- Purpose: Protect database and internal services from direct internet access

## Routing
- Public subnet is connected to an Internet Gateway
- Private subnets do not have direct internet access
- Lambda connects to RDS internally inside the VPC

## Outcome
This setup ensures that:
- EC2 can be accessed publicly
- RDS remains fully private
- Lambda can securely access the database