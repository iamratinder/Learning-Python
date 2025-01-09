# WAP which runs only if the input is bw the no. 2000 and 5000 or the word quit
n = (input("Enter a number between 2000 and 5000 or type 'quit' : "))
if not (n.lower() == 'quit' or '2000' < n < '5000' ):
    raise NameError("Invalid String")
else:
    print("Program works !!!")