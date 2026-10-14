import csv
import numpy as np
from pathlib import Path

csv_path = Path(__file__).parent / "sample.csv"

age = []
marks = []

with open(csv_path, "r", newline="", encoding="utf-8-sig") as file:
    # Ignore empty lines
    reader = csv.DictReader(
        (line for line in file if line.strip())
    )

    print("CSV headers:", reader.fieldnames)

    for row in reader:
        age_value = row["age"].strip()
        marks_value = row["marks"].strip()

        age.append(float(age_value) if age_value else np.nan)
        marks.append(float(marks_value) if marks_value else np.nan)

age = np.array(age, dtype=float)
marks = np.array(marks, dtype=float)


def show_stats(name, values):
    print(f"\n{name} Statistics")
    print("Present values:", np.count_nonzero(~np.isnan(values)))
    print("Minimum:", np.nanmin(values))
    print("Maximum:", np.nanmax(values))
    print("Mean:", f"{np.nanmean(values):.2f}")


show_stats("Age", age)
show_stats("Marks", marks)