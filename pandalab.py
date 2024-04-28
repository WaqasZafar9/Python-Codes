import numpy as np
list = [1, 2, 3, 4, 5]
array = np.array(list)
print("NumPy array from Python list:", array)
array1 = np.array([1, 2, 3, 4])
array2 = np.array([5, 6, 7, 8])

result_addition = array1 + array2
print("Addition result:", result_addition)
result_subtraction = array1 - array2
print("Subtraction result:", result_subtraction)
result_multiplication = array1 * array2
print("Multiplication result:", result_multiplication)