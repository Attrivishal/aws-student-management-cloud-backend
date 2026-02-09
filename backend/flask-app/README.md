# Flask Backend Application (EC2)

This Flask application was deployed on an EC2 instance
to test direct backend-to-database connectivity.

---

## Purpose

The Flask app was created to:
- Verify PostgreSQL RDS connectivity from EC2
- Expose a `/health` endpoint for connection testing
- Understand how EC2 networking interacts with private RDS instances

---

## Environment

- EC2 instance running in a public subnet
- Application bound to `0.0.0.0` on port `5000`
- PostgreSQL RDS located in private subnets
- Access controlled using security groups

---

## Key Observations

- Database access depends entirely on correct security group rules
- Binding Flask to `127.0.0.1` prevents external access
- Connection timeouts usually indicate networking or security issues
