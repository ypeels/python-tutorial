x = int(raw_input("Please enter an integer: "))
if x < 0:
    x = 0
    print 'Negative changed to zero'
elif x == 0:                                # think C preprocessor
    print 'Zero'
elif x == 1:
    print 'Single'
else:
    print 'More'

    
# this is what they mean by "'elif'... is useful to avoid excessive indentation"
# root cause: cannot have "else:" and "if...:" on the same line
x = int(raw_input("Please enter an integer: "))
if x < 0:
    print 'negative'
else: 
    if x == 0:
        print 'Zero'
    else: 
        if x == 1:
            print 'single'
        else:
            print 'more'
            
    