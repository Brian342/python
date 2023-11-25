# Write a program that accepts distance traveled in metres and the time taken in
# minutes and then outputs the speed in kilometers per hour (km/h). E.g. if someone enters a distance (in metres)
# of 500 and a time (in minutes) of 15 the output for speed should be 2 km/h.
import math

distance = int(input("Enter distance in metres->"))
time = int(input("Enter time in minutes->"))

convert_distance_to_kilometres = distance / 1000
convert_minutes_to_hour = time / 60

speed = math.floor(convert_distance_to_kilometres / convert_minutes_to_hour)

print("The speed is->" + str(speed) + " Km/h")

