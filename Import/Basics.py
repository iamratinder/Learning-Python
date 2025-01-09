''' 1. Importing in python is the process of loading code from a Python module into the current script.
    2. This allows you to use the functions and variables defined in the module in your current script, as well as any additional modules that the imported module may depend on.
    3. TO import a module in python, you use the import statement followed by the name of the module.
    For eg. to import the math module, which contains a variety of mathematical functions, you would use the following statement :
    --->  import math                       
    4. Once a module is imported, you can use any of the functions and variables defined in the module by using the the dot notation.
    For eg. to use the sqrt function from the math module, you would write :
    --->  result = math.sqrt(n)  '''
import math
n = int(input("Enter a number : "))
res = math.sqrt(n)
print(f"The square-root of {n} is : {res}")
print(math.floor(4.56564))


