nums = [1,4,9,16,25,36,49,64,81,100]
x=int(input("Enter you x:"))
i=0
for val in nums:
    if val == x:
        print("Value find at", i)
        break
    i+=1
    
