def removePar(n):
    if n < 10:
        if n % 2:
            return n
        else:
            return 0
    else:
        if (n % 10) % 2:
            return n % 10 + 10 * removePar(n // 10)
        else:
            return removePar(n // 10)

# Test the function
result = removePar(24683512)
print(result)  # Output should be 153



