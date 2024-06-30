
n=int(input("Enter a number: "))

rows=1
spaces=n-1
stars=1
while rows<=n:
    m=1
    while m<= spaces:
        print(' ',end='')
        m+=1
    spaces-=1
    k=1
    while k<=stars:
        print('*',end='')
        k+=1
    stars+=2
    print('\n')
    rows+=1


rows=1
spaces=0
stars=9
while rows<=n:
    m=1
    while m<= spaces:
        print(' ',end='')
        m+=1
    spaces+=1
    k=1
    while k<=stars:
        print('*',end='')
        k+=1
    stars-=2
    print('\n')
    rows+=1
