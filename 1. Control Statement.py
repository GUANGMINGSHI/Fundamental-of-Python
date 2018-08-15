'''while: iterate as long as condition is true '''
count = 5
while count > 0:
    print(str(count))
    count -= 1
    
#数当てゲーム
import random
r = random.randrange(100)

#iterate until draw your results. 
while True:
    x = int(input("number?"))
    if x < r:
        print("smaller")
    elif x > r:
        print("bigger")
    else:
        print("right")

        
'''break: break the loop'''
while True:
    value = int(input("yen"))
    if value == 0:
        print("0 is inputted.")
        break;
    print(100 / value)

    
'''continue: continue this loop when if statement occur.'''
remain = 5
while remain > 0:
    print(str(remain))
    value = int(input("what?"))
    if value == 0:
        print("0 is inputted.")
        continue;
    print(100 /value)
    remain -= 1

    

'''
例外処理:
     try:                     
         通常処理                    
     except:
         例外ときの処理
       
       
例外処理は指定することができる： 
     try:
         通常処理
     except ValueError:
         例外ときの処理
'''
    
# Example:    
for i in range(5):
    value = int(input("integer?"))
    try:
        print(100 / int(value))
    except ValueError:
        print("not integer")
        break
    except ZeroDivisionError:
        print("not 0")
        ＃　close this whole loop.
        break
print("over")


'''judge inputted number is prime number or not?''' 
n = int(input("Data?"))
for i in range(1, n + 1):
    if n % i == 0:
        if i != 1 and i != n:
            print("bushisushu")
            break;

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
