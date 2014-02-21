print '''
See the link in Section 5.3 for a comprehensive list of Sequence Types
'''

t = 12345, 54321, 'hello!'
print ">>> t = 12345, 54321, 'hello!'"  # tuple packing
print t                                 # (12345, 54321, 'hello!')

print ">>> x, y, z = t"                 # tuple unpacking
x, y, z = t
print "x =", x, ", y =", y, ", z =", z  # x = 12345 , y = 54321 , z = hello!
print "'Note that multiple assignment is really just a combination of tuple packing and sequence unpacking.'"


print '''
Tuples are immutable!
>>> l = list(t)
>>> l[0] = 0
>>> tuple(l)'''
l = list(t)
l[0] = 0
print tuple(l)

print '''
Empty or singleton tuples have 'inconsistent', hacky syntax...
>>> empty = ()
>>> singleton = 'hello',                # ('hello')! would be a bare string
>>> len(singleton)
>>> singleton'''
empty = ()
singleton = 'hello',
print len(singleton)                    # 1
print singleton                         # ('hello',) - looks like SOMEBODY would prefer the serial comma



print '''
Tuples are:
- immutable!!! (like strings)
- usually heterogeneous
- usually accessed via unpacking or indexing

Lists are:
- mutable
- usually homogeneous
- usually accessed by iterating over the list

Of course, these are interconvertible using list() and tuple()
'''
