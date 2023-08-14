def menorDigito(n):
    if n < 10:
        return n
    else:
        last_digit = n % 10
        rest_digits_min = menorDigito(n // 10)
        return min(last_digit, rest_digits_min)

# Test the function
result = menorDigito(362951)
print(result)  # Output should be the smallest digit in the number, which is 1
