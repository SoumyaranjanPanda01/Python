l = [10,99,232,87,5,12,8,7,980,56,43,10]

x = []
while(len(l)>0):
    min = l[0]
    for i in range(len(l)):
        if (l[i]<=min):
            min = l[i]
    x.append(min)
    l.remove(min)

print(x)
print(l)
