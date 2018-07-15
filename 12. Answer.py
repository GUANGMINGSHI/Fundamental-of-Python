#第12回：It's difficult.

'''ユークリッド互除法'''
a = int(input("a?"))
b = int(input("b?"))
r = a%b
while r:
    a = b
    b = r
    r = a % b
print(b)


'''数当てゲーム'''
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

'''会議の日程調整'''
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
