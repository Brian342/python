# Write a program that accepts the width and length of a rectangle and computes both it’s area and perimeter.

length = int(input("Enter the length: "))
width = int(input("Enter the width: "))

area = length * width
perimeter = 2 * (length + width)

print("The length is->" + str(length), "The width is->" + str(width))
print("The area is: " + str(area))
print("The perimeter is: " + str(perimeter))




