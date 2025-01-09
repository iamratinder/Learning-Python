# Lambda function -> It is a small anonymous function without a name. It is defined using the lambda keyword
# Syntax :-                 
''' lambda argument1, argument2.... : expression to return '''
# 1. Lambda functions are often used in situations where a small function is required for a short period of time.
# 2. They are commonly used as arguments to higher-order functions, such as map, filter, and reduce.
# 3. Can have the multiple arguments, just like regular functions.

#__________________ Function to double the input 
# def double(x):
#     return x*2

#___________________ Lambda function to double the input
# lambda x : x*2

a = int(input("Enter the numver for cube : "))
double = lambda x : x**3
print(double(a))                         ; print("─"*40)

# eg. for lambda function passed as an argument :-
def random(fx, value):
    return 6 + fx(value)

print(random(lambda x : x**3, 3))

# passing more than 1 argument :-
x,y = int(input("Enter 1st number : ")), int(input("Enter 2nd number : "))
product = lambda x, y : print(f"The product of {x} and {y} is : {x*y}")
 
product(x, y)

