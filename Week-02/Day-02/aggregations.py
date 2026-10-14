import numpy as np
def main():
    # 5 Students with their scores in 3 subjects
    marks = np.array([
                    [85, 90, 78],
                    [92, 88, 95],
                    [76, 82, 80],
                    [88, 91, 89],
                    [95, 85, 92]])
    # Original shape of the array is (5, 3) => 5 rows and 3 columns
    print("Marks Array:\n", marks)
    print("Shape of the array:", marks.shape)
    print("Total number of elements:", marks.size)
    # Row-wise Aggregation (Sum of marks for each student)
    students_totals = np.sum(marks, axis=1)
    print("\nSum of marks for each student (row-wise):", students_totals)
    print("Shape of the sum array:", students_totals.shape)
    print("Expected shape of the sum array(5,):", students_totals.shape == (5,))
    # Column-wise Aggregation (Average marks for each subject)
    students_averages = np.mean(marks, axis=0)
    print("\nAverage marks for each subject (column-wise):", students_averages)
    print("Shape of the average array:", students_averages.shape)
    print("Expected shape of the average array(3,):", students_averages.shape == (3,))

    # Overall Aggregate Functions
    overall_sum = np.sum(marks)
    print("\nOverall sum of all marks:", overall_sum)
    overall_average = np.mean(marks)
    print("Overall average of all marks:", overall_average)
    overall_max = np.max(marks)
    print("Overall maximum mark:", overall_max)
    overall_min = np.min(marks)
    print("Overall minimum mark:", overall_min)
    overall_std = np.std(marks)
    print("Overall standard deviation of marks:", overall_std)
    overall_mean = np.mean(marks)
    print("Overall mean of marks:", overall_mean)
    overall_median = np.median(marks)
    print("Overall median of marks:", overall_median)
    overall_percentile_90 = np.percentile(marks, 90)
    print("Overall 90th percentile of marks:", overall_percentile_90)

    # Top 1 student based on total marks
    top_student_index = np.argmax(students_totals)
    print("\nIndex of the top student:", top_student_index)
    print("Total marks of the top student:", students_totals[top_student_index])

    # Using Slicing to get the marks of all students
    student_1_marks = marks[0]
    print("\nMarks for Student 1:", student_1_marks)
    student_2_marks = marks[1]
    print("Marks for Student 2:", student_2_marks)
    student_3_marks = marks[2]
    print("Marks for Student 3:", student_3_marks)
    student_4_marks = marks[3]
    print("Marks for Student 4:", student_4_marks)
    student_5_marks = marks[4]
    print("Marks for Student 5:", student_5_marks)

    # Top 1 student based on total marks
    # Student 1: [85, 90, 78] => Total: 253
    # Manual Calculation: 85 + 90 + 78 = 253
    print("\nManual Calculation of Total Marks for Student 1:", 85 + 90 + 78)
    print("\nTotal Marks for Student 1 from the array:", students_totals[0])
    print("\nMatching Total Marks for Student 1 from the  numpy array:", students_totals[0] == (85 + 90 + 78))


    # Manual Verification of the average marks for one subject
    manual_average_subject_1 = (85 + 92 + 76 + 88 + 95)/5

    print("\nManual average marks for Subject 1:", manual_average_subject_1)
    print("\nMatching average marks for Subject 1 from the array :", students_averages[0])
    print("\nMatching average marks for Subject 1 from the array:", students_averages[0] == (85 + 92 + 76 + 88 + 95)/5)

    manual_average_subject_2 = (90 + 88 + 82 + 91 + 85)/5
    print("\nManual average marks for Subject 2:", manual_average_subject_2)
    print("\nMatching average marks for Subject 2 from the array:", students_averages[1])
    print("\nMatching average marks for Subject 2 from the array:", students_averages[1] == (90 + 88 + 82 + 91 + 85)/5)

    manual_average_subject_3 = (78 + 95 + 80 + 89 + 92)/5
    print("\nManual average marks for Subject 3:", manual_average_subject_3)
    print("\nMatching average marks for Subject 3 from the array:", students_averages[2])
    print("\nMatching average marks for Subject 3 from the array:", students_averages[2] == (78 + 95 + 80 + 89 + 92)/5)

if __name__ == "__main__":
    main()