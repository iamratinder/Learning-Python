# There is no do-while (aka exit-controlled loop) loop in python
# do-while loop is a set of instructions that will execute atleast ONCE

# 1.___Simple raw method -> once write the body outside also of a while loop
a = int(input("Enter a positive number : "))
print(a)
while a>0:
    a = int(input("Enter a positive number : "))
    print(a)
# But this is not convinient ( as for ex: if body have 4000 lines than the code would have become of 8000 lines)
print()

# 2.___Better way :
# here we use an infinite while loop and put our condition in if statement in such a way that the loop breaks when condition of if statement becomes True
while True:
    a = int(input("Enter a negative number : "))
    print(a)
    if not a<0:                # or use -> if a>0
        break
