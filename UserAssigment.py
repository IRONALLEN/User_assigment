class User:
    def __init__(self, name, email,):
        self.name = name
        self.email = email
        self.acount_balance = 0 
        

    def make_deposit(self,amount):
        self.acount_balance += amount
    
    def make_withdraw(self, amount):
        self.acount_balance -= amount

    def display_user_balance(self,acount_balance):
        self.acount_balance
    # bonus have this method decrease the user's balance by the amount and add that amount to other other_user's balance
    #was not able to 
    def transfer_money(self, transfer_positive, transfer_negative):
        self.acount_balance += transfer_positive
        self.acount_balance -= transfer_negative

guido = User("Guido Van Rossum", "guidoman@python.com")
marty = User("Marty Johson", "martinluis@google.com")
jake = User("Jake Lukas", "jakejumping@yallow.com")

guido.make_deposit(300)
guido.make_deposit(500)
guido.make_deposit(200)
guido.make_withdraw(400)

marty.make_deposit(400)
marty.make_deposit(400)
marty.make_withdraw(200)
marty.make_withdraw(100)

jake.make_deposit(1000)
jake.make_withdraw(300)
jake.make_withdraw(200)
jake.make_withdraw(200)

print("guido's account balance: $" + str(guido.acount_balance))
print("Marty's account balance: $" + str(marty.acount_balance))
print("jake's account balance: $" + str(jake.acount_balance))
