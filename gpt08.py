"""
問題71-80: ファイル操作

テキストファイルの読み込み: 与えられたテキストファイルを読み込み、その内容を表示するプログラムを作成してください。
テキストファイルの書き込み: 与えられたテキストを新しいテキストファイルに書き込むプログラムを作成してください。
ファイル行数のカウント: 与えられたテキストファイルの行数をカウントするプログラムを作成してください。
特定の単語の出現回数: 与えられたテキストファイルから特定の単語（例: "Python"）の出現回数をカウントするプログラムを作成してください。
CSVファイルの読み込み: 与えられたCSVファイルを読み込み、その内容を表示するプログラムを作成してください。
CSVファイルの書き込み: 与えられたデータを新しいCSVファイルに書き込むプログラムを作成してください。
ファイルのコピー: 与えられたファイルを別のファイルにコピーするプログラムを作成してください。
ファイルの圧縮: 与えられたテキストファイルをgzipを使って圧縮するプログラムを作成してください。
ファイルの例外処理: ファイルが存在しない場合に備えて、テキストファイルを読み込むプログラムを例外処理を含めて作成してください。
行の逆順: 与えられたテキストファイルの行を逆順にして新しいファイルに書き込むプログラムを作成してください。
"""

# 71
path71 = 'resources/sample71.txt'
# f = open(path71, 'r', encoding='utf-8')
# data = f.read()
# print(data)
# f.close()

with open(path71, 'r', encoding='utf-8') as f:
    sample71 = f.read()
    print(sample71)
    
    
# 72    テキストファイルの書き込み: 与えられたテキストを新しいテキストファイルに書き込むプログラムを作成してください。
path72 = "resources/sample72.txt"
sample72 = """サンプル72用文字列
テキストに書き込み
追記モード
"""
with open(path72, 'a', encoding='utf-8') as f:
    f.write(sample72)


# 73    ファイル行数のカウント: 与えられたテキストファイルの行数をカウントするプログラムを作成してください。
line_cnt = 0
with open(path72, 'r', encoding='utf-8')as f:
    for line in f:
        line_cnt+=1
print(f'{line_cnt}行です。')


# 74    特定の単語の出現回数: 与えられたテキストファイルから特定の単語（例: "Python"）の出現回数をカウントするプログラムを作成してください。
search_word = 'Python'
search_cnt = 0
with open(path72, 'r', encoding='utf-8') as f:
    for line in f:
        search_cnt += line.count(search_word)
print(f'{search_word}: {search_cnt}回出現')


# 75    CSVファイルの読み込み: 与えられたCSVファイルを読み込み、その内容を表示するプログラムを作成してください。
path75 = 'resources/sample75.csv'
# with open(path75, 'r', encoding='utf-8') as f:
#     print(f.read())

""" CSVの読み込みは下記の通りライブラリ使う """
import csv
with open(path75, 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


# 76    CSVファイルの書き込み: 与えられたデータを新しいCSVファイルに書き込むプログラムを作成してください。
data_to_write = [['Name', 'Age'], ['Alice', 25], ['Bob', 30], ['Charlie', 35]]
path76 = 'resources/sample76.csv'
csv_line = ''
with open(path76, 'w', encoding='utf-8') as f:
    for line in data_to_write:
        s_line = map(str, line)
        csv_line = ",".join(s_line) + '\n'
        f.writelines(csv_line)


# 77    ファイルのコピー: 与えられたファイルを別のファイルにコピーするプログラムを作成してください。
import shutil
path77 = 'resources/sample77.csv'
cp_file = shutil.copy(path76, path77)
print(cp_file)


# 78    ファイルの圧縮: 与えられたテキストファイルをgzipを使って圧縮するプログラムを作成してください。
shutil.make_archive('zip_sample', format='zip', root_dir='resources')


# 79    ファイルの例外処理: ファイルが存在しない場合に備えて、テキストファイルを読み込むプログラムを例外処理を含めて作成してください。
try:
    path79 = 'resources/sample79.txt'
    with open(path79, 'r', encoding='utf-8') as f:
        line = f.readline()
        while line:
            print(line)
            line = f.readline()
except FileNotFoundError as e:
    print('ファイルが存在しません。')
else:
    print('ファイルの読み込み成功')
finally:
    print('処理終了')


# 80    行の逆順: 与えられたテキストファイルの行を逆順にして新しいファイルに書き込むプログラムを作成してください。
with open(path71, 'r', encoding='utf-8') as f:
    f_list = f.read().split('\n')

path80 = 'resources/sample80.txt'
with open(path80, 'w', encoding='utf-8')as f:
    for line in reversed(f_list):
        f.write(line + "\n")