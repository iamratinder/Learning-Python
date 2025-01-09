# WAP to detect double spaces in a string , if present than replace it with single space:
a = input("Enter the string : ")
double_spaces = a.find("  ")                            # returns -1 if not found
print("Yes double spaces are present") if double_spaces>0 else print("No double spaces present")

if double_spaces>0:
    print("The string after replacemen is :", a.replace('  ',' '))
