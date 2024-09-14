a = int(input("enter a no."))
if a < 18:
    print("you are underage, you are not allowed to vote")

a = int(input("enter a no."))
if a < 18:
    raise Exception("you are underage, you are not allowed to vote")
    # exceptions made by us depending upon the condition

