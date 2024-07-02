n,a,b=map(int,input("Enter 3 numbers: ").split())
sum=0
for i in range(1,n+1):
    i=str(i)
    sum_dig=0
    for char in i:
        char=int(char)
        sum_dig+=char
    if sum_dig<=b and sum_dig>=a:
        sum+=int(i)
print(sum)
