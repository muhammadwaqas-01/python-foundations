from pathlib import Path
import csv
from math_utils import average


BASE = Path(__file__).parent
path = BASE / "students.csv"


def read_students(path):
    try:
        with open(path, newline="") as f:
            reader = csv.DictReader(f)

            students = []

            for row in reader:
                name = row["name"].strip()
                marks_text = row["marks"].strip()

                # Name ya marks missing hain
                if not name or not marks_text:
                    print("Invalid student data found. Student skipped.")
                    continue

                # Marks number nahi hain
                try:
                    marks = int(marks_text)
                except ValueError:
                    print(f"Invalid marks for {name}. Student skipped.")
                    continue

                # Marks -1 hain
                if marks == -1:
                    print(f"Marks missing for {name}. Student skipped.")
                    continue

                student = {
                    "name": name,
                    "marks": marks
                }

                students.append(student)

            return students

    except FileNotFoundError:
        print("students.csv file not found!")
        return []


def main():
    students = read_students(path)

    if not students:
        print("No students found")
        return

    # Total students
    total_students = len(students)
    print("Total Students:", total_students)

    # Average marks
    all_marks = [student["marks"] for student in students]
    avg_marks = average(all_marks)
    print("Average marks:", avg_marks)

    # Highest marks
    top_student = max(
        students,
        key=lambda student: student["marks"]
    )

    print(
        "Highest marks:",
        top_student["name"],
        top_student["marks"]
    )

    # Above average
    above_avg = [
        student["name"]
        for student in students
        if student["marks"] > avg_marks
    ]

    print("Above avg students:", above_avg)


if __name__ == "__main__":
    main()