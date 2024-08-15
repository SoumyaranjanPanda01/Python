#strings are treated like lists, they are indexed just like lists, starting from 0

c = "coffee"
b = "bread"

print(c[1])
print(c[1:4]) #goes from 1 to 3
print(b[-1])
print(b[1:4]) #goes from 1 to 3

#we can use + and * operators on strings and not - and /

g = "good"

print(g[3]+g[2])
print(g[3]*5)

print('apple' > 'one') #compares every letter of the string
print('apple' > 'one')
a = "huvdskpdjoife1234"
print(len(a))