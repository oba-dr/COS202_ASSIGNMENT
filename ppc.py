# ============================================
# PERSONAL POCKET CGPA CALCULATOR (PPC)
# COS202 Assignment
# Name: ________________________
# Matric No: ___________________
# ============================================

print("=" * 50)
print("      PERSONAL POCKET CGPA CALCULATOR")
print("=" * 50)

total_credit_units = 0
total_grade_points = 0

num_courses = int(input("Enter the number of courses: "))

for i in range(1, num_courses + 1):
    print(f"\nCourse {i}")

    course = input("Course Code: ")
    unit = int(input("Credit Unit: "))
    grade = input("Grade (A, B, C, D, E, F): ").upper()

    # Selection Control Statement
    if grade == "A":
        point = 5
    elif grade == "B":
        point = 4
    elif grade == "C":
        point = 3
    elif grade == "D":
        point = 2
    elif grade == "E":
        point = 1
    elif grade == "F":
        point = 0
    else:
        print("Invalid grade! Grade point set to 0.")
        point = 0

    grade_point = unit * point

    total_credit_units += unit
    total_grade_points += grade_point

if total_credit_units > 0:
    cgpa = total_grade_points / total_credit_units
else:
    cgpa = 0

print("\n" + "=" * 50)
print("RESULT")
print("=" * 50)
print(f"Total Credit Units : {total_credit_units}")
print(f"Total Grade Points : {total_grade_points}")
print(f"CGPA               : {cgpa:.2f}")

# Degree Classification
if cgpa >= 4.50:
    print("Class of Degree    : First Class")
elif cgpa >= 3.50:
    print("Class of Degree    : Second Class Upper")
elif cgpa >= 2.40:
    print("Class of Degree    : Second Class Lower")
elif cgpa >= 1.50:
    print("Class of Degree    : Third Class")
elif cgpa >= 1.00:
    print("Class of Degree    : Pass")
else:
    print("Class of Degree    : Fail")

print("=" * 50)

while True:
    print("\nOptions")
    print("1. Calculate Again")
    print("2. OFF")

    option = input("Choose an option: ")

    if option == "1":
        print("\nRestart the program to calculate another CGPA.")
        break
    elif option == "2":
        print("\nThank you for using the Personal Pocket CGPA Calculator.")
        break
    else:
        print("Invalid option. Try again.")
