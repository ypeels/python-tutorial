print '\n\n'

print u'Hello\u0020World - with escape code \\uXXXX, XXXX in hexadecimal\n'

print ur'Raw Unicode mode, which applies escape codes only for odd number of backslashes' \
'\u0020\\u0020 - supposedly useful when you have lots of backslashes, e.g., for regular expressions'

print "See Section 3.1.3 for other ways to generate Unicode strings"

print 'Implicit in this section is how to escape ASCII characters as \\xYY, YY hexadecimal'
print '"Hello\\x20World" = "Hello\x20World"'