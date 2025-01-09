a = "RatiNDer"    # Strings are immutable (rather a copy is made)
print(a.upper())  # will make a copy of string having all elements in upper case
print(a.lower())  # lower case {Note : NO arguments can be given in these functions}
print(a.casefold()) #same as lower()

b = " Hello Ratinder "
print(b)            # will print as it is
print(b.strip())    # removes any white spaces before and after the string

c = "!!Yayyy!!!!!!"
print(c.rstrip("!")) # removes the trailing characters 

d = "oye ratinder kithe jaa rea"
print(d.replace("ratinder","sonea"))  # replace all occurance of a string with another string

e = "Mai ajj roti ni khani, mood ni hega"
print(e.split(" "))  # splits the given string at the specified instance and returns the seperated strings as list items
print(e.split("r"))  # jithe jithe 'r' aau othe othe string split hoju, te as a list elements strings print hongia

f = "only first characTER of striNG is capitalized, reST are lower cASed"
print(f.capitalize()) 

# Alligns the string to the center as per the parameters given by the user
g = "Allign this"        # length : 11
print(g.center(25))      # will add 14 spaces more (agge 7, pishe 7)to make it move to center (24 spaces)
print(g.center(25,"."))  # we can also provide padding character

h = "ratinder rabri kha ke so gya"
count = h.count("r")  # returns the number of times the given value has occured within the given string
print(count)

i = "Welcome to my place ji !!!"
print(i.endswith("!!!"))  # cheks if the string ends with a given value (true) or not(false)
# we can even chek for a value in-between the string by providing start and end index positions
print(i.endswith("to",3,10))  # after slicing string is : come to

# searches for the first occurance of given value and returns the index where it is present
j = "name is John, he is an honest man."
print(j.find("is"))  # prints the address of first 'i' found of first 'is'
######** IF given value is not found than return -1

print(j.index("is"))  # same as find() ***JUST raise exception(error) if value not found in string

k = "WelcomeTo303Room"   # is Alpha Numeric 
print(k.isalnum())  # returns true only if the entire string only consists of A-Z, a-z, 0-9

l = "WelcomeToRoom" # is Alpha
print(l.isalpha())  # returns true only if string only contains A-Z, a-z

m = "Oye hoye"
print(m.islower())  # returns true if all characters are in lower case

n = "ya ya man! \n" # \n is a non-printable character
print(n.isprintable())  # returns true if all the values within string are printable

o = "This_sentence_do_not_contain_any_white_space"
print(o.isspace())  # returns true only and only if the string contains white spaces (either created by space bar or Tab)

p = "The First Letter Of Each Word Is Capital"
print(p.istitle()) # returns true only if first letter of each word of the string is capitalized

q = "RETURNS TRUE IF ALL CHARACTERS IN STRING ARE IN UPPER CASE"
print(q.isupper())

r = "Yes, this sentence starts with Yes"
print(r.startswith("Yes"))  

s = "upper -> LOWER"
print(s.swapcase())  # converts upper to lower and lower to upper case

t = "capitalizes eAch leTTEr of the Word withiN the STring"
print(t.title())

