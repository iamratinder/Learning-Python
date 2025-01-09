# del is not a method, rather it is a keyword which deletes the set entirely.
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
del cities
# print(cities)  # will give a NmeError as we have deleted the entire set

# clear() : clears(delete) all items(not the entire set itself) in the set and prints the empty set. 
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.clear()
print(cities)