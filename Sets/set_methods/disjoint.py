# isdisjoint() : checks if items of given set are present in another set.
# This method returns False if items are present, else it returns True.
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set3 = {1, 3, 9, 0, 11}
print(set1.isdisjoint(set2))
print(set2.isdisjoint(set3))
