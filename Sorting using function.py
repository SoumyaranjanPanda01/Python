# sorting

def minimum(l):
    mini = l[0]
    for i in range(len(l)):
        if (l[i] < mini):
            mini = l[i]
    return mini

l = [30,40,20,50,10]
x = []

while (len(l)>0):
    x.append(minimum(l))
    l.remove(minimum(l))

print(x)
print(l)