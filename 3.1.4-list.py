print '''
Confusingly, lists use the same syntax as strings, but are NOT read-only...
Let a = ['spam', 'eggs', 100, 1234]

First, READ operations
----------------------'''

a = ['spam', 'eggs', 100, 1234]
print 'a[0] =', a[0] # 'spam'
print 'a[1:-1] =', a[1:-1] # [ 'eggs', 100 ]
print "a[:2] + ['bacon', 2*2 ] =", a[:2] + ['bacon', 2*2 ] # [ 'spam', 'eggs', 'bacon', 4 ]
print "3 * a[:2] =", 3 * a[:2] # [ 'spam', 'eggs', 'spam', 'eggs', 'spam', 'eggs' ]


print '''
Then, WRITE operations
----------------------
>>> a[2] = a[2] + 23
>>> a'''
a[2] = a[2] + 23
print a # ['spam', 'eggs', 123, 1234]
print ''

# ugh forget it, typing is too slow - i'll just do modified copy/paste.

print "Replace some items via list range:"
a[0:2] = [1, 12]
print "a[0:2] = [1, 12]: ", a # [1, 12, 123, 1234]
print ''

print "Remove some:"
a[0:2] = []
print "a[0:2] = []: ", a # [123, 1234]
print ''

print "Insert some (remember your slicing rules from 3.1.2!!):"
a[1:1] = ['bletch', 'xyzzy']
print "a[1:1] = ['bletch', 'xyzzy']: ", a # [123, 'bletch', 'xyzzy', 1234]
print '' 

print "Insert (a copy of) itself at the beginning:"
a[:0] = a
print "a[:0] = a: ", a # [123, 'bletch', 'xyzzy', 1234, 123, 'bletch', 'xyzzy', 1234]
print ''

print "Clear the list: replace all items with an empty list"
a[:] = []
print "a[:] = []:", a # []
print '\n'



print "Finally, nested lists:"
q = [2, 3]
p = [1, q, 4]
# p[1:1] = q # this does NOT work!? "concatenates" instead of nesting
print "q = ", q
print "p = [1, q, 4] =", p

print '''
Note shallow copy:
>>> p[1].append('xtra')'''
p[1].append('xtra')
print "p =", p # [1, [2, 3, 'xtra'], 4]
print "q =", q # [2, 3, 'xtra']


