# As tuple is immutable, hence has limited built-in methods.
# count() : returns no. of times the given element appears in tuple.
tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res = tuple1.count(3)
print("Count of 3 in tuple1 is :",res)
