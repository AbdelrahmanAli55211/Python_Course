n1,n2,n3,n4,n5,n6=map(int,input("Enter the intervals: ").split())
num=int(input("Enter a number: "))
sum=0
if num>=n1 and num<=n2:
    sum+=1
if num>=n3 and num<=n4:
    sum+=1
if num >= n5 and num <= n6:
    sum+=1

print(sum)