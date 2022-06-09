a=int(input("enter number"))
r=0
i=a
while a>0:
    r=r*10+a%10
    a=a//10
if i==r:
    print("palindrome")
else:
    print("not palindrome")