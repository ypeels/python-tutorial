print '''
Chapters 10 and 11 cover the Standard Library.
They are probably too cursory to take detailed notes on...
Here are my "highlights"/"tidbits".
'''

print '''
Section 10.1: Operating System Interface
>>> import os       # for platform-dependent API
>>> import shutil   # for "daily file and directory management tasks" (SHell UTILities)
'''

print '''
Section 10.4: Error Output Redirection and Program Termination
- The most direct way to terminate a script is "sys.exit()"
'''

print '''
Section 10.11: Quality Control
- import doctest
- doctest.testmod() # run tests and checks vs answers EMBEDDED IN DOCSTRINGS!!!