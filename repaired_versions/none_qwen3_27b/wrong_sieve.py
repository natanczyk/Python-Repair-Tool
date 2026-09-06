def sieve(max):
    if max < 2:
        return []
    
    # Create a boolean array "is_prime[0..max]" and initialize all entries as True
    is_prime = [True] * (max + 1)
    is_prime[0] = False
    is_prime[1] = False
    
    p = 2
    while p * p <= max:
        if is_prime[p]:
            # Mark all multiples of p as not prime
            for i in range(p * p, max + 1, p):
                is_prime[i] = False
        p += 1
    
    # Collect all prime numbers
    primes = [p for p in range(2, max + 1) if is_prime[p]]
    return primes