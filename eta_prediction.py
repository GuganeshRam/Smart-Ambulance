class ETAPredictor:

    def calculate_eta(self, distance):
        speed = 25
        eta = (distance / speed) * 60
        return round(eta, 2)