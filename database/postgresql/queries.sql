-- queries.sql
-- SQL queries used by backend services

--  Here i used a simple students table for demonstration purposes. You can replace it with your actual table and fields.

--Using PostgreSQL syntax for creating a students table

-- Insert a new student
INSERT INTO students (name, email, course)
VALUES ('Vishal Attri', 'vishal@example.com', 'Cloud Computing');

-- Fetch all students
SELECT * FROM students;

-- Fetch a student by ID
SELECT * FROM students WHERE id = 1;

-- Delete a student by ID
DELETE FROM students WHERE id = 1;

-- Count total students (used by Lambda)
SELECT COUNT(*) FROM students;

-- Fetch latest student record
SELECT created_at
FROM students
ORDER BY created_at DESC
LIMIT 1;