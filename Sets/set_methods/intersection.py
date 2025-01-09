# intersection() : returns a new set containing common elemeents of two/more sets.
# intersection_update() : updates the existing set with common values.
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
new_set = set1.intersection(set2)
print(new_set)
set1.intersection_update(set2)
print(set1)