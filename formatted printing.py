# end = attribute for the end of command or string, etc.
# sep = seprator between two strings
# for eg. date

d = 6
m = 7
y = 2024
print("today's date is", end=" ")
print(d,m,y, sep="/")

# formatted printing
n= int(input("enter a no."))
for i in range(1, 11):
    # regular print
    print(n, "X", i, "=", n * i)
    # formatted priting
    print(f'{n} X {i} = {n*i}') # objects inside brakets are variables
    # .format
    print('{0} X {1} = {2}'.format(n,i,n*i))
    # %d = integer
    print('%d X %d = %d' % (n, i, n*i))

# %f = float
pi = 22/7
print("value of pi = %f" %(pi))
print(f'value of pi = {pi:.2f}') # :.nf prints n values after the decimal

# eg
print('{0:5d}'.format(1))
print('{0:5d}'.format(11))
print('{0:5d}'.format(111))
print('{0:5d}'.format(1111))
print('{0:5d}'.format(11111))