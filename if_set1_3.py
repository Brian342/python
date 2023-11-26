# Write a program that accepts two numbers and divides the bigger number by the smaller number and displays the results.
# The program should display an error message (and not perform the calculation) if the smaller number is zero.
num1 = int(input("Enter number1: "))
num2 = int(input("Enter number2: "))

if num1 > num2:
    print("num1 / num2: " + str(num1 / num2))
elif num1 < num2:
    print("num2 / num1: " + str(num2 / num1))
elif num1 <= 0 or num2 <= 0:
    print("Error can't divide by a zero value!!")


