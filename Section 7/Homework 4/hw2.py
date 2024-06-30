num=int(input("Enter a number: "))
num2=num
dig_num=0
while num !=0:
    num//=10
    dig_num+=1
num1=0
cnt=0
while cnt<dig_num:
    num1+=(num2%10)*(10**(dig_num-1-cnt))
    num2//=10
    cnt+=1
print(num1,num1*3)
