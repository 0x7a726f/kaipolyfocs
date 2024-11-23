import random
def miller(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    d = n - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1
    for _ in range(30):
        a = random.randint(2, n - 2)  
        x = pow(a, d, n) 
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def find_primes():
    primes = []
    for i in range(2,200):
        if miller(i):
            primes.append(i)
    return primes

def mersenne():
    primes = find_primes()
    for p in primes:
        m_prime = (2 ** p) - 1
        if miller(m_prime):
            print(str(2) + "^" + str(p) + " - 1 = " + str(m_prime) + " is a Mersenne prime")

mersenne()
