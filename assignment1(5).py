n = int(input("Enter total students: "))

# Get 5 subject names from user
subjects = []

for i in range(5):
    subject = input("Enter subject " + str(i + 1) + ": ")
    subjects.append(subject)

students = []

# Get student details
for i in range(n):

    print("\nStudent", i + 1)

    roll = input("Enter Roll No: ")
    name = input("Enter Name: ")

    marks = []

    # Get marks for 5 subjects
    for j in range(5):
        mark = int(input("Enter marks for " + subjects[j] + ": "))
        marks.append(mark)

    total = sum(marks)
    percentage = total / 5

    # Grade
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    students.append([roll, name, marks, total, percentage, grade])


# Sort by total marks
for i in range(n):
    for j in range(i + 1, n):

        if students[i][3] < students[j][3]:
            students[i], students[j] = students[j], students[i]


# Assign rank
for i in range(n):

    if i == 0:
        rank = 1

    elif students[i][3] == students[i - 1][3]:
        rank = students[i - 1][6]

    else:
        rank = i + 1

    students[i].append(rank)


# Display result
print("\n")
print("Rank\tRoll\tName", end="\t")

for subject in subjects:
    print(subject, end="\t")

print("Total\tPercentage\tGrade")


for s in students:

    print(s[6], "\t", s[0], "\t", s[1], end="\t")

    for mark in s[2]:
        print(mark, end="\t")

    print(s[3], "\t", s[4], "\t\t", s[5])
