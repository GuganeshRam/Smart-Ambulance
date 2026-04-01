import random

ambulances = []

for i in range(3):
    lat = round(random.uniform(12.9, 13.1), 6)
    lon = round(random.uniform(80.2, 80.3), 6)
    ambulances.append({"lat": lat, "lng": lon})

hospital = {"lat": 13.0604, "lng": 80.2517}

with open("map_data.js", "w") as f:
    f.write(f"const ambulances = {ambulances};\n")
    f.write(f"const hospital = {hospital};\n")