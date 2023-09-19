class Calculator:
    def add(self, a, b):
        return a+b

    def subtruct(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a*b

    def divid(self, a, b):
        return a/b


calc = Calculator()

print(calc.add(10, 5),
      calc.subtruct(10, 5),
      calc.multiply(10, 5),
      calc.divid(10, 5))
