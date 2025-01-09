# String formatting in Python : using format method
'''
format() : used to combine diffrent data types with strings
The format method takes the passed arguments, formats them, 
and places them in the string where the placeholders {} are '''
# NOTE : 1. format() method takes unlimited no. of arguments
#        2. arguments are placed into respective placeholders {}
#        3. we can use indexes {0} to be sure the arguments are placed in correct placeholders 
print('─'*60)
age = 18
quantity = 3
item = True
# price = 49.99605494       If you want to use .3f(round off to 3 decimal places) than we have to give price value in function itself(keyword argument)
txt = '''My name is Ratinderdeep Singh, I am {} years old
I want {} pieces of {} items, for {price:.3f} dollars.'''
print(txt.format(age, quantity, item, price=39.99325))       ; print('─'*60)

age = 18
quantity = 9
txt2 = '''I am {1} years old, and I want {0} items yeah!!!!'''
print(txt2.format(quantity, age))                   ; print('─'*60)