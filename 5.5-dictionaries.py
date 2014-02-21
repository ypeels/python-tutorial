print '''
Dictionaries are like hashes in Ruby.
Keys can be any immutable type: strings, numbers, and tuples without any mutable elements.

Evidence that dictionaries are more primitive than sets:
- {} creates an empty dictionary, NOT an empty set
- dict: del d[key]   vs.  set: s.remove(elem) [well, sets ain't iterable]
'''

print "dict() constructor can operate on any iterable of iterable pairs? (list and tuple both seem to work)"
print "dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]) =", \
    dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])             # {'sape': 4139, 'jack': 4098, 'guido': 4127}
print "dict((('sape', 4139), ('guido', 4127), ('jack', 4098))) =", \
    dict((('sape', 4139), ('guido', 4127), ('jack', 4098)))             # {'sape': 4139, 'jack': 4098, 'guido': 4127}
print "dict((('sape', 4139), ['guido', 4127], ('jack', 4098))) =", \
    dict((('sape', 4139), ['guido', 4127], ('jack', 4098)))             # {'sape': 4139, 'jack': 4098, 'guido': 4127}
print "dict([('sape', 4139), ['guido', 4127], ('jack', 4098)]) =", \
    dict([('sape', 4139), ['guido', 4127], ('jack', 4098)])             # {'sape': 4139, 'jack': 4098, 'guido': 4127}
print "etc."

print '''
Keyword arguments also automagically work, for keys that are simple strings:
>>> dict(sape=4139, guido=4127, jack=4098)'''
print dict(sape=4139, guido=4127, jack=4098)                            # {'sape': 4139, 'jack': 4098, 'guido': 4127} 

print '''
Finally, DICT COMPREHENSIONS are created just like you would expect, using
{ key: value     for... if... }
>>> {x: x**2 for x in (2, 4, 6)}'''
print {x: x**2 for x in (2, 4, 6)}                                      # {2: 4, 4: 16, 6: 36}