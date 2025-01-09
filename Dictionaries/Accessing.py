# 1. Accessing single values :-
# -> Values in a dict can be accessed using keys. 
# •  By mentioning keys either in square brakets   NOTE : would raise error if key not found
# •  By using get() method                         NOTE : would print None if key not found

dict = {"name": "Ratinder", "age": 18, "eligible": True, 567: "employee1", 568: "employee2"}
print(dict["name"])
print(dict.get("name"))
print(dict.get("name2"))       ; print('─'*60)

# 2. Accessing multiple keys/values : use key() and value() method respectively.
print(dict.keys())
print(dict.values())           ; print('─'*60)

# Also we can iterate using for loop :
for key in dict.keys() :
    print(key)
print()
for value in dict.values() :
    print(value)
print('─'*60)              

for key in dict.keys() :
    print(f"The value corresponding to key {key} is : {dict[key]} ")
print('─'*60)

# Accessing key-value pairs : using items() method.
print(dict.items())            ;print('─'*60)
 
for key,value in dict.items():               #// Unpacking the tupple
    print(f"The value corresponding to key {key} is : {value} ")
print('─'*60)