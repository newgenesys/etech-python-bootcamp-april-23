"""
**Problem 2:** Write a program to compute the pay of Employees. The data is to be read from a file as:

*first name,last name,employee id,hours worked,pay rate*

Adam,Ames,111452,45,17.50

Sally,Sims,111657,35,22.75

Mark,Manning,111932,52,16.50

Cindy,Carson,1117,48,18.50

Jim,Jacobs,111873,38,25

Alice,Andrews,11262,60,19.50

You will write a function called compute_pay that will compute the pay of the employee. The pay is to be computed as

*hours worked multiplied by the pay rate if the number of hours worked is less than 40.*

*If the number of hours worked is greater than 40, then the pay has to be 1.75 * pay_rate * hours_worked.*

The computed pay is to be stored in an output file as:

id    last name    pay
"""
