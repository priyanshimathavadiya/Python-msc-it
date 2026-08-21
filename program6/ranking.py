def rank_students(students):

    students.sort(reverse=True)

    rank = 1

    for i in range(len(students)):

        if i > 0:
            if students[i][0] == students[i-1][0]:
                rank = rank
            else:
                rank = i + 1

        students[i].append(rank)

    return students