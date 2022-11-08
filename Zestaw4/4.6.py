def  sum_seq(sequence):
    sum = 0
    for x in sequence:
        if isinstance(x, (list, tuple)):
            sum += sum_seq(x)
        else:
            sum += x
    return sum