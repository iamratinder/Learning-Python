'''
Why is it useful ?
This idiom is useful bcz it allows you to reuse code from a script by importing it as a 
module into another script, without running the code in the original script. 

def main ():
    print("Running script directly")
if __name__ = "__main__" :
    main()

If you run this script directly, it will output "Running script directly".
However, if you import it as a module into another script, it will not output anything 
until it's call :

import script    # will not output anything
script.main()    # OUTPUT : "Running script directly"

This can be useful if you have code that you want to reuse in multiple scripts, but you 
only want it to run when the script is run directly and not when it's imported as a module. '''

'''
Is it a necessity ?
It's important to note that the  if __name__ == "__main__"  idiom is not required to run
a python script. You can still run a script without it by simply calling the functions or
running the code you want to execute directly.
However, the  if __name__ == "__main__"  idiom can be a useful tool for organizing and 
seperating code that should be run directly from code that should be imported and used as a module.

IN SUMMARY : the idiom is a common pattern used in Python scripts to determine whether the
script is being run directly or being imported as a module into another script. 
It allows you to reuse code from a script by importing it as a module into another script,
without running the code in the original script.  '''