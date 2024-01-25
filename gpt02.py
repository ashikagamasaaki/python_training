"""
問題11-20: 文字列

文字列 s が与えられた場合、その文字列を逆順にしてください。
文字列 s が与えられた場合、各単語の先頭文字を大文字にして新しい文字列を作成してください。
文字列 s が与えられた場合、数字を含む場合はその数字の合計を、含まない場合は0を返してください。
文字列 s が与えられた場合、各単語の出現回数を辞書型で返してください。
文字列 s が与えられた場合、各文字の出現回数を辞書型で返してください。
文字列 s が与えられた場合、文字列内のスペースを全て取り除いてください。
文字列 s が与えられた場合、文字列を単語ごとに分割し、そのリストを返してください。
文字列 s が与えられた場合、文字列内のすべての英字を大文字にしてください。
文字列 s が与えられた場合、文字列内のすべての英字を小文字にしてください。
文字列 s が与えられた場合、文字列内の各単語を逆順にしてください。
"""

# 11    文字列 s が与えられた場合、その文字列を逆順にしてください。
s = "hello world"
print(s[::-1])
print(''.join(reversed(s)))


# 12    文字列 s が与えられた場合、各単語の先頭文字を大文字にして新しい文字列を作成してください。
s = "hello world"
print(s.title())


# 13    文字列 s が与えられた場合、数字を含む場合はその数字の合計を、含まない場合は0を返してください。
s = "abc123def456"
ans = 0
for word in s:
    if word.isdigit():
        ans += int(word)
print(ans)


# 14    文字列 s が与えられた場合、各単語の出現回数を辞書型で返してください。
s = "apple banana apple cherry cherry cherry banana apple apple apple cherry"
s_list = s.split(" ")
s_set = set(s_list)
dict_s = {}
for key in s_set:
    dict_s[key] = s_list.count(key)
print(dict_s)
sort_dict = dict(sorted(dict_s.items(), key=lambda x:x[1]))
print(sort_dict)


# 15    文字列 s が与えられた場合、各文字の出現回数を辞書型で返してください。
s = "hello world"
s_list = list(s)
s_set = set(s_list)
s_dict = {}
for key in s_set:
    s_dict[key] = s_list.count(key)
    # s_disc[key] = s_dict.get(key, 0) + 1  get の第二引数でデフォルトを設定することもできる
print(s_dict)


# 16    文字列 s が与えられた場合、文字列内のスペースを全て取り除いてください。
s = "hello world"
print(s.replace(" ", ""))


# 17    文字列 s が与えられた場合、文字列を単語ごとに分割し、そのリストを返してください。
s = "hello world"
print(s.split(" "))


# 18    文字列 s が与えられた場合、文字列内のすべての英字を大文字にしてください。
s = "hello world"
print(s.upper())


# 19    文字列 s が与えられた場合、文字列内のすべての英字を小文字にしてください。
s = "hELLO wORLD"
print(s.lower())


# 20    文字列 s が与えられた場合、文字列内の各単語を逆順にしてください。
s = "hello world"
s_list = list(reversed(s.split(" ")))
s_rev = " ".join(s_list)
print(s_rev)