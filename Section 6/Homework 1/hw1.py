a,b=map(int,input("Enter two numbers: ").split())
if a%2==1 and b%2==1:
    print(a*b)
elif a%2==0 and b%2==0:
    print(a/b)
elif a%2==1 and b%2==0:
    print(a+b)
else:
    print(a-b)