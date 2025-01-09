# union() : returns a new set containing all items that are present in two/more sets.
# update() : adds items of one set to the other (thus returning all items but in existing set)
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = {6, 7, 8}
new_set = set1.union(set2, set3)
print(new_set, f"\nset1 and set2 are untouched :\n{set1}  {set2}")  ;print('─'*40)
set1.update(set2)       # values of set1 are updated as set1 + set2
print(set1, set2)