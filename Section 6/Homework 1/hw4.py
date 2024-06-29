n1,n2,n3,n4,n5=map(int,input("Enter 5 numbers: ").split())
num=int(input("Enter a number: "))
more=0
less=0
if n1>num:
    more+=1
else:
    less+=1
if n2>num:
    more+=1
else:
    less+=1
if n3>num:
    more+=1
else:
    less+=1
if n4>num:
    more+=1
else:
    less+=1
if n5>num:
    more+=1
else:
    less+=1
print(less,more)