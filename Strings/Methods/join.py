# .join() : takes all the items in an iterable and joins them into one string.
#           A string must be specified as the seperator.

list = ["ratinder", '56', "hello", 'True']  # all items must be string
new_string = "~".join(list)
print(new_string)

list2 = ["hello", "Ratinder ", "how", "are", "you"]
new_string2 = "".join(list2)
print(new_string2)

# NOTE: While using a dictionary as an iterable, the returned values are the keys, not the values