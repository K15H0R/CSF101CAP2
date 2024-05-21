#NAME:KISHOR KUMAR GHALLEY
#DEPARTMENT:MECHANICAL
#STUDENT NUMBER:02230266
##############################################################################################
#REFERENCE:
#
#
#
#
#
#
###################################################################################################
import os
import random
import string

class Account:
    def __init__(self, acc_number, pwd, acc_type, balance=0):
        self.acc_number = acc_number
        self.pwd = pwd
        self.acc_type = acc_type
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: Nu{amount}. New Balance: Nu{self.balance}")
        else:
            print("Invalid amount please be serious while putting amount. hope you have seen money.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: Nu{amount}. New Balance: Nu{self.balance}")
        else:
            print("sorry its disrespectful to say that you have Insufficient funds or invalid amount.")

    def save_to_file(self, file_name='accounts.txt'):
        with open(file_name, 'a') as f:
            f.write(f"{self.acc_number},{self.pwd},{self.acc_type},{self.balance}\n")

class PersonalAccount(Account):
    def __init__(self, acc_number, pwd, balance=0):
        super().__init__(acc_number, pwd, 'personal', balance)

class BusinessAccount(Account):
    def __init__(self, acc_number, pwd, balance=0):
        super().__init__(acc_number, pwd, 'business', balance)

def generate_acc_number():
    return ''.join(random.choices(string.digits, k=5))

def generate_pwd():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=4))

def load_accounts(file_name='accounts.txt'):
    accounts = {}
    if os.path.exists(file_name):
        with open(file_name, 'r') as f:
            lines = f.readlines()
            for line in lines:
                acc_number, pwd, acc_type, balance = line.strip().split(',')
                balance = float(balance)
                if acc_type == 'personal':
                    account = PersonalAccount(acc_number, pwd, balance)
                elif acc_type == 'business':
                    account = BusinessAccount(acc_number, pwd, balance)
                accounts[acc_number] = account
    return accounts

def login(accounts):
    acc_number = input("Enter your account number: ")
    pwd = input("Enter your password: ")
    if acc_number in accounts and accounts[acc_number].pwd == pwd:
        print("Login successful!")
        return accounts[acc_number]
    else:
        print("Invalid acc. number please be careful while inserting acc. number.")
        return None

def send_money(accounts, from_account):
    to_acc_number = input("Enter the recipient's account number: ")
    amount = float(input("Enter the amount to send: "))
    if to_acc_number in accounts:
        if from_account.balance >= amount:
            from_account.withdraw(amount)
            accounts[to_acc_number].deposit(amount)
            print(f"Sent Nu{amount} to {to_acc_number}")
        else:
            print("sorry its direspectful to say but you have Insufficient funds.")
    else:
        print("Recipient account not found.")

def main():
    accounts = load_accounts()

    while True:
        print("\n..........Welcome to the CST Bank............")
        print("1. Open an Account")
        print("2. Login to Account")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            print("Select Account Type:")
            print("1. Personal Account")
            print("2. Business Account")
            acc_type = input("Enter your choice: ")
            if acc_type in ['1', '2']:
                acc_number = generate_acc_number()
                pwd = generate_pwd()
                if acc_type == '1':
                    account = PersonalAccount(acc_number, pwd)
                else:
                    account = BusinessAccount(acc_number, pwd)
                account.save_to_file()
                accounts[acc_number] = account
                print(f"Account created successfully! Account Number: {acc_number}, Password: {pwd}")
            else:
                print("Invalid account type selected.")

        elif choice == '2':
            account = login(accounts)
            if account:
                while True:
                    print("\n.......Account Menu.........")
                    print("1. Check Balance")
                    print("2. Deposit ")
                    print("3. Withdraw ")
                    print("4. transfer funds")
                    print("5. Delete Account")
                    print("6. Logout")
                    acc_choice = input("Enter your choice: ")

                    if acc_choice == '1':
                        print(f"Your Balance: Nu{account.balance}")
                    elif acc_choice == '2':
                        amount = float(input("Enter amount to deposit: "))
                        account.deposit(amount)
                    elif acc_choice == '3':
                        amount = float(input("Enter amount to withdraw: "))
                        account.withdraw(amount)
                    elif acc_choice == '4':
                        send_money(accounts, account)
                    elif acc_choice == '5':
                        del accounts[account.acc_number]
                        print("Account deleted successfully.")
                        break
                    elif acc_choice == '6':
                        print("Logged out successfully.")
                        break
                    else:
                        print("Invalid choice. Please try again.")
        
        elif choice == '3':
            print(".....Thank you for using CST Bank.......")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
