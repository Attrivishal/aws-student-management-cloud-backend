# -------------------------------------
# Student Management Backend API Runs on EC2 and connects to aws RDS PostgreSQL
# Version: 2.0
# -------------------------------------
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

def get_db_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT")
    )

# Serve frontend from /frontend folder
@app.route('/')
def serve_frontend():
    return send_from_directory('frontend', 'index.html')

# Serve other static files from frontend folder
@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('frontend', path)

# API Documentation at /api
@app.route('/api')
def api_info():
    return jsonify({
        "message": "Student Management API",
        "status": "running",
        "version": "2.0",
        "endpoints": {
            "get_students": "GET /students",
            "add_student": "POST /students",
            "delete_student": "DELETE /students/<id>",
            "health": "GET /health"
        }
    })

@app.route('/health')
def health_check():
    try:
        # Test database connection
        conn = get_db_connection()
        conn.close()
        return jsonify({"status": "healthy", "database": "connected"})
    except Exception as e:
        # Still return 200, but show database is down
        return jsonify({"status": "healthy", "database": "disconnected", "error": str(e)})

@app.route('/students', methods=['GET'])
def get_students():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM students;")
        rows = cur.fetchall()
        cur.close()
        conn.close()

        # Convert to list of dictionaries for better JSON
        students = []
        for row in rows:
            students.append({
                'id': row[0],
                'name': row[1],
                'email': row[2],
                'course': row[3],
                'created_at': str(row[4]) if row[4] else None
            })
        return jsonify(students)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/students', methods=['POST'])
def add_student():
    try:
        data = request.json

        # Validate required fields
        if not all(k in data for k in ['name', 'email', 'course']):
            return jsonify({"error": "Missing required fields"}), 400

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO students (name, email, course) VALUES (%s, %s, %s)",
            (data['name'], data['email'], data['course'])
        )
        conn.commit()
        cur.close()
        conn.close()
        return {"message": "Student added successfully"}, 201
    except psycopg2.IntegrityError:
        return {"error": "Email already exists"}, 409
    except Exception as e:
        return {"error": str(e)}, 500

@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    try:
        conn = get_db_connection()
        cur = conn.cursor()

        # Check if student exists
        cur.execute("SELECT * FROM students WHERE id = %s", (student_id,))
        student = cur.fetchone()

        if not student:
            cur.close()
            conn.close()
            return {"error": "Student not found"}, 404

        # Delete the student
        cur.execute("DELETE FROM students WHERE id = %s", (student_id,))
        conn.commit()

        cur.close()
        conn.close()

        return {"message": f"Student with ID {student_id} deleted successfully"}, 200
    except Exception as e:
        return {"error": str(e)}, 500

if __name__ == '__main__':
    print("=" * 50)
    print("Starting Student Management API on port 5000")
    print("=" * 50)
    app.run(host='0.0.0.0', port=5000, debug=True)