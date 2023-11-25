# Write a program that accepts measurements in kilometers and the converts and displays them in metres.
# E.g. if someone enters 0.4 (kilometers) the output should take the form 0.4 kilometers = 400 metres.
import math

measurements = float(input("Enter measurement in Kilometres->"))
convert_kilometers_to_metres = measurements * 1000
output = f'{measurements} kilometers = {math.floor(convert_kilometers_to_metres)} metres.'
print(output)


