# list.sort() : sorts the list in ascending order. NOTE - The original list is updated
#___For descending order : list.sort(reverse=true)  {As by default reverse parameter is set to false}
colors = ["voilet", "2", "indigo", "blue", "green"]
colors.sort()
print(colors)               # sorts alphanumerically
colors.sort(reverse=True)   # would print in descending order
print(colors)                     ;print('─' * 40)

num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.sort()
print(num)
num.sort(reverse=True)
print(num)                       ;print('─' * 40)

# Customize sort function : can be customize using keyword arguments (key=function)
#                           The function will return a number that will be used to sort list(the lowest no. first)
'''Sort the list based on how close the number is to 50 ? '''
def func(n):
    return abs(n - 50)   # kind of mod | |   returns +ve value

lst = [100, 50, 65.5, -82, 23]
lst.sort(key = func)
print(lst)                       ;print('─'*40)

# Case Insensitive Sort :-
 
# By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters :
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

## Luckily we can use built-in functions as key functions when sorting a list.
### So if you want a case-insensitive sort function, use str.lower as key function :
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)
