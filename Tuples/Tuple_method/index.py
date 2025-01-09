# index() : returns the index of first occurance of the given element
# NOTE : This method raises a ValueError if the element is not present.
print('─'*20)
tuple1 = (0, 99, 40, 1, 2, 3, 2, 3, 1, 3, 2)
res = tuple1.index(3)
print("The first occurance of 3 is (in terms of index):",res)

print('─'*20)
# if we find to search a particular element in some portion of tuple :
tuple2 = (0, 99, 4, 13, 24, 2, 90, 13, 100)
res = tuple2.index(13, 4, 9)        # would search for 13 after slicing the tuple 4:9(i.e = 24, 2, 90, 13, 100)
print(res)
print('─'*20)
