# The Enumerate function : is a built-in function in Python that allows you to loop over
#                          a suquence (such as a list, tuple, or string) and get the index 
#                          and value of each element in the sequence at the same time

# • It returns a tuple containing the index and value of each element in the sequence.
# • You can use the for loop to unpack these tuples and assign them to variables. 

list = ['apple', 'banana', 'mango', 'grapes', 'chiku', 99, True]
for some_variable in enumerate(list):
    print(some_variable)
print("\n"+'─'*70)


# Conventional metod :-
list = ['apple', 'banana', 'mango', 'grapes', 'chiku', 99, True]
index = 0
for item in list :
    print(item, end=' ~ ')
    if index == 2:
        print("Wow, Mango!", end=' ~ ')
    index += 1                                  
print("\n"+'─'*70)

# Using enumerate function :-
list = ['apple', 'banana', 'mango', 'grapes', 'chiku', 99, True]

for index, item in enumerate(list) :
    print(item, end=' ~ ')
    if index == 2:
        print("Wow, Mango!", end=' ~ ')
print("\n"+'─'*70)

for index, item in enumerate(list):
    print(index, item)
print("\n"+'─'*70)

               