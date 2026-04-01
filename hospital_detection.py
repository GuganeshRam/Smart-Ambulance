import math
from database_mysql import create_connection

class HospitalDetector:

    def get_hospitals(self):
        conn = create_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT name, latitude, longitude FROM Hospital WHERE emergency_available = TRUE")
        hospitals = cursor.fetchall()

        conn.close()
        return hospitals

    def find_nearest(self, lat, lon):
        hospitals = self.get_hospitals()

        if not hospitals:
            print("No hospitals found in database")
            return None, None, None

        min_dist = float('inf')
        nearest = None
        h_lat = None
        h_lon = None

        for name, latitude, longitude in hospitals:
            dist = math.sqrt((lat - latitude)**2 + (lon - longitude)**2)

            if dist < min_dist:
                min_dist = dist
                nearest = name
                h_lat = latitude
                h_lon = longitude

        return nearest, h_lat, h_lon