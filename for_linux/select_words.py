import csv
import random

p = []
random_line = random.randint(1, 99)
with open("100IRverbs.csv") as file:
    lines = file.readlines()
lines = ' '.join(lines[random_line:random_line+1])
p = lines.split(';')
p = [line.rstrip() for line in p]
print(p)