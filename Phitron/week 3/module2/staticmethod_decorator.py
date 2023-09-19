class Shopping:
    def __init__(self, customer) -> None:
        self.customer = customer
        self.items = []
        self.total = 0

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


person1 = Shopping("Mominur Rahman")

person1.add_to_cart("Potato", 10, 5)
person1.add_to_cart("Biscuit", 20, 3)

person1.checkout()


print(person1.multiply(3, 5))

print(Shopping.multiply(3,4))

