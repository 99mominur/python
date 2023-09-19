class Item:
    all = []

    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price
        self.all.append(self)

    def __repr__(self) -> str:
        return f"Item ({self.name}, {self.price})"


item1 = Item("Bowl", 100)
item2 = Item("Plate", 200)
item1.discount = 10
item1.offer = "60%"
print(Item.all)
print(item1.__dict__)
print(item2.__dict__)
