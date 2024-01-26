# 71.
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

# 72.
text_to_write = "Hello, this is a sample text."
with open('new_file.txt', 'w') as file:
    file.write(text_to_write)

# 73.
with open('example.txt', 'r') as file:
    line_count = sum(1 for line in file)
    print(f"Number of lines: {line_count}")

# 74.
target_word = "Python"
with open('example.txt', 'r') as file:
    content = file.read()
    word_count = content.count(target_word)
    print(f"The word '{target_word}' appears {word_count} times.")

# 75.
import csv

with open('example.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# 76.
data_to_write = [['Name', 'Age'], ['Alice', 25], ['Bob', 30], ['Charlie', 35]]
with open('new_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data_to_write)

# 77.
source_file_path = 'source_file.txt'
destination_file_path = 'copied_file.txt'

with open(source_file_path, 'r') as source_file:
    with open(destination_file_path, 'w') as destination_file:
        destination_file.write(source_file.read())

# 78.
import gzip

with open('example.txt', 'rb') as file:
    content = file.read()
    with gzip.open('compressed_file.gz', 'wb') as compressed_file:
        compressed_file.write(content)

# 79.
file_path = 'nonexistent_file.txt'
try:
    with open(file_path, 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print(f"The file '{file_path}' does not exist.")

# 80.
with open('example.txt', 'r') as file:
    lines = file.readlines()
    reversed_lines = reversed(lines)
    with open('reversed_file.txt', 'w') as reversed_file:
        reversed_file.writelines(reversed_lines)