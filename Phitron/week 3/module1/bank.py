class Bank:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        self.balance -= amount

    def diposit(self, amount):
        self.balance += amount


my_ac = Bank(10000)
my_ac.withdraw(2000)
my_ac.diposit(5000)


print(my_ac.__dict__)
