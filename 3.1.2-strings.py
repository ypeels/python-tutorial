# The string printing rules at the beginning of 3.1.2 only apply in INTERACTIVE mode??
# print "\n\n"
# print "Strings are printed as they would be typed with SINGLE QUOTES on the outside:"
# print 'asdf'		# 'asdf'
# print "asdf" 		# 'asdf'
# print '"asdf"'		# '"asdf"'
# print "\'asdf\'"		
# 
# '"asdf without print"'

print '\n\n'
print "long text with \n \
continuation lines\n\
	giggity - indentation is part of the string literal, not logic\n"
	
	
	
print """
	Or you can use matching triple quotes (single or double)\\
		and this prints a \"verbatim\" chunk of text 
	Too bad that Notepad++ doesn't pick up on this syntax for DOUBLE quotes...
	
"""


print r"Precede a string literal with 'r' to PRINT \n and \ but NOT ignore \
\
newline after the line continuation character. This is called a 'raw' string?\
"


print "\nConcatenate C-style or with '+' and repeat with '*'"
print "doe " 'a deer' # doe a deer
print "a female" + " deer" # a female deer
print 'd\'oh ' * 3 # d'oh d'oh d'oh
print ''



print '''
String indexing LOOKS like C at first...
But beware: there is no separate character type, just strings of unit length.
For the following, let word = 'HelpA'
'''
word = 'Help' + "A"
print 'word[4] =', word[4] 		# A

print '''
Also, such entities are READ-ONLY. For example:
>>> word[0] = "K"
TypeError: \'str\' object does not support item assignment
'''
#word[0] = "K"

print 'Substrings are NOT "MATLAB-like", but their second index APPEARS "off-by-one"'
print 'word[0:2] =', word[0:2] 	# He
print 'word[2:4] =', word[2:4]	# lp
print 'word[:2] =', word[:2]	# He [default first index = 0] - the first two characters
print 'word[2:] =', word[2:]	# lpA [default second index = length] - everything but the first two characters
print ''

print "Implicit graceful bounds-checking/'buffer-overflow handling' (SUBSTRINGS ONLY)"
print "word[1:100] =", word[1:100] 	# elpA
print "word[10:] =", word[10:]	   	# [empty string]
print "word[2:1] =", word[2:1]		# [empty string]
print "word[5] = IndexError: string index out of range"#, word[5]
print ''

print '''
And indices can go NEGATIVE... count BACK from word[-1], the last char.
'''
print "word[-6] = IndexError: string index out of range"#, word[-6]
print "word[-1] =", word[-1] 	# A
print "word[-4:-2]=",word[-4:-2]# el
print "word[-2:] =", word[-2:]	# pA - the last 2 characters
print "word[:-2] =", word[:-2]	# Hel - everything but the last 2 characters
print "word[-5:] =", word[-5:] 	# HelpA
print "word[-9:] =", word[-9:]	# HelpA
print "word[1:-2] =", word[1:-2]# el <======= they glossed over this until Section 3.1.4




print '''
Unifying principle: 'slice-notation'
 +---+---+---+---+---+
 | H | e | l | p | A |
 +---+---+---+---+---+
 0   1   2   3   4   5
-5  -4  -3  -2  -1

In other words, given
- L := len(word)
- -L <= a < b < 0
- A := a + L (or "a mod L")
- B := b + L
- 0 <= C < D

the following are non-trivial strings:
- word[a:b]
- word[a:C] for A < C
- word[a:D] for A < D
- word[C:b] for C < B
- etc.

Notice word[i] = word[i:i+1] for all i EXCEPT -1, which is "pathological"
Also, len(word[i:j]) = j-i mod L, which is probably the REAL motivation for this system.
'''
print "len(word[-4:-2]) =", len(word[-4:-2]) # 2


