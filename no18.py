binary=int(input("enter number"))
i=1
d=0
while binary!=0:
    remaider=binary%10
    binary=binary//10
    d=d+remaider*i
    i=i*2
    print("decimal number is",d)