import time,sys
sys.set_int_max_str_digits(1000000)
memo={}
def fib1(n):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib1(n - 1) + fib1(n - 2)
    return memo[n]

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

def matrix_multiply(A, B):
    return [
        [
            A[0][0] * B[0][0] + A[0][1] * B[1][0],
            A[0][0] * B[0][1] + A[0][1] * B[1][1],
        ],
        [
            A[1][0] * B[0][0] + A[1][1] * B[1][0],
            A[1][0] * B[0][1] + A[1][1] * B[1][1],
        ],
    ]

def matrix(matrix, n):
    result = [[1, 0], [0, 1]]  
    base = matrix
    while n > 0:
        if n % 2 == 1:
            result = matrix_multiply(result, base) 
        base = matrix_multiply(base, base)
        n //= 2

    return result

def fib3(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    fib_matrix = [[1, 1], [1, 0]]
    result_matrix = matrix(fib_matrix, n - 1)
    return result_matrix[0][0]

n = 500
t1 = time.perf_counter()
print("Fibonacci(" + str(n) + ") =", fib1(n))
t2 = time.perf_counter()
print("Time taken: ", t2 - t1, " seconds (recursion + memo)")
t1 = time.perf_counter()
print("Fibonacci(" + str(n) + ") =", fib2(n))
t2 = time.perf_counter()
print("Time taken: ", t2 - t1, " seconds (repeats)")
t1 = time.perf_counter()
print("Fibonacci(" + str(n) + ") =", fib3(n))
t2 = time.perf_counter()
print("Time taken: ", t2 - t1, " seconds (2 x 2 matrix)")
