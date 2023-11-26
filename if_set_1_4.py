# Write a program that computes the area & perimeter of either a rectangle,
# a circle or a right-angled triangle. The program should display a menu that enables the user to
# select the type of figure whose area & perimeter he/she wants to compute. Depending on the users choice,
# the program should prompt for the dimensions and perform the computations. The output should be: -
# The type of figure, the dimensions, the area and the perimeter.
# (NB:The calculation should be for only one figure at any one time.)
import math
pi = 3.142

print("Types of figures available!!!\n"
      "1)   Rectangle\n"
      "2)   Circle\n"
      "3)   rightAngleTriangle\n")

figure = int(input("Kindly select type of figure: "))
if figure == 1:
    length = int(input("Enter the length: "))
    width = int(input("Enter the width: "))
    area = length * width
    perimeter = 2 * (length * width)
    output = (f'The type of figure is Rectangle, The dimensions are-> length {length}, width {width} The area is {area} '
              f'The perimeter is {perimeter}.')
    print(output)
elif figure == 2:
    radius = int(input("Enter the radius: "))
    area = pi * radius * radius
    circumference = 2 * pi * radius
    output = (f'The type of figure is circle, The radius is {radius}, The area is {area} '
              f'The circumference is {circumference}.')
    print(output)
elif figure == 3:
    height = int(input("Enter the height: "))
    base = int(input("Enter the base: "))
    area = base + height + math.sqrt(math.pow(base, 2) + math.pow(height, 2))
    perimeter = base * height / 2
    output = (f'The type of figure is Right angled triangle, The dimensions are-> base {base}, height {height}, '
              f'The area is {area}, The perimeter is {perimeter}.')
    print(output)
else:
    print("Not on the list of figures!!!")



