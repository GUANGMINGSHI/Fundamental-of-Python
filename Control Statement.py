"""control statement"""
# specify data individually
for num in [1,2,3,4,5]:
    print(num)

# specify data's range
for num in range(10):
    print("num=" + str(num))
    print("num*num=" + str(num*num))

# while: run n times until a defined condition is no longer met
count = 5
while count > 0:
    print(str(count))
    count -= 1

# "break;": break the loop
while True:
    value = int(input("yen"))
    if value == 0:
        print("0 is inputted.")
        break;
    print(100 / value)

# "continue": continue this loop
remain = 5
while remain > 0:
    print(str(remain))
    value = int(input("what?"))
    if value == 0:
        print("0 is inputted.")
        continue;
    print(100 /value)
    remain -= 1

    
