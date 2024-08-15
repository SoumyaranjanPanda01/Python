#short hand operator

count = int(input("enter a value"))
count = count + 1
count += 1
print(count)

count2 = int(input("enter another no."))
count2 -= 2
print(count2)

#special operator
#in = in operator, used to find some specific value in string or variable or list,etc

print('alpha' in 'a variable name only can contain alpha-numeric character and underscores')
print('alpha' in 'a persons age only can contain numbers')

#chaining operator
#when two or more relational operators are used together

x = 5
print(10<x<15)
print(10<x>15)
print(10>x<15)
print(10>x>15) #basically it acts like a  logical operator, both statements needs to be true to get the output true
