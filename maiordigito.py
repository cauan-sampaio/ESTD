def maiorDigito(n):
    if n < 10:
        return n
    else:
        if n % 10 > maiorDigito(n // 10):
            return n % 10
        else:
            return maiorDigito(n // 10)
result = maiorDigito(34)
print(result)