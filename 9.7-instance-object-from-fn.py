# Section 9.7: Odds and Ends

class C:
    def foo(self):
        return "My title is " + self.title
    def __init__(self, title):
        self.title = title

c = C("c")
d = C("d")
f = c.foo
print "f.im_self.title =", f.im_self.title      # myTitle. ["secret attribute" im_self yields method object's instance object]
print "f.im_func(d) =", f.im_func(d)            # My title is d ["secret attribute" im_func yields method object's function object]

# remember, method object = (instance object, function object)
# in the example above,
# - method object = f
# - instance object = c
# - function object = C.foo