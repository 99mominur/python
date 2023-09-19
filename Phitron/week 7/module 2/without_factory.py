class Bike:
    def __init__(self, driver, rate=0) -> None:
        self.driver = driver
        self.rate = rate

    def get_fare(self, distance):
        return distance * self.rate


class Car:
    def __init__(self, driver, rate) -> None:
        self.driver = driver
        self.rate = rate

    def get_fare(self, distance):
        return distance * self.rate


class CNG:
    def __init__(self, driver, rate) -> None:
        self.driver = driver
        self.rate = rate

    def get_fare(self, distance):
        return distance * self.rate


bike = Bike("Masud", 5)
car = Car("Mahbub", 10)
cng = CNG("Karim", 8)

customer = [20, 14, 16]

for distance in customer:
    print(bike.get_fare(distance))
    print(car.get_fare(distance))
    print(cng.get_fare(distance))
