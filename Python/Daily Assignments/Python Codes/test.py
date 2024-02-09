# Fibonnacci Series
def fibonacci(n):
    fib_series = [0, 1]
    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series

result = fibonacci(10)
print(result)


# Prime number
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

print(is_prime(7))


# Harshad Number
def is_harshad(num):
    if num <= 0:
        return False
    digit_sum = sum(map(int, str(num)))
    return num % digit_sum == 0

print(is_harshad(18))


# Armstron Number
def is_armstrong(num):
    order = len(str(num))
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10
    return num == sum

print(is_armstrong(153))

# GCD
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

print(gcd(48, 18))




