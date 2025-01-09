# remove() / discard() : to remove items from a given set.
# The main diffrence bw both of them is that if we try to delete an item which is not present :
# __remove() raises an error (yani code us line ton agge run nhi kru), whereas discard() do not.
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.discard("Tokyo")
print(cities)
cities.discard("Samana")
print(cities)

# pop() : removes the last item of set BUT the catch is that we don't know which item
#         gets popped as sets are unordered. However, you can access the popped item 
#         if you assign the pop() method toa variable.
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
popped_item = cities.pop()
print(cities)
print("The popped item was :", popped_item)