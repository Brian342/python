# Write a program that prompts the user for two numbers and then computes them using the following rules.
# If the first number is greater than the second one, the second number is subtracted from the first one.
# If the second number is greater than the first one, the first number is divided by the second one.
# Otherwise, the two numbers are added.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
    print("num1 - num2 = " + str(num1-num2))
elif num1 < num2:
    print("num2 // num1 = " + str(num1 / num2))
else:
    print("Num1 + num2 = " + str(num1 + num2))


