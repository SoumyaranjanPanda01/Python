import random
l = []
for i in range (30):
    l.append(random.randrange(1,365))
l.sort()
print(l)

i = 0
flag = 0
while (i<len(l)-1):
    if (l[i] == l[i+1]):
          print("there is a repetation at", i, "and the no. is", l[i])
          flag = 1
          break
    i = i+1
if (flag == 0):
        print("no repeatation observed")