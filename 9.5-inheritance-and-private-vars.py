class Base:
    def foo(self):
        return "Base.foo()"
    def call_foo(self):
        return self.foo()                   # will call derived class's foo() override
    def __bar(self):
        print "Base.__bar()"
    def call_base_bar_non_virtually(self):
        self.__bar()
    def __normal__(self):
        print "Base.__normal__"
    
    
    
class Derived(Base):
    def foo(self):
        return "Derived.foo()"
    def call_base_foo(self):
        return Base.foo(self)
    def __bar(self):
        print "Derived.__bar()"
        
class Perverse(Base):
    def _Base__bar(self):                   # forcibly override the auto-mangled Base.__bar()
        print "bwahaha"
        

d = Derived()
print "d.foo() =", d.foo()
print "d.call_foo() =", d.call_foo()
print "d.call_base_foo() =", d.call_base_foo()
print "d.__normal__(): ",
d.__normal__()                              # NOT mangled, because it has two TRAILING underscores

print "\nBut name mangling makes Base.__bar() SEEM non-virtual!"
print "d.__bar() will give AttributeError: Derived instance has no attribute '__bar'"
print "d._Derived__bar(): ",
d._Derived__bar()                           # "private"! must mangle name to call "Derived.__bar()"
print "call_base_bar_non_virtually(): ",
d.call_base_bar_non_virtually()

p = Perverse()
print "Perverse.call_base_bar_non_virtually():", 
p.call_base_bar_non_virtually()


print '''
Section 9.6: Private Variables and Class-local References
haha, there are no such things as private instance variables in python

But there IS name mangling, which is why call___bar did NOT use the override to __bar above!!

Here are the rules:
"Any identifier of the form __spam
- at least two leading underscores
- at most one trailing underscore (so that functions like __blah__ behave NORMALLY)
is textually replaced with _classname__spam, 
where classname is the current class name with leading underscore(s) stripped.

Not only does this make __spam() "private" (Class.__spam() does not exist!),
it makes it effectively non-virtual as well
...unless you are Perverse and override the mangled name...

"Note that the mangling rules are designed mostly to avoid accidents;
it still is possible to access or modify a variable that is considered private."

Note also that you couldn't have a method Class.__spam() even if you WANTED
- the automangler will get it
'''