# extend() : This method adds an entire list or any other collection database(set, tuple, dict) to the existing list.
colors = ["voilet", "indigo", "blue"]
rainbow = ["green", "Yellow", "orange", "red"]
colors.extend(rainbow)         # will add rainbow to the end of list 'colors'
print(colors)

# OR Concatenating two lists :-
colors = ["voilet", "indigo", "blue"]
rainbow = ["green", "Yellow", "orange", "red"]
new = colors + rainbow         # will make a new list 'new' and list 'colors' is not affected
print(new)

# another way : join by appending all items one by one :
colors = ["voilet", "indigo", "blue"]
rainbow = ["green", "Yellow", "orange", "red"]
for x in rainbow:
    colors.append(x)
print(colors)



