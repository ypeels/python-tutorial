print '''
Section 7.1: Fancier Output Formatting
- str() converts any value to human-readable string
- repr() converts any value to Python interpreter-readable string

In particular, repr(string) adds string quotes and backslashes

Formatting commands
- string.rjust(<# chars>) right-justifies. see also ljust() and center()
- print '<printf-like string>'.format() is like printf()
- zfill() pads numeric strings with leading zeros
- curly braces in format() are escaped by doubling {{ }}
'''

# without indices, format() works JUST like printf {index:width format}
for x in range(1, 11):
    print '{{ {:2d} {:3d} {:4d}'.format(x, x**2, x**3)
#{  1   1    1
#{  2   4    8
#{  3   9   27
#{  4  16   64
#{  5  25  125
#{  6  36  216
#{  7  49  343
#{  8  64  512
#{  9  81  729
#{ 10 100 1000


# !s and !r apply str() and repr() respectively...
# these don't seem to play well with the other format specifiers {x:yf}...
import math
print 'pi = {} unformatted'.format(math.pi)
print 'pi = {!s} str() formatted'.format(math.pi)
print 'pi = {!r} repr() formatted'.format(math.pi)

# keyword and position arguments work too! 
# Section 4.7.2 rules apply to format()!!
print 'The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred', other='Georg')


# duh, evaluating dictionary[key] inside the {}
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print ('Jack: {0[Jack]:10d}; Sjoerd: {0[Sjoerd]:10d}; '           # inserting {0} in multiple locations
    'Dcab: {0[Dcab]:10d}'.format(table))

# OR just use **dict to convert dictionary to keywords

print '''
Section 7.1.1: Old string formatting
Use "%xx.yyF" for ACTUAL printf formatting
'''