'''
this is a piece of code to check weather the given list has any 0 or not in it. True(1) False(0)
'''

def check0(l):
    if (len(l) == 0):
        return False
    if (l[0] == 0):
        return True
    else:
        return check0(l[1:len(l)])

ans = check0([1,2,0,9,28,37,0,54])
print(ans)

def check_k(l,k):
    for x in l:
        if x == k:
            return True
    return False

ans = check_k([1,2,0,9,28,37,0,54],28)
print(ans)