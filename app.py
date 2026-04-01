from flask import Flask, jsonify
from gps_tracking import GPSTracker
from hospital_detection import HospitalDetector
from route_optimization import RouteOptimizer
from eta_prediction import ETAPredictor

app = Flask(__name__)

gps = GPSTracker()
detector = HospitalDetector()
route = RouteOptimizer()
eta_calc = ETAPredictor()

@app.route("/")
def home():
    return "Ambulance Tracking System Running"

@app.route("/status")
def status():
    location = gps.get_location()
    hospital, h_lat, h_lon = detector.find_nearest(location[0], location[1])

    distance = route.calculate_distance(location[0], location[1], h_lat, h_lon)
    eta = eta_calc.calculate_eta(distance)

    return jsonify({
        "location": location,
        "hospital": hospital,
        "eta": eta
    })

if __name__ == "__main__":
    app.run(debug=True)