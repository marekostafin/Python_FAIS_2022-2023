def factorial(n):
    if n == 0:
        return 1
    else:
        f = 1
        for i in range(1, n+1):
            f *= i
        return f