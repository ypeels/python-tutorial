print '''
Section 9.9: Iterators
This ALMOST doesn't belong in a chapter about classes...
except it shows you how to make your class iterable
(i.e., it can be used in the "in" clause of a "for" loop)
- implement __iter__() method which returns an object with a next() method (typically self)
- implement said next() method
'''

print '''
Section 9.10: Generators
This section almost seems included JUST as an alternative to class-based iterators...

- written like regular functions, but use "yield" instead of "return"
- all data values AND execution point are saved. scary...
- raises StopIteration on termination, which is how "for" loops terminate internally.

"local variables and execution state are automatically saved between calls. 
This made the function easier to write and much more clear than an approach using instance variables 
like self.index and self.data."
- I dunno, it introduces a bunch of mysterious, implicit, unwritten code to me...

See the example:
'''

def reverse(data):                      # generator definition
    for index in range(len(data)-1, -1, -1):
        yield data[index]
        
for char in reverse('golf'):
    print char,                         # f l o g
print ""



print '''
Section 9.11: Generator Expressions
This section seems like it was included because it is the common use case of generator-like syntax?

At first sight, these look more to me like list comprehensions that are not stored...
I would rather think of it as the missing reduce() comprehension-equivalent for Section 5.1.4...
'''

print sum(i*i for i in range(10))       # generator expression
print sum([i*i for i in range(10)])     # list comprehension - less storage-friendly (stores intermediate list)

data = 'golf'
print list(data[i] for i in range(len(data)-1, -1, -1))     # haha, generator expression to generate list
print [data[i] for i in range(len(data)-1, -1, -1)]         # direct list comprehension