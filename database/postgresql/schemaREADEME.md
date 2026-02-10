## schema.sql

I created this file to define the database structure used in this project.
This schema represents the exact table that my backend services interact with.

The `students` table is designed to store student information submitted through
the backend APIs running on EC2 and AWS Lambda.

I used:
- `SERIAL` for automatic primary key generation
- `UNIQUE` constraint on email to prevent duplicate student entries
- `DEFAULT CURRENT_TIMESTAMP` to automatically track record creation time

This schema is used directly by:
- The Flask backend running on EC2
- AWS Lambda functions performing health checks and metrics queries

The schema is intentionally simple, clean, and production-ready.