def nth_fib(n):
    sum=0
    prev_sum=1
    prev_sum2=0
    for i in range(2,n):
        sum=prev_sum2+prev_sum
        prev_sum2 = prev_sum
        prev_sum=sum
    return sum
for i in range(1,10):
    print(i,nth_fib(i))