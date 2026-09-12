n=int(input("Enter a number: "))
fac=1
def fact(m):
    fac=1
    for i in range (1, m+1):
        fac=fac*i
    print(fac)
fact(n)
