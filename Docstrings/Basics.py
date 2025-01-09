# Python docstrings are the string literals that appear right JUST AFTER the definition of a function, method, class, or module.
def square(n):
    '''Takes in a number 'n' and returns the n²'''     # Docstring (NOTE : must be right after the definition)
    print(n**2)
square(int(input("Enter a number : ")))
print(square.__doc__)

# Diffrence between coments and Docstring :
# 1. comments are igmnored while docstrings are stored in  .__doc__ attribute.
# 2. changing comments do not affect program, whereas changing docstring may change the program.
# __comments : These are descroiptions that help programmers better understand the intent and functionality of program.
# __docstring : These are used to document our code. We can access these docstrings using the doc attribute.
# __doc attribute : Whenever string literals are present just after the definition of func, module, class or method,
#                   they are associated with the object as their  doc  attribute. We can later use this attribute to retrieve this docstring.

