Single inheritance:
Single inheritance allows a derivate class to inherit properties of one parent class, and this allows code reuse and the introduction of additional features in existing code.

class Parent:
    def func(self):
        print("Parent")


class Child(Parent):
    def func1(self):
        print("Child")


obj = Child()
obj.func1()
obj.func()


Multiple Inheritance:
When a class can be derived from more than one base class this type of inheritance is called multiple inheritances. In multiple inheritances, all the features of the base classes are inherited into the derived class.

class Mother:
    def mother(self):
        print("Parent")


class Father:
    def father(self):
        print("Father")


class Child(Mother, Father):
    def Child(self):
        print("Child")


obj1 = Child()

obj1.mother()
obj1.father()

Multilevel Inheritance:
In multilevel inheritance, features of the base class and the derived class are further inherited into the new derived class. This is similar to a relationship representing a child and a grandfather.


class Grandfather:
    def grandfather(self):
        print("Grandfather")


class Father(Grandfather):
    def father(self):
        print("Father")


class Son(Father):
    def son(self):
        print("Child")


obj2 = Son()
obj2.grandfather()
obj2.father()
