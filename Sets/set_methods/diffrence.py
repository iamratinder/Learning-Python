# diffrence() : prints only items that are only present in the original set and not in both sets.
# diffrence_update() : updates items to a existing set.
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
new_set = set1.difference(set2)   # kind of A - B (where A and B are sets)
print(new_set)
set1.difference_update(set2)
print(set1)