import random

a = random.sample(list(range(10)),3)
b = random.sample(list(range(10)),3)
c = random.sample(list(range(10)),3)

m = []
m.append(a)
m.append(b)
m.append(c)
print(m)

x = random.sample(list(range(10)),3)
y = random.sample(list(range(10)),3)
z = random.sample(list(range(10)),3)

n = []
n.append(x)
n.append(y)
n.append(z)
print(n)

t = [[0,0,0],[0,0,0],[0,0,0]]
dim = 3

for i in range(dim):
    for j in range(dim):
        for k in range(dim):
            t[i][j] = t[i][j] + m[i][k] * n[k][j]

ans = []

ans.append(t[0])
ans.append(t[1])
ans.append(t[2])

print("matrix multiplication of the given matrices is", ans)

