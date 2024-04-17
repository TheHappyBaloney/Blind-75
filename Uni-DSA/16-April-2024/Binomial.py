# binomial coefficient of a number

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def binomial(n, k):
    if k == 0:
        return 1

    elif k == 1:
        return k

    else:
        binom = factorial(n) / (factorial(k) * factorial(n - k))
        return binom


# Usage of the function

print(binomial(5, 2)) # 10