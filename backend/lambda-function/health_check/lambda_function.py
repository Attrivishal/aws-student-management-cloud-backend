import json
import psycopg2
import time
import os

def lambda_handler(event, context):
    start = time.time()

    conn = psycopg2.connect(
        host=os.environ["DB_HOST"],
        database=os.environ["DB_NAME"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
        port=os.environ["DB_PORT"]
    )

    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM students;")
    total_students = cur.fetchone()[0]
    cur.close()
    conn.close()

    latency = round(time.time() - start, 2)

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps({
            "status": "healthy",
            "database": "postgres",
            "total_students": total_students,
            "latency_seconds": latency
        })
    }