a = int(input('enter a no.'))
b = int(input('enter a no.'))

if a<b:
    small = a
else:
    small = b
print(small)

# inline programming

c = int(input('enter a no.'))
d = int(input('enter a no.'))

large = c if c>d else d
print(large)