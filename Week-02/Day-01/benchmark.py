import numpy as np
import time
# Initializing a large list and a large NumPy array for benchmarking
numbers = list(range(1000001))
arr = np.arange(1000001)

# Method 1: Using a for loop to square each number in the list
def python_loop_square(numbers):
    total = 0
    for number in numbers:
        total += number ** 2
    return total

# Method 2: Using NumPy's vectorized operations to square the array
def numpy_vectorized_square(arr):
    return np.sum(arr ** 2)

#Method 3: Using Comprehension to square each number in the list
def python_comprehension_square(numbers):
    return sum([number ** 2 for number in numbers])
# Method 4 for calculating best time and result of a function
def benchmark(func, data,repeats=5):
    best_time = float('inf')
    result = 0
    for _ in range(repeats):
        start_time = time.perf_counter()
        result = func(data)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        if elapsed_time < best_time:
            best_time = elapsed_time
    return result, best_time

# Benchmarking the three methods
loop_result, loop_time = benchmark(python_loop_square, numbers)
numpy_result, numpy_time = benchmark(numpy_vectorized_square, arr) 
comprehension_result, comprehension_time = benchmark(python_comprehension_square, numbers)
# Printing the results
print(f"Python loop result: {loop_result}, Time taken: {loop_time:.6f} seconds")
print(f"NumPy vectorized result: {numpy_result}, Time taken: {numpy_time:.6f} seconds")
print(f"Python comprehension result: {comprehension_result}, Time taken: {comprehension_time:.6f} seconds") 

# Results equal hain?
print("All results equal:", loop_result == comprehension_result == numpy_result)

# NumPy speedup
if numpy_time > 0:
    print(f"NumPy is {loop_time / numpy_time:.2f}x faster than the Python loop")
    print(f"NumPy is {comprehension_time / numpy_time:.2f}x faster than the Python comprehension")
