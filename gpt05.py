"""
問題41-50: 追加のPythonライブラリ

Pandas: 与えられた辞書 data を使用して、PandasのDataFrameを作成してください。
Pandas: 与えられたPandasのDataFrame df から特定の列を選択して、新しいDataFrameを作成してください。
Pandas: 与えられたPandasのDataFrame df から欠損値（NaN）を含む行を削除してください。
Matplotlib: 与えられたリスト x と y を使用して、Matplotlibを使って散布図を描画してください。
Matplotlib: 与えられたNumPy配列 data を使用して、Matplotlibを使ってヒストグラムを描画してください。
Seaborn: 与えられたPandasのDataFrame df を使用して、Seabornを使ってボックスプロットを描画してください。
Requests: 与えられたURLからデータを取得して、Requestsライブラリを使ってHTTPリクエストを行ってください。
Beautiful Soup: 与えられたHTMLページから特定の要素をBeautiful Soupを使って抽出してください。
Scikit-learn: 与えられたデータセットを使用して、Scikit-learnを使って単純な機械学習モデルを訓練してください。
TensorFlow/Keras: 与えられたデータを使用して、TensorFlowとKerasを使ってニューラルネットワークを構築してください。
"""
import pandas as pd

# 41    Pandas: 与えられた辞書 data を使用して、PandasのDataFrameを作成してください。
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'San Francisco', 'Los Angeles']}
df = pd.DataFrame(data)
print(df)


# 42    Pandas: 与えられたPandasのDataFrame df から特定の列を選択して、新しいDataFrameを作成してください。
name_df = df[['Name']]
print(name_df)

# 43    Pandas: 与えられたPandasのDataFrame df から欠損値（NaN）を含む行を削除してください。
nan_data = {'Name': ['Alice', None, 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'San Francisco', 'Los Angeles']}
df = pd.DataFrame(nan_data)
df_no_missing = df.dropna()
print(df_no_missing)


# 44    Matplotlib: 与えられたリスト x と y を使用して、Matplotlibを使って散布図を描画してください。
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 12, 8, 15, 20]

# plt.plot(x, y)
# plt.scatter(x, y)
# plt.show()


# 45    Matplotlib: 与えられたNumPy配列 data を使用して、Matplotlibを使ってヒストグラムを描画してください。
import numpy as np
data = np.random.randn(1000)
# plt.hist(data, bins=20, color='skyblue', edgecolor='black')
# plt.show()


# 46    Seaborn: 与えられたPandasのDataFrame df を使用して、Seabornを使ってボックスプロットを描画してください。
import seaborn as sns
data = {'Name': ['Alice', 'Bob', 'Charlie', 'AAA', 'BBB', 'CCC', 'DDD', 'EEE'],
        'Age': [25, 30, 35, 11, 89, 23, 55, 12],
        'City': ['New York', 'San Francisco', 'Los Angeles', 'AAA', 'BBB', 'CCC', 'DDD', 'EEE']}
df = pd.DataFrame(data)
sns.boxplot(x="Age", data=df)
plt.show()


# 47    Requests: 与えられたURLからデータを取得して、Requestsライブラリを使ってHTTPリクエストを行ってください。


# 48    Beautiful Soup: 与えられたHTMLページから特定の要素をBeautiful Soupを使って抽出してください。
# 49    Scikit-learn: 与えられたデータセットを使用して、Scikit-learnを使って単純な機械学習モデルを訓練してください。
# 50    TensorFlow/Keras: 与えられたデータを使用して、TensorFlowとKerasを使ってニューラルネットワークを構築してください。