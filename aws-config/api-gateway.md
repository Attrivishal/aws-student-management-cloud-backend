# API Gateway Configuration

Amazon API Gateway was used to expose backend services
as RESTful HTTP endpoints.

---

## Responsibilities

- Route HTTP requests to Lambda functions
- Handle request/response transformation
- Provide stage-based deployment (prod)
- Enable CloudWatch logging

---

## Challenges Faced

During setup, multiple issues were encountered:
- Missing Authentication Token errors
- Internal Server Errors with no logs
- CloudWatch logging misconfiguration

Resolving these required:
- Proper IAM role attachment
- Stage redeployment
- Correct access log destination ARN

These issues reflect real-world cloud debugging scenarios.
