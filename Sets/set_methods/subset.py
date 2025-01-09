# issubset() : checks if all the items of the original set are present in particular set.
# returns true if all items are present, else returns False.
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set3 = {3, 4, 5, 6, 7, 8, 9, 10}
print(set1.issubset(set2))
print(set2.issubset(set3))