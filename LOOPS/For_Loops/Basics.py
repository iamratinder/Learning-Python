# for loops can iterate over a sequence of ITERABLE OBJECTS in python.
# Iterating over a sequence is nothing but iterating over -> strings, lists, tuples, sets etc...
#   string lyi -> iterate over every character
#   list lyi -> will iterate over every element of list
#   And so on.........

#__1. Iterating over a string :
  
name = "Hello"
for i in name:                     # loop will run for every character in string, 'i' is some variable in which the characters are getting stored in every iteration
    print(i, end=',')
print("*")                         # eh print islyi laya kyoki LOOP TON BAAD INTERPRETER AGLI LINE TE NHI AANDA,, tn jdo oh loop ton bahr aau tn use line vch ik * print krke fr next line ton niche ditta loop shuru kru

#__2. Iteration over a list :
    
colours = ["Red", "Green", "Blue", "Yellow"]
for colour in colours:
    print(colour)
print()                           # to give a spce (new line gap) before executing the below loop

#__3. Nested loops :
    
colours = ["Red", "Green", "Blue", "Yellow"]
for colour in colours:
    print(colour)
    for i in colour:
        print(i)
