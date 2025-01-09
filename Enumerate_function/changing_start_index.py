# By default, the enumerate function starts the index at 0, but you can specify a diffrent starting index by passing it as an argument to it

list = ['apple', 'banana', 'mango', 'grapes', 'chiku', 99, True]
for index, item in enumerate(list, start = 2):
    print(index, item)                              # NOTE : e;ements will be starting from 0th index itself, only mapping with index has changed

'''
The enumverate function is often used when you need to loop over a sequence and perform some action
with both the index and value of each element. 
For eg. you might use it to loop over a list of strings and print the index and value of each string in a formatted way :- '''
print('─'*70)

fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits) :
    print(f"{index + 1} -> {fruit}")
