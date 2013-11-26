def find_primes(limit):
    primes = [2]
    i = 3
    while i <= limit:
        is_prime = True
        sqrt_limit = int(i**(0.5) + 1)
        for prime in primes:
            if i % prime == 0:
                is_prime = False
                break
            if prime >= sqrt_limit: 
                break
        if is_prime:
            primes.append(i)
            print ".",
        i += 2
    print
    return primes