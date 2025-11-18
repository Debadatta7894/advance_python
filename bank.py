# from time import sleep
# print("Welcome to state Bnak of India ATM")
# sleep(2)
# print("Please insert your card")
# sleep(2)

# pin_list = [1234, 5678, 9101]
# total_balance = 0
# deposit_amount = 0 
# withdraw_amount = 0

# pin = int(input("Enter your 4 digit pin: "))
# if pin in pin_list:
#     print("Pin accepted")
#     sleep(2)
#     print("please wait while we process your request")
#     sleep(2)
#     print("Select your transaction: ")
#     print("1. Deposit")
#     print("2. Withdraw")
#     print("3. Check Balance")
    
#     choice = int(input("Enter your choice (1/2/3): "))
    
#     if choice == 1:
#         deposit_amount = float(input("Enter amount to deposit: "))
#         total_balance += deposit_amount
#         print(f"Amount deposited: {deposit_amount}")
#         print(f"Total balance: {total_balance}")
        
#     elif choice == 2:
#         withdraw_amount = float(input("Enter amount to withdraw: "))
#         if withdraw_amount <= total_balance:
#             total_balance -= withdraw_amount
#             print(f"Amount withdrawn: {withdraw_amount}")
#             print(f"Total balance: {total_balance}")
#         else:
#             print("Insufficient balance")
            
#     elif choice == 3:
#         print(f"Your total balance is: {total_balance}")
           
        
#     else:
#         print("Invalid choice")

















from time import sleep
import os

print(" Welcome to SBI Bank ATM ")
sleep(2)
print("Insert your ATM card...")
sleep(2)

filename = "accounts.txt"


accounts = {}
if os.path.exists(filename):
    with open(filename, "r") as file:
        for line in file:
            if "," in line:
                pin, bal = line.strip().split(",")
                accounts[int(pin)] = int(bal)
else:
    # default accounts
    accounts = {1234: 0, 5678: 0, 1111: 0, 2222: 0, 3333: 0, 4444: 0}
    with open(filename, "w") as file:
        for pin, bal in accounts.items():
            file.write(f"{pin},{bal}\n")


amount, damount, wamount = 0, 0, 0


role = input("Are you admin or user? (admin/user): ").lower()

# Admin panel
if role == "admin":
    admin_pass = input("Enter admin password: ")
    if admin_pass == "admin123":
        print("\n All Registered Accounts:")
        with open(filename, "r") as file:
            for line in file:
                print(line.strip())
        print(" End of list.")
    else:
        print(" Incorrect admin password.")
    exit()

#  User login / registration
user_type = input("Are you a new user? (yes/no): ").lower()

if user_type == "yes":
    new_pin = int(input("Create a new 4-digit PIN: "))
    sleep(2)
    confirm_pin = int(input("Confirm your new PIN: "))
    sleep(2)
    print("Creating your new PIN...")
    if new_pin == confirm_pin and len(str(new_pin)) == 4:
        if new_pin in accounts:
            print("PIN already exists. Try another one.")
            exit()
        accounts[new_pin] = 0 
        with open(filename, "a") as file:
            file.write(f"{new_pin},0\n")
        print("Your new PIN has been created successfully!")
        pin = new_pin
    else:
        print(" PIN mismatch or invalid PIN format! Try again later.")
        exit()

elif user_type == "no":
    pin = int(input("Enter your existing PIN: "))

else:
    print("Invalid input. Please restart the ATM.")
    exit()

#  ATM Menu
if pin in accounts:
    amount = accounts[pin]  

    while True:
        menu = input("\nSelect option:\n"
                     "d → Deposit Amount\n"
                     "w → Withdrawal Amount\n"
                     "s → Statement\n"
                     "e → Exit\n"
                     "Enter your choice: ").lower()

        if menu == "d":
            damount = int(input("Enter deposit amount: "))
            amount += damount
            accounts[pin] = amount
            print(" Amount deposited successfully.")
            
        elif menu == "w":
            wamount = int(input("Enter withdrawal amount: "))
            if wamount <= amount:
                amount -= wamount
                accounts[pin] = amount
                print(" Please collect your cash.")
            else:
                print("Insufficient balance!")

        elif menu == "s":
            print(f" Your current balance = ₹{amount}")

        elif menu == "e":
            # Save updated balances to file
            with open(filename, "w") as file:
                for p, bal in accounts.items():
                    file.write(f"{p},{bal}\n")
            print(" Thank you for using SBI Bank ATM.\nVisit again!")
            break

        else:
            print(" Invalid option. Please try again.")

else:
    print(" Invalid PIN. Try again later.")

