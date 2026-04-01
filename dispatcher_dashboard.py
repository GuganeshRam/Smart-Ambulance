class DispatcherDashboard:

    def __init__(self):
        self.data = []

    def update(self, location, hospital, eta):
        self.data.append({
            "location": location,
            "hospital": hospital,
            "eta": eta
        })

    def display(self):
        for d in self.data:
            print(d)