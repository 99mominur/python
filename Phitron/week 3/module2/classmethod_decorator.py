class Shopping:
    mall = "Jamuna Future Park"
    time = []

    def __init__(self, customer) -> None:
        self.customer = customer
        self.items = []
        self.total = 0

    @classmethod
    def opening_hours(cls, day):
        return cls.mall

    @staticmethod
    def multiply(a, b):
        return a * b

    def add_to_cart(self, item, price, quantity):
        self.items.append(item)
        item_total = price * quantity
        self.total += item_total

    def checkout(self):

        for item in self.items:
            print(item, end=" ")

        print(f'\nTotal price is {self.total}')


value = Shopping.opening_hours('thursday')
print(value)
