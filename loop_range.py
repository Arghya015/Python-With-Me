n=int(input("Enter your range:"))
m=int(input("Enter your range:"))
print("All your odd numbers are:")
i=n
while i<=m:
    if i%2==0:
        i+=1
        continue
    print(i)
    i+=1
