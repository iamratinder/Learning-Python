# add() : If you want to add a single item to the set.
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.add("Helsinki")
print(cities)

'''
add more than 1 items, simply create 
another set (or any other iterable object like list, tuple, dict),
and use the update() method to add it into the existing set. '''
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
to_add = {"Delhi", "Mumbai", "Samana"}
cities.update(to_add)
print(cities)

