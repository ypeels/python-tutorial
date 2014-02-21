print '''
Section 6.3: The dir() function

This is NOT a filesystem function
Instead, dir(module) lists all names defined in module.
'''

print ">>> import sys"
import sys
print ">>> dir(sys)"
print dir(sys)


# basic syntax from my section 6.1 notes
import imp
fibo = imp.load_source('giggity', '6.0-fibo-module.py') # Hello world from '6.0-fibo-module.py(c)'
print dir(fibo)         # NOT giggity!

print ""
print ">>> dir() # prints all names in current scope"
print dir()

print '''
dir() does not list the names of built-in functions and variables. 
If you want a list of those, they are defined in the standard module __builtin__:
>>> import __builtin__
>>> dir(__builtin__)'''
import __builtin__
print dir(__builtin__)
