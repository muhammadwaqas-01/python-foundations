
import numpy as np


def describe(name, array):
    print(f"\n{name}:")
    print(array)
    print("dtype:", array.dtype)
    print("size:", array.size)
    print("shape:", array.shape)
    print("ndim:", array.ndim)


def main():
    zeros = np.zeros(10)
    arr = np.array([1, 2, 3, 4, 5])
    ones = np.ones(12)
    range_arr = np.arange(2, 10)
    numbers = np.linspace(1, 100, 10)

    describe("Zeros Array", zeros)
    describe("Array", arr)
    describe("Ones Array", ones)
    describe("Range Array", range_arr)
    describe("Numbers Array", numbers)

    print("\nArray DataType Experiment:")

    # The elements are integers, so NumPy selects an integer dtype.
    print(np.array([1, 2, 3]).dtype)

    # Since one element is a float, all elements are converted to floats.
    print(np.array([1, 2, 3.5]).dtype)

    # Mixing integers and strings creates a Unicode string dtype.
    # The numbers are also converted to strings, such as "1" and "2".
    # U21 means each element can contain up to 21 Unicode characters.
    print(np.array([1, 2, "hi"]).dtype)

    # Prediction: There will be 2 rows and 3 columns.
    # Therefore, I expect the shape to be (2, 3) and ndim to be 2.
    arr_2d = np.array([
        [1, 2, 3],
        [4, 5, 6]
    ])

    describe("2D Array", arr_2d)


if __name__ == "__main__":
    main()
