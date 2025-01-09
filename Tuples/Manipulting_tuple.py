'''Tuples are immutable, hence if you want to add, remove or change tuple items, 
___First you must convert the tuple to a list.
___All list methods can be used for manipulation now
___Than perform operation on that list and convert it back to tuple. '''
print('─'*60)
num = (1, 5, 99, 23)
temp = list(num)
temp.append(100)       # add item
temp.pop(0)            # remove item
temp[2] = "HEHEHE"     # change item
num = tuple(temp)
print(num)                      ; print('─'*60)

# But, we can directly concatenate two tuples without converting them to list  :
tup1 = ("Spain", "India", 99, True)
tup2 = ("Yo", 56, "Bonjour", None)
new_tup = tup1 + tup2
print(new_tup)                  ; print('─'*60)