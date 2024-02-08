#/usr/bin/python3

"""
A program to calculate and display the electricity bill for
    a given customer based on the units consumed.
The charges are as follows:
    Units                               Charges per unit(Ksh)
    upto 199                            1.20
    200 and above but less than 400     1.50
    400 and above but less than 600     1.80
    600 and above                       2.00

Steps:
    Prompt the user for CustomerID, CustomerName, and UnitConsumed
    Use if else to determine the correct charge
    Calculate the bill.
    If bill exceeds 400 then a surcharge of 15% will be charged
    Minimum bill should be ksh 100

Input:
    - Customer ID
    - Customer Name
    - Units Consumed

Output:
    - Customer ID
    - Customer Name
    - Units Consumed
    - Charges per Unit
    - Total Amount to Pay
"""

import math

def calculate_the_bill(units):
    if units < 0:
        return units, 0
    elif units < 200:
        return units * 1.2, 1.20
    elif units >= 200 and  units < 400:
        return units * 1.5, 1.50
    elif units >= 400 and units < 600:
        return units * 1.8, 1.80
    else:
        return units * 2, 2.0

def display_output(c_id, c_name, u_consumed, u_charge, total):
    if u_consumed < 100:
        print(f"Dear {c_name} of id {c_id}, {u_consumed} is less than 100, please fix it!")
        exit(1)
    else:
        if total < 400:
            print(f"Dear {c_name} of id {c_id}, {u_consumed} units costs ksh {round(total, 2):.2f} at a rate of ksh {u_charge} per unit")
        else:
            print(f"Dear {c_name} of id {c_id}, {u_consumed} units costs ksh {total+(total*0.15):.2f} at a rate of ksh {u_charge} per unit and a surcharge of 15%")

c_name = input("Enter your name: ")
c_id = input("Enter your customer ID: ")
u_consumed = float(input("Enter the total units consumed: "))
total, u_charge = calculate_the_bill(u_consumed)

display_output(c_id, c_name, u_consumed, u_charge, total)
