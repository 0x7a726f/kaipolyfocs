phi = 1.6180339887498948482
def golden(n):
    return round(pow(phi,n)/2.236067977499789)

def fib2(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    a = 0
    b = 1
    for _ in range(2, n + 1):
        a, b = b, a + b 
    return b  

n = 50
print(golden(n)) , print(fib2(n)) , print()
n = 100
print(golden(n)) , print(fib2(n)) , print()
n = 200
print(golden(n)) , print(fib2(n))


