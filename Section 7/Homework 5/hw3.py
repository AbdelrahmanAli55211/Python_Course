sum=0
for a in range(1,201):
    for b in range(1,201):
        for c in range(1,201):
            d=a+b-c
            if d>=1 and d<=201:
                sum+=1
print(sum)