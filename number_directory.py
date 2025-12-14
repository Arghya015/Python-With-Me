m={}
n=int(input("Enter no of directories you want:"))
for i in range(n):
    mob=int(input("Enter mobile number: "))
    name=input("Enter name:")
    m.update({mob:name})
print(m)
search_no=int(input("Enter the number for searching:"))

print("The name of the person is",m[search_no])
