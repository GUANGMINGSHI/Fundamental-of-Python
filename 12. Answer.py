＃第5回：制御文
1. 条件分岐と制御
age = int(input("your age?"))
if age < 3:
    print("free")
elif 3 < age < 12:
    print("3000")
elif 65 > age > 12:
    weight = int(input("your weight?(kg)"))
    if weight < 100:
        print("10000")
    else:
        print("20000")
else:
    print("5000")
 
    
2. ループの中にループ
for n in range(1, 10):
    for m in range(1, 10):
        print(n * m)

＃第6回：リストなどのデータ構造
1. リスト中から条件を満たすものの数を数える
score = [90, 30, 20, 80, 20, 0, 20, 100, 60, 50]
sum = sum(score)
len = len(score)
average = sum / len
print(average)

count = 0
for i in score:
    if i < 60:
        count += 1

print(str(count))


#第7回：文字列、内包表記
1. 入力されたものの数を辞書の中で数える
city = input("Where are you from?")
print(city.lower())
print(city.replace(" ",""))
city_list = city.split(",")
print(city_list)

# why create empty dictionary?
dict = {}
for i in city_list:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1
print(dict)

2. 入力された値についての内包表記
city = input("Where are you from?")
city_lower = city.lower()
city_rep = city_lower.replace(" ","")
city_list = city_rep.split(",")

# Pay attention "i".
city_t = [ i.upper() for i in city_list if i.startswith("t")]
print(city_t)

#第9回：テキストファイル処理
2. ファイルの書き出し
with open("ok.txt", "w") as file:
    file.write("This is not my zone!")
    
with open("/Users/jimmy/Desktop/Python/iris.csv") as file_in:
    with open("test.txt", "w") as file_out:
        for line in file_in:
            line2 = line.strip("¥n")
            line3 = line2.split(",")
            file_out.write(line3[-1])
        
#＃第10回：クラス 
from math import sqrt
class Triangle:
    def __init__(self, bottom, height):
        self.bottom = bottom
        self.height = height
    def calc_area(self):
        return self.bottom * self.height / 2
        
    def calc_edge(self):
        return sqrt(self.bottom ** 2 + self.height ** 2)

triangle1 = Triangle(3, 4)
print(triangle1.calc_area())


#第12回：It's difficult.
1. 入力された自然数の公約数を全部列挙、素数かどうかを判断 
n = int(input("Data?"))
for i in range(1, n+1):#辞書でもない、リストでもないから、range()を使う。リストなら、括弧はいらん
    if n % i == 0:
        print(i)
       
n = int(input("Data?"))
for i in range(1, n + 1):
    if n % i == 0:
        if i != 1 and i != n: #数学の考え方
            print("bushisushu")
            break;#ループの中断
2. ユークリッド互除法
a = int(input("a?"))
b = int(input("b?"))
r = a%b
while r:
    a = b
    b = r
    r = a % b
print(b)

3. 数当てゲーム
import random
r = random.randrange(100)

while True:#True表示一直循环直到满足break的条件
    p = int(input("What's your number?"))#放在外面会形成无限循环
    if r > p:#要有大小，才能有比较。
        print("Smaller!!")
    elif r < p:
        print("Bigger!!")
    else:
        print("This is right!")
        break
4. 会議の日程調整
＃第13回：例外処理、複雑な反復処理、関数の応用
for i in range(5):
    value = int(input("Zhengshu?"))
    try:
        print(100 / value)
    except:
        print("Over")
        break
else:
    print("This loop is over!")

＃第14回：応用編
plt.show()：used in Pycharm for visualization
