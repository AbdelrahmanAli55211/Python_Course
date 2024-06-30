n=int(input("Enter the numebr of strings: "))
cnt=0
while cnt<n:
    x_str=input()
    str_len=len(x_str)
    if str_len==2:
        if x_str=='NO' or x_str=='No' or x_str=='nO' or x_str=='no' or x_str=='ON' or x_str=='On' or x_str=='oN' or x_str=='on':
            print("Match:",x_str)
    cnt+=1