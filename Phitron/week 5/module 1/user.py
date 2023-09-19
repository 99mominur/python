import hashlib
from random import random, randint
from brta import BRTA
from vehicles import Car, Bike, CNG
from ride_manager import uber


license_authority = BRTA()


class User:
    def __init__(self, name, email, password) -> None:
        self.name = name
        self.email = email
        pwd_encrypted = hashlib.md5(password.encode()).hexdigest()
        with open("users.txt", 'w') as file:
            file.write(f'{email} {pwd_encrypted}')
        file.close()
        print(self.name, "user created")

    @staticmethod
    def log_in(email, password):
        store_password = ''
        with open("users.txt", 'r') as file:
            lines = file.readlines()
            for line in lines:
                if email in line:
                    store_password = line.split()[1]
        file.close()
        hashed_password = hashlib.md5(password.encode()).hexdigest()
        if hashed_password == store_password:
            print("Valid user")
        else:
            print("Invalid user")
        # print("Password found: ", store_password)


class Rider(User):
    def __init__(self, name, email, password, location, balance) -> None:
        self.location = location
        self.balance = balance
        super().__init__(name, email, password)

    def set_location(self, location):
        self.location = location

    def get_location(self):
        return self.location

    def requst_trip(self, destination):
        pass

    def start_a_trip(self, fare):
        self.balance -= fare


class Driver(User):
    def __init__(self, name, email, password, location, license) -> None:
        self.location = location
        self.license = license
        self.valid_driver = license_authority.validate_license(email, license)
        self.earing = 0
        super().__init__(name, email, password)

    def take_driving_test(self):
        result = license_authority.take_driving_test(self.email)
        if result == False:
            print("Sorry your failed")
        else:
            self.license = result
            self.valid_driver = True

    def register_a_vehicle(self, vehicle_type, license_plate, rate):
        if self.valid_driver is True:

            if vehicle_type == "car":
                new_vehicle = Car(
                    license_plate, vehicle_type, rate, self.email)
                uber.add_a_vehicle(vehicle_type, new_vehicle)
            elif vehicle_type == "Bike":
                new_vehicle = Bike(
                    license_plate, vehicle_type, rate, self.email)
                uber.add_a_vehicle(vehicle_type, new_vehicle)
            else:
                new_vehicle = CNG(
                    license_plate, vehicle_type, rate, self.email)
                uber.add_a_vehicle(vehicle_type, new_vehicle)
        else:
            print("Not valid driver")

    def start_a_trip(self, destination, fare):
        self.earing += fare
        self.location = destination


rider1 = Rider("rider1", "rider1@gmail.com", 'rider1', randint(0, 100), 5000)
rider2 = Rider("rider2", "rider2@gmail.com", 'rider2', randint(0, 100), 5000)
rider3 = Rider("rider3", "rider3@gmail.com", 'rider3', randint(0, 100), 5000)

driver1 = Driver("dirver1", "driver1@gmail.com",
                 'driver1', randint(0, 100), 5645)
driver1.take_driving_test()
driver1.register_a_vehicle("car", 5645, 10)

driver2 = Driver("dirver2", "driver2@gmail.com",
                 'driver2', randint(0, 100), 5645)
driver3 = Driver("dirver3", "driver3@gmail.com",
                 'driver3', randint(0, 100), 5645)
driver4 = Driver("dirver4", "driver3@gmail.com",
                 'driver3', randint(0, 100), 5645)
