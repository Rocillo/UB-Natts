from flask import Flask, jsonify, render_template
import psycopg2
from datetime import datetime

app = Flask(__name__)

# Database connection parameters
DB_HOST = 'localhost'
DB_NAME = 'teste-natts'
DB_USER = 'postgres'
DB_PASSWORD = 'postgres'

# Connect to the PostgreSQL database
def connect_db():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None

# Fetch workstation status
def fetch_workstation_status():
    conn = connect_db()
    if not conn:
        return []

    cursor = conn.cursor()
    try:
        query = """
        SELECT w.workstation_id, w.name AS workstation_name,
               op.name AS operator_name, ws.start_time, ws.end_time,
               CASE WHEN ws.end_time IS NULL THEN true ELSE false END AS active
        FROM Workstations w
        LEFT JOIN WorkSessions ws ON w.workstation_id = ws.workstation_id AND ws.is_done = FALSE
        LEFT JOIN Operators op ON ws.operator_id = op.operator_id
        WHERE ws.is_done = FALSE
        ORDER BY w.workstation_id;
        """
        cursor.execute(query)
        rows = cursor.fetchall()
        result = []
        for row in rows:
            result.append({
                'workstation_id': row[0],
                'workstation_name': row[1],
                'operator_name': row[2] if row[2] else 'None',
                'start_time': row[3].strftime('%Y-%m-%d %H:%M:%S') if row[3] else 'N/A',
                'active': row[5]
            })
        return result
    except Exception as e:
        print(f"Error fetching workstation status: {e}")
        return []
    finally:
        cursor.close()
        conn.close()

@app.route('/status')
def status():
    status = fetch_workstation_status()
    return jsonify(status)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)