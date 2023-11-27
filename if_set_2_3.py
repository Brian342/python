# In a certain organization, employees are taxed depending on their gender
# and amount of money they earn. The criterion is shown below.
# Employee                          Tax Rate
# Female earning < 15000                12%
# Female earning >= 15000               14%
# Male earning < 14000                  13%
# Male earning >= 14000                 15%
# a) Write a program to implement the above.
print("What Gender are you\n"
      "1) Male\n"
      "2) Female\n")
gender = str(input("Kindly enter your Gender: "))
earning = int(input("Enter Your earning: "))

if gender == 'male' or 'Male' and earning >= 14000:
    tax_amount = earning * 13.0 / 100
    output = f'The Gender is Male. Your earning is {earning}. The tax amount is. {tax_amount}. '
    print(output)
elif gender == 'male' or 'Male' and earning < 14000:
    tax_amount = earning * 15.0 / 100
    output = f'The Gender  is Male. Your earning is {earning}. The tax amount is. {tax_amount}. '
    print(output)
elif gender == 'female' or 'Female' and earning >= 15000:
    tax_amount = earning * 14.0 / 100
    output = f'The Gender  is Female. Your earning is {earning}. The tax amount is. {tax_amount}. '
    print(output)
elif gender == 'female' or 'Female' and earning < 15000:
    tax_amount = earning * 12.0 / 100
    output = f'The Gender  is Female. Your earning is {earning}. The tax amount is. {tax_amount}. '
    print(output)
else:
    print("Not on the Tax Bracket")
