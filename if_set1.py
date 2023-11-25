# Write a program that when run, produces a menu showing beer brands and their prices
# and then prompts the user enter his/her choice (1,2,3 or 4).
# The user is then asked how many bottles he/she wants. He is then given
# the total cost (depending on the cost of the beer chosen) as the output.
# See sample dialog below. If he/she enters an invalid choice e.g. 8, he/she should get an error message.
# Sample dialog
# * * * * Jamal and Daughters Pub * * * *
# Beer Brand                       Price
# 1) Tusker                         100/=
# 2) Pilsner                        120/=
# 3) Smirnoff Ice                   140/=
# 4) White Cap                       90/=
# Enter your choice: 2
# How many bottles of pilsner do you want? 11
# 11 bottles of pilsner will cost you Kshs. 1320
print("* * * Jamal and Daughters pub * * * \n"
      "Beer Brand                       Price\n"
      "1) Tusker                        100\n"
      "2) Pilsner                       120\n"
      "3) Smirnoff_ice                  140\n"
      "4) White_cap                      90\n")
choice = int(input("Select your Poison(1,2,3,4): "))
bottles = int(input("How many bottles do you want?: "))

if choice == 1:
    message = f'{bottles} bottles of Tusker will cost you {bottles * 100} Kshs'
    print(message)
elif choice == 2:
    message = f"{bottles} bottles of Pilsner will cost you {bottles * 120} Kshs"
    print(message)
elif choice == 3:
    message = f'{bottles} bottles of Smirnoff_ice will cost you {bottles * 140} Kshs'
    print(message)
elif choice == 4:
    message = f"{bottles} bottles of White_cap will cost you {bottles * 90} kshs"
    print(message)
else:
    print("Not on the menu!!!")


