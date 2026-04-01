class GPSTracker:
    def __init__(self):
        self.lat = 13.0400
        self.lon = 80.2300

    def get_location(self):
        self.lat += 0.001
        self.lon += 0.001
        return (round(self.lat, 6), round(self.lon, 6))