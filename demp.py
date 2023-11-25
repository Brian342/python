# Write a program that accepts measurements in cm and converts them into metres.
# If someone enters 200 for example, the output should take the form;
# 200 cm = 2 metres.
number = int(input("Enter a number in cm-> "))

convert_cm_to_metres = number // 100
print(str(number) + "cm " " = " + str(convert_cm_to_metres) + " metres")



