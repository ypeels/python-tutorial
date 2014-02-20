print '''
range(start [default 0], stop [not inclusive], step [default 1])
In C terms:
for (int i = start; (step > 0 && i < stop) || (step < 0 && i > stop); i += step) 
    // generate array of all values of i
'''

print "range(n) returns the list [ 0, ..., n-1 ]. "
print "range(10) =", range(10) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print "range(5, 10) =", range(5, 10) # [5, 6, 7, 8, 9]
print "range(0, 10, 3) =", range(0, 10, 3) # [0, 3, 6, 9]
print "range(-10, -100, -30) =", range(-10, -100, -30) # [-10, -40, -70]

print '''
You can also use range() and len() for C-style indexing, but Tutorial recommends enumerate() instead...
>>> a = ['Mary', 'had', 'a', 'little', 'lamb']
>>> for i in range(len(a)):
...     print i, a[i]'''
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print i, a[i]

