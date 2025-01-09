# 1. Lists are ordered collection of data items. (can store duplicates)
# 2. They store multiple items in a single variable.
# 3. List items are seperated by , and enclosed within [].
# 4. Lists are "changeable" meaning we can alter them after creation.
#__List Index : same as arrays (starts from 0 and goes to n-1)(where n is no. of items in list)
# NOTE : Index can be +ve or -ve {for -ve just assume to be length - no.}(as that in strings)

random = list(("oye",  3,    9,   True,  6.7))    # list can be made this way also using list()
random = ["oye",  3,    9,   True,  6.7]
#          [0]   [1]   [2]   [3]    [4]    -> +ve indexes
#          [-5]  [-4]  [-3]  [-2]   [-1]   -> ve indexes
#  for converting -ve to positive just do length - index
print(random)
print(random[0])
print(random[-3])

print(random[1:3])  # will print from index 1 to 2

# NOTE : Jump index :-
print(random[0:5:2])       # will print (starting from index 0 to 4) by jump of 2