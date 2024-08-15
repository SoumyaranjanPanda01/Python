import random
x = random.sample(list(range(100)),5)
y = random.sample(list(range(100)),5)
print(x)
print(y)

a = 0
for i in range(len(x)):
    b = x[i] * y[i]
    a = a + b
print("dot product of x and y is",a)