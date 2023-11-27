# In the Jomo Kenyatta University Diploma program, a student takes five units each semester.
# The student is then graded using the following criteria: -
# Average Mark                      Order of Merit
# 75 – 100                          Distinction
# 65 – 75                           Credit
# 50 – 65                           Pass
# 0 – 50                            Fail.
# Write a program that accepts marks scored in five subjects and then computes the average
# and prints the order of merit based on the average mark.
subj1 = int(input("Enter subject1: "))
subj2 = int(input("Enter subject2: "))
subj3 = int(input("Enter subject3: "))
subj4 = int(input("Enter subject4: "))
subj5 = int(input("Enter subject5: "))

total = subj1 + subj2 + subj3 + subj4 + subj5
average = total / 5.0

if 75 < average < 100:
    print("congratulation you have attained a Distinction!")
elif 65 < average <= 75:
    print("congratulation you have attained a Credit!")
elif 50 < average <= 65:
    print("congratulation you have attained a pass1")
elif 0 < average <= 50:
    print("you have attained a fail!")
else:
    print("Not on The Grading Merit!!")





