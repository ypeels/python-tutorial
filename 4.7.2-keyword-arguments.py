def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print "-- This parrot wouldn't", action,
    print "if you put", voltage, "volts through it."
    print "-- Lovely plumage, the", type
    print "-- It's", state, "!"
    print ""
        
        
voltage=99
parrot(1000)
parrot(voltage=voltage)                 # "99 volts" - keyword and value live in separate scopes!
parrot(action='die', voltage='123')     # order doesn't matter!
parrot(98, type='Jane Grey')            # mix and match, as long as keyword args are all at the end

#parrot(voltage=5, 'dead')              # SyntaxError: non-keyword arg after keyword arg
#parrot(100, voltage=100)               # TypeError: got multiple values for keyword argument 'voltage'
#parrot(actor='John Cleese')             # TypeError: got an unexpected keyword argument 'actor'


print "-" * 40
def cheeseshop(kind, *unnamed_arguments, **unnamed_keywords):
    print "-- Do you have any", kind, "?"
    print "-- I'm sorry, we're all out of", kind
    print "unnamed_arguments =", unnamed_arguments      # a tuple != a list... see section 5.3?
    for arg in unnamed_arguments:                       # as in ruby, *args allows a variable-length argument list
        print arg
    print "-" * 40
    keys = sorted(unnamed_keywords.keys())              # without calling sorted(), "the order in which the arguments are printed is undefined"
    for kw in keys:                                     # in addition, **keywords allows variable-length keywords
        print kw, ":", unnamed_keywords[kw]
        
cheeseshop(                                                         # n.b. line-continuation character NOT needed!?
    "Limburger",                                                    # not keyword 'kind', to allow non-trivial *unnamed_arguments
    "It's very runny, sir", "It's really very, VERY runny, sir",    # variable-length argument list 
    client = "John Cleese",
    sketch = "Cheese Shop Sketch",
    shopkeeper = "Michael Palin"
)

cheeseshop("bare minimum")