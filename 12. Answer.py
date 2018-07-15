#第12回：It's difficult.
# 最大公約数を求める。ユークリッド互除法
a = int(input("number a?"))
b = int(input("number b?"))

if a > b:
    c = a
    a = b
    b = c
while a != 0:
    b = b % a
    c = a
    a = b
    b = c
print(b)

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
