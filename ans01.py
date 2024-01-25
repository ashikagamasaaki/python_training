# 1.
nums = [4, 7, 1, 9, 3, 6]
max_value = max(nums)
print(max_value)

# 2.
nums = [4, 7, 1, 9, 3, 6]
min_value = min(nums)
print(min_value)

# 3.
nums = [4, 7, 1, 9, 3, 6]
sum_values = sum(nums)
print(sum_values)

# 4.
nums = [4, 7, 1, 9, 3, 6]
even_nums = [num for num in nums if num % 2 == 0]
print(even_nums)

# 5.
a = [1, 2, 3]
b = [4, 5, 6]
sum_list = [x + y for x, y in zip(a, b)]
print(sum_list)

# 6.
nums = [4, 7, 1, 4, 3, 6]
unique_nums = list(set(nums))
print(unique_nums)

# 7.
nums = [4, 7, 1, 9, 3, 6]
reverse_nums = list(reversed(nums))
print(reverse_nums)

# 8.
nums = [4, 7, 1, 9, 3, 6]
double_nums = [num * 2 for num in nums]
print(double_nums)

# 9.
nums = [4, 7, 1, 9, 3, 6]
if len(nums) % 2 == 1:
    middle_element = [nums[len(nums)//2]]
else:
    middle_element = nums[len(nums)//2 - 1:len(nums)//2 + 1]
print(middle_element)

# 10.
nums = [4, 7, 1, 4, 3, 6]
unique_sorted_nums = sorted(list(set(nums)))
print(unique_sorted_nums)