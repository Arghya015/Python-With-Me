nums=(1,4,9,16,25,36,49,64,81,100)
n=int(input("Enter your number:"))
i=0
while i<= len(nums)-1:
    if n==nums[i]:
        print("Matched", n,"at",i)
        break
    else:
        print("no match")
    i+=1
