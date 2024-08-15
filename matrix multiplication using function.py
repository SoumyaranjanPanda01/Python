# matrix multiplication

def mm(x,y):
    z = [[0,0,0],[0,0,0],[0,0,0]]
    dim = 3
    for i in range(dim):
        for j in range(dim):
            for k in range(dim):
                 z[i][j] = z[i][j] + x[i][k] * y[k][j]
    mm = []
    mm.append(z[0])
    mm.append(z[1])
    mm.append(z[2])
    return mm

x = [[4, 6, 9], [7, 9, 1], [7, 4, 0]]
y = [[0, 5, 6], [6, 3, 9], [8, 7, 1]]

print(mm(x,y))
