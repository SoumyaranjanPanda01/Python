def sum(n):
    s = 0
    for i in range(n):
        s = s+i
    return s

import time

a = time.time(); sum(100); b = time.time()
print(b - a)
# gives the time taken to add 100 no's

import Recursion

l = range(100)
Recursion.check_k(l,90)
#finds if 90 is there in first 100 no's or not (Obvious search)
a = time.time(); Recursion.check_k(l,90); b = time.time()
print(b-a)
#prints time taken to find 90 in first 100 no's
