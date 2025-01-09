'''
In Python, the map,filter,and reduce func are built-in functions(higher order i.e. they take functions as their arguments) that allow you to apply
a function to a sequence of elements and return a new sequence.
These functions are known as  Higher-order functions, as they take other functions as arguments. '''
# map : The map function applies a function to each element in a sequence and returns a new sequence containing the transformed elements.
#       Syntax -> map(function, iterable)
#    -> The function argument is a function that is applied to each element in the iterable argument.
#    -> The iterable argument can be list, tuple, or any other iterable object.

def cube(n):
    return n*n*n
numbers = [1, 2, 3, 4, 5]
new_list = list(map(cube, numbers))  # need to typecast bcz map returns map object
print(new_list)

numbers = [1, 2, 3, 4, 5]                  # list of numbers
doubled = map(lambda x : x*2, numbers)     # Double each number using the map function
print(list(doubled))                       # print the doubled numbers