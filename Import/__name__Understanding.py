'''
The   If __name__ == " __main__"   idiom is a common pattern used in python scripts to determine whether 
the script is being run directly or being imported as a module into another script.
In python, the __name__ variable is a built-in variable that is automatically set to the name of the current module.
When a python script is run directly, the __name__ variable is set to the string __main__ 
When the script is imported as a module into another script, the __name__ variable is set to the name of the module. '''
# IN Short : import krde hi file vch likhya code execute hona shuru hoju.

import __fileTOexport     # This single import will print  -> Hey, you are welcome my friend -- from Ratinder
__fileTOexport.welcome()  # This would also print the same -> Hey, you are welcome my friend -- from Ratinder
print()

# The solution :
import __fileTOexport2    # for solution check code in this file
__fileTOexport2.welcome()  
