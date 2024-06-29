n1,n2,n3,n4=map(int,input("Enter the interval: ").split())
if n2>n3 and n1>n3:
    if n2>n4:
        print("The common interval is: [",n1,n4,"]")
    else:
        print("The common interval is: [",n1,n2,"]")
elif n2>n3 and n1<n3:
    if n2<n4:
        print("The common interval is: [", n3, n2, "]")
    else:
        print("The common interval is: [", n3, n4, "]")
else:
    print(-1)