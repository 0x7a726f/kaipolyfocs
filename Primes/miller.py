import random
def miller_rabin(n):
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

def check(prime):
    if miller_rabin(prime):
        print(str(prime) + " is prime")
    else:
        print(str(prime) + " is not prime")
    print()

check(67280421310721)
check(170141183460469231731687303715884105721)
check(pow(2, 2281) - 1)
print("Carmichael numbers: Περνάνε το τέστ fermat αλλά είναι σύνθετοι.")
check(84154807001953)
check(464052305161)

