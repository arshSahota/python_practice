class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance
    
account = BankAccount("Arshdeep", 100)
# print(account.get_balance())   # 100
print(account.__balance)     # would fail