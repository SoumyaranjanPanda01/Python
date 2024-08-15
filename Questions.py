# calculate no. of upper case, lower case, characters and no of words

n = input("enter")
def uc(n):
    upper = 0
    for c in n:
        if (n.isupper()):
            upper += 1
    return (upper)

def lc(n):
    lower = 0
    for c in n:
        if (n.islower()):
            lower += 1
    return (lower)

def char(n):
    char = 0
    for c in n:
        char += 1
    return (char)

def word(n):
    word = 1
    for c in n:
        if (c == " "):
            word += 1
    return (word)

print(uc(n))
print(lc(n))
print(char(n))
print(word(n))