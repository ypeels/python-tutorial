print "\n\n"
print "I fiddled with argument lists (Section 4.7.3) in my notes for 4.7.2"

args = [3,6]
print "args =", args
print ""

print ">>> range(args[0], args[1])"
print range(args[0], args[1]) # [3, 4, 5]
print ""

print ">>> range(*args) # equivalently, unpack arguments out of a list or tuple"
print range(*args) # [3, 4, 5]
print ""

print "Similarly, dictionaries! (which are like Ruby hashes)"
dict = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM", "extra": "giggity"}
def parrot(voltage, state='a stiff', action='voom', **keywords):
    print "-- This parrot wouldn't", action,
    print "if you put", voltage, "volts through it.",
    print "E's", state, "!"
    for kw in keywords.keys()  :
        print kw, ":", keywords[kw]
        
parrot(**dict)