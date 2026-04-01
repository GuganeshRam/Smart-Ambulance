import mysql.connector

def create_server_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root"
    )

def create_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="ambulance_system"
    )

def setup_database():
    conn = create_server_connection()
    cursor = conn.cursor()

    cursor.execute("CREATE DATABASE IF NOT EXISTS ambulance_system")
    conn.database = "ambulance_system"

    # Hospital Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Hospital (
        hospital_id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        latitude DOUBLE,
        longitude DOUBLE
    )
    """)

    # Ambulance Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Ambulance (
        ambulance_id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        latitude DOUBLE,
        longitude DOUBLE
    )
    """)

    conn.commit()
    conn.close()