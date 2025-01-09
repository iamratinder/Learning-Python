# The else keyword in a for loop specifies a block of code to be executed when the loop is finished :
# NOTE : The else block wil NOT be executed if the loop is stopped by a 'break' statement
#        Hence if else executes that means loop actually got complete and is not broken 
for x in range(6):
    print(x+1)
else:                             # This else block is actually the part of for loop block     
    print("finally finished!")    

print()
for x in range(6):
    if x == 3: break
    print(x)
else: print("Finally finished")