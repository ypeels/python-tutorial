print '''
As in C, break and continue operate on the smallest enclosing for() or while() loop.
The new twist is the ELSE clause on loops:
- executed when a loop is TERMINATED NORMALLY (i.e., not by break)'''

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print n, 'equals', x, '*', n/x
            break
    else:                                                                   # loop-else!!
        # loop terminated normally - i.e., n is not divisible by any x < n
        print n, 'is prime'

print ''
for num in range(2, 10):
    if num % 2 == 0:
        print num, "is even"
        continue
        print "never get here"
    print num, "is odd"