'''specify data individually'''
for num in [1,2,3,4,5]:
    print(num)

'''specify data's range'''
for num in range(10):
    print("num=" + str(num))
    print("num*num=" + str(num*num))

'''while: iterate as long as condition is true '''
count = 5
while count > 0:
    print(str(count))
    count -= 1
    
#数当てゲーム
import random
r = random.randrange(100)

while True:
    x = int(input("number?"))
    if x < r:
        print("smaller")
    elif x > r:
        print("bigger")
    else:
        print("right")

        
'''"break;": break the loop'''
while True:
    value = int(input("yen"))
    if value == 0:
        print("0 is inputted.")
        break;
    print(100 / value)

    
'''"continue": continue this loop'''
remain = 5
while remain > 0:
    print(str(remain))
    value = int(input("what?"))
    if value == 0:
        print("0 is inputted.")
        continue;
    print(100 /value)
    remain -= 1

    
'''output index and value from a list'''
city = ["Tokyo", "Beijing", "Hongkong", "Shenzhen"]
for i, c in enumerate(city):
    # string.format() function
    print("{}: {}".format(i, city[i]))

    
'''output from multiple list, use function zip()'''
city = ["Tokyo", "Beijing", "Shanghai", "hangzhou"]
code = [0, 1, 2, 3]

for i,j in zip(city, code):
    # because in loop, so (i, j) not (city, code)
    print("{}({})".format(i,j))
    
    
'''excetions'''
try:
    # run this code
    linux_interaction()
except AssertionError as error:
    # run this code when there is exception
    print(error)
else:
    # no exceptions? run this code
    try:
        with open('file.log') as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)
finally:
    # always run this code
    print('clean up')
    
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
        break
print("over")


'''judge inputted number is prime number or not?''' 
n = int(input("Data?"))
for i in range(1, n + 1):
    if n % i == 0:
        if i != 1 and i != n:
            print("bushisushu")
            # why break?
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
