# What if we do not want to iterate over a sequence?
# What if we want to use for loop for a specific number of times?
# Hence, we can use range() function
#____ The range function returns a sequence of numbers, 
#---> starting from 0 (by default),
#---> and increments by y 1 (by default),
#---> and ends at a specified number.
#____ Syntax : range(starting index, ending index, step/increment by) NOTE : starting index is inclusive(included)__ending index is exclusive(not included)  

for k in range(5):       # goes from 0 (by default) to 4 i.e. [0,5) on steps of 1 (by default)
    print(k)

print()           # for next line

for i in range(1,11):    # goes from 1 to 10 on step of 1 (by default)
    print(i) 

print()

j = 1
for i in range(1,11,2):                # goes from 1 to 10 on step of 2 
    print(str(j)+"number is : ", i)
    j+=1