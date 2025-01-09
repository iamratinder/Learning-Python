# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end                      ex :
#   now append three random characters at the starting and the end                                                      gutter  -> word
# else:                                                                                                         lst utterg iou  -> code word
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode


import string
import random     # define random module
s = 6             # no. of characters in the string
ran = "".join(random.choices(string.ascii_lowercase + string.digits, k = s))

a = input("Enter whether to code or decode a message: ")
if a.lower() == 'code':
    msg = input("Enter the message : ")                                        # hey ratan :
    list = msg.split(" ")                                                      # list = ['hey', 'ratan']
    for word in list :                                                         
        if(len(word)>3):                                                       # ratan :
            encrypted_msg = ran[:3] + word[1:] + word[0] + ran[3:6]            # (3 random char) + atan + r + (3 randoom char)
            print(encrypted_msg, end= ' ')
        else:                                                                  # hey :
            encrypted_msg = word[::-1]                                         # yeh
            print(encrypted_msg, end = ' ')

elif a.lower() == 'decode':
    msg = input("Enter the message : ")    
    list = msg.split(" ")                  
    for word in list : 
        if(len(word)>3):
            decrypted_msg = word[-4:-3] + word[3:-4] 
            print(decrypted_msg, end= ' ')
        else:
            decrypted_msg = word[::-1]
            print(decrypted_msg, end = ' ')

        
        
        
        
        
        
        
    