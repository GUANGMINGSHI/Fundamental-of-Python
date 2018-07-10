"""
text file (Jupyter notebook)
file's input and output
1. open the file
2. read or write the file
3. close the file
"""

# open as read--"r"
file = open("/Users/jimmy/Desktop/Python/iris.csv", "r")
# contain all in one variable
#x = file.read(1)
# divided into rows for each line
lines = file.readlines()
print(lines)
file.close

# use "with...open...as"
with open("/Users/jimmy/Desktop/Python/iris.csv") as file:
    for line in file:
        line2 = line.strip("¥n")
        print(line2)

# 書き出しでファイルを開く, only "string"
with open("/Users/jimmy/Desktop/Python/test.txt", "w") as file:
    file.write("information process")
    file.write("is teaching Python.")
    
# write list use"writelines()"
topic_list = ["A", "B", "C", "D"]
with open("/Users/jimmy/Desktop/Python/test.txt", "w") as file:
    file.write("information process")
    file.write("is")
    file.writelines(topic_list)

# read by rows
file = open("/Users/jimmy/Desktop/Python/iris.csv")
for line in file:
    line2 = line.rstrip("¥n")
    print(line2)
file.close()

# show the csv file last one rows
with open("/Users/jimmy/Desktop/Python/iris.csv") as file:
    for line in file:
        line2 = line.strip("¥n")
        # conver string to list
        line2 = line2.split(",")
        print(line2[-1])
  
# write in another file, rather than show it.
with open("/Users/jimmy/Desktop/Python/iris.csv") as file_in:
    with open("/Users/jimmy/Desktop/Python/iriss.csv", "w") as file_out:
        for line in file_in:
            line2 = line.strip("¥n")
            line_data = line2.split(",")
            file_out.write(line_data[-1] + "¥n")
     
   
""" use module:csv"""
import csv
with open("/Users/jimmy/Desktop/VAAK/Camera01.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)

    

