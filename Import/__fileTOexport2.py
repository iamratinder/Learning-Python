def welcome():
    print("Hey, you are welcome my friend -- from Ratinder")

if __name__ == "__main__" :
    welcome()

ratinder = "The owner"

# If I  print(__name__) here -> it will give output as __main__
# But if I run another file where it is imported and than the output of same print(__name__) here  would be -> name of the file where it has been imported 

print(__name__)
