n=int(input("Enter a number: "))
for i in range(1,n):
    sum=0
    for j in range(1,i):
        if i%j==0:
            sum+=1
    if sum==1 or i==1:
        print(i,end=" ")
