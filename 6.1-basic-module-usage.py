print '''
If you had a file named "fibo.py" in this directory, you could just type
>>> import fibo
and be done with it... but looks like module names cannot start with numbers...

This PARTICULAR INVOCATION would execute the statements in fibo.py EXACTLY ONCE.
'''
#import fibo
#import fibo

# http://stackoverflow.com/questions/67631/how-to-import-a-module-given-the-full-path
print '''
>>> import imp
>>> fibo = imp.load_source('giggity', '6.0-fibo-module.py')
*** Unlike "import fibo", this will execute the statements EVERY TIME. ***
'''
import imp
fibo = imp.load_source('giggity', '6.0-fibo-module.py') # Hello world from '6.0-fibo-module.py'
fibo = imp.load_source('giggity', '6.0-fibo-module.py') # Hello world from '6.0-fibo-module.pyc' [compiled?]
fibo = imp.load_source('giggity', '6.0-fibo-module.py') # Hello world from '6.0-fibo-module.pyc' [6.1.3: platform-independent byte-compiled!!]

print '''
And then you access the module's contents like a namespace, but using class syntax:
>>> fibo.fib(23)'''
fibo.fib(23)          # 1 1 2 3 5 8 13 21


print '''
The module's "scope name" is given by the special "member variable" __name__.
This is NOT necessarily the same name used for direct access,
but it IS the same name used for "from" importing!!
>>> fibo.__name__'''
print fibo.__name__                 # giggity
print "__name__ =", __name__        # __main__
print "giggity.fib(1000) would give NameError: name 'giggity' is not defined"


print '''
>>> from giggity import fib 
  - you can even "import *", which imports all names EXCEPT those beginning with underscore '_' (moar idiosyncracies)
    - bad practice for scripts
    - convenient for interactive sessions
'''
from giggity import fib             # NOT fibo!
print ">>> fib(100)"
fib(100)                            # 1 1 2 3 5 8 13 21 34 55 89


print '\n', '-' * 40, '\n'


print '''
Due to the following test, the enclosed code will not run if this file is imported:
if __name__ == "__main__":
'''
if __name__ == "__main__":          # wtf, can't use "is"?? see 5.7 - use "==" to reliably compare VALUES
    import sys
    print "sys.argv =", sys.argv    # argc doesn't exist, because you can just call len(sys.argv)
    
    # argv[1] exists and is an integer
    if sys.argv[1:2] != [] and sys.argv[1].isdigit():
        fib_max_from_argv = int(sys.argv[1])
        print "command line argv[1] =", fib_max_from_argv
        fib(fib_max_from_argv)
    else:
        print "Usage: python {0} <Fibonacci upper bound>".format(__file__)

        
print '''
Section 6.1.2: The Module Search Path
This is "sys.path".
'''



