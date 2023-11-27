# In a certain organization, people are taxed using the following tax bracket.
# Salary            Tax rate
# >= 20000              15%
# 10000 – 20000         10%
# 0 – 10000             Not taxed
# Write a program that accepts someone’s salary and computes both their tax amount and net salary (Gross – tax)
salary = int(input("Enter your salary: "))

if salary >= 20000:
    tax_amount = salary * 15.0/100
    net_salary = salary - tax_amount
    output = f'The salary is: {salary} The tax_amount: {tax_amount} The net_salary is: {net_salary}.'
    print(output)
elif 10000 < salary < 20000:
    tax_amount = salary * 10.0/100
    net_salary = salary - tax_amount
    output = f'The salary is: {salary} The tax_amount: {tax_amount} The net_salary is: {net_salary}.'
    print(output)
elif 0 < salary < 10000:
    print("Not Taxed!!")
else:
    print("Not on th e Tax Bracket")






