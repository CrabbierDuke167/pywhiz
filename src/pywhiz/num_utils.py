def is_prime(n):
    """Checks if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_armstrong(n):
    """Checks if a number is an Armstrong number (e.g. 153)."""
    temp = n
    digits = len(str(n))
    total = 0
    while temp > 0:
        digit = temp % 10
        total = total + (digit ** digits)
        temp = temp // 10
    if total == n:
        return True
    else:
        return False

def fibonacci(terms):
    """Generates a list of Fibonacci numbers up to n terms."""
    if terms <= 0:
        return []
    if terms == 1:
        return [0]
    series = [0, 1]
    for i in range(2, terms):
        next_term = series[i - 1] + series[i - 2]
        series.append(next_term)
    return series

def hcf(a, b):
    """Finds Highest Common Factor (GCD) of two numbers."""
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Finds Least Common Multiple of two numbers."""
    if a == 0 or b == 0:
        return 0
    return (a * b) // hcf(a, b)