#!/usr/bin/python3

"""
Library Fine Calculation

A program to calculate the fine for overdue library books.

The fine rates are as follows:
    Days Overdue        Charges per day
    Upto 7 days         Ksh. 30
    8 - 14 days         Ksh. 50
    15 days or more     Ksh. 100

Input:
    - bookID
    - dueDate
    - returnDate

Steps:
    Calculate the days overdue. `Hint`: returnDate - dueDate
    Use if else o find the correct rate.

Output:
    - bookID
    - dueDate
    - returnDate
    - daysOverdue
    - fineRate
    - fineAmount
"""

from datetime import datetime

def calculate_fine(d_date, r_date, book_id):
    rf_date = datetime.strptime(r_date, "%Y-%m-%d")
    df_date = datetime.strptime(d_date, "%Y-%m-%d")
    print(d_date)
    overdue_days = (rf_date-df_date).days
    if overdue_days < 0:
        print("No fine for you!")
    else:
        if overdue_days <= 7:
            rate = 20
            print(f"You have a fine of Ksh{overdue_days*rate} on Book ID {book_id} calculated at a rate of {rate} per day as from {d_date} to {r_date} ({overdue_days} days)")
        elif overdue_days <=8 and overdue_days <= 14:
            rate = 50
            print(f"You have a fine of Ksh {overdue_days*rate} on Book ID{book_id} calculated at a rate of {rate} per day as from {d_date} to {r_date} ({overdue_days} days)")
        else:
            rate = 100
            print(f"You have a fine of Ksh {overdue_days*rate} on Book ID{book_id} calculated at a rate of {rate} per day as from {d_date} to {r_date} ({overdue_days} days)")

d_date = input("Enter due date(YYYY-MM-DD): ")
r_date = input("Enter return date(YYYY-MM-DD): ")
book_id = input("Enter book ID: ")

calculate_fine(d_date, r_date, book_id)
