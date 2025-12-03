

# User login 


# class User:
#     def __init__(self, username, password):
#         self.username = username #public attribute
#         self.__password = password  # private attribute

#     def login(self,pwd):
#         if pwd == self.__password:
#             return "Login successful"
#         else:
#             return "Login failed"
#     def change_password(self, old_pwd, new_pwd):
#         if old_pwd == self.__password:
#             self.__password = new_pwd
#             return "Password changed successfully"
#         else:
#             return "Old password is incorrect"
# username = input("Enter username: ")
# password = input("Enter password: ")

# U = User(username,password)
# print(U.login(input("Enter password to login: ")))
# print(U.change_password(input("Enter old password: "), input("Enter new password: ")))
            
        

# Account and ATM function
        

class BankAccount:
    def __init__(self,name,balance):
        self.name = name              # public
        self._account_type = "saving" # protected
        self.__balance = balance      # private    
    
    def deposit(self,amount):
        self.__balance += amount
        print(f"Deposited: {amount}")
        print(f"New Balance: {self.__balance}")

    def withdraw(self,amount):
        if amount > self.__balance:
            print("Low balance")
        else:
            self.__balance -= amount 
            print(f"withdraw amount: {amount}") 
            # print(f"total amount: {self.__balance}")   

    def get_balance(self):
        return self.__balance
name = input("Enter your name : ")
balance = int(input("Enter your name : "))
account = BankAccount(name,balance) 
print(account.name) 
print(account.deposit(int(input("Enter deposit balance : "))))
print(account.withdraw(int(input("Enter withdraw balance : "))))
print(account.get_balance())       