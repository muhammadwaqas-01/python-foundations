
import numpy as np


def main():
    a = np.arange(20).reshape(4, 5)

    print("Original 2D array:")
    print(a)

    print("\n1. Individual element: second row, third column")
    print(a[1, 2])  # Output: 7

    print("\n2. Complete third row")
    print(a[2, :])  # Output: [10 11 12 13 14]

    print("\n3. Complete second column")
    print(a[:, 1])  # Output: [1 6 11 16]

    print("\n4. Rows 1 to 2, columns 2 to 4")
    print(a[0:2, 1:4])

    print("\n5. Last row using negative indexing")
    print(a[-1, :])  # Output: [15 16 17 18 19]

    print("\n6. Every second column")
    print(a[:, ::2])

    print("\nReverse rows:")
    print(a[::-1, :])

    print("\nReverse columns:")
    print(a[:, ::-1])

    print("\n1D vs 2D column selection:")
    col_1d = a[:, 2]
    col_2d = a[:, 2:3]

    print("1D column:", col_1d)
    print("1D shape:", col_1d.shape)

    print("2D column:\n", col_2d)
    print("2D shape:", col_2d.shape)

    # Integer indexing selects one axis position; slicing preserves that axis.
    # Is liye a[:, 2] ki shape (4,) aur a[:, 2:3] ki shape (4, 1) hai.

    print("\n1D view experiment:")
    x = np.arange(8)
    view = x[2:6]
    view[0] = 100

    print("View:", view)
    print("Original x:", x)

    # Basic slicing view deta hai, is liye view mein tabdeeli original ko badalti hai.

    print("\n1D copy experiment:")
    x = np.arange(8)
    copied = x[2:6].copy()
    copied[0] = 100

    print("Copy:", copied)
    print("Original x:", x)

    print("\n2D view experiment:")
    matrix = np.arange(12).reshape(3, 4)
    view_2d = matrix[0:2, 0:2]

    view_2d[0, 0] = 99

    print("2D view:\n", view_2d)
    print("Original matrix after view modification:\n", matrix)

    print("\n2D copy experiment:")
    matrix = np.arange(12).reshape(3, 4)
    copy_2d = matrix[0:2, 0:2].copy()

    copy_2d[0, 0] = 99

    print("2D copy:\n", copy_2d)
    print("Original matrix after copy modification:\n", matrix)


if __name__ == "__main__":
    main()