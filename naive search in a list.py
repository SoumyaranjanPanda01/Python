import random

l = []
for i in range(1000000):
    l.append(random.randrange(1,10000000))
flag = 0
a = 0
while (a>-1):
    print("enter a no., type -1 to exit")
    a = int(input())
    for i in range(len(l)):
        if (a == l[i]):
            print("i found it")
            flag = 1
    if (a > 10000000):
        print("enter a valid value")
        flag = 1
    if (flag == 0):
        print("value not found")