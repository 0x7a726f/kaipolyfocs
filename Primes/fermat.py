import random

def fermat(prime):
    res = True
    for i in range(30):
        a = random.randint(2, prime - 1)
        if pow(a, prime - 1, prime) != 1:
            print(f"{a} is a Fermat liar, {prime} is not prime")
            res = False
            break
    if res:
        print(f"{prime} is prime")
    print()

fermat(67280421310721)
fermat(170141183460469231731687303715884105721)
fermat(pow(2,2281)-1)
print("Carmichael numbers: Περνάνε το τέστ αλλά είναι σύνθετοι.")
fermat(84154807001953)
fermat(464052305161)
