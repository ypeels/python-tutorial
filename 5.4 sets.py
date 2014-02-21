print '''
Lists: mutable ordered collections
Tuples: immutable ordered collections
Sets: UNORDERED collections with NO DUPLICATES

Create sets using {} or set().
An empty set can ONLY be created using set() because {} is an empty dictionary (hash)...

From library API: sets are mutable via member functions:
- update() or |=
- intersection_update() or &=
- difference_update() or -=
- symmetric_difference_update() or ^=
- add(elem)
- remove(elem) [KeyError if not found]
- discard(elem) [no error if not found]
- pop() [remove and return an arbitrary element; KeyError if empty]
'''

fruit_list = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
fruit_set = set(fruit_list)
print fruit_set                 # set(['orange', 'pear', 'apple', 'banana'])
print "Fast membership testing, like 'orange' in fruit_set"

print '''
The best part: set operations are nice and simple too!
>>> a = set('abracadabra')  # {'abracadabra'} yields a SINGLETON set
>>> b = set('alacazam')     # seems more like set() behaves inconsistently...
'''
a = set('abracadabra')
b = set('alacazam')

print "a =", a              # a = set(['a', 'r', 'b', 'c', 'd'])
print "b =", b              # b = set(['a', 'c', 'z', 'm', 'l'])
print "a - b =", a - b      # Difference:           set(['r', 'b', 'd'])
print "a | b =", a | b      # Union:                set(['a', 'c', 'b', 'd', 'm', 'l', 'r', 'z'])
print "a & b =", a & b      # Intersection:         set(['a', 'c'])
print "a ^ b =", a ^ b      # Symmetric Difference: set(['b', 'd', 'm', 'l', 'r', 'z'])
print "(a - b) | (b - a) =", (a - b) | (b - a) # symmetric difference


print '''
Set comprehensions work just like list comprehensions, but with enclosing curly braces {} instead of brackets[]

>>> c = {x for x in 'abracadabra' if x not in 'abc'}
>>> c'''
c = {x for x in 'abracadabra' if x not in 'abc'}
print c                     # set(['r', 'd'])