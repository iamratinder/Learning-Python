# You can also import specific function(s) or variable(s) from a module using from keyword.
# For eg. to import only the sqrt func from the math module, you would write :
from math import sqrt,pi
n = int(input("Enter the number : "))           
result = sqrt(n)                                   # now don't need to do math.
print(f"The square-root of {n} is {result}")
print(f"The area of the circle would be : {pi*n*n}")
