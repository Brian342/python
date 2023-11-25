# Write a program that prompts the user for two numbers.
# The program then prompts the user for the operator (+, - , * , / or %).
# The user is the given the answer depending on the operator entered. If he enters an invalid operator,
# he/she should get an error message. See sample dialog below.
# Sample Dialog
# Enter two numbers: 12 15
# Enter an operator: +
# 12 + 15 = 27
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
opera = (input("kindly select your operator (+, -, *, //, %): "))

if opera == '+':
    output = f'{num1} + {num2} = {num1+num2}'
    print(output)
elif opera == '-':
    output = f'{num1} - {num2} = {num1 - num2}'
    print(output)
elif opera == '*':
    output = f'{num1} * {num2} = {num1 * num2}'
    print(output)
elif opera == '//':
    output = f'{num1} // {num2} = {num1 // num2}'
    print(output)
elif opera == '%':
    output = f'{num1} % {num2} = {num1 % num2}'
    print(output)
else:
    print("Not an Operator!!!")

