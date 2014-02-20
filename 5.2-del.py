a = [-1, 1, 66.25, 333, 333, 1234.5]
print "a =", a                                  # [-1, 1, 66.25, 333, 333, 1234.5]

# notice how del is a KEYWORD, not a function
del a[0]
print "\nafter del a[0]"
print "a =", a                                  # [1, 66.25, 333, 333, 1234.5]

del a[2:4]
print "\nafter del a[2:4]"
print "a =", a                                  # [1, 66.25, 1234.5]

del a[:]
print "\nafter del a[:]"
print "a =", a                                  # []

del a
print a                                         # NameError: name 'a' is not defined