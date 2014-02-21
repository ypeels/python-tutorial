print '''
Section 6.4: Packages
This is like nested namespaces that mirror the subdirectory structure.
There must be an __init__.py file in each subdir that is to be made available.

Section 6.4.1: Importing * From a Package
>>> from <package> import *
This does NOT import everything! (for performance?)
Instead, it ONLY import the packages defined by "__all__" in __init__.py

Section 6.4.2: Intra-package References
- the current package is automagically checked
- you can also explicitly import from "." or ".." relative to the current module

Section 6.4.3: Packages in Multiple Directories
- discusses the exotic package attribute "__path__ "...
'''