# Exception handling is the process of responding to unwanted or unexpected events when a computer program runs.
# Exception handling deals with these events to avoid the program or system crashing, and without this process, exceptions would disrupt the normal operation of a program.
'''
Exceptions in Python : Python has many built-in exceptions that are raised when your program encounters an error (soomething in program goes wrong).
-> When these exceptions occur, the Python interpreter stops the current process and passes it to the calling process until it is handled.
-> If not handled, the program will crash. '''
# Python try...except :-
# 1. try..except blocks are used in Python to handle errors and exceptions.
# 2. The code in try block runs when there is no error.
# 3. If the try block catches the error, then the except block is executed.

'''                             Syntax :
try :
    # statements which could generate exception
except:
    # Solution of generated exception              '''

# eg. 1
n = input("Enter a number : ")
print(f"The multiplication table of {n} is : ")
try :
    for i in range(1,11):
        print(f"{int(n)} X {i} = {int(n) * i}")
except Exception as e :
    print(e)                     # e is the error here (which i have printed) by default

print("Some inportant lines of code")
print("End of Program")                       ; print('─'*60)

# eg. 2
n = input("Enter a number for eg. 2 : ")
print(f"The multiplication table of {n} is : ")
try :
    for i in range(1,11):
        print(f"{int(n)} X {i} = {int(n) * i}")
except :
    print("Invalid input !!!")                 

print("Some inportant lines of code")
print("End of Program")