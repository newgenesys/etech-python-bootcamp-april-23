"""
Solution: Mini Project 1
Date: 12/04/2023
Author: Olouge E.E
Description: Computes the interest on a loan with principal P,
for n months at interest rate of r%
"""
# Variables: principal in $, rate, n_months
# Sample values: principal = 10000, rate=5%, n_months = 36
print("Enter Principal: ")
user_input = input()
principal = float(user_input)

print("Enter Rate: ")
user_input = input()
r = float(user_input)/100

print("Enter Duration (in months): ")
user_input = input()
n_months = int(user_input)

# Auxilliary variables: power, rate_sum, raised
power = n_months/12
rate_sum = 1 + r

# ** is represents power function (raising a number to a power)
raised = rate_sum ** power

# Intermediate variables: total_amount
# total_amount = principal * ( (1+r) ** (n/12) )
total_amount = principal * raised

print("${} is total amount".format(round(total_amount, 2)))
# print(round(total_amount, 2))

# total_amount1 = principal * ( (1+r) ** (n_months/12) )

# print(round(total_amount1, 2))

