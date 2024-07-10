def is_prime(num):
    sum=0
    for i in range(1,num):
        if num%i==0:
            sum+=1
    if sum==1:
        return True
    return False

def nth_prime(n):
    sum=0
    i=1
    while True:
        res=is_prime(i)
        if res==True:
            sum+=1
        if sum==n:
            return i
        i+=1

print(nth_prime(6))

