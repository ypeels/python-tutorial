def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""         # <==== docstring, which can be parsed by documentation generators
    a, b = 0, 1
    while a < n:
        print a,
        a, b = b, a+b
    print ''
    n = -1

# Now call the function we just defined:
nInput = 2000
fib(nInput)
print 'After fib(nInput), nInput =', nInput

print '''
Side notes:
- all variable assignments in a function store the value in the local symbol table
- all variable references [reads?] first look in the local symbol table, then in the local symbol tables of enclosing functions, then in the global symbol table, and finally in the table of built-in names
- Thus, global variables cannot be directly assigned a value within a function (unless named in a global statement), although they may be referenced.
'''


print '''
wtf does this sentence mean??
The actual parameters (arguments) to a function call are introduced in the local symbol table of the called function when it is called; thus, arguments are passed using call by value (where the value is always an object reference, not the value of the object).
'''

def foo(list):
    for i in list:
        print i,
    print ''
    #list.append('haha')         # modifies argument by reference - cf. Section 4.7.1
    #list = list + ['haha']     # why does this NOT modify argument by reference??
    list[len(list):] = ['haha2'] # this works, though?
    #print len(list)
    #return list

myList = [1, 'asdf']
foo(myList)
foo(myList)

print '''
Uh.... empirically, it looks like arguments are passed by value, unless explicitly passed as mutable??
Well, lists are passed by reference, but NOT ALL OPERATIONS are "remembered"?
'''

print '''function pointers are virtually transparent.
fib =''', fib
print '''\
>>> f = fib
>>> f(100)'''
f = fib
f(100)

