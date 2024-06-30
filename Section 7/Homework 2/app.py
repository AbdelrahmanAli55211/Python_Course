a=0
while a==0:
    print("Menu:")
    print("Enter 1 to sum from 1 to N\n2 to evaluate 2 numbers expression\n3 to end the program")
    while 1:
        choice = int(input("Enter 1 or 2 or 3: "))
        if choice !=1 and choice !=2 and choice !=3:
            print("Wrong input please try again! ")
            continue
        else:
            if choice==3:
                print("End of the program Thanks! ")
                a=1
                break
            else:
                if choice==1:
                    num=int(input("Enter N: "))
                    num1=num
                    sum=0
                    while num>0:
                        sum+=num
                        num-=1
                    print("Sum from 1 to",num1,"=",sum)
                elif choice==2:
                    n1,op,n2=input("Enter a simple exp: ").split()
                    n1=int(n1)
                    n2=int(n2)
                    if op=='+':
                        print("Exp. value is:",n1+n2)
                    elif op=='-':
                        print("Exp. value is:", n1 - n2)
                    elif op=='*':
                        print("Exp. value is:", n1 * n2)
                    elif op=='/':
                        if n2==0:
                            print("Cannot find the value!")
                        else:
                            print("Exp. value is:", n1 / n2)
                    else:
                        print("Wrong operation!")
        print("\n")
        break


