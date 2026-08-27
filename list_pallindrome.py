e1=int(input("Enter your first element:"))
e2=int(input("Enter your second element:"))
e3=int(input("Enter your third element:"))
e4=int(input("Enter your fourth element:"))
list1=[e1,e2,e3,e4]
copy_list = list1.copy()
copy_list.reverse()
if(list1==copy_list):
    print("Yes, pallindrome")
else:
    print("No sorry")
