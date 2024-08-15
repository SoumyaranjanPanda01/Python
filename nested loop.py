# nested for loop prints nested statements
#two brothers have t-shirts of color

s = "VIBGYOR"
t = "VIBFYOR"

count=0
for i in range(7):
    for j in range(7):
        print(s[i],t[j])
        count = count + 1
print("no of ways they can wear t-shirts are",count)
