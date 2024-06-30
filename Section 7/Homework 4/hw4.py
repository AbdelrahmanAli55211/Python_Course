t=int(input("Enter the number of test cases: "))
cnt1=0
while cnt1<t:
    n=int(input("Enter number of integers: "))
    cnt2=1
    sum=0
    while cnt2<=n:
        num=int(input("Enter a number: "))
        m=0
        mul=1
        while m<cnt2:
            mul=mul*num
            m+=1
        sum+=mul
        cnt2+=1

    cnt1+=1
    print("Sum=",sum)