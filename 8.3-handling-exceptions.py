# unhandled exceptions are like implicit early returns...
def foo(x):
    print "\nfoo({})".format(x)
    try:
        try:
            y = 1 / x
        except IOError: # can take a tuple "except (IOError, ValueError):", or declare exception variable "except IOError as e:"
            print "level 2 IOError, as if"
        print "the line after the level 3 try/except"   # never executed when x == 0
    except ValueError:
        print "level 2 ValueError, as if"
    except: 
        print "exception in foo; rethrowing"
        raise                                           # "rethrow" the exception (iirc). you can also "raise IOError(args)", etc.
    else:
        print "the else clause is executed if no exceptions are thrown"
                                                        # blank lines are ignored
    finally:
        print "Section 8.6: finally"
        print "\tthe finally clause, however, is ALWAYS executed"
        print "\tahh, so THAT'S what an else clause is for - to execute BEFORE finally."

    print "the line after the level 2 try/except"       # never executed when x == 0
    


try:
    foo(1)
    foo(0)
    foo(-1)                                             # never gets called    
except ZeroDivisionError:
    print "divided by zero! tsk tsk"
print "the line after the level 1 try/except"



print '''
Section 8.7: Predefined Clean-up Actions

As mentioned in Section 7.2, the "with" statement automagically cleans up 
"objects like files" when they "fall out of scope"

For example:
with open("myfile.txt") as f:
    for line in f:
        print line,
'''