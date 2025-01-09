# Short Hand if : if you have only one statement to execute
a = int(input("Enter value of a1 : "))
b = int(input("Enter value of b1 : "))
if a>b : print("a is greater than b")  # will print nothing if b>a

# Short Hand if..else :  *Ternary Operators OR Conditional Expressions
a = int(input("Enter value of a2 : "))
b = int(input("Enter value of b2 : "))
print("a is greater than b") if a>b else print("b is greater than a")

# You can also have multiple else statements on same line:
a = int(input("Enter value of a3 : "))
b = int(input("Enter value of b3 : "))
print('A') if a>b else print("=") if a==b else print("B")
