print("travel from city a to b")
time = int(input("enter time"))
long = int(input("enter long"))
if (time >= long):
    price = int(input("enter price"))
    high = int(input("enter high"))
    if (price >= high):
        print("train")
    else:
        print("coach")
else:
    price = int(input("enter price"))
    high = int(input("enter high"))
    if (price >= high):
        print("daytime flight")
    else:
        print("red eye flight")