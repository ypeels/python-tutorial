print "\n\n"

# 4.7.1
def f(a, L=[], b=0): # like C, default-valued arguments must be at the end of the function declaration
    L.append(a)
    print "b =", b, ", L =", L
    b = b + 1
    return L
print '''
Default argument values for MUTABLE objects (like lists) behave like static variables!! Even if returned!!!
They are assigned ONLY ONCE.

BUT!!! Default argument values for non-mutable objects (like scalars) are assigned ON EVERY INVOCATION!!

This is all a corollary of the fact that
- scalars are passed by value, but
- lists are passed by reference

Basically, if you EVER call f with default argument for L, it will instantiate a static variable L local to f.
'''

list = f(1)     # [1]
list.append(-1) # [1, -1]
f(2)            # [1, -1, 2]
f(3)            # [1, -1, 2, 3]
f(4, list)      # [1, -1, 2, 3, 4]
f(5)            # [1, -1, 2, 3, 4, 5]
print list      # [1, -1, 2, 3, 4, 5]

list2=f(0,[-9]) # [-9, 0]
f(6)            # [1, -1, 2, 3, 4, 5, 6]
f(1, list2)     # [-9, 0, 1]

print "\n\n"
    
    

def fNone(a, L=None):                       # This kludge works because None == NULL is a scalar...
    if L is None:                          
        print "L is None - on every call?"
        L = []
    L.append(a)
    print L
    #return L
    
fNone(1)
fNone(2)
fNone(3)
    