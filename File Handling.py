f = open('my text.txt','w')

f.write("My name is Somu")
f.write("\n")
f.write("I am 19 years old")
f.write("\n")
f.write("I am in IITM")
f.close()

f = open('my text.txt','r')
s = f.read()
print(s)
f.close()
