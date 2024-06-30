while 1:
    n=int(input("Enter a number: "))
    if n<=30 and n>=1:
        cnt=0
        m=0
        while cnt<n:
            while 1:
                if m%3==0 and m%4 !=0:
                    print(m,end=' ')
                    m+=1
                    break
                else:
                    m+=1
            cnt+=1
        break
    else:
        print("Try again!")
        continue