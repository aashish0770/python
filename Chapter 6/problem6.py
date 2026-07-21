# problem6.py
# Que: to calculate the grade of a student from his marks from the following schema:
# 90-100 = A
# 80-89 = B
# 70-79 = C
# 60-69 = D
# 0-59 = E

marks = int(input("Enter marks: "))
if marks < 0 or marks > 100:
    print("Invalid marks")
elif marks >= 90 and marks <= 100:
    print("A")
elif marks >= 80 and marks <= 89:
    print("B")
elif marks >= 70 and marks <= 79:
    print("C")
elif marks >= 60 and marks <= 69:
    print("D")
else:
    print("E")
