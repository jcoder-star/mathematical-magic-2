def is_prime(num):
    """Check if a number is a prime number."""
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def find_two_digit_primes():
    """Find all two-digit prime numbers."""
    primes = []
    for num in range(10, 100):
        if is_prime(num):
            primes.append(num)
    return primes

# Find and print all two-digit prime numbers
two_digit_primes = find_two_digit_primes()
print("Two-digit prime numbers are:", two_digit_primes)
