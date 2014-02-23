class MyClass:
    '''MyClass' (optional) docstring'''
    i = 0                               # class variable ("static member variable" in C++)
    def __init__(this):                 # constructor (can add arguments... see 4.7.1). you can also specify the (dummy) name of "self" or "this"
        this.i = 99                     # instance variable ("member variable" in C++)
        MyClass.i = MyClass.i + 1
        
    def status_report(self, name):
        #print i # NameError: global name 'i' is not defined. class variable NOT visible??
        print "self.i =", self.i, ", MyClass.i =", MyClass.i, "from", name
                                        # 9.4: "no shorthand for referencing data attributes from within methods"

x = MyClass()
x.status_report('x after instantiating x')
y = MyClass()
x.status_report('x after instantiating x and y')
y.status_report('y after instantiating x and y')
x.i = 1
MyClass.i = -1                          # MyClass is an object too
x.status_report('x after "x.i = 1" and "MyClass.i = -1"')
y.status_report('y after "x.i = 1" and "MyClass.i = -1"')


# Section 9.3.3: Instance Objects
x.j = 2                                 # you can ADD data attributes on the fly!




xsr = x.status_report                   # a method object, not a function object.
xsr("xsr")                              # implicit first argument is the class instance, x
#xsr(y, "xsr + y")                      # can't override that implicit argument, either.
MyClass.status_report(x, "MyClass")     # equivalent way of calling as a "class method". see also @staticmethod


print '''
Section 9.4 Random Remarks
- my impression of Python's all-public, modifiable classes: dangerous...
'''