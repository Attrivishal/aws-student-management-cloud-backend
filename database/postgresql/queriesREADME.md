## queries.sql

I created this file to document all SQL queries that are actually executed
by my backend services.

These queries are used by:
- Flask APIs running on an EC2 instance
- AWS Lambda functions connected to PostgreSQL RDS

The queries include:
- Inserting new student records
- Fetching all students
- Deleting students by ID
- Counting total records for monitoring
- Fetching the latest student entry timestamp

This file acts as a reference for understanding how the application
interacts with the database and helps in debugging and future enhancements.
