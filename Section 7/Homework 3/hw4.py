t=int(input("Enter the number of test cases: "))
while t>0:
    n=int(input("Enter the number of integers: "))
    n1 = int(input("Enter an integer: "))
    min=n1
    while n>1:
        if n1<min:
            min=n1
        n1 = int(input("Enter an integer: "))
        n-=1
    if n1<min:
        min=n1
    print("The min=",min)
    t-=1