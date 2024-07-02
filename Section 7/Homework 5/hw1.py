while True:
    n = int(input("Enter an odd number: "))
    if n % 2 != 0:
        for i in range(n):
            for j in range(n):
                if j == i or j == n - 1 - i:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
        break
    else:
        print("Wrong input! Please enter an odd number.")
        continue

"""""
while 1:
    n=int(input("Enter an odd number: "))
    if n%2!=0:
        for i in range(n):
            if i<= n//2:
                for j in range(n-i,n):
                    print(" ",end='')
            else:
                for j in range(i,n-1):
                    print(" ",end='')
            print("*")
            if i <= n // 2:
                for k in range(i*2,n-2):
                    print(" ",end='')
            else:
                for k in range(2*i-n,0,-1):
                    print(" ",end='')
            print("*")
            print("\n")
        break
    else:
        print("Wrong input!")
        continue
"""""
