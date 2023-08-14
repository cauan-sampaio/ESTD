def zerarPar(n):
    if n < 10:
        if n % 2:
            return n
        else:
            return 0
    else:
        if (n % 10) % 2:
            return n % 10 + 10 * zerarPar(n // 10)
        else:
            return 10 * zerarPar(n // 10)

result = zerarPar(45)
print(result)
