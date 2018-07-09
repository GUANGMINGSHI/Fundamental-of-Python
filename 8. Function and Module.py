## define function(1-one argument)
def s(message):
    # don't know this means
    value = int(input(message))
    if value < 0:
        print("you are wrong.")
    return value
# use function you defined, no need input()
bottom = s("bottom")
high = s("high")
print(bottom * high / 2)

## define function(2-many argument)
def s(bottom, high):
    area = bottom * high / 2
    return area
# use function you defined, no need input()
s = s(3, 4)
print(s)
