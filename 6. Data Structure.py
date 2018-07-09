# data type
値の型整数型(int), 浮動小数点型(float), 文字列型(str)

# データ構造
リスト、タプル、集合、辞書


"""list"""
city = ["Tokyo", "Kyoto", "Saporo", "Naha", "Sendai", "Hakata", "Nagoya"]
# show third one
print(city[2])
# change sixth one to "matuyama"
city[5] = "matuyama"
# add another list, should plus "[]"
city = city + ["hiroshima", "kanazawa"]
# repeat this list
city = city * 2
# retrieve a part of list
print(city[2:5])
# add an element to the end of list
print(city.append("Shibuya"))
# delete the last element of list
print(city.pop())
# delete a element of list by "index" and "same thing"
del city[1]
city.remove("Tokyo")
# Align this list
align = sorted(city)
print(align)


"""Tuple: a list cannot change element."Immutable": same as list"""
# create tuple use "()" rather than "[]"
grade_tuple = (10,20,30)
# convert tuple to list.
grade_list = list(grade_tuple)


"""Set: a list have no same value"""
# create a set use "{}"
rank = {"A", "B"}
# also can convert from list


"""Dictionary: a list designate by "key" rather than "Index""""
# create a dictionary
joho_score = {"E0123":60, "T2468":90, "M8901":45}
print(joho_score["E0123"])
