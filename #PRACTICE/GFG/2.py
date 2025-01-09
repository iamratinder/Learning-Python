# To swap two elements in list :
# 1.
list = [1, 2, 3, 4, 5, 6]
a, b = int(input("Enter first position to swap : ")), int(input("Enter second position to swap : "))
list[a-1], list[b-1] = list[b-1], list[a-1]
print(list)

# 2.
list = [1, 2, 3, 4, 5, 6]
a, b = int(input("Enter first position to swap : ")), int(input("Enter second position to swap : "))
# let a = 3, b = 4
element1 = list.pop(a-1)     # 1, 2, 4, 5, 6
element2 = list.pop(b-2)     # 1, 2, 5, 6
list.insert(a-1, element2)   # 1, 2, 4, 5, 6
list.insert(b-1, element1)   # 1, 2, 4, 3, 5, 6
print(list)

# 3. Store the element at pos1 and pos2 as a pair in a tuple variable, say get. Unpack those elements with pos2 and pos1 in that list. Now both positions are swapped

list = [1, 2, 3, 4, 5, 6]
a, b = int(input("Enter first position to swap : ")), int(input("Enter second position to swap : "))
pos1 = a-1
pos2 = b-1
get = list[pos1], list[pos2]   # stores (list[a-1], list[b-1])
list[pos2], list[pos1] = get   # unpacking the tuple
print(list)