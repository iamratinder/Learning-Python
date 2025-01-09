try :
    num = int(input("Enter an integer : ")) 
    a = [5, 6]                                    # list with index 0 and 1 only
    print(a[num]) 
except ValueError:
    print("Number entered is not an integer.")    
except IndexError:
    print("Index Error")    

print("Some inportant lines of code")
print("End of Program")