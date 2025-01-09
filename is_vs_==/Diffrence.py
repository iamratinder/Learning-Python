'''
In Python, is and == are both comparison operators that can be used to check if two values are equal.

== operator -> compares the values of the objects        Will return True if the objects have the same value
is operator -> compares the identity of two objects      Will return True only if the objects being compared are the exact same object in the memory   '''

a = 4
b = "4"
print(a is b)  # False     # compares exact location of object in memory
print(a == b)  # False     # compares value          

l1 = [1, 3, 99] 
l2 = [1, 3, 99] 
print(l1 is l2)   # False   -> both are made diffrently in location (cz it is mutable) (as python knows in future they might be changed)
print(l1 == l2)   # True    -> As values in lists are same

a = 3
b = 3
print(a is b)  # True   -> both are actually pointing the same memory location (cz 3 is a constant) (and python knows value of 3 can't be changed so it will not waste extra memory for b)
print(a == b)  # True   -> As values are same

a = "ratinder"
b = "ratinder"
print(a is b)  # True   -> As strings are also immutable (so both are same objects)
print(a == b)  # True   -> As values are same

a = (2, 4, 6)
b = (2, 4, 6)
print(a is b)  # True   -> As tuples are also immutable (python iko memory location vch bnalu)
print(a == b)  # True   -> As values are same

a = None
b = None
print(a is b)       # True
print(a == b)       # True
print(a is None)    # True

# NOTE : for mutable objects  (like lists) -> is and == may return diffrent result
#        for immutable objects (like integers, strings, tuples) -> is and == will always return the same result