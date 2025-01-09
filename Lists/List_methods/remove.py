# remove() : Removes the first occurance of the item
lst = ["apple", "banana", "cherry", "banana", "kiwi"]
lst.remove("banana")
print(lst)

# pop() : Remove specified index
lst = ["apple", "banana", "cherry"]
lst.pop(1)                         
print(lst)
# NOTE : If you do not specify the index, pop() method removes the last item.
lst = ["apple", "banana", "cherry"]
lst.pop()                         
print(lst)

# del keyword also removes the specified index : 
lst = ["apple", "banana", "cherry"]
del lst[0]                        
print(lst)
# NOTE : del can also delete the list completely :-
del lst 

# clear() : empties the list, the list still remains, but it has no content.
lst = ["apple", "banana", "cherry"]
lst.clear()                         
print(lst)
