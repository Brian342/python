# Write a program using the tax information below: -
# Gross Pay                       Tax Rate
# Over 40,000                       30%
# >= 30,000 but below 40,000        25%
# >=20,000 but below 30,000         15%
# >=10,000 but below 20,000         10%
# Below 10,000                      no tax.
# Write a program that accepts the gross pay and computes both the tax amount and the net pay.
# (Assume the net pay is gross pay – tax amount)
import math
gross_pay = int(input("Enter the gross_pay: "))

if gross_pay >= 40000:
    tax_amount = gross_pay * 30.0 / 100
    net_pay = gross_pay - tax_amount
    output = f'The tax_amount is {math.floor(tax_amount)}. The net_pay is {math.floor(net_pay)}'
    print(output)
elif 30000 >= gross_pay < 40000:
    tax_amount = gross_pay * 25.0 / 100
    net_pay = gross_pay - tax_amount
    output = f'The tax_amount is {math.floor(tax_amount)}. The net_pay is {math.floor(net_pay)}'
    print(output)
elif 20000 >= gross_pay < 30000:
    tax_amount = gross_pay * 15.0 / 100
    net_pay = gross_pay - tax_amount
    output = f'The tax_amount is {math.floor(tax_amount)}. The net_pay is {math.floor(net_pay)}'
    print(output)
elif 10000 >= gross_pay < 20000:
    tax_amount = gross_pay * 10.0 / 100
    net_pay = gross_pay - tax_amount
    output = f'The tax_amount is {math.floor(tax_amount)}. The net_pay is {math.floor(net_pay)}'
    print(output)
elif 10000 <= gross_pay:
    print("Not taxed!!!")
else:
    print("Not on the tax bracket...")

