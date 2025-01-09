#___1. Default Arguments :
def avg(a=2, b=3):          # if we don't give any value while calling than only it will take a=2 b=3
    print("The average is : ", (a+b)/2)

avg()         # average(2,3) = 2.5
avg(1,1)      # average(1,1) = 1.0
avg(5)        # average(5,3) = 4.0
avg(b=5)      # average(2,5) = 3.5
print()

#___2. Keyword Arguments : [aka kwargs]
# we can provide arguments with key=value, this way the interpreter recognizes the arguments by parameter name.
# Hence, the order in which the arguments are passed does not matter.
def name(fname, mname, lname):
    print("Hello", fname + mname, lname)

name(mname="deep", lname="Singh", fname="Ratinder")
print()

#___3. Required Arguments :
# In case we don't pass the arguments with a key=value syntax (in function), then it is necessary to pass the arguments :-
# -> in correct positional order 
# -> and number of arguments passed should match actual function definition.
def avg(a, b=3):          
    print("The average is : ", (a+b)/2)

# avg()         # average(2,3) = 2.5
avg(1,1)      # average(1,1) = 1.0       
avg(5)        # average(5,3) = 4.0       NOTE : Here, a has become the required argument
# avg(b=5)      # average(2,5) = 3.5
print()

#___4. Variable Length Arguments :
''' Sometimes we may need to pass more arguments than those defined in the actual function. 
This can be done using variable-length arguments.
There are two ways to achieve this :-

___1.Arbitary arguments : [aka *args]
--> While creating a function, pass a * before the parameter name while defining the function.
    The function accesses the arguments by processing them in the form of "Tuple".

___2.Keyword Arbitary arguments : [aka **kwargs]
--> While creating a function, pass a ** before the parameter name while defining the function.
    The function accesses the arguments by processing them in the foem of "Dictionary".'''
def average(*numbers):       # here, numbers is tuple
    print("Here in * type taken is : ",type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum/len(numbers)

result = average(5,6,7)    # You can give any amount of arguments -> they all will form a tuple(numbers)
print("The average of numbers is : ", result)
print()

def naam(**name):     # here, numbers is dictionary
    print("Here in ** type taken is : ",type(name))
    print("Hello,", name["fname"], name["mname"], name["lname"])

naam(mname = "deep", lname = "Singh", fname = "Ratinder")