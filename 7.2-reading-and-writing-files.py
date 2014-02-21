# r: read-only
# w: write-only (creates file)
# r+: read and write (assumes file exists)
# default mode is 'r'; add the 'b' flag to prevent binary data corruption!
f = open('workfile.txt', 'w') 

#f.write('asdf\n')


# To read ALL the lines of a file 
# >>> list(f)       # converts f into a '\n'-delimited list. 
# >>> f.readlines()
#                   # Note that BOTH of these methods will scan f to EOF!


# f.tell() == current position in file [bytes from start]
# f.seek(offset, from_what)

f.close() # free system resources

# fine point: the "with" keyword is exception-safe, closing the file automatically when it falls out of scope.
# >>> with open('workfile', 'r') as f:
# ...     read_data = f.read()
# >>> f.closed
# True