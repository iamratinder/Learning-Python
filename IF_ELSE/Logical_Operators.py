# and 
# finding greater of three numbers :
a, b, c = int(input("Enter 1st number : ")), int(input("Enter 2nd number : ")), int(input("Enter 3rd number : "))
if(a>=b and a>=c):
    print(a,"is greatest")
elif(b>=a and b>=c):
    print(b,"is greatest")
elif(c>=a and c>=b):
    print(c,"is greatest")

# or
a = 200
b = 33
c = 500
if a>b or a>c:
    print("At least one of the conditions is True")

# not
a = 33
b = 200
if not a>b:
    print("a is NOT greater than b")

# pass statement : if statements cannot be empty, 
# but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.
a = 33 
b = 200
if b>a :
    pass