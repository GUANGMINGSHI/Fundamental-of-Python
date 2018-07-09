# define function
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
