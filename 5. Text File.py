# ファイルを書き出すで開く
# write() 文字列を一行ずつ書き出す
with open("/Users/shiguang/Desktop/test.txt", "w") as f:
    # write(): 文字列を一行ずつ書き出す。改行コードを入れる。
    # 文字列のみ書き出すことができる。数値などは文字列に変換する必要がある。
    f.write("I love \n")
    f.write("I \n")
    f.write("love \n")
    
# writelinesでリストとタプルをまとめて書き出す
topic_list = [ "概要 \n", "制御文 \n", "関数 \n", "ファイル入出力 \n" ]
with open("/Users/shiguang/Desktop/test2.txt", "w") as file:
    file.write("情報処理論2aで")
    file.write("これまでに勉強したのは: \n")
    # 改行する。
    file.write("\n")
    # リストをwritelinesでまとめて書き出す。タプルも可
    file.writelines(topic_list)

    
# CSVファイルから抽出した品種を別のファイルに書き出す。
with open("/Users/shiguang/Desktop/Python/情報処理論/iris.csv") as filein:
    with open("/Users/shiguang/Desktop/test3.txt", "w") as fileout:
        # 一行ずつ順次読み込む時に、for loopを使う
        for line in filein:
            # 文字列型のメソッドrstrip()は末尾の指定した文字を除去することができるので、改行コードを除去する。
            line2 = line.rstrip("\n")
            # 文字列をリストに変更する
            lineList = line2.split(",")
            # 花の種類をwritelinesメソッドでfileoutに書き込む
            fileout.writelines(lineList[-1])
            # シーケンスの出力結果を改行する。
            fileout.writelines("\n")
 

   
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
