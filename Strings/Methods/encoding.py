# encode() : resposible for returning the encoded form of any given string
# The code points are translated into a series of bytes to efficiently store such strings
# This process is called encoding. 
# Python uses -> 'UTF-8' as its encoding by Default (if no encoding is specified)
# UTF : Unicode Transformation Format.
a = "My name is Ståle"    # å -> special symbol in some other language (latin)
print(a.encode())
# syntax : string.encode(encoding=encoding, errors=errors)
# Some more examples :
print(a.encode(encoding="ascii",errors="backslashreplace"))    # Uses a backslash instead of char that could not be encoded
print(a.encode(encoding="ascii",errors="ignore"))              # ignores the characters that cannot be encoded
print(a.encode(encoding="ascii",errors="namereplace"))         # replaces the character with a text explaining the character
print(a.encode(encoding="ascii",errors="replace"))             # replaces the character with a question mark(?)
print(a.encode(encoding="ascii",errors="xmlcharrefreplace"))   # replaces the character with an xml character
# print(a.encode(encoding="ascii",errors="strict"))              # Default, raises an error on failure

