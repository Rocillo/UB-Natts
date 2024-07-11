import psycopg2
import keyboard
from datetime import datetime
import threading

# Database connection parameters
DB_HOST = 'localhost'
DB_NAME = 'teste-natts'
DB_USER = 'postgres'
DB_PASSWORD = 'postgres'

# Length of the employee number (for example, 5 digits)
EMPLOYEE_NUMBER_LENGTH = 5

# Global buffer for the employee number
employee_number_buffer = ""

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

# Insert a new work session into the database
def insert_work_session(conn, employee_number):
    cursor = conn.cursor()
    try:
        # Fetch operator_id using employee_number
        cursor.execute("SELECT operator_id FROM Operators WHERE employee_number = %s", (employee_number,))
        operator_id = cursor.fetchone()
        
        if operator_id:
            operator_id = operator_id[0]
            # Assuming a workstation_id is known or provided (for example, 1)
            workstation_id = 2
            start_time = datetime.now()

            cursor.execute(
                "INSERT INTO WorkSessions (operator_id, workstation_id, start_time) VALUES (%s, %s, %s)",
                (operator_id, workstation_id, start_time)
            )
            conn.commit()
            print(f"New work session started for employee number: {employee_number}")
        else:
            print(f"No operator found with employee number: {employee_number}")

    except Exception as e:
        conn.rollback()
        print(f"Error inserting work session: {e}")
    finally:
        cursor.close()

# Function to handle keyboard input
def handle_keyboard_input(event):
    global employee_number_buffer
    if event.name.isdigit():
        employee_number_buffer += event.name
        if len(employee_number_buffer) == EMPLOYEE_NUMBER_LENGTH:
            conn = connect_db()
            if conn:
                insert_work_session(conn, employee_number_buffer)
                conn.close()
            employee_number_buffer = ''  # Reset the buffer after processing
    elif event.name == 'backspace':
        employee_number_buffer = employee_number_buffer[:-1]

# Function to start the keyboard listener in a separate thread
def start_keyboard_listener():
    keyboard.on_press(handle_keyboard_input)
    keyboard.wait('esc')  # Press 'esc' to stop the program

#Function to update de Sessions
def end_work_session(conn, session_id):
    cursor = conn.cursor()
    try:
        end_time = datetime.now()
        cursor.execute(
            "UPDATE WorkSessions SET end_time = %s, is_done = TRUE WHERE session_id = %s",
            (end_time, session_id)
        )
        conn.commit()
        print(f"Work session {session_id} ended at {end_time}.")
    except Exception as e:
        conn.rollback()
        print(f"Error ending work session: {e}")
    finally:
        cursor.close()


# Main function
def main():
    global employee_number_buffer
    employee_number_buffer = ''
    print("Listening for keyboard input (press 'esc' to exit)...")
    listener_thread = threading.Thread(target=start_keyboard_listener)
    listener_thread.start()
    listener_thread.join()

if __name__ == "__main__":
    main()