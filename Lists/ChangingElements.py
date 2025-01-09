# Change item value :
lst = ["apple", "banana", "cherry"]
lst[0] = "pumpkin"
print(lst)

# Change a Range of item values :
lst = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
lst[1:3] = ["blackcurrant", "watermelon"]
print(lst)

# NOTE : The length of list will change when the no. of items inserted does not match the no. of items replaced
#__If you insert more items than you replace :
lst = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
lst[1:2] = ["blackcurrant", "watermelon"]
print(lst)

#__If you insert less items than you replace :
lst = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
lst[1:3] = ["watermelon"]
print(lst)


