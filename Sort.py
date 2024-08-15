'''
this code returns sorted form of a list
'''

def min(l):
    x = l[0]
    for i in l:
        if (i<x):
            x = i
    return x

def sort(l):
    if (l==[]) or (len(l)==0):
        return l

    m = min(l)
    l.remove(m)
    return [m]+sort(l)

print(sort([2,5,38,6,0,19 ,12,3,4]))