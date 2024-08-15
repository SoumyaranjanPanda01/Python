import random

r1 = random.sample(list(range(20)),3)
r2 = random.sample(list(range(20)),3)
r3 = random.sample(list(range(20)),3)

A = []
A.append(r1)
A.append(r2)
A.append(r3)


s1 = random.sample(list(range(20)),3)
s2 = random.sample(list(range(20)),3)
s3 = random.sample(list(range(20)),3)

B = []
B.append(s1)
B.append(s2)
B.append(s3)

print(A)
print(B)

dim = 3  #dimension

C = [[0,0,0],[0,0,0],[0,0,0]]

# Matrix addition
for i in range(dim):
    for j in range(dim):
        C[i][j] = A[i][j] + B[i][j]
print(C)
