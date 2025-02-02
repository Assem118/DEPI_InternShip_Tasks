import numpy as np

# 1. Broadcasting
# a) Add a 1D array `[1, 2, 3]` to each row of a 2D array `[[10, 20, 30], [40, 50, 60]]`.
arr_2d = np.array([[10, 20, 30], [40, 50, 60]])
arr_1d = np.array([1, 2, 3])
result_1a = arr_2d + arr_1d
print("1a) Result:\n", result_1a)

# b) Multiply a 2D array `[[1, 2], [3, 4]]` by a 1D array `[10, 20]` column-wise.
arr_2d = np.array([[1, 2], [3, 4]])
arr_1d = np.array([10, 20])
result_1b = arr_2d * arr_1d[:, np.newaxis]
print("1b) Result:\n", result_1b)

# 2. Indexing and Slicing (High Dimensional Arrays)
arr = np.arange(1, 25).reshape(2, 3, 4)

# a) Extract the second slice along axis 0.
result_2a = arr[1]
print("2a) Result:\n", result_2a)

# b) Extract all rows and the last column for all slices.
result_2b = arr[:, :, -1]
print("2b) Result:\n", result_2b)

# c) Reverse the order of slices along axis 0.
result_2c = arr[::-1]
print("2c) Result:\n", result_2c)

# d) Set all even elements in the array to -1.
arr_even = arr.copy()
arr_even[arr_even % 2 == 0] = -1
print("2d) Result:\n", arr_even)

# 3. np.repeat
# a) Given `arr = np.array([1, 2, 3, 4, 5, 6])`, create a new array where every odd element is repeated twice.
arr = np.array([1, 2, 3, 4, 5, 6])
repeats = np.where(arr % 2 != 0, 2, 1)
result_3a = np.repeat(arr, repeats)
print("3a) Result:\n", result_3a)

# b) Given `arr = np.array([1, 2, 3, 4, 5, 6])`, create a new array where elements are repeated based on their value.
repeats = arr
result_3b = np.repeat(arr, repeats)
print("3b) Result:\n", result_3b)

# 4. Normalizing
# a) Normalize a 1D array `arr = np.array([10, 20, 30])` to have values between 0 and 1.
arr = np.array([10, 20, 30])
normalized_arr = (arr - arr.min()) / (arr.max() - arr.min())
print("4a) Result:\n", normalized_arr)

# 5. Bonus Challenge
# a) Create a 3x3 matrix where each element at position (i, j) is i * j.
i = np.arange(3)[:, np.newaxis]
j = np.arange(3)
result_5a = i * j
print("5a) Result:\n", result_5a)

# b) Given a 4x4 matrix, replace all elements on the main diagonal with 0 without using a loop.
arr_4x4 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
np.fill_diagonal(arr_4x4, 0)
print("5b) Result:\n", arr_4x4)