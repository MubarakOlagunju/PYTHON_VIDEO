#GRADING CALCULATOR

print("--- Grading Calculator ---")

grade1 = int(input("enter first grade: "))
grade2 = int(input("enter second grade: "))
grade3 = int(input("enter third grade: "))

average = (grade1 + grade2 + grade3)/3

if average >= 70:
    print("Excellent")
elif average in range(50, 69):
    print("Good")
else:
    print("Needs Improvement")
    

print("Thanks for watching")