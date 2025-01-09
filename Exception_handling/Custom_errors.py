# Raising Custom errors : We can raise custom errors in python using  'raise'  keyword.
salary = int(input("Enter salary bw 2000 and 5000 : "))
if not 2000 < salary < 5000 :
    raise ValueError("Not a valid salary !!!")

# Sometimes, we may need to create our own custom exceptions that serve our purpose.

# Defining Custom Exceptions : In python, we can define custom exceptions by creating
#                              a new class that is derived from the built-in Exception class.

# Syntax :
class CustomError(Exception):
    # code.....
    pass
try :
    pass # code...
except CustomError:
    pass # code...

'''
This is useful bcz sometimes we might want to do something when a particular exception is raised.
For eg. sending an error report to the admin, calling an api etc. '''