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

