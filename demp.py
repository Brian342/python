# Write a program that accepts temperature in degrees Celsius and converts and outputs it in degrees Fahrenheit.

temp = int(input("Enter the Temperature in degree celsius->"))
convert_degree_to_fahrenheit = (temp * (0.9/0.5) + 32)

print("The temperature is->" + str(temp))
print("The temperature in degree fahrenheit is->" + str(convert_degree_to_fahrenheit))


