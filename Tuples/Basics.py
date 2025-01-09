# Tuples are used to store multiple items in a single variable. written in ()
# It is Ordered and UNCHANGEABLE.
'''  Same slicing, printing elements using index, jump index, range etc.. is same as that in lists  
But NOTE - After slicing or any change a new tuple is returned (as tuples are unchangeable) '''
print('─'*40)
tup = (1, 3, 9)
print(type(tup), tup)              ; print('─'*40)

tup2 = (3)                # will be considered simply an integer(of name tup2) enclosed within braces
print(type(tup2), tup2)            ; print('─'*40)

tup3 = (3,)               # NOTE : if you wanna put 1 element in tupple than put , also to make it tupple
print(type(tup3), tup3)            ; print('─'*40)

# Checking :
tup2 = ("Ratinder", 99, True, 5, 6)
if 99 in tup2:
    print("Yes 99 is present in tup2")       ; print('─'*40)