"""
問題31-40: NumPy

与えられたリスト a をNumPy配列に変換してください。
与えられた2つのNumPy配列 arr1 と arr2 を要素ごとに足して新しい配列を作成してください。
与えられたNumPy配列 arr の平均値を計算してください。
与えられたNumPy配列 arr の要素を降順にソートしてください。
与えられたNumPy配列 arr の最大値とそのインデックスを取得してください。
与えられたNumPy配列 arr の各要素を2倍にしてください。
与えられたNumPy配列 matrix を転置してください。
与えられたNumPy配列 arr の中で、条件を満たす要素だけを含む新しい配列を作成してください（例: 偶数の要素のみ）。
与えられた2つのNumPy配列 a と b を内積計算してください。
与えられたNumPy配列 arr の中で、要素が10未満のものだけを含む新しい配列を作成してください。
"""

import numpy as np


# 31    与えられたリスト a をNumPy配列に変換してください。
a = [1, 2, 3, 4, 5]
np_list = np.array(a)
print(np_list)

# 32    与えられた2つのNumPy配列 arr1 と arr2 を要素ごとに足して新しい配列を作成してください。
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
print(np.add(arr1, arr2))


# 33    与えられたNumPy配列 arr の平均値を計算してください。
arr = np.array([1, 2, 3, 4, 5])
print(np.average(arr))


# 34    与えられたNumPy配列 arr の要素を降順にソートしてください。
arr = np.array([3, 1, 4, 1, 5, 9, 2, 6, 5, 3])
print(np.sort(arr)[::-1])


# 35    与えられたNumPy配列 arr の最大値とそのインデックスを取得してください。
arr = np.array([3, 1, 4, 1, 5, 9, 2, 6, 5, 3])
print(f'インデックス:{np.argmax(arr)}, 最大値:{np.max(arr)}')


# 36    与えられたNumPy配列 arr の各要素を2倍にしてください。
arr = np.array([1, 2, 3, 4, 5])
print(arr * 2)


# 37    与えられたNumPy配列 matrix を転置してください。
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(matrix.T)


# 38    与えられたNumPy配列 arr の中で、条件を満たす要素だけを含む新しい配列を作成してください（例: 偶数の要素のみ）。
arr = np.array([1, 2, 3, 4, 5, 6])
print(arr[arr % 2 == 0])


# 39    与えられた2つのNumPy配列 a と b を内積計算してください。
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(np.dot(a,b))


# 40    与えられたNumPy配列 arr の中で、要素が10未満のものだけを含む新しい配列を作成してください。
arr = np.array([8, 15, 3, 6, 2, 10])
print(arr[arr < 10])