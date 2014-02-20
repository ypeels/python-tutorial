x_range = range(11)

squares_C = []
for x in x_range:
    squares_C.append(x**2)   
print 'squares (the C way):', squares_C                 # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

squares_listcomp = [x**2 for x in x_range]
print 'squares (the listcomp way):', squares_listcomp   # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print 'C == listcomp?', squares_C == squares_listcomp   # True

squares_lambda = map(lambda x: x**2, x_range)
print 'squares (the lambda way):', squares_lambda       # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print 'C == lambda?', squares_C == squares_lambda       # True



print ''                                                # [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
print "List comprehensions can also generate tuples (don't forget parentheses!!)"
print [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]  

print ''
print "Basically, this is an alternative syntax for filter/map"

vec = range(-4, 5, 2)
print "vec =", vec                                      # vec = [-4, -2, 0, 2, 4]

print ''                                                # [-8, -4, 0, 4, 8]
print "[x*2 for x in vec] =", [x*2 for x in vec]            
print "map(lambda x: x*2, vec) =", map(lambda x: x*2, vec)

print ''                                                # [0, 2, 4]
print "[x for x in vec if x >= 0] =", [x for x in vec if x >= 0]    
print "filter(lambda x: x >= 0, vec) =", filter(lambda x: x >= 0, vec)

print ''                                                # [4, 2, 0, 2, 4]
print "[abs(x) for x in vec] =", [abs(x) for x in vec]
print "map(lambda x: abs(x), vec) =", map(lambda x: abs(x), vec)

print ''                                                # ['banana', 'loganberry', 'passion fruit']
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
print "freshfruit =", freshfruit
print "[w.strip() for w in freshfruit] =", [w.strip() for w in freshfruit]
print "map(lambda w: w.strip(), freshfruit) =", map(lambda w: w.strip(), freshfruit)

print ''                                                # [(-4, 16), (-2, 4), (0, 0), (2, 4), (4, 16)]
print "[(x, x**2) for x in vec] =", [(x, x**2) for x in vec] # don't forget to parenthesize tuples!!
print "map(lambda x: (x, x**2), vec) =", map(lambda x: (x, x**2), vec)

print ''
print ''
print "Okay, finally, here is an example that seems non-trivial for map/filter:"
matrix = [[1,2,3], [4,5,6], [7,8,9], [10,11,12]]
print "matrix =", matrix
print "[num for row in matrix for num in row] =", [num for row in matrix for num in row]

# -------------------------------------------

print '\n', '-' * 40, '\n'
print "Section 5.1.4.1: Nested List Comprehensions"

print ''
print "matrix =", matrix                                # [[1,2,3], [4,5,6], [7,8,9], [10,11,12]]

# [[1,4,7,10], [2,5,8,11], [3,6,9,12]]
print ''
print "[[row[col] for row in matrix] for col in range(len(matrix[0]))] ="
print [[row[col] for row in matrix] for col in range(len(matrix[0]))]

def print_args(*args):
    for arg in args:
        print arg, ',',
    print ''
    
print ''
print "Alternative using zip() library function..."
print "*matrix ="
print_args(*matrix)
print "zip() documentation: This function returns a list of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables."
print ''
print "[list(row) for row in zip(*matrix)] ="           # inverse of list() is tuple()
print [list(row) for row in zip(*matrix)]
