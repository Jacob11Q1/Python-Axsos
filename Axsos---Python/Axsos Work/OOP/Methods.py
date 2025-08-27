# Methods:

# guido.make_deposit(100)

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # Adding the deposit Method
    def make_deposit(self, amount): # Takes an argument that is the amount of the deposit
        self.account_balance += amount # The specific user's account increases by the amount of the value recieved

# Create user instances
guido = User("Guido van Rossum", "guido@example.com")
monty = User("Monty Python", "monty@example.com")

# Call the deposit method on the user instances
guido.make_deposit(100)
guido.make_deposit(200)
monty.make_deposit(50)
print(guido.account_balance) # Output: 300
print(monty.account_balance) # Output: 50
