# 因为下面有return，所以最后的函数指令无效，因此输出为0
def print_nums(x):
   for i in range(x):
      print(i)
      return
print_nums(10)

# res += i 没理解好吧
def func(x):
   res = 0
   for i in range(x):
      res += i
   return res
print(func(10))
