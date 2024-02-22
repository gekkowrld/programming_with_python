#!/bin/python3

"""
BankAccount
===========

This is a a simple implementation of a banking system.
The user can either:
    - Withdraw
    - Deposit

The account balance is initialized to 0 then incremented/decremented appropriatly.

The following are generated programatically:
    - uuid (account number)
    - date (time of creating account)

The following information is dislayed after each loop:
    - Customer Name
    - Account Number
    - Account Open Date
    - Balance
    - Either deposit or withdraw balance

The "UI" is kep clean and clutterless.
A clear sepearation between one operation and another one is kept when doing the loop.

"""

from datetime import datetime
from uuid import uuid1 as r_acc_num


class BankAccount:
    def __init__(self, acc_num, customer_name):
        self.acc_num = acc_num
        self.open_d = datetime.now()
        self.customer_name = customer_name
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient Funds"
        else:
            self.balance -= amount
            return self.balance

    def check_balance(self):
        return self.balance

    def customer_details(self):
        return self.customer_name, self.acc_num, self.open_d, self.balance


acc_n = r_acc_num()
c_name = input("Enter your name: ")
bank_d = BankAccount(acc_n, c_name)

loop = input("Do you want to bank (Y/N): ")

while loop.lower() == "y":
    ba_op = int(input("Do you want to (1)withdraw or (2)deposit: "))
    if ba_op == 1:
        amount = float(input("Enter withdraw amount: "))
        result = bank_d.withdraw(amount)
    else:
        amount = float(input("Enter deposit amount: "))
        result = bank_d.deposit(amount)

    if isinstance(result, str):  # Check if result is a string (error message)
        print(result)
    else:
        name, acc, opend, bala = bank_d.customer_details()
        print(
            f"\n========================\nCustomer Name: {name}\nAccount Number: {acc}\nAccount Open Date: {opend}\nBalance: {bala}")
        if ba_op == 1:
            print(f"Withdrawn amount: {amount}")
            print("\n========================\n")
        else:
            print(f"Deposited amount: {amount}")
            print("\n========================\n")
    loop = input("Do you want to bank (Y/N): ")
