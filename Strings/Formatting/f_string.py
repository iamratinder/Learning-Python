'''  NOTE -> newly introduced (Python 3.6 onwards)
1. It is a new string formatting mechanism introduced by the PEP 498 (python enhancement proposal).
2. It is also known as "Literal String Interpolation" or more commonly as "F-Strings"
3. The primary focus of this mechanism is to make the interpolation easier.
___When we prefix the string with the letter 'f', the string becomes the f-string itself
___The f-string can be formatted in much same way as the  str.format()  method.
___The f-string offers a convinient way to embed Python expression inside string literals for formatting. '''
print('─'*60)
name = "Ratinder"
age = 18
print(f"My name is {name}, I am {age} years old.")       ; print('─'*60)

# It evaluates at runtime; we can put all valid Python expression in them.
print(f"The product of 2 and 29 is {2*29}")

#__// If you wanna print literally use double {{ }}
print(f"WE USE F-STRINGS LIKE THIS : My name is {{name}}, I am {{age}} years old.")    ; print('─'*60)  