# problem2.py
# Que: to find out whether a student has passed or failed if it requires a total of 40%
# and at least 33% in each subject to pass. Assume 3 subjects and tajke marks as an input from the user.
sub1 = int(input("Enter marks in subject 1: "))
sub2 = int(input("Enter marks in subject 2: "))
sub3 = int(input("Enter marks in subject 3: "))

total = sub1 + sub2 + sub3
avg = total / 3
if sub1 >= 33 and sub2 >= 33 and sub3 >= 33:
    if (sub1 + sub2 + sub3) / 3 >= 40:
        print("The student has passed.")
        print("The average marks is:", avg)
        print("The total marks is:", total)
    else:
        print("The student has failed. The average should be at least 40%.")
        print("The average marks is:", avg)
        print("The total marks is:", total)
else:
    print("The student has failed.")
    print("The average marks is:", avg)
    print("The total marks is:", total)
