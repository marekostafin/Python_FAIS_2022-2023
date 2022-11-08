def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        e = 0
        f = 1
        for i in range(2, n+1):
            g = e + f
            e = f
            f = g
        return f