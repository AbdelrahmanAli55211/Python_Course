num1,num2,num3,num4,num5=map(int,input("Enter 5 numbers: ").split())
req1=(num1+num2+num3+num4+num5)/5
req2=(num1+num2+num3)/(num4+num5)
req3=(num1+num2+num3)/3/(num4+num5)/2
print(req1,req2,req3)