from re import I


n=int(input("enter number"))
i=1
a=i
sum=0
while i<=n:
    a=a*i
    sum=sum+a
    print(a,",",end=",")
    i=i+1
print(sum)