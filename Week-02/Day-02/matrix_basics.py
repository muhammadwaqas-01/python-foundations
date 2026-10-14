
import numpy as np
def main():
    # Part 1: Dot Product

    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])

    # Manual calculation
    manual_dot = (1 * 4) + (2 * 5) + (3 * 6)

    # NumPy calculation
    numpy_dot = np.dot(a, b)

    print("Dot Product (manual):", manual_dot)
    print("Dot Product (NumPy):", numpy_dot)


    # Part 2: Matrix Multiplication

    A = np.array([
        [1, 2, 3],
        [4, 5, 6]
    ])

    B = np.array([
        [7, 8],
        [9, 10],
        [11, 12]
    ])

    print("\nMatrix A:\n", A)
    print("Matrix A shape:", A.shape)

    print("\nMatrix B:\n", B)
    print("Matrix B shape:", B.shape)

    # Manually calculate the first element of A @ B
    first_element = (1 * 7) + (2 * 9) + (3 * 11)

    print("\nFirst element (manual):", first_element)

    # Matrix multiplication
    result = A @ B

    print("\nA @ B:\n", result)
    print("Result shape:", result.shape)


    # Part 3: Incompatible Matrix Shapes

    try:
        invalid_result = A @ A
        print("\nA @ A:\n", invalid_result)

    except ValueError as error:
        print("\nA @ A failed:", error)
        print("Reason: A has shape (2, 3).")
        print("Inner dimensions 3 and 2 do not match.")


if __name__ == "__main__":
    main()