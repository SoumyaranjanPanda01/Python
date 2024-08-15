
s = str(input("enter a string"))

def upper(s):
    upper = 0
    for c in s:
        if (c.isupper()):
            upper += 1
    return (upper)

def lower(s):
    lower = 0
    for c in s:
        if (c.islower()):
            lower += 1
    return (lower)

def characters(s):
    chars = 0
    for c in s:
        chars += 1
    return (chars)

def words (s):
    words = 1
    for c in s:
        if (c==" " ):
            words += 1
    return (words)

print(upper(s))
print(lower(s))
print(characters(s))
print(words(s))