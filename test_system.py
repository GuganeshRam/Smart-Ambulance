from gps_tracking import GPSTracker
from hospital_detection import HospitalDetector

def test_gps():
    gps = GPSTracker()
    loc = gps.get_location()
    assert isinstance(loc, tuple)
    print("GPS Test Passed")

def test_hospital():
    detector = HospitalDetector()
    hospital, _, _ = detector.find_nearest(12.9, 77.5)
    assert hospital is not None
    print("Hospital Detection Test Passed")

if __name__ == "__main__":
    test_gps()
    test_hospital()