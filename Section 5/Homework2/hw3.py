a,b=map(int,input("Enter two numbers: ").split())
print("The reminder:",int((a/b-a//b)*b))
print(a%b)