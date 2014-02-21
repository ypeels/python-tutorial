import sys
print '''
Although it is not part of the Python language per se,
the 'sys' module is built into every Python interpreter.

The variables sys.ps1 and sys.ps2 are the (modifiable) strings 
for the primary and secondary interactive prompts!

Note that these variables are only defined if 
the interpreter is in interactive mode!!
'''

# these commands won't run from a script
#print "sys.ps1 =", sys.ps1
#print "sys.ps2 =", sys.ps2

print 'Also of value is "sys.path", which is mutable'
print "sys.path =", sys.path