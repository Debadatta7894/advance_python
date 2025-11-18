class User:
    def __init__(self, username, password):
        self.username = username #public attribute
        self.__password = password  # private attribute

    def login(self,pwd):
        if pwd == self.__password:
            return "Login successful"
        else:
            return "Login failed"
    def change_password(self, old_pwd, new_pwd):
        if old_pwd == self.__password:
            self.__password = new_pwd
            return "Password changed successfully"
        else:
            return "Old password is incorrect"
username = input("Enter username: ")
password = input("Enter password: ")

U = User(username,password)
print(U.login(input("Enter password to login: ")))
# print(U.change_password(input("Enter old password: "), input("Enter new password: ")))
            
        