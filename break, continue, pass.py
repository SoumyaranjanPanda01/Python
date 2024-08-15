# break = stops the iteration

email = input("enter your student email")
for u in email:
    if(u=='@'):
        break
    print(u)

# continue = skips the iteration

mail = input("enter your mail")
for i in mail:
    if (i == '@'):
        continue
    print(i)

# pass = it's just a place holder

for x in range(11):
    if(x%3 == 0):
        print(x)
    else:
        pass