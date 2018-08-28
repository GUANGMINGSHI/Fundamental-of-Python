# 書き出しでファイルを開く, only "string"
with open("/Users/jimmy/Desktop/Python/test.txt", "w") as file:
    file.write("information process")
    file.write("is teaching Python.")
    
# write list use"writelines()"
topic_list = ["A", "B", "C", "D"]
with open("/Users/jimmy/Desktop/Python/test.txt", "w") as file:
    file.write("information process")
    file.write("is")
    # 以sequence style写入string
    file.writelines(topic_list)

# Question1: show the csv file last one rows
with open("/Users/jimmy/Desktop/Python/iris.csv") as file:
    for line in file:
        # conver string to list
        line2 = line.split(",")
        print(line2[-1])
  
# Question2: write in another file, rather than show it.
with open("/Users/jimmy/Desktop/Python/iris.csv") as file_in:
    with open("/Users/jimmy/Desktop/Python/iriss.csv", "w") as file_out:
        # difference between "w" and "a"; don't foget "w".
        for line in file_in:
            line_data = line.split(",")
            file_out.write(line_data[-1])
 

   
""" csv module - csv file reading and writing. """
# read csv file
import csv
with open("/Users/jimmy/Desktop/VAAK/Camera01.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)
        
# write csv file
word = "Good morning, Hello, Good night"
words = word.split(',') 
with open("/Users/jimmy/Desktop/start.csv", "w") as f:
    writer = csv.writer(f)
    # writer.writerow() must be iterable string or numbers for writer object.
    # writer.writerow([person_x,person_y])
    # writer.writerows() expected list of lists, not list of string. you can split string to columns.
    writer.writerow(words)
    

# read dictionary use csv.DictReader()
with open('dict.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
