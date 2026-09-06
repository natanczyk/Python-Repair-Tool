def sieve(max):
    primes = []
    is_prime = [True] * (max + 1)
    is_prime[0], is_prime[1] = False, False
    
    for n in range(2, max + 1):
        if is_prime[n]:
            primes.append(n)
            for i in range(n*n, max + 1, n):
                is_prime[i] = False
                
    return primes