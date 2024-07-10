def special_multiplication(string):
    str=''
    for idx,value in enumerate(string):
        for i in range(idx+1):
            str+=value
    return str
print(special_multiplication('abcxf'))
