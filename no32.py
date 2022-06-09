a=int(input("enter number"))
i=2
b=1
print(b,end=",")
while i<=a:
    if i%2==0:
        b=i**2
        print("+",b,end="")
    else:
        print("-",i**2,end=",")
    i=i+1