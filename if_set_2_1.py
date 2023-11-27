# Write a program that accepts an integer and checks whether
# it is even or odd and then prints an appropriate message.
import re
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even number!!")
elif num % 2 != 0:
    print("odd number")
else:
    print("Not a number!!!")


