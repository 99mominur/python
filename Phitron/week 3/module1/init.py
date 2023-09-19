import py_compile


class Phone:
    manufactured = "China"

    def __init__(self, brand, price, color):
        self.brand = brand
        self.price = price
        self.color = color


my_phone = Phone("Oppo", 15000, 'black')


print(my_phone.manufactured, my_phone.brand, my_phone.price, my_phone.color)
