# Write a program that accepts the radius of a circle and computes both it’s area and circumference.
import math
pi = 3.142
radius = int(input("Enter the radius->"))
area = pi * pow(radius, 2)
circumference = 2 * pi * radius

print("The radius is: " + str(radius))
print("The area is: " + str(area))
print("The circumference is: " + str(circumference))





