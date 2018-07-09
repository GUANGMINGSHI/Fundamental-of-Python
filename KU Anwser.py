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
n = [90, 30, 20, 80, 20, 0, 20, 100, 60, 50]
条件式を満たしている間、処理を続ける
count = 0
for i in n:
    if i < 60:
        count += 1
print("Failed this exam:" + str(count))

#第7回：文字列、内包表記
1. 入力されたものの数を辞書の中で数える
city1 = input("Where are you from?")
city2 = city1.lower()  #代入する
city3 = city2.replace(" ", "")
city_list = city3.split(",")

city = {}  #空の辞書を作成する
for i in city_list:
    if i in city:
        city[i] += 1
    else:
        city[i] = 0
print(city)

2. 入力された値についての内包表記
city1 = input("Where are you from?")
city2 = city1.lower() ＃小文字
city3 = city2.replace(" ", "")
city_list = city3.split(",") ＃カンマで分割したリストを作る

city_t = [i.upper() for i in city_list if i.startswith("t")]
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
1. クラスを作成する
from math import sqrt

class Triangle:
    #これからはメソッド、関数の定義と同じ書く
    def __init__(self, v1, v2):#メソッドを自動的に呼び出す
        self.bottom = v1#selfはインスタンス変数：クラスに基づいて実際に作成した物
        self.height = v2

    def calc_area(self):
        self.area = self.bottom * self.height / 2#引数に必ずSelfを加える

    def calc_edge(self):
        self.edge = sqrt(self.bottom ** 2 + self.height ** 2)

output = Triangle(2, 2)
output.calc_area()
output.calc_edge()
#print(Triangle):クラス定義の外では変数の前にインスタンス名をつけてアクセスする

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



