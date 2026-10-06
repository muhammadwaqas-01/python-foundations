from csv_reader import read_students
import json
from pathlib import Path
BASE = Path(__file__).parent

def grade(marks):
    if marks>=90:
        return "A"
    elif marks>=80:
        return "B"
    else:
        return "C"

def safe_open_json(path):
    try:
        with open(path) as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"File not found! {path}")
        return None
    except json.JSONDecodeError:
        print(f"Invalid JSON file! {path}")
        return None


def main():
    students = read_students(BASE/"students.csv")

    if not students:
        print("Students not found!")
        return 

    student_path = BASE/"students.json"

    with open(student_path,"w",) as f:
        json.dump(students,f,indent=2)

    loaded = safe_open_json(student_path)
    print(f"Loaded data is same: {loaded == students}")

    for student in students:
        student["grade"] = grade(student["marks"])

    student_graded = BASE/"student_graded.json"
    with open(student_graded,"w",) as f:
        json.dump(students,f,indent=2)
        print("student_graded.json is created!")

    #print("\nBroken JSON test:")
    #safe_open_json(BASE / "broken.json")

    #print("\nMissing file test:")
    #safe_open_json(BASE / "does_not_exist.json")

if __name__ == "__main__":
    main()