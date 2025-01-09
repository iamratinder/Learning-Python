# reduce : the reduce function is a higher-order function that applies a function to a sequence and returns a single value.
#          IT IS PART OF THE  " functools module " in python 
#          Syntax -> reduce(function, iterable)
#       -> The function argument is a function that takes in two arguments and returns a single value.
#       -> The iterable argument is a sequence of elements, such as list or tuple.

# NOTE : The reduce function applies the function to the first two elements in the iterable and then applies the function
#        to the result and the next element, and so on. The reduce function returns the final result.

from functools import reduce

numbers = [1, 2, 3, 4, 5]                                   # List of numbers
sum = reduce(lambda x, y : x + y, numbers)                  # Calculate the sum of numbers using reduce function
print("The sum of all elements in the list is :", sum)      # print the sum

'''
__Actual steps :
-> numbers = [1, 2, 3, 4, 5]
-> numbers = [3, 3, 4, 5]
-> numbers = [6, 4, 5]
-> numbers = [10, 5]
-> numbers = [15]           '''
