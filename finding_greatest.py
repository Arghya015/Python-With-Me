num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
num3 = int(input("Enter three number:"))
num4 = int(input("Enter four number:"))

if num1 > num2 and  num1 > num3 and num1 > num4:
    print("The greatest is", num1)
elif num2 > num3 and num2 > num4:
    print("The greatest is", num2)
elif num3 > num4:
    print("The greatest is", num3)
elif num4 > num3:
    print("The greatestb is", num4)   
