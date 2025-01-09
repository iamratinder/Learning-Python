# Finding String length :
st = input("Enter a string : ")
print("The length of entered string is : ",len(st))

# 1. To Check a certain phrase in a string :

# use keyword 'in'
test = "Hey i am ratinder aka ratan"
print("Hey" in test)                 # prints 'True' if "Hey" is present and 'False' if not

# or use in if statement (To print only if "aka" is present):

if "aka" in test :
    print("Yes, aka is present in test string")

# 2. To check if a certain phrase is NOT present in a string :
    
# Use keyword 'not in' 
test2 = "Hey are you ratinder or ratan"
print("or" not in test2)          # as 'or' is present in string, hence it will print false

# similarly, it can be used in if statements as mentioned in case of Check phrase