class Account:
    
    def __init__(self,name,amount):
        self.name=name 
        self.amount=amount 
        
    def __str__(self):
        return "Account owner: " + self.name + "\nAccount balance: " + str(self.amount)
    
    def deposit(self,dep):
        self.amount=self.amount+dep
        return str(self.amount)
    def withdraw(self,dep):
            tempvar=self.amount
            tempvar=tempvar-dep
            if tempvar<=0:
                print("funds unavailable!")
                return self.amount
            else:
                self.amount=tempvar
                # print("withdrawn")
                return self.amount

# 1. Instantiate the class
acct1 = Account('Jose',100)


# 2. Print the object
print(acct1)

# # 3. Show the account owner attribute
print(acct1.name)


# # 4. Show the account balance attribute
print(acct1.amount)


# # 5. Make a series of deposits and withdrawals
print(acct1.deposit(50))


print(acct1.withdraw(75))


# # 6. Make a withdrawal that exceeds the available balance
print(acct1.withdraw(5000))

