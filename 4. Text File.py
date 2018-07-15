"""
file operation take place three steps:
1. open the file
2. read or write the file
3. close the file
"""
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

# Question1: show the csv file last one rows
with open("/Users/jimmy/Desktop/Python/iris.csv") as file:
    for line in file:
        # conver string to list
        line2 = line2.split(",")
        print(line2[-1])
  
# Question2: write in another file, rather than show it.
with open("/Users/jimmy/Desktop/Python/iris.csv") as file_in:
    with open("/Users/jimmy/Desktop/Python/iriss.csv", "w") as file_out:
        for line in file_in:
            line_data = line.split(",")
            file_out.write(line_data[-1])
 
# Question3: Adjustment of meeting schedule, 
# カウンタをそれぞれ０で初期化
count = []
for i in range(32):
    count.append(0)

# create vip's list    
vip = []

with open("/Users/jimmy/Desktop/Python/days.csv") as file_in:
    for line in file_in:
        x = line.rstrip('\n')
        days_list = x.split(",")
        
        # それぞれのデータについてカウンタに1をプラス
        for i in days_list:
            count[int(i)] += 1
        # why len?
        # 最初の人のデータが空だったら覚えておく
        if len(vip) == 0:
            vip = days
# 最初の人が参加可能な日で最多のものをmに入れる
m = 0
# 最初の人が参加可能な日をそれぞれ見る
for v in vip:
    # その日の人数
    c = count[int(v)]
    # もし今までで最多の日を上回ったらmを更新する
    if c > count[m]:
        m = int(v)

print(m)
  
   
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
    writer.writerow(words)

# read dictionary use csv.DictReader()
with open('dict.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)

        
"""using pandas to operate csv data"""
camera_csv = pd.read_csv(filepath_or_buffer="/Users/jimmy/Desktop/VAAK/Camera01.csv", encoding="ms932", sep=",")
