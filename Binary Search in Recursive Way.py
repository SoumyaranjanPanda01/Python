
def binary_search(l,k,begin,end):
    '''it is to search any no. between the given list in a efficient way'''

    # we need to shrink the list so we could find the no. easily
    # we need to find the mid point first mid point = (end + beginning)//2

    # if there is only one no in the list
    if (end == begin):
        if (l[begin] == k):
            return 1
        else:
            return 0

    # for small lists
    if (end - begin == 1):
        if (end == k) or (begin == k):
            return 1
        else:
            return 0

    if (end - begin > 0):

        mid = (end + begin)//2
        if (mid == k):
            return 1
        # it implies when the no we finding is a mid value

        # if the no. is smaller than mid remove the right side part
        if (k < mid):
            end = mid-1
            # and retain the left hand side to continue the rest of search

        # if the no. is larger than mid remove the left side part
        if (k > mid):
            begin = mid+1
            # and retain the right hand side to continue the rest of searchS

    if (end-begin < 0):
        return 0

    return binary_search(l,k,begin, end)

import time
l = range(10000000)
k = 9999999
a = time.time(); print(binary_search(l,k,0,10000000)); b = time.time()
print(b-a)

def check_k(l,k):
    for x in l:
        if x == k:
            return 1
    return 0
c = time.time(); print(check_k(l,k)); d = time.time()
print(d-c)