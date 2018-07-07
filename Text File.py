import csv

with open("/Users/jimmy/Desktop/VAAK/Camera01.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)
