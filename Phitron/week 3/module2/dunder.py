class Persion:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def __add__(self, other):

        return self.name + " " + other.name + " "


alal = Persion("alal", 30)
dulal = Persion("dulal", 35)
belal = Persion("belal", 40)

print(alal + dulal)
