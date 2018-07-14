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
