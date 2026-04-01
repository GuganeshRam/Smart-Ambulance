import math
import random

class RouteOptimizer:

    def calculate_distance(self, lat1, lon1, lat2, lon2):
        R = 6371

        lat1 = math.radians(lat1)
        lon1 = math.radians(lon1)
        lat2 = math.radians(lat2)
        lon2 = math.radians(lon2)

        dlat = lat2 - lat1
        dlon = lon2 - lon1

        a = math.sin(dlat/2)**2 + math.cos(lat1)*math.cos(lat2)*math.sin(dlon/2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

        distance = R * c
        return distance

    def get_traffic_factor(self):
        return random.uniform(1.2, 2.0)

    def get_optimized_distance(self, distance):
        return distance * self.get_traffic_factor()