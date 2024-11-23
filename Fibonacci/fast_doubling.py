import time,sys
sys.set_int_max_str_digits(100000000)
sys.set_int_max_str_digits(100000000)

def fibonacci(n):
	return fib(n)[0]

def fib(n):
	if n == 0:
		return (0, 1)
	else:
		a, b = fib(n // 2)
		c = a * (b * 2 - a)
		d = a * a + b * b
		if n % 2 == 0:
			return (c, d)
		else:
			return (d, c + d)
n = 1000000
t1 = time.perf_counter()
a = fib(n)[0]
t2 = time.perf_counter()
print("Fibonacci(" + str(n) + ") =", a)
print("Time taken: ", t2 - t1, " seconds")

