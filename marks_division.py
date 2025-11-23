marks = int(input("Enter the marks out of 500: "))
b=(marks/500)*100
print("Your percentage is:",b)
if marks>500:
    print("Wrong Input")
elif b>60:
    print("First Division!!")
elif b>50:
    print("Second Division!!") 
elif b>40:
    print("Third Division!!")
else:
    print("Fail!")               
