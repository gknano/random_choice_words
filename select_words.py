import csv

with open("100IRverbs.csv", newline='') as f:
    reader = csv.reader(f, delimiter=";")
    for line in reader:
        print(line[1])