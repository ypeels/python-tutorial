print '''
Section 5.6: Looping Techniques

The section talks about "looping through a sequence".
This is more general than iterables, since UNORDERED entities like sets and dictionaries can be looped over.

In other words, the techniques in this section are all applicable to:
- lists
- tuples
- sets (unordered)
- dictionaries (unordered)
'''

print '''
Use enumerate() to retrieve an index and value during iteration.
This is admittedly less useful for unordered sequences... running counter, but that's it...

Interestingly, enumerate() returns a black-box "enumerate object" which you can then "sequence-unpack" using "in":
>>> for i, v in enumerate(['tic', 'tac', 'toe']):
...     print i, v, '\t', 
'''
for i, v in enumerate(['tic', 'tac', 'toe']):
    print i, v, ';',                            # 0 tic ; 1 tac ; 2 toe ;
    
    
print '''
To loop over multiple sequences simultaneously, use zip() to generate tuples:
>>> questions = ['name', 'quest', 'favorite color']
>>> answers = ['lancelot', 'the holy grail', 'blue']
>>> punctuation = ['!', '...', '???']
>>> for q, a, p in zip(questions, answers, punctuation):
...     print 'What is your {0}? It is {1}{2}'.format(q, a, p)'''
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
punctuation = ['!', '...', '???']
for q, a, p in zip(questions, answers, punctuation):
    print 'What is your {0}? It is {1}{2}'.format(q, a, p)
    

print '''
Other useful functions:
- reversed(seq)
- sorted(seq)
- dict.iteritems() - use this like enumerate(), except it's "key, value in dict.iteritems()"
- use a COPY to modify your sequence (cf. Section 4.2)'''