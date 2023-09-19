import random


class BRTA:
    def __init__(self) -> None:
        self.__licese = {}

    def take_driving_test(self, email):
        score = random.randint(0, 100)
        if score >= 33:
            print("Congrats, you have passed")
            license_number = random.randint(5000, 9999)
            self.__licese[email] = license_number
            return license_number
        else:
            print("Sorry you failed", score)
            return False

    def validate_license(self, email, license):
        for key, value in self.__licese.items():
            if key == email and value == license:
                print(email, license)
                return True
        return False
