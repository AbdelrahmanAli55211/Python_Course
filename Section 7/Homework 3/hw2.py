n=int(input("Enter a number:"))
n1=0
while n1<=n:
    if n1%8==0 or n1%4==0 and n1%3==0:
        print(n1,end=' ')
    n1+=1