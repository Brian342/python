# The value of y is calculated as follows:-
# y = 4x3 + 2x – 6                      when x > 5
# y = 3x2 – 4y + 12                     when x < 5
# y = 6x – 5                            when x = 5
# Write a program that accepts the value x and then computes the value of y.
import math

x = int(input("Enter value of x: "))

if x > 5:
    y = 4 * math.pow(x, 3) + (2 * x) - 6
    print(y)
elif x < 5:
    y = 3 * math.pow(x,  2) - (4 * x) + 12
    print(y)
elif x == 5:
    y = 6 * x - 5
    print(y)
else:
    print("Not Applicable")

