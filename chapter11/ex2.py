import re

filename = 'mbox.txt'
fhand = open(filename)

sum = 0
cnt = 0
for line in fhand:
    lst = re.findall('New Revision: ([0-9]+)', line)
    if len(lst) > 0:
        sum = sum + int(lst[0])
        cnt = cnt + 1

print(sum/cnt)
