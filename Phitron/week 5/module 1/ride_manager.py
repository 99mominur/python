


class RideManager:
    def __init__(self) -> None:
        print("Ride manager activated")
        self.__available_cars = []   
        self.__available_bike = []   
        self.__available_cng = []   
    
    def add_a_vehicle(self,vehicle_type, vehicle):
        if vehicle_type == "car":
            self.available_cars.append(vehicle)
        elif vehicle_type == "Bike":
            self.__available_bike.append(vehicle)
        else:
            self.__available_cng.append(vehicle)
        
    
    def match_a_vehicle(self):
        pass
    
    
uber = RideManager()