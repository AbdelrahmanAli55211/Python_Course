cnt = int(input())
if 1<=cnt and cnt<=10:
    # read first number
    result = float(input())
    cnt -= 1

    # read UP to 9 times
    if cnt > 0:
        num = float(input())
        cnt -= 1
        if num > result:
            result = num

    if cnt > 0:
        num = float(input())
        cnt -= 1
        if num > result:
            result = num

    if cnt > 0:
        num = float(input())
        cnt -= 1
        if num > result:
            result = num

    if cnt > 0:
        num = float(input())
        cnt -= 1
        if num > result:
            result = num

    if cnt > 0:
        num = float(input())
        cnt -= 1
        if num > result:
            result = num

    if cnt > 0:
        num = float(input())
        cnt -= 1
        if num > result:
            result = num

    if cnt > 0:
        num = float(input())
        cnt -= 1
        if num > result:
            result = num

    if cnt > 0:
        num = float(input())
        cnt -= 1
        if num > result:
            result = num

    if cnt > 0:
        num = float(input())
        cnt -= 1
        if num > result:
            result = num


    print(result)
else:
    print("Wrong input!")