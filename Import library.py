# In this we are using libraries that python have
# for eg: math is a library that python have

import math
print(math.pi)
print(math.sqrt(9))
print(math.factorial(5))
print(math.log(1000,10))

# let's toss a coin

import random
a=random.random()
if (a<0.5):
    print("heads")
else:
    print("tails")

# let's roll a die

import random
print(random.randrange(1,7))

# import calender

'''import calendar
print(calendar.month(2024,7))
print(calendar.calendar(2028))'''

from calendar import * # this helps import the necessary things only from a library
print(calendar(2024))
# we can be more specific
from calendar import month
print(month(2024,7))
import calendar as c
print(c.month(2024,8))
from calendar import month as m
print(m(2024,9))