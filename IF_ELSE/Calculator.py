# Remember instead of '{}' we use "indentations"(whitespaces at beginning of a line) to define scope in the code
x = float(input("Enter the first number : "))
y = input("Enter the operator : ")
z = float(input("Enter the second number : "))
if(y=='+'):
    print("The sum of numbers is : ", x+z)   # give indentations
elif(y=='-'):print("The diffrence of numbers is : ", x-z)  # or can do like this
elif(y=='/'):
    print("The division of numbers is : ", x/z)
elif(y=='*'):
    print("The multiplication of numbers is : ", x*z)
else:
    print("OPERATOR INVALID")
