"""String"""
# Can do same operations as list
# also can use for loop

#create a string
message = "hello!"

# count the numbers
print(message.count("hello!"))
# if contains hello or not
print("hello" in message)
# string slice
print(message[::-1])

# count up using a dictionary
city = input("Where are you from?")
city = city.lower()
city = city.replace(" ","")
city_list = city.split(",")
# create a dictionary
city_dic = {"dongjing":4}
for i in city_list:
    # if city's key exist, then plus 1
    if i in city_dic:
        # designation that key's value
        city_dic[i] += 1
    else:
        city_dic[i] = 0
print(city_dic)


"""list comprehension: [...for ... in ... if...], can create list efficiently."""
# example: create a list
num_square = []
for num in [1,2,3,4,5]:
    num_square.append(num ** 2)
print(num_square)

num_square = [num ** 2 for num in [1,2,3,4,5]]
print(num_square)

# create string use [], set use {}, dictionary use {}
#create dictionary from two list by function zip
day_num = [1, 2, 3, 4, 5, 6, 7]
day_en = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

days = {num:en for (num,en) in zip(day_num,day_en)}
print(days)


# becasue float no iterable, so transform to list.
myresults = []
## range(start, stop) = start, stop-1
## range(1, 3) = [1, 2]
## if hace no "len(cols_x) - 1", output will divergence.
for i in range(len(cols_x)-1):
    distance = math.sqrt((cols_x[i+1] - cols_x[i]) ** 2 + (cols_y[i+1]-cols_y[i]) ** 2)
    print(distance)
    myresults.append(distance)
print(sum(myresults))


# 入力された値についての内包表記
city = input("Where are you from?")
city_lower = city.lower()
city_rep = city_lower.replace(" ","")
city_list = city_rep.split(",")
# have miss in i
city_t = [ i.upper() for i in city_list if i.startswith("t")]
print(city_t)
