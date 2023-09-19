class User:

    def __init__(self, name, phone, password) -> None:
        self.name = name
        self.phone = phone
        self.__password = password

    def get_password(self):
        print(self.__password)

    def user_login(self, name, password):
        if (name is self.name and password is self.__password):
            return True
        return False


person = User("Mominur Rahman", '0192882211', '99mominur')

# print(person.name)
# print(person.phone)
# # print(person.__password)
# person.get_password()


val = person.user_login("Mominur Rahman", "99mominur")

print(val)
