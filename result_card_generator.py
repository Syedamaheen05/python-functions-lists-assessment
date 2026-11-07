# Student Result Card Generator
# This program calculates a student's result and displays a formatted result card.


# Get valid marks for one subject.
def getValidMarks(subject):
    while True:
        try:
            marks = float(input(f"Enter marks for {subject} (0-100): "))

            if 0 <= marks <= 100:
                return marks

            print("Invalid marks! Enter a value between 0 and 100.")

        except ValueError:
            print("Invalid input! Please enter numeric marks.")


# Get a roll number containing digits only.
def getValidRollNumber():
    while True:
        rollNumber = input("Enter roll number: ").strip()

        if rollNumber.isdigit():
            return rollNumber

        print("Invalid roll number! Use digits only.")


# Calculate percentage using obtained and maximum marks.
def calculatePercentage(total, maxTotal):
    return (total / maxTotal) * 100


# Return the letter grade according to the percentage.
def getGrade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "Fail"


# Clean the student's name by removing extra spaces and capitalizing words.
def formatName(name):
    return name.strip().title()


# Decide the final status, considering the minimum subject marks rule.
def getFinalStatus(subjectMarks, grade):
    for marks in subjectMarks:
        if marks < 40:
            return "Fail"

    if grade == "Fail":
        return "Fail"

    return "Pass"


# Display the student's result in a formatted result card.
def displayResultCard(studentName, rollNumber, subjects, subjectMarks,
                      totalObtainedMarks, percentage, grade, finalStatus):
    print("\n" + "=" * 42)
    print("           STUDENT RESULT CARD")
    print("=" * 42)
    print(f"Student Name : {studentName}")
    print(f"Roll Number : {rollNumber}")
    print("-" * 42)

    for subject, marks in zip(subjects, subjectMarks):
        print(f"{subject:<20} : {marks:>6.2f}")

    print("-" * 42)
    print(f"Total Marks : {totalObtainedMarks:.2f} / 500")
    print(f"Percentage : {percentage:.2f}%")
    print(f"Grade      : {grade}")
    print(f"Final Status: {finalStatus}")
    print("=" * 42)


# Main program starts here.
print("==== Student Result Card Generator ====")

studentName = formatName(input("Enter student name: "))
rollNumber = getValidRollNumber()

subjects = ["English", "Mathematics", "Computer", "Physics", "Chemistry"]
subjectMarks = []

for subject in subjects:
    marks = getValidMarks(subject)
    subjectMarks.append(marks)

totalObtainedMarks = sum(subjectMarks)
maximumTotalMarks = len(subjects) * 100

percentage = calculatePercentage(totalObtainedMarks, maximumTotalMarks)
grade = getGrade(percentage)
finalStatus = getFinalStatus(subjectMarks, grade)

displayResultCard(
    studentName,
    rollNumber,
    subjects,
    subjectMarks,
    totalObtainedMarks,
    percentage,
    grade,
    finalStatus
)
