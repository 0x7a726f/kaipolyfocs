import time
def euclid(a,b):
    if a == 0:
        return b
    else:
        return euclid(b % a,a)

def bgcd(a,b):
    if a == b: 
        return a
    elif a % 2 == 0 and b % 2 == 0:
        return 2*bgcd(a//2,b//2)
    elif a % 2 == 0 and b % 2 != 0:
        return bgcd(a//2,b)
    elif b % 2 == 0 and a % 2 != 0:
        return bgcd(a,b//2)
    else:
        return bgcd(min(a,b),abs(a-b)//2)

def bgcd_iter_bits(a,b):
    if a == 0:
        return b
    if b == 0:
        return a

    shift = 0
    while (a | b) & 1 == 0: 
        a >>= 1
        b >>= 1
        shift += 1

    while a & 1 == 0:
        a >>= 1
    while b != 0:
        while b & 1 == 0:
            b >>= 1
        if a > b:
            a, b = b, a
        b -= a
    return a << shift


a = pow(3,245)
b = pow(4,295)

t1 = time.perf_counter()
res1 = euclid(a,b)
t2 = time.perf_counter()
print("Euclid =", res1)
print("Time taken: ", t2 - t1, " seconds")

t1 = time.perf_counter()
res1 = bgcd(a,b)
t2 = time.perf_counter()
print("BGCD =", res1)
print("Time taken: ", t2 - t1, " seconds")

t1 = time.perf_counter()
res1 = bgcd_iter_bits(a,b)
t2 = time.perf_counter()
print("BGCD bit shift / iterably =", res1)
print("Time taken: ", t2 - t1, " seconds")