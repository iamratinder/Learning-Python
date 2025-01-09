# A local variable is a variable that is defined within a function and is only accessible within that function.
# It is created when the function is called and is destroyed when the function returns.

# A Global variable is a variable that is defined outside of a function and is accessible from within any function in your code.
print("─"*70)
x = 4

def hello():
    x = 5
    print(f"The local x is : {x}")
    print("Hello friend")

print(f"The Global x is : {x}")
hello()
print(f"The Global x is : {x}")         ;print("─"*70)

# The global keyword :
# It is used to declare that a vaiable is a global variable and should be accessed from the global scope.
x = 4

def hello():
    global x
    x = 5
    print(f"The local x is : {x}")
    print("Hello friend")

print(f"The Global x is : {x}")
hello()
print(f"The Global x is : {x}")         ;print("─"*70)
