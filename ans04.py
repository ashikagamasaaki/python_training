import numpy as np

# 31.
a = [1, 2, 3, 4, 5]
arr_a = np.array(a)
print(arr_a)

# 32.
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
result_arr = arr1 + arr2
print(result_arr)

# 33.
arr = np.array([1, 2, 3, 4, 5])
mean_value = np.mean(arr)
print(mean_value)

# 34.
arr = np.array([3, 1, 4, 1, 5, 9, 2, 6, 5, 3])
sorted_arr = np.sort(arr)[::-1]
print(sorted_arr)

# 35.
arr = np.array([3, 1, 4, 1, 5, 9, 2, 6, 5, 3])
max_value = np.max(arr)
max_index = np.argmax(arr)
print("Max Value:", max_value)
print("Index of Max Value:", max_index)

# 36.
arr = np.array([1, 2, 3, 4, 5])
doubled_arr = arr * 2
print(doubled_arr)

# 37.
matrix = np.array([[1, 2, 3], [4, 5, 6]])
transposed_matrix = np.transpose(matrix)
print(transposed_matrix)

# 38.
arr = np.array([1, 2, 3, 4, 5, 6])
even_elements = arr[arr % 2 == 0]
print(even_elements)

# 39.
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
dot_product = np.dot(a, b)
print(dot_product)

# 40.
arr = np.array([8, 15, 3, 6, 2, 10])
filtered_arr = arr[arr < 10]
print(filtered_arr)