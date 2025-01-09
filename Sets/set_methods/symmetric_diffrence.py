# symmetric_diffrence() : returns a new set containing items that are not similar to both the sets.
#                         "keeping all but not duplicates"
# symmetric_diffrence_update() : updates in existing set.
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
new_set = set1.symmetric_difference(set2)
print(new_set)
set1.symmetric_difference_update(set2)
print(set1)