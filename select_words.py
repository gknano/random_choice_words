import csv
n = 1
p = []
test = 'test1 test2 test3'
with open("100IRverbs.csv") as file:
    lines = file.readlines()
lines = ' '.join(lines[n:n+1])
p = lines.split(' ')
print(p)