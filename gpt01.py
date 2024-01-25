"""
問題1-10: リスト

リスト nums が与えられた場合、その中の最大値を見つけてください。
リスト nums が与えられた場合、その中の最小値を見つけてください。
リスト nums が与えられた場合、すべての要素の合計を計算してください。
リスト nums が与えられた場合、その中の偶数だけを含む新しいリストを作成してください。
2つのリスト a と b が与えられた場合、それらの要素の和を含む新しいリストを作成してください。
リスト nums が与えられた場合、重複する要素を削除した新しいリストを作成してください。
リスト nums が与えられた場合、要素を逆順にした新しいリストを作成してください。
リスト nums が与えられた場合、リスト内の各要素を2倍にした新しいリストを作成してください。
リスト nums が与えられた場合、要素の個数が奇数の場合は中央の要素を返し、偶数の場合は中央の2つの要素を含む新しいリストを作成してください。
リスト nums が与えられた場合、重複する要素を除いた新しいリストを作成し、ソートしてください。
"""

# 1
nums = [1,4,3,5,7,4,23,43,6]
print(max(nums))

# 2
print(min(nums))

# 3
print(sum(nums))

# 4
new_nums = [i for i in nums if i % 2 == 0]
print(new_nums)

# 5
a = [2,4,3,6,32,12,54,75]
b = [4,8,0,32,38,27,13,92]
sum_nums = [a1 + b1 for a1, b1 in zip(a,b)]
print(sum_nums)

# 6
x = [2,4,3,6,32]
y = [2,4,9,6,1]
new_x = x.copy()
new_x.extend(y)
z = set(new_x)
print(list(z))

# 7
rv_nums = nums.copy()
rv_nums.reverse()
print(rv_nums)

# 8
mul_nums = [i * 2 for i in nums]
print(mul_nums)

# 9
if len(nums) % 2 == 0:
    index = int(len(nums) / 2)
    new_list = [nums[index - 1], nums[index]]
    print(new_list)
elif len(nums) % 2 == 1:
    index = int(len(nums) / 2)
    print(nums[index])
else:
    print('リストは作成できません。')


# 10
set_nums = set(nums)
sort_nums = list(set_nums)
sort_nums.sort()
print(sort_nums)
