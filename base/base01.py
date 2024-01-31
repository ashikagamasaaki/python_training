with open('base/base01.txt', 'r') as f:
    # chunk = 2
    # line = f.read(chunk)
    line = f.readline()
    
    while line:
        print(line, end='')
        line = f.readline()
        # line = f.read(chunk)
        
        
import string

s = """\
    Hi $name.
    $contents
    Have a good day
"""

t = string.Template(s)
sentens = t.substitute(name='Mike', contents='How are you')
print(sentens)


import csv

with open('base/base01.csv', 'w', newline='') as csv_file:
    fieldnames = ['Name', 'Count']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'Name': 'Taro', 'Count': 1})
    writer.writerow({'Name': 'Jiro', 'Count': 2})

with open('base/base01.csv', 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    
    for row in reader:
        print(row['Name'], row['Count'])
        

import os
print(os.path.exists('base/base01.txt'))
print(os.path.isfile('base/base01.txt'))
print(os.path.isdir('base/base01.txt'))


import tempfile

with tempfile.TemporaryFile(mode='w+') as t:
    t.write('hello')
    t.seek(0)
    print(t.read())