# Fibonacci numbers module
# n.b. module name '6.0-fibo-module' did NOT work

def fib(n):             # WRITE Fibonacci series up to n
    a, b = 0, 1
    while b < n:
        print b,
        a, b = b, a+b
        
def fib2(n):            # RETURN Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result

print "Hello world from", __file__