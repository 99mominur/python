""" Manage Bank Account """


class Account:

    accID = 1

    def __init__(self, name, age, nid_num, balance):
        self.name = name
        self.age = age
        self.nid_num = nid_num
        self.balance = balance
        # update acc ID
        self.account_id = Account.accID
        Account.accID += 1

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount


acc_1 = Account("Momin", 22, 102918, 5000)
# acc_2 = Account("Mominur", 23, 10274, 15000)

acc_1.deposit(10000)
acc_1.withdraw(5000)

print(acc_1.balance)
# print(acc_1.account_id)
# print(acc_2.account_id)
