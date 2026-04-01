from database_mysql import create_connection

def seed():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM Hospital")
    cursor.execute("DELETE FROM Ambulance")

    hospitals = [
        ("Apollo Hospital", 13.0604, 80.2517),
        ("Fortis Hospital", 13.0525, 80.2121),
        ("MIOT Hospital", 13.0213, 80.1857),
        ("Global Hospital", 12.8996, 80.2065),
        ("SIMS Hospital", 13.0536, 80.2470)
    ]

    cursor.executemany(
        "INSERT INTO Hospital (name, latitude, longitude) VALUES (%s, %s, %s)",
        hospitals
    )

    ambulances = [
        ("Ambulance 1", 13.0418, 80.2341),
        ("Ambulance 2", 13.0067, 80.2570),
        ("Ambulance 3", 12.9815, 80.2180),
        ("Ambulance 4", 13.0827, 80.2707),
        ("Ambulance 5", 13.0200, 80.2200)
    ]

    cursor.executemany(
        "INSERT INTO Ambulance (name, latitude, longitude) VALUES (%s, %s, %s)",
        ambulances
    )

    conn.commit()
    conn.close()