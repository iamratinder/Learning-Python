# issuperset() : checks if all the items of a particular set are present in the original set.
# returns True if all items are present, else returns False.
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set3 = {3, 4, 5, 6, 7, 8, 9, 10}
print(set1.issuperset(set2))
print(set3.issuperset(set2))
