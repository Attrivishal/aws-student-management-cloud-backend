# API Gateway Configuration

I used Amazon API Gateway as the public entry point for Lambda-based APIs.

## Configuration
- Type: REST API
- Methods: GET
- Integration: AWS Lambda
- Endpoint: /health
- Authorization: None (public for testing)

## Flow
Client → API Gateway → Lambda → RDS → Response

## Features
- Handles HTTPS traffic
- Enables CORS
- Acts as a secure abstraction layer for Lambda

## Outcome
API Gateway allows external clients to safely access backend functionality
without exposing internal infrastructure.