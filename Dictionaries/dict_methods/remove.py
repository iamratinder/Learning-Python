# clear() : removes all the items.   empty dict is created -> {}
print('─'*50)
info = {"name": "Ratinder", "age": 18, "eligible": True}
info.clear()
print(info)                     ;print('─'*50)

# pop() : removes the key-value pair whose key is passed as parameter.
info = {"name": "Ratinder", "age": 18, "eligible": True}
info.pop("eligible")
print(info)                     ;print('─'*50)

# popitem() : removes the last key-value pair from the dictionary.
info = {"name": "Ratinder", "age": 18, "eligible": True}
info.popitem()
print(info)                     ;print('─'*50)

# del : del keyword to remove a dictionary item. NOTE : if key not provided, then it will delete the dict entirely.
info = {"name": "Ratinder", "age": 18, "eligible": True}
del info["age"]
print(info)
del info                        ;print('─'*50)
# print(info) -> will give an error bcz we have deleted info dictionary.