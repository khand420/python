# Packages:-
# for larger collections of code, it is usally desirable to organize module into a hierarchy

# While importing packages, Python looks in the list of directories defined in sys.path, similar as for module search path.


import sys
print(sys.path)



# ------Module vs Packages------
# Modules are easy contains a single file
# Package are hard to manage as multiple related files
# Package Issue:
#    *Code organization
#    *Connections between submodules
#    *Desired usage
# It can get realy messy