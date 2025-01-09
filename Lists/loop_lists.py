# Loop through a list :
lst = ["cherry", 2, "apple", True]
for x in lst:
    print(x)
print('─' * 20)

# Loop through the Index numbers :
for i in range(len(lst)):   # loop through the list items by referring to their index number
    print(lst[i])           # i here varies from '0' to 'length-1' index
print('─' * 20)

# Using while loop :
i = 0
while i < len(lst):
    print(lst[i])
    i+=1
print('─' * 20)

# Loop using list comprehension : offers shortest syntax for looping through lists 
lst2 = ["oye", "wow", 99, None]
[print(x) for x in lst2]
