from student import get_student
from ranking import rank_students
from report import display

n = int(input("Enter number of students: "))

students = []

for i in range(n):

    print("\nStudent", i + 1)

    student = get_student()

    students.append(student)

students = rank_students(students)

display(students)