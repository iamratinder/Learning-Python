# List comprehension offers a shorter syntax when you want to create a new list based on values of an existing list.
# List comprehensions are used for creating new lists from other iterables like :
# lists, tuples, dictionaries, sets, and even in arrays and strings.
''' Syntax --> list = [Expression(items) for item in iterable if condition]
Expression : It is the item which is being iterated.
Iterable   : It can be list, tuples, dictionaries, sets, and even in arrays and strings.
Condition  : Condition checks if the item should ve added to the new list or not.  '''
lst = [i for i in range(7)]     # a list will be made of [0, 1, 2, 3, 4, 5, 6]
print(lst)

lst2 = [i*i for i in range(7)]  # here i*i is an expression for each element being listed 
print(lst2)

lst3 = [i for i in range(7) if i%2==0]  # with condition (i is even)
print(lst3)

'''Some more crazzy examples :- '''
# Accepts items with the small letter "o" in the new list :-
names = ['Milo', 'Sarah', 'Bruno', 'Anastasia', 'Rosa']
new_lst = [item for item in names if 'o' in item]
print(new_lst)

# Accepts items which have more than 4 letters :-
names = ['Milo', 'Sarah', 'Bruno', 'Anastasia', 'Rosa']
new_lst2 = [item for item in names if (len(item) > 4)]
print(new_lst2)
