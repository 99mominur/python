class Bus:
    owner = "Ena Transpot"

    def __init__(self, route, license, driver) -> None:
        self.route = route
        self.license = license 
        self.driver = driver
        self.trips = []

    def start_trip(self, start_time):
        self.trips.append(start_time)

class Driver:
    def __init__(self, name, license, address) -> None:
        self.name = name
        self.license = license
        self.address = address 
        
        