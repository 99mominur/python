class Animal:
    def __init__(self, name) -> None:
        self.name = name

    def make_sound(self):
        print("Animal making sound")


class Cat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def make_sound(self):
        print("meow meow")


class Dog(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def make_sound(self):
        print("Bark Bark")


don = Cat("don")

# don.make_sound()

shepard = Dog("German shepard")
# shepard.make_sound()

doggy = Dog("Doggy")
bilai = Cat("Mini")

animals = [don, shepard, doggy, bilai]

for animal in animals:
    animal.make_sound()
