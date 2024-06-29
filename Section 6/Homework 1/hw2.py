a,b,c=map(int,input("Enter 3 numbers: ").split())
if a<b:
    if a<c:
        min=a
        if b<c:
            mid=b
            max=c
        else:
            mid=c
            max=b
else:
    if b<c:
        min=b
        if c<a:
            mid=c
            max=a
        else:
            mid=a
            max=c
print(min,mid,max)