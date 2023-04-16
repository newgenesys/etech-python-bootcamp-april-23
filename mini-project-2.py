"""
Solution: Mini Project 2
Date: 12/04/2023
Author: Olouge E.E
Description: Computes the area of any circular shape given its radius, r.
"""
# Input variables: r
print("Welcome to Area of a circle App")
print("Enter radius: ")

user_input = input()

r = float(user_input)

# Variables: PI, r in cm
PI = 3.14


# Auxilliary variables: raised
raised = r ** 2

# Intermediate variables: Area

Area = PI * raised
print(Area)

Area2 = PI * (r ** 2)
print(Area2)