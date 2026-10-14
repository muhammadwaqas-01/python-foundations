import numpy as np

def main():
    b = np.array([10, 20, 30, 40])
    # Vectorized Operations
    a = np.array([1, 2, 3, 4])
    print("Array a:", a)
    print("Array b:", b)
    print("Vectorized Operations:\n")
    print("Addition(a + b):", a + b)
    print("Subtraction(a - b):", a - b)
    print("Multiplication(a * b):", a * b)
    print("Division(a / b):", a / b)
    print("Exponentiation(a ** 2):", a ** 2)
    # Scalar Operations
    print("\nScalar Operations:\n")
    print("Scalar Multiplication(a * 10):", a * 10)
    print("Scalar Addition(a + 2):", a + 2)
    print("Scalar Subtraction(a - 1):", a - 1)
    print("Scalar Division(a / 2):", a / 2)

    #Universal Functions (ufuncs)
    print("\nUniversal Functions (ufuncs):\n")
    print("Square Root(np.sqrt(a)):", np.sqrt(a))
    print("Absolute Value(np.abs()):", np.abs(np.array([-1, -2, -3, -4])))

    # Comparison Operations
    print("\nComparison Operations:\n")
    comparison = a > 2
    print("Comparison (a > 2):", comparison)
    print("Type of comparison result:", comparison.dtype)

    # Python list Vs NumPy array
    print("\nPython List vs NumPy Array:\n")
    python_list = [1, 2, 3, 4]
    numpy_array = np.array([1, 2, 3, 4])
    # The following operation will work for both Python lists and NumPy arrays, but the results will be different.
    # python_list*2 will concatenate the list with itself, resulting in [1, 2, 3, 4, 1, 2, 3, 4].
    print("Python List:", python_list*2)
    # numpy_array*2 will perform element-wise multiplication, resulting in [2, 4, 6, 8].
    print("NumPy Array:", numpy_array*2)

    array1 = np.array([1, 2, 3])
    array2 = np.array([4, 5, 6,7])
    # Its gives an error because the shapes of the arrays are not compatible for broadcasting.
    print("\nBroadcasting Error Example:\n")
    try:
        result = array1 + array2
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()