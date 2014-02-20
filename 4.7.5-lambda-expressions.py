# syntactic sugar
def make_incrementor(n):
    return lambda x: x + n # in ruby notation, { |x| x + n }
    
f = make_incrementor(42)
print f(0) # 42
print f(1) # 43



pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]

pairs.sort( key =   # key = function that takes a single argument and returns a key for sorting
    lambda x: x[1]  # lambda [parameter_list]: expression. You can optionally parenthesize the whole lambda, if it makes you feel more at ease... 
) 

print pairs # [4, 1, 3, 2]