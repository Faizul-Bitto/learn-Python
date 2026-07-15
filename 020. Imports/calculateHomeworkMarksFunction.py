def calculateHomeworkMarks(homeWorkAssignmentGrades):
    sumOfMarks = 0

    for x in homeWorkAssignmentGrades.values():
        sumOfMarks += x

    averageGrade = round(sumOfMarks / len(homeWorkAssignmentGrades), 2)

    print(averageGrade)
