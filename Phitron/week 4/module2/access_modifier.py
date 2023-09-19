class Account:
    def __init__(self, holder) -> None:
        self.account_holder = holder


class StudentAcount(Account):
    def __init__(self, holder, balance, school):
        self.__balance = balance

    def withdraw(self, amount):
        if amount > self.__balance:
            return 'No money for you'
        self.__balance -= amount
        return amount

    def diposit(self, amount):
        if amount < 0:
            return "Negative amount can not be added"
        self.__balance += amount

    def get_balance(self):
        return self.__balance


nas = StudentAcount("nas daily", 12000, 'Nas Academy')

nas.diposit(10000)
nas.withdraw(5000)

# print(nas.get_balance())
# print(dir(nas))
# print(nas._StudentAcount__balance)
