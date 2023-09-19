class Account:
    def __init__(self, holder, inition_balace) -> None:
        self.holder = holder
        self._acount_number = 1065
        self.__balance = inition_balace

    def deposit(self, amount):
        print(f"adding {amount} to your account")
        self.__balance += amount

    def withdraw(self, amount):
        print(f"withdrawing {amount} from your account")

        self.__balance -= amount


class StudentAccount(Account):
    def __init__(self, holder, inition_balace, school) -> None:
        self.school = school
        super().__init__(holder, inition_balace)


Rafsan = StudentAccount('Rafsan', 50000, "IUB")
# print(Rafsan.__balance)
print(Rafsan.holder)
Rafsan.deposit(20000)
Rafsan.deposit(35000)
Rafsan.deposit(15000)
# Rafsan.__balance = 0
print(Rafsan._acount_number)
