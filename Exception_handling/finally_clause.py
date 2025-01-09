'''
The finally code block is also a part of exception handling. When we handle exception using the try and except block,
we can include a finally block at the end.
The finally block is always executed ☑️, so it is generally used for doing the concluding tasks like 
closing file resources or closing database connection or may be ending the program execution with a delightful message. '''
# Syntax : 
'''
try :
    # statements which could generate exception
except:
    # Solution of generated exception              
finally:
    # block of which is going yo execute in any situation        '''
# NOTE : One of the important use cases of finally block is in a function which returns a value.

# def func(): 
#     try :
#         list = [1, 5, 6, 7]
#         i = int(input("Enter the index : "))
#         print(list[i])
#     except :
#         print("Some error occurred")
#     finally :
#         print("I am always executed") 
#     print("I will be executed here bcz this function is not returning anything")

# func()

def fun2(): 
    try :
        list = [1, 5, 6, 7]
        i = int(input("Enter the index : "))
        print(list[i])
        return 1
    except :
        print("Some error occurred")
        return 
    finally :
        print("I am always executed") 
    print("I will not be executed here bcz this function is returning values in try and except")

a = fun2()
print(a)