# Python Functions & Lists Assessment

A beginner-friendly Python assessment project containing two console applications: a Student Result Card Generator and a Class Marks Analyzer. The programs demonstrate functions, input validation, string manipulation, lists, loops, and basic data analysis.

## Project Structure

```text
python-functions-lists-assessment/
├── result_card_generator.py
├── class_marks_analyzer.py
└── README.md
```

## Programs

### 1. Student Result Card Generator

`result_card_generator.py` collects a student's name, roll number, and marks in five subjects. It calculates total marks and percentage, assigns a grade, checks the minimum subject marks rule, and prints a formatted result card.

**Features**
- Validates marks between 0 and 100.
- Validates roll numbers using `.isdigit()`.
- Formats names using `.strip()` and `.title()`.
- Calculates percentage and grade.
- Assigns **Fail** if any subject mark is below 40, regardless of percentage.
- Displays subject marks, total, percentage, grade, and final status.

**Functions**
- `getValidMarks(subject)` — collects valid marks for a subject.
- `getValidRollNumber()` — accepts a digits-only roll number.
- `calculatePercentage(total, maxTotal)` — calculates percentage.
- `getGrade(percentage)` — returns the letter grade.
- `formatName(name)` — cleans and formats a student's name.
- `getFinalStatus(subjectMarks, grade)` — applies the final pass/fail rules.
- `displayResultCard(...)` — prints the result card.

### 2. Class Marks Analyzer

`class_marks_analyzer.py` collects names and marks for all students in a class and summarizes their performance.

**Features**
- Validates the class size and every student's marks.
- Stores names and marks in separate lists.
- Calculates class average, highest marks, and lowest marks.
- Identifies students with the highest and lowest marks, including ties.
- Counts passing students (50 or above) and failing students (below 50).
- Displays students scoring above the class average.
- Displays marks sorted from highest to lowest.

**Functions**
- `getStudentCount()` — validates the number of students.
- `getValidMark(studentName)` — collects valid marks for a student.
- `calculateClassAverage(studentMarks)` — calculates the class average.
- `findStudentsWithMarks(...)` — finds students with matching marks.
- `countPassFail(studentMarks)` — counts passing and failing students.
- `displayAboveAverage(...)` — displays above-average students.
- `displaySortedMarks(...)` — displays marks in descending order.
- `displayClassSummary(...)` — prints the class summary.

## Python Concepts Used

- User-defined functions (`def`)
- Parameters and return values
- Lists and list methods (`append()`, `len()`)
- Built-in functions (`sum()`, `max()`, `min()`, `sorted()`)
- `for` and `while` loops
- `if`, `elif`, and `else`
- Input validation with `try` and `except`
- String methods (`strip()`, `title()`, `isdigit()`)
- f-strings and formatted output
- `zip()` for pairing subjects with marks

## Requirements

- Python 3 installed on your computer.
- A terminal, PowerShell, or VS Code.

## How to Run

Open the project folder in VS Code or a terminal.

Run the Result Card Generator:

```bash
python result_card_generator.py
```

Run the Class Marks Analyzer:

```bash
python class_marks_analyzer.py
```

On some Windows installations, you can use `py` instead of `python`.

## Sample Input and Output

### Student Result Card Generator

**Sample input**

```text
Enter student name:   maheen bukhari
Enter roll number: 12345
Enter marks for English (0-100): 92
Enter marks for Mathematics (0-100): 85
Enter marks for Computer (0-100): 95
Enter marks for Physics (0-100): 78
Enter marks for Chemistry (0-100): 88
```

**Sample output**

```text
==========================================
           STUDENT RESULT CARD
==========================================
Student Name : Maheen Bukhari
Roll Number : 12345
------------------------------------------
English              :  92.00
Mathematics          :  85.00
Computer             :  95.00
Physics              :  78.00
Chemistry            :  88.00
------------------------------------------
Total Marks : 438.00 / 500
Percentage : 87.60%
Grade      : A
Final Status: Pass
==========================================
```

### Class Marks Analyzer

**Sample input**

```text
Enter number of students in class: 3

Student 1
Enter student name: Ali
Enter marks for Ali (0-100): 75

Student 2
Enter student name: Sara
Enter marks for Sara (0-100): 90

Student 3
Enter student name: Ahmed
Enter marks for Ahmed (0-100): 45
```

**Sample output**

```text
==========================================
          CLASS MARKS ANALYSIS
==========================================
Class Average : 70.00
Highest Marks: 90.00
Achieved by  : Sara
Lowest Marks : 45.00
Achieved by  : Ahmed
Passing Students: 2
Failing Students: 1
==========================================

Students scoring above class average:
Sara: 90.00

Student marks sorted from highest to lowest:
90.00
75.00
45.00
```


## Assessment Notes

- Both programs are separate and run independently.
- Function names use camelCase for consistency with the requested coding style.
- Each function is designed around one clear responsibility.
- Input validation prevents invalid marks and invalid class sizes from being accepted.
