# abstrack base class

from abc import ABC, abstractmethod
from cgi import print_arguments


class Animal(ABC):

    @abstractmethod
    def eat(self):
        pass

    @property
    def name(self):
        print("Animal")

    @abstractmethod
    def move(self):
        print("Moving around the zoo")


class Monkey(Animal):

    def __init__(self) -> None:
        self.__name = 'Monkey'

    def sing(self):
        print("Monkey is singing")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def eat(self):
        print("Eating banana")

    def move(self):
        return super().move()


layka = Monkey()

# print(layka)
# layka.name = "Moonkey"
# layka.name()
layka.name = "Moonkey"
print(layka.name)
# layka.eat()
# layka.move()
