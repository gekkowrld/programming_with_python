"""
A payroll system
================

Classes:
	Employee (Base)
	SalaryEmployee (Derived->Employee)
	HourlyEmployee (Derived->Employee)
	CommissionEmployee (Derived->SalaryEmployee)

All the Employee types should have a method:
	`calculate_payroll`
The method is for calculating the payroll amount.

This is just to demonstrate inheritance rather than a full-blown payroll system.
"""

from uuid import uuid1 as emp_uuid

class Employee:
	def __init__(self, emp_id, name):
		self.emp_id = emp_id
		self.name = name

class SalaryEmployee(Employee):
	def __init__(self, emp_id, name, week_s):
		super().__init__(emp_id, name)
		self.week_s = week_s

	def calculate_payroll(self):
		 return self.week_s

class HourlyEmployee(Employee):
	def __init__(self, emp_id, name, hours_w, hourly_r):
		super().__init__(emp_id, name)
		self.hours_w = hours_w
		self.hourly_r = hourly_r

	def calculate_payroll(self):
		 return self.hourly_r * self.hours_w

class CommisionEmployee(SalaryEmployee):
	def __init__(self, emp_id, name, week_s, sales):
		super().__init__(emp_id, name, week_s)
		self.sales = sales
	
	def calculate_payroll(self):
		return ((0.15*self.sales)+self.week_s) # Arbitrary calculations

t_emp = int(input("Choose the employee type:\n\t(1): Salary Employee\n\t(2)Hourly Employee\n\t(3)Commision Employee\n\t\t:>"))

def get_required():
	name = input("Enter Name: ")

	return emp_uuid() , name

def print_info(emp_id, name, salary):
	print("\n=================\n")
	print(f"Employee ID: {emp_id}\nName: {name}\nPay: {salary}")
	print("\n=================\n")

if t_emp == 1:
	emp_id, name = get_required()
	we_s = float(input("Enter weekly salary: "))
	s = SalaryEmployee(emp_id, name, we_s)
	salary = s.calculate_payroll()
	print_info(emp_id, name, salary)
elif t_emp == 2:
	emp_id, name = get_required()
	week_h = float(input(f"Enter the hours {name}  worked: "))
	week_r = float(input("Enter the hourly rate for the work: "))
	h = HourlyEmployee(emp_id, name, week_h, week_r)
	salary = h.calculate_payroll()
	print_info(emp_id, name, salary)
elif t_emp == 3:
	emp_id, name = get_required()
	we_s = float(input("Enter the weekly salary: "))
	com_n = float(input(f"Enter {name}'s commision: "))
	c = CommisionEmployee(emp_id, name, we_s, com_n)
	salary = c.calculate_payroll()
	print_info(emp_id, name, salary)
else:
	print("Please make a choice next time")
