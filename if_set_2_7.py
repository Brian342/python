# Write a program that accepts an integer and checks whether it is positive,
# negative or zero and then prints an appropriate message.

number = int(input("Enter a number->"))

if number < 0:
    print("NEGATIVE!")
elif number > 0:
    print("POSITIVE!")
else:
    print("ZERO")