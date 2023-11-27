# A number is said to be evenly divisible by 9 if it is divisible by 9 and at the same time it is even.
# For example 18 is evenly divisible by 9 but 27 is not. A program is required that accepts an integer and checks
# whether it is evenly divisible by 9 or not and then prints an appropriate message
number = int(input("Enter a number: "))

if number % 9 == 0 and number % 2 == 0:
    print("This number is Evenly Divisible by 9!!")
elif number % 9 == 0 and number % 2 != 0:
    print("This number is not Evenly divisible by 9!!")

