import numpy as np
def main():
    marks = np.array([85, 92, np.nan, 78, 88, np.nan, 91, 76, 95, 89, np.nan, 82])
    print("Original Marks:", marks)

    # Normal average calculation by using np.mean() which will return nan if there are any nan values in the marks 
    print("\nNormal average of the marks (with NaN values):", np.mean(marks))
    # Average calculation by using np.nanmean() which will ignore the nan values in the marks and return the average of the non-nan values 
    print("Average of the marks (ignoring NaN values):", np.nanmean(marks))

    # Missing Values Removal: Remove the nan values from the marks using masking
    count_missing = np.isnan(marks).sum()  # Count the number of missing values
    mask = ~np.isnan(marks)  # Create a mask to filter out nan values
    filtered_marks = marks[mask]  # Apply the mask to get the filtered marks marks without nan values
    print("Number of missing values:", count_missing)
    print("Filtered Marks (without NaN values):", filtered_marks)
    print("\nGrade Assignments:",np.where(marks > 80, "Pass", "Fail"))
    print("\nGrade Assignments:",np.where(np.isnan(marks), "Missing Value", np.where(marks > 80, "Pass", "Fail")))  # Display the array with missing values replaced by a string




if __name__ == "__main__":
    main()