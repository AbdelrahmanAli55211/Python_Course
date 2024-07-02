n=int(input("Enter a number: "))
sum=0
for i in range(1,n):
    if n%i==0:
        sum+=1
if sum==1 or n==1:
    print("Yes")
else:
    print("No")