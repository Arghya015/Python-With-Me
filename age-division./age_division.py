age=int(input("Enter your age: "))
if age>0 and age<=3:
    print('Child')
elif age>3 and age<=12:
    print("Kid")  
elif age>12 and age<=19:
    print("Teen")
elif age<=30:
    print("Young")   
elif age<=60:
    print("Man")
else:
    print("Old")      
