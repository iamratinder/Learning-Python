# Sets : 
# 1. Unordered   NOTE : printed in random manner and cannot be accessed using index
# 2. store multiple items in a single variable.
# 3. enclosed within {}
# 4. Unchangeable  (cannot change after creation)
# 5. Sets do not contain  duplicate  items.  NOTE : True/1 and False/0 are considered 1 item
info = {"Carlo", 19, False, 5.9, 19, 1, True, 0}             # 19 is printed one time only (in output)
print(info)          

# Empty Set :
empty = {}  #❌ This is actually dictionary (cz dict also has curly braces)
print(type(empty))
empty_set = set()   #☑️ This will give us an empty set
print(type(empty_set) , empty_set)

# Set constructor :
this_set = set(("apple", 1, "cherry", True, None))   # NOTE : double round-brackets
print(this_set)

# Checking if item exist in a set :
info = {"Carlo", 19, False, 5.9, 19, 1, True, 0}
if "Carlo" in info:
    print("Carlo is present")
else:
    print("Carlo is absent")
