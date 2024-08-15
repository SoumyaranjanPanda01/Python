# find factorial of given no.

n = int(input("enter a no."))
i = 1
f = 1
while (i<=n):
    f=f*i
    i=i+1
print("factorial of",n,"is",f)

# find the no. of digits in the given no.

n = abs(int(input("enter a no.")))
digit = 1
while ( n>9 ):
    n= n//10
    digit += 1
print("no.of digits are",digit)

# reverse the given no.

num = int(input("enter a no."))
rev = num % 10
num = num // 10
while (num > 0):
    r = num % 10
    num = num // 10
    rev = rev * 10 + r
print(rev)