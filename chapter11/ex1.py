import re

fhand = open('mbox.txt')
p = input('Enter a regular expression: ')
cnt = 0
for line in fhand:
    line = line.rstrip()
    if re.search(p, line) != None:
        cnt = cnt + 1

print('mbox.txt had {0} lines that matched {1} '.format(cnt, p))
