al = "abcdefghijklmnopqrstuvwxyz"
t = ''
i = 0
k = 1
n = 'amaan'
t += (al[(al.index(n[i])+k)%26])
t += (al[(al.index(n[i+1])+k)%26])
t += (al[(al.index(n[i+2])+k)%26])
t += (al[(al.index(n[i+3])+k)%26])
t += (al[(al.index(n[i+4])+k)%26])

print(t)

# al.index(n[i]) = finds index of 'i'th letter of n
# al.index(n[i+1]) = increase the index of that specific letter by 1