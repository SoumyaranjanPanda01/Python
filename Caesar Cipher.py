'''the program considares an input file and encrypts it by using caeesar cipher. by that mean, we shift the letters by 3 units .
for example a will become d and f will become i, similarly y will become b and z will become c'''

import string

def create_caesar_dict():
    l = string.ascii_lowercase
    l = list(l)
    d = {}
    for i in range(len(l)):
        d[l[i]] = l[(i+3)%26]
    return d

f = open('Sherlock Holmes.txt', 'r')
g = open('encrypted sherlock holmes.txt','w')
d = create_caesar_dict()

c=f.read(1)
while (c!=''):
    g.write(d[c])
    c=f.read(1)

f.close()
g.close()

x = open('encrypted sherlock holmes.txt','r')
y = x.read()
print(y)