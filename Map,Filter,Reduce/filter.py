# filter : The filter function filters a sequence of elements based on a given predicate(a function that returns a boolean value)
#          and returns a new sequence containing only the elements that meet the predicate. 
#          Syntax -> filter(predicate, iterable)
#       -> The predicate argument is a function that returns a boolean value and is applied to each element in the iterable argument.
#       -> The iterable argument can be a list, tuple, or any other iterable object.
# IN SHORT : jehdia values filter func vch true return krn gia oh aa jan gia te baki nahi

def filter_function(a):
    return a>2

numbers = [1, 2, 3, 4, 5]
newl = list(filter(filter_function, numbers))
print(newl)

numbers = [1, 2, 3, 4, 5]                         # List of numbers
evens = filter(lambda x : x % 2 == 0, numbers)    # Get only the even no. using filter function
print(list(evens))                                # print the even numbers
