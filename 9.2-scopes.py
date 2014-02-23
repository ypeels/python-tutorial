print '''
Section 9.2: Python Scopes and Namespaces
'''

global g_i # this has no effect on more INNER scopes!
g_i = 1
j = 2
g_k = 3



def status_report(description, i, j, k):
    print description
    print "g_i =", i
    print "j =", j
    print "g_k =", k
    i = i + 1
    print '' 

# must pass current scope's g_i, else status_report ALWAYS refers module-scope, not calling function's scope
status_report("before foo() executes", g_i, j, g_k) 
    
#print "before foo() executes"
#print "g_i({}) = {}".format(id(g_i), g_i)
#print "j({}) = {}".format(id(j), j)
#print "g_k =", g_k
#print ''

def foo():
    
    # this actually throws UnboundLocalError if ANY local variables named g_i, j, or g_k are instantiated!!
    # "local variable referenced before assignment"
    # this is basically because Python is smart enough to see a potential name conflict with a local variable.
    #status_report("after foo() was called but before it executes", g_i, j, g_k) 
    
    
    # illegal! basically, LHS declares local variable g_i, and RHS tries to reference it immediately.
    # UnboundLocalError: local variable 'g_i' referenced before assignment
    # Python is smart enough to see when you are trying to use an uninitialized variable!
    #g_i = g_i + 1 
    
    #j = j + 1
    # declares g_i "extern"
    # global variables are always accessible as read-only, but require "extern" to be writeable
    global g_i
    print "ONLY g_i is declared 'global'"
    
    g_i = 9
    j = 10
    g_k = 11
    
    status_report("after foo() executes but before it returns", g_i, j, g_k) 
    #print "after foo() executes but before it returns"
    #print "g_i({}) = {}".format(id(g_i), g_i)
    #print "j({}) = {}".format(id(j), j)
    #print "g_k =", g_k
    #print ''
    
foo()
    
status_report("after foo() executes and returns", g_i, j, g_k) 

print '''
Takeaway lessons
- id() only tells you the id of the OBJECT to which a variable name is bound...
    in this case, the integers 1 and 2
- <name> = expression(<name>) does NOT work, even though 
- Python interpreter catches many common errors
    - uninitialized variables
    - certain name conflicts
- "global" (extern-write) declaration must be made at WRITE-scope

'''