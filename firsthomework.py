class Account:
    
    def __init__(self,name,amount):
        self.name=name 
        self.amount=amount 
        print("created")

# 1. Instantiate the class
acct1 = Account('Jose',100)


# 2. Print the object
print(acct1)

# # 3. Show the account owner attribute
# acct1.owner


# # 4. Show the account balance attribute
# acct1.balance


# # 5. Make a series of deposits and withdrawals
# acct1.deposit(50)


# acct1.withdraw(75)


# # 6. Make a withdrawal that exceeds the available balance
# acct1.withdraw(500)

