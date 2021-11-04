class BankAccount:

    def __init__(self, int_rate = 0.01, balance = 0):
        self.int_rate = int_rate 
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(self.balance)
        return self
    
    def withdraw(self, amount):
        self.balance -= amount
        print(self.balance)
        return self
    
    def yield_interest(self):
        self.balance = self.balance + self.balance * self.int_rate
        print(self.balance)
        return self
    
    def display_account_info(self):
        print("Balance: " + str(self.balance))
        return self

Jacob = BankAccount(0.0388, 2500)
Sarah = BankAccount(0.0491, 2200)

print(Jacob.deposit(550).deposit(450).deposit(300).withdraw(600).yield_interest().display_account_info())
print(Sarah.deposit(944).deposit(784).withdraw(346).withdraw(279).withdraw(568).withdraw(157).yield_interest().display_account_info())

