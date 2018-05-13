# Chapter 10 Exercise 3
import string

filename = 'mbox-short.txt'
try:
    fhand = open(filename)
except:
    print('Failed to open file')

words = []
d = {}
total = 0
for line in fhand:
    line = line.strip()
    line = line.translate(line.maketrans('', '', string.punctuation + string.digits))
    line = line.lower()
    words = line.split()
    for word in words:
        for c in word:
            d[c] = d.get(c, 0) + 1
            total = total + 1

t = list()
for c, cnt in list(d.items()):
    t.append((c, cnt/total))
t.sort()
for item in t:
    print(item[0],  item[1]*100, '*' * int(item[1]*100))
