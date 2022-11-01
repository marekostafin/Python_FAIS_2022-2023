keys = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
values = [1000, 500, 100, 50, 10, 5, 1]

D = dict(zip(keys, values))
D = {}
for (k, v) in zip(keys, values):
    D[k] = v

def roman2int(input):
    sum = 0
    for r in range(0, len(input)-1):
        if D[input[r]] < D[input[r+1]]:
            sum -= D[input[r]]
        else:
            sum += D[input[r]]
    sum += D[input[len(input)-1]]
    return sum