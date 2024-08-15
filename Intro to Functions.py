def add(a,b):
    ans = a+b
    return ans
def sub(a,b):
    ans = a-b
    return ans
def discount(cost,d):
    ans = cost - (cost*(d/100))
    return ans

p = add(10,8)
print(p)
q = sub(100,90)
print(q)

cost = int(input("enter the cost"))
d = int(input("enter the discount"))
print("your final price after the discount of",d,"% would be",discount(cost, d))