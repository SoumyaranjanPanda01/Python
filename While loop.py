# it gets executed till the condition is met
# it quits when condition is met

print("when did india got indipendence?")
year = int(input())
while (year != 1947):
    print("you got it wrong, try again")
    year = int(input())
print("correct answer")

# computed factorial

n = int(input("enter a no."))
i = 1
f = 1
while (i<=n):
    f=f*i
    i=i+1
print("factorial of",n,"is",f)