# data type
値の型整数型(int), 浮動小数点型(float), 文字列型(str)

# データ構造
リスト、タプル、集合、辞書

# text file 
import csv

with open("/Users/jimmy/Desktop/VAAK/Camera01.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)
