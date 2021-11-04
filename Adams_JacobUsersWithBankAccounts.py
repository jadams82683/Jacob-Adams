class User: 

    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account = BankAccount(int_rate = 0.02, balance = 0)
        self.account2 = BankAccount(int_rate = 0.02, balance = 0)
        self.account3 = BankAccount(int_rate = 0.02, balance = 0)

class BankAccount:

    def __init__(self, int_rate, balance):
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
        
Jacob = User("Jacob Adams", "jacobadams83@gmail.com")
Sarah = User("Sarah Burlingham", "sburlingham@yahoo.com")
Salem = User("Salem the Cat", "salemthecat@salem.com")
    
def make_deposit(self):
    self.account.deposit()
    return Jacob.account.balance
print(Jacob.account.deposit(100).deposit(200))
print(Jacob.account2.deposit(2500))
print(Jacob.account.display_account_info())
    
def make_withdrawl(self, amount):
    self.account.withdraw()
print(Jacob.account.withdraw(150))
print(Jacob.account.display_account_info())

def transfer_money(self, other_user, amount):
    self.account_balance -= amount
    other_user.account_balance += amount

def display_user_balance(self):
    print(self.name)
    print("Balance:", self.account.display_account_info)




