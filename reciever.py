import socket
import psycopg2
import sys
import signal
from datetime import datetime

# Server addressing
HOST = 'localhost'
PORT = 5489

# DB connection
try:
    db_conn = psycopg2.connect(dbname='homedata', user='postgres', password='*1Ananthu', host='localhost')
    cursor = db_conn.cursor()
except psycopg2.Error as e:
    print(f"Error connecting to the database: {e}")
    sys.exit(1)

def handle_client(connection, client_address):
    print(f'Connection from {client_address}')
    try:
        while True:
            data = connection.recv(1024)
            if not data:
                break
            received_message = data.decode().strip()
            # Validate received message
            if received_message:
                try:
                    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    insert_query = "INSERT INTO testing (time, msg) VALUES (%s, %s)"
                    cursor.execute(insert_query, (current_time, received_message))
                    db_conn.commit()
                    print(received_message + " was inserted successfully into the DB table")
                except psycopg2.Error as e:
                    db_conn.rollback()
                    print(f"Error inserting into database: {e}")
    except Exception as e:
        print(f"Error handling client connection: {e}")
    finally:
        connection.close()


def main():
    # Create a TCP/IP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Bind the socket to the port
        sock.bind((HOST, PORT))
        # Listen for incoming connections
        sock.listen(1)
        print(f'Server listening on {HOST}:{PORT}')
        
        # Handle graceful shutdown
        def signal_handler(sig, frame):
            print('Shutting down server...')
            sock.close()
            cursor.close()
            db_conn.close()
            sys.exit(0)

        signal.signal(signal.SIGINT, signal_handler)
        signal.signal(signal.SIGTERM, signal_handler)

        while True:
            # Wait for a connection
            print('Waiting for a connection')
            connection, client_address = sock.accept()
            handle_client(connection, client_address)

if __name__ == "__main__":
    main()
