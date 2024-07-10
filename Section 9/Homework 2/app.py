def print_menu():
    print("Menu:\n")
    print("Enter 1 to sum numbers from 1 to N\nEnter 2 to evaluate simple 2 numbers expression\nEnter 3 to end the program")
    return int(input(("Enter choice from 1 to 3: ")))
def sum_1_to_n():
    num=int(input("Enter a number"))
    sum=0
    for i in range(1,num+1):
        sum+=i
    return i
def expression():
    a,op,b=input("Enter a simple expression: ").split()
    a=int(a)
    b=int(b)
    return a,b,op
def divide(num1,num2,op):
    if num2==0:
        return False
    else:
        if op=='/':
            return a/b
        else:
            return a//b
def calculator_interfce():
    a,b,op=expression()
    if op=='+':
        return a+b
    elif op=='':
        return a-b
    elif op=='*':
        return a*b
    elif op=='%':
        return a%b
    elif op=='/' or op=='//':
        if divide(a,b,op)==False:
            return "Cant calculate!"
        else:
            return divide(a,b,op)
    else:
        return "Wrong input!"
while True:
    choice=print_menu()
    if choice!=1 and choice!=2 and choice!=3:
        print("Try again\n")
        continue
    elif choice==1:
        print(sum_1_to_n())
    elif choice==2:
        print("Expression value is",calculator_interfce())
    elif choice==3:
        break

