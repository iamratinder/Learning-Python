# Python also allows you to rename imported modules using the  as  keyword.
# This can be useful if you want to use a shorter or more descriptive name for a module, or if you want to avoid naming conflicts with other modules or variables in your code.
import math as m
result = m.sqrt(9)
print(result)
print(m.pi)

from math import pi, sqrt as sq                 # here, sqrt is imported as sq
print(sq(4))
print(pi)