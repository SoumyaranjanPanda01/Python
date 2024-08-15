# lower = converts string into lower case
# upper = converts string into upper case
# capitalize = converts the first character to upper case
# title = converts the first letter of each word to capital letter
# swapcase = swaps lower to upper case and vice- versa

a = "soumya RANJAN"
print(a.lower())
print(a.upper())
print(a.capitalize())
print(a.title())
print(a.swapcase())

# islower
# isupper
# istitle

x = "Python"
print(x.islower())
print(x.isupper())
print(x.istitle())

# isdigit
# isalpha
# isalnum

i = "somu0438"
print(i.isdigit())
print(i.isalpha())
print(i.isalnum())

# strip
# lstrip
# rstrip

t = "     python     "
print(t.strip())
print(t.lstrip())
print(t.rstrip())

# startswith
# endswith

w = "hello"
print(w.startswith('h'))
print(w.endswith('h'))

# count
# index
# replace

r = "Python String method's"
print(r.count('t'))
print(r.count('s'))
print(r.index('t'))
print(r.index('m'))
print(r.replace('S','s'))