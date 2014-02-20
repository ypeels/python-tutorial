# Measure some strings:
words = ['cat', 'window', 'defenestrate']
for w in words:                             # so it's basically a "foreach"
    print w, len(w)
    
print '\nTo modify a list, loop over a COPY'
#for w in words: # infinite loop if insert() is ever invoked
for w in words[:]: # loops over a slice copy of the entire list
    if len(w) > 6:
        words.insert(0, w)
print words