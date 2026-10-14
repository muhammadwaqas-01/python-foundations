
import numpy as np
def main():
    # Part A: Broadcasting
    
    m = np.arange(12).reshape(3, 4)
    
    print("Original Array:\n", m)
    print("Original Shape:", m.shape)
    
    # 1. Add a row vector
    row_vector = np.array([10, 20, 30, 40])
    
    row_result = m + row_vector
    
    print("\nRow Vector:", row_vector)
    print("Row Vector Shape:", row_vector.shape)
    print("Result after Row Vector Addition:\n", row_result)
    print("Result Shape:", row_result.shape)
    
    # 2. Add a column vector
    column_vector = np.array([[100], [200], [300]])
    
    column_result = m + column_vector
    
    print("\nColumn Vector:\n", column_vector)
    print("Column Vector Shape:", column_vector.shape)
    print("Result after Column Vector Addition:\n", column_result)
    print("Result Shape:", column_result.shape)
    
    # 3. Handle incompatible shapes
    incompatible_vector = np.array([1, 2, 3])
    
    try:
        result = m + incompatible_vector
        print(result)
    except ValueError as error:
        print("\nBroadcasting Error:", error)
        # Shapes are compared from the right:
        # 4 and 3 do not match, and neither dimension is 1.
    
    # Part B: Z-scores
    
    marks = np.array([
        [70, 75, 80],
        [72, 78, 82],
        [68, 74, 79],
        [75, 80, 85],
        [71, 76, 81],
        [73, 150, 83]
    ], dtype=float)
    
    print("\nMarks Array:\n", marks)
    print("Marks Shape:", marks.shape)
    
    # Calculate mean and standard deviation per column
    column_means = marks.mean(axis=0)
    column_stds = marks.std(axis=0)
    
    # Calculate z-scores per subject
    z = (marks - column_means) / column_stds
    
    print("\nColumn Means:", column_means)
    print("Column Standard Deviations:", column_stds)
    
    print("\nZ-scores:\n", np.round(z, 2))
    
    # Verify standardized columns
    print("\nMean of Each Z-score Column:",
          np.round(z.mean(axis=0), 2))
    
    print("Standard Deviation of Each Z-score Column:",
          np.round(z.std(axis=0), 2))
    
    # Identify potential outliers
    outlier_mask = np.abs(z) > 1.5
    
    print("\nOutlier Mask:\n", outlier_mask)
    print("\nFlagged Marks:\n", marks[outlier_mask])
    print("Number of Flagged Values:", outlier_mask.sum())

if __name__ == "__main__":
    main()