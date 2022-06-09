a=int(input("enter number"))
i=0
sum=1
b=1
while i<=a:
    sum=sum+i
    i=i+1
    print(b,"+","x","/",i,"!","+",end="")
    b=b+1
print(sum)