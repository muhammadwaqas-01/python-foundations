import numpy as np

marks = np.array([85, 92, 78, 88, 91, 76, 95, 82, 89])

mean_marks = round(np.mean(marks), 2)
min_marks = np.min(marks)
max_marks = np.max(marks)

print(f"Mean Marks: {mean_marks}")
print("Mean matches:", mean_marks == 86.22)
print(f"Minimum Marks: {min_marks}")
print("Minimum matches:", min_marks == 76)
print(f"Maximum Marks: {max_marks}")
print("Maximum matches:", max_marks == 95)