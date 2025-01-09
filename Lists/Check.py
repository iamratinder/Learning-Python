# We can check if a given item is present in list using 'in' keyword :
random = ["oye",  3,    9,   True,  6.7]
if "oye" in random:
    print("Yes")
else:
    print("No")

if "3" or "9" in random:  # here it's actually -> if ("3") or ("9" in random):   hence always true
    print("Yes")
else: 
    print("No")

if ("3" or "9") in random: 
    print("Yes")
else: 
    print("No")

# Similar can be done in case of strings as well :
if "inder" in "ratinder":
    print("Yes")
else:
    print("No")


