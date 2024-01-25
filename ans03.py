# 21.
my_dict = {'a': 1, 'b': 2, 'c': 3}
flipped_dict = {v: k for k, v in my_dict.items()}
print(flipped_dict)

# 22.
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged_dict = {**dict1, **dict2}
print(merged_dict)

# 23.
grades = {'math': 90, 'english': 85, 'history': 92}
max_subject = max(grades, key=grades.get)
print(max_subject)

# 24.
inventory = {'apple': 10, 'banana': 5, 'cherry': 8}
min_item = min(inventory, key=inventory.get)
print(min_item)

# 25.
book_count = {'book1': 200, 'book2': 150, 'book3': 300}
average_page_count = sum(book_count.values()) / len(book_count)
print(average_page_count)

# 26.
person_data = {'name': 'John', 'age': 30}
formatted_data = f"Name: {person_data['name']}, Age: {person_data['age']}"
print(formatted_data)

# 27.
employee_data = {'Alice': 50000, 'Bob': 60000, 'Charlie': 45000}
max_salary_employee = max(employee_data, key=employee_data.get)
print(max_salary_employee)

# 28.
word_lengths = {'apple': 5, 'banana': 6, 'cherry': 6}
sentence = "apple banana cherry"
word_lengths_list = [word_lengths[word] for word in sentence.split()]
print(word_lengths_list)

# 29.
phonebook = {'Alice': '123-456-7890', 'Bob': '987-654-3210'}
name_to_find = 'Alice'
phone_number = phonebook.get(name_to_find, '名前が見つかりません')
print(phone_number)

# 30.
course_grades = {'math': [90, 85, 92], 'english': [80, 88, 95], 'science': [95, 92, 88]}
average_grades = {subject: sum(grades) / len(grades) for subject, grades in course_grades.items()}
print(average_grades)