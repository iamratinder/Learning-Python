# Finding length of list :
# 1.
list = [1, 2, 3, 4, 5, 6]
print(len(list))

# 2.
list = [1, 2, 3, 4, 5, 6]
count = 0
for i in list:
    count+=1
print(count)

# 3. This technique is lesser known  (defined in operator class)
from operator import length_hint
list = [1, 2, 3, 4, 5, 6]
print(length_hint(list))

# 4. -> using sum() function 
list = [1, 2, 3, 4, 5, 6]
length = sum(1 for i in list)
print(length)

# 5. -> use enumerate function
list = [1, 2, 3, 4, 5, 6]
for i, a in enumerate(list):
    sum = i+1                # bcz i is index
print(sum)

