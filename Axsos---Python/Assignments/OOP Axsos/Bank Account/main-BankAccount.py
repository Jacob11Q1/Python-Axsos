# Bank Account Assignment:

class BankAccount:
    def __init__(self, int_rate , balance = 0):
        self.int_rate = int_rate
        self.balance = balance
    
    def deposit(self , amount):
        self.balance += amount
        return self
    
    def withdraw(self , amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew: ${amount}")
        else:
            print(f"Insufficient Funds: Charging a $5 fee")
            self.balance -= 5
        return self
    
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self
    
    def yield_interest(self):
        if self.balance > 0:
            interest = self.balance * self.int_rate
            self.balance += interest
            print(f"Interest added: ${interest: .2f}")
        else:
            print("No interest added. Balance is non-positive")
        return self