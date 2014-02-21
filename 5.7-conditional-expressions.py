print '''
Section 5.7: More on Conditions
- have discussed them explicitly yet??

1. elem 'in' ('not in') seq checks whether elem occurs (does not occur) in seq
'''


print '''
2. 'is' == '==', and 'is not' == '!='
n.b. type must match, i.e., set(a) != tuple(a)

>>> 1 is 1'''
print 1 is 1                            # True
print ">>> 1 is 2"
print 1 is 2                            # False
print ">>> 1 is not 2"
print 1 is not 2                        # True

print '''
3. Interestingly, comparison operators can be chained!!
>>> 1 < 2 == 2'''
print 1 < 2 == 2                        # True

print '''
4. Boolean 'and' and 'or' evaluate lazily from left to right.

The example in Section 5.7 relies on the definition of False
http://docs.python.org/2/library/stdtypes.html
The following values are considered false:
    None
    False
    zero of any numeric type, for example, 0, 0L, 0.0, 0j.
    any empty sequence, for example, '', (), [].
    any empty mapping, for example, {}.
    instances of user-defined classes, if the class defines a __nonzero__() or __len__() method, 
      when that method returns the integer zero or bool value False. 
All other values are considered true
'''


print '''
Bonus (Section 5.8):
Sequence objects may be compared to other objects with the same sequence type.
The comparison uses lexicographical ordering.

Weirdness
- list(a) < set(b) for ANY a, b. This is because 'list' < 'set'
- similarly, int(i) < string(s) for ANY i, s.
- Mixed [REAL] numeric types are compared according to their numeric value
- complex(c) can ONLY be tested for equality with numeric types
- complex(c) < string(s) for ANY c, s, because 'complex' < 'string'


Moar weirdness: unordered sequences can only be tested for EQUALITY, and not gt/lt
- set > list returns TypeError
- set > seq returns TypeError for ALL sequence types except set
- dict > seq returns TypeError for ALL sequence types except dict
- NOT sure how dict comparisons are made... dicts in alphabetical order?
- NOT sure how dict/numerical comparisons are made
- [set1] > [set2] returns False ALWAYS???

soooooooo much undefined behavior'''