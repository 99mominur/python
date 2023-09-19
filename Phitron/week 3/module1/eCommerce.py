class Cart:
    def __init__(self, name) -> None:
        self.name = name
        self.cart = []

    def add_to_cart(self, item, price, quantity):
        self.cart.append({"item": item, "price": price, "quantity": quantity})

    def checkout(self):
        for item in self.cart:
            print(item)

    def total_amount(self):
        price = 0
        for item in self.cart:
            price += item["price"] * item["quantity"]
        return price


shop = Cart("Mominur Rahman")
shop.add_to_cart('shirt', 400, 2)
shop.add_to_cart('pant', 1400, 2)
shop.add_to_cart('shoe', 1000, 2)


# shop.checkout()
price = shop.total_amount()

print(price)
