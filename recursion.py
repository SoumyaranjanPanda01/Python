# compound interest

def ci(amount,roi,time):
    while (time > 0):
        amount = amount + (amount*roi)/100
        time = time - 1
    return amount

print(ci(1000,5,5))

# sum of n no.

def sum(n):
    if (n == 1):
        return 1
    else:
        return n+sum(n-1)

print(sum(10))

# factorial of n no.

def fact(n):
    if (n == 1):
        return 1
    else:
        return n*fact(n-1)

print(fact(7))
