l = [[],[4],(1,2),[3,4],(5,6,7)]
result = []

for t in l:
    sum = 0
    for n in t:
        sum += n
    result.append(sum)

print(result)