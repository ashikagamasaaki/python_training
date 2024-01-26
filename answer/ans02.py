# 11.
s = "hello world"
reversed_s = s[::-1]
print(reversed_s)

# 12.
s = "hello world"
capitalized_words = ' '.join(word.capitalize() for word in s.split())
print(capitalized_words)

# 13.
s = "abc123def456"
sum_of_numbers = sum(int(char) for char in s if char.isdigit())
print(sum_of_numbers)

# 14.
s = "apple banana apple cherry cherry cherry banana apple apple cherry"
word_count = {}
words = s.split()
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
print(word_count)

# 15.
s = "hello world"
char_count = {}
for char in s:
    char_count[char] = char_count.get(char, 0) + 1
print(char_count)

# 16.
s = "hello world"
no_spaces = s.replace(" ", "")
print(no_spaces)

# 17.
s = "hello world"
word_list = s.split()
print(word_list)

# 18.
s = "hello world"
upper_case_s = s.upper()
print(upper_case_s)

# 19.
s = "HELLO WORLD"
lower_case_s = s.lower()
print(lower_case_s)

# 20.
s = "hello world"
reversed_words = ' '.join(word[::-1] for word in s.split())
print(reversed_words)