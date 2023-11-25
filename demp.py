# Write a program that accepts a number and then outputs its square, cube, square root and cube root.
import math
number = int(input("Enter a number->"))
square = math.pow(number, 2)
cube = math.pow(number, 3)
sqrt = math.sqrt(number)
cubeRoot = math.cbrt(number)

output = (f'the square is->{math.floor(square)}, The cube is->{math.floor(cube)}, The sqrt is->{math.floor(sqrt)}'
          f', The cube-root is->{cubeRoot}')

print(output)





