def sieve(max):
    primes = []
    for n in range(2, max + 1):
        if all(n % p != 0 for p in range(2, int(n ** 0.5) + 1)):
            primes.append(n)
    return primes