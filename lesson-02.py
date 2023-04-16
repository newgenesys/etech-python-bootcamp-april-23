"""
Title: Lesson 02 - Variables and data types
Author: Olouge E.E
Date: 12/04/2023
Last Modified: 12/04/2023
Description: This program illustrates the use of variables
and data types.
"""

"""
x = 40.75
print(x)
print(type(x))

y = 17
print(y)
print(type(y))

z = x + y
print(z)
print(type(z))

z = 'Olouge is 100 year old. '
w = "Olouge is running late, again!"

print(z)
print(type(z))

print(w)
print(type(w))

a = w + z

print(a)

b = str(x) + w
print(b)  # printing the value in b

# print("This is not going to be printed")
"""

"""
This is multiline comment
This is another new line commented
All comments
"""

"""
Some more practical example
"""

x = 1.1
y = 1000
z = x + y

# Income: $
monthly_income = 5000
print("${} is our monthly income".format(monthly_income))

# Taxes:
tax_rate = 0.184
print("{} is our tax rate".format(tax_rate))

# Expenses: $
rent = 1200
food = 320
wifi = 100
transport = 300
misc = 400

# Income: After taxes
tax_amount = tax_rate * monthly_income
print("${} is amount to be paid as tax".format(tax_amount))

income_AT1 = monthly_income - tax_amount
print("${} is income after tax using method 1".format(income_AT1))

income_AT2 = monthly_income * (1 - tax_rate)
print("${} is income after tax using method 2".format(income_AT2))

# Total expenses
expenses = rent + food + wifi + transport + misc

print("${} is our total monthly expenses".format(expenses))

# What is left?

balance = income_AT1 - expenses

print("${} is our balance for the month after tax and expenses. Ready to save?".format(balance))

emergency_funds_over_6_months = expenses * 6  # which is better, 6 * expenses or expenses * 6?

print("we need ${} as 6 months emergency funds".format(emergency_funds_over_6_months))

"""
balance = $1760 - > 1, 
emergency_funds_over_6_months -> x
x = emergency_funds_over_6_months/balance
"""

number_months_to_save_emergency_funds = emergency_funds_over_6_months / balance

print("You will need {} months to save up for emergency".format(round(number_months_to_save_emergency_funds)))


STATE_OFF = False # 0
STATE_ON = True # 1

print(type(STATE_ON))
print(type(STATE_OFF))