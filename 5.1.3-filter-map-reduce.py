# 5.1.3 Functional Programming Tools

def f(x): return x % 2 != 0 and x % 3 != 0  # lookee, an "inline" function
#def g(x, y): return x + y > 10
print "filter:"
print filter(f, range(2, 25))    # [5, 7, 11, 13, 17, 19, 23]
#print "filter (2 sequences):", filter(f, range(1,8), range(1, 8))
print ""

def cube(x): return x**3                    # FORTRAN-STYLE EXPONENTIATION WORKS
def add(x, y): return x+y
print "map:"
print map(cube, range(1, 11))               # [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
print map(add, range(1, 11), range(1, 11))  # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20] - multiple arguments for map() only, NOT filter() or reduce()
print ""

print "reduce:"
print reduce(add, range(1, 11))             # 55
print reduce(add, range(1, 11), 10)         # optional third argument = accumulator initial value