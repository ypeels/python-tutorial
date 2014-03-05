print '''
Section 5.7: More on Conditions
- have discussed them explicitly yet??

1. elem 'in' ('not in') seq checks whether elem occurs (does not occur) in seq
'''


print '''
2. 'is' != '==', and 'is not' != '!=' !!!!!!
- The operators is and is not compare whether two objects are really the same object;
  this only matters for mutable objects like lists.
--- [it does NOT compare values!!]

http://stackoverflow.com/questions/2576826/pythons-preferred-comparison-operators
- x is y is true if and only if id(x) == id(y) 
--- that is, x and y have to be one and the same object (with the same ids).

>>> 1 is 1'''
print 1 is 1                            # True
print ">>> 1 is 2"
print 1 is 2                            # False
print ">>> 1 is not 2"
print 1 is not 2                        # True

print ">>> s = 'abc'"
print ">>> s is 'abc'"
s = 'abc'
print s is 'abc'                        # True!? because string literals are immutable??

print "x, y = 1, 1"
x, y = 1, 1
print ">>> x is y"                      # also True...
print x is y

print '''
Beware!!! __name__ is a special object, and "is" testing will not check value correctly...'''
print "__name__ is '__main__':", __name__ is '__main__'
print "__name__ == '__main__':", __name__ == '__main__'



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

- [set1] > [set2] returns False ALWAYS??? no, my first impression was wrong
-- http://docs.python.org/2/library/stdtypes.html#set-types-set-frozenset
--- gt/lt become SET COMPARISON OPERATORS. Cool!
--- Two sets are equal if and only if every element of each set is contained in the other (each is a subset of the other).
--- A set is less than another set if and only if the first set is a proper subset of the second set (is a subset, but is not equal).
--- A set is greater than another set if and only if the first set is a proper superset of the second set (is a superset, but is not equal).


soooooooo much undefined behavior

AHA! Footnote:
[1]	The rules for comparing objects of different types should not be relied upon; they may change in a future version of the language

in other words, the behavior more or less IS undefined...
'''