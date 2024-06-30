n=int(input("Enter integer n: "))
cnt=0
i=1
odd=0
odd_cnt=0
even=0
even_cnt=0
while cnt<n:
    num=int(input("Enter a number: "))
    if i%2==0:
        even+=num
        even_cnt+=1
    else:
        odd+=num
        odd_cnt+=1
    i+=1
    cnt+=1
print(odd/odd_cnt,even/even_cnt)
