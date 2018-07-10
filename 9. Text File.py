"""
text file (Jupyter notebook)
file's input and output
1. open the file
2. read or write the file
3. close the file
"""

file = open("/Users/jimmy/Desktop/Python/iris.csv")
# contain all in one variable
#x = file.read(1)
# divided into rows for each line
lines = file.readlines()
print(lines)
file.close

# read by rows
file = open("/Users/jimmy/Desktop/Python/iris.csv")
for line in file:
    line2 = line.rstrip("¥n")
    print(line2)
file.close()

# use "with...open...as"
with open("/Users/jimmy/Desktop/Python/iris.csv") as file:
    for line in file:
        line2 = line.strip("¥n")
        print(line2)
  
# what's this?
import csv
with open("/Users/jimmy/Desktop/VAAK/Camera01.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)
