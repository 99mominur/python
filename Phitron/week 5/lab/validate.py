# class Item:
#     def __init__(self, itemName, itemPrice) -> None:
#         assert itemPrice > 0, f"invalid itemPrice"
#         self.itemName = itemName
#         self.itemPrice = itemPrice


# item = Item("plate", -150)

# print(item.itemName, item.itemPrice)

class Person:
    def __init__(self, name, phone, age) -> None:
        assert len(phone) == 11, f"Invalid phone number"
        assert age >= 18, f"You are under 18"
        self.name = name
        self.phone = phone
        self.age = age

    def __repr__(self) -> str:
        return f"{self.name} {self.phone} {self.age}"


user = Person("Mominur", "01928802211", 18)

print(user)
