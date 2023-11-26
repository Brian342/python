# Write a program that can be used by a policeman to determine if a vehicle has exceeded the speed limit and to levy
# a fine.The policeman should enter the vehicles speed and the speed limit.
# If the speed limit is exceeded by less than 30kph a fine of Kshs.
# 2500 should be charged. Otherwise, a fine of Kshs 4000 is charged.
# Your program should then output (in a suitable format) the vehicle speed,
# the speed limit, the excess speed and the fine levied.

vehicleSpeed = int(input("Enter the vehicle speed: "))
speedLimit = int(input("Enter the speed limit: "))

excessSpeed = vehicleSpeed - speedLimit
fineLevied = speedLimit + 30
if speedLimit < vehicleSpeed < fineLevied:
    output = (f'The speed limit is: {speedLimit}, The VehicleSpeed is: {vehicleSpeed},The excessSpeed is:{excessSpeed},'
              f'Your fine will be 2500Kshs!')
    print(output)
elif vehicleSpeed > fineLevied:
    output = (f'The speed limit is: {speedLimit}, The VehicleSpeed is: {vehicleSpeed},The excessSpeed is:{excessSpeed},'
              f'Your fine will be 4000Kshs!')
    print(output)
else:
    print("you are traveling at the right speed have a safe journey!!!")

