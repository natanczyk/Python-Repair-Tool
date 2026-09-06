def sieve(max):
    if max < 2:
        return []
    
    # Create a boolean array "prime[0..max]" and initialize
    # all entries it as true.
    prime = [True for _ in range(max + 1)]
    p = 2
    while (p * p <= max):
        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):
            # Updating all multiples of p
            for i in range(p * p, max + 1, p):
                prime[i] = False
        p += 1
    
    # Collect all prime numbers
    primes = []
    for p in range(2, max + 1):
        if prime[p]:
            primes.append(p)
            
    return primes