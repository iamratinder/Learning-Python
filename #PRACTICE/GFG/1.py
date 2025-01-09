# WAP to interchange first and last elements in a list :
# 1.
lst = [1, 2, 3, 4, 5, 6]
temp = lst[len(lst)-1]
lst[len(lst)-1] = lst[0]
lst[0] = temp
print(lst)

# 2.
lst = [1, 2, 3, 4, 5, 6]
lst[0], lst[len(lst)-1] = lst[len(lst)-1], lst[0]
print(lst)

# 3.
lst = [1, 2, 3, 4, 5, 6]
lst[0], lst[-1] = lst[-1], lst[0]
print(lst)