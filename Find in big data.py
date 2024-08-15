a = open('big data.txt','w')
a.write('9327053058\n')
a.write('8849911745\n')
a.write('9998269964\n')
a.write('7990590921\n')
a.close()


b = open('big data.txt','r')
s = b.readline()
print(s)
s = b.readline()
print(s)
s = b.readline()
print(s)
s = b.readline()
print(s)
b.close()


c = open('big data.txt','r')
flag = 0
s = '0'
while(s != ''):
    s = c.readline()
    if (s != ''):
        x = int(s)
        if (x == 7980590921):
            flag = 1
            print("number is found")
            break
if (flag == 0):
    print("number is not found")
