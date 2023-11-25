# Write a program that accepts the weight of a package in grams and then converts it to kilograms and also specifies
# how many such packages form one kilogram. For example, if the user enters the weight (in grams) of the package as 100,
# the output should be;
# The weight of the package is 0.1 kilograms.
# It takes 10 such packages to form one kilogram.
import math

package = int(input("Enter weight of package in grams->"))
convert_grams_to_kilograms = package / 1000

print("The weight of the package is " + str(convert_grams_to_kilograms) + " kilograms")

if package % 1000 == 0:
    print("IT takes " + str(package) + " such packages to form one kilogram")
else:
    print("it takes " + str(math.floor(1000 / (package % 1000))) + " such packages to form one kilogram")




