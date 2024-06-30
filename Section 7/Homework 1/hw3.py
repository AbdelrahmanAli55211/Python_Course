n=int(input("Enter a number: "))
while n>0:
    star_cnt=0
    while star_cnt<n:
        print('*',end='')
        star_cnt+=1
    print('\n')
    n-=1