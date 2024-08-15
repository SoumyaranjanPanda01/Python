def list_min(l):
    mini = l[0]
    for i in range(len(l)):
        if (l[i] < mini):
            mini = l[i]
    return mini

def list_max(l):
    maxi = l[0]
    for i in range(len(l)):
        if (l[i] > maxi):
            maxi = l[i]
    return maxi

def average(l):
    sum = 0
    for i in range(len(l)):
        sum = sum + l[i]
    avg = sum / len(l)
    return avg

l = [10,11,-10,100,256,13,47]

print(list_min(l))
print(list_max(l))
print(average(l))