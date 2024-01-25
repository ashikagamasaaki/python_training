"""
問題21-30: 辞書

与えられた辞書 my_dict のキーと値を逆にした新しい辞書を作成してください。
与えられた2つの辞書 dict1 と dict2 を結合して、新しい辞書を作成してください。ただし、重複するキーがある場合は dict2 の値を優先してください。
与えられた辞書 grades があります。この辞書から値が最大のキーを返してください。
与えられた辞書 inventory があります。この辞書から値が最小のキーを返してください。
与えられた辞書 book_count があります。この辞書を使って、各本の平均ページ数を計算してください。
与えられた辞書 person_data があります。この辞書から名前と年齢を取り出し、新しい文字列として整形してください。
与えられた辞書 employee_data があります。この辞書から給与が最大の従業員の名前を返してください。
与えられた辞書 word_lengths があります。この辞書を使用して、文字列 "apple banana cherry" の各単語の文字数を表示してください。
与えられた辞書 phonebook があります。この辞書を使用して、指定された名前の電話番号を取得してください。名前が見つからない場合は "名前が見つかりません" と表示してください。
与えられた辞書 course_grades があります。この辞書を使用して、各科目の平均点を計算してください。
"""


# 21    与えられた辞書 my_dict のキーと値を逆にした新しい辞書を作成してください。
my_dict = {
    "apple": "red",
    "banana": "yellow",
    "grape": "perple",
    "peech": "pink"
}
new_dict = {value: key for key, value in my_dict.items()}
print(new_dict)


# 与えられた2つの辞書 dict1 と dict2 を結合して、新しい辞書を作成してください。ただし、重複するキーがある場合は dict2 の値を優先してください。
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
dict1.update(dict2)
print(dict1)


# 与えられた辞書 grades があります。この辞書から値が最大のキーを返してください。
grades = {'math': 90, 'english': 85, 'history': 92}
print(max(grades, key=grades.get))

# 与えられた辞書 inventory があります。この辞書から値が最小のキーを返してください。
inventory = {'apple': 10, 'banana': 5, 'cherry': 8}
print(min(inventory, key=inventory.get))


# 与えられた辞書 book_count があります。この辞書を使って、各本の平均ページ数を計算してください。
book_count = {'book1': 200, 'book2': 150, 'book3': 300}
page_avg = sum(book_count.values()) / len(book_count.values())
print(page_avg)


# 与えられた辞書 person_data があります。この辞書から名前と年齢を取り出し、新しい文字列として整形してください。
person_data = {'name': 'John', 'age': 30}
person_str = f"My Name is {person_data.get("name", "name")}! I'm {person_data.get("age", "20")} years old."
print(person_str)


# 与えられた辞書 employee_data があります。この辞書から給与が最大の従業員の名前を返してください。
employee_data = {'Alice': 50000, 'Bob': 60000, 'Charlie': 45000}
print(max(employee_data, key=employee_data.get))


# 与えられた辞書 word_lengths があります。この辞書を使用して、文字列 "apple banana cherry" の各単語の文字数を表示してください。
word_lengths = {'apple': 5, 'banana': 6, 'cherry': 6}
sentence = "apple banana cherry"
count_len = [word_lengths.get(word) for word in sentence.split()]
print(count_len)


# 与えられた辞書 phonebook があります。この辞書を使用して、指定された名前の電話番号を取得してください。名前が見つからない場合は "名前が見つかりません" と表示してください。
phonebook = {'Alice': '123-456-7890', 'Bob': '987-654-3210'}
name_to_find = 'Takashi'
print(phonebook.get(name_to_find, '名前が見つかりません'))


# 与えられた辞書 course_grades があります。この辞書を使用して、各科目の平均点を計算してください。
course_grades = {'math': [90, 85, 92], 'english': [80, 88, 95], 'science': [95, 92, 88]}
course_avg = {key:sum(value) // len(value) for key, value in course_grades.items()}
print(course_avg)