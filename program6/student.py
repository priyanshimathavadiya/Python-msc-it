def get_student():

    roll = int(input("Enter roll no: "))
    name = input("Enter name: ")

    m1 = int(input("Enter subject 1 marks: "))
    m2 = int(input("Enter subject 2 marks: "))
    m3 = int(input("Enter subject 3 marks: "))
    m4 = int(input("Enter subject 4 marks: "))
    m5 = int(input("Enter subject 5 marks: "))

    total = m1 + m2 + m3 + m4 + m5

    per = total / 5

    if per >= 90:
        grade = "A"
    elif per >= 80:
        grade = "B"
    elif per >= 70:
        grade = "C"
    elif per >= 50:
        grade = "D"
    else:
        grade = "F"

    return [total, roll, name, per, grade]