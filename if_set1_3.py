# Write a program to read a value from the keyboard and output the phrase NEGATIVE if the number is negative,
# POSITIVE if the number is positive or ZERO otherwise.
value = int(input("Enter a value from the keyboard: "))

if value < 0:
    print("NEGATIVE")
elif value > 0:
    print("POSITIVE")
else:
    print("ZERO")


