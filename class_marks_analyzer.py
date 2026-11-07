
# Class Marks Analyzer
# This program analyzes marks and displays the class performance.


# Get a valid number of students greater than zero.
def getStudentCount():
    while True:
        try:
            studentCount = int(input("Enter number of students in class: "))

            if studentCount > 0:
                return studentCount

            print("Invalid number! Enter at least one student.")

        except ValueError:
            print("Invalid input! Enter a whole number.")


# Get valid marks between 0 and 100 for one student.
def getValidMark(studentName):
    while True:
        try:
            marks = float(input(f"Enter marks for {studentName} (0-100): "))

            if 0 <= marks <= 100:
                return marks

            print("Invalid marks! Enter a value between 0 and 100.")

        except ValueError:
            print("Invalid input! Please enter numeric marks.")


# Calculate and return the class average.
def calculateClassAverage(studentMarks):
    return sum(studentMarks) / len(studentMarks)


# Find students who achieved a particular mark.
def findStudentsWithMarks(studentNames, studentMarks, targetMarks):
    matchingStudents = []

    for index in range(len(studentMarks)):
        if studentMarks[index] == targetMarks:
            matchingStudents.append(studentNames[index])

    return matchingStudents


# Count passing and failing students.
def countPassFail(studentMarks):
    passingStudents = 0
    failingStudents = 0

    for marks in studentMarks:
        if marks >= 50:
            passingStudents += 1
        else:
            failingStudents += 1

    return passingStudents, failingStudents


# Display students scoring above class average.
def displayAboveAverage(studentNames, studentMarks, classAverage):
    print("\nStudents scoring above class average:")

    foundStudent = False

    for index in range(len(studentMarks)):
        if studentMarks[index] > classAverage:
            print(f"{studentNames[index]}: {studentMarks[index]:.2f}")
            foundStudent = True

    if not foundStudent:
        print("No students scored above the class average.")


# Display students and their marks from highest to lowest.
def displaySortedMarks(studentNames, studentMarks):
    sortedStudentIndexes = sorted(
        range(len(studentMarks)),
        key=lambda index: studentMarks[index],
        reverse=True
    )

    print("\nStudent marks sorted from highest to lowest:")

    for index in sortedStudentIndexes:
        print(f"{studentNames[index]}: {studentMarks[index]:.2f}")


# Display the class performance summary.
def displayClassSummary(studentNames, studentMarks, classAverage,
                       highestMarks, lowestMarks, passingStudents,
                       failingStudents):

    highestStudents = findStudentsWithMarks(
        studentNames, studentMarks, highestMarks
    )

    lowestStudents = findStudentsWithMarks(
        studentNames, studentMarks, lowestMarks
    )

    print("\n" + "=" * 42)
    print("          CLASS MARKS ANALYSIS")
    print("=" * 42)

    print(f"Class Average    : {classAverage:.2f}")
    print(f"Highest Marks    : {highestMarks:.2f}")
    print(f"Achieved by      : {', '.join(highestStudents)}")
    print(f"Lowest Marks     : {lowestMarks:.2f}")
    print(f"Achieved by      : {', '.join(lowestStudents)}")
    print(f"Passing Students : {passingStudents}")
    print(f"Failing Students : {failingStudents}")

    print("=" * 42)


# Main program starts here.
print("==== Class Marks Analyzer ====")

studentNames = []
studentMarks = []

studentCount = getStudentCount()

for studentNumber in range(1, studentCount + 1):

    print(f"\nStudent {studentNumber}")

    studentName = input("Enter student name: ").strip().title()
    marks = getValidMark(studentName)

    studentNames.append(studentName)
    studentMarks.append(marks)

classAverage = calculateClassAverage(studentMarks)

highestMarks = max(studentMarks)
lowestMarks = min(studentMarks)

passingStudents, failingStudents = countPassFail(studentMarks)

displayClassSummary(
    studentNames,
    studentMarks,
    classAverage,
    highestMarks,
    lowestMarks,
    passingStudents,
    failingStudents
)

displayAboveAverage(studentNames, studentMarks, classAverage)

displaySortedMarks(studentNames, studentMarks)
