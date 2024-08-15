'''This methode is a alternative of obvious search, it'll do the same thing but in an efficient way,
which is popularly called the binary search'''

def binary_search(l,k):
    '''it is to search any no. between the given list in a efficient way'''

    # we need to shrink the list so we could find the no. easily
    # we need to find the mid point first mid point = (end + beginning)//2

    begin = l[0]
    end = l[-1]

    while (end - begin > 1):
        mid = (end + begin)//2
        if (mid == k):
            return 1

        # if the no. is smaller than mid remove the right side part
        if (k < mid):
            end = mid-1
            # and retain the left hand side to continue the rest of search

        # if the no. is larger than mid remove the left side part
        if (k > mid):
            begin = mid+1
            # and retain the right hand side to continue the rest of search

    # now we are out of while loop, it means end- begin is either equal to or smaller than 1
    # it means list only have either one or two values
    if (end == k) or (begin == k):
        return 1
    else:
        return 0

import time
l = range(10000000)
k = 9999999
a = time.time(); print(binary_search(l,k)); b = time.time()
print(b-a)

def check_k(l,k):
    for x in l:
        if x == k:
            return 1
    return 0
c = time.time(); print(check_k(l,k)); d = time.time()
print(d-c)