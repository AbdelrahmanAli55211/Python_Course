n1,n2=map(int,input("Enter 2 numbers: ").split())
cnt1=1
while cnt1<=n1:
    cnt2=1
    while cnt2<=n2:
        print(cnt1,'x',cnt2,'=',cnt1*cnt2)
        cnt2+=1
    cnt1+=1