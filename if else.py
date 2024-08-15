# yob = year of birth
yob = int(input("enter your yob:"))
currentyear = 2024
age = currentyear - yob
if (age < 18):
    print("sorry, you are not allowed")
else:
    print("welcome aboard")

# elif

marks = int(input("enter your marks out of 100:"))
if (marks >= 0 <=100):
    if (marks >= 90):
        print("A grade")
    elif (marks >= 80):
        print("B grade")
    elif (marks >= 70):
        print("C grade")
    elif (marks >= 60):
        print("D grade")
    elif (marks <= 60):
        print("E grade")
else:
    ("invalid input")
